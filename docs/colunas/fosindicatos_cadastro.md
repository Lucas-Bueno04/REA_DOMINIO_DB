# FOSINDICATOS_CADASTRO — Sindicato - Cadastro
121 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_SINDICATOS_CADASTRO | integer(4) | PK |  | Código do sindicato |
| APELIDO | char(20) |  | S | Apelido do sindicato |
| NOME | varchar(115) |  |  | Nome do sindicato |
| CEP | char(8) |  | S | CEP |
| ENDERECO | char(40) |  | S | Endereço |
| NUMERO | integer(4) |  | S | Número |
| COMPLEMENTO | char(25) |  | S | Complemento |
| BAIRRO | char(30) |  | S | Bairro |
| CIDADE | char(40) |  | S | Cidade |
| ESTADO | char(2) |  | S | Estado |
| CGC | char(18) |  | S | CNPJ |
| FONE | char(15) |  | S | Telefone |
| FAX | char(15) |  | S | Fax |
| PAGINA_INTERNET | char(40) |  | S | Endereço da página na Internet |
| EMAIL | char(255) |  | S | Correio eletrônico |
| I_BANCOS | integer(4) |  | S | Código do banco |
| AGENCIA | integer(4) |  | S | Agência |
| TIPO_ENTIDADE | tinyint(1) |  |  | Tipo da entidade:(1=Sindicato, 2=Federação, 3=Confederação, 4=CEES) |
| CODI_ENTIDADE | char(18) |  | S | Código da entidade sindical |
