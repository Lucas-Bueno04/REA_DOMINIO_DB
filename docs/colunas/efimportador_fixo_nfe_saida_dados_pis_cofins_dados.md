# EFIMPORTADOR_FIXO_NFE_SAIDA_DADOS_PIS_COFINS_DADOS — Configuração do leiaute NF-e XML do Importador Fixo - Saída - Dados de PIS/COFINS
5 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_DADOS_PIS_COFINS | integer(4) | PK |  | Sequencial dos dados de PIS/COFINS |
| CODIGO_CST_SAIDA | integer(4) |  | S | CST - Saidas |
| NATUREZA_RECEITA | integer(4) |  | S | Natureza da receita |
| CODIGO_RECOLHIMENTO_PIS | char(6) |  | S | Codigo de recolhimento PIS |
| CODIGO_RECOLHIMENTO_COFINS | char(6) |  | S | Codigo de recolhimento COFINS |
| DEBITO_ALIQUOTA_DIFERENCIADA | char(1) |  |  | Debito por aliquota diferenciada (S/N) - Saidas |
| ALIQUOTA_PIS_DEBITO | numeric(7) |  |  | Aliquota do PIS - Saidas |
| ALIQUOTA_COFINS_DEBITO | numeric(7) |  |  | Aliquota do COFINS - Saidas |
| DEBITO_UNIDADE_MEDIDA | char(1) |  |  | Debito por unidade de medida (S/N) - Saidas |
| UNIDADE_DIFERENTE_DEBITO | char(1) |  |  | Unidade tributada diferente da inventariada (S/N) - Saidas |
| UNIDADE_TRIBUTAVEL_DEBITO | char(6) |  | S | Unidade tributavel - Saidas |
| CODIGO_UNIDADE_DEBITO | integer(4) |  | S | Codigo da unidade tributavel - Saidas |
| FATOR_CONVERSAO_DEBITO | numeric(15) |  |  | Fator de conversao - Saidas |
| VALOR_PIS_DEBITO | numeric(13) |  |  | Valor de PIS - Saidas |
| VALOR_COFINS_DEBITO | numeric(13) |  |  | Valor de COFINS - Saidas |
| CODIGO_CST_NATUREZA_RECEITA | integer(4) |  | S | Código da CST para relacionamento da natureza da receita |
