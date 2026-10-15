import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
from extractor.corpus_sql import cadeias, RUN16
b = pathlib.Path(sys.argv[1]).read_bytes()
alvo = sys.argv[2].encode("utf-16-le")
for obj in cadeias(b):
    i = obj.find(alvo)
    if i < 0:
        continue
    print("objeto de", len(obj), "bytes; achado em", i)
    runs = [(m.start(), m.end()) for m in RUN16.finditer(obj)]
    for k, (s, e) in enumerate(runs):
        if s <= i < e:
            for j in range(max(0, k - 3), min(len(runs), k + 4)):
                s2, e2 = runs[j]
                txt = obj[s2:e2].decode("utf-16-le", "ignore")
                gap = obj[runs[j-1][1]:s2] if j > 0 else b""
                print(f"\n[run {j}] gap_antes={gap[:24]!r} (len {len(gap)}) tamanho_run={e2-s2}\n   inicio: {txt[:70]!r}\n   fim:    {txt[-70:]!r}")
            break
    break
