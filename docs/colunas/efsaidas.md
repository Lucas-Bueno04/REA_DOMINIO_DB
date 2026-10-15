# efsaidas — Notas Fiscais de Saida
513.113 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_esp | integer(4) |  |  | Especie |
| codi_cli | integer(4) |  |  | Cliente |
| codi_emp | integer(4) | PK |  | Empresa |
| codi_sai | integer(4) | PK |  | Codigo |
| codi_acu | integer(4) |  |  | Acumulador |
| codi_nat | integer(4) |  |  | Natureza |
| cexc_sai | integer(4) |  | S | Exclusoes |
| sigl_est | char(2) |  |  | Estado |
| segi_sai | integer(4) |  |  | Segmento |
| nume_sai | numeric(15) |  |  | Documento |
| seri_sai | char(7) |  |  | Serie |
| atex_sai | numeric(15) |  | S | Documento final |
| dsai_sai | date(4) |  | S | Data de saida |
| ddoc_sai | date(4) |  | S | Data de emissao |
| vcon_sai | numeric(13) |  | S | Valor contabil |
| vexc_sai | numeric(13) |  | S | Valor excluido |
| obse_sai | varchar(300) |  | S | Observacao |
| situ_sai | char(1) |  | S | Campo nao utilizado |
| codm_sai | integer(4) |  | S | Municipio |
| codi_usu | char(30) |  | S | Usuario |
| cifob_sai | char(1) |  | S | C-Cif / F-Fob |
| versao_nat | smallint(2) |  |  | Versao da natureza |
| dorig_sai | date(4) |  |  | Data de origem da nota |
| cfopdet_sai | integer(4) |  | S | CFOP estendido/detalhamento |
| cdtransf_sai | integer(4) |  | S | Codigo da transferencia utlizado para notas de transferencia de creditos - RS |
| codi_obs | integer(4) |  | S | Codigo da observacao |
| dvis_sai | date(4) |  | S | Data do Visto (Para notas de transferencia de credito de ICMS) - MG |
| regexp_sai | char(12) |  | S | Registro de exportacao (PER/DCOMP) |
| antecipacao_sai | tinyint(1) |  | S | Codigo que identifica o tipo da Antecipacao Tributaria |
| fatocrf_sai | char(1) |  |  | Fato Gerador da CRF(E - emissao/P - pagamento) |
| codrec_sai | integer(4) |  | S | Tipo da Receita |
| cancelada_sai | char(1) |  | S | Nota cancelada (S/N) |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| vfre_sai | numeric(13) |  | S | Valor do frete |
| vseg_sai | numeric(13) |  | S | Valor do seguro |
| vdesace_sai | numeric(13) |  | S | Valor das despesas acessorias |
| vlortare_sai | numeric(13) |  | S | SE: Valor calculado refente ao TARE da nota. |
| aliqtare_sai | numeric(13) |  | S | SE: Alíquota do valor calculado refente ao TARE da nota. |
| vprod_sai | numeric(13) |  | S | Valor produtos |
| valor_bc_icms_st_sai | tinyint(1) |  | S | Valor da BC-ST e ICMS-ST obtidos da NF (0=Informacoes complementares/1=Quadro Calculo do Imposto) |
| valor_exclusao_01_sai | numeric(13) |  | S | Exclusoes com codigo 01 |
| valor_exclusao_02_sai | numeric(13) |  | S | Exclusoes com codigo 02 |
| valor_exclusao_03_sai | numeric(13) |  | S | Exclusoes com codigo 03 |
| valor_exclusao_04_sai | numeric(13) |  | S | Exclusoes com codigo 04 |
| fatocrfop_sai | char(1) |  | S | Fato gerador da CRFOP(E - emissão/P - pagamento) |
| fatoirrfp_sai | char(1) |  | S | Fato gerador da IRRFP(E - emissão/P - pagamento) |
| codigo_municipio | integer(4) |  |  | Codigo do municipio |
| situacao_sai | tinyint(1) |  | S | Codigo do modelo do documento fiscal |
| cfps_sai | integer(4) |  | S | Codigo fiscal da prestacao de servicos |
| cod_sittrib_sai | integer(4) |  | S | Codigo da Situacao Tributaria |
| sub_serie_sai | integer(4) |  |  | Sub Serie |
| serie_old_sai | char(7) |  | S | Serie backup |
| tipo_titulo_sai | tinyint(1) |  | S | Tipo do Titulo (0=Duplicata/1=Cheque/2=Promissória/3=Recibo/4=Clientes/5=Documento Fiscal/99=Outros) |
| identificacao_sai | varchar(255) |  | S | Identificacao do titulo |
| cop_sai | char(2) |  |  | Codigo de Operacao e Prestacao |
| compte_sai | date(4) |  |  | Competencia |
| ipi_sobre_remessa_sai | numeric(13) |  | S | IPI sobre a remessa |
| operacao_sai | tinyint(1) |  | S | Operacao |
| nro_parecer_fiscal_sai | char(20) |  | S | Numero do parecer fiscal |
| data_parecer_fiscal_sai | date(4) |  | S | Data do parecer fiscal |
| chave_nfe_sai | char(44) |  | S | Chave da nota fiscal eletrônica |
| codigo_fethab_sai | char(6) |  | S | Codigo de recolhimento do FETHAB |
| responsavel_fethab_sai | char(1) |  | S | Responsavel pelo recolhimento FETHAB (C - Cliente/ E - Empresa) |
| deducao_sai | numeric(13) |  | S | Valor da deducao |
| SERI_IDX_SAI | char(7) |  |  | Serie sem espacos |
| CODI_ENT | integer(4) |  | S | Codigo nota de entrada |
| TIPO_CTE_SAI | integer(4) |  | S | TIPO DE CT-E (0 / 1 / 2 / 3 / 4 / 5 / 6) |
| CTE_REFERENCIA_SAI | char(44) |  | S | CT-e referencia |
| ICMS_ESTOQUE_SAI | numeric(13) |  | S | ICMS sobre estoque |
| NRO_PARCELAS_SAI | integer(4) |  | S | Número de parcelas do ICMS sobre o estoque |
| VENCIMENTO_INICIAL_SAI | date(4) |  | S | Vencimento inicial do ICMS sobre estoque |
| CODIGO_INFORMACAO | integer(4) |  | S | Código da informação complementar |
| INFORMACAO_COMPLEMENTAR | varchar(255) |  | S | Informação complementar |
| CLASSE_CONSUMO_SAI | integer(4) |  | S | Classe de consumo |
| TIPO_LIGACAO_SAI | integer(4) |  | S | Tipo de ligação |
| GRUPO_TENSAO_SAI | integer(4) |  | S | Grupo de tensão |
| TIPO_ASSINANTE_SAI | integer(4) |  | S | Tipo de assinante |
| DIFERIMENTO_SAI | numeric(13) |  | S | Valor do diferimento |
| SUSPENCAO_SAI | numeric(13) |  | S | Valor da suspenção |
| EXCLUSAO_SAI | numeric(13) |  | S | Valor da exclusão |
| REDUCAO_BASE_SAI | char(1) |  | S | Operação com redução da Base de Cálculo |
| VALOR_NOTA_SIOPE_SAI | numeric(13) |  | S | Valor da Nota (Saídas Isentas a Órgão Público Estadual) |
| VALOR_ICMS_SIOPE_SAI | numeric(13) |  | S | Valor do ICMS (Saídas Isentas a Órgão Público Estadual) |
| DATA_EMPENHO_SIOPE_SAI | date(4) |  | S | Data do empenho (Saídas Isentas a Órgão Público Estadual) |
| NOTA_EMPENHO_SIOPE_SAI | integer(4) |  | S | Número da nota de empenho (Saídas Isentas a Órgão Público Estadual) |
| UNIDADE_EXECUTORA_SIOPE_SAI | integer(4) |  | S | Código da unidade executora (Saídas Isentas a Órgão Público Estadual) |
| NOTA_ENTRADA_SIOPE_SAI | integer(4) |  | S | Número da nota fiscal de entrada (Saídas Isentas a Órgão Público Estadual) |
| NUMERO_DI_SIOPE_SAI | numeric(10) |  | S | Número da declaração de importação (Saídas Isentas a Órgão Público Estadual) |
| VALOR_ENERGIA_GAS_SAI | numeric(13) |  | S | Valor fornecido/consumido de gás ou energia elétrica |
| VALOR_COBRADO_TERCEIROS_SAI | numeric(13) |  | S | Valor cobrado de terceiros |
| DESPESAS_ACESSORIAS_SAI | numeric(13) |  | S | Valor das despesas acessórias |
| NOVO_ECF | char(1) |  |  | Indica se é nota gerada pela tela de ECF (apenas para uso do desenvolvimento)(S/N) |
| I_REDUCAO | integer(4) |  | S | Código da redução Z |
| NUMERO_FORMULARIO_INICIAL_SAI | numeric(10) |  | S | Número do Formulário Inicial |
| NUMERO_FORMULARIO_FINAL_SAI | numeric(10) |  | S | Número do Formulário Final |
| CST_PISCOFINS_SAI | integer(4) |  | S | CST - PIS/COFINS |
| NATUREZA_RECEITA_SAI | integer(4) |  | S | Natureza da receita |
| VALOR_SERVICO_ITEM_SAI | numeric(13) |  |  | Valor servicos/itens - PIS/COFINS |
| BASE_CALCULO_PISCOFINS_SAI | numeric(13) |  |  | Base de calculo - PIS/COFINS |
| ALIQUOTA_PIS_PISCOFINS_SAI | numeric(7) |  |  | Aliquota de PIS - PIS/COFINS |
| ALIQUOTA_COFINS_PISCOFINS_SAI | numeric(7) |  |  | Aliquota de COFINS - PIS/COFINS |
| DADOS_PISCOFINS_OK | char(1) |  |  | Dados referente ao PIS/COFINS OK (S/N) |
| KWH_SAI | integer(4) |  | S | KWH consumido |
| SERVICO_NAO_TRIBUTADO_ICMS_SAI | numeric(13) |  |  | Valor total dos serviços nao-tributados pelo ICMS |
| VALOR_PRESENTE_SAI | numeric(13) |  |  | Valor presente |
| VALOR_PRESENTE_TAXA_SAI | numeric(13) |  |  | Taxa valor presente |
| VALOR_PRESENTE_JUROS_SAI | numeric(13) |  |  | Juros valor presente |
| VALOR_PRESENTE_TIPO_TAXA_SAI | char(1) |  |  | Tipo taxa valor presente (M=Mensal/ A=Anual/ D=Diario) |
| CODIGO_NATUREZA_SAI | integer(4) |  | S | Código da Natureza |
| DATA_SAIDA | date(4) |  |  | Data de saída da nota |
| CST_IPI | tinyint(1) |  | S | CST IPI |
| NRO_CONTA_CONSUMO_SAI | varchar(12) |  | S | Número da conta de consumo |
| TIPO_UTILIZACAO_SAI | integer(4) |  | S | Tipo de Utilização |
| UF_TERMINAL_TELEFONICO_SAI | char(2) |  | S | UF terminal telefônico |
| DDDF_TERMINAL_SAI | integer(4) |  | S | DDD Terminal/Aparelho Telefônico |
| FONE_TERMINAL_SAI | char(14) |  | S | Telefone Terminal/Aparelho Telefônico |
| I_CST_VIGENCIA_ICMS | integer(4) |  | S | Código sequencial do CST de ICMS |
| UF_CONSUMIDOR_SAI | char(2) |  | S | UF Consumidor |
| I_RECOLHIMENTO_FETHAB | integer(4) |  | S | Sequencial do código de recolhimento do FETHAB |
| I_SCP | integer(4) |  | S | Sequencial do SCP |
| ESTOQUE_APURADO_SAI | date(4) |  | S | Estoque apurado em |
| EMITENTE | char(1) |  |  | Emitente (P - Próprio / T - Terceiros) |
| TIPO_CRED_ACU_SAI | integer(4) |  | S | Tipo de crédito acumulado |
| CLASSE_CONSUMO_SEF_2012_SAI | integer(4) |  | S | Classe de consumo |
| TIPO_SERVICO | integer(4) |  |  | Tipo de Serviço (1 / 2) |
| PRESTACAO_SERVICO_PERIODO | date(4) |  | S | Período da prestação do serviço |
| PRESTACAO_SERVICO_DATA_INICIAL | date(4) |  | S | Período da prestação do serviço - Data inicial |
| PRESTACAO_SERVICO_DATA_FINAL | date(4) |  | S | Período da prestação do serviço - Data final |
| ESPECIFICACAO | varchar(60) |  | S | Especificação |
| RS_NUMERO_RECEITA_AGRONOMICA | char(11) |  |  | RS - Número da receita agronômica |
| VALOR_DESCONTO_SAI | numeric(13) |  |  | Valor do desconto |
| PEDAGIO_SAI | numeric(13) |  |  | Valor pedágio |
| IPI_SAI | numeric(13) |  |  | Valor IPI |
| ICMS_ST_SAI | numeric(13) |  |  | Valor ICMS ST |
| TIPO_ATENDIMENTO_SAI | integer(4) |  |  | TIPO ATENDIMENTO (0 / 1 / 2 / 3 / 4 / 5/ 9) |
| DATA_ESCRITURACAO | date(4) |  | S | Data de escrituração da nota |
| CONSUMIDOR_FINAL | char(1) |  |  | Consumidor Final |
| TIPO_CLIENTE | char(2) |  | S | Tipo de cliente |
| SUBCLASSE | char(2) |  | S | Subclasses |
| PERIODO_LEITURA_ANTERIOR | date(4) |  | S | Período de leitura anterior |
| PERIODO_LEITURA_ATUAL | date(4) |  | S | Período de leitura atual |
| NUMERO_FATURA | varchar(20) |  | S | Número da Fatura |
| MODALIDADE_FRETE_SAI | char(1) |  | S | Modalidade do Frete |
| CODIGO_MUNICIPIO_DESTINO | integer(4) |  |  | Código do município destino |
| CONFERIDO | char(1) |  |  | Conferido (S/N) |
| VALOR_ICMS_DESONERADO_SAI | numeric(13) |  |  | Valor ICMS Desonerado |
| VALOR_ICMS_DEBITO_ICMS_SUSPENSAO_DIFERIMENTO_SAIDAS_CONTRIB_REF | numeric(13) |  |  | Débito de ICMS (Não destacado em NF-e) pela suspensão do diferimento nas saídas a contribuinte do REF - Valor ICMS |
| MODAL_CTE_SAI | integer(4) |  | S | Modelo de CT-e |
| NOTA_COMPLEMENTAR_MOTIVO_SAI | integer(4) |  |  | Nota complementar - Motivo |
| VALOR_IPI_DEVOLUCAO | numeric(13) |  |  | IPI devolução |
| HASH_REFERENCIADO | char(32) |  |  | Hash referenciado |
| SERIE_REFERENCIADA | char(4) |  |  | Série referenciada |
| NUMERO_REFERENCIADO | char(9) |  |  | Número referenciado |
| PERIODO_REFERENCIADO | date(4) |  | S | Período referenciado |
| MODELO_REFERENCIADO | char(2) |  | S | Modelo referenciado |
| ENERGIA_INJETADA | numeric(13) |  |  | Energia injetada |
| VALOR_MULTA_ICMS_EXTEMPORANEO | numeric(13) |  |  | Valor multa ICMS extemporâneo |
| VALOR_JUROS_ICMS_EXTEMPORANEO | numeric(13) |  |  | Valor juros ICMS extemporâneo |
| TIPO_FATURAMENTO_NFCOM | integer(4) |  |  | Tipo de Faturamento NFCom (1 - Faturamento Normal  2 - Faturamento Centralizado  3 - Cofaturamento) |
| VALOR_TOTAL_IBS | numeric(13) |  |  | Valor Total IBS da Nota |
| VALOR_TOTAL_CBS | numeric(13) |  |  | Valor Total CBS da Nota |
| DEDUCOES | numeric(13) |  |  | Deduções |
| TIPO_FATURAMENTO_NFAG | integer(4) |  |  | Tipo de Faturamento NFAg (1 - Faturamento Normal  2 - Faturamento por terceiro  3 - Faturamento conjunto) |
| TIPO_LIGACAO_NFAG | integer(4) |  |  | Tipo de Ligação NFAg (1 - Água  2 - Esgoto  3 - Água e esgoto) |
| FORMA_PAGAMENTO | integer(4) |  | S | Forma de pagamento (0 - Pré pago, 1 - Pós pago) |
| VALOR_IS_SAI | numeric(13) |  |  | Valor IS (Imposto Seletivo) |
| DATA_ENTREGA | date(4) |  | S | DATA ENTREGA |
| FINALIDADE_SAI | integer(4) |  | S | Finalidade da nota |
| TIPO_NOTA_SAI | integer(4) |  | S | Tipo de nota |
