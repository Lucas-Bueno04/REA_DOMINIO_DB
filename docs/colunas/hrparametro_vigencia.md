# HRPARAMETRO_VIGENCIA — Parametro Honorarios - Vigencia
3 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Codigo do escritorio |
| VIGENCIA | date(4) | PK |  | Data de vigencia |
| CONTAS_PAGAR | char(1) |  |  | Contas a pagar S N |
| DIAS_ANTECEDENCIA | integer(4) |  | S | Numero de dias de antecedencia |
| CALCULA_JUROS_RECEBIMENTO | char(1) |  |  | Calcular juros no recebimento S N |
| CALCULA_MULTA_RECEBIMENTO | char(1) |  |  | Calcular multa no recebimento S N |
| NAO_EXIBIR_EVENTO_RECEBIMENTO | char(1) |  |  | Nao exibir a tela de evento no recebimento individual |
| PERCENTUAL_JUROS | numeric(5) |  |  | Percentual de juros |
| PERCENTUAL_MULTA | numeric(5) |  |  | Percentual de multa |
| EMITIR_COMPROVANTE_RECEBIMENTO_INDIVIDUAL | char(1) |  |  | Emitir comprovante no momento do recebimento S N |
| MODELO_RECEBIMENTO_INDIVIDUAL | varchar(80) |  | S | Modelo recebimento individual |
| EMITIR_COMPROVANTE_RECEBIMENTO_GRUPO | char(1) |  |  | Emitir comprovante no momento do recebimento C Cada recebimento U Unico para varios |
| MODELO_RECEBIMENTO_GRUPO | varchar(80) |  | S | Modelo recebimento grupo |
| EMITIR_COMPROVANTE_RECEBIMENTO_ADIANTAMENTO | char(1) |  |  | Emitir comprovante no momento no adiantamento S N |
| MODELO_RECEBIMENTO_ADIANTAMENTO | varchar(80) |  | S | Modelo recebimento adiantamento |
| VALOR_MINIMO_IRRF | numeric(13) |  |  | Valor minimo para retencao do IRRF |
| FATO_GERADOR_IRRF | char(1) |  |  | Fato gerador IRRF R Recebimento E Emissao |
| VALOR_MINIMO_INSS | numeric(13) |  |  | Valor minimo para retencao do INSS |
| VALOR_MINIMO_ISS | numeric(13) |  |  | Valor minimo para retencao do ISS |
| POSSUI_CRF | char(1) |  |  | Possui CRF S N |
| POSSUI_PIS | char(1) |  |  | Possui PIS S N |
| POSSUI_COFINS | char(1) |  |  | Possui COFINS S N |
| POSSUI_CSLL | char(1) |  |  | Possui CSLL S N |
| VALOR_MINIMO_CRF | numeric(13) |  |  | Valor minimo da parcela para calculo da CRF |
| FATO_GERADOR_CRF | char(1) |  |  | Fato gerador CRF R Recebimento E Emissao |
| NAO_FATURAR_VENCIDA | char(1) |  |  | Nao faturar com parcelas vencidas S N |
| QUANTIDADE_PARCELAS_ABERTA | integer(4) |  |  | Quantidade de parcelas em aberta |
| CALCULAR_DESCONTO_ADIMPLENTE | char(1) |  |  | Calcular desconto no contrato para clientes adimplentes S N |
| QUANTIDADE_MESES_ADIMPLENTE | integer(4) |  |  | Quantidade de meses adimplente |
| PERCENTUAL_ADIMPLENTE | numeric(5) |  |  | Percentual adimplente |
| FATURAR_INATIVO | char(1) |  |  | Faturar clientes inativos S N |
| FATURAR_CONSTITUICAO | char(1) |  |  | Faturar clientes em constituicao S N |
| AVISAR_REAJUSTE_VENCIDO | char(1) |  |  | Avisar sobre os reajustes vencidos S N |
| AVISAR_CLIENTE_PARCELA_ABERTA | char(1) |  |  | Avisar se o cliente possuir parcelas em aberto S N |
| NUMERO_PARCELA_ABERTA | integer(4) |  |  | Numero de parcelas em aberto |
| TIPO_VENCIMENTO | tinyint(1) |  |  | Tipo do vencimento 1 Direto 2 Antecipados 3 Adiados 4 Uteis |
| LIMITAR_DIAS_VENCIMENTO | char(1) |  |  | Limitar dias de vencimento S N |
| DIAS_VENCIMENTO | varchar(128) |  |  | Dias para vencimento |
| GERA_LANCAMENTO | char(1) |  |  | Gerar lancamentos contabeis |
| MOSTRAR_BAIXA_RECEBER | char(1) |  |  | Mostrar na baixa de contas a receber individual S N |
| MOSTRAR_LANCAMENTO_PAGAR | char(1) |  |  | Mostrar no lancamento de contas a pagar S N |
| MOSTRAR_BAIXAR_PAGAR | char(1) |  |  | Mostrar na baixa de contas a pagar individual S N |
| MOSTRAR_ADIANTAMENTO | char(1) |  |  | Mostrar no adiantamento S N |
| MOSTRAR_MOVIMENTACAO | char(1) |  |  | Mostrar na movimentacao de contas S N |
| CLIENTE_CRIA_CONTA | char(1) |  |  | Cada cliente gera uma conta S N |
| CLASSIFICACAO_DIFERENTE_CLIENTE | char(1) |  |  | Classificacao diferente para cada conta S N |
| CODIGO_IGUAL_CLIENTE | char(1) |  |  | Codigo do cliente igual ao da conta S N |
| CLASSIFICACAO_CONTA_CLIENTE | varchar(20) |  | S | Classificacao da conta cliente |
| RECEBER_CONTA_MULTA | integer(4) |  |  | Contas a receber conta multa |
| RECEBER_HISTORICO_MULTA | integer(4) |  |  | Contas a receber historico multa |
| RECEBER_CONTA_JUROS | integer(4) |  |  | Contas a receber conta juros |
| RECEBER_HISTORICO_JUROS | integer(4) |  |  | Contas a receber historico juros |
| RECEBER_CONTA_DESCONTO | integer(4) |  |  | Contas a receber conta desconto |
| RECEBER_HISTORICO_DESCONTO | integer(4) |  |  | Contas a receber historico desconto |
| RECEBER_CONTA_ADIANTAMENTO | integer(4) |  |  | Contas a receber conta adiantamento |
| RECEBER_HISTORICO_ADIANTAMENTO | integer(4) |  |  | Contas a receber historico adiantamento |
| RECEBER_HISTORICO_RECEBIMENTO | integer(4) |  |  | Contas a receber historico recebimento |
| PAGAR_CONTA_MULTA | integer(4) |  |  | Contas a pagar conta multa |
| PAGAR_HISTORICO_MULTA | integer(4) |  |  | Contas a pagar historico multa |
| PAGAR_CONTA_JUROS | integer(4) |  |  | Contas a pagar conta juros |
| PAGAR_HISTORICO_JUROS | integer(4) |  |  | Contas a pagar historico juros |
| PAGAR_CONTA_DESCONTO | integer(4) |  |  | Contas a pagar conta desconto |
| PAGAR_HISTORICO_DESCONTO | integer(4) |  |  | Contas a pagar historico desconto |
| PAGAR_HISTORICO_PAGAMENTO | integer(4) |  |  | Contas a pagar historico pagamento |
| CRF_CONTA_COFINS | integer(4) |  |  | CRF conta COFINS |
| CRF_HISTORICO_COFINS | integer(4) |  |  | CRF historico COFINS |
| CRF_CONTA_PIS | integer(4) |  |  | PIS conta COFINS |
| CRF_HISTORICO_PIS | integer(4) |  |  | PIS historico COFINS |
| CRF_CONTA_CSLL | integer(4) |  |  | CSLL conta COFINS |
| CRF_HISTORICO_CSLL | integer(4) |  |  | CSLL historico COFINS |
| IRRF_CONTA | integer(4) |  |  | Conta a recuperar IRRF |
| IRRF_HISTORICO | integer(4) |  |  | Historico IRRF |
| ISS_CONTA_DESPESA | integer(4) |  |  | Conta de despesa ISS |
| ISS_CONTA_RECOLHER | integer(4) |  |  | Conta a recolher ISS |
| ISS_HISTORICO | integer(4) |  |  | Historico de ISS |
| ISSRET_CONTA | integer(4) |  |  | Conta a recuperar de ISS Retido |
| ISSRET_HISTORICO | integer(4) |  |  | Historico de ISS Retido |
| INSSRET_CONTA | integer(4) |  |  | Conta a compensar de INSS Retido |
| INSSRET_HISTORICO | integer(4) |  |  | Historico de INSS Retido |
| EVENTO_FORMULA_MEDIA | tinyint(1) |  |  | Evento com formula considerar a meida do ultimos N meses |
| CONSIDERAR_INADIMPLENCIA | char(1) |  |  | Considerar inadimplencia media S N |
| PERCENTUAL_INADIMPLENCIA | numeric(5) |  |  | Perdentual de inadimplencia media |
| CONSIDERAR_REAJUSTE | char(1) |  |  | Considerar reajuste medio S N |
| PERCENTUAL_REAJUSTE | numeric(5) |  |  | Perdentual de reajuste medio |
| CONSIDERAR_DESCONTO | char(1) |  |  | Considerar desconto de adimplencia media S N |
| PERCENTUAL_DESCONTO | numeric(5) |  |  | Perdentual de desconto de adimplencia media |
| CONSIDERAR_VALOR_ISS_SAIDA | char(1) |  |  | Considerar valor de ISS como saida S N |
| CONSIDERAR_RETENCAO_ENTRADA | char(1) |  |  | Considerar retencoes sobre o faturamento como entrada S N |
| I_CATEGORIA_PAGAR_PROVISAO_PAGAMENTO | integer(4) |  | S | Categoria para pagamento de imposto |
| I_CATEGORIA_PAGAR_IMPOSTO_TERCEIRO | integer(4) |  | S | Categoria para pagamento de impostos de terceiros |
| I_CATEGORIA_PAGAR_PAGAMENTO_FUNCIONARIO | integer(4) |  | S | Categoria para pagamento de funcionarios |
| I_CATEGORIA_RECEBER_ADIANTAMENTO | integer(4) |  | S | Categoria para adiantamento |
| I_CATEGORIA_RECEBER_TRANSFERENCIA_ENTRADA | integer(4) |  | S | Categoria para transferencia entre contas entrada |
| I_CATEGORIA_PAGAR_TRANSFERENCIA_SAIDA | integer(4) |  | S | Categoria para transferencia entre contas saida |
| MODELO_NOTA_FISCAL | char(1) |  |  | Modelo nota fisca (M=Modelo 1/S=Servico/E=Nota Fiscal de Servico Eletronica) |
| NOTA_SERIE | char(7) |  |  | Serie nota fiscal |
| NOTA_SUBSERIE | char(2) |  |  | Sub serie nota fiscal |
| CFOP_ESTADO | integer(4) |  | S | CFOP cliente do estado |
| CFOP_ESTADO_VERSAO | smallint(2) |  | S | CFOP cliente do estado versao |
| CFOP_OUTRO_ESTADO | integer(4) |  | S | CFOP cliente de outro estado |
| CFOP_OUTRO_ESTADO_VERSAO | smallint(2) |  | S | CFOP cliente de outro estado versao |
| CFOP_EXTERIOR | integer(4) |  | S | CFOP cliente do exterior |
| CFOP_EXTERIOR_VERSAO | smallint(2) |  | S | CFOP cliente do exterior versao |
| CFPS_MUNICIPIO | integer(4) |  | S | CFPS do municipio |
| CFPS_OUTRO_MUNICIPIO | integer(4) |  | S | CFPS de outro municipio |
| CFPS_OUTRO_ESTADO | integer(4) |  | S | CFPS de outro estado |
| CFPS_EXTERIOR | integer(4) |  | S | CFPS do exterior |
| GERA_NOTAS_ESCRITA_ENTRADA_FISCAL | char(1) |  |  | Gerar notas de entradas para o modulo Escrita Fiscal S N |
| GERA_NOTAS_ESCRITA_SAIDA_FISCAL | char(1) |  |  | Gerar notas de saidas para o modulo Escrita Fiscal S N |
| GERA_RECEBIMENTO_ESCRITA_FISCAL | char(1) |  |  | Gerar recebimentos para o modulo Escrita Fiscal S N |
| ESPECIE_NOTA_FISCAL | integer(4) |  | S | EspEcie nota fiscal |
| ACUMULADOR_NOTA_FISCAL | integer(4) |  | S | ACUMULADOR NOTA FISCAL (NÃO UTILIZAR ESTA COLUNA) |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| NFSE_SERIE_RPS | char(5) |  | S | Serie da RPS |
| I_SEQUENCIAL_SERVICO_PRESTADO | integer(4) |  | S | Codigo Sequencial do servico prestado |
| NFSE_NATUREZA_OPERACAO | integer(4) |  |  | Natureza da operação (origem de tabela do sistema) |
| NFSE_USA_REGIME_ESPECIAL_TRIB | char(1) |  |  | Usa reginme especial de tributacao (S/N) |
| NFSE_REGIME_ESPECIAL_TRIB | tinyint(1) |  | S | Reginme especial de tributacao |
| NFSE_OPTANTE_SIMPLES_NACIONAL | char(1) |  |  | Optante Simples Nacional (S/N) |
| NFSE_INCENTIVADOR_CULTURAL | char(1) |  |  | Incentivador cultural (S/N) |
| NFSE_INFORMAR_INTERVALO_RPS | char(1) |  |  | Informar intervalo de RPS (S/N) |
| NFSE_MODELO_NOTA_IMPRESSAO | varchar(80) |  |  | Modelo de nota para impressão |
| NFSE_SENHA_CONTRIBUINTE | varchar(100) |  | S | Senha do contribuinte |
| NFSE_MUNICIPIO_PRESTACAO_SERVICO | integer(4) |  | S | Município de prestação do serviço |
| EMPRESA_LANCAMENTO_CONTABIL | integer(4) |  | S | Empresa onde serão gerados os lançamentos contábeis |
| RENEGOCIACAO_CALCULAR_JUROS | char(1) |  |  | Renegociação calcular juros (S/N) |
| RENEGOCIACAO_PERCENTUAL_JUROS | numeric(5) |  | S | Renegociação percentual de juros |
| RENEGOCIACAO_EVENTO_JUROS | integer(4) |  | S | Renegociação evento de juros |
| RENEGOCIACAO_CALCULAR_MULTA | char(1) |  |  | Renegociação calcular multa (S/N) |
| RENEGOCIACAO_PERCENTUAL_MULTA | numeric(5) |  | S | Renegociação percentual de multa |
| RENEGOCIACAO_EVENTO_MULTA | integer(4) |  | S | Renegociação evento de multa |
| NFSE_USUARIO_CONTRIBUINTE | varchar(100) |  | S | Usuário do contribuinte |
| NFSE_DISPOSITIVO_LEGAL | varchar(255) |  | S | Dispositivo legal |
| GERAR_MOVIMENTO_PRODUTO | char(1) |  |  | Gerar movimento de produto (S/N) |
| INFORMAR_PRODUTO | char(1) |  |  | Informar (P=Informar um produto padrÃ£o/ E=Informar um produto para cada evento da nota fiscal) |
| PRODUTO_PADRAO | char(14) |  | S | CÃ³digo do produto padrÃ£o para o movimento de notas de saÃ­da e serviÃ§o |
| NFSE_MODELO | char(1) |  |  | Modelo NFSE (F=Nota fiscal eletrônica de serviço fatura/ S=Nota fiscal eletrônica de serviço simplificado) |
| NFSE_CFPS_MUNICIPIO | integer(4) |  | S | NFSE - CFPS do município |
| NFSE_CFPS_OUTRO_MUNICIPIO | integer(4) |  | S | NFSE - CFPS de outro município |
| NFSE_CFPS_OUTRO_ESTADO | integer(4) |  | S | NFSE - CFPS de outro estado |
| NFSE_CFPS_EXTERIOR | integer(4) |  | S | NFSE - CFPS do exterior |
| NFSE_INFORMACAO_COMPLEMENTAR | varchar(1024) |  |  | NFSE - Informações complementares |
| BLOQUEAR_ACESSO_CLIENTE_INADIMPLENTE | char(1) |  |  | Bloquear o acesso as empresas de clientes inadimplentes nos demais módulos do sistema (S/N) |
| BLOQUEAR_ACESSO_POR_PARCELA | char(1) |  |  | Bloquear acesso aos demais módulos pelo número de parcelas vencidas em aberto (S/N) |
| BLOQUEAR_ACESSO_POR_PARCELA_NRO | integer(4) |  | S | Número de parcelas |
| BLOQUEAR_ACESSO_POR_DIA | char(1) |  |  | Bloquear acesso aos demais módulos pelo número de dias vencidos (S/N) |
| BLOQUEAR_ACESSO_POR_DIA_NRO | integer(4) |  | S | Número de dias |
| BLOQUEAR_ACESSO_EMITIR_AVISO | char(1) |  |  | Emitir aviso informando a data que o cliente será bloqueado por inadimplência na entrada do sistema (S/N) |
| BLOQUEAR_ACESSO_EMITIR_AVISO_NRO | integer(4) |  | S | Número de dias anteriores ao bloqueio |
| NFSE_DATA_ADESAO_SIMPLES_NACIONAL | date(4) |  | S | NFSE - Data de adesão ao Simples Nacional |
| PAGAR_CONTA_IRRF | integer(4) |  |  | Contas a pagar conta IRRF |
| PAGAR_HISTORICO_IRRF | integer(4) |  |  | Contas a pagar historico IRRF |
| PAGAR_CONTA_INSS_RETIDO | integer(4) |  |  | Contas a pagar conta INSS Retido |
| PAGAR_HISTORICO_INSS_RETIDO | integer(4) |  |  | Contas a pagar historico INSS Retido |
| PAGAR_CONTA_ISS_RETIDO | integer(4) |  |  | Contas a pagar conta ISS Retido |
| PAGAR_HISTORICO_ISS_RETIDO | integer(4) |  |  | Contas a pagar historico ISS Retido |
| PAGAR_CONTA_CRF | integer(4) |  |  | Contas a pagar conta CRF |
| PAGAR_HISTORICO_CRF | integer(4) |  |  | Contas a pagar historico CRF |
| NFSE_AEDF | varchar(7) |  | S | NFSE - AEDF |
| NFSE_IDENTIFICARDOR_CNAE | integer(4) |  | S | NFSE - Identificador do CNAE |
| NFSE_NATUREZA_OPERACAO_CADASTRO | integer(4) |  | S | Natureza da operação (origem do cadastro de usuário) |
| NFSE_GERAR_VALOR_APROXIMADO_IBPT | char(1) |  |  | Gerar o valor aproximado dos impostos conforme IBPT na impressão do RPS e da NFS-e (S/N) |
| GERAR_NOTA_EMITIDA_ESCRITORIO_NOTA_ENTRADA | char(1) |  |  | Gerar as notas emitidas pelo escritório como nota de entrada na empresa do cliente (S/N) |
| GERAR_NOTA_EMITIDA_ESCRITORIO_PARCELA_PAGTO | char(1) |  |  | Gerar parcelas e pagamentos para o módulo Escrita Fiscal (S/N) |
| GERAR_VALOR_APROX_IBPT_NOTA_FISCAL | char(1) |  |  | Gerar o valor aproximado dos impostos conforme IBPT na impressão da nota fiscal (S/N) |
| I_ALIQUOTA_IBPT | integer(4) |  | S | Alíquota de impostos IBPT |
| PERMITIR_ALTERAR_LANCTO_EVENTO | char(1) |  |  | Permitir incluir ou alterar o lançamento de eventos em competências já faturadas (S/N) |
| NFSE_CST | integer(4) |  | S | NFSE - CST PARA CLIENTE DO MUNICÍPIO |
| NFSE_AMBIENTE_ENVIO | char(1) |  |  | NFSE - Ambiente de envio |
| NFSE_NUMERO_PROCESSO | varchar(30) |  | S | NFSE - Número do processo |
| NFSE_CHAVE_VALIDACAO | varchar(225) |  | S | NFSE - Chave de validação |
| NFSE_ENVIAR_CANCELAMENTO_PREFEITURA | char(1) |  |  | NFSE - Enviar cancelamento da NFS-e para a prefeitura |
| NFSE_FORMA_RECOLHIMENTO | integer(4) |  | S | NFSE - Forma de recolhimento |
| NFSE_REGIME_TRIBUTARIO | integer(4) |  |  | NFSE - Regime tributário |
| NFSE_INCENTIVADOR_FISCAL | char(1) |  |  | NFSE - Incentivador fiscal |
| NFSE_CFOP_ESTADO | integer(4) |  | S | NFSE - CFOP do estado |
| NFSE_CFOP_ESTADO_VERSAO | smallint(2) |  | S | NFSE - CFOP do estado versão |
| NFSE_CFOP_OUTRO_ESTADO | integer(4) |  | S | NFSE - CFOP de outro estado |
| NFSE_CFOP_OUTRO_ESTADO_VERSAO | smallint(2) |  | S | NFSE - CFOP de outro estado versão |
| NFSE_CFOP_EXTERIOR | integer(4) |  | S | NFSE - CFOP do exterior |
| NFSE_CFOP_EXTERIOR_VERSAO | smallint(2) |  | S | NFSE - CFOP do exterior versão |
| DEDUZIR_VALOR_IRRF_CRF_FATO_GERADOR_RECEBIMENTO | char(1) |  |  | Deduzir o valor do IRRF e CRF do valor a receber quando o fato gerador do imposto for recebimento |
| CONSIDERAR_VENCIMENTO_PARCELA_IRRF_CRF_FATO_GERADOR_RECEBIMENTO | char(1) |  |  | Considerar a data de vencimento da parcela para emitir a guia do IRRF e CRF quando o fato gerador do imposto for recebimento |
| NFSE_DESTACAR_ISS_EMPRESA_OPTANTE_SIMPLES_NACIONAL | char(1) |  |  | Destacar o valor do ISS na impressão da NFS-e em empresa optante pelo Simples Nacional |
| NFSE_ALIQUOTA_IBPT_2014 | numeric(5) |  | S | Alíquota IBPT até 2014 |
| NFSE_ALIQUOTA_IBPT_2015 | numeric(5) |  | S | Alíquota IBPT a partir de 2015 |
| ALIQUOTA_IBPT_2015_NF_IMPRESSA | numeric(5) |  | S | Alíquota IBPT a partir de 2015 - Nota Fiscal Impressa |
| ACUMULADOR_EVENTO_FATURA_CONTRATO | integer(4) |  | S | Eventos que faturam com o contrato |
| ACUMULADOR_EVENTO_NAO_FATURA_CONTRATO | integer(4) |  | S | Eventos que não faturam com o contrato |
| DEFINIR_ACUMULADOR_MUNICIPIO_CLIENTE | char(1) |  |  | Definir acumuladores por município dos clientes |
| CALCULAR_DESCONTO_ADIMPLENTE_CONSIDERAR_PARA | char(1) |  |  | Calcular desconto no contrato para clientes adimplentes - Considerar para |
| RECEBER_CONTA_QUITAR_SEM_RECEBIMENTO | integer(4) |  |  | Contas a receber conta quitar sem recebimento |
| RECEBER_HISTORICO_QUITAR_SEM_RECEBIMENTO | integer(4) |  |  | Contas a receber histórico quitar sem recebimento |
| NFSE_CST_CLIENTE_FORA_MUNICIPIO | integer(4) |  | S | NFSE - CST para cliente de fora do município |
| AVISAR_CONTAS_RECEBER_ATRASO | char(1) |  |  | Emitir avisos na entrada do sistema - Sobre contas a receber em atraso |
| AVISAR_CONTAS_RECEBER_ATRASO_NUMERO_DIAS | integer(4) |  |  | Emitir avisos na entrada do sistema - Sobre contas a receber em atraso - Número de dias em atraso |
| VALOR_MINIMO_RETENCAO_CRF | numeric(13) |  |  | Valor mínimo para retenção do CRF |
| NFSE_FORMA_RECOLHIMENTO_CHAR | char(1) |  |  | NFSE - Forma de recolhimento (N - Não retido / S - Retido dentro do município / F - Retido fora do município / D - Devido fora do município - não retido / I - Sem incidência do ISS) |
| NFSE_ALIQUOTA_SIMPLES_NACIONAL | numeric(7) |  |  | NFSE - Alíquota do Simples Nacional |
| REALIZAR_RETENCAO_ISS_TOMADOR_MESMO_MUNICIPIO_PRESTADOR | char(1) |  |  | Realizar a retenção de ISS apenas para tomador localizado no mesmo município do prestador de serviço |
| NFSE_SERVICO_SIMPLES_NACIONAL | integer(4) |  | S | Serviço do Simples Nacional(Código do Serviço Prestado) |
| NFSE_INFORMAR_INTERVALO_LOTE | char(1) |  |  | Informar intervalo de Lote (S/N) |
| NFSE_REALIZAR_INTEGRACAO_NFE_ESCRITA_EM | integer(4) |  |  | Realizar a integração da NF-e na Escrita Fiscal em (1 - Notas de serviço / 2 - Notas de saída) |
| NFSE_TIPO_ENDERECO_PRESTACAO_SERVICO | tinyint(1) |  |  | Tipo de endereço da prestação do serviço |
| NFSE_ENDERECO_PRESTACAO_SERVICO | varchar(40) |  | S | Endereço da prestação do serviço |
| NFSE_NUMERO_PRESTACAO_SERVICO | integer(4) |  | S | Número do endereço da prestação do serviço |
| NFSE_BAIRRO_PRESTACAO_SERVICO | varchar(60) |  | S | Bairro da prestação do serviço |
| NFSE_COMPLEMENTO_PRESTACAO_SERVICO | varchar(30) |  | S | Complemento da prestação do serviço |
| NFSE_UF_PRESTACAO_SERVICO | char(2) |  | S | UF da prestação do serviço |
| NFSE_CEP_PRESTACAO_SERVICO | char(8) |  | S | CEP da prestação do serviço |
| NFSE_GERAR_ALIQUOTA_ISS_NOTAS_SEM_ALIQUOTA_INFORMADA | char(1) |  | S | Gerar a alíquota do ISS na geração do RPS para as notas que não possuem alíquota informada no evento |
| NFSE_ALIQUOTA_NOTAS_SEM_ALIQUOTA_INFORMADA | numeric(5) |  | S | Aliquota a gerar para notas que não possuem aliquota informada no evento |
| FATURAR_PROCESSO_BAIXA | char(1) |  |  | Faturar clientes em processo de baixa S N |
| NFSE_BENEFICIO_PROCESSO | varchar(100) |  | S | Beneficio do processo |
| NFSE_RESPONSAVEL_RETENCAO | integer(4) |  | S | Responsável retenção ISSQN(1-Tomador, 2=Intermediário, 3=Prestador) |
| NFSE_OPTANTE_SIMEI | char(1) |  |  | Optante SIMEI |
| NFSE_CLIENTE_ID | varchar(60) |  | S | Cliente ID para envio NFSE. |
| NFSE_USA_CNAE_ESPECIFICO_PREFEITURA | char(1) |  |  | Usa CNAE Específico prefeitura(S/N) |
| NFSE_CNAE_ESPECIFICO_PREFEITURA | char(15) |  | S | CNAE Específico prefeitura. |
| NFSE_RECEITA_BRUTA_ACUMULADA_SIMPLES_NACIONAL | numeric(14) |  | S | Receita bruta acumulada simples nacional |
| NFSE_ANEXO_TABELA_SIMPLES_NACIONAL | varchar(30) |  | S | Anexo tabela simples nacional |
| NFSE_DATA_INICIO_ATIVIDADE_SIMPLES_NACIONAL | date(4) |  | S | Data de inicio atividade simples nacional |
| NFSE_REGRA_ARREDONDAMENTO | integer(4) |  |  | 1 - "Matemático"/2 - "ABNT/NBR 5891" |
| CALCULAR_RETENCOES_FEDERAIS_CLIENTES_SIMPLES_NACIONAL | char(1) |  |  | Realiza calculo de retenções federais (IRRF, Retenções na Fonte(CRF) e INSS Retido) para clientes do simples nacional |
| FATURAMENTO_CALCULAR_SEIS_CASAS_DECIMAIS_ISS | char(1) |  |  | Considerar o valor do iss 6 digitos após a vírgula |
| NFSE_FRASE_SECRETA | varchar(100) |  | S | Frase secreta NFSE. |
| CALCULAR_RETENCOES_FEDERAIS_CLIENTES_SIMPLES_NACIONAL_IRRF | char(1) |  |  | Calcula retencões federais quando o cliente for simples nacional para o imposto IRRF |
| CALCULAR_RETENCOES_FEDERAIS_CLIENTES_SIMPLES_NACIONAL_INSS_RETIDO | char(1) |  |  | Calcula retencões federais quando o cliente for simples nacional para o imposto INSS RETIDO |
| CALCULAR_RETENCOES_FEDERAIS_CLIENTES_SIMPLES_NACIONAL_CRF | char(1) |  |  | Calcula retencões federais quando o cliente for simples nacional para o imposto CRF |
| CALCULAR_RETENCOES_FEDERAIS_CLIENTES_SIMPLES_NACIONAL_ISS_RETIDO | char(1) |  |  | Calcula retencões federais quando o cliente for simples nacional para o imposto ISS RETIDO |
| DETALHAR_CATEGORIA_PAGAR_PROVISAO_PAGAMENTO | char(1) |  |  | Detalhar por imposto/encargo pagamento de impostos e encargos |
| NFSE_POSSUI_FONTE_TRIBUTACAO | char(1) |  |  | Caso o município possua fonte de tributação |
| NFSE_FONTE_TRIBUTACAO | char(1) |  | S | Qual a fonte de tributação |
| NFSE_CODIGO_DISTRITO | integer(4) |  | S | Codigo de Distrito |
| ANEXO_SIMPLES_NACIONAL | varchar(50) |  | S | Anexo simples nacional |
| RECEITA_BRUTA_SIMPLES_NACIONAL | numeric(13) |  | S | Receita dupla simples nacional |
| ABRIR_PDF_AUTOMATICAMENTE | char(1) |  | S | Abrur PDF |
| NFSE_MODALIDADE_FRETE | integer(4) |  | S | Modalidade de frete |
| NFSE_TIPO_RECOLHIMENTO | integer(4) |  | S | Tipo de Recolhimento |
| INUTILIZAR_NUMERO_RPS_EXCLUIDO | char(1) |  | S | Coluna criada para verificar se o sistema vai inutilzar rps excluído |
| MOSTRAR_DESCONTO_MENSAL | char(1) |  |  | Mostrar desconto mensal |
| GERAR_ISS_ZERADO_EMISSAO_NFSE | char(1) |  |  | Gerar iss zerado nos xml |
| DEDUZIR_VALOR_ISS_BASE_CALCULO_CRF | char(1) |  |  | Deduzir o valor do ISS da base de cálculo do CRF |
| NFSE_ARQUIVO_AIDF | varchar(255) |  | S | Arquivo AIDF |
| CODIGO_NBS | varchar(10) |  | S | Código NBS - NFSE Nacional |
| NFSE_SERIE_DPS | char(5) |  | S | Serie da DPS |
| NFSE_NACIONAL_AMBIENTE_ENVIO | char(1) |  | S | NFSE Nacional- Ambiente de envio |
| NFSE_INFORMAR_INTERVALO_DPS | char(1) |  |  | Informar intervalo de DPS (S/N) |
| NFSE_INFORMAR_INTERVALO_LOTE_DPS | char(1) |  |  | Informar intervalo de Lote DPS (S/N) |
| INUTILIZAR_NUMERO_DPS_EXCLUIDO | char(1) |  | S | Coluna criada para verificar se o sistema vai inutilzar dps excluído |
| CODIGO_INTERNO_CONTRIBUINTE | varchar(25) |  | S | Código Interno Contribuinte - NFSE Nacional |
| NFSE_REGIME_ESPECIAL_SIMPLES_NAC | integer(4) |  | S | 1 Regime federais e municipal / 2 Regime federais pelo SN e ISSQN / 3 Regime federais pela NFS-e |
| NFSE_OPCAO_OPTANTE_SIMPLES_NACIONAL | integer(4) |  | S | 1 Não Optante / 2 Optante - MEI / 3 Optante - ME-EPP |
| NFSE_NACIONAL_REGIME_ESPECIAL_TRIBUTACAO | integer(4) |  | S | 0 - Nenhum / 1 - Ato Cooperado (Cooperativa) / 2 - Estimativa / 3 - Microempresa Municipal / 4 - Notário ou Registrador / 5 - Profissional Autônomo / 6 - Sociedade de Profissionais |
| NFSE_NACIONAL_MUNICIPIO_PRESTACAO_SERVICO | integer(4) |  | S | Municipio da tributacao nacional do nfse nacional |
| I_SEQUENCIAL_TRIBUTACAO_NACIONAL | integer(4) |  | S | Codigo Sequencial da tributação nacional |
| NFSE_NACIONAL_GERAR_VALOR_APROXIMADO_IBPT | char(1) |  |  | Gerar o valor aproximado dos impostos conforme IBPT na impressão do RPS e da NFS-e (S/N) |
| CST_MODELO_NACIONAL | integer(4) |  | S | Coluna criada para gravar a CST do modelo nacional |
| NFSE_NAO_POSSUI_BENEFICIO_ISS_FIXO | char(1) |  |  | Não possui benefício de ISS Fixo |
| NFSE_POSSUI_MAIS_DE_UM_CONTADOR | char(1) |  |  | Possui mais de um contador responsavel |
| NFSE_DESTACAR_ISS_FIXO_IMPRESSAO_NFSE | char(1) |  |  | Destacar valor do ISS Fixo na impressão da NFS-e |
| NFSE_ISENCAO_IMPOSTO_RETIDO | char(1) |  |  | Isenção do Imposto Retido |
| RENEGOCIACAO_TERMO_CONFISSAO_DIVIDA | char(1) |  |  | Emitir termo de confissão de dívida no momento da renegociação (S/N) |
| NFSE_CODIGO_NBS | varchar(15) |  | S | Código NBS da NFS-e |
| IBS_CBS_CCLASS_TRIB | varchar(6) |  | S | Classificação Tributária IBS/CBS |
| IBS_CBS_CST | varchar(6) |  | S | CST IBS/CBS |
| IBS_ALIQUOTA | numeric(5) |  | S | Alíquota IBS |
| IBS_REDUCAO | numeric(5) |  | S | Redução IBS |
| IBS_CBS_ALIQ_PIS | numeric(5) |  | S | Alíquota PIS para dedução IBS/CBS |
| IBS_CBS_ALIQ_COFINS | numeric(5) |  | S | Alíquota COFINS para dedução IBS/CBS |
| CBS_ALIQUOTA | numeric(5) |  | S | Alíquota CBS |
| CBS_REDUCAO | numeric(5) |  | S | Redução CBS |
| IBS_CONTA_DESPESA | bigint(8) |  | S | Conta contábil de despesa IBS |
| IBS_CONTA_RECOLHER | bigint(8) |  | S | Conta contábil a recolher IBS |
| IBS_HISTORICO | integer(4) |  | S | Histórico padrão IBS |
| CBS_CONTA_DESPESA | bigint(8) |  | S | Conta contábil de despesa CBS |
| CBS_CONTA_RECOLHER | bigint(8) |  | S | Conta contábil a recolher CBS |
| CBS_HISTORICO | integer(4) |  | S | Histórico padrão CBS |
| NFSE_ISS_FIXO | char(1) |  |  | NFSE - ISS Fixo(S/N) |
| NFSE_NATUREZA_OPERACAO_TECNOSPEED | integer(4) |  | S | Natureza da Operação do fornecedor Tecnospeed. |
| NFSE_REGIME_TRIBUTARIO_TECNOSPEED | integer(4) |  | S | Regime tributário do fornecedor Tecnospeed |
| NFSE_TIPO_TRIBUTACAO_TECNOSPEED | integer(4) |  |  | Tipo de Tributação do fornecedor Tecnospeed |
| IBS_CBS_CCLASS_TRIB_REGULAR | varchar(6) |  | S | Classificação Tributária Regular IBS/CBS |
| IBS_CBS_CST_REGULAR | varchar(6) |  | S | CST Regular IBS/CBS |
| IBS_CBS_INDICADOR_OPERACAO | varchar(6) |  | S | Indicador de Operação IBS/CBS |
| PERCENTUAL_DIFERIMENTO_IBS_ESTADUAL | numeric(15) |  | S | Percentual diferimento IBS Estadual |
| PERCENTUAL_DIFERIMENTO_IBS_MUNICIPAL | numeric(15) |  | S | Percentual diferimento IBS Municipal |
| PERCENTUAL_DIFERIMENTO_CBS | numeric(15) |  | S | Percentual diferimento CBS |
| NFSE_ENVIAR_VALORES_IBS_CBS | char(1) |  |  | Enviar valores do IBS/CBS para o fornecedor Tecnospeed (S/N) |
| NFSE_CONSIDERAR_SERIE_DPS_RPS | char(1) |  |  | Considerar a serie para gerar número do RPS ou DPS. |
| NFSE_CODIGO_SERVICO_NACIONAL | varchar(20) |  | S | Código de Serviço Nacional (Tecnospeed) |
| NFSE_REGIME_APURACAO_TRIBUTARIA | integer(4) |  |  | Regime de apuração tributária (Tecnospeed) |
| IBS_ALIQUOTA_INDIVIDUAL_ESTADUAL | numeric(15) |  | S | Alíquota Individual IBS Estadual |
| IBS_ALIQUOTA_INDIVIDUAL_MUNICIPAL | numeric(15) |  | S | Alíquota Individual IBS Municipal |
| CBS_ALIQUOTA_INDIVIDUAL | numeric(15) |  | S | Alíquota Individual CBS |
| NFSE_TIPO_TRIBUTACAO_ISSQN | integer(4) |  |  | 1-Operação Tributável / 2-Imunidade (CF88, Art 150, VI, "a") / 3-Imunidade (CF88, Art 150, VI, "b") / 4-Imunidade (CF88, Art 150, VI, "c") / 5-Imunidade (CF88, Art 150, VI, "d") / 6-Imunidade (CF88, Art 150, VI, "e") / 7-Não Incidência |
| NFSE_CODIGO_INTERNO_CONTRIBUINTE | varchar(20) |  | S | Código interno do contribuinte (Tecnospeed) |
| NFSE_EXIGIBILIDADE_ISS_TECNOSPEED | integer(4) |  | S | Exigibilidade ISS do fornecedor Tecnospeed. |
| NFSE_ANEXO_SIMPLES_NACIONAL_CONAM | integer(4) |  | S | Anexo do Simples Nacional para o fornecedor CONAM. |
| NFSE_DATA_VIGENCIA_SIMPLES_NACIONAL | date(4) |  | S | Data de vigencia do Simples Nacional. |
| NFSE_RESPONSAVEL_RETENCAO_TECNOSPEED | bit(1) |  |  | Tomador responsavel pelo recolhimento do ISSQN para Tecnospeed (0=Nao, 1=Sim) |
| CST_MODELO_TECNOSPEED | integer(4) |  | S | CST PIS/COFINS para modelo Tecnospeed |
| NFSE_REGRA_ARREDONDAMENTO_ISS | integer(4) |  |  | Regra de arredondamento para calculo do ISS (1=Matematico, 2=ABNT/NBR 5891, 3=Round) |
| MUNICIPIO_INCIDENCIA_IBS_CBS | char(1) |  |  | A = Automático, P = Prestador, T = Tomador |
| NFSE_NACIONAL_SUSPENSAO_EXIGIBILIDADE_ISSQN | integer(4) |  |  | NFS-e Padrão Nacional (DPS): suspensão da exigibilidade do ISSQN. 0=Nenhum, 1=Decisão judicial, 2=Processo administrativo. |
| NFSE_NACIONAL_NUMERO_PROCESSO_SUSPENSAO | varchar(30) |  | S | NFS-e Padrão Nacional (DPS): número do processo de suspensão da exigibilidade do ISSQN. |
