"""Motor de consulta do servidor MCP (Fase 4). Somente leitura.

Camadas:
  * descoberta  : módulos, entidades, tabelas, relacionamentos, caminho entre tabelas (catálogo SQLite local, sem tocar o banco)
  * entidades   : consultas curadas pelos modelos YAML (filtros, paginação, vínculos, colunas calculadas)
  * genérica    : qualquer tabela legível do catálogo, com identificadores validados contra o catálogo
  * agregadas   : balancete e contas a receber
Regras sempre ativas (config/seguranca.yaml): credenciais nunca saem, limites de linhas/colunas, tabelas grandes exigem
filtro por coluna líder de índice, SELECT-only, valores sempre como parâmetros, auditoria de cada chamada.
"""
from __future__ import annotations

import collections
import datetime
import decimal
import difflib
import json
import os
import pathlib
import re
import sqlite3
import time
import uuid

import yaml

from extractor import db as bd
from server import sqlbuilder as sb

RAIZ = pathlib.Path(__file__).resolve().parents[2]
CATALOGO = RAIZ / "data" / "catalog" / "dominio_catalog.db"
LOG_AUDITORIA = RAIZ / "logs" / "auditoria.jsonl"
OPS_GENERICOS = {"eq", "diferente", "in", "entre", "gte", "lte", "contem", "prefixo", "nulo"}
ALIAS_OPS = {"igual": "eq", "=": "eq", "em": "in", "entre": "entre", "between": "entre", "maior_ou_igual": "gte", ">=": "gte",
             "menor_ou_igual": "lte", "<=": "lte", "diferente": "diferente", "!=": "diferente", "contem": "contem", "like": "contem",
             "prefixo": "prefixo", "comeca_com": "prefixo", "nulo": "nulo", "eq": "eq", "in": "in", "gte": "gte", "lte": "lte"}


class ErroUso(ValueError):
    """Erro de uso (parâmetro inválido, filtro obrigatório ausente, tabela bloqueada...). A mensagem orienta o chamador."""


def _sugerir(nome: str, opcoes) -> str:
    s = difflib.get_close_matches(nome, list(opcoes), n=4, cutoff=0.5)
    return f" Você quis dizer: {', '.join(s)}?" if s else ""


def _json_seguro(v):
    if isinstance(v, decimal.Decimal):
        return float(v)
    if isinstance(v, (datetime.datetime, datetime.date, datetime.time)):
        return v.isoformat()
    if isinstance(v, (bytes, bytearray, memoryview)):
        return bytes(v).hex()
    if isinstance(v, uuid.UUID):
        return str(v)
    if isinstance(v, str):
        return v.rstrip()
    return v


def _linha(r: dict) -> dict:
    return {k: _json_seguro(v) for k, v in r.items()}


