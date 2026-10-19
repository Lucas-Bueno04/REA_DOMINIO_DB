# geempre_comerciais — Empresa - Referencias Comerciais
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| sequencial | integer(4) | PK |  | Sequencial |
| tipo | char(1) |  |  | Tipo (C - Cliente/F - Fornecedor/A - Ambos) |
| empresa | char(40) |  |  | Nome da empresa |
| endereco | char(40) |  | S | Endereco |
| bairro | char(40) |  | S | Bairro |
| cidade | char(40) |  | S | Cidade |
| uf | char(2) |  | S | UF |
| numero | integer(4) |  | S | Numero |
| cep | char(8) |  | S | CEP |
| complemento | char(30) |  | S | Complemento |
| ddd | integer(4) |  | S | DDD |
| fone | char(14) |  | S | Fone |
| PESSOA_CONTATO | varchar(50) |  | S | Pessoa para contato |
