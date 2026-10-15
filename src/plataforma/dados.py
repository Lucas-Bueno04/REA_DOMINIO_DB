"""Núcleo da plataforma de progresso do mapeamento (REA_DOMINIO_DB).

Responsabilidades
  * status DERIVADO de cada tabela e coluna (a partir do catálogo, dos modelos YAML e da segurança) + marcações MANUAIS (data/progresso.db);
  * resumo/progresso, famílias, fila de trabalho priorizada, histórico e série temporal;
  * rascunho de entidade (YAML) gerado a partir da estrutura da tabela, com validação, teste no banco (só agregados) e promoção ao modelo.
Nada aqui escreve no banco Domínio. Escreve apenas em data/progresso.db, data/rascunhos/ e (na promoção) em src/model/modulos/.
"""
from __future__ import annotations

import collections
import datetime
import json
import math
import pathlib
import re
import sqlite3
import sys
import threading
import time
import unicodedata

import yaml

RAIZ = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "src"))
CATALOGO = RAIZ / "data" / "catalog" / "dominio_catalog.db"
ESTADO = RAIZ / "data" / "progresso.db"
MODULOS = RAIZ / "src" / "model" / "modulos"
RASCUNHOS = RAIZ / "data" / "rascunhos"

# status derivados (em ordem de precedência) e rótulos
STATUS = ["bloqueada", "validada", "modelada", "apoio", "ignorada", "em_analise", "vazia", "nao_iniciada"]
ROTULO = {"bloqueada": "Bloqueada (credenciais)", "validada": "Validada", "modelada": "Modelada (entidade)", "apoio": "Apoio (vínculo)",
          "ignorada": "Ignorada (baixo valor)", "em_analise": "Em análise", "vazia": "Vazia hoje", "nao_iniciada": "Não iniciada"}
MODULO_POR_DEP = {"Fiscal": "fiscal", "Pessoal": "folha", "Contábil": "contabil", "Geral": "geral", "Financeiro do escritório": "honorarios"}
STATUS_MANUAIS_TABELA = {"em_analise", "ignorada", "nenhum"}
STATUS_MANUAIS_COLUNA = {"mapeada", "ignorada", "duvida", "nenhum"}


def agora() -> str:
    return datetime.datetime.now().isoformat(timespec="seconds")


# ======================================================================================= persistência do estado
def estado_db() -> sqlite3.Connection:
    ESTADO.parent.mkdir(exist_ok=True)
    c = sqlite3.connect(ESTADO)
    c.row_factory = sqlite3.Row
    c.executescript("""
        create table if not exists estado_tabela(tabela text primary key, status text, prioridade integer default 0, nota text, atualizado text);
        create table if not exists estado_coluna(tabela text, coluna text, status text, nota text, atualizado text, primary key(tabela, coluna));
        create table if not exists historico(id integer primary key autoincrement, ts text, tipo text, tabela text, detalhe text);
        create table if not exists snapshots(dia text primary key, json text);
        create table if not exists rascunhos(tabela text primary key, modulo text, entidade text, yaml text, validado integer default 0,
                                             testado integer default 0, atualizado text);
    """)
    return c


def registrar(c: sqlite3.Connection, tipo: str, tabela: str | None, detalhe: str) -> None:
    c.execute("insert into historico(ts, tipo, tabela, detalhe) values(?,?,?,?)", (agora(), tipo, tabela, detalhe))


