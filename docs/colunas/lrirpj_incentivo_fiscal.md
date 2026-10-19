# LRIRPJ_INCENTIVO_FISCAL — Lançamentos de Incentivos Fiscais
203 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_IRPJ_INCENTIVO_FISCAL | integer(4) | PK |  | Código |
| COMPETENCIA | date(4) |  |  | Competência |
| I_INCENTIVO_FISCAL | integer(4) |  |  | Incentivo Fiscal |
| NUMERO_REFEICAO | integer(4) |  |  | Número de refeições |
| VALOR_BASE | numeric(13) |  |  | Valor base |
| ALIQUOTA | numeric(5) |  |  | Alíquota |
| VALOR_TOTAL | numeric(13) |  |  | Total |
| I_SCP | integer(4) |  | S | SCP |
| APROVEITAR_ATE | date(4) |  |  | Data limite que será aproveitado |
