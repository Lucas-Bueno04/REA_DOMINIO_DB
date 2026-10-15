# efprodutos — Produtos - Cadastro
221.153 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_pdi | char(14) | PK |  | Codigo |
| codi_emp | integer(4) | PK |  | Empresa |
| codi_gru | integer(4) |  |  | Grupo |
| cnbm_pdi | char(10) |  | S | NBM |
| desc_pdi | char(255) |  |  | Descricao |
| unid_pdi | char(6) |  | S | Unidade de medida |
| vuni_pdi | numeric(15) |  | S | Valor unitario |
| qtin_pdi | numeric(13) |  | S | Quantidade inicial |
| qtfi_pdi | numeric(13) |  | S | Quantidade final |
| vlin_pdi | numeric(13) |  | S | Valor inicial |
| vlfi_pdi | numeric(13) |  | S | Valor final |
| aipi_pdi | numeric(5) |  | S | Aliquota do IPI |
| obse_pdi | char(40) |  | S | Observacao para ser impressa no Livro de Inventario |
| cncm_pdi | char(8) |  | S | Nomenclatura Comum do Mercosul |
| especie_pdi | integer(4) |  | S | Especie - DNF |
| un_padrao_pdi | integer(4) |  | S | Unidade padrao - DNF |
| fator_pdi | numeric(14) |  | S | Fator de conversao |
| dnf_pdi | char(1) |  | S | Codigo DNF |
| cst_pdi | integer(4) |  | S | Codigo da Situacao Tributaria |
| veiculonovo_pdi | char(1) |  | S | Operacoes com veiculos automotores novos (S/N) |
| chassi_pdi | varchar(17) |  | S | Codigo do Chassi do veiculo |
| ean_pdi | varchar(14) |  | S | Codigo EAN/Codigo de Barras - SE |
| relevante_pdi | integer(4) |  | S | Codigo do produto relevante/mapa fisiologico - SE |
| codpro_dnf_pdi | integer(4) |  | S | Codigo do Produto conforme indicado nos Anexos I ou II da DNF |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| capacidade_pdi | integer(4) |  | S | Capacidade volumetrica(ml) |
| incentivo_pdi | char(1) |  | S | Possui incentivo fiscal (S/N) - MS |
| spgrfcbt_pdi | char(1) |  | S | SP: Gera informações para GRF-CBT |
| codigo_spp | integer(4) |  | S | SP: Codigo do produto conforme tabela SEFAZ |
| gera_scanc_pdi | char(1) |  | S | Gera informacoes para o Scanc-CTB (S=Sim/N=Nao) |
| cod_scanc_pdi | integer(4) |  | S | Codigo do produto SCANC |
| possue_gasa_pdi | char(1) |  | S | Possui gasolina A (S=Sim/N=Nao) |
| tipo_scanc_pdi | char(3) |  | S | Tipo Produto SCANC |
| unidadece_pdi | char(2) |  | S | Unidade |
| tipoce_pdi | tinyint(1) |  | S | Unidade |
| gera88st_pdi | char(1) |  | S | Gera informacoes registro 88ST Sintegra (S/N) |
| codigosefaz_pdi | integer(4) |  | S | Codigo do produto na tabela SEFAZ |
| aicms_pdi | numeric(5) |  | S | Aliquota do ICMS |
| tipo_pdi | char(1) |  | S | Tipo(V=Veíc. Novos/M=Medicamentos/A=Armas Fogo/O=Outros/C=Combustíveis/U=Comunicação/E=Energ. Elétr./S=Veíc. Usados) |
| tipo_arma_pdi | tinyint(1) |  | S | Tipo da arma (0=Permitido/1=Restrito) |
| descricao_arma_pdi | varchar(255) |  | S | Descricao completa da arma |
| genero_pdi | tinyint(1) |  | S | Codigo do genero |
| servico_pdi | integer(4) |  | S | Codigo do servico |
| classificacao_pdi | integer(4) |  | S | Classificacao do servico |
| tipo_item_pdi | tinyint(1) |  | S | Tipo do item (0=Mercadoria/1=Materia Prima/2=Produto Intermediario/3=Produto em Fabricacao/4=Produto Acabado/5=Embalagem/9=Serviços/10=Outros insumos/99=Outros) |
| ncm_exterior_pdi | tinyint(1) |  | S | Codigo NCM Exterior |
| imposto_exterior_pdi | tinyint(1) |  | S | Codigo Imposto Importacao |
| produto_composto_pdi | char(1) |  | S | Produto composto (S/N) |
| info_ipm_dpi_pdi | char(1) |  | S | Informacoes complementares do IPM da PDI (S/N) |
| codigo_ipm_dpi_pdi | tinyint(1) |  | S | Codigo produto/servico do IPM da DPI |
| cesta_basica_pdi | char(1) |  | S | Faz parte da cesta basica |
| codigo_dam_am | integer(4) |  | S | Codigo do produto DAM - AM |
| anexo7_cte_pdi | char(1) |  | S | Produto relacionado na Posicao 3301 a 3307 do Anexo VII do CTE (S/N) |
| tipo_pe_pdi | tinyint(1) |  | S | Tipo de produto SEF-PE(1-Mercadorias/2-Materias-primas/3-Produtos intermediarios/4-Materiais de embalagem/5-Produtos manufaturados/6-Produtos em fabricação) |
| codigo_barras_pdi | char(16) |  | S | Codigo de barras |
| tipo_medicamento_pdi | tinyint(1) |  | S | Tipo de medicamento (0 - Similar/1 - Generico/2 - Etico ou de marca) |
| incluido_subtri_pdi | char(1) |  | S | Produto incluido no campo da Substituicao Tributaria (S/N) |
| data_inicio_subtri_pdi | date(4) |  | S | Data de Inicio da Substituicao tributaria |
| data_levan_estoque_pdi | date(4) |  | S | Data do levantamento dos estoques |
| preco_tabelado_pdi | char(1) |  | S | Produto com Preco Tabelado (S/N) |
| valor_unit_subtri_pdi | numeric(13) |  | S | Valor Unitario da Substituicao Tributaria |
| mva_subtri_pdi | numeric(7) |  | S | MVA da Substituicao Tributaria |
| grupo_subtri_pdi | tinyint(1) |  | S | Grupo da Substituição Tributária |
| equipamento_ecf_pdi | char(1) |  | S | Equipamento de ECF(S/N) |
| tributado_issqn_pdi | char(1) |  | S | Servico tributado pelo ISSQN (S/N) |
| codigo_unidade | integer(4) |  | S | Codigo da unidade |
| ex_tipi_pdi | char(3) |  | S | EX TIPI |
| pdic_ipi_pdi | char(1) |  | S | Periodicidade do IPI (D - decendial/M - Mensal) |
| classificacao_spedf_pdi | integer(4) |  | S | Classificacao de Itens de Energia Eletrica, Servicos de Comunicacao e Telecomunicacao |
| PRODUTO_REGIME_ESPECIAL_DF | integer(4) |  | S | Produto sujeito ao Regime Especial de Apuração - REA/ICMS(Decreto 29.179/2008) |
| ITEM_PADRAO_PRODUTO_REGIME_ESPECIAL_DF | integer(4) |  | S | Item padrão referente ao produto sujeito ao Regime Especial de Apuração - REA/ICMS(Decreto 29.179/2008) |
| CODI_CTA_IND_PROP_0 | integer(4) |  | S | Conta contábil(Do informante em seu poder) |
| CODI_CTA_IND_PROP_1 | integer(4) |  | S | Conta contábil(Do informante em posse de terceiros) |
| CODI_CTA_IND_PROP_2 | integer(4) |  | S | Conta contábil(De terceiros em posse do informante) |
| UNIDADE_DIFERENTE | char(1) |  |  | Unidade inventariada diferente da comercializada(S/N) |
| TIPO_RECEITA_SPED_PDI | char(1) |  | S | Tipo de receita(0-Receita Própria/1-Receita Terceiros) |
| RESSARCIMENTO_COMPLEMENTO_CAT_17_99_PDI | char(1) |  | S | Controlar ressarcimento ou complemento - Portaria CAT nº 17/99 (S/N) |
| SALDO_INICIAL_CAT_17_99_PDI | date(4) |  | S | Data do Saldo Inicial para o controle da Portaria CAT nº 17/99 |
| VALOR_UNITARIO_CAT_17_99_PDI | numeric(15) |  | S | Valor unitário para o controle da Portaria CAT nº 17/99 |
| QUANTIDADE_CAT_17_99_PDI | numeric(13) |  | S | Quantidade para o controle da Portaria CAT nº 17/99 |
| VALOR_TOTAL_CAT_17_99_PDI | numeric(13) |  | S | Valor final para o controle da Portaria CAT nº 17/99 |
| CADASTRO_PDI | date(4) |  | S | Data do cadastro do produto |
| ESCRITURADO_LMC_PDI | char(1) |  | S | Produto escriturado no LMC(S/N) |
| CODIGO_COMBUSTIVEL_DF | char(4) |  | S | Código do combustível conforme tabela do DF |
| CODIGO_COMBUSTIVEL_ANP | char(9) |  | S | Código do combustível conforme tabela da ANP |
| CFEM_PDI | char(1) |  |  | Produto Tributado pelo CFEM(S/N) |
| REGIME_LAVRA_GARIMPEIRA_PDI | char(1) |  |  | Extraída sob o Regime de Permissão de Lavra Garimpeira (S/N) |
| PROCESSO_DNPM_PDI | numeric(11) |  |  | Número do processo no DNPM |
| ALIQUOTA_CFEM_PDI | numeric(5) |  |  | Alíquota do CFEM |
| CODIGO_SPED_PDI | char(60) |  | S | Código do produto para o SPED Fiscal e SPED PIS/COFINS |
| PB_GERA_GIM_PDI | char(1) |  |  | PB - Gera informações para a GIM (S/N) |
| PB_CODIGO_PRODUTO_GIM_PDI | integer(4) |  | S | PB - Código do produto na GIM |
| GRUPO_SUBTRI_SP_PDI | integer(4) |  | S | Grupo da Substituição Tributária - SP |
| SIMP_PDI | char(1) |  |  | Exportar para o arquivo I-SIMP |
| SIMP_FATOR_CONVERSAO_UNIDADE_PDI | numeric(15) |  |  | Fator de Conversão p/ Un.Med.ANP |
| SIMP_FATOR_CONVERSAO_20_C_PDI | numeric(15) |  |  | Fator de Correção p/ 20C° |
| SIMP_MASSA_ESPECIFICA_PDI | numeric(7) |  |  | Massa Específica |
| SIMP_RECIPIENTE_GLP_PDI | integer(4) |  | S | Recipiente do GLP |
| PERMITE_INFORMAR_DESCRICAO_COMPLEMENTAR_PDI | char(1) |  |  | Permitir informar a descrição complementar no lançamento das notas |
| INSS_FOLHA_PRODUTO_RELACIONADO_PDI | char(1) |  |  | Produto relacionado nos Arts. 7º e 8º da Lei 12.546/2011 |
| I_ATIVIDADE_INSS_FOLHA_PDI | char(8) |  | S | Código da Atividade do produto relacionado nos Arts. 7º e 8º da Lei 12.546/2011 |
| DACON_TIPO_PRODUTO | integer(4) |  | S | Tipo produto - DACON |
| DACON_CALCULADO_SOBRE | integer(4) |  |  | Calculado sobre - DACON |
| RJ_CALCULAR_FECP_ICMS_NORMAL | char(1) |  |  | Calcular FECP-ICMS Normal |
| SC_GERAR_CREDITO_PRESUMIDO_DERIVADO_LEITE | char(1) |  |  | Gera Crédito Presumido - RICMS, Anexo 2, Art. 15, XIV |
| SC_GERAR_CREDITO_PRESUMIDO_DERIVADO_LEITE_TIPO | integer(4) |  |  | Gera Crédito Presumido - RICMS, Anexo 2, Art. 15, XIV - Tipo do produto |
| DF_PRODUTO_SUJEITO_ADICIONAL_FUNDO_POBREZA | char(1) |  |  | Produto sujeito ao adicional na alíquota do imposto - Fundo de Combate a Pobreza |
| RS_PARTICIPA_BASE_CALCULO_FUNDESA | char(1) |  |  | Produto faz parte da base de cálculo do FUNDESA |
| RS_PARTICIPA_BASE_CALCULO_FUNDESA_TABELA | integer(4) |  | S | Produto faz parte da base de cálculo do FUNDESA - Tipo do Produto |
| RS_PARTICIPA_BASE_CALCULO_FUNDESA_INCIDENCIA | integer(4) |  |  | Produto faz parte da base de cálculo do FUNDESA - Incidência |
| IMPORTACOES_RZ_INFORMAR_CFOP_SIT_TRIB | char(1) |  |  | Informar o CFOP para relacionar com situação tributária |
| IMPORTACOES_RZ_CFOP_SIT_TRIB | integer(4) |  | S | CFOP para relacionar com situação tributária |
| IMPORTACOES_RZ_CFOP_VERSAO_SIT_TRIB | smallint(2) |  | S | Versão CFOP para relacionar com situação tributária |
| I_SEQUENCIAL_CST | integer(4) |  | S | Codigo da Situacao Tributaria |
| IMPORTACOES_CFOPS_RELACIONAR | char(1) |  |  | Relacionar os CFOPs a serem utilizados na importação de notas de entrada |
| ALIQUOTA_INTERNA | numeric(5) |  |  | Aliquota interna |
| MT_PRODUTO_FETHAB | char(1) |  |  | MT - Produto faz parte da base de cálculo no FETHAB |
| MT_CODIGO_RECOLHIMENTO_FETHAB | char(6) |  | S | MT - Código de Recolhimento do Imposto FETHAB |
| MT_RESPONSAVEL_RECOLHIMENTO | tinyint(1) |  | S | MT - Responsável pelo Recolhimento do Imposto FETHAB (1 - Cliente / 2 - Empresa) |
| SC_GERAR_CREDITO_PRESUMIDO | char(1) |  |  | SC - Gerar Crédito Presumido |
| SC_TIPO_CREDITO_PRESUMIDO | integer(4) |  | S | SC - Tipo de Crédito Presumido |
| SC_TIPO_PRODUTO | integer(4) |  | S | SC - Tipo do Produto |
| RO_PRODUTO_POSSUI_INCENTIVO_CONSIT | char(1) |  |  | RO - Produto possui incentivo tributário CONSIT - Decreto n 12.988/2007, art. 2, I |
| BA_GERAR_PRODUTO_DMD | char(1) |  |  | Gerar produto no informativo DMD - ICMS Diferido |
| BA_I_DMD | integer(4) |  | S | Código na DMD |
| BA_NUMERO_HABILITACAO | varchar(12) |  |  | Número da Habilitação |
| BA_MADEIRA_EM_PE | char(1) |  |  | Madeira em pé (Floresta) |
| BA_UNIDADE_INVENTARIADA_DIFERENTE_DMD | char(1) |  |  | Unidade inventariada diferente da unidade de medida informada no DMD |
| RS_CREDITO_ARROZ_PDI | char(1) |  |  | RS - Gera crédito presumido nas saídas interestaduais de arroz beneficiado |
| RS_CREDITO_ARROZ_PDI_TIPO | tinyint(1) |  | S | RS - Tipo do produto (1 - Arroz em casca / 2 - Arroz beneficiado) |
| RS_CREDITO_ARROZ_PDI_UNIDADE | char(1) |  |  | RS - Unidade inventariada diferente da unidade de cálculo (kg) |
| RS_CREDITO_ARROZ_PDI_UNIDADE_CALCULO | integer(4) |  | S | RS - Unidade de cálculo |
| RS_CREDITO_ARROZ_PDI_FATOR_CONVERSAO | numeric(13) |  |  | RS - Fator de conversão |
| PRODUTO_CUSTO_IMPORTADOS_DENTRO_LIMITE | char(1) |  |  | Produto possui custo de insumos importados dentro do limite previsto no Art. 2°, §3°, do Decreto n° 7.633/2011 |
| EXCLUIDO_SUBTRI_PDI | char(1) |  | S | Produto Excluído da Substituição Tributária |
| DATA_INICIO_EXCLUIDO_SUBTRI_PDI | date(4) |  | S | Data Final - Excluído da Substituição Tributária |
| DATA_LEVAN_ESTOQUE_EXCLUIDO_SUBTRI_PDI | date(4) |  | S | Data do Levamentamento dos Estoques - Excluído da Substituição Tributária |
| MVA_EXCLUIDO_SUBTRI_PDI | numeric(7) |  |  | Percentual IVA(%) - Excluído da Substituição Tributária |
| RJ_PRODUTO_INDUSTRIAL_FLUMINENSE_PDI | char(1) |  |  | RJ - Produto é industrializado no estabelecimento Fluminense - Art. 2º Decreto 42.649/2010 |
| CODI_PDI_BANCO | char(14) |  |  | Código do produto sem acentos com UpperCase |
| DESC_PDI_BANCO | char(255) |  |  | Descrição do produto sem acentos com UpperCase |
| BA_FUNCEP_CALCULAR_ALIQ_ICMS | char(1) |  |  | BA - FUNCEP - Calcular o adicional na alíquota do imposto ICMS (S/N) |
| AL_TIPO_COMBUSTIVEL_DAC | char(1) |  |  | AL - Tipo de combustível no informativo DAC |
| AL_TIPO_COMBUSTIVEL_DAC_CODIGO | integer(4) |  | S | AL - Tipo de combustível no informativo DAC - Código |
| PLACA_PDI | varchar(7) |  |  | Placa |
| VEICULO_ESTOQUE_SALDO | tinyint(1) |  | S | Saldo do Estoque de Produto Tipo Veículos Usados (0-Sem / 1-Com) |
| SC_CREDITO_PRESUMIDO_ENTRADA_LEITE_PDI | char(1) |  |  | SC - Calcular Crédito Presumido na entrada de leite in natura (S/N) |
| SC_CREDITO_PRESUMIDO_ENTRADA_LEITE_TIPO_PDI | integer(4) |  |  | SC - Calcular Crédito Presumido na entrada de leite in natura - Tipo do Produto (1/2/3) |
| TO_TIPO_COMBUSTIVEL_GIAM_CODIGO | integer(4) |  | S | TO - Tipo de combustível no informativo GIAM - Código |
| PRECO_VENDA_SUBTRI_PDI | numeric(13) |  |  | RJ - Preço de venda |
| RJ_GERAR_CREDITO_PRESUMIDO | char(1) |  |  | RJ - Gerar Crédito Presumido |
| RJ_TIPO_CREDITO_PRESUMIDO | integer(4) |  | S | RJ - Tipo de Crédito Presumido |
| I_TIPO_SERVICO | integer(4) |  | S | Sequencial do Tipo de Serviço - e_Social |
| AM_GERAR_PRODUTO_DIA | char(1) |  |  | AM - Gerar produto na DIA (S/N) |
| AM_DECLARAR_PRODUTO_MATRIZ_NACIONAL | char(1) |  |  | AM -  Declarar produto no arquivo Matriz Nacional (S/N) |
| AM_DECLARAR_PRODUTO_MATRIZ_NACIONAL_CODIGO | integer(4) |  | S | AM - Código de tributação do produto |
| AM_PRODUTO_UTILIZADO_COMO_INSUMO | char(1) |  |  | AM - Produto utilizado como insumo (S/N) |
| AM_PRODUTO_UTILIZADO_COMO_INSUMO_CODIGO | char(14) |  | S | AM - Código do produto acabado |
| MG_GERAR_CREDITO_PRESUMIDO | char(1) |  |  | MG - Gerar Crédito Presumido (S/N) |
| MG_TIPO_CREDITO_PRESUMIDO | integer(4) |  | S | MG - Tipo de Crédito Presumido |
| MG_TIPO_PRODUTO | integer(4) |  | S | MG - Tipo do Produto |
| MG_CALCULAR_FEM_ADICIONAL_ALIQ_IMP_ICMS | char(1) |  |  | MG - FEM - Calcular o adicional na alíquota do imposto ICMS (S/N) |
| RS_GERAR_CREDITO_PRESUMIDO | char(1) |  |  | RS - Gerar Crédito Presumido (S/N) |
| RS_TIPO_CREDITO_PRESUMIDO | integer(4) |  | S | RS - Tipo de Crédito Presumido |
| PA_GERA_COMBUSTIVEL_DIEF | char(1) |  |  | PA - Gera combustível na DIEF (S/N) |
| PA_CODIGO_COMBUSTIVEL_DIEF | integer(4) |  | S | PA - Código do combustível na DIEF |
| SC_CALCULAR_CREDITO_PRESUMIDO_SAIDA_INTERESTADUAL | char(1) |  |  | SC - Calcular o crédito presumido somente nas saídas interestaduais (S/N) |
| AL_PRODUTO_QUADRO_III_DAC | char(1) |  |  | AL - Produto relacionado para gerar no quadro III do informativo DAC (Agropecuário) |
| AL_PRODUTO_QUADRO_III_DAC_TIPO | integer(4) |  |  | AL - Produto relacionado para gerar no quadro III do informativo DAC (Agropecuário) - Tipo |
| VEICULO_MARCA | integer(4) |  | S | Marca do veículo |
| VEICULO_MODELO | varchar(255) |  |  | Modelo do veículo |
| VEICULO_ANO_FABRICACAO | integer(4) |  |  | Ano de fabricação do veículo |
| VEICULO_ANO_MODELO | integer(4) |  |  | Ano do modelo do veículo |
| VEICULO_CHASSI | varchar(17) |  |  | Chassi do veículo |
| VEICULO_RENAVAM | varchar(11) |  |  | Renavam do veículo |
| VEICULO_COR | varchar(255) |  |  | Cor do veículo |
| VEICULO_CATEGORIA | integer(4) |  | S | Categoria do veículo (1-Oficial \ 2-De representação diplomática ou outros orgões do Governo \ 3-Particular \ 4-Aluguel \ 5-Aprendizagem) |
| VEICULO_ESPECIE | integer(4) |  | S | Espécie do veículo (1-Passageiros \ 2-Carga \ 3-Misto \ 4-Competição \ 5-Tração \ 6-Especial \ 7-Coleção) |
| RS_PRODUTO_AGROTOXICO_FITOSSANITARIO | char(1) |  |  | RS - Produto agrotóxico fitossanitário |
| RS_PRODUTO_AGROTOXICO_NOME_INGREDIENTE_ATIVO | varchar(35) |  |  | RS - Nome ingrediente ativo do produto agrotóxico fitossanitário |
| RS_PRODUTO_AGROTOXICO_FORMULACAO | varchar(120) |  |  | RS - Formulação do produto agrotóxico fitossanitário |
| RS_PRODUTO_AGROTOXICO_CLASSE | varchar(65) |  |  | RS - Classe do produto agrotóxico fitossanitário |
| RS_PRODUTO_AGROTOXICO_CONCENTRACAO | varchar(10) |  |  | RS - Concentração do produto agrotóxico fitossanitário |
| CT_CONTROLE_ESTOQUE_EM_PROCESSO | integer(4) |  | S | Conta contábil - Controle da produção e do estoque - Em processo |
| HT_CONTROLE_ESTOQUE_EM_PROCESSO | integer(4) |  | S | Histórico - Controle da produção e do estoque - Em processo |
| CT_CONTROLE_ESTOQUE_ACABADO | integer(4) |  | S | Conta contábil - Controle da produção e do estoque - Em acabado |
| HT_CONTROLE_ESTOQUE_ACABADO | integer(4) |  | S | Histórico - Controle da produção e do estoque - Em acabado |
| CODIGO_CEST | char(7) |  | S | Código CEST |
| SC_CALCULAR_CREDITO_PRESUMIDO_SOBRE | char(1) |  |  | Calcular o Crédito Presumido sobre |
| REGISTRO_EXPORTACAO | numeric(12) |  | S | Registro de Exportação(RE) |
| SC_CREDITO_PRESUMIDO_ENTRADA_LEITE_QUEIJO_PRATO_MOZARELA | char(1) |  |  | Considerar as saídas para fora do estado do queijo prato e mozarela no cálculo da proporção das saídas tributadas |
| SC_PRODUTO_AUTORIZADO_MANUTENCAO_CREDITO | char(1) |  | S | Produto não autorizado a manutenção de créditos acumulados |
| SC_CALCULAR_CREDITO_PRESUMIDO_ART_15_XXVIII_SAIDA_INTERESTADUAL | char(1) |  |  | Calcular o crédito presumido Art. 15, XXVIII nas saídas interestaduais |
| GUID_CONTABIL | uniqueidentifier(16) |  | S | Identificador Único do registro no banco do Contábil |
| GUID_ONVIO | uniqueidentifier(16) |  | S | Identificador Único do registro no banco do Atendimento Onvio |
| RESSARCIMENTO_COMPLEMENTO_CAT_42_18 | char(1) |  |  | Controlar ressarcimento ou complemento - Portaria CAT nº 42/18 |
| SALDO_INICIAL_CAT_42_18 | date(4) |  | S | Saldo Inicial CAT |
| QUANTIDADE_CAT_42_18 | numeric(13) |  |  | Quantidade CAT |
| ICMS_PROPRIO_CAT_42_18 | numeric(13) |  |  | ICMS Próprio CAT |
| ICMS_ST_CAT_42_18 | numeric(13) |  |  | ICMS ST CAT |
| ICMS_SUPORTADO_TOTAL_CAT_42_18 | numeric(13) |  |  | ICMS Suportado Total CAT |
| SP_PERCENTUAL_BASE_CALCULO_ICMS_PROPRIO_ENTRADAS | numeric(5) |  |  | SP - Percentual base de cálculo ICMS Próprio nas entradas |
| DIF_PAPEL_IMUNE_PDI | char(1) |  |  | Produto incluído no regime especial papel imune - Lei nº 11.945/2009 |
| DIF_PAPEL_IMUNE_TIPO_PDI | char(1) |  |  | Produto incluído no regime especial papel imune - Lei nº 11.945/2009 - Tipo |
| DIF_PAPEL_IMUNE_I_TIPO_PAPEL | integer(4) |  | S | Produto incluído no regime especial papel imune - Lei nº 11.945/2009 - Tipo de Papel |
| DIF_PAPEL_IMUNE_I_PUPLICACAO | integer(4) |  | S | Produto incluído no regime especial papel imune - Lei nº 11.945/2009 - Publicação |
| IMPORTACOES_SAIDAS_INFORMAR_CFOP_SIT_TRIB | char(1) |  | S | Importações - CFOP - Saídas - (CFOP) Informar o CFOP para importação de NFC-e. |
| IMPORTACOES_SAIDAS_CFOP_SIT_TRIB | integer(4) |  | S | Importações - CFOP - Saídas - Informar o CFOP para importação de NFC-e. |
| IMPORTACOES_RZ_CST_SIT_TRIB | integer(4) |  | S | CST para relacionar com situação tributária |
| IMPORTACOES_RZ_INFORMAR_CST_SIT_TRIB | char(1) |  | S | Informar o CST para relacionar com situação tributária |
| GERA_SCANC_MONOFASICO_ICMS_PDI | char(1) |  |  | Gera informações para SCANC do produto sujeito ao regime monofásico do ICMS |
| COD_SCANC_MONOFASICO_ICMS_PDI | integer(4) |  | S | Gera informações para SCANC do produto sujeito ao regime monofásico do ICMS - Codigo do Produto |
| TIPO_SCANC_MONOFASICO_PDI | char(4) |  | S | Tipo Produto SCANC Monofasico |
| IMPORTACOES_SAIDAS_INFORMAR_CFOP_IMPORTACAO_CFE | char(1) |  | S | Importações - CFOP - Saídas - (CFOP) Informar o CFOP para importação de CF-e. |
| IMPORTACOES_SAIDAS_CFOP_IMPORTACAO_CFE | integer(4) |  | S | Importações - CFOP - Saídas - Informar o CFOP para importação de CF-e |
| CODIGO_NBS | char(9) |  | S | Código do NBS |
