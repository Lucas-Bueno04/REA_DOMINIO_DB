"""Exporta o grafo de relações (exports/grafo.json) e gera o relatório docs/relacionamentos.md.

Uso: python src/model/exportar_grafo.py
"""
import collections
import json
import pathlib
import sqlite3

RAIZ = pathlib.Path(__file__).resolve().parents[2]
DB = RAIZ / "data" / "catalog" / "dominio_catalog.db"


def main() -> None:
    d = sqlite3.connect(DB)
    d.row_factory = sqlite3.Row
    q = lambda s, *a: d.execute(s, a).fetchall()

    tabs = {r["nome"]: dict(depto=r["departamento"], linhas=r["linhas"], legivel=r["legivel"], desc=r["comentario"])
            for r in q("select nome, departamento, linhas, legivel, comentario from tabelas where tipo='BASE'")}
    rels = []
    for r in q("select id, filha, pai, tipo, origens, confianca, ocorrencias, arquivos, role from relacoes where tipo<>'temporaria'"):
        cols = [[c["col_filha"], c["col_pai"]] for c in q("select col_filha, col_pai from relacao_colunas where relacao_id=?", r["id"])]
        rels.append(dict(filha=r["filha"], pai=r["pai"], tipo=r["tipo"], origens=r["origens"].split(","),
                         confianca=r["confianca"], ocorrencias=r["ocorrencias"], arquivos=r["arquivos"],
                         role=r["role"], colunas=cols))
    out = RAIZ / "exports" / "grafo.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps({"tabelas": tabs, "relacoes": rels}, ensure_ascii=False), encoding="utf-8")
    print(f"grafo.json: {len(tabs)} tabelas, {len(rels)} relações ({out.stat().st_size/1e6:.1f} MB)")

    # --- relatório
    L = ["# Relacionamentos (Fase 2)", "",
         "Gerado por `src/model/exportar_grafo.py` a partir de `data/catalog/dominio_catalog.db`.", "",
         "## Fontes e confiança", "",
         "| Origem | Descrição | Confiança |", "|---|---|---|",
         "| declarada | FK criada no banco | 1,0 |",
         "| observada | igualdade `A.col = B.col` minerada dos executáveis/.pbd da Domínio, validada contra o catálogo | 0,5 a 0,9 (pelo nº de usos) |",
         "| inferida | filha contém toda a chave do pai **e** o nome começa com o do pai (`EFMVSPRO_*` → `efmvspro`); "
         "precisão medida contra as FKs declaradas: ~72% (sem a regra de nome: 17%) | 0,6 |", "",
         "Tipos: `fk` (chave completa), `vigencia` (ligação por período, tabelas `*_vigencia`), "
         "`ligacao` (colunas em comum sem chave completa de nenhum lado), `temporaria` (`eftmp_*`, fora do grafo).", "",
         "## Resumo", "", "| Origens | Tipo | Relações | Confiança média |", "|---|---|---|---|"]
    for r in q("select origens, tipo, count(*) n, round(avg(confianca),2) c from relacoes group by 1,2 order by 3 desc"):
        L.append(f"| {r['origens']} | {r['tipo']} | {r['n']} | {r['c']} |")

    L += ["", "## Cobertura por departamento (tabelas base legíveis)", "",
          "| Departamento | Tabelas | Com relação | % |", "|---|---|---|---|"]
    for r in q("""select t.departamento dp, count(*) n,
                         sum(exists(select 1 from relacoes x where x.tipo<>'temporaria' and (lower(x.filha)=t.nome_lower or lower(x.pai)=t.nome_lower))) c
                    from tabelas t where t.tipo='BASE' and t.legivel=1 group by 1 order by 2 desc"""):
        L.append(f"| {r['dp']} | {r['n']} | {r['c']} | {100*r['c']/r['n']:.0f}% |")

    L += ["", "## Tabelas mais referenciadas (como pai)", "", "| Tabela | Filhas | Descrição |", "|---|---|---|"]
    for r in q("""select r.pai, count(distinct r.filha) n, t.comentario from relacoes r join tabelas t on t.nome_lower=lower(r.pai)
                   where r.tipo<>'temporaria' and r.confianca>=0.7 group by r.pai order by n desc limit 30"""):
        L.append(f"| {r['pai']} | {r['n']} | {(r['comentario'] or '')[:70]} |")

    L += ["", "## Relações usadas pela Domínio e NÃO declaradas como FK (mais frequentes)", "",
          "| Filha | Pai | Colunas (filha → pai) | Usos | Programas | Tipo |", "|---|---|---|---|---|---|"]
    for r in q("""select id, filha, pai, tipo, ocorrencias, arquivos from relacoes
                   where origens='observada' and tipo in ('fk','ligacao','vigencia') order by ocorrencias desc limit 40"""):
        cs = ", ".join(f"{c['col_filha']}→{c['col_pai']}" for c in q("select col_filha, col_pai from relacao_colunas where relacao_id=? limit 4", r["id"]))
        L.append(f"| {r['filha']} | {r['pai']} | {cs} | {r['ocorrencias']} | {r['arquivos']} | {r['tipo']} |")

    L += ["", "## Tabelas base sem nenhuma relação", ""]
    sem = [r["nome"] for r in q("""select nome from tabelas t where tipo='BASE' and legivel=1 and not exists
                  (select 1 from relacoes x where x.tipo<>'temporaria' and (lower(x.filha)=t.nome_lower or lower(x.pai)=t.nome_lower)) order by nome""")]
    L.append(f"{len(sem)} tabelas (lista completa em `exports/tabelas_sem_relacao.txt`).")
    (RAIZ / "exports" / "tabelas_sem_relacao.txt").write_text("\n".join(sem), encoding="utf-8")
    (RAIZ / "docs" / "relacionamentos.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("docs/relacionamentos.md gerado")


if __name__ == "__main__":
    main()
