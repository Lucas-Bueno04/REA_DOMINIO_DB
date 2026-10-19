# EFIMPORTADOR_XML_PORTAL_FEDERAL — Configuração de Importação do Download do XML do Portal Federal
638 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| IMPORTAR_NOTAS_VIA_WEB_SERVICE | char(1) |  |  | Importar notas via Web Service |
| CERTIFICADO_DIGITAL | varchar(256) |  | S | CERTIFICADO DIGITAL - ENTRADA |
| CERTIFICADO_DIGITAL_A3 | char(1) |  |  | CERTIFICADO DIGITAL - TIPO A3 - ENTRADA |
| ENVIAR_NOTAS_ENTRADA_BOXE | char(1) |  |  | Enviar as notas de entrada para o BOX-e |
| ULTIMO_NSU_ENVIADO | numeric(15) |  |  | ÚLTIMO NSU ENVIADO - ENTRADA |
| LOCAL_DOWNLOAD_XML | char(1) |  |  | Downlaod do XML |
| ENVIAR_NOTAS_ENTRADA_BOXE_A_PARTIR | date(4) |  | S | Enviar as notas de entrada para o BOX-e a partir de |
| IMPORTAR_NOTAS_VIA_WEB_SERVICE_SAIDA | char(1) |  |  | Importar notas via Web Service - Saída |
| CERTIFICADO_DIGITAL_SAIDA | varchar(256) |  | S | Certificado digital  - Saída |
| CERTIFICADO_DIGITAL_A3_SAIDA | char(1) |  |  | Certificado digital - Tipo A3  - Saída |
| ENVIAR_NOTAS_SAIDA_BOXE | char(1) |  |  | Enviar as notas de saída para o BOX-e |
| ULTIMO_NSU_ENVIADO_SAIDA | numeric(15) |  |  | Último NSU enviado  - Saída |
| IMPORTAR_NOTAS_VIA_WEB_SERVICE_ENTRADA | char(1) |  |  | Importar notas via Web Service - Entrada |
| ENVIAR_NOTAS_SAIDA_BOXE_A_PARTIR | date(4) |  | S | Enviar as notas de saída para o Box-e a partir de |
| BUSCAR_CNPJ_CPF_SAIDA_DO | integer(4) |  |  | Campo para buscar CNPJ/CPF do certificado de saída |
| MANIFESTAR_NOTA_ENTRADA | varchar(1) |  |  | Manifestar nota de entrada. |
| IMPORTAR_CTE_VIA_WEB_SERVICE_ENTRADA | char(1) |  | S | Importar CT-es via Web Service |
| IMPORTAR_CTE_VIA_WEB_SERVICE_SAIDA | char(1) |  | S | Importar CT-es via Web Service - Saída |
| ENVIAR_CTE_ENTRADA_BOXE | char(1) |  | S | Enviar as CT-es de entrada para o BOX-e |
| ENVIAR_CTE_SAIDA_BOXE | char(1) |  | S | Enviar as CT-es de saída para o BOX-e |
| ENVIAR_CTE_ENTRADA_BOXE_A_PARTIR | date(4) |  | S | Enviar as CT-es de entrada para o BOX-e a partir de |
| ENVIAR_CTE_SAIDA_BOXE_A_PARTIR | date(4) |  | S | Enviar as CT-es de saída para o BOX-e a partir de |
| ULTIMO_NSU_ENVIADO_CTE_ENTRADA | numeric(15) |  | S | Último NSU enviado - Entrada - CT-e |
| ULTIMO_NSU_ENVIADO_CTE_SAIDA | numeric(15) |  | S | Último NSU enviado - Saída - CT-e |
| MANIFESTAR_CONFIRMACAO_OPERACAO | char(1) |  |  | Manifestar como Confirmação da Operação |
| IMPORTAR_NFSE_VIA_WEB_SERVICE_ENTRADA | char(1) |  |  | Importar NFS-es Entrada via Web Service |
| IMPORTAR_NFSE_VIA_WEB_SERVICE_SERVICO | char(1) |  |  | Importar NFS-es Serviço via Web Service |
| ENVIAR_NFSE_ENTRADA_BOXE | char(1) |  |  | Enviar as NFS-es de entrada para o BOX-e |
| ENVIAR_NFSE_SERVICO_BOXE | char(1) |  |  | Enviar as NFS-es de serviço para o BOX-e |
| ENVIAR_NFSE_ENTRADA_BOXE_A_PARTIR | date(4) |  | S | Enviar as NFS-es de entrada para o BOX-e a partir de |
| ENVIAR_NFSE_SERVICO_BOXE_A_PARTIR | date(4) |  | S | Enviar as NFS-es de serviço para o BOX-e a partir de |
| ULTIMO_NSU_ENVIADO_NFSE | numeric(15) |  | S | Último NSU enviado - NFS-e |
| IMPORTAR_NFCE_VIA_WEB_SERVICE_SAIDA | char(1) |  | S | Importar NFC-es via Web Service - Saída. |
| ENVIAR_NFCE_SAIDA_BOXE | char(1) |  | S | Enviar as NFC-es de saída para o BOX-e |
| ENVIAR_NFCE_SAIDA_BOXE_A_PARTIR | date(4) |  | S | Enviar as NFC-es de saída para o BOX-e a partir de |
| DATA_HORA_ULTIMO_NFCE_SAIDA | timestamp(8) |  | S | Data e hora da última nota retornada pelo webservice. |
| ULTIMO_NSU_ENVIADO_NFCE_SC | numeric(15) |  | S | Último NSU enviado - NFC-e SC |
