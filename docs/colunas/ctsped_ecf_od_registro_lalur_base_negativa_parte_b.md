# CTSPED_ECF_OD_REGISTRO_LALUR_BASE_NEGATIVA_PARTE_B — SPED ECF - Outros Dados - Registros de conta parte b LALUR
194 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_OUTROS_DADOS | integer(4) | PK |  | Sequencial |
| COMPETENCIA | date(4) | PK |  | Competência |
| REGISTRO | varchar(4) | PK |  | Registro |
| CODIGO | numeric(10) | PK |  | Código do registro |
| VIGENCIA | date(4) | PK |  | Vigência do registro |
| I_BASE_NEGATIVA_PARTE_B | integer(4) | PK |  | Sequencial da parte b |
| VALOR | numeric(14) |  |  | Valor |
| DESCRICAO | varchar(140) |  |  | Descrição |
| INDICADOR_LANCAMENTO | char(1) |  |  | Indicador de lançamento |
| IDENTIFICADOR_SPED_ECF | varchar(15) |  |  | Identificador SPED ECF |
