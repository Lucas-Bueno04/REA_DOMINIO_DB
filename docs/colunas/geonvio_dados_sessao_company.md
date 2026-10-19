# GEONVIO_DADOS_SESSAO_COMPANY — Dados de sessão do company referentes à Company
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CHAVE | integer(4) | PK |  |  |
| COMPANY_ID | uniqueidentifier(16) |  |  |  |
| POSSUI_MODULO_CUSTOS | bit(1) |  |  | Possui a FRP Applications\BRCustos |
| POSSUI_MODULO_PORTAL_EMPREGADO | bit(1) |  |  | Possui a FRP Applications\BREmployeePortal |
| POSSUI_MODULO_GESTTA_PROCESSOS | bit(1) |  |  | Possui a FRP Applications\BRProcess |
| POSSUI_MODULO_CHAT | bit(1) |  |  | Possui a FRP Applications\BRChat |
| POSSUI_MODULO_ICEBERG | bit(1) |  |  | Possui a FRP Applications\BRIceberg |
| POSSUI_MODULO_CONSIGNADO | bit(1) |  |  | Possui a FRP Applications\BREmprestimoConsignado |
| POSSUI_ACESSO_IMPORTACAO_API | bit(1) |  |  | Possui acesso Importacao API |
| POSSUI_LINK_PUBLICO | bit(1) |  |  | Possui IAC BR_EnablePublishingPublicLink ou FRP OnvioBR.EnablePublishingPublicLink |
| POSSUI_CARGA_INICIAL_BR_CLIENT | bit(1) |  |  | Possui a FRP de carga inicial BRClient |
| POSSUI_CADASTRO_EMP_BR_CLIENT | bit(1) |  |  | Possui a FRP de cadastro BRClient |
| POSSUI_MODULO_PORTAL_DO_CLIENTE | bit(1) |  | S | Possui a FRP Applications\BRAtendimento. 0 - Nao , 1 - Sim , NULL - Opcao para forcar a atualizacao da coluna |
| CONECTADO_DOMINIO_INOVA | bit(1) |  | S | Ja integrou alguma vez com Dominio Inova. 0 - Nao , 1 - Sim |
| POSSUI_MUDANCA_PORTAL_EMPREGADO | bit(1) |  |  | Possui IAC BR_EnablePublishingPublicLink ou FRP OnvioBR.EnablePublishingPublicLink |
| POSSUI_APP_PARA_VOCE | bit(1) |  |  | Possui IAC BR_NewEmployeePortal ou FRP OnvioBR.NewEmployeePortal |
| POSSUI_ENVIO_CERTIFICADO | bit(1) |  | S | Possui FRP certificado |
| POSSUI_PRODUTO_CERTIFICADO | bit(1) |  | S | Possui Produto Certificado |
