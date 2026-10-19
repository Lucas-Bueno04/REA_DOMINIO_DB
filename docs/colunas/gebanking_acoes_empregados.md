# GEBANKING_ACOES_EMPREGADOS — Controle de acoes de empregados para integracao com FinTech
1.420 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Codigo sequencial do registro |
| COMPANY_ID | uniqueidentifier(16) |  |  | Guid do escritorio |
| CLIENT_ID | uniqueidentifier(16) |  |  | Guid da empresa |
| CODI_EMP | integer(4) |  |  | Codigo da empresa |
| BANKING_EMPLOYEE_ID | uniqueidentifier(16) |  | S | Identificador do empregado na Fintech |
| I_EMPREGADOS | integer(4) |  |  | Codigo do empregado |
| CPF | char(11) |  |  | CPF do empregado |
| EVENT_TYPE | varchar(20) |  |  | Tipo de evento (CREATE, UPDATE, DELETE) |
| PROCESSADO | bit(1) |  |  | Indica se o registro foi processado 0- Não Processado/1-Processado |
| DATA_HORA | timestamp(8) |  |  | Data e hora da criacao do registro |
| NUMERO_TENTATIVAS | integer(4) |  |  | Numero de tentativas de processamento que falharam |
| DATA_HORA_ULTIMA_TENTATIVA | timestamp(8) |  | S | Data e hora da ultima tentativa de processamento |
