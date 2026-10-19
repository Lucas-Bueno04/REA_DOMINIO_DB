# foconfarquivocols — Colunas da Configuracao de Arquivos
30 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_confarquivo | integer(4) | PK |  | Codigo arquivo |
| i_codigo | integer(4) | PK |  | Codigo |
| i_tipo_reg | integer(4) | PK |  | Tipo Registro |
| i_sequencia | integer(4) | PK |  | Sequencia |
| nome | char(30) |  |  | Nome |
| campo | integer(4) |  |  | Campo |
| conteudo | varchar(255) |  |  | conteudo |
| tamanho | integer(4) |  |  | Tamanho |
| mascara | varchar(255) |  |  | Mascara |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
