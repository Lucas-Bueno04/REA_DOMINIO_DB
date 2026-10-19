# EFEMPREENDIMENTOS_IMOBILIARIOS_CONTRATOS_VENDA_PAGAMENTOS — Empreendimentos imobiliários - Contratos de venda - Parcelas - Pagamentos
6 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CONTRATO | integer(4) | PK |  | Código do contrato |
| I_PARCELA | integer(4) | PK |  | Código da parcela |
| I_PAGAMENTO | integer(4) | PK |  | Código do pagamento |
| DATA_PAGAMENTO | date(4) |  |  | Data do pagamento |
| VALOR_PAGO | numeric(13) |  |  | Valor pago |
| VALOR_CORRECAO | numeric(13) |  |  | Valor da correção |
| VALOR_JUROS | numeric(13) |  |  | Valor dos juros |
| VALOR_MULTA | numeric(13) |  |  | Valor da multa |
| VALOR_DESCONTO | numeric(13) |  |  | Valor do desconto |
| VALOR_LIQUIDO | numeric(13) |  |  | Valor líquido |
| BASE_CALCULO_PIS | numeric(13) |  |  | Base de cálculo do PIS |
| BASE_CALCULO_COFINS | numeric(13) |  |  | Base de cálculo da COFINS |
| ORIGEM_PAGAMENTO | char(1) |  |  | ORIGEM DO PAGAMENTO (B - BAIXA/L - LANÇAMENTO/R - RESCINDIDA) |
| VALOR_DEVOLUCAO | numeric(13) |  |  | Valor devolução |
| CST_PIS_COFINS_RECEITA_FINANCEIRA_CORRECAO | integer(4) |  | S | CST - Receita financeira - Correção |
| BASE_CALCULO_PIS_COFINS_RECEITA_FINANCEIRA_CORRECAO | numeric(13) |  |  | Base de PIS e COFINS - Receita financeira - Correção |
| BASE_CALCULO_PIS_COFINS_RECEITA_FINANCEIRA_JUROS_MULTA | numeric(13) |  |  | Base de PIS e COFINS - Receita financeira - Juros e Multa |
| REDUTOR_AJUSTE_IBS_CBS | numeric(13) |  |  | Redutor de ajuste do IBS/CBS |
| REDUTOR_SOCIAL_IBS_CBS | numeric(13) |  |  | Redutor social do IBS/CBS |
| BASE_CALCULO_IBS | numeric(13) |  |  | Base de cálculo do IBS |
| ALIQUOTA_IBS | numeric(5) |  |  | Alíquota do IBS |
| VALOR_IBS | numeric(13) |  |  | Valor do IBS |
| BASE_CALCULO_CBS | numeric(13) |  |  | Base de cálculo da CBS |
| ALIQUOTA_CBS | numeric(5) |  |  | Alíquota da CBS |
| VALOR_CBS | numeric(13) |  |  | Valor da CBS |
