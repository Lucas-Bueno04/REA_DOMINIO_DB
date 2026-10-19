# FOEMPRESTIMOS_CRED_TRAB_RESCISAO_API_RETORNO — Empréstimo Crédito do Trabalhador - Retorno Consulta API
166 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_SEQUENCIAL | integer(4) | PK |  | Código sequencial da tabela |
| CODI_EMP | integer(4) |  |  | Codigo da empresa |
| COMPETENCIA | date(4) |  |  | Competencia da rescisao |
| I_EMPREGADOS | integer(4) |  |  | Codigo do empregado |
| MENSAGEM | varchar(1000) |  | S | Mensagem |
| JSON_RESPOSTA | long varchar(32767) |  | S | Json de retorno da API |
| DATA_CONSULTA_API | timestamp(8) |  |  | Data da consulta a API do Credito do Trabalhador |
