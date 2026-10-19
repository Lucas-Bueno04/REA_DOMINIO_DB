# EFSDOIMP_ESTADUAL_PE — Saldo dos Impostos - Estadual PE
418 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| CREDITO_PRESUMIDO_TRANSPORTE | numeric(13) |  |  | Valor Crédito Presumido Transporte |
| ICMS_ANTECIPADO_CREDITO | numeric(13) |  |  | CrÃ©dito ICMS Antecipado |
| ICMS_ANTECIPADO_ESTORNO_CREDITO | numeric(13) |  |  | Estorno crÃ©dito ICMS Antecipado |
| ICMS_ANTECIPADO_CREDITO_PAGAMENTOS | numeric(13) |  |  | CrÃ©dito ICMS Antecipado pelos pagamentos |
| TRANSF_SALDO_CREDOR_MES_SEG_PRODEPE_INDUSTRIA | numeric(13) |  |  | Transf. Saldo Credor Mês Seguinte PRODEPE Indústria |
| TRANSF_SALDO_CREDOR_MES_SEG_PRODEPE_CENTRAL_ENT | numeric(13) |  |  | Transf. Saldo Credor Mês Seguinte PRODEPE Central Entradas |
| TRANSF_SALDO_CREDOR_MES_SEG_PRODEPE_CENTRAL_SAI | numeric(13) |  |  | Transf. Saldo Credor Mês Seguinte PRODEPE Central Saídas |
| TRANSF_SALDO_CREDOR_MES_ANT_PRODEPE_INDUSTRIA | numeric(13) |  |  | Transf. Saldo Credor Mês Anterior PRODEPE Indústria |
| TRANSF_SALDO_CREDOR_MES_ANT_PRODEPE_CENTRAL_ENT | numeric(13) |  |  | Transf. Saldo Credor Mês Anterior PRODEPE Central Entradas |
| TRANSF_SALDO_CREDOR_MES_ANT_PRODEPE_CENTRAL_SAI | numeric(13) |  |  | Transf. Saldo Credor Mês Anterior PRODEPE Central Saídas |
| CREDITO_PRESUMIDO_PRODEPE_INDUSTRIA | numeric(13) |  |  | Crédito Presumido PRODEPE Indústria |
| CREDITO_PRESUMIDO_PRODEPE_CENTRAL_ENTRADAS | numeric(13) |  |  | Crédito Presumido PRODEPE Central Entradas |
| CREDITO_PRESUMIDO_PRODEPE_CENTRAL_SAIDAS | numeric(13) |  |  | Crédito Presumido PRODEPE Central Saídas |
| CREDITO_PRESUMIDO_PRODEAUTO | numeric(13) |  |  | Crédito Presumido PRODEAUTO |
| CREDITO_PRESUMIDO_PRODEPE_IMPORTACAO_SAIDAS_INTERNAS | numeric(13) |  |  | Crédito Presumido PRODEPE Importação Saídas Internas |
| CREDITO_PRESUMIDO_PRODEPE_IMPORTACAO_SAIDAS_INTERESTADUAIS | numeric(13) |  |  | Crédito Presumido PRODEPE Importação Saídas Interestaduais |
| CREDITO_PRESUMIDO_PRODEPE_IMPORTACAO_ICMS_ENTRADAS_IMPORTACAO | numeric(13) |  |  | Crédito Presumido PRODEPE Importação ICMS Entradas Importação |
| CREDITO_ATIVO_IMOBILIZADO | numeric(13) |  |  | Crédito Ativo Imobilizado |
| ESTORNO_ICMS_DOCUMENTOS_EXTEMPORANEOS | numeric(13) |  |  | Estorno ICMS documentos extemporaneo |
| ICMS_DOCUMENTOS_EXTEMPORANEOS_RECOLHER | numeric(13) |  |  | ICMS documentos extemporaneo recolher |
| VALOR_PAGO_ICMS_DOCUMENTOS_EXTEMPORANEOS | numeric(13) |  |  | Valor pago ICMS documento extemporaneo |
| DATA_VENCIMENTO_ICMS_DOCUMENTOS_EXTEMPORANEOS | date(4) |  | S | Data vencimento IMCS documentos extemporaneo |
| OUTROS_CREDITOS_ICMS_ST_CREDITADO_AQUIS_INTERNAS | numeric(13) |  |  | ICMS-ST creditado nas aquisições internas |
| OUTROS_CREDITOS_ICMS_ST_CREDITADO_AQUIS_INTERESTADUAIS | numeric(13) |  |  | ICMS-ST antecipação creditado nas aquisições interestaduais |
| ESTORNO_DEBITO_OPERACOES_CTE_SUBSTITUTO | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |
| ESTORNO_CREDITO_PRESUMIDO_ATACADISTA | numeric(13) |  |  | Estorno de crédito presumido Decreto 38455/2012 |
| SALDO_CREDITO_PRESUMIDO_PERIODO_ANTERIOR_ATACADISTA | numeric(13) |  |  | Saldo de crédito presumido período anterior Decreto 38455/2012 |
| CREDITO_PRESUMIDO_COMERCIO_ATACADISTA | numeric(13) |  |  | Crédituo presumido comércio atacadista Decreto 38455/2012 |
| RECOLHIMENTO_ESPECIFICO_VENDAS_CONSUMIDOR_FINAL | numeric(13) |  |  | Recolhimento específico sobre vendas a consumidor final não inscrito no CNPJ |
| ALIQUOTA_AMP_ATACADISTA | numeric(11) |  |  | Coluna para salvar o valor AMP para utilizar nos relatórios |
| ICMS_ANTECIPADO_ATACADISTA | numeric(13) |  |  | Coluna para gravar o icms antecipado e utilizar nos relatórios |
| CREDITO_PRESUMIDO_ATACADISTA_NAO_APROVEITADO | numeric(13) |  |  | Crédito Presumido Atacadista que não foi usado para utilizar no mes seguinte |
| CREDITO_ICMS_MONOFASICO_AQUISICAO_COMBUSTIVEL_INSUMO | numeric(13) |  |  | Crédito de ICMS monofásico na aquisição de combustíveis para insumos conforme Convênios ICMS nº 199/2022 e 15/2023 |
