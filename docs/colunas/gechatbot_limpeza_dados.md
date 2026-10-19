# GECHATBOT_LIMPEZA_DADOS — Controla quando deve limpar os dados referente ao chatbot quando houver cancelamento, downgrade ou cessão de direitos envolvendo FRP no Onvio Messenger
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CHAVE | integer(4) | PK |  |  |
| STATUS_LIMPEZA_DADOS | tinyint(1) |  |  | 0 - Não executar limpeza, 1 - Executar limpeza, 2 - Limpeza concluída |
| DATA_SOLICITACAO_LIMPEZA | date(4) |  | S | Data em que foi recebida a informação que o contrato não tem mais acesso ao chatbot |
| DATA_ULTIMA_LIMPEZA | date(4) |  | S | Data da última limpeza de dados executada. |
