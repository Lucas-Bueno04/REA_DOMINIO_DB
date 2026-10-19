# CTSPED_ECF_OD_REGISTRO — SPED ECF - Outros Dados - Registros de colunas valor
8.584.047 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_OUTROS_DADOS | integer(4) | PK |  | Sequencial |
| COMPETENCIA | date(4) | PK |  | Competência |
| REGISTRO | varchar(4) | PK |  | Registro |
| CODIGO | numeric(10) | PK |  | Código do registro |
| VIGENCIA | date(4) | PK |  | Vigência do registro |
| VALOR | numeric(19) |  |  | Valor |
| CONTAS | varchar(4096) |  | S | Contas |
| SALDO_ANTERIOR | numeric(14) |  |  | Saldo anterior |
| DETERMINAR_FORMA_IMPORTAR_SALDO_CONTA_CONTABIL | char(1) |  |  | Determinar a forma de importar o saldo das contas contábeis |
| FORMA_IMPORTACAO | integer(4) |  |  | Forma de importação (1-Total Débito / 2-Total Crédito / 3-Saldo Período / 4-Saldo Exercício) |
