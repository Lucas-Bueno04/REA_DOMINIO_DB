# EFSIMULACAO_REFORMA_TRIBUTARIA_IMPOSTOS — Simulador Reforma Tributaria - Impostos Apuracao
131 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| PERIODO | date(4) | PK |  | Periodo - Competencia |
| CODI_IMP | integer(4) | PK |  | Codigo Imposto |
| COMPETENCIA_TRIBUTACAO | char(1) |  |  | Competencia da Tributacao (F - Federal, E - Estadual, M - Municipal) |
| VALOR_IMPOSTO | numeric(13) |  |  | Valor do Imposto |
| VALOR_IMPOSTO_RETIDO | numeric(13) |  |  | Valor do Imposto Retido |
