# FOMONITORAMENTO_SAUDE_TRABALHADOR_EXAMES — Monitoramento da Saúde do Trabalhador - Exames realizados.
190 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| SEQUENCIAL | integer(4) | PK |  | Código sequencial. |
| SEQUENCIAL_EXAME | integer(4) | PK |  | Código sequencial do exame. |
| DATA_EXAME | date(4) |  |  | Data do exame. |
| I_EXAMES | integer(4) |  |  | Código do exame. |
| ORDEM_EXAME | smallint(2) |  |  | Ordem do exame (0=Não aplicável, 1=Inicial, 2=Sequencial) |
| INDICACAO_RESULTADOS | smallint(2) |  | S | Indicação dos resultados (1=Normal/2=Alterado/3=Estável/4=Agravamento). |
| OBSERVACAO | varchar(999) |  | S | Observação. |
