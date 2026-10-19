# FOGUIA_INSS_SERVICOS_VALORES — Valores de encargos de INSS pagos por serviço.
117.690 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_SERVICOS | integer(4) | PK |  | Código do Serviço |
| I_GUIAINSS_OLD | integer(4) |  | S | Código da guia do INSS - Renomeado |
| TIPO_VALOR | smallint(2) | PK |  | Tipo de valor. (1=Terceiros/2=INSS Frete/3=INSS Empresa empregados/4=INSS Empresa contribuintes/5=RAT/6=RAT Especial 15 anos/7=RAT Especial 20 anos/8=RAT Especial 25 anos) |
| PERCENTUAL | numeric(7) |  |  | Percentual. |
| VALOR | numeric(13) |  |  | Valor. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
| BASE_CALCULO | numeric(15) |  |  | Base de cálculo. |
| VALOR_AVISO_PREVIO | numeric(13) |  |  | Valor Aviso Prévio |
| BASE_CALCULO_AVISO_PREVIO | numeric(15) |  |  | Base de cálculo Aviso Prévio |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_GUIAINSS | uniqueidentifier(16) | PK |  | Código da guia do INSS |
