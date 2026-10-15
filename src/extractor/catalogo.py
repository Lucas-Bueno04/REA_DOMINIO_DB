"""Fase 1/2: extrai o dicionário de dados (estrutura apenas, sem dados de clientes)
do owner `bethadba` para um SQLite local em data/catalog/dominio_catalog.db.

Uso:  python src/extractor/catalogo.py
"""
import pathlib
import re
import sqlite3
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from extractor.db import conectar, select  # noqa: E402

RAIZ = pathlib.Path(__file__).resolve().parents[2]
DB = RAIZ / "data" / "catalog" / "dominio_catalog.db"
SQL_GERADOR = RAIZ / "sql" / "gerador_lista_tabelas.original.sql"
OWNER = "bethadba"

DEPARTAMENTO = {
    "EF": "Fiscal", "AT": "Fiscal", "VW": "Fiscal",
    "FO": "Pessoal", "PO": "Pessoal",
    "CT": "Contábil", "LR": "Contábil", "LA": "Contábil", "PM": "Contábil", "PA": "Contábil",
    "GE": "Geral", "US": "Geral",
    "HR": "Financeiro do escritório", "HN": "Financeiro do escritório", "HO": "Financeiro do escritório",
    "PC": "Processos", "PR": "Processos",
    "RG": "Societário",
    "AU": "Sistema", "SU": "Sistema", "MO": "Sistema", "SY": "Sistema", "TE": "Sistema", "TM": "Sistema",
}

SCHEMA = """
DROP TABLE IF EXISTS tabelas; DROP TABLE IF EXISTS colunas; DROP TABLE IF EXISTS fks; DROP TABLE IF EXISTS meta;
CREATE TABLE tabelas(
  table_id INTEGER PRIMARY KEY, nome TEXT NOT NULL, nome_lower TEXT NOT NULL, tipo TEXT, linhas INTEGER,
  comentario TEXT, prefixo TEXT, departamento TEXT, subcluster TEXT,
  legivel INTEGER, na_lista_gerador INTEGER, ultima_alteracao TEXT, view_def TEXT);
CREATE TABLE colunas(
  table_id INTEGER, tabela TEXT, ordem INTEGER, nome TEXT, tipo TEXT, tamanho INTEGER, tamanho_sys INTEGER,
  aceita_nulo INTEGER, pk INTEGER, padrao TEXT, comentario TEXT, PRIMARY KEY(table_id, ordem));
CREATE TABLE fks(
  id INTEGER PRIMARY KEY AUTOINCREMENT, filha TEXT, pai TEXT, role TEXT,
  colunas_filha TEXT, colunas_pai TEXT, origem TEXT DEFAULT 'declarada');
CREATE TABLE meta(chave TEXT PRIMARY KEY, valor TEXT);
CREATE INDEX ix_col_tab ON colunas(tabela); CREATE INDEX ix_tab_lower ON tabelas(nome_lower);
CREATE INDEX ix_fk_filha ON fks(filha); CREATE INDEX ix_fk_pai ON fks(pai);
"""


def excluidas_gerador() -> set[str]:
    txt = SQL_GERADOR.read_text(encoding="utf-8-sig")
    trecho = txt[txt.upper().index("NOT IN"):]
    return {m.upper() for m in re.findall(r"'([A-Za-z0-9_]+)'", trecho)}


def classificar(nome: str) -> tuple[str, str, str]:
    n = nome.upper()
    pref = n[:2]
    resto = n[2:]
    sub = resto.split("_")[0] if "_" in resto else "NUCLEO"
    return pref, DEPARTAMENTO.get(pref, "Outros"), sub or "NUCLEO"


def parse_colunas_fk(s: str) -> tuple[str, str]:
    filhas, pais = [], []
    for par in (s or "").split(","):
        if " IS " in par:
            a, b = par.split(" IS ", 1)
            filhas.append(a.strip())
            pais.append(b.strip())
    return ",".join(filhas), ",".join(pais)


