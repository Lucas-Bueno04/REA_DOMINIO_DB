"""Pós-processamento dos módulos gerados em lote (idempotente):
 1. remove colunas de texto que identificam certificado digital (a regra do projeto é credencial nunca sair);
 2. marca `sensivel: parcial` em colunas de texto/identificador com dado pessoal (CPF/CNPJ, inscrição, e-mail, telefone, endereço).
Uso: python scripts/marcar_sensiveis.py            (todos os arquivos "Gerado em lote")
"""
import pathlib, re, sqlite3, sys
import yaml

RAIZ = pathlib.Path(__file__).resolve().parents[1]
MODULOS = RAIZ / "src" / "model" / "modulos"
d = sqlite3.connect(RAIZ / "data/catalog/dominio_catalog.db")
cat = {(r[0].lower(), r[1].lower()): (r[2], r[3] or "") for r in d.execute("select tabela, nome, tipo, comentario from colunas")}
PESSOAL = re.compile(r"cnpj|cpf|inscri[cç]|e-?mail|telefone|\bfone\b|endere[cç]o|logradouro|bairro|\bcep\b|raz[aã]o", re.I)
CERT = re.compile(r"certificad", re.I)
# só em tabelas do departamento Pessoal (folha, ponto, eSocial): dado pessoal/saúde e valores de remuneração
PESSOAL_P = re.compile(r"nascim|cid|defici|ra[cç]a|etnia|estado civil|sexo|pis|pasep|ctps|eleitor|m[aã]e|pai|c[oô]njuge|dependente|atestado|doen[cç]a|nome do (empregado|funcion|dependente|s[oó]cio|aut[oô]nomo|contribuinte)|rg|identidade|cnh|passaporte|biometr|foto", re.I)
FINANC_P = re.compile(r"sal[aá]rio|remunera|proventos|vencimento|l[ií]quido|valor (bruto|do evento|pago)|pens[aã]o|rescis", re.I)
dep = {r[0].lower(): r[1] for r in d.execute("select nome, departamento from tabelas")}


def main():
    marc = rem = 0
    for arq in sorted(MODULOS.glob("*.yaml")):
        txt = arq.read_text(encoding="utf-8")
        if "Gerado em lote" not in txt[:200]:
            continue
        cab = txt.split("\nmodulo:", 1)[0]
        y = yaml.safe_load(txt); mudou = False
        for nome, e in y["entidades"].items():
            t = e["tabela"].lower()
            for api, v in list(e["colunas"].items()):
                col = (v["coluna"] if isinstance(v, dict) else v)
                tipo, com = cat.get((t, col.lower()), ("", ""))
                if CERT.search(col) and tipo in ("varchar", "char") and (d.execute("select tamanho from colunas where tabela=? collate nocase and nome=? collate nocase", (e["tabela"], col)).fetchone() or [0])[0] > 1:
                    del e["colunas"][api]; rem += 1; mudou = True
                    for f in [k for k, fv in e.get("filtros", {}).items() if fv["coluna"] == col]:
                        del e["filtros"][f]
                    continue
                if dep.get(t) == "Pessoal" and not (isinstance(v, dict) and v.get("sensivel")):
                    nivel = "financeiro" if (FINANC_P.search(col + " " + com) and tipo in ("numeric", "decimal", "integer")) else                             "pessoal" if (PESSOAL_P.search(col + " " + com) and tipo in ("varchar", "char", "date")) else None
                    if nivel:
                        e["colunas"][api] = {**(v if isinstance(v, dict) else {"coluna": v}), "sensivel": nivel}
                        marc += 1; mudou = True; v = e["colunas"][api]
                if PESSOAL.search(col + " " + com) and tipo in ("varchar", "char", "integer", "numeric", "decimal", "bigint"):
                    if tipo in ("integer", "numeric", "decimal", "bigint") and not re.search(r"cnpj|cpf|inscri", col + " " + com, re.I):
                        continue
                    if not (isinstance(v, dict) and v.get("sensivel")):
                        e["colunas"][api] = {**(v if isinstance(v, dict) else {"coluna": v}), "sensivel": "parcial"}
                        marc += 1; mudou = True
        if mudou:
            arq.write_text(cab + "\n" + yaml.safe_dump(y, allow_unicode=True, sort_keys=False, width=160, default_flow_style=None), encoding="utf-8")
    print(f"{marc} colunas marcadas como sensivel; {rem} colunas de certificado removidas")


if __name__ == "__main__":
    main()
