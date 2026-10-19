"""Mapeamento em lote: gera, valida e testa (no banco REAL, somente leitura) entidades para as tabelas "não iniciadas" de um departamento.

Uso:  python scripts/mapear_lote.py --dep Fiscal [--fam "EF · cupom"] [--min-linhas 1] [--max-tabelas N] [--sem-teste]
Saída: src/model/modulos/<dep>_<familia>.yaml (um por família; famílias de até 3 tabelas vão para <dep>_outros.yaml)
       data/lotes/<dep>.json  (relatório: o que foi gerado, validado, testado e o que falhou)

A fonte da verdade do andamento é a plataforma (status derivado dos YAML) e o STATUS.md; este script não cria outro controle.
Rascunho gerado automaticamente nasce com `regras: []` (status "modelada"); as regras só entram depois de medidas
(scripts/medir_fatos.py) ou conferidas à mão.
"""
import argparse, collections, datetime, json, pathlib, re, sys, time
import yaml

RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from plataforma import dados
from model.validar_modelo import validar
from extractor import db as bd
from server import sqlbuilder as sb

MODULOS = RAIZ / "src" / "model" / "modulos"
RELATORIOS = RAIZ / "data" / "lotes"
TIPOS_FORA = ("binary", "long varchar", "uniqueidentifier", "timestamp")


SCRIPT = re.compile(r"script|^fil\d$|^frm_|compila|^comando_|clausula|^codi_comp$", re.I)


def eh_codigo_do_sistema(c):
    """Scripts, fórmulas e cláusulas compiladas do próprio sistema (texto longo): são código do software, não dado de negócio."""
    return bool(SCRIPT.search(c["nome"])) and (c["tipo"] or "") in ("varchar", "char") and (c["tamanho"] or 0) >= 1000


_CHAVES_FK = None


def chaves_de_fk(b):
    """{(tabela, coluna)} que participam de alguma FK (como filha ou pai): colunas GUID/long só são excluídas quando NÃO são chave de ligação."""
    global _CHAVES_FK
    if _CHAVES_FK is None:
        _CHAVES_FK = set()
        for r in b.cat.execute("select lower(filha) f, colunas_filha cf, lower(pai) p, colunas_pai cp from fks"):
            for c in r["cf"].split(","):
                _CHAVES_FK.add((r["f"], c.strip().lower()))
            for c in r["cp"].split(","):
                _CHAVES_FK.add((r["p"], c.strip().lower()))
    return _CHAVES_FK


def escolher_colunas(b, d, maximo=60):
    cols = [dict(r) for r in b.cat.execute("select * from colunas where tabela=? collate nocase order by ordem", (d["nome"],))]
    pk = [c for c in cols if c["pk"]]
    if not pk:
        ind = b.cat.execute("select colunas from indices where lower(tabela)=? and unico=1 order by length(colunas) limit 1", (d["t"],)).fetchone()
        nomes = [x.strip().lower() for x in ind["colunas"].split(",")] if ind else [cols[0]["nome"].lower()]
        pk = [c for c in cols if c["nome"].lower() in nomes]
    pkn = {c["nome"].lower() for c in pk}
    chaves_fk = chaves_de_fk(b)
    ok = lambda c: (not b.re_cred.search(c["nome"]) and "SEM USO" not in (c["comentario"] or "").upper()
                    and not (re.search(r"certificad", c["nome"], re.I) and (c["tipo"] or "") in ("varchar", "char") and (c["tamanho"] or 0) > 1)
                    and not eh_codigo_do_sistema(c)
                    and (c["pk"] or (d["t"], c["nome"].lower()) in chaves_fk
                         or not any(t in (c["tipo"] or "").lower() for t in TIPOS_FORA)))
    resto = [c for c in cols if c["nome"].lower() not in pkn and ok(c)]
    return [c["nome"] for c in pk] + [c["nome"] for c in resto][: max(maximo - len(pk), 0)]


def fmt(n):
    return f"{n:,}".replace(",", ".")


def renomear_repetidas(e):
    """Nomes de API gerados do comentário que acabam em _2, _3... (comentário repetido) passam a usar o nome da coluna do banco."""
    usados = set(e["colunas"])
    ren = {}
    for api, v in list(e["colunas"].items()):
        col = v["coluna"] if isinstance(v, dict) else v
        if re.search(r"_\d+$", api):
            novo = dados._slug(col, 40)
            while novo in usados:
                novo += "_c"
            ren[api] = novo; usados.add(novo)
    if not ren:
        return
    e["colunas"] = {ren.get(k, k): v for k, v in e["colunas"].items()}
    if e.get("filtros"):
        e["filtros"] = {ren.get(k, k): v for k, v in e["filtros"].items()}
    ac = e.get("acesso", {})
    if ac.get("exige_algum"):
        ac["exige_algum"] = [ren.get(k, k) for k in ac["exige_algum"]]


