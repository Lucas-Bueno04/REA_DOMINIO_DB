# EFACUMULADOR_VIGENCIA_IMPOSTOS — Acumuladores - Cadastro - Impostos
896.703 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_ACU | integer(4) | PK |  | Acumulador |
| VIGENCIA_ACU | date(4) | PK |  | Vigencia |
| CODI_IMP | integer(4) | PK |  | Imposto |
| ALBC_IAC | numeric(7) |  |  | Aliquota da Base de Calculo |
| CODREC_PADRAO_IAC | char(6) |  | S | Codigo de recolhimento padrao do imposto |
| ORIGEM_REG | integer(4) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| DIFERENCA_IAC | integer(4) |  |  | Diferenca da base de calculo com valor contabil lancar em (1-Isentas/2-Outras/3-Nao lancar/4-IPI/5-SUBTRI/6-Nao tributadas/7-parcela reduzida) |
| REDUCAO_IAC | numeric(6) |  | S | Percentual de reducao do imposto |
| REDUZ_IMPOSTO_IAC | char(1) |  | S | Reduz valor do imposto(S/N) |
| CALCULO_REDUCAO_IAC | char(1) |  | S | Forma de calculo da reducao(N - Lancamento da nota / A - Estorno na apuracao) |
| SIMPLESN_ANEXO_IAC | integer(4) |  | S | Simples Nacional - Anexo |
| SIMPLESN_SECAO_IAC | integer(4) |  | S | Simples Nacional - Secao |
| SIMPLESN_TABELA_IAC | integer(4) |  | S | Simples Nacional - Tabela |
| SIMPLESN_IRPJ_IAC | char(1) |  | S | SIMPLES NACIONAL - SITUACAO IRPJ(0/1/2/3/4/5/6/I/R/A/B/"") |
| SIMPLESN_CSLL_IAC | char(1) |  | S | SIMPLES NACIONAL - SITUACAO CSLL(0/1/2/3/4/5/6/I/R/A/B/"") |
| SIMPLESN_COFINS_IAC | char(1) |  | S | SIMPLES NACIONAL - SITUACAO COFINS(0/1/2/3/4/5/6/I/R/A/B/"") |
| SIMPLESN_PIS_IAC | char(1) |  | S | SIMPLES NACIONAL - SITUACAO PIS(0/1/2/3/4/5/6/I/R/A/B/"") |
| SIMPLESN_INSS_IAC | char(1) |  | S | SIMPLES NACIONAL - SITUACAO INSS(0/1/2/3/4/5/6/I/R/A/B/"") |
| SIMPLESN_IPI_IAC | char(1) |  | S | SIMPLES NACIONAL - SITUACAO IPI(0/1/2/3/4/5/6/I/R/A/B/"") |
| SIMPLESN_ICMS_IAC | char(1) |  | S | SIMPLES NACIONAL - SITUACAO ICMS(0/1/2/3/4/5/6/I/R/A/B/"") |
| SIMPLESN_ISS_IAC | char(1) |  | S | SIMPLES NACIONAL - SITUACAO ISS(0/1/2/3/4/5/6/I/R/A/B/"") |
| SIMPLESN_ARBC_ICMS_IAC | numeric(5) |  | S | Aliquota de reducao da base de calculo do ICMS |
| SIMPLESN_ARBC_ISS_IAC | numeric(5) |  | S | Aliquota de reducao da base de calculo do ISS |
| RESPONSAVEL_FETHAB_IAC | char(1) |  | S | Responsavel pelo recolhimento FETHAB (C - Cliente/ E - Empresa) |
| MODALIDADE_OPERACAO_IAC | integer(4) |  | S | Modalidade da importacao(1 - Com direito a credito/2 - Compensacao/3 - Regime especial/4 - Sem direito a credito) |
| DEBITO_ESPECIAL_SPED_IAC | char(1) |  |  | Gerar débito especial para o SPED (S/N) |
| CODIGO_DEBITO_IAC | char(10) |  |  | Código do débito especial |
| DESCRICAO_DEBITO_IAC | char(255) |  |  | Descrição do débito especial |
| SIMPLESN_UTILIZAR_ARBC_MUNICIPAL_IAC | char(1) |  | S | Utilizar a redução da Base de cálculo da tabela alíquota Municipal(S/N) |
| DACON_LANCAMENTO_OUTRAS_RECEITAS_IAC | char(1) |  |  | Lançamento de outras receitas sem valor de imposto (C=Conforme o CFOP / E=Especificar) |
| DACON_TIPO_RECEITA_IAC | integer(4) |  |  | Tipo de receita |
| DACON_GERAR_TIPO_BASE_CREDITO_IAC | char(1) |  |  | Gerar o tipo da base do crédito (C=Conforme o CFOP / E=Especificar) |
| DACON_TIPO_BASE_CREDITO_IAC | integer(4) |  |  | Tipo da base do crédito |
| DETALHAR_OUTRAS_ICMS_IAC | char(1) |  |  | Detalhar o valor do campo outras de ICMS(S/N) |
| I_RECOLHIMENTO | integer(4) |  | S | Sequencial do código de recolhimento |
| SIMPLESN_ARBC_PIS_IAC | numeric(13) |  |  | Simples Nacional - Alíquota de Redução de Base de Cálculo do PIS |
| SIMPLESN_ARBC_COFINS_IAC | numeric(13) |  |  | Simples Nacional - Alíquota de Redução de Base de Cálculo do COFINS |
| DEDUZIR_VALOR_SUBTRI_ICMS_ANTECIPACAO_TOTAL_ST_IAC | char(1) |  |  | Deduzir o valor de ST do imposto ST/AT |
| DEDUZIR_VALOR_DO_IPID_BASE_RECALI | char(1) |  |  | Deduzir o valor do imposto IPI da base de cálculo |
| SIMPLESN_TROCA_AUTOMATICA_DE_ANEXO_IAC | char(1) |  |  | Efetuar a troca automática para os anexos III ou V quando o fator r for igual/superior ou inferior a 28%, conforme LC 123/2006, art. 18, §5º-J e §5º-M |
| SOMAR_VALOR_DO_IPI_NO_VALOR_ICMS_ORIGEM | char(1) |  |  | Somar o IPI no cálculo do valor do ICMS origem |
| SIMPLESN_UTILIZAR_ARBC_ICMS_IAC | char(1) |  |  | Aplicar a redução da base de cálculo para o ICMS |
| SOMAR_VALOR_DO_IPI_BASE_CALCULO | char(1) |  |  | Somar o valor do imposto IPI na base de cálculo |
| UTILIZAR_VALOR_PRODUTO_COMO_BASE_CALCULO | char(1) |  |  | Utilizar valor do produto como base de cálculo |
| DEDUZIR_VALOR_DO_IPI_BASE_CALCULO | char(1) |  |  | Dedzuir valor do IPI base de Calculo (S/N) |
| MT_BASE_CALCULO_OPERACOES_SAIDA_FEEF_IAC | char(1) |  |  | Base de cálculo nas operações de saída FEEF |
| CODI_NAT_RENDIMENTO | integer(4) |  | S | Código da Natureza de Rendimento |
| SIMPLESN_SERVICOS_702_705 | char(1) |  |  | Serviços relacionados nos subitens 7.02 e 7.05 da lista anexa à LC 116/2003 |
| SIMPLESN_ALIQUOTA_MUNICIPAL_PATO_BRANCO | char(1) |  |  | Simples Nacional - Alíquota municipal - Pato Branco |
| SIMPLESN_ALIQUOTA_MUNICIPAL_PATO_BRANCO_ALIQUOTA | numeric(5) |  |  | Simples Nacional - Alíquota municipal - Pato Branco Aliquota |
| CALCULAR_PIS_COFINS_NA_IMPORTACAO_DE | char(1) |  | S | Calcular PIS e COFINS na importação de (S - Serviço / B - Bens) |
| RECOLHIMENTO_ADICIONAL_DE_RETENCAO_CFE_LEI_9711_98 | char(1) |  |  | Não recolhe adicional de retenção cfe Lei 9.711/98 |
| SIMPLESN_CONSIDERAR_VALOR_FRETE_TRIBUTADO_PELO_ICMS | char(1) |  |  | Considerar o valor de frete como tributado pelo ICMS |
| TIPO_ISENCAO | integer(4) |  | S | Tipo de isenção para rendimentos isentos |
| DESCRICAO_ISENCAO | varchar(100) |  | S | Descrição de isenção para rendimentos isentos |
| OPERACAO_AQUISICAO_INTEREST_NAO_TRIBUTADA_ICMS | char(1) |  |  | Operação de aquisição interestadual não tributada pelo ICMS na origem |
