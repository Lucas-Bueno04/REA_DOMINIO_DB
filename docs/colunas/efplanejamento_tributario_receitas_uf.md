# EFPLANEJAMENTO_TRIBUTARIO_RECEITAS_UF — Planejamento Tributário - Receitas por estado
150 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| REGIME | char(1) | PK |  | Regime de Planejamento (P - Presumido, R - Real, S - Simples) |
| PERIODO | date(4) | PK |  | Periodo Planejamento |
| TIPO_RECEITA | char(3) | PK |  | Tipo Receita (RBC, RBS, RBI, CC, CI, ED, DVC, DVI) |
| UF_ORIGEM | char(2) | PK |  | Estado Origem |
| UF_DESTINO | char(2) | PK |  | Estado Destino |
| RECEITA | numeric(13) |  |  | Receita |
| VALOR_IPI | numeric(13) |  |  | Valor IPI |
| VALOR_ICMS_ST | numeric(13) |  |  | Valor ICMS ST |
| AUMENTO | numeric(13) |  |  | Aumento |
| REDUCAO | numeric(13) |  |  | Reducao |
| RECEITA_ESTIMATIVA | numeric(13) |  |  | Receita Estimativa |
| VALOR_IPI_ESTIMATIVA | numeric(13) |  |  | Valor IPI Estimativa |
| VALOR_ICMS_ST_ESTIMATIVA | numeric(13) |  |  | Valor ICMS ST Estimativa |
