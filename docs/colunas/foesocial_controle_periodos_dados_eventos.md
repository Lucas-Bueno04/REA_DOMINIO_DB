# FOESOCIAL_CONTROLE_PERIODOS_DADOS_EVENTOS — Lista de envios de abertura/fechamento do período para o eSocial.
227 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| COMPETENCIA | date(4) | PK |  | Competência. |
| I_DADOS_EVENTOS | integer(4) | PK |  | Sequencial de envio ao eSocial. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Imp. tabelas/2=Imp. layout/3=Imp. tabelas concorrentes) |
