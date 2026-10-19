# FOVIGENCIA_UNIDADE_CALCULO — Vigência para o tipo de unidade do cálculo das rubricas.
1.372 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| COMPETENCIA | date(4) | PK |  | Competência. |
| DESCRICAO | varchar(300) |  |  | Descrição. |
| TIPO_UNIDADE_CALCULO | smallint(2) |  |  | Tipo de unidade do cálculo. (1=Conforme unidade das rubricas/2=Conforme a categoria do empregado) |
| UNIDADE_CALCULO_MENSALISTAS | smallint(2) |  |  | Unidade do cálculo para mensalistas. (1=Horas/2=Dias) |
| UNIDADE_CALCULO_SEMANALISTAS | smallint(2) |  |  | Unidade do cálculo para semanalistas. (1=Horas/2=Dias) |
| UNIDADE_CALCULO_TAREFEIROS | smallint(2) |  |  | Unidade do cálculo para tarefeiros. (1=Horas/2=Dias) |
| UNIDADE_CALCULO_DIARISTAS | smallint(2) |  |  | Unidade do cálculo para diaristas. (1=Horas/2=Dias) |
| UNIDADE_CALCULO_COMISSIONADOS | smallint(2) |  |  | Unidade do cálculo para comissionados. (1=Horas/2=Dias) |
| UNIDADE_CALCULO_PROFESSOR_MENSALISTA | smallint(2) |  |  | Unidade do cálculo para professores mensalistas. (1=Horas/2=Dias) |
| UNIDADE_CALCULO_CONTRIBUINTES | smallint(2) |  |  | Unidade do cálculo para contribuintes. (1=Horas/2=Dias) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
