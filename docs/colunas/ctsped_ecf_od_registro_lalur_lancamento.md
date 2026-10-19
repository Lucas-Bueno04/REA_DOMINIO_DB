# CTSPED_ECF_OD_REGISTRO_LALUR_LANCAMENTO — SPED ECF - Outros Dados - Registros de lançamento contábil LALUR
14.978 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_OUTROS_DADOS | integer(4) | PK |  | Sequencial |
| COMPETENCIA | date(4) | PK |  | Competência |
| REGISTRO | varchar(4) | PK |  | Registro |
| CODIGO | numeric(10) | PK |  | Código do registro |
| VIGENCIA | date(4) | PK |  | Vigência do registro |
| I_LANCAMENTO | integer(4) | PK |  | Sequencial do lançamento |
| NUMERO_LOTE | integer(4) |  |  | Número do lote |
| DATA_LANCAMENTO | date(4) |  | S | Data do lançamento |
| VALOR | numeric(14) |  |  | Valor do lançamento |
| CODIGO_HISTORICO | integer(4) |  | S | Código do histórico do lançamento |
| HISTORICO | varchar(1000) |  |  | Histórico do lançamento |
| I_CONTA | integer(4) | PK |  | Sequencial da conta |
| TIPO_SALDO | char(1) |  | S | Tipo Saldo:  D-Devedor ou C-Credor. |