# ======================================================================================= base derivada (com cache)
class Base:
    """Fotografia derivada do catálogo + modelos + segurança. Reconstruída quando algo muda no disco."""
    _cache = None
    _chave = None

    _trava = threading.Lock()

    @classmethod
    def obter(cls) -> "Base":
        chave = (CATALOGO.stat().st_mtime, tuple(sorted((p.name, p.stat().st_mtime) for p in MODULOS.glob("*.yaml"))),
                 (RAIZ / "config" / "seguranca.yaml").stat().st_mtime)
        with cls._trava:
            if cls._cache is None or cls._chave != chave:
                cls._cache, cls._chave = cls(), chave
            return cls._cache

    def __init__(self):
        cat = sqlite3.connect(f"file:{CATALOGO.as_posix()}?mode=ro", uri=True, check_same_thread=False)
        cat.row_factory = sqlite3.Row
        self.cat = cat
        seg = yaml.safe_load((RAIZ / "config" / "seguranca.yaml").read_text(encoding="utf-8"))
        self.bloqueadas = {t.lower() for t in seg["tabelas_bloqueadas"]}
        self.re_cred = re.compile(seg["colunas_credencial_regex"])
        # ---- modelos YAML: quem usa cada tabela e quais colunas ficam expostas
        self.entidades, self.dominios = {}, {}
        self.raiz = collections.defaultdict(list)      # tabela -> [entidades-raiz]
        self.apoio = collections.defaultdict(list)     # tabela -> [entidades que a usam como vínculo]
        self.expostas = collections.defaultdict(lambda: collections.defaultdict(set))   # tabela -> coluna -> {entidades}
        self.validada = set()                          # tabelas-raiz de entidades com regras validadas (campo `regras`)
        for arq in sorted(MODULOS.glob("*.yaml")):
            y = yaml.safe_load(arq.read_text(encoding="utf-8"))
            self.dominios.update(y.get("dominios", {}))
            for n, e in y["entidades"].items():
                self.entidades[n] = {**e, "_modulo": y["modulo"], "_arquivo": arq.name}
                t = e["tabela"].lower()
                self.raiz[t].append(n)
                if e.get("regras"):
                    self.validada.add(t)
                for v in e["colunas"].values():
                    self.expostas[t][(v["coluna"] if isinstance(v, dict) else v).lower()].add(n)
                for f in e.get("filtros", {}).values():
                    for c in (f["coluna"] if isinstance(f["coluna"], list) else [f["coluna"]]):
                        self.expostas[t][c.lower()].add(n)
                for k in e["chave"]:
                    self.expostas[t][k.lower()].add(n)
                for vn, v in e.get("vinculos", {}).items():
                    vt = v["tabela"].lower()
                    self.apoio[vt].append(n)
                    for c in v["colunas"].values():
                        self.expostas[vt][c.lower()].add(n)
                    for c in v["liga"].values():
                        self.expostas[vt][c.lower()].add(n)
                    for c in v["liga"].keys():
                        self.expostas[t][c.lower()].add(n)
        # ---- tabelas
        self.tabelas = {}
        progs = collections.Counter()
        for r in cat.execute("select lower(tabela) t, count(distinct arquivo) n from uso_tabela_arquivo group by 1"):
            progs[r["t"]] = r["n"]
        nrel = collections.Counter()
        for r in cat.execute("select lower(filha) f, lower(pai) p from relacoes where tipo<>'temporaria' and confianca>=0.8"):
            nrel[r["f"]] += 1; nrel[r["p"]] += 1
        ncols = collections.Counter(); sem_uso = collections.Counter(); cred = collections.Counter()
        for r in cat.execute("select lower(tabela) t, nome, comentario from colunas"):
            ncols[r["t"]] += 1
            if r["comentario"] and "SEM USO" in r["comentario"].upper():
                sem_uso[r["t"]] += 1
            if self.re_cred.search(r["nome"]):
                cred[r["t"]] += 1
        for r in cat.execute("select * from tabelas where tipo='BASE'"):
            t = r["nome_lower"]
            no_escopo = bool(r["legivel"] and r["na_lista_gerador"])
            fam_sub = r["subcluster"]
            self.tabelas[t] = {
                "nome": r["nome"], "t": t, "dep": r["departamento"], "pref": r["prefixo"], "fam": f"{r['prefixo']} · {'núcleo' if fam_sub == 'NUCLEO' else fam_sub.lower()}",
                "linhas": r["linhas"] or 0, "desc": r["comentario"], "escopo": no_escopo, "colunas": ncols[t], "sem_uso": sem_uso[t], "cred": cred[t],
                "programas": progs[t], "relacoes": nrel[t]}
        self._agregar_exposicao()

    def _agregar_exposicao(self):
        for t, d in self.tabelas.items():
            d["expostas"] = len(self.expostas.get(t, {}))
            d["entidades"] = self.raiz.get(t, [])
            d["usada_em"] = sorted(set(self.apoio.get(t, [])))

    # ---- status derivado (sem manual)
    def status_auto(self, d: dict) -> str:
        t = d["t"]
        if t in self.bloqueadas:
            return "bloqueada"
        if t in self.raiz:
            return "validada" if t in self.validada else "modelada"
        if t in self.apoio:
            return "apoio"
        if d["linhas"] == 0:
            return "vazia"
        return "nao_iniciada"


# ======================================================================================= estado final de cada tabela
def _manual(c: sqlite3.Connection) -> dict:
    return {r["tabela"]: dict(r) for r in c.execute("select * from estado_tabela")}


def lista_tabelas(incluir_fora_do_escopo: bool = False) -> list[dict]:
    b, c = Base.obter(), estado_db()
    try:
        man = _manual(c)
    finally:
        c.close()
    out = []
    for t, d in b.tabelas.items():
        if not d["escopo"] and not incluir_fora_do_escopo:
            continue
        auto = b.status_auto(d)
        m = man.get(t, {})
        st = auto
        if auto in ("nao_iniciada", "vazia") and m.get("status") in ("em_analise", "ignorada"):
            st = m["status"]
        out.append({"t": t, "nome": d["nome"], "dep": d["dep"], "fam": d["fam"], "linhas": d["linhas"], "status": st, "auto": auto,
                    "prioridade": m.get("prioridade", 0), "colunas": d["colunas"], "expostas": d["expostas"], "programas": d["programas"],
                    "nota": bool(m.get("nota"))})
    return out


