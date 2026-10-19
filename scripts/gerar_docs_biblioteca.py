"""Gera docs/biblioteca/: README.md (índice por módulo) e um .md por módulo da biblioteca com as ferramentas (nome, tabela, parâmetros obrigatórios, status de validação).
Descrições completas só das ferramentas curadas / casos de uso (as geradas são montadas do modelo em tempo de carga e já estão em docs/modelo-*.md).
Somente leitura do banco (nem toca nele). Uso: python scripts/gerar_docs_biblioteca.py"""
import pathlib, sys
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from biblioteca import estado
from biblioteca.registro import carregar

DOCS = RAIZ / "docs" / "biblioteca"
SIMBOLO = {"validada": "✔", "falhou": "✘", "nao_validada": "·"}


def main():
    b = carregar()
    c = estado.abrir(); estado.sincronizar(c, b)
    st = {r["nome"]: r["status"] for r in c.execute("select nome, status from ferramenta")}
    DOCS.mkdir(parents=True, exist_ok=True)
    for f in DOCS.glob("*.md"):
        f.unlink()
    r = estado.resumo(c)
    idx = ["# Biblioteca de tools MCP do banco Domínio", "",
           "Uma ou mais ferramentas por tabela, organizadas em `src/biblioteca/<modulo>/<tabela>.py`, mais os casos de uso em `src/biblioteca/casos_de_uso/`. "
           "Tipos: **consultar** (filtros, ordenação, paginação), **obter** (um registro pela chave), **totais** (contagem e soma por grupo), **caso_de_uso** (regra de negócio entre várias tabelas).",
           "", "Gerado por `scripts/gerar_docs_biblioteca.py`. Status de validação: ✔ validada, ✘ falhou, · não validada. O acompanhamento ao vivo está na aba **Biblioteca de tools** da plataforma.", "",
           f"- Ferramentas: **{r['ferramentas']}** ({r['ferramentas_validadas']} validadas, {r['ferramentas_com_falha']} com falha)",
           f"- Tabelas com ferramenta: **{r['tabelas']}**", "", "| Módulo | Tabelas | Ferramentas | Validadas |", "|---|---:|---:|---:|"]
    for mod in sorted(b.por_modulo):
        fs = b.por_modulo[mod]
        nome = mod
        idx.append(f"| [{nome}]({nome}.md) | {len({t for f in fs for t in f.tabelas})} | {len(fs)} | {sum(1 for f in fs if st.get(f.nome) == 'validada')} |")
        out = [f"# Módulo `{mod}`", "", "| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |", "|---|---|---|---|---|"]
        for f in sorted(fs, key=lambda x: (x.tabelas[0] if x.tabelas else "", x.tipo)):
            out.append(f"| `{f.nome}` | {f.tipo} | {', '.join(f.tabelas)} | {', '.join(p.nome for p in f.parametros if p.obrigatorio) or '—'} | {SIMBOLO.get(st.get(f.nome, 'nao_validada'), '·')} |")
        for f in fs:
            if not f.gerada or f.tipo == "caso_de_uso":
                out += ["", f"## `{f.nome}`", "", f.descricao, "", "Parâmetros:", ""]
                out += [f"- `{p.nome}`{' (obrigatório)' if p.obrigatorio else ''}: {p.descricao}" for p in f.parametros]
        (DOCS / f"{mod}.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    (DOCS / "README.md").write_text("\n".join(idx) + "\n", encoding="utf-8")
    print(f"docs/biblioteca: {len(b.por_modulo)} módulos")


if __name__ == "__main__":
    main()
