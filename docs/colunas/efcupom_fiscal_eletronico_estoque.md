# EFCUPOM_FISCAL_ELETRONICO_ESTOQUE — Cupom Fiscal Eletrônico - CF-e - Estoque
12.416.469 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_CFE | integer(4) | PK |  | Código do CF-e |
| I_ESTOQUE | integer(4) | PK |  | Sequencial do estoque |
| CODI_PDI | char(14) |  |  | Produto |
| CODIGO_UNIDADE | integer(4) |  | S | Código da unidade |
| UNIDADE | char(6) |  | S | Unidade comercializada |
| QUANTIDADE | numeric(13) |  |  | Quantidade |
| VALOR_UNITARIO | numeric(15) |  |  | Valor unitário |
| VALOR_PRODUTO | numeric(13) |  |  | Valor do produto |
| DESCONTO | numeric(13) |  |  | Valor do desconto |
| ACRESCIMO | numeric(13) |  |  | Valor do acréscimo |
| VALOR_TOTAL | numeric(13) |  |  | Valor total |
| CODI_NAT | integer(4) |  |  | CFOP |
| VERSAO_NAT | smallint(2) |  |  | Versão da CFOP |
| CODI_ACU | integer(4) |  |  | Código do acumulador |
| I_BICO | integer(4) |  | S | Bico do combustível |
| I_TANQUE | integer(4) |  | S | Tanque do combustível |
| CST_ICMS | integer(4) |  |  | Codigo da Situação Tributaria(ICMS) |
| I_CST_VIGENCIA_ICMS | integer(4) |  | S | Código sequencial do CST de ICMS |
| BASE_CALCULO_ICMS | numeric(13) |  |  | Base de cálculo do ICMS |
| ALIQUOTA_ICMS | numeric(5) |  |  | Alíquota do ICMS |
| VALOR_ICMS | numeric(13) |  |  | Valor do ICMS |
| CST_PIS | integer(4) |  |  | CST do PIS |
| NATUREZA_RECEITA_PIS | integer(4) |  | S | Natureza da receita do PIS |
| PERCENTUAL_REDUCAO_BC_PIS | numeric(5) |  |  | Percentual Redução Base Cálculo PIS |
| BASE_CALCULO_PIS | numeric(13) |  |  | Base de cálculo do PIS |
| ALIQUOTA_PIS | numeric(7) |  |  | Alíquota do PIS |
| VALOR_PIS | numeric(13) |  |  | Valor do PIS |
| QTDE_TRIBUTARIA_MEDIDA_PIS | numeric(13) |  |  | Quantidade tributada PIS por unidade de medida |
| VALOR_UNIDADE_MEDIDA_PIS | numeric(13) |  |  | Valor unidade PIS por unidade de medida |
| VALOR_MEDIDA_PIS | numeric(13) |  |  | Valor PIS por unidade de medida |
| CST_COFINS | integer(4) |  |  | CST da COFINS |
| NATUREZA_RECEITA_COFINS | integer(4) |  | S | Natureza da receita do COFINS |
| PERCENTUAL_REDUCAO_BC_COFINS | numeric(5) |  |  | Percentual Redução Base Cálculo COFINS |
| BASE_CALCULO_COFINS | numeric(13) |  |  | Base de cálculo da COFINS |
| ALIQUOTA_COFINS | numeric(7) |  |  | Alíquota da COFINS |
| VALOR_COFINS | numeric(13) |  |  | Valor da COFINS |
| QTDE_TRIBUTARIA_MEDIDA_COFINS | numeric(13) |  |  | Quantidade tributada COFINS por unidade de medida |
| VALOR_UNIDADE_MEDIDA_COFINS | numeric(13) |  |  | Valor unidade COFINS por unidade de medida |
| VALOR_MEDIDA_COFINS | numeric(13) |  |  | Valor COFINS por unidade de medida |
| DADOS_PISCOFINS_OK | char(1) |  |  | Dados referente ao PIS/COFINS OK (S/N) |
| EXCLUSAO_COOPERATIVA | numeric(13) |  | S | Exclusão cooperativa |
| COMBUSTIVEL_OPERACAO | integer(4) |  | S | Operação |
| COMBUSTIVEL_MODAL | integer(4) |  | S | Modal |
| COMBUSTIVEL_CODIGO_VEICULO | varchar(7) |  |  | Código Veículo |
| COMBUSTIVEL_SERVICO | integer(4) |  | S | Serviço |
| I_RECOLHIMENTO_PIS | integer(4) |  | S | Código Sequencial do Recolhimento do PIS |
| CODIGO_RECOLHIMENTO_PIS | char(6) |  |  | Código do Recolhimento do PIS |
| I_RECOLHIMENTO_COFINS | integer(4) |  | S | Código Sequencial do Recolhimento do COFINS |
| CODIGO_RECOLHIMENTO_COFINS | char(6) |  |  | Código do Recolhimento do COFINS |
| CODIGO_CEST | char(7) |  | S | Código CEST |
| SP_BASE_CALCULO_FECOEP_PROPRIO | numeric(13) |  |  | FECOEP - ICMS Próprio - Base de cálculo |
| SP_ALIQUOTA_FECOEP_PROPRIO | numeric(5) |  |  | FECOEP - ICMS Próprio - Alíquota |
| SP_VALOR_FECOEP_PROPRIO | numeric(13) |  |  | FECOEP - ICMS Próprio - Valor |
| CE_BASE_CALCULO_FECOP | numeric(13) |  |  | FECOP CE - ICMS Próprio - Base de cálculo |
| CE_ALIQUOTA_FECOP | numeric(5) |  |  | FECOP CE - ICMS Próprio - Alíquota |
| CE_VALOR_FECOP | numeric(13) |  |  | FECOP CE - ICMS Próprio - Valor |
