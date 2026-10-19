# EFPARCELAMENTO_IMPOSTO_SN_PARCELA_DADOS — Parcelamento de Impostos Simples Nacional - Dados
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_PARCELAMENTO_SN | integer(4) | PK |  | Sequencial do parcelamento Simples Nacinal |
| TOTAL_PARCELADO | numeric(13) |  |  | Total parcelado |
| NUMERO_DE_PARCELA | integer(4) |  |  | Número de parcelas |
| VALOR_PARCELA | numeric(13) |  |  | Valor da parcela |
| VENCIMENTO_INICIAL | date(4) |  |  | Vencimento inicial |
| TIPO_PARCELAMENTO | integer(4) | PK |  | Tipo Parcela: 1-Parcela / 2-Parcela da Entrada |
| PERCENTUAL_ENTRADA | numeric(6) |  |  | Percentual da Entrada |
| PERCENTUAL_ENTRADA_CALCULADO | numeric(23) |  |  | Percentual da Entrada - Todas Casas decimais |
| VALOR_PRINCIPAL | numeric(13) |  |  | Valor Principal |
| VALOR_MULTA | numeric(13) |  |  | Valor Multa |
| VALOR_JURO | numeric(13) |  |  | Valor Juros |
| VALOR_ENCARGOS_HONORARIOS | numeric(13) |  |  | Valor Encargos Honorarios |
| VALOR_TOTAL | numeric(13) |  |  | Valor Total |
| PERCENTUAL_PRIMEIRA_PARCELA | numeric(5) |  |  | Percentual da primeira parcela |
| VALOR_PRIMEIRA_PARCELA | numeric(13) |  |  | Valor da primeira parcela |
