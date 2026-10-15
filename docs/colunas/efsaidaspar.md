# efsaidaspar — Notas Fiscais de Saida - Parcelas
181.154 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_sai | integer(4) | PK |  | Saida |
| vcto_saip | date(4) |  |  | Data de vencimento da parcela |
| vlor_saip | numeric(13) |  | S | Valor da Parcela |
| tipo_saip | tinyint(1) |  | S | Tipo da parcela (1-a vista/0 - Outro valor a prazo) |
| acrf_saip | numeric(5) |  | S | Aliquota da CRF |
| vcrf_saip | numeric(13) |  | S | Valor da CRF |
| vbru_saip | numeric(13) |  | S | Valor Bruto da parcela |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| parc_saip | integer(4) | PK |  | Numero da parcela |
| virrf_saip | numeric(13) |  | S | Valor do IRRF |
| vissr_saip | numeric(13) |  | S | Valor do ISS retido |
| vinss_saip | numeric(13) |  | S | Valor do INSS retido |
| apiscrfop_saip | numeric(5) |  | S | Aliquota do PIS da CRFOP |
| vpiscrfop_saip | numeric(13) |  | S | Valor do PIS da CRFOP |
| acofcrfop_saip | numeric(5) |  | S | Aliquota da COFINS da CRFOP |
| vcofcrfop_saip | numeric(13) |  | S | Valor da COFINS da CRFOP |
| acsoccrfop_saip | numeric(5) |  | S | Aliquota da CSLL da CRFOP |
| vcsoccrfop_saip | numeric(13) |  | S | Valor da CSLL da CRFOP |
| airpjcrfop_saip | numeric(5) |  | S | Aliquota do IRPJ da CRFOP |
| virpjcrfop_saip | numeric(13) |  | S | Valor do IRPJ da CRFOP |
| virrfp_saip | numeric(13) |  | S | Valor do IRRFP |
| vpisret_saip | numeric(13) |  | S | Valor do PIS retido |
| vcofret_saip | numeric(13) |  | S | Valor da COFINS retido |
| vcsocret_saip | numeric(13) |  | S | Valor da CSLL retido |
| VFUNRURAL_SAIP | numeric(13) |  | S | Valor do Funrural |
| VALOR_PRESENTE_JUROS_SAIP | numeric(13) |  |  | Juros valor presente |
| VALOR_PRESENTE_NDIAS_SAIP | integer(4) |  |  | Numero de dias valor presente |
| NUMERO_TITULO_SAIP | char(60) |  | S | Número do título |
| FETHAB | numeric(13) |  |  | FETHAB |
| VALOR_ICMS_ST | numeric(13) |  |  | Valor ICMS ST |
