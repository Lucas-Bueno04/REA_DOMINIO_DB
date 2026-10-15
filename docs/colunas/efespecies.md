# efespecies — Especies - Cadastro
55 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_esp | integer(4) | PK |  | Codigo |
| nome_esp | char(30) |  |  | Nome |
| mode_esp | integer(4) |  | S | Modelo do documento fiscal |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| codigo_modelo | char(2) |  | S | Codigo do modelo |
| tipo_esp | integer(4) |  | S | Tipo da especie |
| DOCUMENTO_NAO_FISCAL | char(1) |  |  | Documento não fiscal (S/N) |
| NOTA_FISCAL_CONJUGADA | char(1) |  |  | Nota fiscal conjugada (S/N) |
