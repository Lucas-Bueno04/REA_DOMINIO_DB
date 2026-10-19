# FOPARAMETRO_THREAD — Informa se o sitema irá utilizar thread para processos de cálculo
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_PARAMETRO_THREAD | integer(4) | PK |  | Código do parâmetro. |
| UTILIZA_THREAD | smallint(2) |  |  | Utiliza thread. (0=Não/1=Sim). |
| TIPO_PROCESSAMENTO | tinyint(1) |  |  | 0 - Mínimo, 1 - Médio, 2 - Máximo, 3 - Definir |
| QUANTIDADE_THREADS | tinyint(1) |  |  | Número de threads para o tipo de processamento 3 - Definir |
