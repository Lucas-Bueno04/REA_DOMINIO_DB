# fotabelas — Tabelas
546 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_tabelas | integer(4) | PK |  | Tipo de tabela (1=Estabilidades/2=Locais de trabalho/4=Descrição de Serviço RPA/5=Motivos de alteração salarial/6=Pagamentos do INSS/7=Nível salarial/9=Motivos de resilição professor) |
| i_codigo | integer(4) | PK |  | Sequencial |
| nome | char(100) |  |  | Descricao conteudo campo |
| aux1 | varchar(40) |  | S | Auxiliar1 |
| aux2 | varchar(40) |  | S | Auxiliar2 |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
