# FOENCARGO_SIMPLES_DOMESTICO_RESCISORIO — Tabela do encargo rescisório do simples doméstico.
260 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| TIPO | integer(4) | PK |  | Tipo da rescisão. |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo da rescisão - Renomeado |
| BASE_CALCULO | numeric(13) |  |  | Base de cálculo |
| VALOR_FGTS | numeric(13) |  |  | Valor do FGTS. |
| VALOR_INDENIZACAO | numeric(13) |  |  | Valor de indenização |
| VALOR_TOTAL | numeric(13) |  |  | Valor total da guia |
| I_PAGTO | integer(4) |  | S | Código do pagamento. |
| VENCIMENTO | date(4) |  |  | Data de vencimento |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo da rescisão. |
