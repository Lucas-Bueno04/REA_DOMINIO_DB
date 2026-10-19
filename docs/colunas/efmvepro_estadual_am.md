# EFMVEPRO_ESTADUAL_AM — Notas Fiscais de Entrada - Produtos - Estadual AM
1.887 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_ENT | integer(4) | PK |  | Código sequencial da nota de entrada |
| NUME_MEP | integer(4) | PK |  | Código sequencial do estoque |
| CODI_PDI | char(14) |  |  | Código do produto |
| DIA_POSSUI_ISENCAO | char(1) |  |  | Possui isenção (S/N) |
| DIA_POSSUI_ISENCAO_CODIGO_TRIBUTACAO | integer(4) |  | S | Código de tributação do produto - DIA |
| DIFALI_CODIGO_TRIBUTACAO | integer(4) |  | S | Código de tributação do produto - DIFALI |
| DIFALI_BASE_CALCULO | numeric(13) |  |  | Base de Cálculo - DIFALI |
| DIFALI_ALIQUOTA | numeric(7) |  |  | Alíquota - DIFALI |
| DIFALI_VALOR | numeric(13) |  |  | Valor - DIFALI |
| ICMS_ANTECIPACAO_CODIGO_TRIBUTACAO | integer(4) |  | S | Código de tributação do produto - ICMSA |
| ICMS_ANTECIPACAO_BASE_CALCULO | numeric(13) |  |  | Base de Cálculo - ICMSA |
| ICMS_ANTECIPACAO_ALIQUOTA | numeric(7) |  |  | Alíquota - ICMSA |
| ICMS_ANTECIPACAO_VALOR | numeric(13) |  |  | Valor - ICMSA |
| ICMS_ST_ANTECIPACAO_TOTAL_CODIGO_TRIBUTACAO | integer(4) |  | S | Código de tributação do produto - ICMSST |
| ICMS_ST_ANTECIPACAO_TOTAL_BASE_CALCULO | numeric(13) |  |  | Base de Cálculo - ICMSST |
| ICMS_ST_ANTECIPACAO_TOTAL_ALIQUOTA | numeric(7) |  |  | Alíquota - ICMSST |
| ICMS_ST_ANTECIPACAO_TOTAL_VALOR | numeric(13) |  |  | Valor - ICMSST |
