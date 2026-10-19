"""Gera docs/funcoes.md a partir do catálogo FUNCOES de src/server/consultas.py (nome, descrição, parâmetros, fontes e como foi validada).
É a especificação para mapear as funções em ferramentas MCP. Uso: python scripts/gerar_docs_funcoes.py"""
import pathlib, sys
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from server.consultas import FUNCOES

L = ["# Funções de consulta (`src/server/consultas.py`)", "",
     "Gerado por `scripts/gerar_docs_funcoes.py` a partir do catálogo `FUNCOES`. Todas são **somente leitura**, recebem o `Motor` e devolvem dicionário JSON-seguro; "
     "ainda **não estão registradas como ferramentas MCP** (decisão do dono do projeto): para registrar, basta expor `FUNCOES[nome][\"executar\"]` em `src/server/mcp_server.py`.", "",
     f"{len(FUNCOES)} funções.", "", "| Função | Para quê | Parâmetros |", "|---|---|---|"]
for nome, f in FUNCOES.items():
    ps = ", ".join(f"`{k}`" for k in f["parametros"])
    L.append(f"| `{nome}` | {f['descricao']} | {ps} |")
L.append("")
for nome, f in FUNCOES.items():
    L += [f"## `{nome}`", "", f["descricao"], "", "**Parâmetros:**"] + [f"- `{k}`: {v}" for k, v in f["parametros"].items()]
    L += ["", "**Fontes:** " + ", ".join(f"`{x}`" for x in f["fontes"]), "", f"**Validação:** {f['validada']}", ""]
(RAIZ / "docs" / "funcoes.md").write_text("\n".join(L), encoding="utf-8")
print(f"docs/funcoes.md: {len(FUNCOES)} funções")
