"""Pós-processamento dos módulos gerados em lote (idempotente): em tabelas com 100 mil linhas ou mais, garante que alguma coluna
OBRIGATÓRIA (empresa ou `exige_algum`) lidere um índice, para a consulta nunca varrer a tabela inteira.
Cria os filtros das colunas líderes de índice (PK/únicos primeiro, até 3) e os torna `exige_algum`.
Uso: python scripts/proteger_acesso.py
"""
import pathlib, sqlite3
import yaml

RAIZ = pathlib.Path(__file__).resolve().parents[1]
MODULOS = RAIZ / "src" / "model" / "modulos"
d = sqlite3.connect(RAIZ / "data/catalog/dominio_catalog.db")
LIM = 100_000


def lideres(t):
    """colunas (minúsculas) que lideram algum índice, únicos primeiro"""
    out = []
    for r in d.execute("select colunas, unico from indices where lower(tabela)=? order by unico desc", (t,)):
        c = r[0].split(",")[0].strip().lower()
        if c not in out:
            out.append(c)
    return out


def main():
    mod = prot = 0
    for arq in sorted(MODULOS.glob("*.yaml")):
        txt = arq.read_text(encoding="utf-8")
        if "Gerado em lote" not in txt[:200]:
            continue
        cab = txt.split("\nmodulo:", 1)[0]
        y = yaml.safe_load(txt); mudou = False
        for nome, e in y["entidades"].items():
            t = e["tabela"].lower()
            linhas = (d.execute("select linhas from tabelas where nome_lower=?", (t,)).fetchone() or [0])[0] or 0
            if linhas < LIM:
                continue
            ac = e.setdefault("acesso", {})
            emp = (ac.get("empresa") or "").lower()
            lid = lideres(t)
            obrig = {emp} if emp else set()
            for x in ac.get("exige_algum", []):
                if x == "periodo":
                    per = ac.get("periodo")
                    if isinstance(per, str):
                        obrig.add(per.lower())
                elif x in e.get("filtros", {}) and isinstance(e["filtros"][x]["coluna"], str):
                    obrig.add(e["filtros"][x]["coluna"].lower())
            if obrig & set(lid):
                continue
            expostas = {(v["coluna"] if isinstance(v, dict) else v).lower(): api for api, v in e["colunas"].items()}
            cand = [c for c in lid if c in expostas and c != emp][:3]
            if not cand:
                continue
            e.setdefault("filtros", {})
            nomes = list(ac.get("exige_algum", []))
            for c in cand:
                fn = next((k for k, f in e["filtros"].items() if isinstance(f["coluna"], str) and f["coluna"].lower() == c), None)
                if not fn:
                    tipo = (d.execute("select tipo from colunas where tabela=? collate nocase and nome=? collate nocase", (e["tabela"], c)).fetchone() or [""])[0]
                    fn = expostas[c]
                    e["filtros"][fn] = {"coluna": next(v["coluna"] if isinstance(v, dict) else v for v in e["colunas"].values() if (v["coluna"] if isinstance(v, dict) else v).lower() == c),
                                        "ops": ["eq", "entre", "gte", "lte"] if tipo == "date" else ["eq", "in"]}
                if fn not in nomes:
                    nomes.append(fn)
            ac["exige_algum"] = nomes
            if linhas >= 1_000_000:
                ac["volume"] = "grande"
            mudou = True; prot += 1
        if mudou:
            mod += 1
            arq.write_text(cab + "\n" + yaml.safe_dump(y, allow_unicode=True, sort_keys=False, width=160, default_flow_style=None), encoding="utf-8")
    print(f"{prot} entidades protegidas em {mod} arquivos")


if __name__ == "__main__":
    main()
