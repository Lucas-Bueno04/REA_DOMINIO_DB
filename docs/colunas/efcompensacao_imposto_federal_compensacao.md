# EFCOMPENSACAO_IMPOSTO_FEDERAL_COMPENSACAO — Compensações de Impostos Federais - Compensação
135 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_COMPENSACAO | integer(4) | PK |  | Sequencial da compensação |
| I_COMPENSACAO_SEQUENCIAL | integer(4) | PK |  | Sequencial |
| CODI_IMP | integer(4) |  |  | Imposto |
| COMPETENCIA | date(4) |  |  | Competência |
| PARCELA | integer(4) |  | S | Parcela |
| VENCIMENTO | date(4) |  | S | Vencimento |
| VALOR_EM_ABERTO | numeric(13) |  |  | Valor em aberto |
| VALOR_COMPENSACOES | numeric(13) |  |  | Valor compensações |
| VALOR_PARCELA | numeric(13) |  |  | Valor parcela |
| I_RECOLHIMENTO | integer(4) |  | S | Sequencial do Recolhimento |
| PERIODICIDADE | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| I_CNO | integer(4) |  | S | Código CNO |
| VALOR_JUROS | numeric(13) |  |  | Valor de Juros |
| VALOR_MULTA | numeric(13) |  |  | Valor de Multa |
