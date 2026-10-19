# FOESOCIAL_IMPORTACOES_MENSAGENS — Mensagens e validações provenientes de telas de cadastros e outros processos do contábil à importação do eSocial.
3.080 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_MENSAGENS | integer(4) | PK |  | Código da mensagem. |
| ORIGEM | smallint(2) |  |  | A tela ou processo que originou a mensagem. |
| TABELA_DADOS | varchar(128) |  | S | Tabela do sistema Contábil representado pela origem. |
| CHAVE_TABELA_DADOS | varchar(1024) |  | S | Chave da tabela do sistema Contábil representado pela origem. |
| CHAVE_TABELA_DADOS_IMPORTACAO | varchar(1024) |  | S | Chave do registro a ser importado do eSocial. |
| TITULO | varchar(64) |  |  | Título da mensagem. |
| MENSAGEM | varchar(1024) |  |  | Mensagem. |
| TIPO | smallint(2) |  |  | Tipo da mensagem. (1=Aviso/2=Alerta/3=Erro/4=Pergunta) |
| OPCAO_SELECIONADA | smallint(2) |  |  | Opção selecionada. (1=Ok/2=Sim/3=Não/4=Cancelar) |
| ACAO | smallint(2) |  |  | Ação à importação. (1=Ignorar/2=Bloquear) |
| DATA_REGISTRO | timestamp(8) |  |  | Data do registro. |
| VERIFICADO | smallint(2) |  |  | Indica se a mensagem foi verificada pelo usuário. (0=Não/1=Sim) |
| CODIGO_SOLUCAO | varchar(4) |  | S | Código da solução se a mensagem carregá-la consigo. |
