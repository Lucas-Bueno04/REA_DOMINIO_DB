# EFSDOIMP_SCP — Saldo dos Impostos - SCP
2.041 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| I_SCP | integer(4) | PK |  | Sequencial do SCP |
| PARCELA | integer(4) |  |  | Parcela |
| SALDO_RECOLHER | numeric(13) |  |  | Saldo a recolher |
| SALDO_DEVEDOR | numeric(13) |  |  | Saldo devedor |
| SALDO_CREDOR | numeric(13) |  |  | Saldo credor |
| SALDO_DIFERIDO | numeric(13) |  |  | Saldo diferido |
| SALDO_CREDOR_ANTERIOR | numeric(13) |  |  | Saldo credor anterior |
| SALDO_DIFERIDO_ANTERIOR | numeric(13) |  |  | Saldo diferido anterior |
| VALOR_PAGO | numeric(13) |  |  | Valor pago |
| DATA_VENCIMENTO | date(4) |  | S | Data do vencimento |
| DEVOLUCAO_EMPREEN_PERIODO_FINAL | numeric(13) |  |  | Ajuste de redução - Devoluções de débitos empreendimento imobiliário utilizado no período |
| DEVOLUCAO_EMPREEN_PERIODO_ANTERIOR | numeric(13) |  |  | Ajuste de redução período anterior - Devolução |
| DEVOLUCAO_EMPREEN_PERIODO_ATUAL | numeric(13) |  |  | Ajuste de redução - Devolução |
| DEVOLUCAO_EMPREEN_PERIODO_SEGUINTE | numeric(13) |  |  | Ajuste de redução para o período seguinte - Devolução |
| DEVOLUCAO_VENDA_PERIODO_FINAL | numeric(13) |  |  | Ajuste de redução - Devoluções de vendas utilizado no período |
| DEVOLUCAO_VENDA_PERIODO_ANTERIOR | numeric(13) |  |  | Ajuste de redução período anterior - Devolução |
| DEVOLUCAO_VENDA_PERIODO_ATUAL | numeric(13) |  |  | Ajuste de redução - Devolução |
| DEVOLUCAO_VENDA_PERIODO_SEGUINTE | numeric(13) |  |  | Ajuste de redução para o período seguinte - Devolução |
| RETENCAO | numeric(13) |  |  | Retenções |
| COMPENSACAO_PAGAMENTO_A_MAIOR | numeric(13) |  |  | Compensação de pagamento indevido ou a maior |
| COMPENSACAO_RESSARCIMENTO_IPI | numeric(13) |  |  | Compensação de ressarcimento de IPI |
| COMPENSACAO_RESSARCIMENTO_IRPJ | numeric(13) |  |  | Compensação de saldo negativo de IRPJ |
| COMPENSACAO_RESSARCIMENTO_CSLL | numeric(13) |  |  | Compensação de saldo negativo de CSLL |
| COMPENSACAO_IRRF_COOPERATIVA | numeric(13) |  |  | Compensação de IRRF cooperativas de trabalho |
| COMPENSACAO_IRRF_JURO_CAPITAL | numeric(13) |  |  | Compensação de IRRF juros sobre capital próprio |
| DEBITO_UNIDADE_IMOBILIARIA | numeric(13) |  |  | Débito unidade imobiliária |
| DEVOLUCAO_VENDA | numeric(13) |  |  | Devolução de venda |
| RETENCAO_APROVEITADA | numeric(13) |  |  | Retenção aproveitada |
| DEBITO_CONTABILIZACAO | numeric(13) |  |  | Débito para contabilização |
| CREDITO_PERIODO_FINAL | numeric(13) |  |  | Total de créditos |
| CREDITO_PERIODO_ANTERIOR | numeric(13) |  |  | Ajuste de acréscimo período anterior - SCP |
| CREDITO_PERIODO_ATUAL | numeric(13) |  |  | Ajuste de acréscimo - SCP |
| CREDITO_PERIODO_SEGUINTE | numeric(13) |  |  | Ajuste de acréscimo para o período seguinte - SCP |
| CREDITO_DEVOLUCAO_EMPREEN_PERIODO_FINAL | numeric(13) |  |  | Ajuste de redução - Devoluções de créditos empreendimentos imobiliário utilizado no período |
| CREDITO_DEVOLUCAO_EMPREEN_PERIODO_ANTERIOR | numeric(13) |  |  | Ajuste de redução período anterior - Devolução |
| CREDITO_DEVOLUCAO_EMPREEN_PERIODO_ATUAL | numeric(13) |  |  | Ajuste de redução - Devolução |
| CREDITO_DEVOLUCAO_EMPREEN_PERIODO_SEGUINTE | numeric(13) |  |  | Ajuste de redução para o período seguinte - Devolução |
| CREDITO_DEVOLUCAO_COMPRA_PERIODO_FINAL | numeric(13) |  |  | Ajuste de redução - Devoluções de compras utilizado no período |
| CREDITO_DEVOLUCAO_COMPRA_PERIODO_ANTERIOR | numeric(13) |  |  | Ajuste de redução período anterior - Devolução |
| CREDITO_DEVOLUCAO_COMPRA_PERIODO_ATUAL | numeric(13) |  |  | Ajuste de redução - Devolução |
| CREDITO_DEVOLUCAO_COMPRA_PERIODO_SEGUINTE | numeric(13) |  |  | Ajuste de redução para o período seguinte - Devolução |
| SAIDA_CONTABILIZACAO | numeric(13) |  |  | Saídas para contabilização |
| DEVOLUCAO_COMPRA_FORA_PERIODO_CONTABILIZACAO | numeric(13) |  |  | Devolução de compra fora do período para contabilização |
| DEVOLUCAO_COMPRA_PERIODO_CONTABILIZACAO | numeric(13) |  |  | Devolução de compra para contabilização |
| DEVOLUCAO_VENDA_CONTABILIZACAO | numeric(13) |  |  | Devolução de venda para contabilização |
| CREDITO_CUSTO_INCORRIDO | numeric(13) |  |  | Crédito custo incorrido |
| CREDITO_PRESUMIDO_ORCADO | numeric(13) |  |  | Crédito presumido orçado |
| REDUCAO_RECEITA_CUMULATIVA | numeric(13) |  |  | Redução receita cumulativa |
| CREDITO_DEVOLUCAO_COMPRA_PERIODO | numeric(13) |  |  | Crédito devolução de compra no período |
| IRPJ_SAIDA_VALOR_RECEITA | numeric(13) |  |  | Saída valor receita |
| IRPJ_SAIDA_VALOR_CONTABIL | numeric(13) |  |  | Saída valor contábil |
| IRPJ_SAIDA_BASE_CALCULO | numeric(13) |  |  | Saída base de cálculo |
| IRPJ_SERVICO_VALOR_RECEITA | numeric(13) |  |  | Serviço valor receita |
| IRPJ_SERVICO_VALOR_CONTABIL | numeric(13) |  |  | Serviço valor contábil |
| IRPJ_SERVICO_BASE_CALCULO | numeric(13) |  |  | Serviço base de cálculo |
| IRPJ_ENTRADA_VALOR_RECEITA | numeric(13) |  |  | Entrada valor receita |
| IRPJ_ENTRADA_VALOR_CONTABIL | numeric(13) |  |  | Entrada valor contábil |
| IRPJ_ENTRADA_BASE_CALCULO | numeric(13) |  |  | Entrada base cálculo |
| IRPJ_IMOBILIARIA_VALOR_RECEITA | numeric(13) |  |  | Imobiliária valor receita |
| IRPJ_IMOBILIARIA_VALOR_CONTABIL | numeric(13) |  |  | Imobiliária valor contábil |
| IRPJ_IMOBILIARIA_BASE_CALCULO | numeric(13) |  |  | Imobiliária base de cálculo |
| IRPJ_IMOBILIARIA_DEV_VALOR_CONTABIL | numeric(13) |  |  | Imobiliária Devolução valor contábil |
| IRPJ_IMOBILIARIA_DEV_BASE_CALCULO | numeric(13) |  |  | Imobiliária Devolução base de cálculo |
| IRPJ_OUTRAS_RECEITAS | numeric(13) |  |  | Outras Receitas |
| IRPJ_ESTORNO_DESPESAS | numeric(13) |  |  | Estorno de Despeass |
| IRPJ_OUTRAS_DESPESAS | numeric(13) |  |  | Outras Despesas |
| IRPJ_ESTORNO_RECEITAS | numeric(13) |  |  | Estorno de Receitas |
| IRPJ_OUTRAS_DEDUCOES | numeric(13) |  |  | Outras Deduções |
| IRPJ_OUTROS_ACRESCIMOS | numeric(13) |  |  | Outros Acréscimos |
| IRPJ_INCENTIVO_PAT | numeric(13) |  |  | Incentivo PAT |
| IRPJ_VALE_TRANSPORTE | numeric(13) |  |  | Vale Transporte |
| IRPJ_OUTRAS_RECEITAS_SERVICO | numeric(13) |  |  | Outras Receitas de Serviço |
| IRPJ_PAGAMENTO_A_MAIOR | numeric(13) |  |  | Pagamento Indevido ou a Maior |
| IRPJ_VALOR_RETIDO_NOTA | numeric(13) |  |  | Valor Retido Nota |
| IRPJ_VALOR_RETIDO_OUTROS | numeric(13) |  |  | Valor Retido Outros |
| IRPJ_VALOR_RETIDO_CRFOP | numeric(13) |  |  | Valor Retido CRFOP |
| IRPJ_VALOR_RETIDO_IRRFP | numeric(13) |  |  | Valor Retido IRRFP |
| IRPJ_VALOR_DEVEDOR_MES_ANTERIOR | numeric(13) |  |  | Valor Devedor Mês Anterior |
| IRPJ_VALOR_ANTECIPADO_MES_ANTERIOR | numeric(13) |  |  | Valor Antecipado Mês Anterior |
| IRPJ_VALOR_DEVEDOR_SEGUNDO_MES | numeric(13) |  |  | Valor Devedor Segundo Mês |
| IRPJ_VALOR_RETENCAO_MES_ANTERIOR | numeric(13) |  |  | Valor Retenção Mês Anterior |
| IRPJ_VALOR_ANTECIPADO_SEGUNDO_MES | numeric(13) |  |  | Valor Antecipado Segundo Mês |
| IRPJ_VALOR_IRRF_PROPAGANDA_MES_ANTERIOR | numeric(13) |  |  | Valor IRRF Propaganda Mês Anterior |
| IRPJ_VALOR_RETENCAO_SEGUNDO_MES | numeric(13) |  |  | Valor Retenção Segundo Mês |
| IRPJ_VALOR_IRRF_PROPAGANDA_SEGUNDO_MES | numeric(13) |  |  | Valor IRRF Propaganda Segundo Mês |
| IRPJ_VALOR_ADICIONAL_IRPJ_MES_ANTERIOR | numeric(13) |  |  | Valor Adicional IRPJ Mês Anterior |
| IRPJ_BASE_NEGATIVA_ANTERIOR | numeric(13) |  |  | Base Negativa Anterior |
| IRPJ_BASE_NEGATIVA_ATUAL | numeric(13) |  |  | Base Negativa Atual |
| IRPJ_BASE_NEGATIVA_SEGUINTE | numeric(13) |  |  | Base Negativa Seguinte |
| IRPJ_VALOR_ADICIONAL | numeric(13) |  |  | Valor Adicional |
| IRPJ_VALOR_ADICIONAL_ANTERIOR | numeric(13) |  |  | Valor Adicional Anterior |
| IRPJ_BASE_CALCULO_MES_ANTERIOR | numeric(13) |  |  | Base Calculo Mês Anterior |
| IRPJ_BASE_CALCULO_SEGUNDO_MES | numeric(13) |  |  | Base Calculo Segundo Mês |
| IRPJ_RESSARCIMENTO_PISCOFINS | numeric(13) |  |  | Ressarcimento PIS/COFINS |
| IRPJ_VALOR_FIA | numeric(13) |  |  | Valor FIA |
| IRPJ_BASE_CALCULO_PERIODO | numeric(13) |  |  | Base de cálculo do período |
| CSLL_SAIDA_VALOR_RECEITA | numeric(13) |  |  | Saída valor receita |
| CSLL_SAIDA_VALOR_CONTABIL | numeric(13) |  |  | Saída valor contábil |
| CSLL_SAIDA_BASE_CALCULO | numeric(13) |  |  | Saída base de cálculo |
| CSLL_SERVICO_VALOR_RECEITA | numeric(13) |  |  | Serviço valor receita |
| CSLL_SERVICO_VALOR_CONTABIL | numeric(13) |  |  | Serviço valor contábil |
| CSLL_SERVICO_BASE_CALCULO | numeric(13) |  |  | Serviço base de cálculo |
| CSLL_ENTRADA_VALOR_RECEITA | numeric(13) |  |  | Entrada valor receita |
| CSLL_ENTRADA_VALOR_CONTABIL | numeric(13) |  |  | Entrada valor contábil |
| CSLL_ENTRADA_BASE_CALCULO | numeric(13) |  |  | Entrada base cálculo |
| CSLL_IMOBILIARIA_VALOR_RECEITA | numeric(13) |  |  | Imobiliária valor receita |
| CSLL_IMOBILIARIA_VALOR_CONTABIL | numeric(13) |  |  | Imobiliária valor contábil |
| CSLL_IMOBILIARIA_BASE_CALCULO | numeric(13) |  |  | Imobiliária base de cálculo |
| CSLL_IMOBILIARIA_DEV_VALOR_CONTABIL | numeric(13) |  |  | Imobiliária Devolução valor contábil |
| CSLL_IMOBILIARIA_DEV_BASE_CALCULO | numeric(13) |  |  | Imobiliária Devolução base de cálculo |
| CSLL_OUTRAS_RECEITAS | numeric(13) |  |  | Outras Receitas |
| CSLL_ESTORNO_DESPESAS | numeric(13) |  |  | Estorno de Despeass |
| CSLL_OUTRAS_DESPESAS | numeric(13) |  |  | Outras Despesas |
| CSLL_ESTORNO_RECEITAS | numeric(13) |  |  | Estorno de Receitas |
| CSLL_OUTRAS_DEDUCOES | numeric(13) |  |  | Outras Deduções |
| CSLL_OUTROS_ACRESCIMOS | numeric(13) |  |  | Outros Acréscimos |
| CSLL_OUTRAS_RECEITAS_SERVICO | numeric(13) |  |  | Outras Receitas de Serviço |
| CSLL_PAGAMENTO_A_MAIOR | numeric(13) |  |  | Pagamento Indevido ou a Maior |
| CSLL_VALOR_RETIDO_NOTA | numeric(13) |  |  | Valor Retido Nota |
| CSLL_VALOR_RETIDO_OUTROS | numeric(13) |  |  | Valor Retido Outros |
| CSLL_VALOR_RETIDO_CRFOP | numeric(13) |  |  | Valor Retido CRFOP |
| CSLL_VALOR_ANTECIPADO_MES_ANTERIOR | numeric(13) |  |  | Valor Antecipado Mês Anterior |
| CSLL_VALOR_ANTECIPADO_SEGUNDO_MES | numeric(13) |  |  | Valor Antecipado Segundo Mês |
| CSLL_VALOR_RETENCAO_MES_ANTERIOR | numeric(13) |  |  | Valor Retenção Mês Anterior |
| CSLL_VALOR_RETENCAO_SEGUNDO_MES | numeric(13) |  |  | Valor Retenção Segundo Mês |
| CSLL_BASE_CALCULO_MES_ANTERIOR | numeric(13) |  |  | Base Calculo Mês Anterior |
| CSLL_BASE_CALCULO_SEGUNDO_MES | numeric(13) |  |  | Base Calculo Segundo Mês |
| CSLL_VALOR_DEVEDOR_MES_ANTERIOR | numeric(13) |  |  | Valor Devedor Mês Anterior |
| CSLL_VALOR_DEVEDOR_SEGUNDO_MES | numeric(13) |  |  | Valor Devedor Segundo Mês |
| CSLL_BASE_NEGATIVA_ANTERIOR | numeric(13) |  |  | Base Negativa Anterior |
| CSLL_BASE_NEGATIVA_ATUAL | numeric(13) |  |  | Base Negativa Atual |
| CSLL_BASE_NEGATIVA_SEGUINTE | numeric(13) |  |  | Base Negativa Seguinte |
| CSLL_BASE_CALCULO_PERIODO | numeric(13) |  |  | Base de cálculo do período |
| RETENCAO_PERIODO | numeric(13) |  |  | Retenção do período |
| CREDITO_ENTRADA | numeric(13) |  |  | Créditos pelas Entradas |
| CSLL_OUTRAS_COMPENSACOES | numeric(13) |  |  | CSLL Outras compensações |
| IRPJ_OUTRAS_COMPENSACOES | numeric(13) |  |  | IRPJ Outras compensações |
| CSLL_OUTRAS_COMPENSACOES_COM_QUOTAS | numeric(13) |  |  | CSLL Outras compensações com quotas |
| CSLL_OUTRAS_COMPENSACOES_SEM_QUOTAS | numeric(13) |  |  | CSLL Outras compensações sem quotas |
| IRPJ_OUTRAS_COMPENSACOES_COM_QUOTAS | numeric(13) |  |  | IRPJ Outras compensações com quotas |
| IRPJ_OUTRAS_COMPENSACOES_SEM_QUOTAS | numeric(13) |  |  | IRPJ Outras compensações sem quotas |
| CSLL_PAGAMENTO_A_MAIOR_COM_QUOTAS | numeric(13) |  |  | CSLL Pagamento indevido com quotas |
| CSLL_PAGAMENTO_A_MAIOR_SEM_QUOTAS | numeric(13) |  |  | CSLL Pagamento indevido sem quotas |
| IRPJ_PAGAMENTO_A_MAIOR_COM_QUOTAS | numeric(13) |  |  | IRPJ Pagamento indevido com quotas |
| IRPJ_PAGAMENTO_A_MAIOR_SEM_QUOTAS | numeric(13) |  |  | IRPJ Pagamento indevido sem quotas |
| CSLL_ENTRADA_BONIFICACAO_VALOR_RECEITA | numeric(13) |  |  | CSLL Entrada Bonificação Valor Receita |
| CSLL_ENTRADA_BONIFICACAO_VALOR_CONTABIL | numeric(13) |  |  | CSLL Entrada Bonificação Valor Contabil |
| CSLL_ENTRADA_BONIFICACAO_BASE_CALCULO | numeric(13) |  |  | CSLL Entrada Bonificação Base Calculo |
| IRPJ_ENTRADA_BONIFICACAO_VALOR_RECEITA | numeric(13) |  |  | IRPJ Entrada Bonificação Valor Receita |
| IRPJ_ENTRADA_BONIFICACAO_VALOR_CONTABIL | numeric(13) |  |  | IRPJ Entrada Bonificação Valor Contabil |
| IRPJ_ENTRADA_BONIFICACAO_BASE_CALCULO | numeric(13) |  |  | IRPJ Entrada Bonificação Base Calculo |
| IRPJ_COMPENSACAO_SALDO_NEGATIVO | numeric(13) |  |  | IRPJ Compensação saldo negativo |
| CREDITO_PRESCRITO_PRAZO_DECADENCIAL | numeric(13) |  |  | Créditos prescritos em decorrência do término do prazo decadencial |
| RETENCAO_CRFOP_SALDO_RETENCOES_PERIODO | numeric(13) |  |  | Detalhamento CRFOP - Saldo das retenções do período |
| RETENCAO_CRFOP_RETENCOES_PERIODO | numeric(13) |  |  | Detalhamento CRFOP - Retenções do período |
| RETENCAO_CRFOP_SALDO_PERIODO_ANTERIOR | numeric(13) |  |  | Detalhamento CRFOP - Retenções do período anterior |
| RETENCAO_CRFOP_SALDO_DEVOLUCAO_VENDAS | numeric(13) |  |  | Detalhamento CRFOP - Saldo das devoluções de vendas do período |
| RETENCAO_CRFOP_DEVOLUCAO_PERIODO | numeric(13) |  |  | Detalhamento CRFOP - Devoluções de vendas do período |
| RETENCAO_CRFOP_DEVOLUCAO_PERIODO_ANTERIOR | numeric(13) |  |  | Detalhamento CRFOP - Devoluções de vendas do período anterior |
| RETENCAO_CRFOP_DEVOLUCAO_UTILIZADA | numeric(13) |  |  | Detalhamento CRFOP - Devoluções de vendas utilizadas no período |
| RETENCAO_CRFOP_DEVOLUCAO_RESTO | numeric(13) |  |  | Detalhamento CRFOP - Valor das devoluções de vendas para o período seguinte |
| RETENCAO_CRFOP_UTILIZADAS_PERIODO | numeric(13) |  |  | Detalhamento CRFOP - Valor das retenções a serem utilizadas no período |
| RETENCAO_CRFOP_PROXIMOS_PERIODOS | numeric(13) |  |  | Detalhamento CRFOP - Valor das retenções para o período seguinte |
| INSS_RB_DEVOLUCAO_RESTO | numeric(13) |  |  | Devolução de Vendas Total de todos os estabelecimentos - Resto |
| INSS_RB_DEVOLUCAO_RESTO_RELACIONADA | numeric(13) |  |  | Devolução de Vendas dos produtos ou serviços relacionados - Resto |
| INSS_RB_DEVOLUCAO_RESTO_NAO_RELACIONADA | numeric(13) |  |  | Devolução de Vendas dos produtos ou serviços não relacionados - Resto |
| INSS_RB_DEVOLUCAO_RESTO_RELACIONADA_EXPORTACAO | numeric(13) |  |  | Devolução de vendas dos produtos ou serviços relacionados de exportação - Resto |
| INSS_RB_DEVOLUCAO_RESTO_NAO_RELACIONADA_EXPORTACAO | numeric(13) |  |  | Devolução de Vendas dos produtos ou serviços não relacionados de exportação - Resto |
| INSS_RB_PERCENTUAL_NAO_RELACIONADO | numeric(16) |  |  | Percentual Não Relacionado |
| CSLL_VALOR_RETENCAO_APROVEITADA_MES | numeric(13) |  |  | CSLL Valor Retenção Aproveitada Mês |
| IRPJ_VALOR_RETENCAO_APROVEITADA_MES | numeric(13) |  |  | IRPJ Valor Retenção Aproveitada Mês |
| CREDITO_ATIVO_IMOBILIZADO | numeric(13) |  |  | Crédito Sobre Ativo Imobilizado |
| RET_BASE_CALCULO | numeric(13) |  |  | RET PAF e PMCMV - Base de cálculo |
| RET_BASE_CALCULO_APENAS_PAGO | numeric(13) |  |  | RET PAF e PMCMV - Base de cálculo apenas do valor pago |
| RET_BASE_NEGATIVA_ANTERIOR | numeric(13) |  |  | RET PAF e PMCMV - Base de devolução negativa do período anterior |
| RET_BASE_NEGATIVA_ATUAL | numeric(13) |  |  | RET PAF e PMCMV - Base de devolução negativa do período atual |
| RET_BASE_NEGATIVA_SEGUINTE | numeric(13) |  |  | RET PAF e PMCMV - Base de devolução negativa para o período seguinte |
| RET_VALOR_CORRECOES_APENAS_PAGO | numeric(13) |  |  | RET PAF e PMCMV - Valor das correções do valor pago |
| CSLL_VALOR_ANTECIPACAO_MAJORACAO_ANUAL | numeric(13) |  |  | CSLL Valor Antecipação Majoração Anual |
| IRPJ_VALOR_ANTECIPACAO_MAJORACAO_ANUAL | numeric(13) |  |  | IRPJ Valor Antecipação Majoração Anual |
| VALOR_CREDITO_LIMITE_TRIMESTRAL | numeric(13) |  |  | Valor de crédito limite disponível no trimestre |
