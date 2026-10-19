# EFSIMULACAO_REFORMA_TRIBUTARIA_BASE_POR_ACUMULADOR — Simulador Reforma Tributaria - Base por Acumulador
121 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| PERIODO | date(4) | PK |  | Periodo - Competencia |
| FILIAL | integer(4) | PK |  | Filial |
| CODI_ACU | integer(4) | PK |  | Codigo Acumulador |
| TIPO_MOVIMENTO | char(2) | PK |  | TIPO MOVIMENTO (CE - CREDITO ENTRADA / DE - DEBITO ENTRADA / DS - DEBITO SAIDA) |
| VALOR_CONTABIL | numeric(13) |  |  | Valor contabil |
| VALOR_ICMS | numeric(13) |  |  | Valor ICMS |
| VALOR_DIFAL | numeric(13) |  |  | Valor DIFAL |
| VALOR_ICMS_ST | numeric(13) |  |  | Valor ICMS ST |
| VALOR_ISS | numeric(13) |  |  | Valor ISS |
| VALOR_PIS | numeric(13) |  |  | Valor PIS |
| VALOR_COFINS | numeric(13) |  |  | Valor COFINS |
| VALOR_LIQUIDO | numeric(13) |  |  | Valor Liquido |
| VALOR_LIQUIDO_2027 | numeric(13) |  |  | Valor Liquido base para 2027 |
| VALOR_LIQUIDO_2033 | numeric(13) |  |  | Valor Liquido base para 2033 |
