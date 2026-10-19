# EFPRODUTOS_ALTERACAO — Produtos - Alterações - Cadastro
127 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_PDI | char(14) | PK |  | Produto |
| DATA_ALTERACAO | date(4) | PK |  | Data da alteração |
| CAMPO | integer(4) | PK |  | Campo alterado |
| DE | varchar(255) |  |  | Valor anterior a alteração |
| PARA | varchar(255) |  |  | Valor posterior a alteração |
| COMPETENCIA_GERACAO_REGISTRO_0205 | date(4) |  | S | Competência de geração do registro 0205 |
