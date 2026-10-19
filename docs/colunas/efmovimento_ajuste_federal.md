# EFMOVIMENTO_AJUSTE_FEDERAL — Ajuste Impostos lançados federais - Geral
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_AJUSTE | integer(4) | PK |  | Sequencial do movimento do ajuste |
| DATA_AJUSTE | date(4) |  |  | Data |
| CODI_AJU | integer(4) |  |  | Código do ajuste |
| VALOR | numeric(13) |  |  | Valor |
| OBSERVACAO | varchar(250) |  | S | Observação |
| I_RECOLHIMENTO | integer(4) |  | S | Sequencial do código de recolhimento |
| CODIGO_RECEITA | char(8) |  | S | Código de receita |
| ORIGEM_CREDITO | char(1) |  | S | Origem do credito (I-interno/E-externo) |
| CODIGO_AJUSTE_SPED | char(8) |  | S | Código do ajuste do SPED |
