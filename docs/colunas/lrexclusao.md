# LREXCLUSAO — Cadastro de Exclusões
29 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_EXCLUSAO | integer(4) | PK |  | Código |
| DESCRICAO | varchar(1000) |  |  | Descrição |
| EXCLUIR_IMPOSTO | char(1) |  |  | Adicionar ao imposto (C=Contribuição Social/ I=IRPJ/ A=Ambos) |
| LUCRO_EXPLORACAO | char(1) |  |  | Lucro da Exploração (S/N) |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| I_GRUPO_CSLL_EXCLUSAO_GERAL | integer(4) |  | S | Grupo da Contribuição Social - Geral |
| I_GRUPO_CSLL_EXCLUSAO_SF | integer(4) |  | S | Grupo da Contribuição Social - Sistema Financeiro |
| I_GRUPO_IRPJ_EXCLUSAO_GERAL | integer(4) |  | S | Grupo do IRPJ - Geral |
| I_GRUPO_IRPJ_EXCLUSAO_SF | integer(4) |  | S | Grupo do IRPJ - Sistema Financeiro |
| I_GRUPO_EXCLUSAO_LUCRO_EXPLORACAO | integer(4) |  | S | Grupo do Lucro da Exploração |
| REGISTRAR_AUTOMATICAMENTE_PARTE_B | char(1) |  |  | Registrar automaticamente na Parte B os lançamentos com esta adição |
| PARTE_B_CONTA | integer(4) |  | S | Conta da Parte B |
| PARTE_B_HISTORICO | varchar(250) |  |  | Histórico da Parte B |
| DEFINIR_PERCENTUAL_LIMITE_IMPORTACAO_SALDO_CONTAS | char(1) |  |  | Definir o percentual limite para importação dos saldos das contas |
| LIMITE_IMPORTACAO | numeric(4) |  |  | Limite para importação |
| I_GRUPO_CSLL_EXCLUSAO_S | integer(4) |  | S | Grupo da Contribuição Social - Sociedade Seguradora |
| I_GRUPO_IRPJ_EXCLUSAO_S | integer(4) |  | S | Grupo da IRPJ - Sociedade Seguradora |
| I_GRUPO_CSLL_EXCLUSAO_RURAL | integer(4) |  | S | Grupo da Contribuição Social - Rural |
| I_GRUPO_IRPJ_EXCLUSAO_RURAL | integer(4) |  | S | Grupo do IRPJ - Rural |
| REGISTRAR_AUTOMATICAMENTE_BASE_NEGATIVA | char(1) |  |  | Registrar automaticamente na Base Negativa os lançamentos com esta adição |
| BASE_NEGATIVA_CONTA | integer(4) |  | S | Conta da Base Negativa |
| BASE_NEGATIVA_HISTORICO | varchar(250) |  |  | Historico da base negativa |
