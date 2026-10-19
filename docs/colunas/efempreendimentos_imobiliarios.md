# EFEMPREENDIMENTOS_IMOBILIARIOS — Empreendimentos imobiliários - cadastro
7 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_EMPREENDIMENTO | integer(4) | PK |  | Código do empreendimento |
| NOME | varchar(255) |  |  | Nome |
| TIPO_UNIDADE_IMOBILIARIA | char(2) |  | S | Tipo de unidade imobiliária |
| NATUREZA_ESPECIFICA | char(2) |  | S | Natureza específica do empreendimento |
| DESCRICAO_RESUMIDA | char(90) |  | S | Descrição resumida |
| DATA_INICIO | date(4) |  | S | Data do início do empreendimento |
| AREA_TOTAL | numeric(13) |  | S | Área total |
| AREA_COM_DIREITO_A_CREDITO | numeric(13) |  | S | Área com direito a crédito |
| CALCULAR_CREDITO_PRESUMIDO_CUSTO_ORCADO | char(1) |  | S | Calcular crédito presumido do custo orçado |
| POSSUI_PROCESSO_REFERENCIADO | char(1) |  |  | Possui processo referenciado (S/N) |
| IDENTIFICACAO_REFERENCIADO | varchar(20) |  | S | Identificacao do processo |
| ORIGEM_REFERENCIADO | char(1) |  |  | Origem do processo (1=Justica Federal/ 3=Secretaria da Receita Federal do Brasil/ 9=Outros) |
| SECAO_JUDICIARIA | char(255) |  | S | Identificação da Seção judiciária |
| VARA | char(2) |  | S | Identificação da Vara |
| NATUREZA_ACAO | char(2) |  | S | Natureza da ação judicial |
| DATA_SENTENCA | date(4) |  | S | Data da Sentença/Decisão Judicial |
| DESCRICAO_PROCESSO | char(100) |  | S | Descrição |
| CT_DEBITO_CUSTO_INCORRIDO | integer(4) |  |  | Conta débito do custo incorrido |
| CT_CREDITO_CUSTO_INCORRIDO | integer(4) |  |  | Conta crédito do custo incorrido |
| CH_CUSTO_INCORRIDO | integer(4) |  |  | Histórico do custo incorrido |
| CT_DEBITO_CUSTO_ORCADO | integer(4) |  |  | Conta débito do custo orçado |
| CT_CREDITO_CUSTO_ORCADO | integer(4) |  |  | Conta crédito do custo orçado |
| CH_CUSTO_ORCADO | integer(4) |  |  | Histórico do custo orçado |
| CT_DEBITO_CONTRATO_RECEITA | integer(4) |  |  | Conta débito da receita do contrato de venda |
| CT_CREDITO_CONTRATO_RECEITA | integer(4) |  |  | Conta crédito da receita do contrato de venda |
| CH_CONTRATO_RECEITA | integer(4) |  |  | Histórico da receita do contrato de venda |
| CT_DEBITO_CONTRATO_ATUALIZACAO_MONETARIA | integer(4) |  |  | Conta débito da atualização monetária do contrato de venda |
| CT_CREDITO_CONTRATO_ATUALIZACAO_MONETARIA | integer(4) |  |  | Conta crédito da atualização monetária do contrato de venda |
| CH_DEBITO_CONTRATO_ATUALIZACAO_MONETARIA | integer(4) |  |  | Histórico da atualização monetária do contrato de venda |
| CT_RECEBIMENTO_RECEITA | integer(4) |  |  | Conta da receita do recebimento de parcelas |
| CH_RECEBIMENTO_RECEITA | integer(4) |  |  | Histórico da receita do recebimento de parcelas |
| CT_RECEBIMENTO_JUROS | integer(4) |  |  | Conta dos juros do recebimento de parcelas |
| CH_RECEBIMENTO_JUROS | integer(4) |  |  | Histórico dos juros do recebimento de parcelas |
| CT_RECEBIMENTO_MULTA | integer(4) |  |  | Conta da multa do recebimento de parcelas |
| CH_RECEBIMENTO_MULTA | integer(4) |  |  | Histórico multa do recebimento de parcelas |
| CT_RECEBIMENTO_DESCONTO | integer(4) |  |  | Conta da desconto do recebimento de parcelas |
| CH_RECEBIMENTO_DESCONTO | integer(4) |  |  | Histórico desconto do recebimento de parcelas |
| CT_RECEBIMENTO_ATUALIZACAO_MONETARIA | integer(4) |  |  | Conta da atualização monetária do recebimento de parcelas |
| CH_RECEBIMENTO_ATUALIZACAO_MONETARIA | integer(4) |  |  | Histórico da atualização monetária do recebimento de parcelas |
| CALCULAR_PIS_COFINS_CORRECAO_MONETARIA | char(1) |  |  | Cálcular PIS e COFINS para receitas de correção monetária |
| SOMA_VALOR_DESCONTO_BASE_CALCULO_PIS_COFINS | char(1) |  |  | Soma o valor do desconto na base de cálculo do PIS e da COFINS |
| CT_DEVOLUCAO_RECEITA | integer(4) |  |  | Conta da receita da devolução |
| CH_DEVOLUCAO_RECEITA | integer(4) |  |  | Histórico da receita da devolução |
| CT_DEVOLUCAO_ATUALIZACAO_MONETARIA | integer(4) |  |  | Conta da atualização monetária da devolução |
| CH_DEVOLUCAO_ATUALIZACAO_MONETARIA | integer(4) |  |  | Histórico da atualização monetária da devolução |
| RECEITA_BRUTA_DIFERENTE_CNAE_PRINCIPAL | char(1) |  |  | Receita bruta desse empreendimento é diferente do CNAE principal (S/N) |
| I_SCP | integer(4) |  | S | Sequencial do SCP |
| CONSIDERAR_DESCONTO_CALCULO_IRPJ_LP_CSOC | char(1) |  |  | Considerar o valor do desconto para o cálculo dos impostos IRPJ-LP e CSOC |
| CALCULAR_INSS_RB_CORRECAO_JURO_MULTA | char(1) |  |  | Não calcular INSS Receita Bruta para receitas de correção monetária, juros e multas |
| DATA_MATRICULA_CEI | date(4) |  | S | Data da matrícula no CEI |
| APLICAR_PERCENTUAL_PRESUNCAO_IRPJ_CSLL_JURO_MULTA | char(1) |  |  | Aplicar o percentual de presunção dos impostos IRPJ-LP e CSLL no cálculo das receitas de juros e multa |
| CH_DEVOLUCAO_DESCONTO | integer(4) |  |  | Histórico do Desconto da Devolução |
| CONTABILIZAR_CUSTO_INCORRIDO_VENDA_UNIDADE | char(1) |  |  | Contabilizar os custos incorridos na venda da unidade imobiliária |
| CONTABILIZAR_CUSTO_INCORRIDO_VENDA_UNIDADE_TIPO | integer(4) |  |  | Contabilizar os custos incorridos na venda da unidade imobiliária - Tipo (1/2) |
| CONTABILIZAR_CUSTO_RECEITA_PROPORCIONAL | char(1) |  |  | Contabilizar custos e receita proporcional ao recebimento da parcela |
| CONTABILIZAR_CUSTO_RECEITA_PROPORCIONAL_TIPO | integer(4) |  |  | Contabilizar custos e receita proporcional ao recebimento da parcela - Tipo (1/2) |
| CT_TRANSFERENCIA_CUSTO_INCORRIDO | integer(4) |  |  | Custo Incorrido - Transferência de custo incorrido na venda - Conta |
| CH_TRANSFERENCIA_CUSTO_INCORRIDO | integer(4) |  |  | Custo Incorrido - Transferência de custo incorrido na venda - Histórico |
| CT_RECEBIMENTO_RECONHECIMENTO_RECEITA | integer(4) |  |  | Recebimento de Parcela - Reconhecimento da Receita - Conta |
| CH_RECEBIMENTO_RECONHECIMENTO_RECEITA | integer(4) |  |  | Recebimento de Parcela - Reconhecimento da Receita - Histórico |
| CT_RECEBIMENTO_RECONHECIMENTO_CUSTO_RECEITA | integer(4) |  |  | Recebimento de Parcela - Reconhecimento Custo da Receita - Conta |
| CH_RECEBIMENTO_RECONHECIMENTO_CUSTO_RECEITA | integer(4) |  |  | Recebimento de Parcela - Reconhecimento Custo da Receita - Histórico |
| CONSIDERAR_RECEITAS_CORRECAO_MONETARIA_CALCULO_PIS_COFINS | integer(4) |  |  | Considerar as receitas de correção monetária no cálculo do PIS/COFINS |
| SOMA_VALOR_DESCONTO_BASE_CALCULO_INSS_RB | char(1) |  |  | Somar o valor do desconto na base de cálculo do INSS Receita Bruta |
| ENDERECO_EMPREENDIMENTO | varchar(60) |  | S | Endereço do Empreendimento Imobiliário |
| NUMERO_EMPREENDIMENTO | integer(4) |  | S | Número do Empreendimento Imobiliário |
| BAIRRO_EMPREENDIMENTO | varchar(60) |  | S | Bairro do Empreendimento Imobiliário |
| COMPLEMENTO_EMPREENDIMENTO | varchar(60) |  | S | Complemento do Empreendimento Imobiliário |
| CODIGO_MUNICIPIO_EMPREENDIMENTO | integer(4) |  | S | Municipio do Empreendimento Imobiliário |
| UF_EMPREENDIMENTO | char(2) |  | S | UF do Empreendimento Imobiliário |
| CEP_EMPREENDIMENTO | char(8) |  | S | CEP do Empreendimento Imobiliário |
| TIPO_EMPREENDIMENTO | char(1) |  |  | Tipo do Empreendimento Imobiliário (U/R) |
| I_CNO | integer(4) |  | S | Código CNO |
