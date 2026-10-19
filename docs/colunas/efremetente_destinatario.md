# efremetente_destinatario — REMETENTES/DESTINATARIOS - CADASTRO
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | EMPRESA |
| codigo | integer(4) | PK |  | SEQUENCIAL |
| codigo_municipio | integer(4) |  | S | MUNICIPIO |
| tipo_inscricao | integer(4) |  | S | TIPO DA INSCRIÇÃO (1 - CNPJ/2 - CPF/3 - CEI/4 - OUTROS/6 - CAEPF) |
| cnpj | char(14) |  | S | CNPJ/CPF |
| inscricao | char(20) |  | S | INSCRICAO ESTADUAL |
| uf | char(2) |  | S | UF |
| nome | char(40) |  | S | NOME |
| endereco | char(80) |  | S | ENDERECO |
| TIPO_CONTRIBUINTE | integer(4) |  | S | Tipo contribuinte |
