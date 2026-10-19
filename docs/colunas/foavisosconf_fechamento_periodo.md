# FOAVISOSCONF_FECHAMENTO_PERIODO — Configurações do aviso de competências sem fechamento no eSocial
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_AVISOSCONF | integer(4) | PK |  | Código do aviso de vencimento. |
| TIPO_CALCULO | smallint(2) | PK |  | Tipo de cálculo. (0=Folha Mensal/1=Folha Anual) |
| EXIBIR_AVISO | smallint(2) |  |  | Exibir aviso. (0=Não/1=Sim) |
| DIAS_ANTECEDENCIA | integer(4) |  | S | Dias de antecedência para exibir o aviso. |
