# hnagencias — Agencias Bancarias - Cadastro
8 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_banco | integer(4) |  |  | Banco |
| i_agencia | integer(4) | PK |  | Sequencial |
| nome_age | varchar(50) |  |  | Nome |
| agencia_dv | char(2) |  |  | Digito verificador |
| codi_age | integer(4) |  |  | Codigo da agencia |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| endereco | char(40) |  | S | Endereco |
| bairro | char(40) |  | S | Bairro |
| cidade | char(40) |  | S | Cidade |
| numero | integer(4) |  | S | Numero |
| uf | char(2) |  | S | UF |
| cep | char(8) |  | S | CEP |
| complemento | char(30) |  | S | Complemento |
| ddd | integer(4) |  | S | DDD |
| fone | char(14) |  | S | Fone |
| COOPERATIVA_CREDITO | char(1) |  |  | Cooperativa de crédito (S/N) |
| COOPERATIVA_CREDITO_CNPJ | char(14) |  | S | CNPJ da cooperativa de crédito |
| COOPERATIVA_CREDITO_AGENCIA | integer(4) |  | S | Agência da cooperativa |
| COOPERATIVA_CREDITO_AGENCIA_DV | char(1) |  | S | Agência da cooperativa - Dígito verificador |
| COOPERATIVA_CREDITO_BANCO | char(1) |  |  | BANCO DA COOPERATIVA (U=UNICRED/S=SICOOB/N=UNIPRIME) |
| COOPERATIVA_CREDITO_CODIGO | varchar(13) |  | S | Código da cooperativa |
| COOPERATIVA_CREDITO_PREFIXO | char(3) |  | S | Prefixo da cooperativa |
