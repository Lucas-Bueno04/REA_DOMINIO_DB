# FOMEMORIA_CALCULO_DIFERENCA — Memória de cálculo do cálculo da diferença
26.117 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CALCULOS_DIFERENCA_OLD | integer(4) |  | S | Código do cálculo da diferença - Renomeado |
| I_CALCULOS_AJUSTADO_OLD | integer(4) |  | S | Código do cálculo ajustado - Renomeado |
| DIFERENCA_CCT | smallint(2) |  |  | Cálculo de diferença CCT.(0=Não/1=Sim) |
| ANTECIPACAO_SALARIAL | smallint(2) |  |  | Diferença referente a antecipação salarial.(0=Não/1=Sim) |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de leiaute/3=Conversão) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS_AJUSTADO | uniqueidentifier(16) | PK |  | Código do cálculo ajustado |
| I_CALCULOS_DIFERENCA | uniqueidentifier(16) | PK |  | Código do cálculo da diferença |
