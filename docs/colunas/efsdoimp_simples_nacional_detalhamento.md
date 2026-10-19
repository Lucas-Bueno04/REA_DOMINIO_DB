# EFSDOIMP_SIMPLES_NACIONAL_DETALHAMENTO — Saldo dos Impostos - Simples Nacional - Exigibilidade Suspensa
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| FILIAL | integer(4) | PK |  | Codigo da filial |
| ANEXO | tinyint(1) | PK |  | Anexo |
| SECAO | tinyint(1) | PK |  | Secao |
| TABELA | tinyint(1) | PK |  | Tabela |
| ARBCICMS | numeric(13) | PK |  | Aliquota de reducao da base de calculo do ICMS |
| ARBCISS | numeric(13) | PK |  | Aliquota de reducao da base de calculo do ISS |
| SITUACOES | char(16) | PK |  | Situacoes fiscais |
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| IMPOSTO | integer(4) | PK |  | Imposto com exigibilidade suspensa(1 - ICMS/2 -IPI/3 - ISS/4 - PIS/5 - COFINS/6 - CSLL/7 - IRPJ/8 - INSS) |
| MOTIVO | char(1) |  |  | Motivo(1 - Liminar em Mandado de Seguranca/2 - Deposito Judicial/3 - Antecipacao de Tutela/4 - Liminar em Medida Cautelar/5 - Deposito Administrativo/6 - Outros) |
| PROCESSO | char(20) |  | S | Numero do processo |
| VARA | integer(4) |  | S | Vara |
| CODIGO_MUNICIPIO | integer(4) |  | S | Municipio |
| UF | char(2) |  | S | UF |
| DEPOSITO | char(1) |  | S | Com deposito(S/N) |
| MUNICIPIO | integer(4) | PK |  | Código do município |
| ARBCPIS | numeric(13) | PK |  | Alíquota de Redução de Base de Cálculo do PIS |
| ARBCCOFINS | numeric(13) | PK |  | Alíquota de Redução de Base de Cálculo do COFINS |
| TIPO_RECEITA | integer(4) | PK |  | Tipo Receita (1- Mercado Interno / 2- Exportação) |
| ANEXO_ORIGEM | integer(4) | PK |  | Anexo Origem |
| SECAO_ORIGEM | integer(4) | PK |  | Seção Origem |
| TABELA_ORIGEM | integer(4) | PK |  | Tabela Origem |
| APLICA_REDUCAO_BASE_CALCULO_ICMS | char(1) | PK |  | Aplica redução na base de calculo do ICMS |
| APLICA_REDUCAO_ISS | char(1) | PK |  | Redução do ISS aplicado na Alíquota ou na Base de Calculo |
