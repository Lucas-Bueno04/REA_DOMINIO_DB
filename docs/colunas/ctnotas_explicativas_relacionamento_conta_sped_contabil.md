# CTNOTAS_EXPLICATIVAS_RELACIONAMENTO_CONTA_SPED_CONTABIL — Relacionamento de notas explicativas com o SPED contabil
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Codigo da empresa |
| I_RELACIONAMENTO | integer(4) | PK |  | Codigo do relacionamento |
| I_CONTA | integer(4) | PK |  | Codigo da conta contabil |
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| I_SCP | integer(4) |  | S | Código do SCP |
| NOTA_EXP_OBS_SCP | varchar(255) |  |  | Observação da nota explicativa relativa ao bloco J do SPED Contabil |
