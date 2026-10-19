# FOALTERACAO_SALARIAL_COMPLEMENTOS — Alterações salariais com complementos de cálculos
623 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| COMPETENCIA | date(4) | PK |  | Competência da alteração salarial |
| TIPO | smallint(2) | PK |  | Tipo da alteração salarial: (1=Normal, 2=Valor hora-aula, 3=Grade salarial) |
| I_CALCULOS_COMPLEMENTOS_OLD | integer(4) |  | S | Código do complemento de cálculo - Renomeado |
| ORIGEM | smallint(2) | PK |  | Origem do complemento. (1=Lançamento de eventos/2=Alteração salarial/3=Rescisão/4=Alteração salarial CCT) |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro: (0=Sistema, 1=Importação de tabelas, 2=Importação de leiaute, 3=Conversão) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS_COMPLEMENTOS | uniqueidentifier(16) | PK |  | Código do complemento de cálculo |
