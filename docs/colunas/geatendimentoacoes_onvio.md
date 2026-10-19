# GEATENDIMENTOACOES_ONVIO — Ações à serem enviadas para o Onvio.
1.081.410 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Sequencial autoincremento |
| CODIGO_TABELA | integer(4) |  |  | Código da tabela |
| ACAO | tinyint(1) |  |  | 1 - Inclusão, 2 - Exclusão, 3 - Desativação, 4 - Carga Inicial, 5 - Consulta chaves Onvio |
| GUID_CONTABIL | uniqueidentifier(16) |  | S | GUID gerado pelo Contábil para identificação do registro |
| CLAUSULA | varchar(512) |  | S | Cláusula com argumentos para geração de carga inicial e para versões anteriores de geração |
| STATUS | smallint(2) |  |  | Tipos de Status (-3=Ignorado\-2=Aguardando prioridades\-1=Erro\0=Pendente\1=Concluído\2=Aviso\3=Consulta pendente\10=Ação concluida via .SQL\11=Ação concluida via contabilidade |
| GUID_ONVIO | uniqueidentifier(16) |  | S | GUID recebido pelo Onvio quando o registro foi enviado pela primeira vez |
| ENDPOINT_EXCLUSAO | varchar(512) |  | S | EndPoint referencial do registro no Onvio |
| GUID_CHAIN | uniqueidentifier(16) |  | S | GUID retornado no header x-chain-Id para identificação da requisição. |
| CODI_EMP | integer(4) |  |  | Código da empresa |
| ORDEM | integer(4) |  |  | Ordem da tabela no envio |
| ORIGEM_ACAO | tinyint(1) |  | S | 0 - Aplicação, 1 - Carga Inicial, 2 - Reenvio de ação pai |
| DATA_HORA_INSERCAO | timestamp(8) |  | S | Data e hora da inserção da ação na tabela. |
| DATA_HORA_ULTIMO_PROCESSAMENTO | timestamp(8) |  | S | Data e hora do último processamento do registro. |
| I_FILIAL | integer(4) |  |  | Coluna que indica o código referente a filial |
| NUMERO_TENTATIVAS | integer(4) |  |  | Coluna que indica a quantidade de vezes que foi tentado enviar esta ação |
| EMPRESA_USA_DA | bit(1) |  |  | Empresa usa o DA quando a ação foi processada. (0=Não usa/1=Usa) |
| I_CONFUSUARIO | integer(4) |  |  | Código do usuário utilizado para realizar o login específico ao enviar a ação. |
| REGISTRO_CONFLITADO | bit(1) |  |  | Indica que ocorreu conflito no envio do registro |
| CORE_ONVIO_ID | uniqueidentifier(16) |  | S | GUID do registro no Onvio em casos específicos em que o mesmo é diferente do GUID no Portal do Cliente |
| OPERATION_LOCATION | varchar(512) |  | S | endpoint para consulta de envio Assíncrono |
| DATA_HORA_PROXIMA_CONSULTA_OPERATION | timestamp(8) |  | S | Data e hora do próximo momento que o endpoint operation será consultado |
| ATUALIZAR_REGISTRO | bit(1) |  |  | Indica que a ação foi enviada com metodo PUT para o onvio |
| DATA_HORA_PROXIMA_EXECUCAO | timestamp(8) |  | S | Data e hora da prÃ³xima execuÃ§Ã£o. |
