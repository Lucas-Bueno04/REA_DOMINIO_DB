# CTSPED_ECF_OD_REGISTRO_LALUR_CONTA — SPED ECF - Outros Dados - Registros de conta contábil LALUR
1.825 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_OUTROS_DADOS | integer(4) | PK |  | Sequencial |
| COMPETENCIA | date(4) | PK |  | Competência |
| REGISTRO | varchar(4) | PK |  | Registro |
| CODIGO | numeric(10) | PK |  | Código do registro |
| VIGENCIA | date(4) | PK |  | Vigência do registro |
| CODI_CTA | integer(4) |  |  | Conta contábil |
| CODI_EMP_PLANO | integer(4) |  |  | Empresa do plano de contas |
| VALOR | numeric(14) |  |  | Valor |
| I_CONTA | integer(4) | PK |  | Sequencial da conta |
| TIPO_SALDO | char(1) |  | S | Tipo Saldo:  D-Devedor ou C-Credor. |
