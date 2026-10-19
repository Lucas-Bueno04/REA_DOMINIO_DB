# EFEMPREENDIMENTOS_IMOBILIARIOS_VIGENCIA — Empreendimentos imobiliários - Cadastro Vigência
7 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_EMPREENDIMENTO | integer(4) | PK |  | Código do empreendimento |
| VIGENCIA | date(4) | PK |  | Vigência |
| DESCRICAO | char(80) |  |  | Descrição Vigência |
| APLICAR_PERCENTUAL_PRESUNCAO_IRPJ_CSLL_JURO_MULTA | char(1) |  |  | Aplicar o percentual de presunção dos impostos IRPJ-LP e CSLL no cálculo das receitas de juros e multa |
| CALCULAR_INSS_RB_CORRECAO_JURO_MULTA | char(1) |  |  | Não calcular INSS Receita Bruta para receitas de correção monetária, juros e multas |
| CH_CONTRATO_RECEITA | integer(4) |  |  | Histórico da receita do contrato de venda |
| CH_CUSTO_INCORRIDO | integer(4) |  |  | Histórico do custo incorrido |
| CH_CUSTO_ORCADO | integer(4) |  |  | Histórico do custo orçado |
| CH_DEBITO_CONTRATO_ATUALIZACAO_MONETARIA | integer(4) |  |  | Histórico da atualização monetária do contrato de venda |
| CH_DEVOLUCAO_ATUALIZACAO_MONETARIA | integer(4) |  |  | Histórico da atualização monetária da devolução |
| CH_DEVOLUCAO_DESCONTO | integer(4) |  |  | Histórico do Desconto da Devolução |
| CH_DEVOLUCAO_RECEITA | integer(4) |  |  | Histórico da receita da devolução |
| CH_RECEBIMENTO_ATUALIZACAO_MONETARIA | integer(4) |  |  | Histórico da atualização monetária do recebimento de parcelas |
| CH_RECEBIMENTO_DESCONTO | integer(4) |  |  | Histórico desconto do recebimento de parcelas |
| CH_RECEBIMENTO_JUROS | integer(4) |  |  | Histórico dos juros do recebimento de parcelas |
| CH_RECEBIMENTO_MULTA | integer(4) |  |  | Histórico multa do recebimento de parcelas |
| CH_RECEBIMENTO_RECEITA | integer(4) |  |  | Histórico da receita do recebimento de parcelas |
| CH_RECEBIMENTO_RECONHECIMENTO_CUSTO_RECEITA | integer(4) |  |  | Recebimento de Parcela - Reconhecimento custo da Receita - Histórico |
| CH_RECEBIMENTO_RECONHECIMENTO_RECEITA | integer(4) |  |  | Recebimento de Parcela - Reconhecimento da Receita - Histórico |
| CH_TRANSFERENCIA_CUSTO_INCORRIDO | integer(4) |  |  | Custo Incorrido - Transferência de custo incorrido na venda - Histórico |
| CONSIDERAR_DESCONTO_CALCULO_IRPJ_LP_CSOC | char(1) |  |  | Considerar o valor do desconto para o cálculo dos impostos IRPJ-LP e CSOC |
| CONSIDERAR_RECEITAS_CORRECAO_MONETARIA_CALCULO_PIS_COFINS | integer(4) |  |  | Considerar as receitas de correção monetária no cálculo do PIS/COFINS |
| CONTABILIZAR_CUSTO_INCORRIDO_VENDA_UNIDADE | char(1) |  |  | Contabilizar os custos incorridos na venda da unidade imobiliária |
| CONTABILIZAR_CUSTO_INCORRIDO_VENDA_UNIDADE_TIPO | integer(4) |  |  | Contabilizar os custos incorridos na venda da unidade imobiliária - Tipo (1/2/3) |
| CONTABILIZAR_CUSTO_RECEITA_PROPORCIONAL | char(1) |  |  | Contabilizar custos e receita proporcional ao recebimento da parcela |
| CONTABILIZAR_CUSTO_RECEITA_PROPORCIONAL_TIPO | integer(4) |  |  | Contabilizar custos e receita proporcional ao recebimento da parcela - Tipo (1/2) |
| CT_CREDITO_CONTRATO_ATUALIZACAO_MONETARIA | integer(4) |  |  | Conta crédito da atualização monetária do contrato de venda |
| CT_CREDITO_CONTRATO_RECEITA | integer(4) |  |  | Conta crédito da receita do contrato de venda |
| CT_CREDITO_CUSTO_INCORRIDO | integer(4) |  |  | Conta crédito do custo incorrido |
| CT_CREDITO_CUSTO_ORCADO | integer(4) |  |  | Conta crédito do custo orçado |
| CT_DEBITO_CONTRATO_ATUALIZACAO_MONETARIA | integer(4) |  |  | Conta débito da atualização monetária do contrato de venda |
| CT_DEBITO_CONTRATO_RECEITA | integer(4) |  |  | Conta débito da receita do contrato de venda |
| CT_DEBITO_CUSTO_INCORRIDO | integer(4) |  |  | Conta débito do custo incorrido |
| CT_DEBITO_CUSTO_ORCADO | integer(4) |  |  | Conta débito do custo orçado |
| CT_DEVOLUCAO_ATUALIZACAO_MONETARIA | integer(4) |  |  | Conta da atualização monetária da devolução |
| CT_DEVOLUCAO_RECEITA | integer(4) |  |  | Conta da receita da devolução |
| CT_RECEBIMENTO_ATUALIZACAO_MONETARIA | integer(4) |  |  | Conta da atualização monetária do recebimento de parcelas |
| CT_RECEBIMENTO_DESCONTO | integer(4) |  |  | Conta da desconto do recebimento de parcelas |
| CT_RECEBIMENTO_JUROS | integer(4) |  |  | Conta dos juros do recebimento de parcelas |
| CT_RECEBIMENTO_MULTA | integer(4) |  |  | Conta da multa do recebimento de parcelas |
| CT_RECEBIMENTO_RECEITA | integer(4) |  |  | Conta da receita do recebimento de parcelas |
| CT_RECEBIMENTO_RECONHECIMENTO_CUSTO_RECEITA | integer(4) |  |  | Recebimento de Parcela - Reconhecimento custo da Receita - Conta |
| CT_RECEBIMENTO_RECONHECIMENTO_RECEITA | integer(4) |  |  | Recebimento de Parcela - Reconhecimento da Receita - Conta |
| CT_TRANSFERENCIA_CUSTO_INCORRIDO | integer(4) |  |  | Custo Incorrido - Transferência de custo incorrido na venda - Conta |
| RECEITA_BRUTA_DIFERENTE_CNAE_PRINCIPAL | char(1) |  |  | Receita bruta desse empreendimento é diferente do CNAE principal (S/N) |
| SOMA_VALOR_DESCONTO_BASE_CALCULO_INSS_RB | char(1) |  |  | Somar o valor do desconto na base de cálculo do INSS Receita Bruta |
| SOMA_VALOR_DESCONTO_BASE_CALCULO_PIS_COFINS | char(1) |  |  | Soma o valor do desconto na base de cálculo do PIS e da COFINS |
| TIPO_UNIDADE_IMOBILIARIA | varchar(2) |  | S | Tipo de unidade imobiliária |
| NATUREZA_ESPECIFICA | varchar(2) |  | S | Natureza específica do empreendimento |
| I_SCP | integer(4) |  | S | Sequencial do SCP |
| I_CNO | integer(4) |  | S | Sequencial do CNO |
| DESCRICAO_RESUMIDA | varchar(90) |  | S | Descrição Resumida |
| DATA_INICIO | date(4) |  | S | Data do início do empreendimento |
| DATA_MATRICULA_CEI | date(4) |  | S | Data da matrícula no CEI |
| AREA_TOTAL | numeric(13) |  | S | Área total |
| AREA_COM_DIREITO_A_CREDITO | numeric(13) |  | S | Área com direito a crédito |
| CALCULAR_CREDITO_PRESUMIDO_CUSTO_ORCADO | char(1) |  | S | Calcular crédito presumido do custo orçado |
| CONTABILIZAR_RECONHECIMENTO_REC_CTB_POC | char(1) |  |  | Contabilizar o reconhecimento da receita contábil conforme o Percentual de Obra Concluída - POC |
| CT_DEBITO_CONTRATO_REC_CTB | integer(4) |  |  | Conta débito contrato receita contábil |
| CT_CREDITO_CONTRATO_REC_CTB | integer(4) |  |  | Conta crédito contrato receita contábil |
| CH_CONTRATO_REC_CTB | integer(4) |  |  | Histório contrato receita contábil |
| CT_DEVOLUCAO_REC_CTB | integer(4) |  |  | Conta devolução contrato receita contábil |
| CH_DEVOLUCAO_REC_CTB | integer(4) |  |  | Histórico devolução contrato receita contábil |
| SOMA_VALOR_JUROS_E_MULTAS_BASE_CALCULO_PIS_COFINS | char(1) |  |  | Soma valor juros e multas base de calculo PIS e COFINS |
| DESCONSIDERAR_DESCONTO_BASE_CALCULO_RET | char(1) |  |  | Desconsiderar o valor do desconto na base de cálculo do RET |
| CONTABILIZAR_RECONHECIMENTO_REC_CTB_POC_TIPO | char(1) |  |  | Contabilizar o reconhecimento da receita contábil conforme o Percentual de Obra Concluída - POC TIPO |
| CALCULAR_IBS_CBS_ALIENACAO_BEM_IMOVEL | char(1) |  |  | Calcular IBS e CBS no momento do ato de alienação do bem imóvel |
| CONSIDERAR_RECEITA_E_CUSTO_UNIDADES | char(1) |  |  | Considerar a receita atualizada do contrato e o custo sobre as unidades vendidas |
