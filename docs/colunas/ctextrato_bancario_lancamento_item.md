# CTEXTRATO_BANCARIO_LANCAMENTO_ITEM — Lançamento de extrato bancário - lançamentos
25.400 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_LANCAMENTO | integer(4) | PK |  | Código extrato |
| I_ITEM | integer(4) | PK |  | Sequencial do item |
| DATA_ITEM | date(4) |  |  | Data |
| HISTORICO | varchar(350) |  |  | Histórico |
| DOCUMENTO | varchar(100) |  | S | Documento |
| VALOR | numeric(13) |  |  | Valor |
| TIPO | char(1) |  |  | Tipo (D=Soma/C=Subtrai) |
| ORIGEM | char(1) |  |  | Origem (M=Manualmente/ I=Importação) |
| VERSAO | tinyint(1) |  |  | Versão do extrato (1=Antigo/ 2=Novo) |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| TIPO_LANCAMENTO | char(1) |  |  | Tipo (X = Um débito para um crédito / V = Varios débitos para varios créditos) |
| FILIAL | integer(4) |  | S | Código da filial |
