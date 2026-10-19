# EFPARCELAMENTO_IMPOSTO_SN_PARCELA_PARCELAMENTO — Parcelamento de Impostos Simples Nacional - Parcelamento
12 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_PARCELAMENTO_SN | integer(4) | PK |  | Sequencial do parcelamento Simples Nacinal |
| I_PARCELAMENTO_SN_PARCELA_PARCELAMENTO | integer(4) | PK |  | Sequencial da parcela do parcelamento Simples Nacinal |
| COMPETENCIA | date(4) |  |  | Competência |
| DATA_VENCIMENTO | date(4) |  |  | Vencimento |
| VALOR_PRINCIPAL | numeric(13) |  |  | Valor principal |
| VALOR_MULTA | numeric(13) |  |  | Valor multa |
| VALOR_JURO | numeric(13) |  |  | Valor juros |
| VALOR_TOTAL | numeric(13) |  |  | Valor total |
| TIPO_PARCELAMENTO | integer(4) | PK |  | Tipo Parcela: 1-Parcela / 2-Parcela da Entrada |
| VALOR_ENCARGOS_HONORARIOS | numeric(13) |  |  | Valor encargos/honorários |
