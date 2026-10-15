"""Fase 2: consolida as relações entre tabelas a partir de três fontes.

  declarada  - FKs do banco (SYS.SYSFOREIGNKEYS)                       confiança 1.0
  observada  - igualdades A.col = B.col mineradas dos programas Domínio 0.5 - 0.9 (por nº de usos)
  inferida   - filha possui todas as colunas da chave de outra tabela   0.4

Tipos: fk | vigencia (ligação por período) | ligacao (sem chave completa) | temporaria (eftmp_*)

Tabelas geradas no catálogo: relacoes, relacao_colunas.
Uso: python src/model/relacoes.py
"""
import collections
import math
import pathlib
import re
import sqlite3

DB = pathlib.Path(__file__).resolve().parents[2] / "data" / "catalog" / "dominio_catalog.db"
TEMP = re.compile(r"(?i)(^|_)(tmp|temp)(_|$)|^tmp|^eftmp")


# colunas genéricas (período/sequência) não identificam uma entidade: não servem de base para inferência
GENERICAS = {"competencia", "data", "vigencia", "ano", "mes", "dia", "periodo", "sequencial", "seq", "tipo",
             "numero", "nume", "codigo", "data_ini", "data_fim", "hora", "linha", "ordem", "item", "sequ"}
MAX_FILHAS = 1000
# modos de inferência (cada letra liga uma regra extra) — calibrados em scripts/calibrar_inferencia.py
# contra as FKs declaradas (verdade-terreno): sem regra 17% de precisão; só "P" ~72% (cobertura 27%).
#   U: o pai precisa ser a única tabela com aquela chave (tabelas irmãs com a mesma PK são ambíguas)
#   P: o nome da filha começa com o nome do pai + "_" (convenção de nomes da Domínio: EFMVSPRO_*)
MODO_PADRAO = "P"
CONF_INFERIDA = 0.6  # precisão medida da regra P (limite inferior: inclui relações reais não declaradas)


def inferir(cols: dict, chave: dict, modo: str, max_filhas: int = MAX_FILHAS):
    """Devolve [(filha, pai, chave_pai)] por coincidência de chave. Não consulta FKs declaradas."""
    por_chave = collections.Counter(frozenset(k) for k in chave.values())
    out = []
    for pai, k in chave.items():
        extra = k - {"codi_emp"}
        if not extra or len(k) > 4 or TEMP.search(pai):
            continue
        ident = [c for c in extra if (c.startswith(("codi_", "i_")) and c not in GENERICAS
                                       and not any(g in c for g in ("competencia", "vigencia", "sequ")))]
        if not ident:
            continue
        if "U" in modo and por_chave[frozenset(k)] > 1:
            continue
        cand = []
        for filha, cs in cols.items():
            if filha == pai or not k <= set(cs) or TEMP.search(filha):
                continue
            if any(cols[pai][c][0] != cs[c][0] for c in k):
                continue
            if chave.get(filha) == k:
                continue
            if "P" in modo and not filha.startswith(pai + "_"):
                continue
            cand.append(filha)
        if len(cand) > max_filhas:
            continue
        out += [(f, pai, k) for f in cand]
    return out


def conf_observada(occ: int, arqs: int) -> float:
    if occ >= 50 and arqs >= 3:
        return 0.9
    if occ >= 10:
        return 0.8
    if occ >= 3:
        return 0.7
    return 0.5