def resumo() -> dict:
    ts = lista_tabelas()
    b = Base.obter()
    por = collections.Counter(x["status"] for x in ts)
    linhas = collections.Counter();
    for x in ts:
        linhas[x["status"]] += x["linhas"]
    total_l = sum(linhas.values())
    modeladas = ("validada", "modelada", "apoio")
    # relevantes: o que realmente vale mapear (não vazia, não ignorada, não bloqueada)
    relevantes = [x for x in ts if x["status"] not in ("vazia", "ignorada", "bloqueada")]
    rel_modeladas = [x for x in relevantes if x["status"] in modeladas]
    grandes = [x for x in relevantes if x["linhas"] >= 1000]          # a meta realista: tabelas com 1.000 linhas ou mais
    grandes_mod = [x for x in grandes if x["status"] in modeladas]
    cols_total = sum(x["colunas"] for x in ts)
    cols_exp = sum(x["expostas"] for x in ts if x["status"] in modeladas)
    cols_utes = sum(d["colunas"] - d["sem_uso"] - d["cred"] for d in b.tabelas.values() if d["escopo"])
    deps = collections.defaultdict(lambda: collections.Counter())
    for x in ts:
        deps[x["dep"]][x["status"]] += 1
    fora = collections.Counter()
    for t, d in b.tabelas.items():
        if not d["escopo"]:
            fora["base_interna"] += 1
    cat = b.cat
    fora["temporarias"] = cat.execute("select count(*) from tabelas where tipo='GBL TEMP'").fetchone()[0]
    fora["views"] = cat.execute("select count(*) from tabelas where tipo='VIEW'").fetchone()[0]
    r = {
        "gerado_em": agora(), "tabelas": len(ts), "por_status": dict(por), "linhas_por_status": dict(linhas), "linhas_total": total_l,
        "tabelas_modeladas": sum(por[s] for s in modeladas), "linhas_modeladas": sum(linhas[s] for s in modeladas),
        "relevantes": len(relevantes), "relevantes_modeladas": len(rel_modeladas), "grandes": len(grandes), "grandes_modeladas": len(grandes_mod),
        "colunas_total": cols_total, "colunas_uteis_total": cols_utes, "colunas_expostas": cols_exp,
        "entidades": len(b.entidades), "entidades_validadas": sum(1 for e in b.entidades.values() if e.get("regras")),
        "dominios": len(b.dominios), "dominios_confirmados": sum(1 for d in b.dominios.values() if d.get("confirmado") is True),
        "por_departamento": {k: dict(v) for k, v in deps.items()}, "fora_do_escopo": dict(fora), "rotulos": ROTULO, "ordem_status": STATUS,
    }
    return r


def familias() -> list[dict]:
    ts = lista_tabelas()
    fam = collections.defaultdict(lambda: {"dep": None, "n": 0, "mod": 0, "vazias": 0, "linhas": 0, "linhas_mod": 0, "em_analise": 0, "relevantes": 0})
    for x in ts:
        f = fam[x["fam"]]; f["dep"] = x["dep"]; f["n"] += 1; f["linhas"] += x["linhas"]
        if x["status"] in ("validada", "modelada", "apoio"):
            f["mod"] += 1; f["linhas_mod"] += x["linhas"]
        if x["status"] == "vazia":
            f["vazias"] += 1
        if x["status"] == "em_analise":
            f["em_analise"] += 1
        if x["status"] in ("nao_iniciada", "em_analise", "validada", "modelada", "apoio"):
            f["relevantes"] += 1
    return sorted(({"familia": k, **v} for k, v in fam.items()), key=lambda f: -f["linhas"])


def fila(limite: int = 40, departamento: str | None = None) -> list[dict]:
    """Próximas tabelas a mapear, por valor estimado: volume de dados, uso pelos programas da Domínio e conectividade."""
    b = Base.obter()
    out = []
    for x in lista_tabelas():
        if x["status"] not in ("nao_iniciada", "em_analise") or (departamento and x["dep"] != departamento):
            continue
        d = b.tabelas[x["t"]]
        vol = math.log10(x["linhas"] + 1)
        score = 2.0 * vol + min(d["programas"], 60) / 6 + min(d["relacoes"], 40) / 8
        if x["linhas"] < 1000:
            score -= 2.5
        if x["prioridade"]:
            score += 10
        if x["status"] == "em_analise":
            score += 1.5
        pk = [r["nome"] for r in b.cat.execute("select nome from colunas where tabela=? collate nocase and pk=1 order by ordem", (d["nome"],))][:3]
        out.append({**x, "score": round(score, 2), "desc": d["desc"], "pk": pk,
                    "motivo": f"{x['linhas']:,} linhas · usada por {d['programas']} programas · {d['relacoes']} relações".replace(",", ".")})
    out.sort(key=lambda r: -r["score"])
    return out[:limite]


def historico(limite: int = 80) -> list[dict]:
    c = estado_db()
    try:
        return [dict(r) for r in c.execute("select ts, tipo, tabela, detalhe from historico order by id desc limit ?", (limite,))]
    finally:
        c.close()


