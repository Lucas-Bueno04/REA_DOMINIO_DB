# GEDADOS_AUDITOR — Dados do Auditor Digital
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | tinyint(1) | PK |  | Chave primária |
| CODIGO_CONTROLE_ASIS | varchar(256) |  |  | Código identificador do contrato da ASIS. |
| CODIGO_CONTROLE_APLICACAO | varchar(256) |  |  | Código identificador da aplicação pareceira ASIS. |
| SITUACAO_CONTRATO | integer(4) |  |  | Situação do contrato: -1 - Inativo, 0 - Sem Contrato, 1 - Ativo, 2 - Em Processamento |
| SITUACAO_VERIFICACAO | integer(4) |  |  | Situação da verificação: 1 - Executando, 0 - Parada |
| INICIO_VERIFICAO | timestamp(8) |  | S | Horário do começo da última verificação. |
| FIM_VERIFICACAO | timestamp(8) |  | S | Horário do fim da última verificação. |
| LIBERACAO_VENDEDOR | integer(4) |  | S | Indica se a liberação é de vendedor. 0 - Não; 1 - Sim. |
| PRODUTO | integer(4) |  | S | Código do produto Auditor Fiscal utilizado pelo cliente |
