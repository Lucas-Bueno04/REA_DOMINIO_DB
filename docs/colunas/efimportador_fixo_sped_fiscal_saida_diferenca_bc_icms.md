# EFIMPORTADOR_FIXO_SPED_FISCAL_SAIDA_DIFERENCA_BC_ICMS — Configuração do leiaute SPED Fiscal do Importador Fixo - Saída - Diferença entre valor contábil e base de cálculo ICMS
8.148 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_DIFERENCA | integer(4) | PK |  | Sequencial da diferença |
| CST | integer(4) |  |  | Código do CST |
| DEFINICAO | char(1) |  |  | Definição da diferença |
| SELECAO_ESPECIE | char(1) |  |  |  |
| I_SEQUENCIAL_CST | integer(4) |  |  | Chave sequencial do CST |
| DETALHAMENTO_OUTROS_VALORES_MG | integer(4) |  | S | MG - Detalhamento de outros valores |