def snapshot_hoje(forcar: bool = False) -> dict:
    r = resumo()
    snap = {"dia": datetime.date.today().isoformat(), "tabelas_modeladas": r["tabelas_modeladas"], "linhas_modeladas": r["linhas_modeladas"],
            "entidades": r["entidades"], "colunas_expostas": r["colunas_expostas"], "validadas": r["por_status"].get("validada", 0),
            "em_analise": r["por_status"].get("em_analise", 0), "relevantes_modeladas": r["relevantes_modeladas"]}
    c = estado_db()
    try:
        c.execute("insert or replace into snapshots(dia, json) values(?,?)", (snap["dia"], json.dumps(snap)))
        c.commit()
        return snap
    finally:
        c.close()


def serie() -> list[dict]:
    c = estado_db()
    try:
        return [json.loads(r["json"]) for r in c.execute("select json from snapshots order by dia")]
    finally:
        c.close()


# ======================================================================================= detalhe da tabela
def detalhe(tabela: str) -> dict:
    b = Base.obter()
    t = (tabela or "").lower()
    d = b.tabelas.get(t)
    if not d:
        raise KeyError(f"tabela '{tabela}' não existe")
    cat = b.cat
    c = estado_db()
    try:
        man = c.execute("select * from estado_tabela where tabela=?", (t,)).fetchone()
        mcols = {r["coluna"]: dict(r) for r in c.execute("select * from estado_coluna where tabela=?", (t,))}
        rasc = c.execute("select entidade, modulo, validado, testado, atualizado from rascunhos where tabela=?", (t,)).fetchone()
    finally:
        c.close()
    perfil = {r["coluna"]: r for r in cat.execute("select * from perfil_colunas where tabela=?", (t,))}
    cols = []
    for r in cat.execute("select * from colunas where tabela=? collate nocase order by ordem", (d["nome"],)):
        cn = r["nome"].lower()
        com = r["comentario"] or ""
        p = perfil.get(cn)
        util = None
        if p and p["linhas"]:
            util = round(100 * ((p["nao_nulos"] or 0) - (p["em_branco"] or 0) - (p["sentinela"] or 0) - (0 if r["pk"] else (p["zeros"] or 0))) / p["linhas"], 1)
        if b.re_cred.search(r["nome"]):
            auto = "credencial"
        elif "SEM USO" in com.upper():
            auto = "sem_uso"
        elif cn in b.expostas.get(t, {}):
            auto = "exposta"
        elif util is not None and util < 1:
            auto = "vazia"
        else:
            auto = "pendente"
        m = mcols.get(cn, {})
        cols.append({"nome": r["nome"], "tipo": r["tipo"], "tamanho": r["tamanho"], "pk": bool(r["pk"]), "nulo": bool(r["aceita_nulo"]), "comentario": com,
                     "auto": auto, "manual": m.get("status"), "nota": m.get("nota"), "util": util, "entidades": sorted(b.expostas.get(t, {}).get(cn, []))})
    rels = []
    for r in cat.execute("""select id, filha, pai, tipo, origens, confianca, ocorrencias from relacoes where (lower(filha)=? or lower(pai)=?) and tipo<>'temporaria'
                            order by confianca desc, ocorrencias desc limit 60""", (t, t)):
        cs = [[x["col_filha"], x["col_pai"]] for x in cat.execute("select col_filha, col_pai from relacao_colunas where relacao_id=?", (r["id"],))]
        pai = r["pai"].lower() == t
        rels.append({"papel": "pai de" if pai else "filha de", "tabela": r["filha"] if pai else r["pai"], "tipo": r["tipo"], "origens": r["origens"], "confianca": r["confianca"], "colunas": cs})
    idx = [dict(r) for r in cat.execute("select indice, colunas, unico from indices where lower(tabela)=? order by unico desc", (t,))]
    auto = b.status_auto(d)
    st = auto if not man or auto not in ("nao_iniciada", "vazia") else (man["status"] if man["status"] in ("em_analise", "ignorada") else auto)
    return {"t": t, "nome": d["nome"], "desc": d["desc"], "dep": d["dep"], "fam": d["fam"], "linhas": d["linhas"], "escopo": d["escopo"], "bloqueada": t in b.bloqueadas,
            "status": st, "auto": auto, "prioridade": (man["prioridade"] if man else 0), "nota": (man["nota"] if man else ""), "programas": d["programas"],
            "colunas": cols, "relacoes": rels, "indices": idx, "entidades": d["entidades"], "usada_em": d["usada_em"],
            "rascunho": dict(rasc) if rasc else None, "modulo_sugerido": MODULO_POR_DEP.get(d["dep"], "outros")}