def chave_sem_pk(b, x, e):
    """Tabela sem PK e sem índice único: nenhuma coluna identifica a linha; a chave passa a ser o conjunto de colunas expostas (até 12)."""
    t = x["t"]
    tem_pk = b.cat.execute("select 1 from colunas where tabela=? collate nocase and pk=1 limit 1", (x["nome"],)).fetchone()
    tem_un = b.cat.execute("select 1 from indices where lower(tabela)=? and unico=1 limit 1", (t,)).fetchone()
    if not tem_pk and not tem_un:
        e["chave"] = list(dict.fromkeys((v["coluna"] if isinstance(v, dict) else v) for v in e["colunas"].values()))[:12]


def prefixo(dep):
    return dados._slug(dep.split()[0], 20)             # sem acento: "Contábil" -> contabil


def slug_modulo(dep, fam):
    s = re.sub(r"[^a-z0-9]+", "_", dados._slug(fam.split("·", 1)[-1].strip(), 30)).strip("_") or "nucleo"
    return f"{prefixo(dep)}_{s}"


def testar(e):
    """Mesmo teste da plataforma (SELECT real, 200 linhas, fan-out dos vínculos), sem gravar rascunho."""
    ac = e.get("acesso", {})
    cn = bd.conectar()
    try:
        f, emp = {}, None
        if ac.get("empresa"):
            r = bd.select(cn, f"SELECT codi_emp, COUNT(*) AS n FROM bethadba.{e['tabela']} GROUP BY codi_emp ORDER BY n", timeout=120)
            if not r:
                return {"ok": True, "linhas": 0, "nota": "sem linhas"}
            emp = r[len(r) // 2]["codi_emp"]; f["empresa"] = emp
        for x in ac.get("exige_algum", []):
            if x == "periodo":
                f["periodo"] = ("entre", (datetime.date(2000, 1, 1), datetime.date(2100, 12, 31)))
            else:
                col = e["filtros"][x]["coluna"]
                vals = bd.select(cn, f"SELECT DISTINCT TOP 3 {col} AS c FROM bethadba.{e['tabela']}" + (" WHERE codi_emp = ?" if emp else ""), (emp,) if emp else (), timeout=120)
                f[x] = ("in", [v["c"] for v in vals])
        t0 = time.time()
        sql, par = sb.montar(e, f, limite=200)
        rows = bd.select(cn, sql, tuple(par), timeout=120)
        ms = round((time.time() - t0) * 1000)
        fan = "n/a"
        if e.get("vinculos"):
            sc, pc = sb.montar(e, f, contar=True)
            com = bd.select(cn, sc, tuple(pc), timeout=120)[0]["total"]
            sem = dict(e); sem["vinculos"] = {}
            sb2, pb = sb.montar(sem, f, contar=True)
            base = bd.select(cn, sb2, tuple(pb), timeout=120)[0]["total"]
            fan = "ok" if com == base else f"MULTIPLICA ({base}->{com})"
        return {"ok": fan in ("ok", "n/a"), "empresa": emp, "linhas": len(rows), "ms": ms, "fan_out": fan}
    finally:
        cn.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dep", required=True)
    ap.add_argument("--fam")
    ap.add_argument("--min-linhas", type=int, default=1)
    ap.add_argument("--max-tabelas", type=int, default=0)
    ap.add_argument("--sem-teste", action="store_true")
    ap.add_argument("--maximo-colunas", type=int, default=60)
    ap.add_argument("--status", default="nao_iniciada", help="status de partida das tabelas (ex.: apoio: tabelas usadas só como vínculo, sem entidade própria)")
    ap.add_argument("--tabelas", default="", help="lista de tabelas (minúsculas, separadas por vírgula) em vez de todas do departamento")
    a = ap.parse_args()

    b = dados.Base.obter()
    so = {x.strip().lower() for x in a.tabelas.split(",") if x.strip()}
    ts = [x for x in dados.lista_tabelas() if x["status"] == a.status and x["dep"] == a.dep and x["linhas"] >= a.min_linhas
          and (not a.fam or x["fam"] == a.fam) and (not so or x["t"] in so)]
    ts.sort(key=lambda x: -x["linhas"])
    if a.max_tabelas:
        ts = ts[: a.max_tabelas]
    por_fam = collections.defaultdict(list)
    for x in ts:
        por_fam[x["fam"]].append(x)
    por_mod = collections.defaultdict(list)
    for fam, lst in por_fam.items():
        mod = slug_modulo(a.dep, fam) if len(lst) > 3 else f"{prefixo(a.dep)}_outros"
        por_mod[mod] += lst
    print(f"{len(ts)} tabelas -> {len(por_mod)} módulos", flush=True)

    rel = {"departamento": a.dep, "gerado_em": dados.agora(), "modulos": {}}
    for mod, lst in sorted(por_mod.items()):
        alvo = MODULOS / f"{mod}.yaml"
        doms, ents, usados = {}, {}, set(b.entidades)
        falhas = []
        if alvo.exists():                      # reaproveita o que já existe no arquivo (execuções incrementais)
            y0 = yaml.safe_load(alvo.read_text(encoding="utf-8"))
            doms.update(y0.get("dominios", {})); ents.update(y0["entidades"])
            usados -= set(y0["entidades"])
        for x in lst:
            if any(e["tabela"].lower() == x["t"] for e in ents.values()):
                continue
            try:
                r = dados.gerar_rascunho(x["nome"], modulo=mod, colunas=escolher_colunas(b, b.tabelas[x["t"]], a.maximo_colunas))
                y = yaml.safe_load(r["yaml"])
            except Exception as ex:
                falhas.append({"tabela": x["nome"], "etapa": "gerar", "erro": str(ex)[:200]}); continue
            e = y["entidades"][r["entidade"]]
            nome = dados._slug(x["t"], 60)               # nome previsível e único: o da tabela
            while nome in ents or nome in usados:
                nome += "_x"
            for dn, dv in y.get("dominios", {}).items():
                novo = dn.replace(r["entidade"], nome, 1) if dn.startswith(r["entidade"]) else f"{nome}_{dn[-20:]}"
                for c in e["colunas"].values():
                    if isinstance(c, dict) and c.get("dominio") == dn:
                        c["dominio"] = novo
                doms[novo] = dv
            renomear_repetidas(e)
            chave_sem_pk(b, x, e)
            e["descricao"] = e["descricao"].replace(" (descrição a completar)", "") + f" {fmt(x['linhas'])} linhas no catálogo; chave: {', '.join(e['chave'])}."
            ents[nome] = e
        cab = {"modulo": mod, "titulo": f"{a.dep} - {mod.split('_', 1)[-1]} (rascunho em lote)"}
        if doms:
            cab["dominios"] = doms
        cab["entidades"] = ents
        texto = ("# Gerado em lote por scripts/mapear_lote.py a partir da ESTRUTURA do banco (comentários, PK, FK) e testado no banco real.\n"
                 "# Entidades sem `regras` ainda não foram conferidas contra dados; domínios extraídos de comentários são hipóteses até medir (medir_fatos.py).\n"
                 + yaml.safe_dump(cab, allow_unicode=True, sort_keys=False, width=160, default_flow_style=None))
        alvo.write_text(texto, encoding="utf-8")
        print(f"[{mod}] {len(ents)} entidades escritas", flush=True)
        rel["modulos"][mod] = {"arquivo": alvo.name, "entidades": len(ents), "falhas_geracao": falhas, "validacao": [], "teste": {}}

    # ---- validação global
    arqs = sorted(MODULOS.glob("*.yaml"))
    _, erros, avisos, _ = validar(arqs)
    print(f"validação: {len(erros)} erros, {len(avisos)} avisos", flush=True)
    for e in erros[:40]:
        print("  ERRO", e)
    rel["erros_validacao"] = erros
    rel["avisos_validacao"] = avisos[:200]

    # ---- teste no banco
    if not a.sem_teste:
        for mod in rel["modulos"]:
            y = yaml.safe_load((MODULOS / f"{mod}.yaml").read_text(encoding="utf-8"))
            res = {}
            for nome, e in y["entidades"].items():
                try:
                    res[nome] = testar(e)
                except Exception as ex:
                    res[nome] = {"ok": False, "erro": str(ex)[:300]}
                s = res[nome]
                print(f"  {'OK  ' if s.get('ok') else 'FALHA'} {mod}.{nome[:44]:<44} {s.get('linhas','-')} linhas {s.get('ms','-')} ms fan-out={s.get('fan_out','-')} {s.get('erro','')[:120]}", flush=True)
            rel["modulos"][mod]["teste"] = res
    RELATORIOS.mkdir(parents=True, exist_ok=True)
    (RELATORIOS / f"{prefixo(a.dep)}.json").write_text(json.dumps(rel, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    nf = sum(1 for m in rel["modulos"].values() for s in m["teste"].values() if not s.get("ok"))
    print(f"fim: {sum(m['entidades'] for m in rel['modulos'].values())} entidades; {nf} falhas de teste; {len(erros)} erros de validação")


if __name__ == "__main__":
    main()
