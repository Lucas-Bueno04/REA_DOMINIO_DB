# efentradas — Notas Fiscais de Entrada
511.949 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_ent | integer(4) | PK |  | Codigo |
| codi_for | integer(4) |  |  | Fornecedor |
| codi_esp | integer(4) |  |  | Especie |
| cexc_ent | integer(4) |  | S | Exclusoes |
| codi_acu | integer(4) |  |  | Acumulador |
| codi_nat | integer(4) |  |  | Natureza |
| segi_ent | integer(4) |  |  | Segmento |
| nume_ent | numeric(15) |  |  | Documento |
| seri_ent | char(7) |  |  | Serie |
| atex_ent | numeric(15) |  | S | Documento final |
| dent_ent | date(4) |  | S | Data de entrada |
| ddoc_ent | date(4) |  | S | Data de emissao |
| vcon_ent | numeric(13) |  | S | Valor contabil |
| vexc_ent | numeric(13) |  | S | Valor excluido |
| obse_ent | varchar(300) |  | S | Observacao |
| situ_ent | char(1) |  | S | Campo nao utilizado |
| codi_usu | char(30) |  | S | Usuario |
| cifob_ent | char(1) |  | S | C-Cif / F-Fob |
| versao_nat | smallint(2) |  |  | Versao da natureza |
| emitente_ent | char(1) |  | S | Emitente da Nota Fiscal  ( P-Proprio / T-Terceiro ) |
| dorig_ent | date(4) |  |  | Data de origem da nota |
| codm_ent | integer(4) |  | S | Codigo do municipio |
| cfopdet_ent | integer(4) |  | S | CFOP estendido/detalhamento |
| cdtransf_ent | integer(4) |  | S | RS: Codigo da transferencia utilizado para notas de transferencia de creditos |
| creciss_ent | char(6) |  | S | Codigo de Recolhimento do ISS Retido |
| crecirrf_ent | char(6) |  | S | Codigo de Recolhimento do IRRF |
| codi_obs | integer(4) |  | S | Codigo da observacao |
| dvis_ent | date(4) |  | S | Data do Visto (Para notas de transferencia de credito de ICMS em MG) |
| fatocrf_ent | char(1) |  |  | Fato Gerador da CRF(E-emissao/P-pagamento) |
| fatoirrf_ent | char(1) |  |  | Fato Gerador do IRRF(E-emissao/P-pagamento) |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| vfre_ent | numeric(13) |  | S | Valor do frete |
| vseg_ent | numeric(13) |  | S | Valor do Seguro |
| vdesace_ent | numeric(13) |  | S | Valor das despesas acessorias |
| vpis_ent | numeric(13) |  | S | Valor do PIS |
| antecipacao_ent | tinyint(1) |  | S | Codigo que identifica o tipo da Antecipacao Tributaria |
| vcof_ent | numeric(13) |  | S | Valor do COFINS |
| vlortare_ent | numeric(13) |  | S | SE: Valor calculado refente ao TARE da nota. |
| aliqtare_ent | numeric(13) |  | S | SE: Alíquota do valor calculado refente ao TARE da nota. |
| valor_bc_icms_st_ent | tinyint(1) |  | S | Valor da BC-ST e ICMS-ST obtidos da NF (0=Informacoes complementares/1=Quadro Calculo do Imposto/2=Apurado pelo informante) |
| valor_exclusao_01_ent | numeric(13) |  | S | Exclusoes com codigo 01 |
| valor_exclusao_03_ent | numeric(13) |  | S | Exclusoes com codigo 03 |
| valor_exclusao_04_ent | numeric(13) |  | S | Exclusoes com codigo 04 |
| cod_ressarcimento_ent | integer(4) |  | S | Codigo ressarcimento |
| vprod_ent | numeric(13) |  | S | Valor produtos |
| codigo_municipio | integer(4) |  |  | Codigo do municipio |
| situacao_ent | tinyint(1) |  | S | Codigo do modelo do documento fiscal |
| cod_sittrib_ent | integer(4) |  | S | Codigo da Situacao Tributaria |
| sub_serie_ent | integer(4) |  |  | Sub Serie |
| serie_old_ent | char(7) |  | S | Serie backup |
| cop_ent | char(2) |  |  | Codigo de Operacao e Prestacao |
| ded_rec_trib_ent | numeric(13) |  | S | Valor a ser deduzido da receita tributavel |
| compte_ent | date(4) |  |  | Competencia |
| operacao_ent | tinyint(1) |  | S | Operacao |
| nro_parecer_fiscal_ent | char(20) |  | S | Numero do parecer fiscal |
| data_parecer_fiscal_ent | date(4) |  | S | Data do parecer fiscal |
| declaracao_importacao_ent | char(15) |  | S | Numero da declaracao de importacao |
| beneficio_fiscal_ent | char(1) |  | S | Possui beneficio fiscal(S/N) |
| chave_nfe_ent | char(44) |  | S | Chave da nota fiscal eletrônica |
| codigo_fethab_ent | char(6) |  | S | Codigo de recolhimento do FETHAB |
| responsavel_fethab_ent | char(1) |  | S | Responsavel pelo recolhimento FETHAB (C - Cliente/ E - Empresa) |
| CFOP_SAI_ENT | integer(4) |  | S | CFOP documento fiscal |
| TIPO_CTE_ENT | integer(4) |  | S | TIPO DE CT-E (0 / 1 / 2 / 3 / 4 / 5 / 6) |
| CTE_REFERENCIA_ENT | char(44) |  | S | CT-e referencia |
| MODALIDADE_IMPORTACAO_ENT | integer(4) |  | S | Modalidade da importação(1 - Com direito a crédito/2 - Compensação/3 - Regime especial/4 - Sem direito a crédito/5 - Outras situações - Sem crédito) |
| CODIGO_INFORMACAO | integer(4) |  | S | Código da informação complementar |
| INFORMACAO_COMPLEMENTAR | varchar(255) |  | S | Informação complementar |
| CLASSE_CONSUMO_ENT | integer(4) |  | S | Classe de consumo |
| TIPO_LIGACAO_ENT | integer(4) |  | S | Tipo de ligação |
| GRUPO_TENSAO_ENT | integer(4) |  | S | Grupo de tensão |
| TIPO_ASSINANTE_ENT | integer(4) |  | S | Tipo de assinante |
| KWH_ENT | integer(4) |  | S | KWH consumido |
| VALOR_ENERGIA_GAS_ENT | numeric(13) |  | S | Valor fornecido/consumido de gás ou energia elétrica |
| VALOR_COBRADO_TERCEIROS_ENT | numeric(13) |  | S | Valor cobrado de terceiros |
| DESPESAS_ACESSORIAS_ENT | numeric(13) |  | S | Valor das despesas acessórias |
| TIPO_IMPORTACAO_ENT | integer(4) |  | S | TIPO DO DOCUMENTO DE IMPORTAÇÃO(0 - DECLARAÇÃO DE IMPORTAÇÃO/1 - DECLARAÇÃO SIMPLIFICADA DE IMPORTAÇÃO/2- DECLARAÇÃO ÚNICA DE IMPORTAÇÃO) |
| NUMERO_AC_DRAWBACK_ENT | char(20) |  | S | Número do Ato Concessório do regime Drawback |
| CHAVE_NFSE_ENT | varchar(60) |  | S | Chave da nota fiscal de servico eletronica |
| NATUREZA_FRETE_ENT | tinyint(1) |  |  | Natureza do frete |
| NRO_PROCESSO_ATO_CONCESSORIO_ENT | varchar(15) |  | S | Numero do processo ou ato concessorio |
| ORIGEM_PROCESSO_ENT | char(1) |  |  | Origem do processo (1=Justica Federal/ 3=Secretaria da Receita Federal do Brasil/ 9=Outros) |
| CST_PISCOFINS_ENT | integer(4) |  | S | CST - PIS/COFINS |
| BASE_CREDITO_ENT | integer(4) |  | S | Base do credito - PIS/COFINS |
| VALOR_SERVICO_ITEM_ENT | numeric(13) |  |  | Valor servicos/itens - PIS/COFINS |
| BASE_CALCULO_PISCOFINS_ENT | numeric(13) |  |  | Base de calculo - PIS/COFINS |
| ALIQUOTA_PIS_PISCOFINS_ENT | numeric(7) |  |  | Aliquota de PIS - PIS/COFINS |
| ALIQUOTA_COFINS_PISCOFINS_ENT | numeric(7) |  |  | Aliquota de COFINS - PIS/COFINS |
| DADOS_PISCOFINS_OK | char(1) |  |  | Dados referente ao PIS/COFINS OK (S/N) |
| SERVICO_NAO_TRIBUTADO_ICMS_ENT | numeric(13) |  |  | Valor total dos serviços nao-tributados pelo ICMS |
| VALOR_PRESENTE_ENT | numeric(13) |  |  | Valor presente |
| VALOR_PRESENTE_TAXA_ENT | numeric(13) |  |  | Taxa valor presente |
| VALOR_PRESENTE_JUROS_ENT | numeric(13) |  |  | Juros valor presente |
| VALOR_PRESENTE_TIPO_TAXA_ENT | char(1) |  |  | Tipo taxa valor presente (M=Mensal/ A=Anual/ D=Diario) |
| DATA_REGISTRO_SISCOMEX_ENT | date(4) |  | S | Data do registro SISCOMEX |
| DATA_DESEMBARACO_ENT | date(4) |  | S | Data de desembaraço da mercadoria |
| DESPESAS_QUE_NAO_COMPOE_BASE_ICMS_ENT | numeric(13) |  |  | Despesas aduaneiras que não compõe Base de cálculo do ICMS |
| DESPESAS_QUE_COMPOE_BASE_ICMS_ENT | numeric(13) |  |  | Despesas aduaneiras que compõe Base de cálculo do ICMS |
| TIPO_TITULO_ENT | integer(4) |  | S | Tipo do título (0=Duplicata/1=Cheque/2=Promissória/3=Recibo/99=Outros) |
| IDENTIFICACAO_ENT | varchar(255) |  | S | Identificação do título |
| TIPO_RECOLHIMENTO_ST | char(1) |  |  | Tipo de recolhimento ST (G - GNRE/D - DARE) |
| NUMERO_LICENCA_IMPORTACAO_ENT | varchar(10) |  |  | Número da Licença de Importação |
| DATA_ENTRADA | date(4) |  |  | Data de entrada da nota |
| DATA_ESCRITURACAO | date(4) |  | S | Data de escrituração da nota |
| CFPS_ENT | integer(4) |  | S | Código fiscal da prestação de serviços |
| VALOR_CREDITO_PRESUMIDO | numeric(13) |  |  | Credito Presumido Guajará-Mirim |
| CST_IPI | tinyint(1) |  | S | CST IPI |
| I_CST_VIGENCIA_ICMS | integer(4) |  | S | Código sequencial do CST de ICMS |
| I_RECOLHIMENTO_FETHAB | integer(4) |  | S | Sequencial do código de recolhimento do FETHAB |
| I_SCP | integer(4) |  | S | Sequencial do SCP |
| TIPO_SERVICO | integer(4) |  |  | Tipo de Serviço (1 / 2) |
| ESPECIFICACAO | varchar(60) |  | S | Especificação |
| RS_NUMERO_RECEITA_AGRONOMICA | char(11) |  |  | RS - Número da receita agronômica |
| RELACAO_FONTE_PAGADORA_E_BENEFICIARIO_PJ_ENT | integer(4) |  | S | Relação fonte pagadora e beneficiário pessoa jurídica |
| TIPO_DE_RENDIMENTO_ENT | integer(4) |  | S | Tipo de rendimento |
| FORMA_DE_TRIBUTACAO_ENT | integer(4) |  | S | Forma de tributação |
| VALOR_RESSARCIMENTO_1603_2603_SUBTRI | numeric(13) |  |  | Valor do Ressarcimento 1603 / 2603 - SUBTRI |
| VALOR_DESCONTO_ENT | numeric(13) |  |  | Valor do desconto |
| PEDAGIO_ENT | numeric(13) |  |  | Valor Pedágio |
| IPI_ENT | numeric(13) |  |  | Valor IPI |
| ICMS_ST_ENT | numeric(13) |  |  | Valor ICMS ST |
| CODIGO_MUNICIPIO_DESTINO | integer(4) |  |  | Código Município destino |
| VALOR_IPI_DEVOLUCAO | numeric(13) |  |  | IPI devolução |
| MODALIDADE_FRETE_ENT | char(1) |  | S | Modalidade do Frete |
| CONFERIDO | char(1) |  |  | Conferido (S/N) |
| NUMERO_OTC | numeric(15) |  |  | Número da Ordem de Transferência de Crédito - OTC |
| NUMERO_DOCUMENTO_ARRECADACAO_ENT | varchar(255) |  | S | Número do documento de arrecadação |
| VALOR_ICMS_DESONERADO_ENT | numeric(13) |  |  | Valor ICMS desonerado Entradas |
| MODAL_CTE_ENT | integer(4) |  | S | Modelo CT-e |
| HASH_REFERENCIADO | char(32) |  |  | Hash referenciado |
| SERIE_REFERENCIADA | char(4) |  |  | Série referenciada |
| NUMERO_REFERENCIADO | char(9) |  |  | Número referenciado |
| PERIODO_REFERENCIADO | date(4) |  | S | Período referenciado |
| MODELO_REFERENCIADO | char(2) |  | S | Modelo referenciado |
| ENERGIA_INJETADA | numeric(13) |  |  | Energia injetada |
| TIPO_FATURAMENTO_NFCOM | integer(4) |  |  | Tipo de Faturamento NFCom (1 - Faturamento Normal  2 - Faturamento Centralizado  3 - Cofaturamento) |
| VALOR_TOTAL_IBS | numeric(13) |  |  | Valor Total IBS da Nota |
| VALOR_TOTAL_CBS | numeric(13) |  |  | Valor Total CBS da Nota |
| DEDUCOES | numeric(13) |  |  | Deduções |
| TIPO_FATURAMENTO_NFAG | integer(4) |  |  | Tipo de Faturamento NFAg (1 - Faturamento Normal  2 - Faturamento por terceiro  3 - Faturamento conjunto) |
| TIPO_LIGACAO_NFAG | integer(4) |  |  | Tipo de Ligação NFAg (1 - Água  2 - Esgoto  3 - Água e esgoto) |
| VALOR_IS_ENT | numeric(14) |  |  | Valor IS (Imposto Seletivo) |
| FINALIDADE_ENT | integer(4) |  | S | Finalidade da nota |
| TIPO_NOTA_ENT | integer(4) |  | S | Tipo de nota |