def main() -> None:
    d = sqlite3.connect(DB)
    d.row_factory = sqlite3.Row
    nome = {r["nome_lower"]: r["nome"] for r in d.execute("select nome_lower, nome from tabelas")}
    linhas = {r["nome_lower"]: (r["linhas"] or 0) for r in d.execute("select nome_lower, linhas from tabelas")}

    cols = collections.defaultdict(dict)  # tab -> {col: (tipo, pk)}
    for r in d.execute("select lower(tabela) t, lower(nome) c, tipo, pk from colunas"):
        cols[r["t"]][r["c"]] = (r["tipo"], r["pk"])

    # chave de cada tabela: PK; se não houver, primeiro índice único
    chave = {}
    for t, cs in cols.items():
        pk = [c for c, (_, p) in cs.items() if p]
        if pk:
            chave[t] = set(pk)
    for r in d.execute("select lower(tabela) t, lower(colunas) c from indices where unico=1 order by length(colunas)"):
        if r["t"] not in chave:
            chave[r["t"]] = set(r["c"].split(","))

    d.executescript("""
        DROP TABLE IF EXISTS relacoes; DROP TABLE IF EXISTS relacao_colunas;
        CREATE TABLE relacoes(id INTEGER PRIMARY KEY AUTOINCREMENT, filha TEXT, pai TEXT, tipo TEXT, origens TEXT,
                              confianca REAL, ocorrencias INTEGER DEFAULT 0, arquivos INTEGER DEFAULT 0, role TEXT);
        CREATE TABLE relacao_colunas(relacao_id INTEGER, col_filha TEXT, col_pai TEXT, ocorrencias INTEGER DEFAULT 0);
        CREATE INDEX ix_rel_filha ON relacoes(filha); CREATE INDEX ix_rel_pai ON relacoes(pai);
        CREATE INDEX ix_relc ON relacao_colunas(relacao_id);""")

    def tipo_rel(a: str, b: str, ca: set, cb: set) -> str:
        if TEMP.search(a) or TEMP.search(b):
            return "temporaria"
        if "vigencia" in a or "vigencia" in b or any(c.startswith("vigencia") for c in ca | cb):
            return "vigencia"
        return "fk"

    def inserir(filha, pai, tipo, origens, conf, occ, arqs, role, pares):
        cur = d.execute("insert into relacoes(filha,pai,tipo,origens,confianca,ocorrencias,arquivos,role) values(?,?,?,?,?,?,?,?)",
                        (nome.get(filha, filha), nome.get(pai, pai), tipo, ",".join(origens), conf, occ, arqs, role))
        d.executemany("insert into relacao_colunas values(?,?,?,?)",
                      [(cur.lastrowid, cf, cp, n) for cf, cp, n in pares])

    # observações agregadas por par de colunas, indexadas pelo par de tabelas (a < b)
    obs = collections.defaultdict(list)  # (a,b) -> [(ca, cb, occ, arqs)]
    for r in d.execute("select tab_a, col_a, tab_b, col_b, ocorrencias, arquivos from joins_observados"):
        obs[(r["tab_a"], r["tab_b"])].append((r["col_a"], r["col_b"], r["ocorrencias"], r["arquivos"]))

    # ---- 1) declaradas, com suporte observado
    usadas = set()
    n_decl = 0
    for r in d.execute("select filha, pai, role, colunas_filha, colunas_pai from fks"):
        f, p = r["filha"].lower(), r["pai"].lower()
        cf, cp = r["colunas_filha"].lower().split(","), r["colunas_pai"].lower().split(",")
        par = (f, p) if f < p else (p, f)
        occ = arqs = 0
        for ca, cb, o, a in obs.get(par, []):
            mapa = {(x, y) for x, y in zip(cf, cp)}
            ok = ((ca, cb) in mapa) if par == (f, p) else ((cb, ca) in mapa)
            if ok:
                occ += o
                arqs = max(arqs, a)
                usadas.add((par, ca, cb))
        origens = ["declarada"] + (["observada"] if occ else [])
        inserir(f, p, tipo_rel(f, p, set(cf), set(cp)), origens, 1.0, occ, arqs, r["role"],
                [(x, y, 0) for x, y in zip(cf, cp)])
        n_decl += 1

    # ---- 2) observadas não cobertas por FK declarada
    n_obs = 0
    for (a, b), lst in obs.items():
        resto = [x for x in lst if ((a, b), x[0], x[1]) not in usadas]
        if not resto:
            continue
        mx = max(x[2] for x in resto)
        resto = [x for x in resto if x[2] >= max(2, 0.1 * mx)]
        if not resto:
            continue
        ca, cb = {x[0] for x in resto}, {x[1] for x in resto}
        ka, kb = chave.get(a), chave.get(b)
        # a ligação costuma omitir codi_emp (multiempresa): testa a chave sem ele, se sobrar alguma coluna
        ka_ef = (ka - {"codi_emp"}) or ka if ka else ka
        kb_ef = (kb - {"codi_emp"}) or kb if kb else kb
        a_pai = bool(ka_ef) and ka_ef <= ca
        b_pai = bool(kb_ef) and kb_ef <= cb
        if a_pai and not b_pai:
            pai, filha, inv = a, b, False
        elif b_pai and not a_pai:
            pai, filha, inv = b, a, True
        elif a_pai and b_pai:
            pai, filha, inv = (a, b, False) if linhas.get(a, 0) <= linhas.get(b, 0) else (b, a, True)
        else:
            pai, filha, inv = b, a, True  # sem chave completa: ordem alfabética
        # x = (col_a, col_b, ocorrencias, arquivos); saída = (col_filha, col_pai, ocorrencias)
        # inv=False: pai=a, filha=b  |  inv=True: pai=b, filha=a
        pares = [((x[0], x[1], x[2]) if inv else (x[1], x[0], x[2])) for x in resto]
        occ = sum(x[2] for x in resto)
        arqs = max(x[3] for x in resto)
        tipo = tipo_rel(filha, pai, ca, cb)
        if tipo == "fk" and not (a_pai or b_pai):
            tipo = "ligacao"
        inserir(filha, pai, tipo, ["observada"], conf_observada(occ, arqs), occ, arqs, None, pares)
        n_obs += 1
        usadas.add(((a, b), None, None))

    # ---- 3) inferidas por nome de chave (somente chaves com coluna além de codi_emp)
    pares_existentes = set()
    for r in d.execute("select lower(filha) f, lower(pai) p from relacoes"):
        pares_existentes.add((r["f"], r["p"]))
        pares_existentes.add((r["p"], r["f"]))
    n_inf = 0
    for filha, pai, k in inferir(cols, chave, MODO_PADRAO):
        if (filha, pai) in pares_existentes:
            continue
        inserir(filha, pai, "fk", ["inferida"], CONF_INFERIDA, 0, 0, None, [(c, c, 0) for c in sorted(k)])
        n_inf += 1

    d.commit()
    q = lambda s: d.execute(s).fetchall()
    print(f"declaradas={n_decl} observadas(novas)={n_obs} inferidas={n_inf}")
    print("por origem/tipo:")
    for r in q("select origens, tipo, count(*), round(avg(confianca),2) from relacoes group by 1,2 order by 3 desc"):
        print("  ", tuple(r))
    print("tabelas base com alguma relação:", q("""select count(*) from tabelas t where tipo='BASE' and exists
          (select 1 from relacoes r where lower(r.filha)=t.nome_lower or lower(r.pai)=t.nome_lower)""")[0][0],
          "de", q("select count(*) from tabelas where tipo='BASE'")[0][0])


if __name__ == "__main__":
    main()
