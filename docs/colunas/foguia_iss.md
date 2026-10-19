# FOGUIA_ISS — Guia do ISS
611 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_GUIA_ISS_OLD | integer(4) |  | S | Sequencial da guia - Renomeado |
| CODI_EMP | integer(4) |  |  | Código da empresa. |
| I_FILIAIS | integer(4) |  |  | Código da filial. |
| COMPETENCIA | date(4) |  |  | Competência. |
| DATA_VENCIMENTO | date(4) |  |  | Data de vencimento. |
| VALOR | numeric(13) |  |  | Valor da guia. |
| I_PAGTO | integer(4) |  | S | Sequencial de pagamento. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de leiaute/3=Conversão) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_GUIA_ISS | uniqueidentifier(16) | PK |  | Sequencial da guia. |
