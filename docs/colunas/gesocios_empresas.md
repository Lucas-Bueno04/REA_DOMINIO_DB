# gesocios_empresas — Socios - Cadastro - Empresas que Participa
2.022 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_socio | integer(4) | PK |  | Codigo socio |
| razao_social | char(40) |  |  | Razao Social |
| cnpj | char(14) | PK |  | CNPJ |
| data_entrada | date(4) |  | S | Data de entrada |
| data_saida | date(4) |  | S | Data de saida |
| participacao | numeric(5) |  | S | Participacao percentual |
| dirigente | char(1) |  |  | Dirigente (S/N) |
