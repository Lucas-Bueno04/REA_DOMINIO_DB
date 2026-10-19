# FOCALCULOS_BASES_INSS_TERCEIROS — Bases de cálculo do INSS
879.775 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CALCULOSBASES_OLD | integer(4) |  | S | Sequencial da base de cálculo. |
| CODIGO_CONVENIO | smallint(2) | PK |  | Código do convênio de terceiros. |
| I_CADBASES | integer(4) |  |  | Código da base de cálculo. |
| BASE | numeric(17) |  |  | Base |
| TAXA | numeric(11) |  |  | Taxa |
| VALOR | numeric(20) |  |  | Valor |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOSBASES | uniqueidentifier(16) | PK |  | CÓDIGO DA BASE DE CÁLCULO. |
