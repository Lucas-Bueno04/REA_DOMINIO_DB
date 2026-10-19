# GEIBGE_TIPO_OBRAS_SERVICOS — Cadastro dos tipos de obras e serviços segundo classificação do IBGE
86 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_IBS | integer(4) | PK |  | Código |
| CODI_IBGE | char(9) |  |  | Código do IBGE |
| TIPO_IBS | char(1) |  |  | Tipo (I=IBGE/N=NOVO) |
| DESCRICAO_IBS | varchar(200) |  |  | Descrição |
