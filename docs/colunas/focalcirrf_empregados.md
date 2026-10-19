# FOCALCIRRF_EMPREGADOS — Valores da guia separados por empregado.
55.171 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| PERIODO_INICIO | date(4) | PK |  | Período início. |
| CODIGO_REC | integer(4) | PK |  | Código de recolhimento. |
| CODI_EMP_FILIAL | integer(4) | PK |  | Código da empresa do empregado. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| VALOR | numeric(13) |  |  | Valor de IRRF. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/3=Importação de layout) |
| TIPO_GUIA | smallint(2) | PK |  | Tipo de guia. (1=Empregados e Contribuintes/2=Domésticos) |
| BASE | numeric(13) |  |  | Valor da base utilizado para o calculo do recolhimento |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
