# REA_DOMINIO_DB

Projeto para mapear o banco do Sistema Domínio (SQL Anywhere 17, banco `Contabil`) por engenharia reversa e expô-lo como servidor **MCP somente leitura**, com consulta, filtro e paginação.

- **Mapa visual do que foi mapeado:** [`exports/modelo_relacional.html`](exports/modelo_relacional.html) (abrir no navegador; regenerar com `python src/model/gerar_visual.py`)
- **Usar o servidor MCP:** [`docs/uso-mcp.md`](docs/uso-mcp.md) (lançador: `executar_servidor.cmd`; testes: `python -m pytest`)
- **Funções de consulta nomeadas** (futuras ferramentas MCP): [`docs/funcoes.md`](docs/funcoes.md) · código em `src/server/consultas.py`
- **Biblioteca de tools MCP** (uma ou mais por tabela, uma pasta por módulo, validada contra o banco): [`docs/biblioteca.md`](docs/biblioteca.md) · catálogo em [`docs/biblioteca/`](docs/biblioteca/README.md) · código em `src/biblioteca/` · acompanhamento na aba “Biblioteca de tools” da plataforma
- Estado do mapeamento: 2.117 entidades cobrem 99,99% das linhas do banco (≈ 90 tabelas curadas e conciliadas à mão, o resto gerado em lote e medido); ver `STATUS.md` e o painel (`executar_plataforma.cmd`)
- Plano completo: [`PLANO.md`](PLANO.md)
- Andamento: [`STATUS.md`](STATUS.md)
- Descobertas já obtidas: [`docs/descobertas-rea.md`](docs/descobertas-rea.md)
- Relacionamentos entre tabelas: [`docs/relacionamentos.md`](docs/relacionamentos.md)
- Modelo de entidades: [Fiscal](docs/modelo-fiscal.md) · [Contábil](docs/modelo-contabil.md) · [Folha](docs/modelo-folha.md) · [Honorários](docs/modelo-honorarios.md) · [Geral](docs/modelo-geral.md) · [EFD-Reinf](docs/modelo-reinf.md) · [CF-e](docs/modelo-cfe.md) · [Contab. referencial](docs/modelo-referencial.md) · [SPED ECF](docs/modelo-sped_ecf.md) · [Empresa](docs/modelo-comum.md) (formato em [`docs/formato-modelo.md`](docs/formato-modelo.md))

## Estrutura
| Pasta | Conteúdo |
|---|---|
| `config/` | `.env.example` (copiar para `.env`, que não vai ao git) |
| `docs/` | descobertas, modelo por módulo, uso do MCP |
| `sql/` | consultas SQL extraídas do gerador e consultas de catálogo |
| `scripts/` | utilitários (extração de strings dos `.pbd`, consulta somente leitura) |
| `data/raw/` | material bruto (inventário, strings extraídas) |
| `data/catalog/` | catálogo SQLite gerado (estrutura, sem dados de clientes) |
| `src/extractor` · `src/model` · `src/server` · `src/biblioteca` | extração do catálogo, modelo relacional, servidor MCP, biblioteca de tools por tabela |
| `tests/` | testes |
| `exports/` | grafos, diagramas, dicionários exportados |

## Regras
1. Somente leitura (SELECT).
2. Credenciais só em `config/.env` ou variáveis de ambiente.
3. Dados de clientes não entram no catálogo nem no git.

## Como usar o utilitário de consulta (somente leitura)
```powershell
$env:DOM_UID = '<usuario>'; $env:DOM_PWD = '<senha>'
.\scripts\consulta_readonly.ps1 -Sql "SELECT COUNT(*) FROM bethadba.geempre"
```
O script recusa qualquer comando que não seja `SELECT`/`WITH` e sempre desfaz a transação.


## Plataforma de progresso do mapeamento
`executar_plataforma.cmd` abre o painel visual (http://127.0.0.1:8800) com o que já foi mapeado, o que falta e a fila do que atacar a seguir; permite gerar, validar, testar e promover rascunhos de entidades. Ver `docs/plataforma.md`.