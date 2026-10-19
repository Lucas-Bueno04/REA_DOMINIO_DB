# GEATENDIMENTO_BANCOS_ICEBERG — Cadastro de Instituições Financeiras para o Iceberg
15 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO_BANCO | integer(4) | PK |  | Código da Instituição Financeira |
| DESCRICAO_BANCO | varchar(100) |  |  | Nome da Instituição Financeira |
| NOME_BANCO | varchar(100) |  |  | Identificador da Instituição Financeira |
| NUMERO_CODIGO_BC | char(3) |  | S | Identificador do Banco Central para participantes do Sistema de Transferências de Reservas. |
| CONEXAO_DIRETA | integer(4) |  | S | Informa se a instituição usa conexão direta |
