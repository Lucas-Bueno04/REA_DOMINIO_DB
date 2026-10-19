# prCliEve — Clientes Eventuais - Cadastro
23 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_cev | integer(4) | PK |  | Codigo |
| nome_cev | char(40) |  |  | Nome |
| cont_cev | char(40) |  | S | Contato |
| ende_cev | char(40) |  | S | Endereco |
| comp_cev | char(25) |  | S | Complemento |
| bair_cev | char(25) |  | S | Bairro |
| cepe_cev | char(8) |  | S | CEP |
| cida_cev | char(30) |  | S | Cidade |
| fone_cev | char(14) |  | S | Fone |
| esta_cev | char(2) |  | S | UF |
| apel_cev | char(15) |  | S | Apelido |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
