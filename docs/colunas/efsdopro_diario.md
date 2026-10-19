# EFSDOPRO_DIARIO — Saldo dos Produtos - Diário
249.231 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| DATA_PRO | date(4) | PK |  | Competência |
| CODI_PDI | char(14) | PK |  | Código do produto |
| DIA_SALDO | date(4) | PK |  | Dia |
| SALDO_FISICO_ANTERIOR | numeric(18) |  |  | Saldo fisíco anterior |
| SALDO_VALOR_ANTERIOR | numeric(15) |  |  | Saldo valor anterior |
| ICMS_TOTAL_ANTERIOR | numeric(13) |  |  | Valor do ICMS anterior |
| SALDO_FISICO_FINAL | numeric(18) |  |  | Saldo fisíco final |
| SALDO_VALOR_FINAL | numeric(15) |  |  | Saldo valor final |
| ICMS_TOTAL_FINAL | numeric(13) |  |  | Valor do ICMS final |
| SALDO_FISICO_ICMS_ST_ANTERIOR | numeric(18) |  |  | Saldo fisíco ICMS ST anterior |
| ICMS_ST_TOTAL_ANTERIOR | numeric(13) |  |  | Valor do ICMS ST anterior |
| SALDO_FISICO_ICMS_ST_FINAL | numeric(18) |  |  | Saldo fisíco ICMS ST final |
| ICMS_ST_TOTAL_FINAL | numeric(13) |  |  | Valor do ICMS ST final |
| SALDO_VALIDO | char(1) |  | S |  |
