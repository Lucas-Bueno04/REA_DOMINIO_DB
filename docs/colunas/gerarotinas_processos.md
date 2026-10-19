# GERAROTINAS_PROCESSOS — PROCESSOS DAS ROTINAS AUTOMÁTICAS
53.754 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_ROTINAS | integer(4) | PK |  | CÓDIGO DA ROTINA |
| I_SISTEMA | smallint(2) | PK |  | CÓDIGO DO SISTEMA |
| I_PROCESSOS | smallint(2) | PK |  | CÓDIGO DO PROCESSO: (1-140) |
| SELECIONADO | smallint(2) |  |  | SELECIONADO |
| OPCOES_TELA | varchar(32000) |  |  | OPÇÕES DA TELA |
