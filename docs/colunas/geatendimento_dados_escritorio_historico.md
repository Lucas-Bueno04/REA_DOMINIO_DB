# GEATENDIMENTO_DADOS_ESCRITORIO_HISTORICO — Tabela de histórico de mudança da tabela GEATENDIMENTO_DADOS_ESCRITORIO
17 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| SEQUENCIAL | integer(4) | PK |  |  |
| CODIGO_CLIENTE | integer(4) |  |  |  |
| SITUACAO_ANTIGA | smallint(2) |  | S |  |
| SITUACAO_NOVA | smallint(2) |  |  |  |
| MENSAGEM_DETALHE | varchar(512) |  | S |  |
| DATA_HORA_MUDANCA_SITUACAO | timestamp(8) |  |  |  |
| ESTAGIO_MIGRACAO_COM_DADOS | integer(4) |  |  |  |
| DATA_HORA_ENTRADA_ESTAGIO_SWIFT | timestamp(8) |  | S | Data e hora no fuso horário do Onvio |
| ESTAGIO_MIGRACAO_COM_DADOS_TEMP | integer(4) |  |  |  |
| BOXE_ATIVO | integer(4) |  | S | Indica que o cliente possui boxe ativo ou empresas manifesto |
