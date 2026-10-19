# FOEQUIPAMENTOS_PROTECAO_INDIVIDUAL — Equipamento de proteção individual
9 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EPI | integer(4) | PK |  | Código do EPI. |
| DESCRICAO | varchar(150) |  |  | Descrição do EPI. |
| NUMERO_CA | char(255) |  |  | Número do C.A. |
| ESPECIFICACOES | varchar(5000) |  | S | Especificações. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout/3=Importação tabelas concorrentes ) |
