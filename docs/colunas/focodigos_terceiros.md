# FOCODIGOS_TERCEIROS — Códigos de terceiros
316 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Código. |
| DESCRICAO | varchar(60) |  |  | Descrição. |
| PERCENTUAL | numeric(5) |  |  | Percentual. |
| CODIGO_FPAS | integer(4) |  | S | Código FPAS. |
| SUSPENSAO | smallint(2) |  |  | Indica se é um código de suspensão. (0=Não/1=Sim) |
| VIGENCIA_INICIAL | date(4) |  |  | Período inicial de vigência do código de terceiros. |
| DETERMINAR_FIM | smallint(2) |  |  | Determinar fim do uso do registro. (0=Não/1=Sim) |
| VIGENCIA_FINAL | date(4) |  | S | Período fim de vigência do código de terceiros. |
| SEQUENCIAL | integer(4) | PK |  | Sequencia de registros. |
