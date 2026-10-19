# FOFPAS — Tabela com códigos FPAS
1.475 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_FPAS | integer(4) | PK |  | Sequencial Tabela FPAS |
| CODIGO_FPAS | integer(4) |  |  | Código FPAS |
| DESCRICAO | varchar(12000) |  |  | Descrição FPAS |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro: 0=Sistema/1=Importação de tabelas/2=Importação de leiaute/3=Conversão |
