# EFOUTROSDADOS_PLANEJAMENTO_TRIBUTARIO_CFOPS_CONSIDERADOS — Outros Dados - Planejamento Tributário - CFOPs considerados para o cálculo (debito e credito)
658 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| COMPETENCIA | date(4) | PK |  | Competência |
| I_INFORMATIVOS | integer(4) | PK |  | Informativo |
| TIPO | char(1) | PK |  | Tipo (D - Débito / C- Crédito) |
| I_SEQUENCIAL | integer(4) | PK |  | Sequencial |
| ATIVIDADE | integer(4) | PK |  | Atividade (1 - Comercio / 2 - Industria / 3 - Serviço) |
| CFOP_CONSIDERADO | integer(4) |  | S | CFOP_CONSIDERADO |
