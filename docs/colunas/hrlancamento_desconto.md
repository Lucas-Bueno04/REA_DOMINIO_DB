# HRLANCAMENTO_DESCONTO — Lancamentos de descontos
291 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_CLIENTE | integer(4) | PK |  | Cliente |
| I_DESCONTO | integer(4) | PK |  | Codigo |
| COMPETENCIA | date(4) |  |  | Competencia |
| I_RECEBER | integer(4) |  | S | Lancamento receber |
| I_CONTRATO | integer(4) |  | S | Contrato |
| ADICIONAL_ANUAL | char(1) |  | S | O desconto e para o adicional anual S N |
| TIPO_LANCAMENTO | char(1) |  |  | Tipo de lancamento V Valor P Percentual |
| VALOR_PERCENTUAL | numeric(13) |  |  | Valor ou percentual |
| HISTORICO | varchar(100) |  |  | Historico |
| ENCERRAR | char(1) |  |  | Definir encerramento do desconto (S/N) |
| DATA_ENCERRAMENTO | date(4) |  | S | Data de encerramento do desconto |
| ORIGEM | char(1) |  |  | Origem do desconto (C=Competência/ P=Período) |
| DATA_LANCAMENTO | date(4) |  | S | Data de lançamento |
