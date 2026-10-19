# LRTABELA_GRUPO_IRPJ_EXCLUSAO_GERAL — Tabela grupos de Exclusões da IRPJ - Geral
355 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_GRUPO_IRPJ_EXCLUSAO_GERAL | integer(4) | PK |  | Código |
| CODIGO_ECF_GERAL | varchar(10) |  |  | Código SPED ECF Geral |
| CODIGO_ECF_RURAL | varchar(10) |  |  | Código SPED ECF Rural |
| DESCRICAO | varchar(512) |  |  | Descrição |
| VALIDADE_INICIO | date(4) |  | S | Ínicio validade |
| VALIDADE_FIM | date(4) |  | S | Fim validade |
| IMPORTA_CONTAS_PARTE_B | char(1) |  |  | Importar somente contas de relacionamento com parte B |
