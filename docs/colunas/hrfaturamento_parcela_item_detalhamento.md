# HRFATURAMENTO_PARCELA_ITEM_DETALHAMENTO — Faturamento - Parcelas - Itens - Detalhamento
27.868 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_FATURAMENTO | integer(4) | PK |  | Faturamento |
| I_PARCELA | integer(4) | PK |  | Parcela |
| I_EVENTO | integer(4) | PK |  | Evento |
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| PAGO_ESCRITORIO | char(1) | PK |  | Pago pelo escritorio S N |
| COMPLEMENTO | varchar(500) |  |  | Complemento |
| VALOR | numeric(13) |  | S | Valor |
| VALOR_DESCONTO | numeric(13) |  | S | Valor de desconto |
| VALOR_DESCONTO_ADIMPLENTE | numeric(13) |  | S | Valor de desconto concedido por adimplente |
| VALOR_ORIGINAL | numeric(13) |  | S | Valor original |
| VALOR_IRRF | numeric(13) |  | S | Valor IRRF aproveitado |
| VALOR_IRRF_CALCULADO | numeric(13) |  | S | Valor IRRF calculado |
| ALIQUOTA_IRRF | numeric(5) |  | S | Aliquota de IRRF |
| VALOR_ISS | numeric(13) |  | S | Valor de ISS |
| ALIQUOTA_ISS | numeric(5) |  | S | Aliquota de ISS |
| VALOR_ISS_RETIDO | numeric(13) |  | S | Valor de ISS Retido |
| VALOR_ISS_RETIDO_CALCULADO | numeric(13) |  | S | Valor de ISS Retido calculado |
| ALIQUOTA_ISS_RET | numeric(5) |  | S | Aliquota de ISS |
| VALOR_INSS_RETIDO | numeric(13) |  | S | Valor de INSS Retido |
| VALOR_INSS_RETIDO_CALCULADO | numeric(13) |  | S | Valor de INSS Retido calculado |
| ALIQUOTA_INSS_RET | numeric(5) |  | S | Aliquota de INSS |
| VALOR_CRF | numeric(13) |  | S | Valor de CRF aproveitado |
| VALOR_CRF_CALCULADO | numeric(13) |  | S | Valor de CRF calculado |
| VALOR_CRF_PIS_CALCULADO | numeric(13) |  | S | Valor de CRF PIS calculado |
| VALOR_CRF_COFINS_CALCULADO | numeric(13) |  | S | Valor de CRF COFINS calculado |
| VALOR_CRF_CSLL_CALCULADO | numeric(13) |  | S | Valor de CRF CSLL calculado |
| VALOR_CRF_PIS | numeric(13) |  | S | Valor de CRF PIS aproveitado |
| VALOR_CRF_COFINS | numeric(13) |  | S | Valor de CRF COFINS aproveitado |
| VALOR_CRF_CSLL | numeric(13) |  | S | Valor de CRF CSLL aproveitado |
| ALIQUOTA_RETENCAO_FONTE | numeric(5) |  | S | Aliquota de Retencao na Fonte |
| VALOR_PIS | numeric(13) |  | S | Valor de PIS (Usado somente para DF) |
| ALIQUOTA_PIS | numeric(5) |  | S | Aliquota de PIS (Usado somente para DF) |
| VALOR_COFINS | numeric(13) |  | S | Valor de COFINS (Usado somente para DF) |
| ALIQUOTA_COFINS | numeric(5) |  | S | Aliquota de COFINS (Usado somente para DF) |
| VALOR_IBS | numeric(13) |  | S | Valor IBS |
| BASE_CALCULO_IBS | numeric(13) |  | S | Base de cálculo IBS |
| ALIQUOTA_IBS | numeric(5) |  | S | Alíquota IBS |
| VALOR_CBS | numeric(13) |  | S | Valor CBS |
| BASE_CALCULO_CBS | numeric(13) |  | S | Base de cálculo CBS |
| ALIQUOTA_CBS | numeric(5) |  | S | Alíquota CBS |
| ALIQUOTA_EFETIVA_IBS | numeric(5) |  | S | Aliquota efetiva IBS |
| ALIQUOTA_EFETIVA_CBS | numeric(5) |  | S | Aliquota efetiva CBS |
