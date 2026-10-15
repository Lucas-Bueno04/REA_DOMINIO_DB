"""Lista colunas do modelo quase vazias / com valor-padrão, usando perfil_colunas.
Uso: python scripts/analisar_perfil.py [limite_%=1] [modulo ...]      (padrão: fiscal)
Colunas com `dominio` são códigos: zero é valor legítimo e não conta como vazio."""
import pathlib, sqlite3, sys, yaml
RAIZ = pathlib.Path(__file__).resolve().parents[1]
lim = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
mods = sys.argv[2:] or ["fiscal"]
d = sqlite3.connect(RAIZ / "data/catalog/dominio_catalog.db")
perfil = {(t, c): (tp, n, nn, br or 0, ze or 0, se or 0, mn, mx)
          for t, c, tp, n, nn, br, ze, se, mn, mx in d.execute("select tabela,coluna,tipo,linhas,nao_nulos,em_branco,zeros,sentinela,minimo,maximo from perfil_colunas")}
for arq in [RAIZ / "src/model/modulos" / f"{m}.yaml" for m in mods]:
    y = yaml.safe_load(arq.read_text(encoding="utf-8"))
    for nome, e in y["entidades"].items():
        t = e["tabela"].lower()
        ruins = []
        for api, v in e["colunas"].items():
            c = (v["coluna"] if isinstance(v, dict) else v).lower()
            codigo = isinstance(v, dict) and bool(v.get("dominio"))
            p = perfil.get((t, c))
            if not p:
                continue
            tp, n, nn, br, ze, se, mn, mx = p
            if not n:
                continue
            uteis = nn - br - se - (0 if codigo else ze)       # preenchidos com valor "de verdade"
            pct = 100 * uteis / n
            if pct < lim:
                motivo = "sentinela 1900-01-01" if se / n > .5 else "zerada" if ze / n > .5 else "em branco" if br / n > .5 else "nula"
                ruins.append(f"{api}({c}) {pct:.2f}% [{motivo}]")
        if ruins:
            print(f"{nome} ({e['tabela']}):\n   " + "\n   ".join(ruins))
