# Plataforma de progresso do mapeamento

Painel web local para ver **o que já foi mapeado e o que falta** no banco do Sistema Domínio, e continuar o trabalho aos poucos.

- Iniciar: `executar_plataforma.cmd` (abre http://127.0.0.1:8800). Código: `src/plataforma/` (`dados.py` núcleo, `servidor.py` HTTP, `web/index.html` interface).
- Escuta **somente em 127.0.0.1**, recusa `Host`/`Origin` que não sejam locais, sem dependências externas na interface.
- Não altera o banco Domínio. Só lê (e apenas agregados, no teste de rascunho). As únicas gravações são: `data/progresso.db` (marcações, notas, histórico, snapshots, rascunhos), `data/rascunhos/` e, na promoção, `src/model/modulos/`.

## Como o status é calculado
Cada uma das 4.727 tabelas legíveis tem um status, em ordem de precedência:

| Status | Origem |
|---|---|
| Bloqueada | tabela com credenciais em `config/seguranca.yaml` (nunca vira entidade) |
| Validada | está numa entidade que tem `regras` de negócio conferidas |
| Modelada | está numa entidade curada |
| Apoio | só aparece como vínculo de outra entidade |
| Ignorada | marcação manual (baixo valor) |
| Em análise | marcação manual |
| Vazia | 0 linhas hoje (a Domínio pode usar mais tarde; reavalie ao regenerar o catálogo) |
| Não iniciada | o resto |

"Validada" **é derivada de a entidade ter `regras`**, não de uma conferência feita pela plataforma.

## Abas
- **Painel**: barra segmentada por status, progresso por medida (tabelas ≥ 1.000 linhas, relevantes, linhas cobertas, colunas expostas), evolução diária, por departamento, próximas da fila.
- **Mosaico**: uma célula por tabela, agrupada por departamento e família; filtros de status, tamanho, busca e priorizadas.
- **Fila de trabalho**: pontuação = 2·log10(linhas) + programas/6 + relações/8 (−2,5 se < 1.000 linhas, +10 se priorizada).
- **Famílias**, **Histórico**.
- **Gaveta da tabela**: Resumo (marcar, priorizar, notas), Colunas (status derivado + marcação sua), Relações, Mapear.

## Fluxo para mapear uma tabela
1. Abra a tabela (fila ou mosaico) → aba **Mapear**.
2. **Gerar rascunho**: monta o YAML com colunas escolhidas, domínios extraídos dos comentários (marcados `confirmado: parcial`), vínculos sugeridos pelas FKs declaradas e filtros. Colunas "SEM USO" e credenciais ficam de fora.
3. Revise/edite → **Salvar** → **Validar** (confere tabelas, colunas, junções, domínios contra o catálogo) → **Testar no banco** (tempo, multiplicação de linhas, % de preenchimento; só agregados).
4. **Promover**: grava `src/model/modulos/<módulo>__<entidade>.yaml`. **Reinicie o servidor MCP** para a entidade aparecer; rode `pytest` e `scripts/testar_entidades.py`.
5. Escreva as `regras` de negócio **só depois de conferir com dados reais**.

## Limites
- Promover não significa validar: a entidade nasce sem regras; o status só vira "Validada" quando as regras forem escritas e conferidas.
- Os domínios extraídos de comentários são hipóteses (`confirmado: parcial`).
- A API é serializada por um lock (uso de uma pessoa); não há autenticação, portanto use só em 127.0.0.1.
- Testes: `tests/test_plataforma.py` (usa diretórios temporários; não polui os modelos reais).
