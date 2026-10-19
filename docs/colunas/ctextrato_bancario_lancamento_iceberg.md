# CTEXTRATO_BANCARIO_LANCAMENTO_ICEBERG — Lançamento de extrato ICEBERG
5.992 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_EMP_LANCTO | integer(4) | PK |  | Código da empresa do lançamento |
| I_EXTRATO_BANCARIO | integer(4) | PK |  | Sequencial do extrato |
| ID_TRANSACAO | char(50) |  |  | Identificador da transação (eventId) |
| DATA_EXTRATO | date(4) |  |  | Data do extrato |
| CODI_TRANSACAO | decimal(20) |  |  | Código de transação |
| VALOR | numeric(13) |  |  | Valor do extrato |
| CODI_LOTE | integer(4) |  | S | Código do lote contábil |
| INSCRICAO | char(20) |  | S | Inscrição da pessoa envolvida na transação |
| NOME | char(150) |  | S | Nome da pessoa envolvida na transação, tarifa ou estabelecimento comercial |
| I_EXTRATO_BANCARIO_ITEM | integer(4) | PK |  | Sequencial |
| TIPO_LANCAMENTO | tinyint(1) |  |  | 1-Valor do extrato, 2-Valor original, 3-Multa, 4-Juros, 5-Desconto |
| I_BANCO | integer(4) |  |  | Codigo de identificacão do banco |
| DATA_HORA_EXTRATO | timestamp(8) |  | S | DATA E HORA DA TRANSACAO |
| TIPO_VALOR | char(1) |  |  | C - Credito / D - Debito |
| STATUS | integer(4) |  |  | 0=Pendente(Contab.)/Contabilizada/Mesmo Beneficiario/Desconsiderada / 4=Aguardando NF / 5=Pendente(Transacao) |
| DESCONSIDERAR_EXTRATO_BANCARIO | char(1) |  |  | Desconsiderar o extrato bancário digital na tela de lançamentos contábeis digital(S/N) |
| PARTNER | varchar(100) |  | S | Parceiro de conexão Open Banking |
| SALDO | numeric(13) |  | S | Saldo da conta após a transação |
| STATUS_TRANSACAO_ROTA | integer(4) |  |  | Situação da transação após processamento (1=Transação Original/2=Atualizada/3=Atualizada Apos Fechamento/4=Excluida Apos Fechamento/5=Atualizada Com Vinculo/6=Excluida Com Vinculo/7=Atualizada Apos Contabilização/8=Excluida Apos Contabilização) |
| CODI_HISTORY | integer(4) |  | S | Sequencial do JSON que atualizou o extrato |
| ORDEM_DATA_EXTRATO | integer(4) |  |  | Ordem da transação no dia. |
| TRANSACTION_ID | varchar(50) |  | S | Identificador da transação por client_id (transaction.id) |
