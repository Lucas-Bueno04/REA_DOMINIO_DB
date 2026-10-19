# FOESOCIAL_IMPORTACOES_COLABORADORES — Colaboradores a serem importados do site do eSocial.
536 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| CPF | varchar(11) |  |  | CPF do colaborador. |
| DATA_ADMISSAO | date(4) |  |  | Data de admissão do colaborador. |
| TIPO_COLABORADOR | smallint(2) |  |  | Tipo do colaborador. (1=Empregado/2=Estagiário/3=Contribuinte) |
| IMPORTADO | smallint(2) |  |  | Colaborador importado. (0=Não/1=Sim) |
| CATEGORIA_ESOCIAL | integer(4) |  | S | Código da categoria eSocial. |
| I_COLABORADORES | integer(4) | PK |  | Código do colaborador. |
