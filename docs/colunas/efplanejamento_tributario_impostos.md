# EFPLANEJAMENTO_TRIBUTARIO_IMPOSTOS — Planejamento Tributário - Impostos
204 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| REGIME | char(1) | PK |  | Regime de Planejamento (P  - Presumido, R - Real, S - Simples) |
| PERIODO | date(4) | PK |  | Período planejamento |
| IMPOSTO | integer(4) | PK |  | Imposto |
| COMPETENCIA_TRIBUTACAO | char(1) |  |  | Competencia da Tributacao (F - Federal, E - Estadual, M - Municipal, O - Folha) |
| ALIQUOTA | numeric(5) |  |  | Alíquota |
| VALOR | numeric(13) |  |  | Valor |
