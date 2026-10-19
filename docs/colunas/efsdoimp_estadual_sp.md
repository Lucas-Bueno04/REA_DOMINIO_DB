# EFSDOIMP_ESTADUAL_SP — Saldo dos Impostos - Estadual SP
19.335 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| CREDITO_CONFORME_ALIQUOTA_SN | numeric(13) |  |  | Crédito de ICMS conforme alíquota do Simples Nacional |
| DEVOLUCAO_MERCADORIA_ADQUIRIDA_SN | numeric(13) |  |  | Devolução de mercadoria adquirida de Simples Nacional |
| OUTROS_DEBITOS_REMESSA_PARA_VENDA_FORA_ESTAB | numeric(13) |  |  | Outros débitos - Remessa para venda fora do estabelecimento |
| ESTORNO_DEBITOS_REMESSA_PARA_VENDA_FORA_ESTAB | numeric(13) |  |  | Estorno de débitos - Remessa para venda fora do estabelecimento |
| DEBITO_ICMS_SOBRE_ESTOQUE_INCLUIDAS_SUBTRI_CAT_26_15 | numeric(13) |  |  | Débito de ICMS sobre estoque incluídas Sub. Trib. CAT 26/15 |
| CREDITO_ICMS_SOBRE_ESTOQUE_EXCLUIDAS_SUBTRI | numeric(13) |  |  | Crédito de ICMS sobre estoque excluídos Sub. Trib. |
| CREDITO_ESTOQUE_APROVEITADO_CAT_26_15 | numeric(13) |  |  | Crédito de ICMS sobre estoque aproveitado CAT 26/15 |
| TRANSFERENCIA_SALDO_CREDOR_ENTRADA | numeric(13) |  |  | Trasferência de saldo credor através das entradas com CFOP 1602 |
| TRANSFERENCIA_SALDO_DEVEDOR_ENTRADA | numeric(13) |  |  | Trasferência de saldo devedor através das entradas com CFOP 1605 |
| TRANSFERENCIA_SALDO_CREDOR_SAIDA | numeric(13) |  |  | Trasferência de saldo credor através das saídas com CFOP 5602 |
| TRANSFERENCIA_SALDO_DEVEDOR_SAIDA | numeric(13) |  |  | Trasferência de saldo devedor através das saídas com CFOP 5605 |
| CREDITO_ICMS_PROP_VENDA_OUTRA_UF_PORT_CAT_158_2015 | numeric(13) |  |  | Crédito de ICMS próprio na venda para outra UF - CAT |
| RESSARCIMENTO_ICMS_ST_PORTARIA_CAT_158_2015 | numeric(13) |  |  | Ressarcimento de ICMS ST - CAT |
| CREDITO_OUTORGADO_EMPRESAS_TEXTEIS | numeric(13) |  |  | Crédito Outorgado - art. 41, Anexo III, do RICMS |
| ESTORNO_CREDITO_OUTORGADO_EMPRESAS_TEXTEIS | numeric(13) |  |  | Estorno de Crédito - art. 41, Anexo III, do RICMS |
| CREDITO_OUTORGADO_EMPRESAS_TEXTEIS_SAIDAS | numeric(13) |  |  | Crédito Outorgado - art. 41, Anexo III, do RICMS - Saídas |
| CREDITO_OUTORGADO_EMPRESAS_TEXTEIS_DEVOLUCAO | numeric(13) |  |  | Crédito Outorgado - art. 41, Anexo III, do RICMS - Devolução |
| ESTORNO_CREDITO_OUTORGADO_EMPRESAS_TEXTEIS_LETRA_B | numeric(13) |  |  | Estorno Crédito Outorgado Empresas Texteis Letra B |
| ESTORNO_CREDITO_OUTORGADO_EMPRESAS_TEXTEIS_LETRA_C | numeric(13) |  |  | Estorno Crédito Outorgado Empresas Texteis Letra C |
| ESTORNO_CREDITO_OUTORGADO_EMPRESAS_TEXTEIS_LETRA_T | numeric(13) |  |  | Estorno Crédito Outorgado Empresas Texteis Letra T |
| ESTORNO_CREDITO_ICMS_PROP_VENDA_OUTRA_UF_PORT_CAT_158_2015 | numeric(13) |  |  | Estorno Crédito de ICMS próprio na venda para outra UF - CAT |
| ESTORNO_RESSARCIMENTO_ICMS_ST_PORTARIA_CAT_158_2015 | numeric(13) |  |  | Estorno Ressarcimento de ICMS ST - CAT |
| VALOR_RESSARCIMENTO | numeric(13) |  |  | Valor Ressarcimento |
| VALOR_COMPLEMENTO | numeric(13) |  |  | Valor Complemento |
| VALOR_ICMS_CREDITO | numeric(13) |  |  | Valor ICMS Crédito |
| VALOR_ICMS_ESTORNO_CREDITO | numeric(13) |  |  | Valor ICMS Estorno Crédito |
| ESTORNO_CREDITO_DEVOLUCOES_RETORNO_OUTORGADO_EMPRESAS_TEXTEIS | numeric(13) |  |  | Estorno de Crédito pelas Devoluções/Retorno - art. 41, Anexo III, do RICMS |
| OUTROS_DEBITOS_REGIME_ESP_TRIBUTA_ICMS_FORNECI_ALIMENTACAO | numeric(13) |  |  | Regime especial de tributação no fornecimento de alimentação - Dec. 51.597/07 |
| OUTROS_CREDITOS_INSUMO_OPER_FORNECI_ALIMENTACAO | numeric(13) |  |  | Crédito de insumos nas operações com fornec. de alimentação - Dec. 51.597/07 |
| CREDITO_ATIVO_IMOBILIZADO_ANTERIOR | numeric(13) |  |  | Créditos de ICMS de Ativo Imobilizado não utilizados em períodos anteriores |
| EXCLUSAO_MERCADORIA_SUBTRI_PORT_CAT_28_2020 | numeric(13) |  |  | Exclusão de mercadorias da substituição tributária - Art. 3º, Port CAT-28/2020 |
| CREDITO_AQUISICAO_COMBUSTIVEL_PARA_INSUMO_CONV_ICMS_199_22_E_15_23 | numeric(13) |  |  | Crédito na aquisição de combustíveis para insumo - Conv. ICMS nº 199/22 e 15/23 |
| ESTORNO_DEBITO_OPERACOES_CTE_SUBSTITUTO | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |
| ESTORNO_CREDITO_PRESUMIDO_TRANSPORTE_OPERACORES_CTE_SUBSTITUTO | numeric(13) |  |  | Estorno de crédito presumido transportes - Operações com CT-e e/ou CT-eOS |
| CREDITO_OUTORGADO_SAIDAS_INTERNAS_CARNE | numeric(13) |  |  | Crédito Outorgado - art. 40, Anexo III, do RICMS |
| ESTORNO_CREDITO_OUTORGADO_SAIDAS_INTERNAS_CARNE | numeric(13) |  |  | Estorno de Crédito - art. 40, Anexo III, do RICMS |
| ESTORNO_CREDITO_OUTORGADO_DEVOLUCOES_RETORNO_SAIDAS_INTERNAS_CARNE | numeric(13) |  |  | Estorno de Crédito pelas Devoluções/Retorno - art. 40, Anexo III, do RICMS |
| CREDITO_OUTORGADO_SAIDAS_INTERNAS_CARNE_SAIDAS | numeric(13) |  |  | Crédito Outorgado - art. 40, Anexo III, do RICMS - Saídas |
| CREDITO_OUTORGADO_SAIDAS_INTERNAS_CARNE_DEVOLUCAO | numeric(13) |  |  | Crédito Outorgado - art. 40, Anexo III, do RICMS - Devolução |
| ESTORNO_CREDITO_OUTORGADO_SAIDAS_INTERNAS_CARNE_LETRA_B | numeric(13) |  |  | Estorno Crédito Outorgado Saídas internas Carne Letra B |
| ESTORNO_CREDITO_OUTORGADO_SAIDAS_INTERNAS_CARNE_LETRA_C | numeric(13) |  |  | Estorno Crédito Outorgado Saídas internas Carne Letra C |
| ESTORNO_CREDITO_OUTORGADO_SAIDAS_INTERNAS_CARNE_LETRA_T | numeric(13) |  |  | Estorno Crédito Outorgado Saídas internas Carne Letra T |
| LANCAMENTO_EXTEMP_REF_EXCLUSAO_MERC_SUBTRI | numeric(13) |  |  | Lançamento Extemp. ref. exclusão de merc. da subst. trib. - Art. 2º, Port SRE-07/2026 |
