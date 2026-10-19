# EFOUTROS_CREDITOS_PISCOFINS_IMOBILIZADO — Outros creditos PIS/COFINS - Credito sobre imobilizado
48 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_IMOBILIZADO | integer(4) | PK |  | Codigo |
| DATA_IMOBILIZADO | date(4) |  |  | Data |
| CODI_BEM | numeric(16) |  | S | Codigo do bem (Patrimônio 1) |
| DATA_AQUISICAO | date(4) |  | S | Data da aquisicao |
| DESCRICAO | varchar(80) |  |  | Descricao |
| TIPO_CREDITO | tinyint(1) |  |  | Tipo do Credito (9=Credito sobre encargos de depreciacao/ 10=Credito com base no valor de aquisicao/ 11=Amortizacao e depreciacao de edificacoes e benfeitorias em imoveis) |
| ESPECIE_BEM | tinyint(1) |  |  | Especie do bem (1=Edificacoes e Benfeitorias em Imoveis Proprios/ 2=Edificacoes e Benfeitorias em Imoveis de Terceiros/ 3=Instalacoes/ 4=Maquinas/ 5=Equipamentos/ 6=Veiculos/ 99=Outros bens incorporados ao ativo imobilizado) |
| TIPO_UTILIZACAO | tinyint(1) |  |  | Tipo de utilizacao (1=Producao de Bens Destinados a Venda/ 2=Prestacao de Servicos/ 3=Locacao a Terceiros/ 9=Outros) |
| ORIGEM_BEM | char(1) |  |  | Origem do bem (N=Nacional/ I=Importado) |
| PERIODO_CALCULO | integer(4) |  |  | Periodo de calculo (12=1/12/ 24=1/24/ 48=1/48 540=Cfe. MP 540/11) |
| CODIGO_CST | integer(4) |  | S | CST PIS/COFINS |
| VALOR_AQUISICAO | numeric(13) |  |  | Valor de aquisicao |
| BASE_CALCULO | numeric(13) |  |  | Base de calculo |
| ALIQUOTA_PIS | numeric(5) |  |  | Aliquota de PIS |
| CREDITO_PIS | numeric(13) |  |  | Credito de PIS |
| ALIQUOTA_COFINS | numeric(5) |  |  | Aliquota de COFINS |
| CREDITO_COFINS | numeric(13) |  |  | Credito de COFINS |
| CONTA_BEM | integer(4) |  |  | Conta contabil do bem |
| DESCRICAO_COMPLEMENTAR | varchar(80) |  |  | Descricao complementar |
| POSSUI_PROCESSO_REFERENCIADO | char(1) |  |  | Possui processo referenciado (S/N) |
| IDENTIFICACAO_REFERENCIADO | varchar(15) |  | S | Identificacao do processo |
| ORIGEM_REFERENCIADO | char(1) |  |  | Origem do processo (1=Justica Federal/ 3=Secretaria da Receita Federal do Brasil/ 9=Outros) |
| MODULO_ORIGEM | char(1) |  |  | Modulo de origem (E=Escrita Fiscal/ P=Patrimonio) |
| SECAO_JUDICIARIA | char(255) |  | S | Identificação da Seção judiciária |
| VARA | char(2) |  | S | Identificação da Vara |
| DATA_SENTENCA | date(4) |  | S | Data da Sentença/Decisão Judicial |
| NATUREZA_ACAO | char(2) |  | S | Natureza da ação judicial |
| DESCRICAO_PROCESSO | char(100) |  | S | Descrição |
| APROVEITAR_CREDITO_PROPORCIONAL | char(1) |  |  | Aproveitar crédito proporcional(N=Crédito vinculado somente as receitas Não Cumulativas/ S=Crédito vinculado as receitas Cumulativas e Não Cumulativas) |
| I_BEM | numeric(16) |  | S | Codigo do bem (Patrimônio 2) |
| I_RECOLHIMENTO_PIS | integer(4) |  | S | Código Sequencial do Recolhimento do PIS |
| CODIGO_RECOLHIMENTO_PIS | char(6) |  |  | Código do Recolhimento do PIS |
| I_RECOLHIMENTO_COFINS | integer(4) |  | S | Código Sequencial do Recolhimento do COFINS |
| CODIGO_RECOLHIMENTO_COFINS | char(6) |  |  | Código do Recolhimento do COFINS |
| PARCELA_EXCLUIR_VALOR_AQUISICAO | numeric(13) |  |  | Parcela a excluir do valor de aquisição |
| BASE_CALCULO_TOTAL | numeric(13) |  |  | Valor da base de cálculo |
| ENCARGOS_DEPRECIACAO | numeric(13) |  |  | Encargos de depreciação |
| VALOR_EXCLUSAO | numeric(13) |  |  | Valor de exclusão |
| I_SCP | integer(4) |  | S | Sequencial do SCP |
