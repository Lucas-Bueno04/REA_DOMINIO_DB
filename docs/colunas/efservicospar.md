# efservicospar — Notas Fiscais de Servico - Parcelas
115.341 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_ser | integer(4) | PK |  | Servico |
| vcto_serp | date(4) |  |  | Vencimento da Parcela |
| vlor_serp | numeric(13) |  | S | Valor da parcela |
| tipo_serp | tinyint(1) |  | S | Tipo da parcela (1-a vista/0 - Outro valor a prazo) |
| acrf_serp | numeric(5) |  | S | Aliquota da CRF |
| vcrf_serp | numeric(13) |  | S | Valor da CRF |
| virrf_serp | numeric(13) |  | S | Valor do IRRF |
| vissr_serp | numeric(13) |  | S | Valor do ISS Retido na Fonte |
| vbru_serp | numeric(13) |  | S | Valor Bruto da parcela |
| vinss_serp | numeric(13) |  | S | Valor do INSS Retido |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| parc_serp | tinyint(1) | PK |  | Numero da parcela |
| apiscrfop_serp | numeric(5) |  | S | Aliquota do PIS da CRFOP |
| vpiscrfop_serp | numeric(13) |  | S | Valor do PIS da CRFOP |
| acofcrfop_serp | numeric(5) |  | S | Aliquota da COFINS da CRFOP |
| vcofcrfop_serp | numeric(13) |  | S | Valor da COFINS da CRFOP |
| acsoccrfop_serp | numeric(5) |  | S | Aliquota da CSLL da CRFOP |
| vcsoccrfop_serp | numeric(13) |  | S | Valor da CSLL da CRFOP |
| airpjcrfop_serp | numeric(5) |  | S | Aliquota do IRPJ da CRFOP |
| virpjcrfop_serp | numeric(13) |  | S | Valor do IRPJ da CRFOP |
| virrfp_serp | numeric(13) |  | S | Valor do IRRFP |
| vpisret_serp | numeric(13) |  | S | Valor do PIS retido |
| vcofret_serp | numeric(13) |  | S | Valor da COFINS retido |
| vcsocret_serp | numeric(13) |  | S | Valor da CSLL retido |
| VALOR_PRESENTE_JUROS_SERP | numeric(13) |  |  | Juros valor presente |
| VALOR_PRESENTE_NDIAS_SERP | integer(4) |  |  | Numero de dias valor presente |
| NUMERO_TITULO_SERP | char(60) |  | S | Número do título |
