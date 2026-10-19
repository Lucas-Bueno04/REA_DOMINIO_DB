# FOEMPRESTIMOS_CONSIGNADOS_IMPORTACAO — Empréstimos consignados realizados pela importação de arquivos.
2.832 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| I_BANCOS | integer(4) | PK |  | Código do banco. |
| COMPETENCIA_DESCONTO | date(4) | PK |  | Competência de desconto. |
| VALOR_PARCELA | numeric(13) |  |  | Valor da parcela. |
| NUMERO_CONTRATO | varchar(15) | PK |  | Número do contrato. |
| DATA_INICIO_CONTRATO | date(4) |  |  | Data de início do contrato. |
| DATA_FIM_CONTRATO | date(4) |  |  | Data de término do contrato. |
| DATA_INICIO_DESCONTO | date(4) |  |  | Data de início de desconto da parcela. |
| NUMERO_PARCELAS | smallint(2) |  |  | Número de parcelas. |
| VALOR_TOTAL | numeric(13) |  |  | Valor total do empréstimo. |
| I_USUARIO | integer(4) |  | S | Usuário que realizou o processo de importação. |
| DATA_IMPORTACAO | timestamp(8) |  | S | data que o arquivo foi importado. |
| NOME_ARQUIVO | varchar(255) |  | S | Arquivo que foi processado as informações. |
