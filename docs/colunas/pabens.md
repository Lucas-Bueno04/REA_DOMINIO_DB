# pabens — Bens - Cadastro
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_bem | numeric(16) | PK |  | Codigo |
| desc_bem | varchar(80) |  |  | Descricao |
| dat_aqui_bem | date(4) |  |  | Aquisicao |
| fornece_bem | char(30) |  | S | Fornecedor |
| doc_ori_bem | char(30) |  | S | Documento de origem |
| codi_cta | integer(4) |  |  | Conta patrimonial |
| codi_ccu | integer(4) |  |  | Centro de custo |
| tx_dep_alter | numeric(6) |  |  | Taxa alternativa (-1 - usa da conta) |
| vl_orig_moe | numeric(13) |  |  | Valor original em moeda |
| vl_orig_ind | numeric(13) |  |  | Valor original em indice |
| vl_avaliado | numeric(13) |  |  | Valor avaliado |
| cor_mon_acum | numeric(13) |  |  | Correcao monetaria acumulada |
| dep_acum_ind | numeric(13) |  |  | Depreciacao acumulada em indice |
| dep_acum_moe | numeric(13) |  |  | Depreciacao acumulada em moeda |
| historico | varchar(80) |  | S | Historico |
| agregado_a | numeric(16) |  | S | Agregado a |
| ent_val_moe | numeric(13) |  |  | Entradas - Valor em moeda |
| ent_val_ind | numeric(13) |  |  | Entradas - Valor em indice |
| ent_dep_moe | numeric(13) |  |  | Entradas - depreciacao em moeda |
| ent_dep_ind | numeric(13) |  |  | Entradas - depreciacao em indice |
| sai_val_moe | numeric(13) |  |  | Saidas - Valor em moeda |
| sai_val_ind | numeric(13) |  |  | Saidas - valor em indice |
| sai_dep_moe | numeric(13) |  |  | Saidas  - depreciacao em moeda |
| sai_dep_ind | numeric(13) |  |  | Saidas - depreciacao em indice |
| val_icms_cre | numeric(13) |  |  | Valor Total do Credito de ICMS |
| dat_ini_dep | date(4) |  |  | Data de inicio da depreciacao |
| data_baixa | date(4) |  | S | Data da baixa |
| deprecia_bem | char(1) |  | S | Deprecia bem (S/N) |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| ident_bem | char(20) |  |  | Identificador |
| calcula_piscofins | char(1) |  |  | Calcula credito de PIS/COFINS (S/N) |
| credito_procargas_bem | char(1) |  |  | Credio Pro Cargas (S/N) |
| valor_aquisicao_bem | numeric(13) |  | S | Valor da aquisicao |
| calcula_piscofins_a | char(1) |  |  | Calcula credito de PIS/COFINS sobre aquisicao (S/N) |
| periodo_calculo | integer(4) |  | S | Periodo de calculo do PIS/COFINS |
| TIPO_BEM | char(1) |  |  | Tipo (B=Bem/ C=Componente) |
| CLASSIFICACAO_BEM | char(1) |  |  | Classificacao (I=Bem individual/ R=Bem resultante/ A=Imobilizado em andamento/ C=Imobilizado concluido) |
| ORIUNDO_ATIVO_CIRCULANTE_BEM | char(1) |  |  | Oriundo do ativo circulante (S/N) |
| FUNCAO_BEM | varchar(512) |  |  | Funcao |
| APROVEITAR_CRED_RESULTANTE_BEM | char(1) |  |  | Aproveitar credito somente no bem resultante (S/N) |
| FISCAL_NUMERO_BEM | numeric(15) |  | S | Numero do documento fiscal |
| ALIQUOTA_BEM | numeric(6) |  | S | Aliquota |
| FISCAL_SERIE_BEM | char(7) |  | S | Serie do documento fiscal |
| FISCAL_DATA_EMISSAO_BEM | date(4) |  | S | Data de emissao do documento fiscal |
| FISCAL_MODELO_BEM | integer(4) |  | S | Espécie do documento fiscal |
| FISCAL_CHAVE_NFE_BEM | char(44) |  | S | Chave NFe do documento fiscal |
| FISCAL_CODI_FOR_BEM | integer(4) |  | S | Fornecedor do documento fiscal |
| FISCAL_EMITENTE_BEM | char(1) |  | S | Emitente do documento fiscal (T=Terceiro/ P=Proprio) |
| FISCAL_SEQUENCIAL_ITEM_BEM | integer(4) |  | S | Sequencial do item do documento fiscal |
| FISCAL_CODI_PDI | char(14) |  | S | Produto |
| ORIGEM_BEM | char(1) |  | S | Origem do bem (N=Nacional/ I=Importado) |
| TIPO_CREDITO_BEM | tinyint(1) |  | S | Tipo do credito (9=Maq. equip. e out. bens incorporados ao ativo imob. (credito sobre encargos de dep.)/ 10=Maq. equip. e out. bens incorporados ao ativo imob. (credito com base no valor de aqui.)/ 11=Amortizacao de edif. e benf. em imoveis) |
| ESPECIE_BEM | tinyint(1) |  | S | Especie (1=Edificacoes e Benfeitorias em Imoveis Proprios/ 2=Edificacoes e Benfeitorias em Imoveis de Terceiros/ 3=Instalacoes/ 4=Maquinas/ 5=Equipamentos/ 6=Veiculos/ 99=Outras Situacoes) |
| TIPO_UTILIZACAO_BEM | tinyint(1) |  | S | Tipo de utilizacao (1=Producao de Bens Destinados a Venda/ 2=Prestacao de Servicos/ 3=Locacao a Terceiros/ 9=Outros) |
| CODIGO_CST_BEM | integer(4) |  | S | CST |
| ALIQUOTA_PIS_BEM | numeric(5) |  |  | Aliquota PIS |
| CREDITO_PIS_BEM | numeric(13) |  |  | Credito PIS |
| ALIQUOTA_COFINS_BEM | numeric(5) |  |  | Aliquota COFINS |
| CREDITO_COFINS_BEM | numeric(13) |  |  | Credito PIS |
| DESCRICAO_COMPLEMENTAR_BEM | varchar(80) |  |  | Descricao complementar |
| POSSUI_PROCESSO_REFERENCIADO_BEM | char(1) |  |  | Possui processo referenciado (S/N) |
| IDENTIFICACAO_REFERENCIADO_BEM | varchar(15) |  | S | Identificacao do processo |
| ORIGEM_REFERENCIADO_BEM | char(1) |  | S | Origem (1=Justica Federal/ 3=Secretaria da Receita Federal do Brasil/ 9=Outros) |
| SECAO_JUDICIARIA_BEM | char(255) |  | S | Identificação da Seção judiciária |
| VARA_BEM | char(2) |  | S | Identificação da Vara |
| DATA_SENTENCA_BEM | date(4) |  | S | Data da Sentença/Decisão Judicial |
| NATUREZA_ACAO_BEM | char(2) |  | S | Natureza da ação judicial |
| DESCRICAO_PROCESSO_BEM | char(100) |  | S | Descrição |
| VALOR_ICMS_BEM | numeric(13) |  |  | Valor ICMS |
| VALOR_ICMS_SUBTRI_BEM | numeric(13) |  |  | Valor ICMS - Substituicao tributaria |
| VALOR_ICMS_FRETE_BEM | numeric(13) |  |  | Valor ICMS sobre frete |
| VALOR_ICMS_DIFALI_BEM | numeric(13) |  |  | Valor ICMS - Diferencial aliquota |
| APROVEITAR_CREDITO_PROPORCIONAL_BEM | char(1) |  |  | Aproveitar crédito proporcional(N=Crédito vinculado somente as receitas Não Cumulativas/ S=Crédito vinculado as receitas Cumulativas e Não Cumulativas) |
| DEPRECIAR_100_INICIO_DEPRECIACAO_BEM | char(1) |  |  | Depreciar 100% no mês de início da depreciação (S/N) |
| DEBITO_ICMS_RECOLHER_BEM | char(1) |  |  | Recolher o débito do ICMS deste bem em 01/48 - Operações de importação (S/N) |
| CREDITO_ICMS_MES_INICIO_EFETIVO_BEM | char(1) |  |  | Utilizar o crédito de ICMS no mês de inicio efetivo das atividades (S/N) |
| MES_INICIO_EFETIVO_BEM | date(4) |  | S | Mês do início efetivo de suas atividades |
| PRODUZIDO_ADQUIRIDO_NO_ESTADO_BEM | char(1) |  |  | Bem produzido e adquirido no Estado com apropriação do crédito de ICMS em 1/42 ou 1/36 conforme Decreto 49.382/2012 |
