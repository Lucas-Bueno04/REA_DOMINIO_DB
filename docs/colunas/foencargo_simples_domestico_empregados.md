# FOENCARGO_SIMPLES_DOMESTICO_EMPREGADOS — Tabela de empregados que formaram a guia do simples doméstico.
12.544 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| COMPETENCIA | date(4) | PK |  | Competência do cálculo |
| TIPO_PROCESSO | integer(4) | PK |  | Tipo de cálculo |
| I_FILIAIS | integer(4) | PK |  | Código da filial |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| BASE_CALCULO | numeric(13) |  |  | Base de cálculo |
| VALOR_INSS | numeric(13) |  |  | Valor de INSS |
| VALOR_INSS_EMPRESA | numeric(13) |  |  | Valor de INSS Empresa |
| VALOR_CONTRIBUICAO_SOCIAL | numeric(13) |  |  | Valor da contribuição social |
| VALOR_FGTS | numeric(13) |  |  | Valor de FGTS |
| VALOR_INDENIZACAO | numeric(13) |  |  | Valor de indenização |
| VALOR_IRRF | numeric(13) |  |  | Valor de IRRF |
| VALOR_TOTAL | numeric(13) |  |  | Valor total dos encargos |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
| VALOR_SALARIO_FAMILIA | numeric(13) |  |  | Valor do salário família. |
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
