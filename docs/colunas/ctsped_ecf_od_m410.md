# CTSPED_ECF_OD_M410 — SPED ECF - Outros Dados - Registro M410
5.083 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_OUTROS_DADOS | integer(4) | PK |  | Sequencial Outros Dados |
| COMPETENCIA | date(4) | PK |  | Competência |
| SEQUENCIAL | integer(4) | PK |  | Sequencial Interno |
| TIPO_CONTA | char(1) | PK |  | Tipo da Conta (B=Base Negativa / P=Parte B) |
| HISTORICO | varchar(40) |  |  | Histórico |
| LANCAR_REALIZACAO_VALOR_TRIBUTACAO_DIFERIDA | char(1) |  |  | Lanç. realização de valores cuja tributação tenha sido diferida |
| I_BASE_NEGATIVA_PARTE_B | integer(4) |  | S | Código da parte b ou base negativa |
| VALOR | numeric(14) |  |  | Valor |
| INDICADOR_LANCAMENTO | char(2) |  |  | Indicador do lançamento (DB-Débito / CR-Crédito / PF-Prejuízo do exercício / BC-Base de cálculo negativa da CSLL) |
| IDENTIFICADOR_SPED_ECF | varchar(30) |  |  | Identificador SPED ECF |
| CONTA_CONTRAPARTIDA | integer(4) |  | S | Código conta contra partida |
