# EFSDOIMP_SIMPLES_NACIONAL_CONTROLE_BASE_NEGATIVA_DEVOLUCAO_SECUNDARIA — Saldo Simples Nacional Controle Base de Base Negativa Devolução Secundária 2025
63 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da Empresa |
| CODI_IMP | integer(4) | PK |  | Código do Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| PERIODO_APURACAO | date(4) | PK |  | Período da Origem da Base Negativa Deevolução Secundária |
| ANEXO | tinyint(1) | PK |  | ANEXO |
| SECAO | tinyint(1) | PK |  | SECAO |
| TABELA | tinyint(1) | PK |  | TABELA |
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
| APLICA_REDUCAO_BASE_CALCULO_ICMS | char(1) | PK |  | Aplica redução na base de calculo do ICMS |
| APLICA_REDUCAO_ISS | char(1) | PK |  | Redução do ISS aplicado na Alíquota ou na Base de Calculo |
| VALOR_BASE_DESCONTAR | numeric(13) |  |  | Valor da base secundaria a descontar da devolução |
