# CTSPED_ECF_OD — SPED ECF - Outros Dados
2.533 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_OUTROS_DADOS | integer(4) | PK |  | Sequencial |
| ANO_CALENDARIO | date(4) |  |  | Ano da emissão do SPED |
| I_SCP | integer(4) |  | S | SCP |
| INDICADOR_SITUACAO_ESPECIAL | char(1) |  |  | Indicador de situação especial (S/N) |
| INDICADOR_SITUACAO_ESPECIAL_EVENTO | integer(4) |  |  | Evento do indicador de situação especial (1 - Extinção / 2 - Fusão 3 - Incorporação/Incorporada / 4 - Incorporação/Incorporadora / 5 - Cisão Total / 6 - Cisão Parcial / 7 - Transformação / 8 - Desenquadramento de Imune/Isenta / 9 - Inclusão no SN) |
| INDICADOR_SITUACAO_ESPECIAL_DATA_EVENTO | date(4) |  |  | Data do evento do indicador de situação especial |
| PATRIMONIO_REMANESCENTE_CISAO | numeric(7) |  |  | Patrimônio remanescente em caso de cisão do indicador de situação especial |
| RETIFICADORA | char(1) |  |  | TIPO DA ESCRITURAÇÃO RETIFICADORA (N - ECF ORIGINAL / S - ECF RETIFICADORA / F - ECF ORIGINAL COM MUDANÇA DE FORMA DE TRIBUTAÇÃO (IN Nº 166/1999)) |
| RETIFICADORA_NUMERO_RECIBO | varchar(41) |  |  | Número do recibo da retificadora |
| INDICADOR_INICIO_PERIODO | integer(4) |  |  | Indicador de início de período |
| OPTANTE_REFIS | char(1) |  |  | Optante pelo Refis (S/N) |
| OPTANTE_PAES | char(1) |  |  | Optante pelo Paes (S/N) |
| OPTANTE_EXTINCAO_RTT_2014 | char(1) |  |  | Optante pela extinção do RTT no ano-calendário de 2014 (S/N) |
| EXISTE_DIFERENCA_CONTABILIDADE_SOCIETARIA_FCONT | char(1) |  |  | Existe diferença entre a contabilidade societária e FCONT (S/N) |
| GERAR_CONTAS_CCU | char(1) |  |  | Gerar contas por centros de custos (S/N) |
| GERAR_CONTAS_POR | integer(4) |  |  | Gerar as contas contábeis por |
| FORMA_TRIBUTACAO | integer(4) |  |  | FORMA DE TRIBUTAÇÃO DO LUCRO (1 - LUCRO REAL / 2 - LUCRO REAL/ARBITRADO / 3 - LUCRO PRESUMIDO/REAL / 5 - LUCRO PRESUMIDO / 6 - LUCRO ARBITRADO / 7 - LUCRO PRESUMIDO/ARBITRADO / 8 - IMUNE DE IRPJ / 9 - ISENTO DO IRPJ) |
| PERIODO_APURACAO_IRPJ_CSLL | char(1) |  |  | Período de apuração do IRPJ e CSLL (T - Trimestral / A - Anual) |
| QUALIFICACAO_PESSOA_JURIDICA | integer(4) |  |  | QUALIFICACAO DA PESSOA JURIDICA (1 - PJ EM GERAL / 2 - PJ COMPONENTE DO SISTEMA FINANCEIRO / 3 - SOCIEDADES SEGURADORAS, DE CAPITALIZACAO OU ENTIDADE ABERTA DE PREVIDENCIA COMPLEMENTAR / 4 - SOCIEDADE ANONIMA DO FUTEBOL) |
| TIPO_ENTIDADE_ISENTA_IMUNE | integer(4) |  |  | Tipo de entidade imune/isenta |
| TIPO_ESCRITURACAO | char(1) |  |  | Tipo de escrituração (L - Livro Caixa (Lucro Presumido) ou Sem Escrituração / C - Contábil (Lucro Presumido, Imunes ou Isentas)) |
| EXISTENCIA_ATIVIDADE_TRIBUTADA_IRPJ_CSLL | char(1) |  |  | Existência atividade tributada pelo IRPJ e CSLL |
| APURACAO_CSLL | char(1) |  |  | Apuração da CSLL |
| FORMA_DETERMINACAO_ESTIMATIVA_MENSAL_01 | char(1) |  | S | Forma de determinação das estimativas mensais - Janeiro |
| FORMA_DETERMINACAO_ESTIMATIVA_MENSAL_02 | char(1) |  | S | Forma de determinação das estimativas mensais - Fevereiro |
| FORMA_DETERMINACAO_ESTIMATIVA_MENSAL_03 | char(1) |  | S | Forma de determinação das estimativas mensais - Março |
| FORMA_DETERMINACAO_ESTIMATIVA_MENSAL_04 | char(1) |  | S | Forma de determinação das estimativas mensais - Abril |
| FORMA_DETERMINACAO_ESTIMATIVA_MENSAL_05 | char(1) |  | S | Forma de determinação das estimativas mensais - Maio |
| FORMA_DETERMINACAO_ESTIMATIVA_MENSAL_06 | char(1) |  | S | Forma de determinação das estimativas mensais - Junho |
| FORMA_DETERMINACAO_ESTIMATIVA_MENSAL_07 | char(1) |  | S | Forma de determinação das estimativas mensais - Julho |
| FORMA_DETERMINACAO_ESTIMATIVA_MENSAL_08 | char(1) |  | S | Forma de determinação das estimativas mensais - Agosto |
| FORMA_DETERMINACAO_ESTIMATIVA_MENSAL_09 | char(1) |  | S | Forma de determinação das estimativas mensais - Setembro |
| FORMA_DETERMINACAO_ESTIMATIVA_MENSAL_10 | char(1) |  | S | Forma de determinação das estimativas mensais - Outubro |
| FORMA_DETERMINACAO_ESTIMATIVA_MENSAL_11 | char(1) |  | S | Forma de determinação das estimativas mensais - Novembro |
| FORMA_DETERMINACAO_ESTIMATIVA_MENSAL_12 | char(1) |  | S | Forma de determinação das estimativas mensais - Dezembro |
| PJ_SUJEITA_ALIQUOTA_CSLL_15 | char(1) |  |  | PJ sujeita à alíquota da CSLL de 15% (S/N) |
| ADMINISTRADORA_FUNDOS_CLUBES_INVESTIMENTO | char(1) |  |  | Administradora de fundos e clubes de investimentos (S/N) |
| OPERACAO_EXTERIOR | char(1) |  |  | operações com o exterior (S/N) |
| OPERACAO_PESSOA_VINCULADA | char(1) |  |  | operações com pessoa vinculada/interposta pessoa/pais com tributação favorecida (S/N) |
| PJ_ENQUADRADA_ART_58 | char(1) |  |  | PJ enquadrada no art. 58-A da IN nº 1.312/2012 (S/N) |
| PARTICIPACAO_EXTERIOR | char(1) |  |  | Participações no exterior (S/N) |
| PARTICIPACAO_PERMANENTE_COLIGADA | char(1) |  |  | Participação permanente em colignadas ou controladas (S/N) |
| PJ_EFETUOU_VENDAS_EXPORTACAO | char(1) |  |  | PJ efetuou vendas a empresa comercial exportadora com fim específico de exportação (S/N) |
| RECEBIMENTO_EXTERIOR | char(1) |  |  | Recebimentos do exterior ou de não residentes (S/N) |
| PARTICIPACAO_CONSORCIO | char(1) |  |  | Participações em consórcios de empresas (S/N) |
| LUCRO_EXPLORACAO | char(1) |  |  | Lucro da exploração (S/N) |
| ISENCAO_REDUCAO_IMPOSTO_LUCRO_PRESUMIDO | char(1) |  |  | Isenção e redução do imposto para Lucro Presumido (S/N) |
| FINOR_FINAM_FUNRES | char(1) |  |  | FINOR/FINAM/FUNRES (S/N) |
| DOACAO_CAMPANHA_ELEITORAL | char(1) |  |  | Doações a campanhas eleitorais (S/N) |
| ATIVIDADE_RURAL | char(1) |  |  | Atividade rural (S/N) |
| ATIVO_EXTERIOR | char(1) |  |  | Ativos no exterior (S/N) |
| PJ_COMERCIAL_EXPORTADORA | char(1) |  |  | PJ comercial exportadora (S/N) |
| PAGAMENTO_EXTERIOR | char(1) |  |  | Pagamentos ao exterior ou a não residentes (S/N) |
| COMERCIO_ELETRONICO_TECNOLOGIA_INFORMACAO | char(1) |  |  | Comércio eletrônico e tecnologia da informação (S/N) |
| ROYALTIES_RECEBIDO_BRASIL_EXTERIOR | char(1) |  |  | Royalties recebidos do Brasil e do exterior (S/N) |
| ROYALTIES_PAGO_BRASIL_EXTERIOR | char(1) |  |  | Royalties pagos a beneficiários do Brasil e do exterior (S/N) |
| RENDIMENTO_SERVICO_JUROS_BRASIL_EXTERIOR | char(1) |  |  | Rendimentos relativos a serviços, juros e dividendos a beneficiários do Brasil e do exterior (S/N) |
| PAGAMENTO_SERVICO_JUROS_BRASIL_EXTERIOR | char(1) |  |  | Pagamentos ou remessas a título de serviços, juros e dividendos a beneficiários do Brasil e do exterior (S/N) |
| INOVACAO_TECNOLOGICA | char(1) |  |  | Inovação tencológica e desenvolvimento tencológico (S/N) |
| CAPACITACAO_INFORMATICA | char(1) |  |  | Capacitação de informática e inclusão digital (S/N) |
| REPES_RECAP_PADIS | char(1) |  |  | Repes, Recap, Padis, PATVD, Reidi, Repenec, Reicomp, Retaero, Recine, Resíduos sólidos, Recopa, Copa do mundo, Retid, REPNBL-Redes, Reif e Olimpíadas (S/N) |
| POLO_INDUSTRIAL_MANAUS_AMAZONIA_OCIDENTAL | char(1) |  |  | Pólo industrial de Manaus e Amazônia Ocidental (S/N) |
| ZONA_PROCESSAMENTO_EXPORTACAO | char(1) |  |  | Zonas de processamento de exportação (S/N) |
| AREA_LIVRE_COMERCIO | char(1) |  |  | Áreas de livre comércio (S/N) |
| CODI_EMP_I_SCP | integer(4) |  | S | Empresa - SCP |
| GERAR_SOMENTE_CONTAS_COM_MOVIMENTO | char(1) |  |  | Gerar somente contas com movimento |
| GERAR_SOMENTE_TABELAS_COM_MOVIMENTO | char(1) |  |  | Gerar somente tabelas com movimento |
| FORMA_TRIBUTACAO_TRIMESTRE_1 | integer(4) |  |  | FORMA DE TRIBUTA?O DO TRIMESTRE 1 (1 - LUCRO REAL / 5 - LUCRO PRESUMIDO / 6 - ARBITRADO) |
| FORMA_TRIBUTACAO_TRIMESTRE_2 | integer(4) |  |  | FORMA DE TRIBUTA?O DO TRIMESTRE 2 (1 - LUCRO REAL / 5 - LUCRO PRESUMIDO / 6 - ARBITRADO) |
| FORMA_TRIBUTACAO_TRIMESTRE_3 | integer(4) |  |  | FORMA DE TRIBUTA?O DO TRIMESTRE 3 (1 - LUCRO REAL / 5 - LUCRO PRESUMIDO / 6 - ARBITRADO) |
| FORMA_TRIBUTACAO_TRIMESTRE_4 | integer(4) |  |  | FORMA DE TRIBUTA?O DO TRIMESTRE 4 (1 - LUCRO REAL / 5 - LUCRO PRESUMIDO / 6 - ARBITRADO) |
| GERAR_BLOCO_Q_LIVRO_CAIXA | char(1) |  |  | Gerar bloco Q - Livro Caixa |
| PJ_SUJEITA_ALIQUOTA_CSLL | numeric(5) |  |  | Alíquota da PJ CSLL (9=9% / 17=17% / 20=20%) |
| CRITERIO_DE_RECONHECIMENTO_DE_RECEITAS | integer(4) |  |  | Critério de reconhecimento de receitas (1 - Regime de caixa / 2 - Regime de competência) |
| REGIME_ESPECIAL_REPES | char(1) |  |  | Repes |
| REGIME_ESPECIAL_RECAP | char(1) |  |  | Recap |
| PROGRAMA_APOIO_PADIS | char(1) |  |  | Padis |
| PROGRAMA_APOIO_PATVD | char(1) |  |  | PATVD |
| REGIME_ESPECIAL_REIDI | char(1) |  |  | Reidi |
| REGIME_ESPECIAL_REPENEC | char(1) |  |  | Repenec |
| REGIME_ESPECIAL_REICOMP | char(1) |  |  | Reicomp |
| REGIME_ESPECIAL_RETAERO | char(1) |  |  | Retaero |
| REGIME_ESPECIAL_RECINE | char(1) |  |  | Recine |
| ESTABELECIMENTO_INDUSTRIAL_DEZEMBRO_2010 | char(1) |  |  | Estabelecimentos industriais - 30 de dezembro de 2010 |
| REGIME_ESPECIAL_RECOPA | char(1) |  |  | Recopa |
| HABILITADA_BENEFICIO_FISCAL_COPA_CONFEDERACAO_OUTUBRO_2011 | char(1) |  |  | Habilitada benefícios fiscais copa das confederações - 11 de outubro de 2011 |
| REGIME_ESPECIAL_RETID | char(1) |  |  | Retid |
| REGIME_ESPECIAL_REDES | char(1) |  |  | Redes |
| REGIME_ESPECIAL_REIF | char(1) |  |  | REIF |
| HABILITADA_BENEFICIO_FISCAL_JOGO_OLIMPICO_2016 | char(1) |  |  | Habilitada benefícios fiscais dos jogos olímpicos de 2016 |
| OBRIGADO_ENTREGA_DECLARACAO_PAIS_A_PAIS | char(1) |  |  | Obrigado à entrega da Declaração País-a-País |
| GERAR_REGISTRO_U100_U150_BALANCO_PATRIMONIAL | char(1) |  |  | Gerar os registros U100 e U150 com o Balanço patrimonial e a Demonstração do resultado (S/N) |
| GERAR_BLOCO_Q_CONTAS_EQUIVALENTES_CAIXA | char(1) |  |  | Gerar no bloco Q lançametnos contas equivalentes de caixa |
| DECLARACAO_UTILIZACAO_MOEDA_EXTRANGEIRA_DEREX | char(1) |  |  | Declaração sobre utilização dos recursos em moeda estrangeira decorrentes do recebimento de exportações (DEREX) |
| PJ_SUJEITA_ALIQUOTA_CSLL_2019 | numeric(30) |  |  | Alíquota da PJ CSLL (9=9% 15=15%/15=15%-20%/20=20%-25%/12=9%-12%/17=15%-17,5%) |
| REGIME_SUSPENSAO_OLEO_BUNKER | char(1) |  |  | Regime de Suspensão de Óleo Bunker |
| REGIME_TRIBUTARIO_REPORTO | char(1) |  |  | Reporto |
| REGIME_ESPECIAL_RETII | char(1) |  |  | RET_II |
| REGIME_ESPECIAL_RET_PMCMV | char(1) |  |  | RET-PMCMV |
| REGIME_ESPECIAL_RET_EEI | char(1) |  |  | RET-EEI |
| ENTIDADE_BENEFICIENTE_EBAS | char(1) |  |  | EBAS |
| REGIME_ESPECIAL_REPETRO_INDUSTRIALIZACAO | char(1) |  |  | REPETRO-INDUSTRIALIZAÇÃO |
| REGIME_TRIBUTARIO_REPETRO_NACIONAL | char(1) |  |  | REPETRO-NACIONAL |
| REGIME_TRIBUTARIO_REPETRO_PERMANENTE | char(1) |  |  | REPETRO-PERMANENTE |
| REGIME_TRIBUTARIO_REPETRO_TEMPORARIO | char(1) |  |  | REPETRO-TEMPORARIO |
| PRECO_TRANSFERENCIA | char(1) |  |  | Opção pelas novas regras de preços de transferência no ano-calendário 2023 |
| POSSUI_CEBAS | char(1) |  |  | Possui número CEBAS (Certificado de Entidade Beneficente de Assistência Social) |
| CEBAS | varchar(255) |  |  | Número CEBAS (Certificado de Entidade Beneficente de Assistência Social) |
| REGIME_TRIBUTARIO_REDATA | char(1) |  |  | REDATA |
