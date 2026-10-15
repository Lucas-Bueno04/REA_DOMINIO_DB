# geestado — Cadastro de estados
28 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codigo_uf | integer(4) | PK |  | Codigo do estado |
| nome_uf | char(255) |  |  | Nome do estado |
| regiao | integer(4) |  |  | Regiao do estado |
| sigla_uf | char(2) |  |  | Sigla do estado |
| aliquota | numeric(7) |  |  | Aliquota de ICMS |
| simplesn_tabela_icms | char(1) |  | S | /* SEM USO */ |
| simplesn_usa_sub_limite | char(1) |  | S | /* SEM USO */ |
| simplesn_limite_ate | numeric(13) |  | S | /* SEM USO */ |
| simplesn_permite_icms_fixo | char(1) |  | S | /* SEM USO */ |
| simplesn_icms_fixo_por | char(1) |  | S | /* SEM USO */ |
| simplesn_icms_fixo_tipo | char(1) |  | S | /* SEM USO */ |
| SIMPLESN_TABELA_PROPRIA_ICMS | char(1) |  | S | /* SEM USO */ |
| CODIGO_INTEGRA | varchar(6) |  | S | Código para Thomson Reuters INTEGRA |