# ======================================================================================= edição do estado manual
def definir_tabela(tabela: str, status: str | None = None, prioridade: int | None = None, nota: str | None = None) -> dict:
    t = tabela.lower()
    if t not in Base.obter().tabelas:
        raise KeyError(tabela)
    if status is not None and status not in STATUS_MANUAIS_TABELA:
        raise ValueError(f"status manual inválido: {status}")
    c = estado_db()
    try:
        ant = c.execute("select * from estado_tabela where tabela=?", (t,)).fetchone()
        novo = {"status": (ant["status"] if ant else None), "prioridade": (ant["prioridade"] if ant else 0), "nota": (ant["nota"] if ant else "")}
        if status is not None:
            novo["status"] = None if status == "nenhum" else status
        if prioridade is not None:
            novo["prioridade"] = 1 if prioridade else 0
        if nota is not None:
            novo["nota"] = nota[:4000]
        c.execute("insert or replace into estado_tabela(tabela, status, prioridade, nota, atualizado) values(?,?,?,?,?)",
                  (t, novo["status"], novo["prioridade"], novo["nota"], agora()))
        if status is not None and (not ant or ant["status"] != novo["status"]):
            registrar(c, "status", t, f"{(ant['status'] if ant else None) or 'automático'} → {novo['status'] or 'automático'}")
        if prioridade is not None and (not ant or ant["prioridade"] != novo["prioridade"]):
            registrar(c, "prioridade", t, "priorizada" if novo["prioridade"] else "prioridade removida")
        if nota is not None and (not ant or (ant["nota"] or "") != novo["nota"]):
            registrar(c, "nota", t, "nota atualizada")
        c.commit()
    finally:
        c.close()
    return detalhe(t)


def definir_coluna(tabela: str, coluna: str, status: str | None = None, nota: str | None = None) -> dict:
    t, cn = tabela.lower(), coluna.lower()
    b = Base.obter()
    if t not in b.tabelas or not b.cat.execute("select 1 from colunas where tabela=? collate nocase and nome=? collate nocase", (b.tabelas[t]["nome"], coluna)).fetchone():
        raise KeyError(f"{tabela}.{coluna}")
    if status is not None and status not in STATUS_MANUAIS_COLUNA:
        raise ValueError(f"status manual de coluna inválido: {status}")
    c = estado_db()
    try:
        ant = c.execute("select * from estado_coluna where tabela=? and coluna=?", (t, cn)).fetchone()
        st = (None if status == "nenhum" else status) if status is not None else (ant["status"] if ant else None)
        nt = (nota[:2000] if nota is not None else (ant["nota"] if ant else ""))
        c.execute("insert or replace into estado_coluna(tabela, coluna, status, nota, atualizado) values(?,?,?,?,?)", (t, cn, st, nt, agora()))
        if status is not None and (not ant or ant["status"] != st):
            registrar(c, "coluna", t, f"{coluna}: {(ant['status'] if ant else None) or 'pendente'} → {st or 'pendente'}")
        c.commit()
    finally:
        c.close()
    return {"ok": True}


# ======================================================================================= rascunho de entidade
def _slug(txt: str, maximo: int = 40) -> str:
    s = unicodedata.normalize("NFKD", txt or "").encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    if not s or s[0].isdigit():
        s = "c_" + s
    return s[:maximo].rstrip("_")


def dominio_do_comentario(com: str) -> dict | None:
    """Extrai códigos de comentários como 'Tipo (A=Analitico/S=Sintetico)' ou 'Situacao (A - Ativa/ I - Inativa)'."""
    for seg in re.findall(r"\(([^()]*)\)", com or ""):
        pares = []
        for parte in seg.split("/"):
            m = re.match(r"^\s*([A-Za-z0-9]{1,4})\s*(?:=|-)\s*(\S.*?)\s*$", parte)
            if m:
                pares.append((m.group(1), m.group(2)))
        if len(pares) >= 2 and len(pares) >= 0.7 * len([p for p in seg.split("/") if p.strip()]):
            return dict(pares)
    return None


def _yq(v) -> str:
    return json.dumps(v, ensure_ascii=False)       # JSON é YAML válido (texto entre aspas duplas)


