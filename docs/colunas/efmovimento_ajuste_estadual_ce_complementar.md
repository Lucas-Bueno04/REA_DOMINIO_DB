# EFMOVIMENTO_AJUSTE_ESTADUAL_CE_COMPLEMENTAR — CE - Ajuste Impostos lançados estaduais - Complementar
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_AJUSTE | integer(4) | PK |  | Sequencial do movimento do ajuste |
| CODIGO_ESPECIE | integer(4) |  | S | Código da espécie |
| NUMERO_DAE | numeric(15) |  | S | Número da DAE |
| NUMERO_IDA | numeric(15) |  | S | Numero da IDA |
| DESCRICAO | varchar(100) |  | S | Descrição |
| CODIGO_RECEITA | varchar(6) |  | S | Código de receita |
| I_RECOLHIMENTO | integer(4) |  | S | Sequencial do código do recolhimento |
| DATA_VENCIMENTO | date(4) |  | S | Data de vencimento |
