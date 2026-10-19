# GEATENDIMENTOGRUPOEXECUCAO — Grupos de execução do Agente de Comunicação
62 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  |  |
| DESCRICAO_GRUPO | varchar(100) |  | S |  |
| TIPO | integer(4) |  |  | Tipo da thread (1=Envio/2=Recebimento) |
| MINUTOS | integer(4) |  |  |  |
| STATUS | integer(4) |  | S |  |
| TIPO_DESTINO | integer(4) |  | S | Tipos de destino (TIPOS DE DESTINO (1=DA/2=INTEGRA/3=SERVIÃ‡OS TREINAMENTO/4=ONBALANCE/5=ATENDIMENTO ONVIO/6=ESOCIAL/7=ASIS/8=ONVIO VIA OPERATIONS/9=CONTA AZUL/10=ONVIO MESSENGER/11=ONVIO WEBSOCKET/12=ICEBERG WEBSOCKET/13=BANKING/14=EFD-REINF/15=SGDNOTIFICACAO/16=QUANTUM/17=DOMINIO CONTA DIGITAL/18=BAIXAPARCELANF/19=FOLHA/20=ENVIO DE EVENTOS REFORMA)/21=INGESTÃƒO ESOCIAL/22=APURAÃ‡ÃƒO ASSISTIDA/23=DeRE/24=DOMÃ?NIO IA) |
| ORDEM_GUIA_AGENTE | integer(4) |  |  |  |
| ULTIMO_PROTOCOLO | integer(4) |  |  |  |
| MOSTRA_TABPAGE | integer(4) |  |  |  |
| GERA_MONITORIA | integer(4) |  |  | Coluna que indica se o grupo gera ações para monitoria quando der erro |
| ATIVO | bit(1) |  |  | 1 - Ativo, 0 - Inativo |
| PERMITE_INSERIR_ACOES | bit(1) |  |  | 1 - Permite inserção de ações para as tabelas filhas, 0 - Não permite inserção de ações para as tabelas filhas |
| UTILIZA_WEBSOCKET | bit(1) |  |  | Informa se utiliza WebSocket para comunicação. |
| UTILIZA_DOWNLOAD_API_ZIP | bit(1) |  |  | Informa se libera utilizacao do download de notas em zip apenas grupo API. |