def gerar_rascunho(tabela: str, modulo: str | None = None, nome: str | None = None, colunas: list[str] | None = None, maximo: int = 40) -> dict:
    b = Base.obter()
    t = tabela.lower()
    d = b.tabelas.get(t)
    if not d or not d["escopo"] or t in b.bloqueadas:
        raise ValueError("tabela fora do escopo ou bloqueada")
    cat = b.cat
    cols = [dict(r) for r in cat.execute("select * from colunas where tabela=? collate nocase order by ordem", (d["nome"],))]
    por = {c["nome"].lower(): c for c in cols}
    pk = [c["nome"] for c in cols if c["pk"]]
    if not pk:
        ind = cat.execute("select colunas from indices where lower(tabela)=? and unico=1 order by length(colunas) limit 1", (t,)).fetchone()
        pk = ind["colunas"].split(",") if ind else [cols[0]["nome"]]
    modulo = modulo or MODULO_POR_DEP.get(d["dep"], "outros")
    nome = _slug(nome or d["desc"] or d["nome"], 38)
    if nome in b.entidades:
        nome = _slug(f"{nome}_{t}", 38)
    # --- colunas escolhidas
    if colunas:
        esc = [por[x.lower()] for x in colunas if x.lower() in por and not b.re_cred.search(x)]
    else:
        pri = [por[k.lower()] for k in pk if k.lower() in por]
        resto = [c for c in cols if c["nome"].lower() not in {p["nome"].lower() for p in pri}
                 and not b.re_cred.search(c["nome"]) and "SEM USO" not in (c["comentario"] or "").upper()]
        esc = (pri + resto)[:maximo]
    usados, campos = set(), {}
    for c in esc:
        base = _slug(c["comentario"]) if c["comentario"] and len(_slug(c["comentario"])) >= 3 else _slug(c["nome"])
        api, i = base, 2
        while api in usados:
            api, i = f"{base}_{i}", i + 1
        usados.add(api); campos[c["nome"]] = api
    # --- domínios extraídos dos comentários
    doms, lin_col = {}, []
    for c in esc:
        api = campos[c["nome"]]
        dm = dominio_do_comentario(c["comentario"]) if c["tipo"] in ("char", "tinyint", "smallint", "integer", "varchar") else None
        dn = None
        if dm:
            dn = f"{_slug(nome)}_{api}"[:50]
            doms[dn] = dm
        lin_col.append((c, api, dn))
    # --- empresa, período, volume
    emp = next((c["nome"] for c in cols if c["nome"].lower() == "codi_emp"), None)
    datas = [c for c in esc if c["tipo"] == "date"]
    def pontua(c):
        n = c["nome"].lower()
        return (3 if n.startswith(("data_", "dat", "d")) and "data" in n else 0) + (2 if "data" in n else 0) + (1 if c["nome"] not in pk else 0)
    periodo = max(datas, key=pontua)["nome"] if datas else None
    linhas = d["linhas"]
    volume = "pequeno" if linhas < 10_000 else "medio" if linhas < 1_000_000 else "grande"
    # --- vínculos sugeridos: FK declarada (conf. 1,0) cujo pai tem a PK inteira coberta e uma coluna de nome
    vinc, vis = [], set()
    for r in cat.execute("select id, lower(pai) p, pai from relacoes where lower(filha)=? and confianca>=1.0 and tipo='fk'", (t,)):
        if r["p"] == t or r["p"] in vis or r["p"] not in b.tabelas:
            continue
        pcols = [dict(x) for x in cat.execute("select * from colunas where tabela=? collate nocase order by ordem", (r["pai"],))]
        ppk = [x["nome"].lower() for x in pcols if x["pk"]]
        rc = [(x["col_filha"], x["col_pai"]) for x in cat.execute("select col_filha, col_pai from relacao_colunas where relacao_id=?", (r["id"],))]
        if not ppk or {cp.lower() for _, cp in rc} != set(ppk):
            continue
        if not all(cf.lower() in por for cf, _ in rc):
            continue
        nomec = next((x for x in pcols if x["tipo"] in ("char", "varchar") and not x["pk"] and re.search(r"nome|descri|razao", x["nome"] + " " + (x["comentario"] or ""), re.I)), None)
        if not nomec:
            continue
        vis.add(r["p"])
        vn = _slug(r["pai"], 24)
        vinc.append((vn, r["pai"], rc, nomec["nome"], f"{vn}_nome"))
        if len(vinc) >= 6:
            break
    # --- filtros
    filtros, fvis = [], set()
    def add_filtro(c, ops):
        api = campos[c["nome"]]
        if api not in fvis and len(filtros) < 14:
            fvis.add(api); filtros.append((api, c["nome"], ops))
    for c in esc:
        if c["nome"] in pk and c["nome"].lower() != "codi_emp":
            add_filtro(c, ["eq", "in"])
    for c in esc:
        if c["tipo"] == "date":
            add_filtro(c, ["entre", "gte", "lte"])
    for c in esc:
        if c["tipo"] in ("char", "varchar") and (c["tamanho"] or 0) <= 20 and c["nome"].lower() != "codi_emp":
            add_filtro(c, ["eq", "in"])
        elif c["tipo"] in ("char", "varchar") and (c["tamanho"] or 0) > 20:
            add_filtro(c, ["contem", "prefixo"])
        elif c["tipo"] in ("integer", "smallint", "tinyint") and re.search(r"codi_|^i_|tipo|situ|cod", c["nome"], re.I) and c["nome"].lower() != "codi_emp":
            add_filtro(c, ["eq", "in"])
    # --- texto YAML
    L = [f"# RASCUNHO gerado em {agora()} pela plataforma de progresso a partir de {d['nome']} ({d['dep']}, {linhas:,} linhas).".replace(",", "."),
         "# Gerado automaticamente a partir da ESTRUTURA do banco: revise nomes, domínios, filtros e escreva as regras SOMENTE depois de conferir com dados.",
         "# Domínios extraídos de comentários vêm marcados 'confirmado: parcial': o comentário do banco nem sempre corresponde aos dados (já vimos casos).",
         f"modulo: {modulo}", f"titulo: {_yq(modulo.capitalize())}"]
    if doms:
        L.append("dominios:")
        for dn, dm in doms.items():
            L += [f"  {dn}:", "    confirmado: parcial", "    nota: \"Extraído do comentário da coluna; não confirmado contra os dados.\"",
                  "    valores: {" + ", ".join(f"{_yq(k)}: {_yq(v)}" for k, v in dm.items()) + "}"]
    L += ["entidades:", f"  {nome}:", f"    titulo: {_yq(d['desc'] or d['nome'])}", f"    descricao: {_yq((d['desc'] or d['nome']) + '. (descrição a completar)')}",
          f"    tabela: {d['nome']}", f"    chave: [{', '.join(pk)}]", "    acesso:"]
    L.append(f"      empresa: {emp}" if emp else "      empresa: null")
    if periodo:
        L.append(f"      periodo: {periodo}")
    if volume == "grande":     # tabela grande: exige filtrar por uma coluna da chave ou por período
        chave_f = next((a for a, cn, _ in filtros if cn in pk and cn.lower() != "codi_emp"), None) or ("periodo" if periodo else None)
        if chave_f:
            L.append(f"      exige_algum: [{chave_f}]")
    L.append(f"      volume: {volume}")
    ordem = ([f"[{periodo}, desc]"] if periodo else []) + [f"[{k}, asc]" for k in pk if k.lower() not in ("codi_emp", (periodo or "").lower())][:2]
    L.append("    ordem: [" + ", ".join(ordem) + "]")
    L.append("    colunas:")
    for c, api, dn in lin_col:
        L.append(f"      {api}: {{coluna: {c['nome']}, dominio: {dn}}}" if dn else f"      {api}: {c['nome']}")
    if vinc:
        L.append("    vinculos:")
        for vn, tab, rc, nc, api in vinc:
            L += [f"      {vn}:", f"        tabela: {tab}", "        liga: {" + ", ".join(f"{cf}: {cp}" for cf, cp in rc) + "}", f"        colunas: {{{api}: {nc}}}"]
    if filtros:
        L.append("    filtros:")
        for api, cn, ops in filtros:
            L.append(f"      {api}: {{coluna: {cn}, ops: [{', '.join(ops)}]}}")
    L.append("    regras: []   # preencha só com regras VALIDADAS contra dados reais (cite a evidência)")
    return {"tabela": d["nome"], "entidade": nome, "modulo": modulo, "yaml": "\n".join(L) + "\n", "colunas_escolhidas": len(esc), "colunas_total": len(cols),
            "dominios": list(doms), "vinculos": [v[1] for v in vinc], "filtros": len(filtros)}


