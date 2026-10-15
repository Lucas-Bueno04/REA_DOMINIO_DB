"""Fase 2/3: extrai o corpus de SQL embutido nos executáveis/.pbd da Domínio.

Os DataWindows/scripts do PowerBuilder ficam como texto dentro dos .pbd, em blocos de
512 bytes com cabeçalho 'DAT*' (10 bytes). Remove-se o cabeçalho para reunir strings
quebradas entre blocos e extraem-se os trechos SELECT ... FROM ... .

Saída: data/raw/sql_corpus.jsonl  (uma linha por SQL: arquivo, sql)
Uso:   python src/extractor/corpus_sql.py [pasta ...]   (padrão: C:\\Contabil)
"""
import hashlib
import json
import pathlib
import re
import sys
import time

RAIZ = pathlib.Path(__file__).resolve().parents[2]
SAIDA = RAIZ / "data" / "raw" / "sql_corpus.jsonl"

# trecho "imprimível": ASCII + latin-1 acentuado + quebras de linha/tab
RUN = re.compile(rb"[\x09\x0a\x0d\x20-\x7e\xc0-\xff]{30,}")
SELECT_FROM = re.compile(rb"(?is)\bselect\b.{3,}?\bfrom\b")
# PowerBuilder Unicode (12.x): texto em UTF-16LE (caractere + \x00)
RUN16 = re.compile(rb"(?:[\x09\x0a\x0d\x20-\x7e\xc0-\xff]\x00){30,}")
SELECT_FROM16 = re.compile(r"(?is)\bselect\b.{3,}?\bfrom\b")


def cadeias(b: bytes):
    """Reconstrói os objetos seguindo a cadeia de blocos DAT*.

    Bloco: 'DAT*'(4) + próximo bloco (int32, deslocamento absoluto; 0 = fim) + tamanho útil (uint16) + dados.
    Devolve um bytes por objeto (cabeça de cadeia = bloco que ninguém aponta).
    """
    n = len(b)
    prox, tam, alvos = {}, {}, set()
    for off in range(0, n - 10, 512):
        if b[off:off + 4] == b"DAT*":
            nx = int.from_bytes(b[off + 4:off + 8], "little", signed=True)
            prox[off] = nx
            tam[off] = min(int.from_bytes(b[off + 8:off + 10], "little"), 502)
            if nx > 0:
                alvos.add(nx)
    for cab in prox:
        if cab in alvos:
            continue
        partes, off, guarda = [], cab, 0
        while off in prox and guarda < 100000:
            partes.append(b[off + 10: off + 10 + tam[off]])
            off = prox[off]
            guarda += 1
            if off <= 0:
                break
        yield b"".join(partes)


def extrair(arq: pathlib.Path):
    dados = arq.read_bytes()
    visto = set()
    for buf in list(cadeias(dados)) + [dados]:
        candidatos = []
        for m in RUN.finditer(buf):
            r = m.group(0)
            if SELECT_FROM.search(r):
                try:
                    candidatos.append(r.decode("cp1252"))
                except UnicodeDecodeError:
                    candidatos.append(r.decode("latin-1"))
        for m in RUN16.finditer(buf):
            s16 = m.group(0).decode("utf-16-le", "ignore")
            if SELECT_FROM16.search(s16):
                candidatos.append(s16)
        for s in candidatos:
            s = re.sub(r"\s+", " ", s).strip()
            h = hashlib.md5(s.encode("utf-8", "ignore")).hexdigest()
            if h in visto:
                continue
            visto.add(h)
            yield s


def main(pastas: list[str]) -> None:
    t0 = time.time()
    arqs = []
    for p in pastas:
        pp = pathlib.Path(p)
        arqs += [f for f in pp.rglob("*") if f.is_file() and f.suffix.lower() in (".pbd", ".exe")]
    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    total = 0
    globais = set()
    with SAIDA.open("w", encoding="utf-8") as out:
        for i, f in enumerate(sorted(arqs), 1):
            n = 0
            for s in extrair(f):
                h = hashlib.md5(s.encode("utf-8", "ignore")).hexdigest()
                if h in globais:
                    continue
                globais.add(h)
                out.write(json.dumps({"arquivo": f.name, "sql": s}, ensure_ascii=False) + "\n")
                n += 1
            total += n
            if i % 100 == 0 or i == len(arqs):
                print(f"{i}/{len(arqs)} arquivos, {total} SQLs, {time.time()-t0:.0f}s", flush=True)
    print(f"ok -> {SAIDA}")


if __name__ == "__main__":
    main(sys.argv[1:] or [r"C:\Contabil"])
