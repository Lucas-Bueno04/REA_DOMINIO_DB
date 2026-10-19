# fotabcalc_patronal — Tabela de Contribuição Sindical Patronal
24 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_fotabcalc_patronal | integer(4) | PK |  | Código |
| nome | char(40) |  |  | Nome |
| ATIVIDADE_ENSINO | smallint(2) |  |  | Atividade de ensino. (0=Não/1=Sim) |
| UTILIZAR_RECEITA_BRUTA | smallint(2) |  |  | Utilizar receita bruta para o cálculo. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
