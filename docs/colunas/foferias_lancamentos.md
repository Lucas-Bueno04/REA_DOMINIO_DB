# FOFERIAS_LANCAMENTOS — TABELA DE LANÇAMENTOS DE FÉRIAS
1.134 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | CÓDIGO DA EMPRESA |
| I_EMPREGADOS | integer(4) | PK |  | CÓDIGO DO EMPREGADO |
| I_FERIAS_GOZO | integer(4) | PK |  | CÓDIGO DO GOZO |
| I_EVENTOS | integer(4) | PK |  | CÓDIGO DO EVENTO |
| VALOR_INFORMADO | numeric(13) |  |  | VALOR INFORMADO |
| VALOR_CALCULADO | numeric(13) |  | S | VALOR CALCULADO |
| ORIGEM | tinyint(1) |  |  | ORIGEM |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| PLANO_SAUDE_RATEIO | smallint(2) |  | S | Forma do rateio: 0=Não ratear/1=Quantidade de beneficiários/2=Percentual definido/3=Todo para o empregado |
| FORMA_RATEIO_PENSAO_ALIMENTICIA | smallint(2) |  |  | Frm de rateio da pensão alimentícia. (0=Não rateado/1=Rateio pela qtd de ben/2=Rat do valor da rubrica por percentual definido) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