def salvar_rascunho(tabela: str, texto: str) -> dict:
    t = tabela.lower()
    y = yaml.safe_load(texto)          # lança se não for YAML válido
    if not isinstance(y, dict) or "entidades" not in y or len(y["entidades"]) != 1:
        raise ValueError("o rascunho deve ter 'modulo' e exatamente uma entidade em 'entidades'")
    nome = next(iter(y["entidades"]))
    RASCUNHOS.mkdir(parents=True, exist_ok=True)
    (RASCUNHOS / f"{t}.yaml").write_text(texto, encoding="utf-8")
    c = estado_db()
    try:
        c.execute("insert or replace into rascunhos(tabela, modulo, entidade, yaml, validado, testado, atualizado) values(?,?,?,?,0,0,?)", (t, y.get("modulo"), nome, texto, agora()))
        registrar(c, "rascunho", t, f"rascunho salvo ({nome})")
        c.commit()
    finally:
        c.close()
    return {"ok": True, "entidade": nome, "modulo": y.get("modulo")}


def validar_rascunho(tabela: str, texto: str | None = None) -> dict:
    from model.validar_modelo import validar
    t = tabela.lower()
    if texto is not None:
        salvar_rascunho(t, texto)
    arq = RASCUNHOS / f"{t}.yaml"
    if not arq.exists():
        raise FileNotFoundError("sem rascunho salvo para esta tabela")
    prefixo = f"{arq.stem}."
    arqs = sorted(MODULOS.glob("*.yaml")) + [arq]
    _, erros, avisos, _ = validar(arqs)
    meus_e = [e for e in erros if e.startswith(prefixo) or ("domínio" in e and arq.stem in e)]
    meus_a = [a for a in avisos if a.startswith(prefixo)]
    ok = not meus_e
    c = estado_db()
    try:
        c.execute("update rascunhos set validado=?, atualizado=? where tabela=?", (1 if ok else 0, agora(), t))
        registrar(c, "validacao", t, "rascunho válido" if ok else f"{len(meus_e)} erro(s)")
        c.commit()
    finally:
        c.close()
    return {"ok": ok, "erros": meus_e, "avisos": meus_a}


