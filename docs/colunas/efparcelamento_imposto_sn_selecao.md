# EFPARCELAMENTO_IMPOSTO_SN_SELECAO — Parcelamento de Impostos Simples Nacional - Seleção
12 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_PARCELAMENTO_SN | integer(4) | PK |  | Sequencial do parcelamento Simples Nacinal |
| I_PARCELAMENTO_SN_SELECAO | integer(4) | PK |  | Sequencial da seleção do parcelamento Simples Nacinal |
| COMPETENCIA | date(4) |  |  | Competência |
| DATA_VENCIMENTO | date(4) |  |  | Vencimento |
| SALDO_DEVEDOR | numeric(13) |  |  | Saldo devedor |
| VALOR_EM_ABERTO | numeric(13) |  |  | Valo em aberto |
| VALOR_NAO_PARCELAR | numeric(13) |  |  | Valor não parcelar |
| VALOR_PARCELAR | numeric(13) |  |  | Valor parcelar |
| I_PARCELAMENTO_DEBITO_NAO_CALCULADO | integer(4) |  | S | Código do parcelamento |
