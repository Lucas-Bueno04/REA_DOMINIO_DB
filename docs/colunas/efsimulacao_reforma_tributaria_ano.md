# EFSIMULACAO_REFORMA_TRIBUTARIA_ANO — Simulador Reforma Tributaria
76 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| PERIODO | date(4) | PK |  | Periodo - Competencia |
| REFORMA_TRIBUTARIA_ANO | integer(4) | PK |  | Reforma tributaria conforme ano |
| TRIBUTOS_ATUAIS | numeric(13) |  |  | Valor tributos atuais |
| TRIBUTOS_APOS_REFORMA | numeric(13) |  |  | Valor tributos apos reforma |
| DIFERENCA_APOS_REFORMA | numeric(13) |  |  | Diferenca apos reforma tributaria |
| DIFERENCA_APOS_REFORMA_PERCENTUAL | numeric(13) |  |  | Diferenca apos reforma tributaria - Percentual |
