"""Procura no catálogo colunas/tabelas que possam guardar segredos (senha, token, certificado, chave privada)."""
import pathlib, re, sqlite3
d = sqlite3.connect(pathlib.Path(__file__).resolve().parents[1] / "data/catalog/dominio_catalog.db")
PAD = re.compile(r"(?i)(senha|password|passwd|pwd|token|secret|segredo|certificad|pfx|chave_priv|private|cripto|hash|api_key|apikey|client_secret|credencial)")
achados = {}
for t, c, tp, lin, com in d.execute("""select c.tabela, c.nome, c.tipo, t.linhas, c.comentario from colunas c join tabelas t on t.table_id=c.table_id
                                       where t.tipo='BASE' and t.legivel=1 and t.na_lista_gerador=1"""):
    if PAD.search(c) or PAD.search(com or ""):
        achados.setdefault(t, []).append((c, tp, lin))
print(f"{len(achados)} tabelas legíveis com coluna suspeita:\n")
for t, cs in sorted(achados.items(), key=lambda x: -(x[1][0][2] or 0)):
    print(f"{t:<46}{cs[0][2] or 0:>10,} linhas  colunas: {', '.join(c for c, _, _ in cs[:5])}".replace(",", "."))
