# PMTRANSFERENCIA_MATRIZ_FILIAL — Plano de contas SPED ECF Entidades Fechadas da Previdência Comp Referencial - Saldo anterior por Centro de Custo
8 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_TRANSFERENCIA | integer(4) | PK |  | Sequencial transferência |
| I_BEM | numeric(16) |  |  | Bem |
| DATA_TRANSFERENCIA | date(4) |  |  | Data da transferência |
| VALOR_DEPRECIACAO_FISCAL_ACUMULADA | numeric(13) |  |  | Valor da depreciação fiscal acumulada |
| VALOR_DEPRECIACAO_SOCIETARIA_ACUMULADA | numeric(13) |  |  | Valor da depreciação societária acumulada |
| VALOR_SALDO_ATUAL | numeric(13) |  |  | Valor do saldo do bem na data de transferência |
| CODI_EMP_DESTINO | integer(4) |  |  | Empresa destino transferência |
| I_CONTA_PATRIMONIAL_DESTINO | integer(4) |  |  | Conta patrimonial destino transferência |
| I_CENTRO_CUSTO_DESTINO | integer(4) |  |  | Centro de custo destino transferência |
| I_BEM_DESTINO | numeric(16) |  |  | Bem destino |
| I_HISTORICO | integer(4) |  | S | Código histórico |
| HISTORICO | varchar(512) |  | S | Historico |
| NAO_TRANSFERIR_CREDITO_REMANESCENTE_ICMS | char(1) |  |  | Não transferir crédito remanescente icms |
| NAO_TRANSFERIR_DEBITO_REMANESCENTE_ICMS | char(1) |  |  | Não transferir débito remanescente icms importacao |
| FISCAL_NUMERO | numeric(15) |  | S | Documento fiscal - Número |
| FISCAL_SERIE | char(7) |  | S | Documento fiscal - Série |
| FISCAL_DATA_EMISSAO | date(4) |  | S | Documento fiscal - Data de emissão |
| FISCAL_MODELO | integer(4) |  | S | Documento fiscal - Modelo |
| FISCAL_CHAVE_NFE | char(44) |  | S | Documento fiscal - Chave NFe |
| FISCAL_CODI_CLI | integer(4) |  | S | Documento fiscal - Cliente |
| FISCAL_EMITENTE | char(1) |  | S | Documento fiscal - Emitente (T=Terceiros/P=Próprio) |
| FISCAL_CODI_PDI | char(14) |  | S | Documento fiscal - Produto |
| FISCAL_SEQUENCIAL_ITEM | integer(4) |  | S | Documento fiscal - Sequencial do item |
| NAO_TRANSFERIR_DEBITO_REMANESCENTE_ICMS_DIF_ALI | char(1) |  |  | Não transferir débito remanescente icms diferencial aliquota |
| ULTIMA_PARCELA_CREDITO_ICMS | integer(4) |  | S | Última parcela calculada credito ICMS |