def _coagir(v):
    """Converte texto ISO (AAAA-MM-DD) em data; deixa o resto como está."""
    if isinstance(v, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", v):
        try:
            return datetime.date.fromisoformat(v)
        except ValueError:
            return v
    if isinstance(v, (list, tuple)):
        return [_coagir(x) for x in v]
    return v


class Motor:
    def __init__(self, catalogo: pathlib.Path = CATALOGO, auditar: bool = True):
        self.ents, self.doms = sb.carregar_modelo()
        self.cat = sqlite3.connect(f"file:{catalogo.as_posix()}?mode=ro", uri=True, check_same_thread=False)
        self.cat.row_factory = sqlite3.Row
        cfg = yaml.safe_load((RAIZ / "config" / "seguranca.yaml").read_text(encoding="utf-8"))
        self.lim = cfg["limites"]
        self.re_cred = re.compile(cfg["colunas_credencial_regex"])
        self.cred_excecoes = {c.lower() for c in cfg.get("colunas_credencial_excecoes", [])}
        self.bloqueadas = {t.lower() for t in cfg["tabelas_bloqueadas"]}
        self.auditar = auditar
        self._tab = {r["nome_lower"]: dict(r) for r in self.cat.execute("select * from tabelas")}
        self._ent_por_tabela = collections.defaultdict(list)
        for n, e in self.ents.items():
            self._ent_por_tabela[e["tabela"].lower()].append(n)

    # ------------------------------------------------------------------ infraestrutura
    def _conectar(self):
        return bd.conectar()

    def _sql(self, sql: str, params, cn=None):
        cn = cn or self._conectar()
        try:
            return bd.select(cn, sql, tuple(params), timeout=self.lim["timeout_segundos"])
        finally:
            cn.close()

    def _auditoria(self, ferramenta: str, args: dict, linhas: int | None, ms: float, erro: str | None = None):
        if not self.auditar:
            return
        try:
            LOG_AUDITORIA.parent.mkdir(exist_ok=True)
            reg = {"ts": datetime.datetime.now().isoformat(timespec="seconds"), "ferramenta": ferramenta, "ms": round(ms),
                   "linhas": linhas, "erro": erro, "args": json.dumps(args, default=str, ensure_ascii=False)[:1500]}
            with LOG_AUDITORIA.open("a", encoding="utf-8") as f:
                f.write(json.dumps(reg, ensure_ascii=False) + "\n")
        except Exception:
            pass

    def _executar(self, ferramenta: str, args: dict, fn):
        t0 = time.time()
        try:
            r = fn()
            self._auditoria(ferramenta, args, len(r.get("linhas", [])) if isinstance(r, dict) and "linhas" in r else None, (time.time() - t0) * 1000)
            return r
        except Exception as e:
            self._auditoria(ferramenta, args, None, (time.time() - t0) * 1000, f"{type(e).__name__}: {e}"[:300])
            raise

    # ------------------------------------------------------------------ catálogo
    def _tabela(self, nome: str) -> dict:
        t = self._tab.get((nome or "").strip().lower())
        if not t or t["tipo"] not in ("BASE", "VIEW"):
            raise ErroUso(f"Tabela '{nome}' não existe no catálogo.{_sugerir((nome or '').lower(), self._tab)}")
        return t

    def _colunas(self, tabela: str) -> list[dict]:
        return [dict(r) for r in self.cat.execute("select * from colunas where tabela=? collate nocase order by ordem", (tabela,))]

    def _pk(self, tabela: str) -> list[str]:
        return [r[0] for r in self.cat.execute("select nome from colunas where tabela=? collate nocase and pk=1 order by ordem", (tabela,))]

    def _indices(self, tabela: str) -> list[dict]:
        return [dict(r) for r in self.cat.execute("select indice, colunas, unico from indices where lower(tabela)=lower(?) order by unico desc, indice", (tabela,))]

    def _chave_ordenacao(self, t: dict, cols: list[dict]) -> list[str]:
        """Colunas que ordenam de forma determinística: PK; senão o primeiro índice único; senão a 1ª coluna."""
        pk = self._pk(t["nome"])
        if pk:
            return pk
        for ind in self._indices(t["nome"]):
            if ind["unico"]:
                return ind["colunas"].split(",")
        return [cols[0]["nome"]]

    def _credencial(self, coluna: str) -> bool:
        return bool(self.re_cred.search(coluna)) and coluna.lower() not in self.cred_excecoes

    # ------------------------------------------------------------------ descoberta
    def listar_modulos(self) -> dict:
        mods = collections.defaultdict(list)
        for n, e in self.ents.items():
            mods[e["_modulo"]].append(n)
        deps = self.cat.execute("""select departamento, count(*) as tabelas, sum(linhas) as linhas from tabelas
                                   where tipo='BASE' and legivel=1 and na_lista_gerador=1 group by 1 order by 2 desc""").fetchall()
        return {
            "modulos_modelados": {m: {"entidades": len(v), "nomes": v} for m, v in sorted(mods.items())},
            "departamentos_do_banco": [{"departamento": r["departamento"], "tabelas": r["tabelas"], "linhas": r["linhas"]} for r in deps],
            "consultas_agregadas": ["balancete", "contas_a_receber"],
            "dica": "Use listar_entidades/descrever_entidade para consultas curadas; buscar_tabelas/descrever_tabela/consultar_tabela para qualquer outra tabela.",
        }

    def listar_entidades(self, modulo: str | None = None) -> dict:
        out = []
        for n, e in self.ents.items():
            if modulo and e["_modulo"] != modulo:
                continue
            ac = e.get("acesso", {})
            out.append({"entidade": n, "modulo": e["_modulo"], "titulo": e.get("titulo"), "tabela": e["tabela"], "volume": ac.get("volume"),
                        "exige_empresa": bool(ac.get("empresa")), "exige_algum_destes": ac.get("exige_algum"), "periodo": bool(ac.get("periodo")),
                        "filtros": list(e.get("filtros", {}))})
        if modulo and not out:
            raise ErroUso(f"Módulo '{modulo}' sem entidades.{_sugerir(modulo, {e['_modulo'] for e in self.ents.values()})}")
        return {"total": len(out), "entidades": out}

    def descrever_entidade(self, entidade: str) -> dict:
        e = self._entidade(entidade)
        cols = []
        for api, v in e["colunas"].items():
            d = v if isinstance(v, dict) else {"coluna": v}
            c = next((x for x in self._colunas(e["tabela"]) if x["nome"].lower() == d["coluna"].lower()), {})
            cols.append({"campo": api, "coluna": d["coluna"], "tipo": c.get("tipo"), "dominio": d.get("dominio"), "sensivel": d.get("sensivel"),
                         "descricao": c.get("comentario"), "nota": d.get("nota")})
        dom = {}
        for c in cols:
            if c["dominio"]:
                dom[c["dominio"]] = self.doms.get(c["dominio"], {})
        return {"entidade": entidade, "titulo": e.get("titulo"), "descricao": (e.get("descricao") or "").strip(), "modulo": e["_modulo"],
                "tabela": e["tabela"], "chave": e["chave"], "acesso": e.get("acesso", {}), "ordem_padrao": e.get("ordem"),
                "campos": cols, "colunas_calculadas": e.get("calculadas", {}), "colunas_coalescidas": e.get("coalescidas", {}),
                "vinculos": {k: {"tabela": v["tabela"], "liga": v["liga"], "colunas": list(v["colunas"])} for k, v in e.get("vinculos", {}).items()},
                "filtros": e.get("filtros", {}), "filhos": e.get("filhos", {}), "regras": e.get("regras", []), "privacidade": e.get("privacidade"),
                "dominios": dom}

    def dominio(self, nome: str) -> dict:
        d = self.doms.get(nome)
        if not d:
            raise ErroUso(f"Domínio '{nome}' não existe.{_sugerir(nome, self.doms)}")
        return {"dominio": nome, **d}

    def buscar_tabelas(self, termo: str, departamento: str | None = None, so_modeladas: bool = False, limite: int = 25) -> dict:
        t = f"%{termo.strip().lower()}%"
        q = """select distinct t.nome, t.comentario, t.linhas, t.departamento, t.tipo, t.legivel, t.na_lista_gerador from tabelas t
               left join colunas c on c.table_id=t.table_id
               where t.tipo in ('BASE','VIEW') and (t.nome_lower like ? or lower(t.comentario) like ? or lower(c.comentario) like ? or lower(c.nome) like ?)"""
        par = [t, t, t, t]
        if departamento:
            q += " and lower(t.departamento)=lower(?)"; par.append(departamento)
        q += " order by (t.nome_lower like ?) desc, t.linhas desc limit 300"; par.append(t)
        res = []
        for r in self.cat.execute(q, par):
            nome = r["nome"].lower()
            modeladas = self._ent_por_tabela.get(nome, [])
            if so_modeladas and not modeladas:
                continue
            res.append({"tabela": r["nome"], "descricao": r["comentario"], "linhas": r["linhas"], "departamento": r["departamento"],
                        "consultavel": bool(r["legivel"] and r["na_lista_gerador"] and nome not in self.bloqueadas), "entidades": modeladas})
            if len(res) >= min(int(limite), 100):
                break
        return {"termo": termo, "total": len(res), "tabelas": res}

    def descrever_tabela(self, tabela: str) -> dict:
        t = self._tabela(tabela)
        cols = []
        for c in self._colunas(t["nome"]):
            p = self.cat.execute("select linhas, nao_nulos, em_branco, zeros, sentinela from perfil_colunas where tabela=? and coluna=?",
                                 (t["nome_lower"], c["nome"].lower())).fetchone()
            preench = None
            if p and p["linhas"]:
                preench = round(100 * ((p["nao_nulos"] or 0) - (p["em_branco"] or 0) - (p["sentinela"] or 0)) / p["linhas"], 1)
            cols.append({"coluna": c["nome"], "tipo": f"{c['tipo']}({c['tamanho']})", "pk": bool(c["pk"]), "aceita_nulo": bool(c["aceita_nulo"]),
                         "descricao": c["comentario"], "bloqueada_por_credencial": self._credencial(c["nome"]) or None,
                         "preenchimento_pct": preench})
        rel = self.cat.execute("select count(*) from relacoes where (lower(filha)=? or lower(pai)=?) and tipo<>'temporaria'", (t["nome_lower"],) * 2).fetchone()[0]
        return {"tabela": t["nome"], "descricao": t["comentario"], "tipo": t["tipo"], "linhas": t["linhas"], "departamento": t["departamento"],
                "consultavel": bool(t["legivel"] and t["na_lista_gerador"] and t["nome_lower"] not in self.bloqueadas),
                "bloqueada": t["nome_lower"] in self.bloqueadas, "entidades_que_usam": self._ent_por_tabela.get(t["nome_lower"], []),
                "chave_primaria": self._pk(t["nome"]), "indices": self._indices(t["nome"]), "relacionamentos": rel, "colunas": cols}

    def relacionamentos(self, tabela: str, confianca_minima: float = 0.5, limite: int = 60) -> dict:
        t = self._tabela(tabela)
        rows = self.cat.execute("""select id, filha, pai, tipo, origens, confianca, ocorrencias, role from relacoes
                                   where (lower(filha)=? or lower(pai)=?) and tipo<>'temporaria' and confianca>=?
                                   order by confianca desc, ocorrencias desc limit ?""", (t["nome_lower"], t["nome_lower"], confianca_minima, min(int(limite), 300))).fetchall()
        out = []
        for r in rows:
            cols = [[c["col_filha"], c["col_pai"]] for c in self.cat.execute("select col_filha, col_pai from relacao_colunas where relacao_id=?", (r["id"],))]
            eh_pai = r["pai"].lower() == t["nome_lower"]
            out.append({"papel": "pai de" if eh_pai else "filha de", "tabela_relacionada": r["filha"] if eh_pai else r["pai"], "tipo": r["tipo"],
                        "origens": r["origens"], "confianca": r["confianca"], "usos_em_programas": r["ocorrencias"], "colunas_filha_pai": cols,
                        "nome_da_fk": r["role"]})
        return {"tabela": t["nome"], "total": len(out), "relacoes": out,
                "aviso": "Relações 'observada'/'inferida' não são FKs do banco: confiança 1,0 = FK declarada; 0,5–0,9 = usada nos programas da Domínio; 0,6 = inferida por nome."}

    def caminho_entre(self, origem: str, destino: str, max_saltos: int = 4, confianca_minima: float = 0.7) -> dict:
        a, b = self._tabela(origem)["nome_lower"], self._tabela(destino)["nome_lower"]
        adj = collections.defaultdict(list)
        for r in self.cat.execute("select id, lower(filha) f, lower(pai) p, tipo, confianca from relacoes where tipo<>'temporaria' and confianca>=?", (confianca_minima,)):
            if r["f"] == r["p"]:
                continue
            adj[r["f"]].append((r["p"], r["id"])); adj[r["p"]].append((r["f"], r["id"]))
        HUB = "geempre"      # a empresa liga quase tudo: só vale como extremo, senão todo caminho "passa" por ela
        fila, visto = collections.deque([(a, [])]), {a}
        while fila:
            no, caminho = fila.popleft()
            if no == b:
                break
            if len(caminho) >= max_saltos:
                continue
            for viz, rid in adj[no]:
                if viz in visto or (viz == HUB and viz != b):
                    continue
                visto.add(viz); fila.append((viz, caminho + [(no, viz, rid)]))
        else:
            return {"origem": origem, "destino": destino, "encontrado": False, "dica": "Tente aumentar max_saltos ou baixar confianca_minima."}
        passos = []
        for de, para, rid in caminho:
            r = self.cat.execute("select filha, pai, tipo, origens, confianca from relacoes where id=?", (rid,)).fetchone()
            cols = [[c["col_filha"], c["col_pai"]] for c in self.cat.execute("select col_filha, col_pai from relacao_colunas where relacao_id=?", (rid,))]
            passos.append({"de": self._tab[de]["nome"], "para": self._tab[para]["nome"], "filha": r["filha"], "pai": r["pai"], "tipo": r["tipo"],
                           "origens": r["origens"], "confianca": r["confianca"], "colunas_filha_pai": cols})
        return {"origem": origem, "destino": destino, "encontrado": True, "saltos": len(passos), "passos": passos,
                "aviso": "O caminho é o MAIS CURTO no grafo de relações, não necessariamente o semanticamente correto. Confira com descrever_entidade."}

    # ------------------------------------------------------------------ entidades
    def _entidade(self, nome: str) -> dict:
        e = self.ents.get(nome)
        if not e:
            raise ErroUso(f"Entidade '{nome}' não existe.{_sugerir(nome, self.ents)} Use listar_entidades.")
        return e

    def _filtros_entidade(self, e: dict, empresa, filtros) -> dict:
        out = {}
        ac = e.get("acesso", {})
        if empresa is not None:
            if not ac.get("empresa"):
                raise ErroUso("Esta entidade não depende de empresa (tabela global): não informe 'empresa'.")
            out["empresa"] = ("in", [int(x) for x in empresa]) if isinstance(empresa, (list, tuple)) else int(empresa)
        for nome, v in (filtros or {}).items():
            if nome == "empresa":
                out["empresa"] = v; continue
            op, val = self._par(v, periodo=(nome == "periodo"))
            if nome != "periodo" and nome not in e.get("filtros", {}):
                raise ErroUso(f"Filtro '{nome}' não existe nesta entidade.{_sugerir(nome, e.get('filtros', {}))} Filtros: {', '.join(e.get('filtros', {}))}")
            out[nome] = (op, _coagir(val))
        return out

    def _par(self, v, periodo: bool = False):
        if isinstance(v, dict):
            if periodo and set(v) <= {"de", "ate"}:
                if "de" in v and "ate" in v:
                    return "entre", [v["de"], v["ate"]]
                return ("gte", v["de"]) if "de" in v else ("lte", v["ate"])
            if len(v) != 1:
                raise ErroUso("Cada filtro aceita um operador: {\"entre\": [a, b]}, {\"in\": [...]}, {\"contem\": \"x\"}, {\"gte\": v}, {\"lte\": v}, {\"prefixo\": \"x\"} ou um valor simples.")
            op, val = next(iter(v.items()))
            if op not in ALIAS_OPS:
                raise ErroUso(f"Operador '{op}' desconhecido. Use: eq, in, entre, gte, lte, contem, prefixo.")
            return ALIAS_OPS[op], val
        if isinstance(v, (list, tuple)):
            return "in", list(v)
        return "eq", v

    def consultar_entidade(self, entidade: str, empresa=None, filtros: dict | None = None, colunas: list[str] | None = None,
                           ordem: list[str] | None = None, limite: int = 50, offset: int = 0, contar: bool = False, decodificar: bool = False) -> dict:
        args = {"entidade": entidade, "empresa": empresa, "filtros": filtros, "colunas": colunas, "ordem": ordem, "limite": limite, "offset": offset}
        return self._executar("consultar_entidade", args, lambda: self._consultar_entidade(entidade, empresa, filtros, colunas, ordem, limite, offset, contar, decodificar))

    def _consultar_entidade(self, entidade, empresa, filtros, colunas, ordem, limite, offset, contar, decodificar):
        e = self._entidade(entidade)
        f = self._filtros_entidade(e, empresa, filtros)
        limite = max(1, min(int(limite or self.lim["linhas_padrao"]), self.lim["linhas_maximo"]))
        offset = max(0, int(offset or 0))
        ord_ = None
        if ordem:
            ord_ = []
            reais = {api: (v["coluna"] if isinstance(v, dict) else v) for api, v in e["colunas"].items()}
            for item in ordem:
                partes = item.strip().split()
                campo, d = partes[0], (partes[1].lower() if len(partes) > 1 else "asc")
                if campo not in reais:
                    raise ErroUso(f"Ordenação por '{campo}' não permitida: use um campo da própria entidade ({', '.join(reais)}).")
                if d not in ("asc", "desc"):
                    raise ErroUso("Direção de ordenação deve ser asc ou desc.")
                ord_.append([reais[campo], d])
        try:
            sql, par = sb.montar(e, f, colunas=colunas, limite=limite, offset=offset, ordem=ord_)
            linhas = [_linha(r) for r in self._sql(sql, par)]
            total = None
            if contar:
                sc, pc = sb.montar(e, f, contar=True)
                total = self._sql(sc, pc)[0]["total"]
        except sb.ErroConsulta as ex:
            raise ErroUso(str(ex)) from None
        if decodificar:
            for api, v in e["colunas"].items():
                dn = v.get("dominio") if isinstance(v, dict) else None
                if dn and dn in self.doms:
                    mapa = {str(k): str(x) for k, x in (self.doms[dn].get("valores") or {}).items()}
                    for r in linhas:
                        if api in r and r[api] is not None:
                            r[f"{api}_descricao"] = mapa.get(str(r[api]).strip())
        res = {"entidade": entidade, "tabela": e["tabela"], "linhas": linhas, "retornadas": len(linhas), "limite": limite, "offset": offset,
               "proximo_offset": offset + len(linhas) if len(linhas) == limite else None}
        if total is not None:
            res["total"] = total
        regras = e.get("regras")
        if regras:
            res["regras_da_entidade"] = len(regras)
            res["dica"] = "Veja descrever_entidade para as regras de negócio validadas desta entidade."
        return res

    # ------------------------------------------------------------------ tabela genérica
    def consultar_tabela(self, tabela: str, empresa=None, filtros=None, colunas: list[str] | None = None, ordem: list[str] | None = None,
                         limite: int = 50, offset: int = 0, contar: bool = False) -> dict:
        args = {"tabela": tabela, "empresa": empresa, "filtros": filtros, "colunas": colunas, "ordem": ordem, "limite": limite, "offset": offset}
        return self._executar("consultar_tabela", args, lambda: self._consultar_tabela(tabela, empresa, filtros, colunas, ordem, limite, offset, contar))

    def _consultar_tabela(self, tabela, empresa, filtros, colunas, ordem, limite, offset, contar):
        t = self._tabela(tabela)
        nome_l = t["nome_lower"]
        if nome_l in self.bloqueadas:
            raise ErroUso(f"A tabela {t['nome']} é um cofre de credenciais/usuários e está bloqueada neste servidor.")
        if not (t["legivel"] and t["na_lista_gerador"]):
            raise ErroUso(f"A tabela {t['nome']} é interna do sistema (não consta nas fontes de dados do gerador) e não é consultável.")
        cols = self._colunas(t["nome"])
        por_nome = {c["nome"].lower(): c for c in cols}
        bloqueadas = [c["nome"] for c in cols if self._credencial(c["nome"])]
        # colunas a selecionar
        if colunas:
            if len(colunas) > self.lim["colunas_maximo"]:
                raise ErroUso(f"No máximo {self.lim['colunas_maximo']} colunas por consulta.")
            sel = []
            for c in colunas:
                if c.lower() not in por_nome:
                    raise ErroUso(f"Coluna '{c}' não existe em {t['nome']}.{_sugerir(c.lower(), por_nome)}")
                if self._credencial(c):
                    raise ErroUso(f"A coluna {c} guarda credencial e não pode ser consultada.")
                sel.append(por_nome[c.lower()]["nome"])
            avisos = []
        else:
            livres = [c["nome"] for c in cols if not self._credencial(c["nome"])]
            sel = livres[: self.lim["colunas_padrao_tabela_generica"]]
            avisos = []
            if len(livres) > len(sel):
                avisos.append(f"A tabela tem {len(livres)} colunas consultáveis; devolvidas as {len(sel)} primeiras. Use 'colunas' para escolher.")
        if bloqueadas:
            avisos.append(f"{len(bloqueadas)} coluna(s) de credencial omitida(s): {', '.join(bloqueadas[:6])}")
        # filtros
        conds, params, filtradas = [], [], set()
        if empresa is not None:
            if "codi_emp" not in por_nome:
                raise ErroUso(f"{t['nome']} não tem coluna codi_emp: não use 'empresa'.")
            op, val = ("in", [int(x) for x in empresa]) if isinstance(empresa, (list, tuple)) else ("eq", int(empresa))
            conds.append(sb._condicao("t.codi_emp", op, val, params)); filtradas.add("codi_emp")
        itens = filtros if isinstance(filtros, list) else [{"coluna": k, "valor": v} for k, v in (filtros or {}).items()]
        for it in itens:
            col = (it.get("coluna") or "").lower()
            if col not in por_nome:
                raise ErroUso(f"Coluna de filtro '{it.get('coluna')}' não existe em {t['nome']}.{_sugerir(col, por_nome)}")
            if self._credencial(col):
                raise ErroUso(f"Não é permitido filtrar pela coluna {col} (credencial).")
            op, val = self._par(it["valor"]) if "op" not in it else (ALIAS_OPS.get(it["op"]), it.get("valor"))
            if op not in OPS_GENERICOS:
                raise ErroUso(f"Operador inválido em '{col}'. Use: {', '.join(sorted(OPS_GENERICOS))}.")
            expr = f"t.{por_nome[col]['nome']}"
            if op == "nulo":
                conds.append(f"{expr} IS {'NULL' if val in (True, 'sim', 1, 'S') else 'NOT NULL'}")
            elif op == "diferente":
                params.append(_coagir(val)); conds.append(f"{expr} <> ?")
            else:
                if op in ("contem", "prefixo") and por_nome[col]["tipo"] not in ("char", "varchar", "long varchar"):
                    raise ErroUso(f"'{op}' só vale para colunas de texto; {col} é {por_nome[col]['tipo']}.")
                if op == "in" and len(val) > self.lim["valores_em_in_maximo"]:
                    raise ErroUso(f"'in' aceita no máximo {self.lim['valores_em_in_maximo']} valores.")
                conds.append(sb._condicao(expr, op, _coagir(val), params))
            filtradas.add(col)
        # proteção de tabela grande: precisa filtrar por coluna que lidere algum índice
        if (t["linhas"] or 0) >= self.lim["tabela_grande_linhas"]:
            lideres = {i["colunas"].split(",")[0].lower() for i in self._indices(t["nome"])}
            if not (filtradas & lideres):
                raise ErroUso(f"{t['nome']} tem {t['linhas']:,} linhas: informe ao menos um filtro por coluna indexada "
                              f"({', '.join(sorted(lideres)[:8])}) ou por 'empresa'.".replace(",", "."))
        # ordenação (determinística, para paginar sem repetir)
        if ordem:
            partes = []
            for o in ordem:
                p = o.strip().split()
                if p[0].lower() not in por_nome:
                    raise ErroUso(f"Ordenação por coluna inexistente: {p[0]}")
                partes.append(f"t.{por_nome[p[0].lower()]['nome']} {'DESC' if len(p) > 1 and p[1].lower() == 'desc' else 'ASC'}")
        else:
            partes = [f"t.{c} ASC" for c in self._chave_ordenacao(t, cols)]
        limite = max(1, min(int(limite or self.lim["linhas_padrao"]), self.lim["linhas_maximo"]))
        offset = max(0, int(offset or 0))
        base = f"FROM {sb.OWNER}.{t['nome']} t" + (" WHERE " + " AND ".join(conds) if conds else "")
        sql = f"SELECT TOP {limite} START AT {offset + 1} " + ", ".join(f"t.{c}" for c in sel) + f" {base} ORDER BY " + ", ".join(partes)
        linhas = [_linha(r) for r in self._sql(sql, params)]
        res = {"tabela": t["nome"], "colunas": sel, "linhas": linhas, "retornadas": len(linhas), "limite": limite, "offset": offset,
               "proximo_offset": offset + len(linhas) if len(linhas) == limite else None}
        if contar:
            res["total"] = self._sql(f"SELECT COUNT(*) AS total {base}", params)[0]["total"]
        if avisos:
            res["avisos"] = avisos
        return res

    # ------------------------------------------------------------------ agregadas
    def balancete(self, empresa: int, data_inicial: str, data_final: str, filial: int | None = None, somente_com_movimento: bool = True) -> dict:
        args = {"empresa": empresa, "data_inicial": data_inicial, "data_final": data_final, "filial": filial}
        def run():
            di, df = _coagir(data_inicial), _coagir(data_final)
            if not isinstance(di, datetime.date) or not isinstance(df, datetime.date):
                raise ErroUso("data_inicial e data_final devem estar no formato AAAA-MM-DD.")
            if di > df:
                raise ErroUso("data_inicial deve ser menor ou igual a data_final.")
            sql, par = sb.montar_balancete(int(empresa), di, df, filial)
            rows = [_linha(r) for r in self._sql(sql, par)]
            for r in rows:
                r["saldo_final"] = round(float(r["saldo_anterior"] or 0) + float(r["debitos"] or 0) - float(r["creditos"] or 0), 2)
                r["natureza_saldo_final"] = "D" if r["saldo_final"] > 0 else "C" if r["saldo_final"] < 0 else "-"
            if somente_com_movimento:
                rows = [r for r in rows if r["saldo_anterior"] or r["debitos"] or r["creditos"]]
            tot = lambda k: round(sum(float(r[k] or 0) for r in rows), 2)
            return {"empresa": empresa, "periodo": [data_inicial, data_final], "contas": len(rows), "linhas": rows,
                    "totais": {"debitos": tot("debitos"), "creditos": tot("creditos"), "saldo_anterior": tot("saldo_anterior"), "saldo_final": tot("saldo_final")},
                    "aviso": "Saldo = débitos − créditos (positivo = devedor). Só contas analíticas. A conta é resolvida pelo plano de contas do lançamento (plano_empresa), que pode ser de outra empresa. Totais devem fechar: débitos = créditos e saldo final = 0."}
        return self._executar("balancete", args, run)

    def contas_a_receber(self, escritorio: int, vencimento_de: str | None = None, vencimento_ate: str | None = None, situacao: str | None = None,
                         cliente_codigo: int | None = None, limite: int = 50, offset: int = 0, contar: bool = False) -> dict:
        args = {"escritorio": escritorio, "vencimento_de": vencimento_de, "vencimento_ate": vencimento_ate, "situacao": situacao, "cliente_codigo": cliente_codigo}
        def run():
            try:
                kw = dict(vencimento_de=_coagir(vencimento_de), vencimento_ate=_coagir(vencimento_ate), situacao=situacao, cliente_codigo=cliente_codigo)
                sql, par = sb.montar_contas_a_receber(int(escritorio), limite=limite, offset=offset, **kw)
                linhas = [_linha(r) for r in self._sql(sql, par)]
                res = {"escritorio": escritorio, "linhas": linhas, "retornadas": len(linhas), "limite": min(int(limite), self.lim["linhas_maximo"]), "offset": int(offset),
                       "proximo_offset": int(offset) + len(linhas) if len(linhas) == min(int(limite), self.lim["linhas_maximo"]) else None}
                if contar:
                    sc, pc = sb.montar_contas_a_receber(int(escritorio), contar=True, **kw)
                    res["total"] = self._sql(sc, pc)[0]["total"]
            except sb.ErroConsulta as ex:
                raise ErroUso(str(ex)) from None
            res["aviso"] = ("saldo = Σ valor dos itens − Σ valor LÍQUIDO dos recebimentos. situacao: aberta (>0), quitada (=0), inconsistente (<0). "
                            "'escritorio' é o CODI_EMP do escritório (1 ou 930), não da empresa-cliente. O módulo Honorários não tem dados de 2026.")
            return res
        return self._executar("contas_a_receber", args, run)
