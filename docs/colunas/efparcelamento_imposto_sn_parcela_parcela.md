# EFPARCELAMENTO_IMPOSTO_SN_PARCELA_PARCELA — Parcelamento de Impostos Simples Nacional - Parcela
60 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_PARCELAMENTO_SN | integer(4) | PK |  | Sequencial do parcelamento Simples Nacinal |
| I_PARCELAMENTO_SN_PARCELA_PARCELA | integer(4) | PK |  | Sequencial da parcela do parcelamento Simples Nacinal |
| NUMERO_PARCELA | integer(4) |  |  | Número da parcela |
| VENCIMENTO | date(4) |  |  | Data de vencimento |
| VALOR_PRINCIPAL | numeric(13) |  |  | Valor principal |
| VALOR_MULTA | numeric(13) |  |  | Valor multa |
| VALOR_JURO | numeric(13) |  |  | Valor juros |
| VALOR_TOTAL | numeric(13) |  |  | Valor total |
| VALOR_PAGO | numeric(13) |  |  | Valor pago |
| COMPETENCIA | date(4) |  |  | Competência |
| TIPO_PARCELAMENTO | integer(4) | PK |  | Tipo Parcela: 1-Parcela / 2-Parcela da Entrada |
| VALOR_ENCARGOS_HONORARIOS | numeric(13) |  |  | Valor encargos/honorários |