def testar_rascunho(tabela: str) -> dict:
    """Executa o rascunho no banco REAL (somente leitura): roda a consulta gerada, confere fan-out dos vínculos e mede o preenchimento. Só agregados."""
    from extractor import db as bd
    from server import sqlbuilder as sb
    t = tabela.lower()
    arq = RASCUNHOS / f"{t}.yaml"
    if not arq.exists():
        raise FileNotFoundError("sem rascunho salvo")
    y = yaml.safe_load(arq.read_text(encoding="utf-8"))
    nome, e = next(iter(y["entidades"].items()))
    ac = e.get("acesso", {})
    cn = bd.conectar()
    try:
        f, aviso = {}, []
        emp = None
        if ac.get("empresa"):
            r = bd.select(cn, f"SELECT codi_emp, COUNT(*) AS n FROM bethadba.{e['tabela']} GROUP BY codi_emp ORDER BY n")
            if not r:
                return {"ok": True, "linhas": 0, "aviso": ["tabela sem linhas: nada a testar"]}
            emp = r[len(r) // 2]["codi_emp"]; f["empresa"] = emp
        for x in ac.get("exige_algum", []):
            if x == "periodo":
                f["periodo"] = ("entre", (datetime.date(2000, 1, 1), datetime.date(2100, 12, 31)))
            else:
                col = e["filtros"][x]["coluna"]
                vals = bd.select(cn, f"SELECT DISTINCT TOP 3 {col} AS c FROM bethadba.{e['tabela']}" + (" WHERE codi_emp = ?" if emp else ""), (emp,) if emp else ())
                f[x] = ("in", [v["c"] for v in vals])
        t0 = time.time()
        sql, par = sb.montar(e, f, limite=200)
        rows = bd.select(cn, sql, tuple(par))
        ms = (time.time() - t0) * 1000
        fan = "n/a"
        if e.get("vinculos"):
            sc, pc = sb.montar(e, f, contar=True)
            com = bd.select(cn, sc, tuple(pc))[0]["total"]
            sem = dict(e); sem["vinculos"] = {}
            sb2, pb = sb.montar(sem, f, contar=True)
            base = bd.select(cn, sb2, tuple(pb))[0]["total"]
            fan = "ok" if com == base else f"MULTIPLICA LINHAS ({base} -> {com})"
        preench = {}
        for k in (rows[0].keys() if rows else []):
            preench[k] = round(100 * sum(1 for r in rows if r[k] not in (None, "", 0)) / len(rows))
    finally:
        cn.close()
    ok = fan in ("ok", "n/a")
    c = estado_db()
    try:
        c.execute("update rascunhos set testado=?, atualizado=? where tabela=?", (1 if ok else 0, agora(), t))
        registrar(c, "teste", t, f"teste no banco: {len(rows)} linhas, {ms:.0f} ms, fan-out {fan}")
        c.commit()
    finally:
        c.close()
    return {"ok": ok, "empresa_usada": emp, "linhas_amostra": len(rows), "ms": round(ms), "fan_out": fan, "preenchimento_pct": preench}


def promover_rascunho(tabela: str, sobrescrever: bool = False) -> dict:
    t = tabela.lower()
    arq = RASCUNHOS / f"{t}.yaml"
    if not arq.exists():
        raise FileNotFoundError("sem rascunho salvo")
    v = validar_rascunho(t)
    if not v["ok"]:
        raise ValueError("o rascunho tem erros de validação; corrija antes de promover: " + "; ".join(v["erros"][:3]))
    y = yaml.safe_load(arq.read_text(encoding="utf-8"))
    nome = next(iter(y["entidades"]))
    destino = MODULOS / f"{y['modulo']}__{nome}.yaml"
    if destino.exists() and not sobrescrever:
        raise FileExistsError(f"{destino.name} já existe")
    destino.write_text(arq.read_text(encoding="utf-8").replace("# RASCUNHO gerado", "# PROMOVIDO de rascunho gerado", 1), encoding="utf-8")
    arq.unlink()
    c = estado_db()
    try:
        c.execute("delete from rascunhos where tabela=?", (t,))
        registrar(c, "promocao", t, f"entidade {nome} promovida para {destino.name}")
        c.commit()
    finally:
        c.close()
    Base._cache = None
    snapshot_hoje()
    return {"ok": True, "arquivo": f"src/model/modulos/{destino.name}", "entidade": nome,
            "proximo_passo": "Reinicie o servidor MCP para expor a entidade; rode pytest e scripts/testar_entidades.py; escreva as regras de negócio após conferir com dados."}


def rascunho_salvo(tabela: str) -> dict | None:
    c = estado_db()
    try:
        r = c.execute("select * from rascunhos where tabela=?", (tabela.lower(),)).fetchone()
        return dict(r) if r else None
    finally:
        c.close()
