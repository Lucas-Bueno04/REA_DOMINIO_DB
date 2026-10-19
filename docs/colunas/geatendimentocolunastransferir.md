# GEATENDIMENTOCOLUNASTRANSFERIR — Colunas utilizadas pelo Agente de Comunicação para realizar envios de dados
1.140 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  |  |
| CODIGO_TABELA | integer(4) |  |  |  |
| COLUNA | varchar(1024) |  | S | Nome da coluna no DB |
| NOME_XML | varchar(1024) |  | S |  |
| ATRIBUTO_XML | integer(4) |  | S |  |
| SUB_QUERY | integer(4) |  | S |  |
| CONTEUDO_SUB_QUERY | varchar(2048) |  | S |  |
| COLUNA_CONTROLE_ATENDIMENTO | integer(4) |  | S |  |
| CHAVE_TABELA_AUXILIAR | integer(4) |  | S |  |
| COLUNA_BASE_64 | integer(4) |  | S |  |
| TIPO_COLUNA | integer(4) |  | S |  |
| COLUNA_CHAVE | bit(1) |  |  | 0 - Coluna normal, 1 - Coluna chave |
| TRANSMITIR_COLUNA | bit(1) |  |  | 0 - Coluna não transmitida, 1 - Coluna transmitida |
| NOME_PARAMETRO_COLUNA_CONTROLE_ATENDIMENTO | varchar(256) |  | S | Nome do parâmetro do EndPoint para o valor máximo da coluna de controle |
| VALOR_PADRAO | varchar(1024) |  | S | Valor padrão da coluna quando o valor não existir |
| COLUNA_FILTRO | bit(1) |  |  | 0 - Coluna normal, 1 - Coluna utilizado para filtro de consulta |
| COLUNA_OBRIGATORIA | bit(1) |  |  | 0 - Coluna opcional para o envio do registro, 1 - Coluna obrigatória para o envio do registro |
| CODIGO_TABELA_PAI | integer(4) |  |  | Código da tabela pai da coluna obrigatória. |
| SUB_QUERY_GUID_CONTABIL | varchar(2048) |  | S | Subquery para busca do GUID_CONTABIL do registro pai. |
| ALIAS | varchar(1024) |  |  | Apelido da coluna |
