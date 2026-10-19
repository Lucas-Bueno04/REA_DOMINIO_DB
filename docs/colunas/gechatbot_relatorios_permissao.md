# GECHATBOT_RELATORIOS_PERMISSAO — Configuração de permissão de relatórios para o Assistente Virtual
32 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO_RELATORIO | integer(4) | PK |  | Código do relatório que a permissão esta relacionada. |
| DESCRICAO | varchar(256) |  |  | Descrição do nome do relatório. |
| MODULO | varchar(128) |  |  | Nome do módulo ao qual o relatório pertence. |
| MENU | varchar(128) |  |  | Descrição do menu ao qual o relatório pertence. |
| PERMITE_EMITIR | bit(1) |  |  | Informa se pode emitir o relatório pelo Agente de Execução do Assistente Virtual. 0 - NAO, 1 - SIM |
