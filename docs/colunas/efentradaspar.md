# efentradaspar — Notas Fiscais de Entrada - Parcelas
157.539 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_ent | integer(4) | PK |  | Entrada |
| vcto_entp | date(4) |  |  | Data de vencimento da Parcela |
| vlor_entp | numeric(13) |  | S | Valor da Parcela |
| tipo_entp | tinyint(1) |  | S | Tipo da parcela (1-a vista/0 - Outro valor a prazo) |
| acrf_entp | numeric(5) |  | S | Aliquota da CRF |
| vcrf_entp | numeric(13) |  | S | Valor da CRF |
| virrf_entp | numeric(13) |  | S | Valor do IRRF |
| vissr_entp | numeric(13) |  | S | Valor do ISS Retido na Fonte |
| vbru_entp | numeric(13) |  | S | Valor Bruto da parcela(vlor_entp + vcrf_entp + virrf_entp + vissr_entp) |
| vinss_entp | numeric(13) |  | S | Valor do INSS Retido |
| vfunrural_entp | numeric(13) |  | S | Valor do Funrural |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| parc_entp | integer(4) | PK |  | Numero da parcela |
| vpisret_entp | numeric(13) |  | S | Valor do PIS retido |
| vcofret_entp | numeric(13) |  | S | Valor da COFINS retido |
| vcsocret_entp | numeric(13) |  | S | Valor da CSLL retido |
| VIRRFPF_ENTP | numeric(13) |  | S | Valor do IRRF pessoa fisica |
| VALOR_PRESENTE_JUROS_ENTP | numeric(13) |  |  | Juros valor presente |
| VALOR_PRESENTE_NDIAS_ENTP | integer(4) |  |  | Numero de dias valor presente |
| ICMS_ANTECIPADO | numeric(13) |  |  | ICMS Antecipado |
| FETHAB | numeric(13) |  |  | FETHAB |
| FUNDESA | numeric(13) |  |  | FUNDESA |
| APISCRFOP_ENTP | numeric(5) |  |  | Alíquota PIS CRFOP |
| VPISCRFOP_ENTP | numeric(13) |  |  | Valor PIS CRFOP |
| ACOFCRFOP_ENTP | numeric(5) |  |  | Alíquota COFINS CRFOP |
| VCOFCRFOP_ENTP | numeric(13) |  |  | Valor COFINS CRFOP |
| ACSOCCRFOP_ENTP | numeric(5) |  |  | Alíquota CSOC CRFOP |
| VCSOCCRFOP_ENTP | numeric(13) |  |  | Valor CSOC CRFOP |
| AIRPJCRFOP_ENTP | numeric(5) |  |  | Alíquota IRPJ CRFOP |
| VIRPJCRFOP_ENTP | numeric(13) |  |  | Valor IRPJ CRFOP |
| GO_FUNDEPEC | numeric(13) |  |  | GO - FUNDEPEC |
| NUMERO_TITULO_ENTP | char(60) |  | S | Numero do Título/Parcela |
| BASE_IRRF_ENTP | numeric(13) |  |  | Valor da base de cálculo do IRRF |
| TIPO_ISENCAO | integer(4) |  | S | Tipo de isenção para rendimentos isentos |
| DESCRICAO_ISENCAO | varchar(100) |  | S | Descrição de isenção para rendimentos isentos |
