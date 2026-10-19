# PMPARAMETRO — Parâmetros - Patrimônio
817 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| PERIODO_INICIAL | date(4) |  |  | Período inicial |
| PERIODO_FINAL | date(4) |  |  | Período atual |
| MASCARA_CODIGO_BEM | char(16) |  |  | Máscara do código do bem |
| NAO_ATUALIZAR_VALOR_DATA_ANTERIOR | char(1) |  |  | Não atualizar valores para bens cadastrados com data anterior (S/N) |
| DEDUZIR_VALOR_ICMS_VALOR_ORIGINAL | char(1) |  |  | Deduzir valor do ICMS da valor original (S/N) |
| DEDUZIR_VALOR_PISCOFINS_VALOR_ORIGINAL | char(1) |  |  | Deduzir valor do PIS e COFINS da valor original (S/N) |
| CALCULAR_DEPRECIACAO_TODOS_DIAS | char(1) |  |  | Calcular a depreciação considerando todos os dias do mês na competência que os bens foram adquiridos ou baixados (S/N) |
| CALCULAR_DEPRECIACAO_SOCIETARIA | char(1) |  |  | Calcular a depreciação societária (S/N) |
| CALCULAR_DEPRECIACAO_SOCIETARIA_INICIO | date(4) |  | S | Competência inicial do cálculo societário |
| GERAR_LANCAMENTO_CONTABIL | char(1) |  |  | Gerar lançamentos contábeis (S/N) |
| EMPRESA_LANCAMENTO_CONTABIL | integer(4) |  | S | Empresa onde serão gerados os lançamentos contábeis |
| GERAR_LANCAMENTO_CONTABIL_AQUISICAO | char(1) |  |  | Gerar lançamentos contábeis do valor de aquisição de novos bens (S/N) |
| GERAR_LANCAMENTO_CONTABIL_BAIXA | char(1) |  |  | Gerar lançamentos contábeis dos valores de baixas (S/N) |
| GERAR_LANCAMENTO_CONTABIL_TRANSFERENCIA_CONTA | char(1) |  |  | Gerar lançamentos contábeis dos valores de transferência de conta patrimonial (S/N) |
| GERAR_LANCAMENTO_CONTABIL_CONTA_CCU | char(1) |  |  | Gerar lançamentos a partir de contas patrimoniais e centros de custos (S/N) |
| GERAR_LANCAMENTO_CONTABIL_CCU_BEM | char(1) |  |  | Gerar lançamentos por centros de custos conforme informado no cadastro do bem (S/N) |
| TIPO_LANCAMENTO_BAIXA | char(1) |  |  | Tipo de lançamento contábil - Baixa (B=Ao efetuar a baixa/ I=Na integração contábil) |
| TIPO_LANCAMENTO_CREDITO_PISCOFINS | char(1) |  |  | Tipo de lançamento contábil - Crédito PIS/COFINS (B=Por bem/ C=Por competência) |
| TIPO_LANCAMENTO_AQUISICAO | char(1) |  |  | Tipo de lançamento contábil - Aquisição de novos bens (B=Ao cadastrar o bem/ I=Na integração contábil) |
| TIPO_LANCAMENTO_TRANSFERENCIA_CONTA | char(1) |  |  | Tipo de lançamento contábil - Transferência de conta patrimonial (B=Ao transferir o bem/ I=Na integração contábil) |
| CONTA_PIS_RECUPERAR | integer(4) |  |  | Conta contábil - PIS a recuperar |
| HISTORICO_PIS_RECUPERAR | integer(4) |  |  | Histórico contábil - PIS a recuperar |
| CONTA_COFINS_RECUPERAR | integer(4) |  |  | Conta contábil - COFINS a recuperar |
| HISTORICO_COFINS_RECUPERAR | integer(4) |  |  | Histórico contábil - COFINS a recuperar |
| FECHAMENTO_DATA | date(4) |  | S | Data do fechamento |
| DEDUZIR_DEP_FISCAL_DEP_SOCIETARIA_SEM_AVALIACAO | char(1) |  |  | Deduzir a depreciação fiscal acumulada da base de cálculo da depreciação societária para bens sem avaliação (S/N) |
| GERAR_LANCAMENTO_CONTABIL_SUBCONTA_DIFERENCA_DEPRECIACAO_FISCAL_SOCIETARIA | char(1) |  |  | Gerar lançamentos em subcontas conforme Lei nº 12.973/2014 quando houver diferença entre depreciação fiscal e societária |
| GERAR_SPED_CONTABIL_RAZAO_AUXILIAR | char(1) |  |  | Gerar o SPED Contábil - Razão Auxiliar |
| GERAR_LANCAMENTO_CONTABIL_AQUISICAO_VALOR | char(1) |  |  | Gerar lançamentos contábeis do valor de aquisição de novos bens (Valor Aquisição/Valor Original) |
| SOCIEDADE_EM_CONTA_PARTICIPACAO_PAR | char(1) |  |  | Possui Sociedade em Conta de Participação - SCP |
| POSSUI_BENS_MANTIDOS_PARA_VENDA | char(1) |  |  | Possui bens mantidos para venda |
| GERAR_LANCAMENTOS_VALORES_BENS_MANTIDOS_PARA_VENDA | char(1) |  |  | Gerar lanÃ§amentos contÃ¡beis dos valores dos bens mantidos para venda |
| TIPO_LANCAMENTO_BEM_MANTIDO_PARA_VENDA | char(1) |  |  | B - POR BEM, I - Na integraÃ§Ã£o contÃ¡bil |
