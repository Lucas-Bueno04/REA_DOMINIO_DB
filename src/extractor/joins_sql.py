"""Fase 2: minera os JOINs reais usados pela Domínio nos seus próprios executáveis/.pbd.

Para cada objeto (cadeia de blocos DAT*) extrai o texto SQL, resolve aliases
(`bethadba.efsaidas AS S`) e coleta igualdades `A.col = B.col` entre tabelas distintas,
validando que as duas colunas existem no catálogo. Também registra o uso de tabelas
por arquivo (mapa módulo/programa -> tabelas).

Saída (no catálogo SQLite): joins_observados, uso_tabela_arquivo.
Uso: python src/extractor/joins_sql.py [pasta ...]      (padrão: C:\\Contabil)
"""
import bisect
import collections
import multiprocessing as mp
import pathlib
import re
import sqlite3
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from extractor.corpus_sql import cadeias  # noqa: E402

RAIZ = pathlib.Path(__file__).resolve().parents[2]
DB = RAIZ / "data" / "catalog" / "dominio_catalog.db"

RUN8 = re.compile(rb"[\x09\x0a\x0d\x20-\x7e\xc0-\xff]{12,}")
RUN16 = re.compile(rb"(?:[\x09\x0a\x0d\x20-\x7e\xc0-\xff]\x00){12,}")
PRE_FILTRO = re.compile(r"(?i)\b(select|where|join)\b")
ID = r"[A-Za-z_][A-Za-z0-9_$#]*"
RE_ALIAS = re.compile(rf"(?i)\b(?:(?:bethadba|dsdba)\s*\.\s*)?({ID})\b(?:\s+as)?\s+({ID})\b")
RE_PRED = re.compile(
    rf"(?i)(?:(?:bethadba|dsdba)\s*\.\s*)?({ID})\s*\.\s*({ID})\s*=\s*(?:(?:bethadba|dsdba)\s*\.\s*)?({ID})\s*\.\s*({ID})")
RE_TABELA_BETHADBA = re.compile(rf"(?i)\bbethadba\s*\.\s*({ID})")
KEYWORDS = set("""select from where and or on join inner left right full outer cross natural group by order having union all
distinct as case when then else end in is not null like between exists lateral key set values into top start with
asc desc over partition rows only for update using intersect except sum count min max avg coalesce""".split())

_TAB: dict[str, set] = {}


def _init(db_path: str) -> None:
    lite = sqlite3.connect(db_path)
    cols = collections.defaultdict(set)
    for t, c in lite.execute("select lower(tabela), lower(nome) from colunas"):
        cols[t].add(c)
    _TAB.update(cols)
    lite.close()


def textos_do_arquivo(dados: bytes):
    unicode_pb = dados[:6] == b"HDR*P\x00"
    for obj in list(cadeias(dados)) + [dados]:
        if unicode_pb:
            partes = [m.group(0).decode("utf-16-le", "ignore") for m in RUN16.finditer(obj)]
        else:
            partes = [m.group(0).decode("cp1252", "ignore") for m in RUN8.finditer(obj)]
        if not partes:
            continue
        txt = " ".join(partes)
        if PRE_FILTRO.search(txt):
            yield re.sub(r"\s+", " ", txt)


