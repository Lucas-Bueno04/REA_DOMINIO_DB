# FOAFASTAMENTOS_ESTABILIDADE — Estabilidades do empregado geradas pelo afastamento.
1.565 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| DATA_REAL_DN | numeric(10) | PK |  | Data real do afastamento. |
| I_ESTABILIDADE | integer(4) | PK |  | Código do tipo de estabilidade. |
| SEQUENCIAL | integer(4) | PK |  | Código sequencial da estabilidade. |
| ESTABILIDADE_CCT | smallint(2) |  |  | Estabilidade gerada pela Convenção Coletiva de Trabalho (0=Não/1=Sim ). |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
