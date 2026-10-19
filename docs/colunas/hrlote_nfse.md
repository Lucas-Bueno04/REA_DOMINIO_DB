# HRLOTE_NFSE — Lotes para notas fiscais de servico eletronica emitidas
33.094 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_LOTE | integer(4) | PK |  | Lote |
| NUMERO_PROTOCOLO | varchar(100) |  |  | Numero do protocolo |
| DATA_HORA_ENVIO | timestamp(8) |  |  | Data e hora de envio |
| DATA_HORA_ULTIMA_CONSULTA | timestamp(8) |  |  | Data e hora da ultima consulta |
| SITUACAO | tinyint(1) |  |  | Situacao do lote (0=Enviado/ 1=Nao Recebido/ 2=Nao Processado/ 3=Processado com Erro/ 4=Processado com Sucesso/ 5=Aguardando assinatura) |
| DESCRICAO | varchar(128) |  | S | DescriÃ§Ã£o do lote |
| NFSE_AMBIENTE_ENVIO | char(1) |  |  | NFSE - Ambiente de envio |
| I_SEQUENCIAL_LOTE | integer(4) |  | S | Sequencial do Lote. |
| NUMERO_LOTE_ENVIO | integer(4) |  |  | Numero do Lote de envio. |
| I_SEQUENCIAL_LOTE_NACIONAL | integer(4) |  | S | Sequencial do Lote NFSe Nacional |
