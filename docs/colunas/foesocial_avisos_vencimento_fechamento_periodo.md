# FOESOCIAL_AVISOS_VENCIMENTO_FECHAMENTO_PERIODO — Armazena os avisos de vencimentos para os períodos sem fechamentos no eSocial
29.696 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| COMPETENCIA | date(4) | PK |  | Competência |
| TIPO | smallint(2) | PK |  | Tipo de cálculo. (0=Mensal/1=Anual) |
| SITUACAO | smallint(2) |  |  | Situação. (0=Aberto/1=Fechado) |
| COMPANY_ID | uniqueidentifier(16) |  | S | ONVIO company global unique identifier |
