# FOENCARGO_SIMPLES_DOMESTICO — Tabela de encargos do simples doméstico.
6.326 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| COMPETENCIA | date(4) | PK |  | Competência do cálculo |
| TIPO_PROCESSO | integer(4) | PK |  | Tipo de cálculo |
| I_FILIAIS | integer(4) | PK |  | Código da filial |
| VALOR | numeric(13) |  |  | Valor do encargo na competência. |
| I_PAGTO | integer(4) |  | S | Sequência de pagamento |
| VENCIMENTO | date(4) |  |  | Data de vencimento |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
| VALOR_SALARIO_FAMILIA | numeric(13) |  | S | Valor de salário família na competência. |
| VALOR_COMPENSACAO_SALARIO_FAMILIA | numeric(13) |  | S | Valor compensado na competência. |
| VALOR_A_COMPENSAR_SALARIO_FAMILIA | numeric(13) |  | S | Valor a compensar da competência. |
| VALOR_A_COMPENSAR_SALARIO_FAMILIA_NA_COMPETENCIA | numeric(13) |  | S | Valor a compensar na competência. |
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
