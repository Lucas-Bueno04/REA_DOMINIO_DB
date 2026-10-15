# efmvepro — Notas Fiscais de Entrada - Produtos
620.302 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_pdi | char(14) |  |  | Produto |
| codi_emp | integer(4) | PK |  | Empresa |
| codi_ent | integer(4) | PK |  | Entrada |
| qtde_mep | numeric(13) |  |  | Quantidade |
| vlor_mep | numeric(13) |  |  | Valor total (Base calculo + Valor IPI) |
| vipi_mep | numeric(13) |  |  | Valor do IPI |
| bcal_mep | numeric(13) |  |  | Base de calculo |
| nume_mep | integer(4) | PK |  | Sequencial |
| orig_mep | tinyint(1) |  |  | Origem do movimento (1 - Nota/2 - Extra) |
| data_mep | date(4) |  | S | Data |
| nrodi_mep | numeric(10) |  | S | Numero da DI |
| cst_mep | integer(4) |  | S | Codigo da Situacao Tributaria |
| vpro_mep | numeric(13) |  | S | Valor do Produto |
| vdes_mep | numeric(13) |  | S | Valor do Desconto |
| bicms_mep | numeric(13) |  | S | Base do ICMS |
| bicmsst_mep | numeric(13) |  | S | Base do ICMS para Substituicao Tributaria |
| aliicms_mep | numeric(13) |  | S | Aliquota do ICMS |
| incentivado_mep | char(1) |  | S | Produto incentivado (S/N) - PE |
| apuracao_mep | integer(4) |  | S | Codigo da Apuracao - PE |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| vfre_mep | numeric(13) |  | S | Valor do frete |
| vseg_mep | numeric(13) |  | S | Valor do seguro |
| vdesace_mep | numeric(13) |  | S | Valor das despesas acessorias |
| qtd_gasolinaa_mep | numeric(13) |  | S | Quantidade de Gasolina A |
| valor_icms_mep | numeric(13) |  | S | Valor do ICMS |
| valor_subtri_mep | numeric(13) |  |  | Valor da SUBTRI |
| isentas_ipi_mep | numeric(13) |  | S | Valor de isentas IPI |
| outras_ipi_mep | numeric(13) |  | S | Valor de outras IPI |
| icms_nfp_mep | numeric(13) |  | S | ICMS NFP |
| valor_unit_mep | numeric(15) |  | S | Valor unitario |
| aliq_st_mep | numeric(5) |  | S | Aliquota da Substituicao tributaria |
| codigo_trib_mep | tinyint(1) |  | S | Codigo de tributacao |
| aliq_ipi_mep | numeric(5) |  | S | Aliquota de IPI |
| bc_issqn_mep | numeric(13) |  | S | Base de calculo ISSQN |
| aliq_issqn_mep | numeric(5) |  | S | Aliquota de ISSQN |
| valor_issqn_mep | numeric(13) |  | S | Valor ISSQN |
| cfop_mep | integer(4) |  | S | CFOP |
| serie_ecf_mep | char(20) |  | S | Serie de fabricacao do ECF |
| aliq_pis_mep | numeric(7) |  | S | Aliquota do PIS |
| valor_pis_mep | numeric(13) |  | S | Valor do PIS |
| aliq_cofins_mep | numeric(7) |  | S | Aliquota da COFINS |
| valor_cofins_mep | numeric(13) |  | S | Valor da COFINS |
| custo_total_mep | numeric(13) |  | S | Custo total do produto |
| cst_pis_mep | integer(4) |  | S | CST do PIS |
| bc_pis_mep | numeric(13) |  | S | Base de calculo do PIS |
| cst_cofins_mep | integer(4) |  | S | CST do COFINS |
| bc_cofins_mep | numeric(13) |  | S | Base de calculo do COFINS |
| chassi_mep | varchar(17) |  | S | Chassi do veiculo |
| operacao_veiculo_mep | tinyint(1) |  | S | Tipo de operacao com veiculo(0=Concessionaria/1=Faturamento/2=Venda direta/9=Outras) |
| lote_medic_mep | varchar(255) |  | S | Lote do medicamento |
| qtde_item_lote_mep | integer(4) |  | S | Quantidade de item por lote de medicamento |
| validade_mep | date(4) |  | S | Data de validade |
| fabricacao_mep | date(4) |  | S | Data de fabricacao do medicamento |
| referencia_bc_mep | tinyint(1) |  | S | REFERENCIA BASE DE CALCULO (0 - TABELADO/1 - NEGATIVA/2 - POSITIVA/3  NEUTRA/4 - MARGEM VALOR AGREGADO/5 - PAUTA/6-VALOR DA OPERAÇÃO) |
| valor_tab_max_mep | numeric(13) |  | S | Valor tabelado/maximo |
| nro_serie_arma_mep | varchar(255) |  | S | Numero de serie da arma |
| nro_serie_cano_mep | varchar(255) |  | S | Numero de serie do cano |
| enquadramento_ipi_mep | char(3) |  | S | Enquadramento do IPI |
| MOVIMENTACAO_FISICA_MEP | char(1) |  |  | Movimentação física de produto (S/N) |
| CODIGO_UNIDADE | integer(4) |  | S | Código da unidade |
| UNIDADE | char(6) |  | S | Unidade comercializada |
| COMPLEMENTO_CFOP_CAT_17_99 | integer(4) |  | S | Complemento da CFOP - Portaria Cat nº 17/99 |
| CODI_SAI_DEVOLVIDA | integer(4) |  | S | Código da nota de saída devolvida |
| I_TANQUE | integer(4) |  | S | Tanque do combustível |
| VALOR_CONTABIL_MEP | numeric(13) |  | S | Valor contabil produto |
| QTDE_TRIBUTARIA_MEDIDA_PIS_MEP | numeric(13) |  | S | Quantidade tributada PIS por unidade de medida |
| VALOR_UNIDADE_MEDIDA_PIS_MEP | numeric(13) |  | S | Valor unidade PIS por unidade de medida |
| VALOR_MEDIDA_PIS_MEP | numeric(13) |  | S | Valor PIS por unidade de medida |
| QTDE_TRIBUTARIA_MEDIDA_COFINS_MEP | numeric(13) |  | S | Quantidade tributada COFINS por unidade de medida |
| VALOR_UNIDADE_MEDIDA_COFINS_MEP | numeric(13) |  | S | Valor unidade COFINS por unidade de medida |
| VALOR_MEDIDA_COFINS_MEP | numeric(13) |  | S | Valor COFINS por unidade de medida |
| BASE_CREDITO_MEP | integer(4) |  | S | Base do credito |
| DADOS_PISCOFINS_OK | char(1) |  |  | Dados referente ao PIS/COFINS OK (S/N) |
| I_REDUCAO_DEVOLVIDA | integer(4) |  | S | Código da redução Z devolvida |
| I_CUPOM_DEVOLVIDO | integer(4) |  | S | Código do cupom fiscal devolvido |
| TIPO_DOCUMENTO_DEVOLVIDO | char(1) |  | S | Tipo do documento fiscal que está sendo devolvido(S - Nota de saída/Z - Redução Z/C - Cupom fiscal/F - Cupom fiscal eletrônico) |
| COMBUSTIVEL_OPERACAO_MEP | integer(4) |  | S | Operação |
| COMBUSTIVEL_MODAL_MEP | integer(4) |  | S | Modal |
| COMBUSTIVEL_CODIGO_VEICULO_MEP | varchar(7) |  |  | Código Veículo |
| COMBUSTIVEL_SERVICO_MEP | integer(4) |  | S | Serviço |
| DESCRICAO_COMPLEMENTAR_MEP | varchar(255) |  | S | Descrição complementar |
| CST_PIS_DEVOLVIDA_MEP | integer(4) |  | S | CST do PIS da nota devolvida |
| CST_COFINS_DEVOLVIDA_MEP | integer(4) |  | S | CST do COFINS da nota devolvida |
| FUNDESA_INCIDENCIA | integer(4) |  |  | FUNDESA - Incidência |
| FUNDESA_VALOR_UNITARIO | numeric(18) |  |  | FUNDESA - Valor unitário |
| FUNDESA_VALOR_PRODUTOR | numeric(13) |  |  | FUNDESA - Valor produtor |
| FUNDESA_VALOR_INDUSTRIA | numeric(13) |  |  | FUNDESA - Valor indústria |
| FUNDESA_VALOR_TOTAL | numeric(13) |  |  | FUNDESA - Valor total |
| VINCULO_CREDITO_PIS_MEP | tinyint(1) |  | S | Vínculo do crédito do PIS |
| VINCULO_CREDITO_COFINS_MEP | tinyint(1) |  | S | Vínculo do crédito do COFINS |
| I_CST_VIGENCIA_ICMS | integer(4) |  | S | Código sequencial do CST de ICMS |
| CUSTO_MEDIO_REMESSA_MEP | numeric(16) |  |  | Custo médio da Nota de Remessa |
| CODIGO_IMPOSTO_IPI | integer(4) |  |  | Código do Imposto IPI |
| UNIDADE_MEDIDA_QUANTIDADE_TRIBUTADA_IPI | numeric(13) |  |  | Unidade de Medida Quantidade Tributada IPI |
| UNIDADE_MEDIDA_VALOR_POR_UNIDADE_IPI | numeric(13) |  |  | Unidade de Medida Valor por Unidade IPI |
| UNIDADE_MEDIDA_VALOR_IMPOSTO_IPI | numeric(13) |  |  | Unidade de Medida Valor do Imposto IPI |
| EXCLUSAO_PIS | numeric(13) |  |  | Exclusão PIS |
| EXCLUSAO_COFINS | numeric(13) |  |  | Exclusão COFINS |
| PERCENTUAL_REDUCAO_BC_PIS_MEP | numeric(5) |  |  | Percentual Redução Base Cálculo PIS |
| PERCENTUAL_REDUCAO_BC_COFINS_MEP | numeric(5) |  |  | Percentual Redução Base Cálculo COFINS |
| I_RECOLHIMENTO_IPI | integer(4) |  | S | Sequencial do Código de Recolhimento do IPI |
| CODIGO_RECOLHIMENTO_IPI | char(6) |  | S | Código de Recolhimento do IPI |
| I_RECOLHIMENTO_PIS_DEVOLVIDO | integer(4) |  | S | Código Sequencial do Recolhimento do PIS Nota Devolvida |
| CODIGO_RECOLHIMENTO_PIS_DEVOLVIDO | char(6) |  |  | Código do Recolhimento do PIS Nota Devolvida |
| I_RECOLHIMENTO_COFINS_DEVOLVIDO | integer(4) |  | S | Código Sequencial do Recolhimento do COFINS Nota Devolvida |
| CODIGO_RECOLHIMENTO_COFINS_DEVOLVIDO | char(6) |  |  | Código do Recolhimento do COFINS Nota Devolvida |
| I_RECOLHIMENTO_PIS | integer(4) |  | S | Código Sequencial do Recolhimento do PIS |
| CODIGO_RECOLHIMENTO_PIS | char(6) |  |  | Código do Recolhimento do PIS |
| I_RECOLHIMENTO_COFINS | integer(4) |  | S | Código Sequencial do Recolhimento do COFINS |
| CODIGO_RECOLHIMENTO_COFINS | char(6) |  |  | Código do Recolhimento do COFINS |
| VALOR_CREDITO_PRESUMIDO_BEBIDA_FRIA_13097_PIS | numeric(13) |  |  | Crédito Presumido na aquisição de bebidas frias - Art. 31 da Lei 13.097/2015 - PIS |
| VALOR_CREDITO_PRESUMIDO_BEBIDA_FRIA_13097_COFINS | numeric(13) |  |  | Crédito Presumido na aquisição de bebidas frias - Art. 31 da Lei 13.097/2015 - COFINS |
| VALOR_RESSARCIDO_ST_MEP | numeric(13) |  |  | Valor Ressarcido ST |
| CODIGO_CEST | char(7) |  | S | Código CEST |
| COMBUSTIVEL_ARMAZENAR_EM_MAIS_DE_UM_TANQUE | char(1) |  |  | Combústivel - Armazenar em mais de um tanque |
| I_CFE_DEVOLVIDA | integer(4) |  | S | Código do cupom fiscal eletrônico devolvido |
| MEDICAMENTO_INFORMAR_MAIS_DE_UM_LOTE | char(1) |  |  | Medicamentos - Informar mais de um lote (S/N) |
| PRECO_FOB | numeric(13) |  |  | Preço FOB |
| SEQUENCIAL_ITEM_MEP | integer(4) |  | S | Sequencial Item |
| RJ_I_SEQUENCIAL_BENEFICIO | integer(4) |  | S | Sequencial do Código do Benefício RJ |
| BOLETIM_CONFORMIDADE | varchar(10) |  | S | Boletim de Conformidade |
| VALOR_ICMS_CALCULADO | numeric(13) |  |  | Valor do ICMS calculado quando não houver valor de "ICMS Próprio" no produto |
| SC_I_SEQUENCIAL_BENEFICIO | integer(4) |  | S | Sequencial do Código do Benefício SC |
| VALOR_ICMS_PROPRIO_DIFERIDO | numeric(13) |  |  | ICMS Diferido |
| SP_I_SEQUENCIAL_BENEFICIO | integer(4) |  | S | Sequencial do codigo do beneficio SP |
| GO_I_SEQUENCIAL_BENEFICIO | integer(4) |  | S | Sequencial do codigo do beneficio GO |
| CODIGO_CRED_PRESUM_PROD_RURAL | integer(4) |  | S | Código do crédito presumido de produtor rural(1 - Aquisição de produtor rural não contribuinte - art. 168 da LC 214/2025) |
