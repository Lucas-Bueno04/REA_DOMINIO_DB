# GEATENDIMENTO_DADOS_ESCRITORIO — Dados obtidos do SGD à respeito do escritório
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO_CLIENTE | integer(4) | PK |  | Código do cliente do SGD |
| SITUACAO | smallint(2) |  |  | Situação do ambiente utilizado do Atendimento: 1 - Ambiente DA, 5 - Ambiente Onvio nativo, 6 - Convertido SGD x Onvio, 7 - Em Processo de migração sem dados, 8 - Migrado Onvio sem dados, 9 - Ambiente Onvio Migrado com Dados, 10 - Cliente reativou contrato com Portal do Cliente |
| USUARIOS_EM_CONVERSAO_SGD | bit(1) |  |  | Indica que os usuários do SGD estão em conversão para o Onvio |
| ESTAGIO_MIGRACAO_COM_DADOS | integer(4) |  |  | 0 - Sem migração cadastrada, 1 - Iniciar migração DA Onvio, 2 - Sincronização DA iniciada, 3 - Sincronização DA finalizada, 5 - Sincronização DA com erro, 10 - Migração Swift iniciada, 11 - Migração Swift finalizada, 15 - Migração Swift com erro, 20 - Sincronização de códigos Swift iniciada, 21 - Sincronização de códigos Swift finalizada, 25 - Sincronização de códigos Swift com erro, 30 - Swift enviar e-mail iniciado, 31 - Swift enviar e-mail finalizado, 35 - Swift enviar e-mail erro, 40 - Swift interromper migração iniciado, 41 - Swift interromper migração finalizado, 45 - Swift interromper migração erro, 50 - Swift Rollback iniciado, 51 - Swift Rollback finalizado, 55 - Swift Rollback erro, 60 - Agente Rollback iniciado, 61 - Agente Rollback finalizado, 65 - Agente Rollback erro |
| ESTAGIO_MIGRACAO_COM_DADOS_TEMP | integer(4) |  |  | 0 - Sem migração cadastrada, 1 - Iniciar migração DA Onvio, 2 - Sincronização DA iniciada, 3 - Sincronização DA finalizada, 5 - Sincronização DA com erro, 10 - Migração Swift iniciada, 11 - Migração Swift finalizada, 15 - Migração Swift com erro, 20 - Sincronização de códigos Swift iniciada, 21 - Sincronização de códigos Swift finalizada, 25 - Sincronização de códigos Swift com erro, 30 - Swift enviar e-mail iniciado, 31 - Swift enviar e-mail finalizado, 35 - Swift enviar e-mail erro, 40 - Swift interromper migração iniciado, 41 - Swift interromper migração finalizado, 45 - Swift interromper migração erro, 50 - Swift Rollback iniciado, 51 - Swift Rollback finalizado, 55 - Swift Rollback erro, 60 - Agente Rollback iniciado, 61 - Agente Rollback finalizado, 65 - Agente Rollback erro |
| DATA_HORA_ENTRADA_ESTAGIO_SWIFT | timestamp(8) |  | S | Data e hora no fuso horário do Onvio |
| ULTIMO_SEQUENCIAL_NFE_DISPONIVEL_LEGADO | bigint(8) |  |  |  |
| ULTIMO_SEQUENCIAL_NFE_BAIXADO_LEGADO | bigint(8) |  |  |  |
| BOXE_ATIVO | integer(4) |  | S | Informação de se o cliente usa manifesto ou BOX-e, campo criado pois informação da tabela GEATENDIMENTO_ESCRITORIO não considera manifesto |
