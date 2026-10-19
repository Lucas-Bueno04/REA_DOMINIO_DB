# HRLANCAMENTO_RECEBER — Lancamentos de contas a receber - Mensais e Fixos
6.371 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_CLIENTE | integer(4) | PK |  | Cliente |
| I_RECEBER | integer(4) | PK |  | Codigo |
| COMPETENCIA | date(4) |  |  | Competencia para lancamento mensal ou Inicia em para lancamento fixo |
| I_MOVIMENTO_ESCRITORIO | integer(4) |  | S | Conta corrente escritorio |
| I_MOVIMENTO_CLIENTE | integer(4) |  | S | Conta corrente cliente |
| I_MOVIMENTO_CLIENTE_SEQ | integer(4) |  | S | Conta corrente cliente sequencial |
| PRIMEIRO_FATURAMENTO | date(4) |  |  | Competencia do primeiro faturamento do lancamento |
| FIXO | char(1) |  |  | Lancamento fixo S N |
| I_EVENTO | integer(4) |  |  | Evento |
| DATA_LANCAMENTO | date(4) |  |  | Data do lancamento |
| FATURA_CONTRATO | char(1) |  |  | Fatura com o contrato S N |
| I_CONTRATO | integer(4) |  | S | Contrato |
| DATA_VENCIMENTO | date(4) |  | S | Data de vencimento para o lancamento mensal |
| DIA_VENCIMENTO | tinyint(1) |  | S | Dia de vencimento para o lancamento fixo |
| MES_VENCIMENTO | char(1) |  |  | Mes de vecimento para o lancamento fixo N No mes de faturamento A Apos o mes de faturamento S No segundo mes de faturmento |
| MES_FATURAMENTO | char(1) |  |  | Meses para faturamento para o lancamento fixo T Todos os meses S Selecionar meses |
| MES_SELECIONADO | varchar(40) |  |  | Meses selecionados para o lancamento fixo |
| ENCERRAR | char(1) |  |  | Definir encerramento do lancamento fixo S N |
| DATA_ENCERRAMENTO | date(4) |  | S | Data de encerramento do lancamento fixo |
| QUANTIDADE | integer(4) |  | S | Quantidade |
| VALOR | numeric(13) |  |  | Valor |
| PAGO_ESCRITORIO | char(1) |  |  | Pago pelo escritorio S N |
| COMPLEMENTO | varchar(512) |  |  | Complemento |
| ORIGEM | char(1) |  |  | Origem do lancamento L Lancamento C Contrato |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| MODULO_ORIGEM | char(2) |  |  | Modulo que originou o lancamento (HR=Honorarios, EF=Escrita Fiscal, FO=Folha) |
| CONSIDERAR_ADICIONAL_ANUAL | char(1) |  |  | Considerar adicionar anual |
| OBSERVACAO | varchar(1000) |  | S | OBSERVACAO DO LANCAMENTO |
