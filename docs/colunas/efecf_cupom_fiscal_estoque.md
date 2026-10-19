# EFECF_CUPOM_FISCAL_ESTOQUE — ECF - Cupom fiscal - Estoque
189.652 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_REDUCAO | integer(4) | PK |  | Código da redução Z |
| I_CUPOM | integer(4) | PK |  | Sequencial do cupom fiscal |
| I_ESTOQUE | integer(4) | PK |  | Sequencial do estoque |
| CODI_PDI | char(14) |  |  | Produto |
| QUANTIDADE | numeric(13) |  |  | Quantidade |
| QUANTIDADE_CANCELADA | numeric(15) |  |  | Quantidade cancelada |
| CODIGO_UNIDADE | integer(4) |  | S | Código da unidade |
| UNIDADE | char(6) |  | S | Unidade comercializada |
| VALOR_UNITARIO | numeric(15) |  |  | Valor unitário |
| VALOR_TOTAL | numeric(13) |  |  | Valor total |
| DESCONTO | numeric(13) |  |  | Valor do desconto |
| CANCELAMENTO | numeric(13) |  |  | Valor do cancelamento |
| ACRESCIMO | numeric(13) |  |  | Valor do acréscimo |
| VALOR_LIQUIDO | numeric(13) |  |  | Valor líquido |
| VALOR_ISSQN | numeric(13) |  |  | Valor do ISSQN |
| CST_ICMS | integer(4) |  |  | Código da Situação Tributária ICMS |
| OPERACAO | integer(4) |  |  | Operação |
| CFOP | integer(4) |  |  | CFOP |
| BASE_CALCULO_ICMS | numeric(13) |  |  | Base de cálculo do ICMS |
| ALIQUOTA_ICMS | numeric(5) |  |  | Alíquota do ICMS |
| VALOR_ICMS | numeric(13) |  |  | Valor do ICMS |
| ISENTAS_ICMS | numeric(13) |  |  | Valor de isentas do ICMS |
| NAO_TRIBUTADAS_ICMS | numeric(13) |  |  | Valor não tributado do ICMS |
| ADQUIRIDA_SUBTRI | numeric(13) |  |  | Valor adquirido com ST |
| BASE_CALCULO_PIS | numeric(13) |  |  | Base de cálculo do PIS |
| ALIQUOTA_PIS | numeric(7) |  |  | Alíquota do PIS |
| VALOR_PIS | numeric(13) |  |  | Valor do PIS |
| BASE_CALCULO_COFINS | numeric(13) |  |  | Base de cálculo da COFINS |
| ALIQUOTA_COFINS | numeric(7) |  |  | Alíquota da COFINS |
| VALOR_COFINS | numeric(13) |  |  | Valor da COFINS |
| MOVIMENTACAO_FISICA | char(1) |  |  | Movimentação física de produto(S/N) |
| ORIGEM_REG | integer(4) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| CST_PIS | integer(4) |  |  | CST do PIS |
| CST_COFINS | integer(4) |  |  | CST da COFINS |
| I_BICO | integer(4) |  | S | Bico do combustível |
| QTDE_TRIBUTARIA_MEDIDA_PIS | numeric(13) |  |  | Quantidade tributada PIS por unidade de medida |
| VALOR_UNIDADE_MEDIDA_PIS | numeric(13) |  |  | Valor unidade PIS por unidade de medida |
| VALOR_MEDIDA_PIS | numeric(13) |  |  | Valor PIS por unidade de medida |
| QTDE_TRIBUTARIA_MEDIDA_COFINS | numeric(13) |  |  | Quantidade tributada COFINS por unidade de medida |
| VALOR_UNIDADE_MEDIDA_COFINS | numeric(13) |  |  | Valor unidade COFINS por unidade de medida |
| VALOR_MEDIDA_COFINS | numeric(13) |  |  | Valor COFINS por unidade de medida |
| DADOS_PISCOFINS_OK | char(1) |  |  | Dados referente ao PIS/COFINS OK (S/N) |
| CST_ISSQN | integer(4) |  | S | CST do ISSQN |
| BASE_CALCULO_ISSQN | numeric(13) |  |  | Base de cálculo do ISSQN |
| ALIQUOTA_ISSQN | numeric(5) |  |  | Alíquota do ISSQN |
| ISENTAS_ISSQN | numeric(13) |  |  | Isentas de ISSQN |
| NAO_INCIDENCIA_ISSQN | numeric(13) |  |  | Não incidência de ISSQN |
| COMBUSTIVEL_OPERACAO | integer(4) |  | S | Operação |
| COMBUSTIVEL_MODAL | integer(4) |  | S | Modal |
| COMBUSTIVEL_CODIGO_VEICULO | varchar(7) |  |  | Código Veículo |
| COMBUSTIVEL_SERVICO | integer(4) |  | S | Serviço |
| NATUREZA_RECEITA_PIS | integer(4) |  | S | Natureza da receita do PIS |
| NATUREZA_RECEITA_COFINS | integer(4) |  | S | Natureza da receita do COFINS |
| EXCLUSAO_COOPERATIVA | numeric(13) |  | S | Exclusão cooperativa |
| I_CST_VIGENCIA_ICMS | integer(4) |  | S | Código sequencial do CST de ICMS |
| I_TANQUE | integer(4) |  | S | Tanque do combustível |
| PERCENTUAL_REDUCAO_BC_PIS | numeric(5) |  |  | Percentual Redução Base Cálculo PIS |
| PERCENTUAL_REDUCAO_BC_COFINS | numeric(5) |  |  | Percentual Redução Base Cálculo COFINS |
| I_RECOLHIMENTO_PIS | integer(4) |  | S | Código Sequencial do Recolhimento do PIS |
| CODIGO_RECOLHIMENTO_PIS | char(6) |  |  | Código do Recolhimento do PIS |
| I_RECOLHIMENTO_COFINS | integer(4) |  | S | Código Sequencial do Recolhimento do COFINS |
| CODIGO_RECOLHIMENTO_COFINS | char(6) |  |  | Código do Recolhimento do COFINS |
| BASE_AMPARA_ICMS_PROPRIO | numeric(13) |  |  | Base  Ampara/RS |
| ALIQUOTA_AMPARA_ICMS_PROPRIO | numeric(13) |  |  | Alíquota  Ampara/RS |
| VALOR_AMPARA_ICMS_PROPRIO | numeric(13) |  |  | Valor  Ampara/RS |
| SP_BASE_CALCULO_FECOEP_PROPRIO | numeric(13) |  |  | FECOEP SP - ICMS PRÓPRIO - BASE DE CÁLCULO |
| SP_ALIQUOTA_FECOEP_PROPRIO | numeric(5) |  |  | FECOEP SP - ICMS PRÓPRIO - ALÍQUOTA |
| SP_VALOR_FECOEP_PROPRIO | numeric(13) |  |  | FECOEP SP - ICMS PRÓPRIO - VALOR |
| TO_BASE_CALCULO_FECOEP_PROPRIO | numeric(13) |  |  | FECOEP TO - ICMS Próprio - Base de cálculo |
| TO_ALIQUOTA_FECOEP_PROPRIO | numeric(5) |  |  | FECOEP TO - ICMS Próprio - Alíquota |
| TO_VALOR_FECOEP_PROPRIO | numeric(13) |  |  | FECOEP TO - ICMS Próprio - Valor |
| PR_BASE_CALCULO_FECOEP_PROPRIO | numeric(13) |  |  | FECOEP PR - ICMS Próprio - Base de cálculo |
| PR_ALIQUOTA_FECOEP_PROPRIO | numeric(5) |  |  | FECOEP PR - ICMS Próprio - Alíquota |
| PR_VALOR_FECOEP_PROPRIO | numeric(13) |  |  | FECOEP PR - ICMS Próprio - Valor |
| MS_BASE_CALCULO_FECOMP_MS_ICMS_PROPRIO | numeric(13) |  |  | FECOMP MS - ICMS Próprio - Base de cálculo |
| MS_ALIQUOTA_FECOMP_MS_ICMS_PROPRIO | numeric(13) |  |  | FECOMP MS - ICMS Próprio - Alíquota |
| MS_VALOR_FECOMP_MS_ICMS_PROPRIO | numeric(13) |  |  | FECOMP MS - ICMS Próprio - Valor |
| RO_BASE_CALCULO_FECOEP_PROPRIO | numeric(13) |  |  | FECOEP RO - ICMS Próprio - Base de cálculo |
| RO_ALIQUOTA_FECOEP_PROPRIO | numeric(5) |  |  | FECOEP RO - ICMS Próprio - Alíquota |
| RO_VALOR_FECOEP_PROPRIO | numeric(13) |  |  | FECOEP RO - ICMS Próprio - Valor |
| PRECO_FOB | numeric(13) |  |  | Preço FOB |
| MT_BASE_CALCULO_FECEP | numeric(13) |  |  | FECEP MT - ICMS Próprio - Base de cálculo |
| MT_ALIQUOTA_FECEP | numeric(5) |  |  | FECEP MT - ICMS Próprio - Alíquota |
| MT_VALOR_FECEP | numeric(13) |  |  | FECEP MT - ICMS Próprio - Valor |
| PI_BASE_CALCULO_FECOP | numeric(13) |  |  | FECOP PI - Base de cálculo |
| PI_ALIQUOTA_FECOP | numeric(13) |  |  | FECOP PI - Alíquota |
| PI_VALOR_FECOP | numeric(13) |  |  | FECOP PI - Valor |
| ES_BASE_CALCULO_FUNCOP | numeric(13) |  |  | FUNCOP-ES Base de cálculo |
| ES_ALIQUOTA_FUNCOP | numeric(5) |  |  | FUNCOP-ES Alíquota |
| ES_VALOR_FUNCOP | numeric(13) |  |  | FUNCOP-ES Valor |
| RN_BASE_CALCULO_FECOP | numeric(13) |  |  | FECOP RN - ICMS Próprio - Base de cálculo |
| RN_ALIQUOTA_FECOP | numeric(5) |  |  | FECOP RN - ICMS Próprio - Alíquota |
| RN_VALOR_FECOP | numeric(13) |  |  | FECOP RN - ICMS Próprio - Valor |
| CE_BASE_CALCULO_FECOP | numeric(13) |  |  | FECOP CE - ICMS Próprio - Base de cálculo |
| CE_ALIQUOTA_FECOP | numeric(5) |  |  | FECOP CE - ICMS Próprio - Alíquota |
| CE_VALOR_FECOP | numeric(13) |  |  | FECOP CE - ICMS Próprio - Valor |
