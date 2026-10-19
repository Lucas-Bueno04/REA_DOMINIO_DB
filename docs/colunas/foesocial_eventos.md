# FOESOCIAL_EVENTOS — Eventos do e-Social
44 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_EVENTO_ESOCIAL | integer(4) | PK |  | Código do evento do e-Social |
| DESCRICAO | varchar(50) |  |  | Descrição do evento do e-Social |
| GRUPO | smallint(2) |  | S | Grupo (1=Iniciais e Tabelas/2=Não periódicos/3=Periódicos) |
| ORDEM | smallint(2) |  |  | Ordem de envio do evento para o eSocial. |
| GERAR_AUTOMATICO | smallint(2) |  |  | Gerar automaticamento quando antecessor for validado. |
| RETORNO_SIMULACAO | smallint(2) |  |  | Sem uso. |
| VALIDAR_SEM_RECIBO | smallint(2) |  |  | Validar sem recibo quando retornar código 537 |
