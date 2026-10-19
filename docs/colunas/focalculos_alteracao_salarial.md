# FOCALCULOS_ALTERACAO_SALARIAL — Cálculos que pagaram alterações salariais
236.299 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo - Renomeado |
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| DATA_ALTERACAO | date(4) | PK |  | Data da alteração salarial |
| TIPO_GRADE | smallint(2) | PK |  | Tipo da alteração salarial: (1=Normal, 2=Valor hora-aula, 3=Grade salarial, 4=Resilição Professor) |
| TIPO_SALARIO | smallint(2) | PK |  | Tipo da utilização da alteração no cálculo. (1=Cálculo do salário no mês, 2=Cálculo do período retroativo) |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro: (0=Sistema, 1=Importação de tabelas, 2=Importação de leiaute, 3=Conversão) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo |
