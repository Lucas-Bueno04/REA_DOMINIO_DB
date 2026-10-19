# EFPLANEJAMENTO_TRIBUTARIO_RECEITAS — Planejamento Tributário - Receitas
192 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| REGIME | char(1) | PK |  | Regime de Planejamento (P - Presumido, R - Real, S - Simples) |
| PERIODO | date(4) | PK |  | Periodo Planejamento |
| TIPO_RECEITA | char(3) | PK |  | Tipo Receita (RBC, RBS, RBI, CC, CI, ED, DVC, DVI) |
| RECEITA_INTERNA | numeric(13) |  |  | Receita Interna base |
| RECEITA_EXTERNA | numeric(13) |  |  | Receita Externa base |
| RECEITA_TOTAL | numeric(13) |  |  | Receita Total base |
| VALOR_IPI_INTERNO | numeric(13) |  |  | Valor IPI Interno base |
| VALOR_IPI_EXTERNO | numeric(13) |  |  | Valor IPI Externo base |
| VALOR_IPI_TOTAL | numeric(13) |  |  | Valor IPI Total base |
| VALOR_ICMS_ST_INTERNO | numeric(13) |  |  | Valor ICMS ST Interno base |
| VALOR_ICMS_ST_EXTERNO | numeric(13) |  |  | Valor ICMS ST Externo base |
| VALOR_ICMS_ST_TOTAL | numeric(13) |  |  | Valor ICMS ST Total base |
| AUMENTO | numeric(13) |  |  | Aumento |
| REDUCAO | numeric(13) |  |  | Reducao |
| RECEITA_INTERNA_ESTIMATIVA | numeric(13) |  |  | Receita Interna estimativa |
| RECEITA_EXTERNA_ESTIMATIVA | numeric(13) |  |  | Receita Externa estimativa |
| RECEITA_TOTAL_ESTIMATIVA | numeric(13) |  |  | Receita Total estimativa |
| VALOR_IPI_INTERNO_ESTIMATIVA | numeric(13) |  |  | Valor IPI Interno estimativa |
| VALOR_IPI_EXTERNO_ESTIMATIVA | numeric(13) |  |  | Valor IPI Externo estimativa |
| VALOR_IPI_TOTAL_ESTIMATIVA | numeric(13) |  |  | Valor IPI Total estimativa |
| VALOR_ICMS_ST_INTERNO_ESTIMATIVA | numeric(13) |  |  | Valor ICMS ST Interno estimativa |
| VALOR_ICMS_ST_EXTERNO_ESTIMATIVA | numeric(13) |  |  | Valor ICMS ST Externo estimativa |
| VALOR_ICMS_ST_TOTAL_ESTIMATIVA | numeric(13) |  |  | Valor ICMS ST Total estimativa |
