# GEATENDIMENTOTABELASTRANSFERIR — Tabelas utilizadas pelo Agente de Comunicação para realizar o envio de dados
175 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  |  |
| GRUPO | integer(4) |  |  |  |
| TABELA | varchar(1024) |  |  |  |
| CRIADOR | varchar(32) |  |  |  |
| TAG_PAI_XML_RECEBIMENTO | varchar(1024) |  | S |  |
| NOME_XML | varchar(1024) |  | S |  |
| ORDEM | integer(4) |  | S |  |
| POSSUI_TABELA_AUXILIAR | integer(4) |  | S |  |
| CODIGO_TABELA_BAIXAR | integer(4) |  |  |  |
| COMANDO_CARGA_INICIAL | varchar(10000) |  | S |  |
| TAG_ID_XML | integer(4) |  |  |  |
| DESCRICAO_TABELA | varchar(1024) |  |  |  |
| VERSAO_XML | integer(4) |  | S |  |
| TABELA_BLOCO_INFORMACOES | integer(4) |  | S | Endpoint utilizado para a transferência da tabela. |
| ENDPOINT | varchar(512) |  | S | Endpoint utilizado para a transferência da tabela. |
| LOGIN_POR_USUARIO | bit(1) |  |  | 0 - Login GERENTE, 1 - Login por usuário específico |
| BUSCA_REGISTRO_POR_GUID | bit(1) |  |  | 0 - Busca por clausula, 1 - Busca por GUID Contabil |
| USA_METODO_POST | bit(1) |  |  | 0 - Não usa método POST, 1 - Usa método POST |
| EXCLUIR_REGISTROS_NAO_RECEBIDOS | bit(1) |  |  | 0 - Mantém registros que não foram recebidos pelo Atendimento no Onvio, 1 - Exclui os registros que foram recebidos pelo Atendimento no Onvio |
| TIPO_RETORNO | tinyint(1) |  |  | 1 - SimpleDtoWithIdAndDeletePath, 2 - SimpleDtoWithId, 3 - None, 4 - SimpleDtoWithIdAndHATEOS |
| SINCRONIA_ONVIO_CONCLUIDA | bit(1) |  |  | Coluna utilizada apenas pelas tabelas do grupo 28. |
| ULTIMA_CHAVE_SINCRONIZADA | bigint(8) |  | S | Coluna utilizada apenas pelas tabelas do grupo 28. |
| FILTRO_CONSULTA | long varchar(32767) |  | S | Coluna utilizada apenas pelas tabelas do grupo 28. |
| FILTRO_CONSULTA_POS_WHERE | long varchar(32767) |  | S | Coluna utilizada apenas pelas tabelas do grupo 28. |
| ENVIO_ASSINCRONO | integer(4) |  | S | 0 - Envio Sincrono/ 1-Envio Assincrono |
| NOME_TABELA_BLOCO_INFORMACOES | varchar(50) |  | S | Tabela base do bloco de informação |
| UPLOAD_STATIC_FILES | bit(1) |  |  | Arquivo será enviado para o static files. |
| CODIGO_TABELA_DEPENDENTE | integer(4) |  | S | Tabela que deverá ser verificada primeiro. Coluna será utilizada pela Central de Conflitos |
| ENDPOINT_CONSULTA | varchar(512) |  | S | ENDPOINT de consulta dos registros no Onvio. Coluna será utilizada pela Central de Conflitos |
| USAR_TRIGGER_SINCRONIZACAO_ONVIO | smallint(2) |  |  | Usa trigger de sincronização com o Onvio. (0=Não/1=Sim) |
| PERMITE_INSERIR_UNICA_ACAO_ONVIO | smallint(2) |  |  | Permite inserir uma única ação do Onvio. (0=Não/1=Sim) |
| ENDPOINT_INATIVACAO | varchar(512) |  | S | Endpoint inativação do registro. |
| RATE_LIMIT | bit(1) |  |  | Indica se o endpoint será afetado pelo circuitbreaker (0=Não/1=Sim) |
