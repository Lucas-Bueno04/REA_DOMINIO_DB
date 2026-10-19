# LRTABELA_GRUPO_IRPJ_EXCLUSAO_SEGURADORA — Tabela grupos de Exclusões da IRPJ - Seguradoras ou Entidades Abertas de Previdência Complementar
157 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_GRUPO_IRPJ_EXCLUSAO_S | integer(4) | PK |  | Código |
| CODIGO_ECF | varchar(10) |  |  | Código SPED ECF |
| DESCRICAO | varchar(512) |  |  | Descrição |
| VALIDADE_INICIO | date(4) |  | S | Ínicio validade |
| VALIDADE_FIM | date(4) |  | S | Fim validade |
| IMPORTA_CONTAS_PARTE_B | char(1) |  |  | Importar somente contas de relacionamento com parte B |