def main() -> None:
    t0 = time.time()
    cn = conectar()
    DB.parent.mkdir(parents=True, exist_ok=True)
    lite = sqlite3.connect(DB)
    lite.executescript(SCHEMA)

    print("tabelas ...", flush=True)
    tabs = select(cn, f"""
        SELECT t.table_id, t.table_name, t.table_type_str, t.count, t.last_modified_at,
               s.remarks, s.view_def
          FROM SYS.SYSTAB t
          JOIN SYS.SYSUSER u ON u.user_id = t.creator
          LEFT JOIN SYS.SYSTABLE s ON s.table_id = t.table_id
         WHERE u.user_name = '{OWNER}'""")

    leg = select(cn, """
        SELECT DISTINCT p.stable_id AS table_id
          FROM SYS.SYSTABLEPERM p JOIN SYS.SYSUSER g ON g.user_id = p.grantee
         WHERE g.user_name IN ('_somenteconsulta','PUBLIC') AND p.selectauth IN ('Y','G')""")
    legiveis = {r["table_id"] for r in leg}
    excl = excluidas_gerador()

    for t in tabs:
        nome = t["table_name"]
        pref, depto, sub = classificar(nome)
        no_gerador = int(
            (t["table_type_str"] or "").upper() in ("BASE", "VIEW")
            and not nome.upper().startswith(("AUDIT_", "PBCAT"))
            and nome.upper() not in excl)
        lite.execute(
            "INSERT INTO tabelas VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (t["table_id"], nome, nome.lower(), t["table_type_str"], t["count"],
             (t["remarks"] or "").strip() or None, pref, depto, sub,
             int(t["table_id"] in legiveis), no_gerador,
             str(t["last_modified_at"]) if t["last_modified_at"] else None,
             t["view_def"] if (t["table_type_str"] or "").upper() == "VIEW" else None))
    lite.commit()
    print(f"  {len(tabs)} tabelas/views", flush=True)

    print("colunas ...", flush=True)
    cols = select(cn, f"""
        SELECT c.tname, c.cname, c.colno, c.coltype, c.length, c.syslength, c.nulls,
               c.in_primary_key, c.default_value, c.remarks
          FROM SYS.SYSCOLUMNS c WHERE c.creator = '{OWNER}'""")
    ids = {r[0].lower(): r[1] for r in lite.execute("SELECT nome, table_id FROM tabelas")}
    n = 0
    for c in cols:
        tid = ids.get(c["tname"].lower())
        if tid is None:
            continue
        lite.execute(
            "INSERT OR REPLACE INTO colunas VALUES(?,?,?,?,?,?,?,?,?,?,?)",
            (tid, c["tname"], c["colno"], c["cname"], c["coltype"], c["length"], c["syslength"],
             int((c["nulls"] or "N") == "Y"), int((c["in_primary_key"] or "N") == "Y"),
             c["default_value"], (c["remarks"] or "").strip() or None))
        n += 1
    lite.commit()
    print(f"  {n} colunas", flush=True)

    print("chaves estrangeiras ...", flush=True)
    fks = select(cn, f"""
        SELECT foreign_tname, primary_tname, role, columns
          FROM SYS.SYSFOREIGNKEYS WHERE foreign_creator = '{OWNER}'""")
    for f in fks:
        cf, cp = parse_colunas_fk(f["columns"])
        lite.execute("INSERT INTO fks(filha,pai,role,colunas_filha,colunas_pai) VALUES(?,?,?,?,?)",
                     (f["foreign_tname"], f["primary_tname"], f["role"], cf, cp))
    lite.commit()
    print(f"  {len(fks)} FKs", flush=True)

    info = select(cn, "SELECT PROPERTY('ProductVersion') AS v, DB_NAME() AS db")[0]
    for k, v in {"gerado_em": time.strftime("%Y-%m-%d %H:%M:%S"), "versao_servidor": info["v"],
                 "banco": info["db"], "owner": OWNER, "duracao_s": f"{time.time()-t0:.1f}"}.items():
        lite.execute("INSERT OR REPLACE INTO meta VALUES(?,?)", (k, v))
    lite.commit()
    lite.close()
    cn.close()
    print(f"ok -> {DB}  ({time.time()-t0:.1f}s)")


if __name__ == "__main__":
    main()
