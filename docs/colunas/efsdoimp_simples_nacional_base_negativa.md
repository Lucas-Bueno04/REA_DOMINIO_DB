# EFSDOIMP_SIMPLES_NACIONAL_BASE_NEGATIVA — Saldo dos Impostos - Detalhamento do Simples Nacional - Base negativa
13.429 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da Empresa |
| CODI_IMP | integer(4) | PK |  | Código do Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| PERIODO_APURACAO | date(4) | PK |  | Período da Origem da Base Negativa |
| ANEXO | tinyint(1) | PK |  | Anexo |
| SECAO | tinyint(1) | PK |  | SECAO |
| TABELA | tinyint(1) | PK |  | Tabela |
| BASE_CALCULO_TOTAL | numeric(13) |  |  | Base de Cálculo Total |
| VALOR_DEDUCAO_PERIODO_ANTERIOR | numeric(13) |  |  | Valor da Dedução do Período Anterior |
| VALOR_DEDUCAO_PERIODO_ATUAL | numeric(13) |  |  | Valor da Dedução do Período Atual |
| VALOR_DEDUZIDO | numeric(13) |  |  | Valor Deduzido |
| BASE_CALCULO_FINAL | numeric(13) |  |  | Base de Cálculo Final |
| VALOR_A_DEDUZIR | numeric(13) |  |  | Valor a Deduzir |
| FILIAL | integer(4) | PK |  | Código Empresa Filial |
| ARBCISS | numeric(13) | PK |  | Aliquota de reducao da base de calculo do ISS |
| TIPO_RECEITA | integer(4) | PK |  | Tipo Receita (1- Mercado Interno / 2- Exportação) |
| ARBCPIS | numeric(13) | PK |  | Alíquota de Redução de Base de Cálculo do PIS |
| ARBCCOFINS | numeric(13) | PK |  | Alíquota de Redução de Base de Cálculo do COFINS |
| SITUACOES | char(16) | PK |  | Situacoes fiscais |
| ARBCICMS | numeric(13) | PK |  | Aliquota de reducao da base de calculo do ICMS |
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| MUNICIPIO | integer(4) | PK |  | Código do município |
| CONSIDERAR_ALIQUOTA_REDUCAO_ICMS | char(1) | PK |  | CONSIDERAR ALÍQUOTA REDUCÃO ICMS |
| ANEXO_ORIGEM | integer(4) | PK |  | Anexo Origem |
| SECAO_ORIGEM | integer(4) | PK |  | Seção Origem |
| TABELA_ORIGEM | integer(4) | PK |  | Tabela Origem |
| VALOR_TRANSFERIDO_OUTRA_TABELA | numeric(13) |  |  | Valor transferido outra tabela |
| TRANSFERIDO | char(1) |  |  | Transferido para outra tabela(S/N) |
| VALOR_SALAO_PARCEIRO | numeric(13) |  |  | Valor salão-parceiro |
| APLICA_REDUCAO_BASE_CALCULO_ICMS | char(1) | PK |  | Aplica redução na base de calculo do ICMS |
| APLICA_REDUCAO_ISS | char(1) | PK |  | Redução do ISS aplicado na Alíquota ou na Base de Calculo |
