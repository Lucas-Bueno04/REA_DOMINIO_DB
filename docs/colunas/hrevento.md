# HREVENTO — Eventos
89 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_EVENTO | integer(4) | PK |  | Codigo |
| DESCRICAO | varchar(60) |  |  | Descricao |
| DATA_CADASTRO | date(4) |  |  | Data de cadastro |
| UNIDADE | char(1) |  |  | Unidade V Valor Q Quantidade P Percentual sobre contrato F Formula |
| REFERENCIA | numeric(13) |  | S | Referencia |
| I_CATEGORIA_RECEBER | integer(4) |  |  | Categoria |
| CODI_IMP | integer(4) |  | S | Codigo do imposto |
| SOMA_IRRF | char(1) |  |  | Soma na base do IRRF S N |
| ALIQUOTA_IRRF | numeric(5) |  |  | Aliquota de IRRF |
| SOMA_ISS | char(1) |  |  | Soma na base do ISS S N |
| ALIQUOTA_ISS | numeric(5) |  |  | Aliquota de ISS |
| SOMA_RETENCAO_FONTE | char(1) |  |  | Soma na base da Retencao na Fonte S N |
| ALIQUOTA_RETENCAO_FONTE | numeric(5) |  |  | Aliquota de Retencao na Fonte |
| SOMA_INSS_RET | char(1) |  |  | Soma na base do INSS Retido S N |
| ALIQUOTA_INSS_RET | numeric(5) |  |  | Aliquota de INSS |
| SOMA_ISS_RET | char(1) |  |  | Soma na base do ISS Retido S N |
| ALIQUOTA_ISS_RET | numeric(5) |  |  | Aliquota de ISS |
| COMPLEMENTO | varchar(350) |  |  | Complemento |
| DIA_VENCIMENTO | tinyint(1) |  | S | Dia de vencimento |
| MES_VENCIMENTO | char(1) |  | S | Mes de vencimento N No mesmo mes A Apos o mes S No segundo mes |
| FATURA_CONTRATO | char(1) |  | S | Fatura com contrato S N |
| PAGO_ESCRITORIO | char(1) |  | S | Pago pelo escritorio S N |
| I_CONTA_FINANCEIRA | integer(4) |  | S | Conta financeira |
| NAO_PEDIR_COMPLEMENTO | char(1) |  |  | Nao pedir no lancamento complemento S N |
| NAO_PEDIR_VENCIMENTO | char(1) |  |  | Nao pedir no lancamento vencimento S N |
| NAO_PEDIR_FATURAR_CONTRATO | char(1) |  |  | Nao pedir no lancamento faturar com contrato S N |
| NAO_PEDIR_PAGO_ESCRITORIO | char(1) |  |  | Nao pedir no lancamento pago pelo escritorio S N |
| NAO_PEDIR_CONTA | char(1) |  |  | Nao pedir no lancamento conta financeira S N |
| NAO_GERAR_CONTABILIZACAO | char(1) |  |  | Nao gerar lancamento contabil S N |
| CONTA_CREDITO | integer(4) |  |  | Conta credito |
| HISTORICO_CREDITO | integer(4) |  |  | Historico credito |
| CONTA_DEBITO | integer(4) |  |  | Conta debito |
| HISTORICO_DEBITO | integer(4) |  |  | Historico debito |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| VENCIMENTO | char(1) |  | S | Vencimento (F=Fixo/ C=Conforme contrato) |
| RELACIONAR_PRODUTO_NOTA_ESCRITA | char(1) |  |  | Relacionar produto para o movimento de notas de saÃ­da e serviÃ§o (S/N) |
| PRODUTO_EVENTO | char(14) |  | S | Produto para o movimento de notas de saÃ­da e serviÃ§o |
| SOMA_PIS | char(1) |  |  | Soma na base do PIS (S/N) |
| CST_PIS | integer(4) |  | S | CST do PIS |
| ALIQUOTA_PIS | numeric(5) |  |  | Aliquota de PIS |
| SOMA_COFINS | char(1) |  |  | Soma na base do COFINS (S/N) |
| CST_COFINS | integer(4) |  | S | CST do COFINS |
| ALIQUOTA_COFINS | numeric(13) |  |  | Aliquota de COFINS |
| NFSE_DESCRICAO_ITEM | varchar(130) |  | S | NFSe - Descrição do item |
| SOMA_BASE_IBS_CBS | char(1) |  | S | Soma na base IBS/CBS |
