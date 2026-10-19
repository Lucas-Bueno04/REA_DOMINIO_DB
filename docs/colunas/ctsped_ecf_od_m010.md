# CTSPED_ECF_OD_M010 — SPED ECF - Outros Dados - Registro M010
520 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_OUTROS_DADOS | integer(4) | PK |  | Sequencial Outros Dados |
| I_BASE_NEGATIVA_PARTE_B | integer(4) | PK |  | Código da parte b ou base negativa |
| DATA_CRIACAO | date(4) |  |  | Data de criação |
| SALDO_INICIAL | numeric(14) |  |  | Saldo inicial |
| DESCRICAO | varchar(140) |  |  | Descrição da parte b ou base negativa |
| INDICADOR_SALDO_INICIAL | char(1) |  |  | Indicador do Saldo inicial (D-Prejuízos ou valores que reduzam o lucro real ou a base de cálculo da contribuição social em períodos subsequent / C-Valores que aumentam o lucro real ou a base de cálculo da contribuição social em períodos subsequentes) |
| TIPO_CONTA | char(1) | PK |  | Tipo da Conta (B=Base Negativa / P=Parte B) |
| IDENTIFICADOR_SPED_ECF | varchar(30) |  |  | Identificador SPED ECF |
| TIPO_CONTA_RFB_PARTE_B | integer(4) |  | S | Codigo padrao RFB parte B |
| DESCRICAO_TIPO_CONTA_RFB_PARTE_B | varchar(1000) |  | S | Descrição Codigo padrao RFB parte B |
