# EFSAIDASPAR_PIS_COFINS — Notas Fiscais de Saida - Pagamento das Parcelas - PIS/COFINS
1.288 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_SAI | integer(4) | PK |  | Código da saída |
| PARC_SAIP | integer(4) | PK |  | Número da parcela |
| I_PIS_COFINS | integer(4) | PK |  | Sequencial |
| NROPAG_SAIP | tinyint(1) | PK |  | Número do pagamento(sequencial) |
| DATA_PAGAMENTO | date(4) |  |  | Data do pagamento |
| CST | integer(4) |  |  | CST |
| NATUREZA_RECEITA | integer(4) |  | S | Natureza da receita |
| VALOR_CONTABIL | numeric(13) |  |  | Valor contábil |
| EXCLUSOES | numeric(13) |  |  | Exclusões |
| BASE_CALCULO | numeric(13) |  |  | Base de cálculo |
| ALIQUOTA_PIS | numeric(7) |  |  | Alíquota do PIS |
| ALIQUOTA_COFINS | numeric(7) |  |  | Alíquota da COFINS |
| QUANTIDADE_TRIBUTADA | numeric(13) |  |  | Quantidade tributada |
| VALOR_UNIDADE_MEDIDA_PIS | numeric(13) |  |  | Valor por unidade do PIS por unidade de medida |
| VALOR_UNIDADE_MEDIDA_COFINS | numeric(13) |  |  | Valor por unidade da COFINS por unidade de medida |
| VALOR_PIS | numeric(13) |  |  | Valor do PIS |
| VALOR_COFINS | numeric(13) |  |  | Valor da COFINS |
| PERCENTUAL_REDUCAO_BC | numeric(5) |  |  | Percentual Redução Base Cálculo |
| VALOR_FETHAB | numeric(13) |  |  | Valor do FETHAB |
| CODIGO_BENEFICIO_DIRBI | integer(4) |  | S | Código do Benefício DIRBI |
