# PCMOVIMENTO_ATIVIDADE — Movimentos atividades
61 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_VINCULO | integer(4) | PK |  | Código do vínculo |
| I_SEQUENCIAL_ATIVIDADE | integer(4) | PK |  | Sequencial da atividade |
| I_SEQUENCIAL_MOVIMENTO | integer(4) | PK |  | Sequencial |
| DATA_INICIO | date(4) |  |  | Data de início |
| COMPETENCIA_REFERENCIA | date(4) |  |  | Competência de referência |
| DATA_VENCIMENTO_ORIGINAL | date(4) |  |  | Data de vencimento original |
| DATA_VENCIMENTO | date(4) |  |  | Data de vencimento |
| DATA_VENCIMENTO_LEGAL_ORIGINAL | date(4) |  | S | Data de vencimento legal original |
| DATA_VENCIMENTO_LEGAL | date(4) |  | S | Data de vencimento legal |
| CONCLUIDA | char(1) |  |  | Concluída (S/N) |
| DATAHORA_CONCLUSAO | timestamp(8) |  | S | Data e hora da conclusão |
| USUARIO_CONCLUSAO | varchar(30) |  | S | Usuário que concluiu |
| ANOTACAO | varchar(1000) |  | S | Anotação |
| DATA_VENCIMENTO_AVISO | date(4) |  | S | Data do vencimento do aviso |
| DATA_INICIO_AVISO | date(4) |  | S | Data que inicia o aviso |
| ALTERADO_INICIO_VENCIMENTO_UTILITARIO | tinyint(1) |  |  | Informar neste campo se o movimento foi alterado pelo utilitario "Alterar Unício e Vencimento das Atividades" |
