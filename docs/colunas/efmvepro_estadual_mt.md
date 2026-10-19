# EFMVEPRO_ESTADUAL_MT — Notas Fiscais de Entrada - Produtos - Estadual MT
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_ENT | integer(4) | PK |  | Código sequencial da nota de entrada |
| NUME_MEP | integer(4) | PK |  | Código sequencial do estoque |
| CODI_PDI | char(14) |  |  | Código do produto |
| ICMS_ESTIMATIVA_SIMPLIFICADO_BASE_CALCULO | numeric(13) |  |  | Base de cálculo ICMS |
| ICMS_ESTIMATIVA_SIMPLIFICADO_ALIQUOTA | numeric(5) |  |  | Alíquota ICMS |
| ICMS_ESTIMATIVA_SIMPLIFICADO_VALOR | numeric(13) |  |  | Valor ICMS |
| ICMS_ST_ESTIMATIVA_SIMPLIFICADO_BASE_CALCULO | numeric(13) |  |  | Base de cálculo ICMS ST |
| ICMS_ST_ESTIMATIVA_SIMPLIFICADO_ALIQUOTA | numeric(5) |  |  | Alíquota ICMS ST |
| ICMS_ST_ESTIMATIVA_SIMPLIFICADO_VALOR | numeric(13) |  |  | Valor ICMS ST |
| ICMSA_BASE_CALCULO | numeric(13) |  |  | Base de cálculo ICMSA |
| ICMSA_ALIQUOTA | numeric(13) |  |  | Alíquota ICMSA |
| ICMSA_VALOR | numeric(13) |  |  | Valor ICMSA |
| I_RECOLHIMENTO_ICMSA | integer(4) |  | S | Sequencial recolhimento ICMSA |
| CODIGO_RECOLHIMENTO_ICMSA | char(6) |  | S | Código recolhimento ICMSA |
| FECEP_MT_ICMS_ES_BASE_CALCULO | numeric(13) |  |  | Base de cálculo FECEP-MT |
| FECEP_MT_ICMS_ES_ALIQUOTA | numeric(5) |  |  | Alíquota FECEP-MT |
| FECEP_MT_ICMS_ES_VALOR | numeric(13) |  |  | Valor FECEP-MT |
| FECEP_MT_ICMS_ST_BASE_CALCULO | numeric(13) |  |  | FECEP-MT - ICMS ST - Base Cálculo |
| FECEP_MT_ICMS_ST_ALIQUOTA | numeric(5) |  |  | FECEP-MT - ICMS ST - Alíquota |
| FECEP_MT_ICMS_ST_VALOR | numeric(13) |  |  | FECEP-MT - ICMS ST - Valor |
