"""Procura colunas por padrão no nome/comentário dentro de uma tabela (catálogo + perfil).
Uso: python scripts/procurar_colunas.py tabela padrao [padrao ...]     (tabela pode ser um padrão LIKE, ex.: 'ct%')"""
import pathlib, sqlite3, sys
d = sqlite3.connect(pathlib.Path(__file__).resolve().parents[1] / "data/catalog/dominio_catalog.db")
t = sys.argv[1]
for pad in sys.argv[2:]:
    if "%" in t:    # várias tabelas: lista só as primeiras correspondências
        for tab, n, c in d.execute("""select tabela, nome, comentario from colunas where tabela like ? and (nome like ? or comentario like ?)
                                      and tabela not like '%SPED%' and tabela not like '%\\_REF%' escape '\\' order by tabela, ordem limit 40""", (t, f"%{pad}%", f"%{pad}%")):
            print(f"{tab:<34}{n:<36}{(c or '-')[:60]}")
        continue
    for n, tp, c, linhas, nn, br, ze, se in d.execute("""select c.nome, c.tipo, c.comentario, p.linhas, p.nao_nulos, p.em_branco, p.zeros, p.sentinela
            from colunas c left join perfil_colunas p on p.tabela=lower(c.tabela) and p.coluna=lower(c.nome)
            where c.tabela=? collate nocase and (c.nome like ? or c.comentario like ?) order by c.ordem""", (t, f"%{pad}%", f"%{pad}%")):
        uso = "" if not linhas else f"útil={100*((nn or 0)-(br or 0)-(ze or 0)-(se or 0))/linhas:.1f}%"
        print(f"{t}.{n:<30}{tp:<10}{uso:<12}{c or ''}")
