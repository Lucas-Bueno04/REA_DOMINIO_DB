# gesocios_dependentes — Socios - Cadastro - Dependentes
3 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_socio | integer(4) | PK |  | Codigo socio |
| sequencial | integer(4) | PK |  | Sequencial |
| tipo | tinyint(1) |  |  | Tipo (21 - Filho/24 - Descendente/31 - Dependente Ascendente/41 - Menor Probre/90 - Outros) |
| nome | char(40) |  |  | Nome |
| dtnascimento | date(4) |  |  | Data de nascimento |
