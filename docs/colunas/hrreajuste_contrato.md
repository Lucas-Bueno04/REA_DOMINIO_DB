# HRREAJUSTE_CONTRATO — Reajuste de contratos
2.979 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_CONTRATO | integer(4) | PK |  | Contrato |
| COMPETENCIA | date(4) | PK |  | Competencia |
| DATA_REAJUSTE | date(4) |  |  | Data que ocorreu o reajuste |
| DATA_VENCIMENTO | date(4) |  |  | Compentencia em que o contrato deveria ter sido reajustado |
| I_HISTORICO | integer(4) |  | S | Codigo do historico |
| HISTORICO | varchar(512) |  |  | Historico |
| FORMA_REAJUSTE | char(1) |  |  | Forma de reajuste P Percentual A Adicionar valor N Novo valor C Conforme o valor do indice |
| VALOR_APLICADO | numeric(13) |  |  | Valor aplicado ao contrato |
| VALOR_NOVO_CONTRATO | numeric(13) |  |  | Novo valor do contrato apos reajuste |
| VALOR_ANTERIOR_REAJUSTE | numeric(13) |  |  | Valor do contrato antes do reajuste |
