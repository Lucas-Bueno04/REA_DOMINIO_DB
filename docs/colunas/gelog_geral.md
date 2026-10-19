# GELOG_GERAL — Tabela de logs gerais do contÃ¡bil.
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| GUID_LOG | uniqueidentifier(16) | PK |  | Guid do registro. |
| TIPO | integer(4) |  |  | 1: Erro copiando dll relatorios DW. / 2: Exclusão Controle Brclient. / 3: Erro ao coletar dados de observabilidade. |
| DATA_HORA | timestamp(8) |  |  | Data hora da gravaÃ§Ã£o. |
| USUARIO | varchar(20) |  |  | UsuÃ¡rio logado. |
| MENSAGEM_LOG | varchar(5000) |  |  | Mensagem do log. |
