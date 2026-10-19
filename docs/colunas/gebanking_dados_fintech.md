# GEBANKING_DADOS_FINTECH — Configuracao de feature flags para integracao com a Fintech por empresa
1.969 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| COMPANY_ID | uniqueidentifier(16) | PK |  | Guid do escritorio |
| CODI_EMP | integer(4) | PK |  | Codigo da empresa |
| CLIENT_ID | uniqueidentifier(16) |  | S | Guid da empresa |
| FEATURE_FLAG_BENEFICIOS | bit(1) |  |  | Flag para ativar nova integracao de beneficios (0=Desativado, 1=Ativado) |
| DATA_HORA_FEATURE_FLAG | timestamp(8) |  | S | Data e hora da ativacao da feature flag de beneficios |
| CARGA_INICIAL_EMPLOYEES_EXECUTADA | bit(1) |  |  | Flag para controle de execucao da carga inicial de empregados (0=Nao Executada, 1=Executada) |
| DATA_HORA_CARGA_INICIAL | timestamp(8) |  | S | Data e hora da execucao da carga inicial de empregados |
| USA_PORTAL_EMPREGADO | bit(1) |  |  | Flag para controle de uso do portal do empregado (0=Nao, 1=Sim) |
| DATA_HORA_PORTAL_EMPREGADO | timestamp(8) |  | S | Data e hora da ativacao ou inativacao do portal do empregado |
| ENVIO_CARGA_INICIAL_PORTAL_EMPREGADO | bit(1) |  |  | Flag indicando se carga inicial de empregados por motivo portal foi enviada para esta empresa (0=Nao, 1=Sim) |
| DATA_HORA_ENVIO_CARGA_INICIAL_PORTAL_EMPREGADO | timestamp(8) |  | S | Data e hora do envio da carga inicial do portal do empregado |
| ENVIO_CARGA_INICIAL_PORTAL_BENEFICIO | bit(1) |  |  | Flag indicando se carga inicial de beneficios foi enviada para esta empresa (0=Nao, 1=Sim) |
| DATA_HORA_ENVIO_CARGA_INICIAL_BENEFICIO | timestamp(8) |  | S | Data e hora do envio da carga inicial do beneficio. |
