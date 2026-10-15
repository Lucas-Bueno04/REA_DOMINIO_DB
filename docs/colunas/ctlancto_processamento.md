# CTLANCTO_PROCESSAMENTO — Tabela de controle de processamento de saldos contábeis
0 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) |  |  | Código da empresa |
| CODI_EMP_PLANO | integer(4) |  |  | Código da empresa do plano de contas |
| FILI_LAN | integer(4) |  |  | Filial do lançamento |
| CODI_CTA | integer(4) |  |  | Código da conta contábil |
| DATA_LAN | date(4) |  |  | Data do lançamento |
| ORIG_LAN | tinyint(1) |  |  | Origem do lançamento |
| CONNECTION_ID | integer(4) |  |  | ID da conexão que fez o INSERT |
| ID_PROCESSAMENTO | uniqueidentifier(16) | PK |  | Identificador único do registro de processamento |
