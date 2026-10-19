# PMBEM — Bens
4.353 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_BEM | numeric(16) | PK |  | Código |
| IDENTIFICADOR | varchar(60) |  |  | Identificaor |
| NOME | varchar(100) |  |  | Nome |
| DATA_AQUISICAO | date(4) |  |  | Data da aquisição |
| DATA_BAIXA | date(4) |  | S | Data da baixa |
| I_CONTA_PATRIMONIAL | integer(4) |  |  | Conta patrimonial |
| I_CENTRO_CUSTO | integer(4) |  |  | Centro de custo |
| HISTORICO | varchar(512) |  |  | Histórico |
| TIPO | char(1) |  |  | Tipo (B=Bem adquirido/ C=Componente adquirido/ E=Bem transferido /O=Componente transferido) |
| CLASSIFICACAO | char(1) |  |  | Classificação (I=Bem individual/ R=Bem Resultante/ A=Imobilizado em Andamento/ C=Imobilizado concluído) |
| I_BEM_VINCULADO | numeric(16) |  | S | Vinculado a |
| ORIUNDO_ATIVO_CIRCULANTE | char(1) |  |  | Oriundo do ativo circulante (S/N) |
| FUNCAO | varchar(512) |  |  | Função |
| VALOR_AQUISICAO | numeric(13) |  |  | Valor aquisicição |
| ALIQUOTA_ICMS | numeric(5) |  |  | Alíquota ICMS |
| VALOR_ICMS | numeric(13) |  |  | Valor ICMS |
| VALOR_ICMS_ST | numeric(13) |  |  | Valor ICMS - Substituição Tributária |
| VALOR_ICMS_DIFALI | numeric(13) |  |  | Valor ICMS - Diferencial Alíquota |
| VALOR_ICMS_FRETE | numeric(13) |  |  | Valor ICMS sobre frete |
| VALOR_TOTAL_CREDITO_ICMS | numeric(13) |  |  | Valor total do Crédito do ICMS |
| ALIQUOTA_PIS | numeric(5) |  |  | Alíquota PIS |
| VALOR_CREDITO_PIS | numeric(13) |  |  | Valor do crédito do PIS |
| ALIQUOTA_COFINS | numeric(5) |  |  | Alíquota COFINS |
| VALOR_CREDITO_COFINS | numeric(13) |  |  | Valor do crédito do COFINS |
| VALOR_ORIGINAL | numeric(13) |  |  | Valor original |
| VALOR_CORRECAO_MONETARIA_ACUMULADA | numeric(13) |  |  | Correção monetárioa acumulada |
| VALOR_RESIDUAL | numeric(13) |  |  | Valor residual |
| BASE_CALCULO_DEPRECIACAO | numeric(13) |  |  | Base de cálculo da depreciação |
| CALCULAR_CREDITO_ICMS | char(1) |  |  | Calcular crédito de ICMS (S/N) |
| CALCULAR_CREDITO_PISCOFINS | char(1) |  |  | Calcular crédito de PIS e COFINS (S/N) |
| DEPRECIAR | char(1) |  |  | Depreciar bem (S/N) |
| CALCULO_FISCAL_DEPRECIAR_100_INICIO | char(1) |  |  | Cálculo Fiscal - Depreciar 100% no mês de início da depreciação (S/N) |
| CALCULO_FISCAL_DATA_INICIO | date(4) |  |  | Cálculo Fiscal - Data início |
| CALCULO_FISCAL_INFORMAR_DEPRECIACAO_ATE | char(1) |  |  | Cálculo Fiscal - Informar depreciação acumulada até (S/N) |
| CALCULO_FISCAL_DEPRECIACAO_ATE | date(4) |  | S | Cálculo Fiscal - Depreciação acumulada até |
| CALCULO_FISCAL_VALOR_DEPRECIACAO | numeric(13) |  |  | Cálculo Fiscal - Valor da depreciação acumulada |
| CALCULO_FISCAL_TAXA_ALTERNATIVA | numeric(7) |  |  | Cálculo Fiscal - Taxa alternativa |
| CALCULO_SOCIETARIA_DATA_INICIO | date(4) |  |  | Cálculo Societário - Data início |
| CALCULO_SOCIETARIA_INFORMAR_DEPRECIACAO_ATE | char(1) |  |  | Cálculo Societário - Informar depreciação acumulada até (S/N) |
| CALCULO_SOCIETARIA_DEPRECIACAO_ATE | date(4) |  | S | Cálculo Societário - Depreciação acumulada até |
| CALCULO_SOCIETARIA_VALOR_DEPRECIACAO | numeric(13) |  |  | Cálculo Societário - Valor da depreciação acumulada |
| CALCULO_SOCIETARIA_TAXA_INICIAL | numeric(7) |  |  | Cálculo Societário - Taxa inicial |
| FISCAL_NUMERO | numeric(15) |  | S | Documento fiscal - Número |
| FISCAL_SERIE | char(7) |  | S | Documento fiscal - Série |
| FISCAL_DATA_EMISSAO | date(4) |  | S | Documento fiscal - Data de emissão |
| FISCAL_MODELO | integer(4) |  | S | Documento fiscal - Espécie |
| FISCAL_CHAVE_NFE | char(44) |  | S | Documento fiscal - Chave NFe |
| FISCAL_CODI_FOR | integer(4) |  | S | Documento fiscal - Fornecedor |
| FISCAL_EMITENTE | char(1) |  | S | Documento fiscal - Emitente (T=Terceiros/ P=Próprio) |
| FISCAL_CODI_PDI | char(14) |  | S | Documento fiscal - Produto |
| FISCAL_SEQUENCIAL_ITEM | integer(4) |  | S | Documento fiscal - Sequencial do ítem |
| APROPRIAR_CREDITO_BEM_RESULTANTE | char(1) |  |  | Apropriar crédito somente no bem resultante (S/N) |
| CREDITO_ICMS_PRO_CARGAS | char(1) |  |  | Crédito de ICMS Pró Cargas (S/N) |
| PRODUZIDO_ADQUIRIDO_ESTADO | char(1) |  |  | Bem produzido e qdquirido no Estado com apropriação do crédito de ICMS em 1/42 ou 1/36 conforme Decreto 49.382/2012 (S/N) |
| CREDITO_ICMS_MES_INICIO_EFETIVO | char(1) |  |  | Utilizar o crédito de ICMS no mês de início efetivo das atividades (S/N) |
| CREDITO_ICMS_MES_INICIO_EFETIVO_INICIO | date(4) |  | S | Mês de início efetivo de suas atividades |
| DEBITO_ICMS_OPERACAO_IMPORTACAO | char(1) |  |  | Recolher o débito do ICMS deste bem em 1/48 - Operações de importação (S/N) |
| PIS_COFINS_CALCULAR_BASE_DEPRECIACAO | char(1) |  |  | PIS e COFINS - Calcular com base nos encargos de depreciação (S/N) |
| PIS_COFINS_CALCULAR_BASE_AQUISICAO | char(1) |  |  | PIS e COFINS - Calcular com base no valor de aquisição (S/N) |
| PIS_COFINS_INICIO_CALCULO | date(4) |  | S | PIS e COFINS - Início do cálculo |
| PIS_COFINS_ORIGEM_BEM | char(1) |  | S | PIS e COFINS - Origem do bem (N=Nacional/ I=Importado) |
| PIS_COFINS_BASE_CREDITO | tinyint(1) |  | S | PIS e COFINS - Base do crédito |
| PIS_COFINS_ESPECIE | tinyint(1) |  | S | PIS e COFINS - Espécie (1=Edificações e Benfeitorias em Imóveis Próprios/ 2=Edificações e Benfeitorias em Imóveis de Terceiros/ 3=Instalações/ 4=Máquinas/ 5=Equipamentos/ 6=Veículos/ 99=Outras Situações) |
| PIS_COFINS_TIPO_UTILIZACAO | tinyint(1) |  | S | PIS e COFINS - Tipo utilizado (1=Produção de Bens Destinados a Venda/ 2=Prestação de Serviços/ 3=Locação a Terceiros/ 9=Outros) |
| PIS_COFINS_BASE_CALCULO | numeric(13) |  | S | PIS e COFINS - Base de cálculo |
| PIS_COFINS_PERIODO_CALCULO | integer(4) |  | S | PIS e COFINS - Período de cáclulo |
| PIS_COFINS_CST | integer(4) |  | S | PIS e COFINS - CST |
| PIS_COFINS_VINCULO_CREDITO | char(1) |  | S | PIS e COFINS - Vínculo do crédito (N=Crédito vinculado somente as receitas Não Cumulativas/ C=Crédito vinculado as receitas Cumulativas e Não Cumulativas) |
| PIS_COFINS_DESCRICAO_COMPLEMENTAR | varchar(80) |  | S | PIS e COFINS - Descrição complementar |
| PIS_COFINS_PROCESSO_REFERENCIADO | char(1) |  |  | PIS e COFINS - Possui processo referenciado (S/N) |
| PIS_COFINS_IDENTIFICACAO | varchar(15) |  | S | PIS e COFINS - Identificação |
| PIS_COFINS_ORIGEM_PROCESSO | char(1) |  | S | PIS e COFINS - Origem (J=Justiça Federal/ S=Secex/SRF/ O=Outros) |
| PIS_COFINS_SECAO_JUDICIARIA | varchar(255) |  | S | PIS e COFINS - Seção judiciária |
| PIS_COFINS_VARA | char(2) |  | S | PIS e COFINS - Vara |
| PIS_COFINS_NATUREZA_ACAO | tinyint(1) |  | S | Natureza da ação (1=Decisão judicial transitada em julgado, a favor da pessoa jurídica/Processo Administrativo de Consulta/ 2=Decisão judicial não transitada em julgado, a favor da pessoa jurídica/Despacho Decisório/ 3=Decisão judicial oriunda de liminar em mandado de segurança/Ato Declaratório Executivo/ 4=Decisão judicial oriunda de liminar em medida cautelar/Ato Declaratório Interpretativo/ 5=Decisão judicial oriunda de antecipação de tutela/Decisão Administrativa de DRJ ou do CARF/ 6=Decisão judicial vi |
| PIS_COFINS_DATA_SENTENCA_DESPACHO | date(4) |  | S | PIS e COFINS - Data da sentença ou despacho |
| PIS_COFINS_DESCRICAO_PROCESSO | varchar(100) |  | S | PIS e COFINS - Descrição do processo |
| DATA_CADASTRO | date(4) |  |  | Data de cadastro do bem |
| QUANTIDADE_PARCELAS_DEPRECIACAO_SOCIETARIA | integer(4) |  | S | Quantidade de parcelas para cálculo de depreciação societária |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| DEBITO_ICMS_OPERACAO_IMPORTACAO_PERIODO | tinyint(1) |  |  | Período de cálculo |
| QUANTIDADE | numeric(12) |  |  | Quantidade de Bens |
| FISCAL_CT_NUMERO | numeric(15) |  | S | Documento fiscal - Conhecimento de transporte - Número |
| FISCAL_CT_SERIE | char(7) |  | S | Documento fiscal - Série |
| FISCAL_CT_DATA_EMISSAO | date(4) |  | S | Documento fiscal - Data de emissão |
| FISCAL_CT_MODELO | integer(4) |  | S | Documento fiscal - Espécie |
| FISCAL_CT_EMITENTE | char(1) |  | S | Documento fiscal - Emitente (T=Terceiros/ P=Próprio) |
| FISCAL_CT_CHAVE_NFE | char(44) |  | S | Documento fiscal - Chave NFe |
| FISCAL_CT_CODI_FOR | integer(4) |  | S | Documento fiscal - Fornecedor |
| INFORMAR_VALORES_CREDITADOS_ATE | char(1) |  |  | Crédito de ICMS - Informar valores creditados até |
| VALORES_CREDITADOS_ATE | date(4) |  | S | Crédito ICMS - Valores creditados até |
| CODIGO_RECOLHIMENTO_PIS | varchar(6) |  | S | Código de recolhimento PIS |
| CODIGO_RECOLHIMENTO_COFINS | varchar(6) |  | S | Código de recolhimento COFINS |
| APROPRIACAO_CREDITO_ICMS_PARCELA_UNICA | char(1) |  |  | BEM COM APROPRIAÇÃO DE CRÉDITO DE ICMS EM PARCELA ÚNICA CONFORME DECRETO 703/2016 |
| UTILIZAR_CREDITO_ICMS_MES_SEQUINTE_AQUISICAO | char(1) |  |  | Utilizar o crédito de ICMS no mês seguinte a data de aquisição do bem |
| BASE_CALCULO_ICMS | numeric(13) |  |  | Base de cálculo do ICMS |
| CREDITO_ICMS_MES_INICIO_EFETIVO_APROPRIAR_48 | char(1) |  |  | Apropriar credito de ICMS em 1/48 a partir do mês início efetivo das atividades |
| DEBITO_ICMS_OPERACAO_DIFERENCIAL_ALIQUOTA | char(1) |  |  | Recolher o débito do ICMS Diferencial de Alíquotas deste bem em 1/48 - Bem oriundo de outro estado (S/N) |
| VALOR_PARCELA_EXCLUIR | numeric(13) |  |  | Parcela a excluir do valor de aquisição |
| DATA_TRANSFERENCIA | date(4) |  | S | Data de transferência |
| DATA_TRANSFERIDO | date(4) |  | S | Data quando bem foi transferido |
| I_SCP | integer(4) |  | S | SCP |
| DEBITO_ICMS_DIFERENCIAL_ALIQUOTA_PARCELA_UNICA | char(1) |  |  | Recolher débito de ICMS em parcela única |
| APROPRIACAO_CREDITO_ICMS_ANUAL | char(1) |  | S | Campo para verificar o decreto 272/2019 |
| APROPRIACAO_CREDITO_ICMS_ANUAL_2014 | char(1) |  | S | Campo para verificar o decreto 46.575/2014 |
| APROPRIACAO_CREDITO_ICMS_PARCELA_UNICA_RICMS_DDTT | char(1) |  | S | Campo para verificar o art. 29 do RICMS-DDTT |
| APROPRIACAO_CREDITO_ICMS_ANUAL_2024 | char(1) |  | S | Campo para verificar o decreto 82/2024 |
| APROPRIACAO_CREDITO_ICMS_PARCELA_UNICA_RICMS | char(1) |  | S | Campo para verificar o art. 5, anexo VIII - parte 2 do RICMS |
| APROPRIACAO_CREDITO_ICMS_PARCELA_UNICA_ART_31_RICMS | char(1) |  | S | Campo para verificar o art. 31, § 6, Livro I do RICMS |
| CREDITO_ICMS_ATIVO_IMOBILIZADO_INDUSTRIA_SN | char(1) |  |  | Crédito ICMS Ativo Imobilizado Indústria SN 7% - An2, Art. 15, § 25, incisos II e III |
| CREDITO_ICMS_ATIVO_IMOBILIZADO_PRODEIC_INVESTE | char(1) |  |  | Crédito ICMS Ativo Imobilizado vinculado ao PRODEIC Investe - Decreto 288/2019 |
