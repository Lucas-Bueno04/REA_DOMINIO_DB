# LRTABELA_GRUPO_IRPJ_EXCLUSAO_GERAL_VIGENCIA — TABELA DESCRICAO DO GRUPO IRPJ EXCLUSAO GERAL POR VIGENCIA
720 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_GRUPO_IRPJ_EXCLUSAO_GERAL | integer(4) | PK |  | Código sequencial com referencia a tabela LRTABELA_GRUPO_IRPJ_EXCLUSAO_GERAL |
| VIGENCIA | date(4) | PK |  | Vigencia da descrição |
| DESCRICAO | varchar(512) |  | S | Descrição utilizada na vigencia |
| IMPORTA_ADICAO_EXCLUSAO_PARTE_B | char(1) |  |  | Importar adições e exclusões de parte B |
| IMPORTA_CONTAS_PARTE_B | char(1) |  |  | Importar somente contas de relacionamento com parte B |
| TIPO_IMPORTACAO | char(15) |  |  | GUARDA O TIPO DE RELACIONAMENTO |
