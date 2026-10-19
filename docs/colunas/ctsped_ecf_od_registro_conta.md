# CTSPED_ECF_OD_REGISTRO_CONTA — SPED ECF - Outros Dados - Registros de conta contábil
4.866 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CONTA | integer(4) | PK |  | Sequencial da tabela |
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_OUTROS_DADOS | integer(4) | PK |  | Sequencial dos outros dados |
| COMPETENCIA | date(4) | PK |  | Competência |
| REGISTRO | varchar(4) | PK |  | Registro |
| CODIGO | numeric(10) | PK |  | Código do registro |
| VIGENCIA | date(4) | PK |  | Vigência do registro |
| CODI_CTA | integer(4) |  |  | Conta contábil |
| FORMA_IMPORTACAO | integer(4) |  |  | Forma de importação (1-Total Débito / 2-Total Crédito / 3-Saldo Período / 4-Saldo Exercício / 5-Saldo Anterior) |
| OPERACAO | integer(4) |  | S | Operação (1-Somar (+) / 2-Subtrair (-)) |
| CODI_EMP_PLANO | integer(4) |  |  | Empresa do plano de contas |
| DETERMINAR_FORMA_IMPORTAR_SALDO_CONTA_CONTABIL | varchar(4) |  |  | Determinar forma de importar saldo |