def minerar_texto(txt: str, joins: collections.Counter, uso: collections.Counter) -> None:
    defs = []  # (pos, alias, tabela)
    for m in RE_ALIAS.finditer(txt):
        tab, ali = m.group(1).lower(), m.group(2).lower()
        if tab in _TAB:
            uso[tab] += 1
            if ali not in KEYWORDS:
                defs.append((m.start(), ali, tab))
    for m in RE_TABELA_BETHADBA.finditer(txt):
        t = m.group(1).lower()
        if t in _TAB:
            uso[t] += 0  # garante presença
    if not defs and not any(True for _ in RE_PRED.finditer(txt)):
        return
    pos_def = [d[0] for d in defs]
    por_alias = collections.defaultdict(list)
    for i, (_, ali, _) in enumerate(defs):
        por_alias[ali].append(i)

    def resolver(q: str, pos: int):
        q = q.lower()
        idxs = por_alias.get(q)
        if idxs:
            ant = [i for i in idxs if defs[i][0] < pos]
            i = ant[-1] if ant else idxs[0]
            return defs[i][2]
        return q if q in _TAB else None

    for m in RE_PRED.finditer(txt):
        qa, ca, qb, cb = (m.group(i).lower() for i in range(1, 5))
        ta, tb = resolver(qa, m.start()), resolver(qb, m.start())
        if not ta or not tb or ta == tb:
            continue
        if ca not in _TAB[ta] or cb not in _TAB[tb]:
            continue
        a, b = (ta, ca), (tb, cb)
        if a > b:
            a, b = b, a
        joins[(a[0], a[1], b[0], b[1])] += 1


def processar(arq: str):
    joins, uso = collections.Counter(), collections.Counter()
    try:
        dados = pathlib.Path(arq).read_bytes()
        for txt in textos_do_arquivo(dados):
            minerar_texto(txt, joins, uso)
    except Exception as e:  # arquivo ilegível não derruba o lote
        return arq, joins, uso, str(e)
    return arq, joins, uso, None


def main(pastas: list[str]) -> None:
    t0 = time.time()
    arqs = []
    for p in pastas:
        pp = pathlib.Path(p)
        arqs += [str(f) for f in pp.rglob("*") if f.is_file() and f.suffix.lower() in (".pbd", ".exe")]
    arqs.sort(key=lambda f: -pathlib.Path(f).stat().st_size)
    print(f"{len(arqs)} arquivos", flush=True)

    lite = sqlite3.connect(DB)
    lite.executescript("""
        DROP TABLE IF EXISTS joins_observados; DROP TABLE IF EXISTS uso_tabela_arquivo;
        CREATE TABLE joins_observados(tab_a TEXT, col_a TEXT, tab_b TEXT, col_b TEXT, ocorrencias INTEGER,
                                      arquivos INTEGER, exemplos TEXT, PRIMARY KEY(tab_a,col_a,tab_b,col_b));
        CREATE TABLE uso_tabela_arquivo(arquivo TEXT, tabela TEXT, ocorrencias INTEGER, PRIMARY KEY(arquivo,tabela));""")
    agg = collections.defaultdict(lambda: [0, []])
    erros = []
    with mp.Pool(min(8, mp.cpu_count()), initializer=_init, initargs=(str(DB),)) as pool:
        for i, (arq, joins, uso, err) in enumerate(pool.imap_unordered(processar, arqs, chunksize=1), 1):
            nome = pathlib.Path(arq).name
            if err:
                erros.append((nome, err))
            for k, v in joins.items():
                agg[k][0] += v
                agg[k][1].append(nome)
            lite.executemany("INSERT OR REPLACE INTO uso_tabela_arquivo VALUES(?,?,?)",
                             [(nome, t, n) for t, n in uso.items() if n > 0])
            if i % 100 == 0 or i == len(arqs):
                print(f"{i}/{len(arqs)} arquivos, {len(agg)} pares de join, {time.time()-t0:.0f}s", flush=True)
    lite.executemany(
        "INSERT INTO joins_observados VALUES(?,?,?,?,?,?,?)",
        [(*k, v[0], len(set(v[1])), ",".join(sorted(set(v[1]))[:5])) for k, v in agg.items()])
    lite.commit()
    lite.close()
    print(f"ok: {len(agg)} pares de colunas; {len(erros)} arquivos com erro; {time.time()-t0:.0f}s")
    for e in erros[:5]:
        print("  erro:", e)


if __name__ == "__main__":
    main(sys.argv[1:] or [r"C:\Contabil"])
