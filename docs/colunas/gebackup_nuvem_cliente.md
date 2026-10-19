# GEBACKUP_NUVEM_CLIENTE — Tabela com os dados do cliente.
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Código do cliente no SGD. |
| SITUACAO_CONTRATO | integer(4) |  |  | Situação do contrato: 1 - Ativo, 0 - Sem contrato, -1 - Cancelado. |
| DATA_ATIVACAO | date(4) |  | S | Data de ativação do contrato. |
| DATA_CANCELAMENTO | date(4) |  | S | Data de cancelamento do contrato. |
