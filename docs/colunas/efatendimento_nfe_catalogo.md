# EFATENDIMENTO_NFE_CATALOGO — Catálogo de Notas - Domínio Atendimento
67.201 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CATALOGO | integer(4) | PK |  | Código do catálogo |
| CODI_EMP | integer(4) |  |  | Empresa |
| SEQUENCIAL | bigint(8) |  | S | Código sequencial do site |
| TIPO | smallint(2) |  |  | Tipo da nota (1=Entrada/2=SaÃ­da/3=Cancelamento/4=ServiÃ§o/5=Outros) |
| EMISSAO | date(4) |  |  | Data de emissão da nota |
| BAIXADO | smallint(2) |  |  | Baixa do arquivo (0=Download do XML ainda não realizado/1=Download do XML já realizado) |
| IMPORTADA | smallint(2) |  |  | Importação do arquivo (0=Nota ainda não importada para a Escrita/1=Nota já importada para a Escrita) |
| CHAVE | varchar(256) |  | S | Chave |
| DATA_BAIXADO | date(4) |  | S | Data que o xml foi baixado |
| ORIGEM_XML | smallint(2) |  | S | Tipo da nota (1=Baixado automaticamente/2=Baixado pelo utilitários/3=Baixado automaticamente pela Consulta NF-e SEFAZ RS/4=Baixado automaticamente pela Importação NF-e via Web Service Portal Federal) |
| XML_EXCLUIDO | smallint(2) |  |  | Exclusão do XML (0=Não excluído/1=Excluído) |
| TIPO_NOTA | integer(4) |  | S | Tipo da nota (1=NFe, 2=CTe, 3=NFCe, 4=CFe, 5=Baixa de parcela, 6=NFSe, 7=Impostos Escrita, 8=Encargos Folha, 9=Pagamentos Folha, 14=NFSe Padrão Nacional) |
| ORIGEM_ATENDIMENTO | integer(4) |  |  | Flag que indica se o registro vem do DA(1) ou não (0) |
| GUID_ONVIO_EMPRESA | uniqueidentifier(16) |  | S | Identificador único da empresa banco do Atendimento Onvio |
| DATA_HORA_REGISTRO_ONVIO | timestamp(8) |  | S | Data e hora da criação/última alteração do registro da nota no Onvio |
| TIPO_ENDPOINT | tinyint(1) |  |  | 0 - Registro DA antigo, 1 - ServiÃ§o Onvio Boxe, 2 - ServiÃ§o Onvio Manifesto, 3 - ServiÃ§o Onvio API, 4 - Conta Azul |
| NOTA_ENTRADA | tinyint(1) |  |  | 0 - Nota de Saída, 1 - Nota de Entrada (uso interno agente de comunicação) |
| NOTA_CANCELADA | tinyint(1) |  |  | 0 - Nota regular, 1 - Nota cancelada (uso interno agente de comunicação) |
| URL_XML_NOTA | varchar(1024) |  | S | URL de download do XML da nota |
| URL_XML_CANCELAMENTO | varchar(1024) |  | S | URL de download do XML do cancelamento |
| XML_EXCLUIDO_MANUALMENTE | tinyint(1) |  |  | 0 - Não, 1 - Sim |
| ENVIOU_BOXE | char(1) |  | S | Nota foi enviada ao box-e |
| QUANTIDADE_TENTATIVAS_BOXE | integer(4) |  | S | Quantidade de tentativas de envios ao box-e |
| PROTOCOLO_BOXE | varchar(30) |  | S | Protocolo |
| GUID_INVOICE_INTEGRATION | uniqueidentifier(16) |  | S | Identificador único da nota no banco da Invoice Integration API |
| MOTIVO_BOXE | varchar(1024) |  | S | Motivo |
| NSU_NOTA | numeric(15) |  | S | NSU Nota |
| CODIGO_PROCESSO_AUDITOR | integer(4) |  | S | Código do processo criado no Auditor ASIS |
| STATUS_ASIS | integer(4) |  | S | Status do arquivo no Auditor ASIS (0=Ignorar,1=Pendente,2=Enviado,3=Contrato inativo) |
| URL_XML_COMPLEMENTO | varchar(1024) |  | S | URL de download do XML do complemento |
| COMPLEMENTO_BAIXADO | smallint(2) |  |  | Baixa do arquivo complementar (0=Download do XML ainda nÃ£o realizado/1=Download do XML jÃ¡ realizado) |
| COMPLEMENTO_DATA_BAIXADO | date(4) |  | S | Data que o xml complementar foi baixado |
| PARCEIRO | varchar(50) |  | S | Parceiro |
