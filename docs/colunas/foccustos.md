# foccustos — Centro de Custos - Cadastro
1.629 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_ccustos | integer(4) | PK |  | Codigo |
| nome | varchar(85) |  |  | Nome |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| USOU_EPI_POR_INVIABILIDADE_APOS_TENTATIVA_IMPLEMENTACAO_MEDIDAS_PROTECAO_COLETIVA | smallint(2) |  |  | Houve tentativa de implementação de medidas de proteção coletiva antes da opção pelo EPI. (0=Não/1=Sim) |
| FORAM_OBSERVADAS_CONDICOES_FUNCIONAMENTO_USO_EPI_CONFORME_ESPECIFICACAO_FABRICANTE | smallint(2) |  |  | Foram observadas as condições de funcionamento e do uso ininterrupto do EPI conforme especificação do fabricante. (0=Não/1=Sim) |
| FOI_OBSERVADO_PRAZO_VALIDADE_CONFORME_CERTIFICADO_APROVAVAO_MTE | smallint(2) |  |  | Foi observado o prazo de validade, conforme Certificado de Aprovação-CA do MTE. (0=Não/1=Sim) |
| FOI_OBSERVADA_PERIODICIDADE_TROCA_DEFINIDA_PROGRAMAS_AMBIENTAIS | smallint(2) |  |  | Foi observada a periodicidade de troca definida pelos programas ambientais. (0=Não/1=Sim) |
| FOI_OBSERVADA_HIGIENIZACAO | smallint(2) |  |  | Foi observada a higienização. (0=Não/1=Sim) |
| TIPO | smallint(2) |  | S | Tipo de centro de custos. (1-Sintético/2=Analítico) |
| I_CCUSTOS_SINTETICO | integer(4) |  | S | Código do centro de custos sintético. |
| MASCARA | varchar(50) |  | S | Mascara de ordenação da consulta. |
| GUID_CONTABIL | uniqueidentifier(16) |  |  | Identificador único do registro no banco do Contábil |
| GUID_ONVIO | uniqueidentifier(16) |  | S | Identificador único do registro no banco do Atendimento Onvio |
| ENDPOINT_EXCLUSAO | varchar(1024) |  | S | Endpoint utilizado para a exclusão do registro. |
