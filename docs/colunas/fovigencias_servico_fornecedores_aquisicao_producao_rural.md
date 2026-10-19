# FOVIGENCIAS_SERVICO_FORNECEDORES_AQUISICAO_PRODUCAO_RURAL — Fornecedores para importar notas fiscais de produção rural.
6 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_SERVICOS | integer(4) | PK |  | Código do serviço. |
| VIGENCIA | date(4) | PK |  | Vigência. |
| CODI_FOR | integer(4) | PK |  | Código do fornecedor. |
| SEQUENCIAL | integer(4) | PK |  | Sequencial. |
| COMPETENCIA_INICIO | date(4) |  |  | Competência início. |
| DETERMINAR_FIM | smallint(2) |  |  | Determinar fim. (0=Não/1=Sim) |
| COMPETENCIA_FIM | date(4) |  | S | Competência fim. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Imp. tabelas/2=Imp. layout/3=Imp. tabelas concorrentes) |
| CODI_EMP_FOR | integer(4) | PK |  | Codigo empresa fornecedor. |
