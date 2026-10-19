# FOMODELOS_ETIQUETAS_CTPS — Modelos das etiquetas de atualização da CTPS.
6 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_MODELO | integer(4) | PK |  | Código do modelo. |
| TIPO | smallint(2) |  |  | Tipo de modelo. (1=Contrato de trabalho/2=Contrato de experiência/3=Alteração de salário/4=Anotações de férias/5=Alteração de cargo/6=Livre) |
| TEXTO | long varchar(32767) |  |  | Texto. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
