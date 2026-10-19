# EFPLANEJAMENTO_TRIBUTARIO_IMPOSTOS_SIMPLES — Planejamento Tributário - Impostos Simples
40 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| REGIME | char(1) | PK |  | Regime de Planejamento (P - Presumido / R - Real / S - Simples Nacional) |
| PERIODO | date(4) | PK |  | Periodo planejamento |
| IMPOSTO | integer(4) | PK |  | Imposto |
| ANEXO | integer(4) | PK |  | Anexo |
| SECAO | integer(4) | PK |  | Secao |
| TABELA | integer(4) | PK |  | Tabela |
| TIPO | char(1) | PK |  | Tipo (A - Ambos / I - Interno / E - Externo) |
| IMPOSTO_REPARTICAO | integer(4) | PK |  | Imposto - Reparticao |
| VALOR | numeric(13) |  |  | Valor |
