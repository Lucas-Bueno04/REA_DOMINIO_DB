# GEATENDIMENTO_PUBLICAR_DOCUMENTOS — Relação de documentos publicados
42.851 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_DOCUMENTO | integer(4) | PK |  |  |
| EMPRESA | integer(4) |  | S |  |
| DEPARTAMENTO | integer(4) |  | S |  |
| PASTA | varchar(255) |  | S |  |
| NOME | varchar(255) |  | S |  |
| ARQUIVO | varchar(255) |  | S |  |
| PDF | long binary(32767) |  | S |  |
| USUARIO | integer(4) |  | S |  |
| SUBSTITUIR | integer(4) |  | S |  |
| OBSERVACAO | varchar(1024) |  | S |  |
| COMPETENCIA | date(4) |  | S | Competencia do relatório publicado |
| VENCIMENTO | date(4) |  | S | Vencimento do relatório publicado |
| CPF_CNPJ_CEI_EMPRESA | varchar(50) |  | S | CNPJ da Empresa que publicou o documento |
| DATA_PUBLICADO | timestamp(8) |  | S | Coluna para verificar a quantos dias o documento foi enviado |
| NOME_ARQUIVO_ONVIO | varchar(255) |  | S | Nome do arquivo à ser publicado no Onvio |
| GUID_CONTABIL | uniqueidentifier(16) |  |  | Identificador único do registro no banco do Contábil |
| GUID_ONVIO | uniqueidentifier(16) |  | S | Identificador único do registro no banco do Atendimento Onvio |
| NOME_COMPLETO | varchar(255) |  | S | Nome Completo da guia publicada |
| VALOR | numeric(13) |  | S | Valor da guia publicada |
| IMPOSTO | bit(1) |  |  | 0 - nÃ£o Ã© imposto , 1 - Ã© imposto |
| DESTINO_PUBLICACAO | integer(4) |  |  | Tipo de publicaÃ§Ã£o: 1-Documents / 2-Portal Empregado / 3-Gestta Processos / 4-Gestta Express |
| JSON_CONTRATO | varchar(1024) |  | S | Json de contrato para upload |
| I_EMPREGADOS | integer(4) |  | S |  |
| ONVIO_CHAT | bit(1) |  |  | 0 - Publicação gerada pelo usuário, 1 - Publicação gerada pelo Chatbot. |
| VERSAO_DOCUMENTO | integer(4) |  |  | Campo informa qual a versÃ£o do arquivo, este campo serva para arquivos que ja foram visualizador pelo cliente mas precisam de uma nova versÃ£o ex NomeRelatorio (2) |
| LINK_PUBLICACAO | varchar(2048) |  | S | Link da Publicação |
| JSON_APP_PARA_VOCE | varchar(1024) |  | S | Json para publicar no App Para Você. |
