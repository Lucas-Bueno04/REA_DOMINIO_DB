# GESCP_QUADRO_SOCIETARIO_SOCIO — SCP - Quadro Societário - Sócios
36 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_SCP | integer(4) | PK |  | Sequencial do SCP |
| DATA | date(4) | PK |  | Data |
| I_SOCIO | integer(4) | PK |  | Sócio |
| TIPO | char(1) | PK |  | Tipo (S - Socio/A - Administrador/R - Representante Legal/E - Empresário) |
| ORDEM | integer(4) |  |  | Ordem |
| PARTICIPACAO | numeric(5) |  |  | Participação % |
| VALOR_QUOTA_INTEGRALIZADA | numeric(13) |  |  | Quotas integralizadas |
| VALOR_QUOTA_INTEGRALIZAR | numeric(13) |  |  | Quotas a integralizar |
| QUANTIDADE_QUOTAS | numeric(13) |  |  | Quantidade de quotas |
| VALOR_QUOTA | numeric(13) |  |  | Valor da quota |
| VALOR_CAPITAL_INTEGRALIZADO | numeric(13) |  |  | Capital integralizado |
| VALOR_CAPITAL_INTEGRALIZAR | numeric(13) |  |  | Capital a integralizar |
| MESES_PARA_INTEGRALIZACAO | integer(4) |  |  | Meses para integralização |
| CONDICAO | integer(4) |  |  | Condição |
| EXERCE_ATIVIDADE | integer(4) |  |  | Exerce atividade (1 - Sim/0 - Não) |
| CARGO | varchar(30) |  |  | Cargo |
| POSSUI_RESPONSAVEL_LEGAL | char(1) |  |  | Possui responsável legal (S/N) |
| DATA_INGRESSO | date(4) |  |  | Data de  ingresso |
| DATA_SAIDA | date(4) |  | S | Data de saída |
