# efmvspro — Notas Fiscais de Saida - Produtos
1.338.693 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_pdi | char(14) |  |  | Produto |
| codi_emp | integer(4) | PK |  | Empresa |
| codi_sai | integer(4) | PK |  | Saida |
| qtde_msp | numeric(13) |  |  | Quantidade |
| bcal_msp | numeric(13) |  |  | Base de Calculo do IPI |
| vipi_msp | numeric(13) |  |  | Valor do IPI |
| nume_msp | integer(4) | PK |  | Sequencial |
| orig_msp | tinyint(1) |  |  | Origem (1 - Nota/2 - Extra) |
| data_msp | date(4) |  | S | Data |
| vsai_msp | numeric(16) |  | S | Valor total da saida pelo custo medio |
| cst_msp | integer(4) |  | S | Codigo da Stituacao Tributaria |
| vpro_msp | numeric(13) |  | S | Valor do Produto |
| vdes_msp | numeric(13) |  | S | Valor do Desconto |
| bicms_msp | numeric(13) |  | S | Base do ICMS |
| bicmsst_msp | numeric(13) |  | S | Base do ICMS para Substituicao Tributaria |
| aliicms_msp | numeric(13) |  | S | Aliquota do ICMS |
| chassi_msp | varchar(17) |  | S | Codigo do Chassi do veiculo |
| incentivado_msp | char(1) |  | S | Produto incentivado (S/N) - PE |
| apuracao_msp | integer(4) |  | S | Codigo da Apuracao - PE |
| situacao_msp | char(4) |  | S | Situacao Tributada do produto qto ao ECF - SE |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| vfre_msp | numeric(13) |  | S | Valor do frete |
| vseg_msp | numeric(13) |  | S | Valor do seguro |
| vdesace_msp | numeric(13) |  | S | Valor das despesas acessorias |
| qtd_gasolinaa_msp | numeric(13) |  | S | Quantidade de Gasolina A |
| valor_icms_msp | numeric(13) |  | S | Valor do ICMS |
| valor_subtri_msp | numeric(13) |  | S | Valor do SUBTRI |
| isentas_ipi_msp | numeric(13) |  | S | Valor de isentas IPI |
| outras_ipi_msp | numeric(13) |  | S | Valor de outras IPI |
| valor_unit_msp | numeric(15) |  | S | Valor unitario |
| aliq_st_msp | numeric(5) |  | S | Aliquota da Substituicao tributaria |
| codigo_trib_msp | tinyint(1) |  | S | Codigo de tributacao |
| aliq_ipi_msp | numeric(5) |  | S | Aliquota de IPI |
| bc_issqn_msp | numeric(13) |  | S | Base de calculo ISSQN |
| aliq_issqn_msp | numeric(5) |  | S | Aliquota de ISSQN |
| valor_issqn_msp | numeric(13) |  | S | Valor ISSQN |
| lote_medic_msp | varchar(255) |  | S | Lote do medicamento |
| validade_msp | date(4) |  | S | Data de validade |
| referencia_bc_msp | tinyint(1) |  | S | REFERENCIA BASE DE CALCULO (0=TABELADO/1=NEGATIVA/2=POSITIVA/3=NEUTRA/4=MARGEM VALOR AGREGADO/5=PAUTA/6=VALOR DA OPERAÇÃO) |
| valor_tab_max_msp | numeric(13) |  | S | Valor tabelado/maximo |
| nro_serie_arma_msp | varchar(255) |  | S | Numero de serie da arma |
| nro_serie_cano_msp | varchar(255) |  | S | Numero de serie do cano |
| operacao_veiculo_msp | tinyint(1) |  | S | Tipo de operacao com veiculo(0=Concessionaria/1=Faturamento/2=Venda direta/9=Outras) |
| qtde_cancelada_msp | numeric(15) |  | S | Quantidade cancelada |
| valor_cancel_msp | numeric(13) |  | S | Valor do cancelamento |
| isentas_icms_msp | numeric(13) |  | S | Isentas de ICMS |
| nao_incidencia_icms_msp | numeric(13) |  | S | Nao incidencia de ICMS |
| adquirido_st_msp | numeric(13) |  | S | Valor acumulado adquirido com ST |
| cfop_msp | integer(4) |  | S | CFOP |
| fabricacao_msp | date(4) |  | S | Data de fabricacao do medicamento |
| serie_ecf_msp | char(20) |  | S | Serie de fabricacao do ECF |
| cst_pis_msp | integer(4) |  | S | CST do PIS |
| bc_pis_msp | numeric(13) |  | S | Base de calculo do PIS |
| aliq_pis_msp | numeric(7) |  | S | Aliquota do PIS |
| valor_pis_msp | numeric(13) |  | S | Valor do PIS |
| cst_cofins_msp | integer(4) |  | S | CST do COFINS |
| bc_cofins_msp | numeric(13) |  | S | Base de calculo do COFINS |
| aliq_cofins_msp | numeric(7) |  | S | Aliquota do COFINS |
| valor_cofins_msp | numeric(13) |  | S | Valor do COFINS |
| qtde_item_lote_msp | integer(4) |  | S | Quantidade de item por lote de medicamento |
| enquadramento_ipi_msp | char(3) |  | S | Enquadramento do IPI |
| CST_ISSQN_MSP | integer(4) |  | S | CST do ISSQN |
| ISENTAS_ISSQN_MSP | numeric(13) |  | S | Isentas de ISS |
| NAO_INCIDENCIA_ISSQN_MSP | numeric(13) |  | S | Não incidência de ISS |
| MOVIMENTACAO_FISICA_MSP | char(1) |  |  | Movimentação física de produto (S/N) |
| CODIGO_UNIDADE | integer(4) |  | S | Código da unidade |
| UNIDADE | char(6) |  | S | Unidade comercializada |
| COMPLEMENTO_CFOP_CAT_17_99 | integer(4) |  | S | Complemento da CFOP - Portaria Cat nº 17/99 |
| CODI_ENT_DEVOLVIDA | integer(4) |  | S | Código da nota de entrada devolvida |
| I_BICO | integer(4) |  | S | Bico do combustível |
| VALOR_CONTABIL_MSP | numeric(13) |  | S | Valor contabil produto |
| QTDE_TRIBUTARIA_MEDIDA_PIS_MSP | numeric(13) |  | S | Quantidade tributada PIS por unidade de medida |
| VALOR_UNIDADE_MEDIDA_PIS_MSP | numeric(13) |  | S | Valor unidade PIS por unidade de medida |
| VALOR_MEDIDA_PIS_MSP | numeric(13) |  | S | Valor PIS por unidade de medida |
| QTDE_TRIBUTARIA_MEDIDA_COFINS_MSP | numeric(13) |  | S | Quantidade tributada COFINS por unidade de medida |
| VALOR_UNIDADE_MEDIDA_COFINS_MSP | numeric(13) |  | S | Valor unidade COFINS por unidade de medida |
| VALOR_MEDIDA_COFINS_MSP | numeric(13) |  | S | Valor COFINS por unidade de medida |
| DADOS_PISCOFINS_OK | char(1) |  |  | Dados referente ao PIS/COFINS OK (S/N) |
| MOTIVO_CFEM_MSP | char(1) |  | S | Motivo CFEM (T - Transformação/C - Consumo/U - Utilização) apenas para saídas extras (V - Venda) apenas para notas de saída |
| COMBUSTIVEL_OPERACAO_MSP | integer(4) |  | S | Operação |
| COMBUSTIVEL_MODAL_MSP | integer(4) |  | S | Modal |
| COMBUSTIVEL_CODIGO_VEICULO_MSP | varchar(7) |  |  | Código Veículo |
| COMBUSTIVEL_SERVICO_MSP | integer(4) |  | S | Serviço |
| DESCRICAO_COMPLEMENTAR_MSP | varchar(255) |  | S | Descrição complementar |
| NATUREZA_RECEITA_PIS_MSP | integer(4) |  | S | Natureza da receita do PIS |
| NATUREZA_RECEITA_COFINS_MSP | integer(4) |  | S | Natureza da receita do COFINS |
| EXCLUSAO_COOPERATIVA_MSP | numeric(13) |  | S | Exclusão cooperativa |
| CST_PIS_DEVOLVIDA_MSP | integer(4) |  | S | CST do PIS da nota devolvida |
| CST_COFINS_DEVOLVIDA_MSP | integer(4) |  | S | CST do COFINS da nota devolvida |
| BASE_CALCULO_FRETE_PIS | numeric(13) |  |  | Base de Cálculo Frete - PIS |
| VALOR_FRETE_PIS | numeric(13) |  |  | Valor Frete - PIS |
| BASE_CALCULO_SEGURO_PIS | numeric(13) |  |  | Base de Cálculo Seguro - PIS |
| VALOR_SEGURO_PIS | numeric(13) |  |  | Valor Seguro - PIS |
| BASE_CALCULO_DESPESA_ACESSORIA_PIS | numeric(13) |  |  | Base de Cálculo Despesas Acessórias - PIS |
| VALOR_DESPESA_ACESSORIA_PIS | numeric(13) |  |  | Valor Despesas Acessórias - PIS |
| BASE_CALCULO_FRETE_COFINS | numeric(13) |  |  | Base de Cálculo Frete - COFINS |
| VALOR_FRETE_COFINS | numeric(13) |  |  | Valor Frete - COFINS |
| BASE_CALCULO_SEGURO_COFINS | numeric(13) |  |  | Base de Cálculo Seguro - COFINS |
| VALOR_SEGURO_COFINS | numeric(13) |  |  | Valor Seguro - COFINS |
| BASE_CALCULO_DESPESA_ACESSORIA_COFINS | numeric(13) |  |  | Base de Cálculo Despesas Acessórias - COFINS |
| VALOR_DESPESA_ACESSORIA_COFINS | numeric(13) |  |  | Valor Despesas Acessórias - COFINS |
| VINCULO_CREDITO_PIS_DEVOLVIDA_MSP | tinyint(1) |  | S | Vínculo do crédito do PIS da nota devolvida |
| VINCULO_CREDITO_COFINS_DEVOLVIDA_MSP | tinyint(1) |  | S | Vínculo do crédito do COFINS da nota devolvida |
| DATA_NOTA_DEVOLVIDA_MSP | date(4) |  | S | Data da nota devolvida |
| I_CST_VIGENCIA_ICMS | integer(4) |  | S | Código sequencial do CST de ICMS |
| I_TANQUE | integer(4) |  | S | Tanque do combustível |
| ICMS_ST_VALOR_RESSARCIDO | numeric(13) |  |  | ICMS Substituição Tributária - Valor Ressarcido |
| ICMS_VALOR_RESSARCIDO | numeric(13) |  |  | ICMS - Valor Ressarcido |
| CODIGO_IMPOSTO_IPI | integer(4) |  |  | Código do Imposto IPI |
| I_CLASSE_ENQUADRAMENTO_IPI | integer(4) |  | S | Classe do Enquadramento IPI |
| UNIDADE_MEDIDA_QUANTIDADE_TRIBUTADA_IPI | numeric(13) |  |  | Unidade de Medida Quantidade Tributada IPI |
| UNIDADE_MEDIDA_VALOR_POR_UNIDADE_IPI | numeric(13) |  |  | Unidade de Medida Valor por Unidade IPI |
| UNIDADE_MEDIDA_VALOR_IMPOSTO_IPI | numeric(13) |  |  | Unidade de Medida Valor do Imposto IPI |
| PERCENTUAL_REDUCAO_BC_PIS_MSP | numeric(5) |  |  | Percentual Redução Base Cálculo PIS |
| PERCENTUAL_REDUCAO_BC_COFINS_MSP | numeric(5) |  |  | Percentual Redução Base Cálculo COFINS |
| I_RECOLHIMENTO_IPI | integer(4) |  | S | Sequencial do Código de Recolhimento do IPI |
| CODIGO_RECOLHIMENTO_IPI | char(6) |  | S | Código de Recolhimento do IPI |
| CUSTO_MEDIO_REMESSA_MSP | numeric(16) |  |  | Custo médio da Nota de Remessa |
| I_RECOLHIMENTO_PIS_DEVOLVIDO | integer(4) |  | S | Código Sequencial do Recolhimento do PIS Nota Devolvida |
| CODIGO_RECOLHIMENTO_PIS_DEVOLVIDO | char(6) |  |  | Código do Recolhimento do PIS Nota Devolvida |
| I_RECOLHIMENTO_COFINS_DEVOLVIDO | integer(4) |  | S | Código Sequencial do Recolhimento do COFINS Nota Devolvida |
| CODIGO_RECOLHIMENTO_COFINS_DEVOLVIDO | char(6) |  |  | Código do Recolhimento do COFINS Nota Devolvida |
| I_RECOLHIMENTO_PIS | integer(4) |  | S | Código Sequencial do Recolhimento do PIS |
| CODIGO_RECOLHIMENTO_PIS | char(6) |  |  | Código do Recolhimento do PIS |
| I_RECOLHIMENTO_COFINS | integer(4) |  | S | Código Sequencial do Recolhimento do COFINS |
| CODIGO_RECOLHIMENTO_COFINS | char(6) |  |  | Código do Recolhimento do COFINS |
| CODIGO_CEST | char(7) |  | S | Código CEST |
| MEDICAMENTO_INFORMAR_MAIS_DE_UM_LOTE | char(1) |  |  | Medicamentos - Informar mais de um lote (S/N) |
| PRECO_FOB | numeric(13) |  |  | Preço FOB |
| PR_I_SEQUENCIAL_BENEFICIO | integer(4) |  | S | Sequencial do Código do Benefício |
| RJ_I_SEQUENCIAL_BENEFICIO | integer(4) |  | S | Sequencial do Código do Benefício RJ |
| SEQUENCIAL_ITEM | integer(4) |  | S | Sequencial Item |
| DF_I_SEQUENCIAL_BENEFICIO | integer(4) |  | S | Sequencial do Código do Benefício DF |
| BOLETIM_CONFORMIDADE | varchar(10) |  | S | Boletim de Conformidade |
| SC_I_SEQUENCIAL_BENEFICIO | integer(4) |  | S | Sequencial do Código do Benefício |
| VALOR_ICMS_PROPRIO_DIFERIDO | numeric(13) |  |  | ICMS Diferido |
| VALOR_ISSRET_MSP | numeric(13) |  | S | Valor ISS Retido |
| VALOR_ICMS_ST_DESONERADO | numeric(13) |  |  | Valor do ICMS ST Desonerado |
| I_MOTIVO_DESONERACAO_ICMS_ST | integer(4) |  | S | Motivo da Desoneração do ICMS ST |
| ES_I_SEQUENCIAL_BENEFICIO | integer(4) |  | S | Sequencial do Código do Benefício |
| SP_I_SEQUENCIAL_BENEFICIO | integer(4) |  | S | Sequencial do codigo do beneficio SP |
| GO_I_SEQUENCIAL_BENEFICIO | integer(4) |  | S | Sequencial do codigo do beneficio GO |
