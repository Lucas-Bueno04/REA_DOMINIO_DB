# CTEXTRATO_BANCARIO_CONFIGURACAO_ICEBERG_OUTROS — Outras configurações de lançamentos - encargos
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_TRANSACAO | decimal(20) | PK |  | tipo de transação |
| JUROS_CODI_CTA | integer(4) |  | S | codigo da conta designada a Juros |
| JUROS_CODI_HIS | integer(4) |  | S | codigo do historico designado a Juros |
| JUROS_HISTORICO | varchar(300) |  | S | codigo do historico designado a Juros |
| MULTA_CODI_CTA | integer(4) |  | S | codigo da conta designada a Multa |
| MULTA_CODI_HIS | integer(4) |  | S | codigo do historico designado a Multa |
| MULTA_HISTORICO | varchar(300) |  | S | codigo do historico designado a Multa |
| DESCONTO_CODI_CTA | integer(4) |  | S | codigo da conta designada a Desconto |
| DESCONTO_CODI_HIS | integer(4) |  | S | codigo do historico designado a Desconto |
| DESCONTO_HISTORICO | varchar(300) |  | S | codigo do historico designado a Desconto |
