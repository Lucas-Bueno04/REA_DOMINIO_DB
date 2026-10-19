# fosindicatospatronal — Sindicato - Cadastro - Patronal
34 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_sindicatos_p | integer(4) | PK |  | Código do sindicato patronal |
| nome | varchar(115) |  |  | nome |
| cgc | char(18) |  | S | CNPJ |
| endereco | char(40) |  | S | Endereco |
| numero | integer(4) |  | S | Numero |
| bairro | char(30) |  | S | Bairro |
| complemento | char(25) |  | S | Complemento |
| cep | char(8) |  | S | CEP |
| cidade | char(40) |  | S | Cidade |
| estado | char(2) |  | S | Estado |
| fone | char(15) |  | S | Fone |
| fax | char(15) |  | S | Fax |
| agencia | integer(4) |  | S | Agência |
| tipo_entidade | tinyint(1) |  |  | Tipo da entidade 1=Sindicato, 2=Federacao, 3=Confederacao, 4=Cees |
| codi_entidade | char(15) |  |  | Codigo da entidade |
| i_fotabcalc_patronal | integer(4) |  | S | Codigo do sindicato patronal |
| EMAIL | char(255) |  | S | Correio eletrônico |
| PAGINA_INTERNET | char(40) |  | S | Endereço da página na Internet |
| APELIDO | char(20) |  | S | Apelido |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
