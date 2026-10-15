"""Mostra as relações de uma ou mais tabelas.  Uso: python scripts/ver_relacoes.py ctcontas [outra ...]"""
import os, sqlite3, sys, pathlib
d = sqlite3.connect(pathlib.Path(__file__).resolve().parents[1] / "data/catalog/dominio_catalog.db")
for t in sys.argv[1:]:
    print(f"[{t}]")
    rows = d.execute("""select r.filha, r.pai, r.tipo, r.origens, r.confianca, r.ocorrencias,
            (select group_concat(col_filha||'->'||col_pai) from (select * from relacao_colunas c where c.relacao_id=r.id limit 3))
            from relacoes r where (lower(r.filha)=lower(?) or lower(r.pai)=lower(?)) and r.tipo<>'temporaria'
            order by r.confianca desc, r.ocorrencias desc limit ?""", (t, t, int(os.environ.get("LIM", 14)))).fetchall()
    for f, p, tp, o, c, n, cols in rows:
        lado = f"pai de {f}" if p.lower() == t.lower() else f"filha de {p}"
        print(f"  {lado:<48} {tp:<8} {o:<20} conf={c:<4} usos={n:<6} {cols}")
