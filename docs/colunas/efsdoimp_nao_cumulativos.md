# efsdoimp_nao_cumulativos — Saldo do Impostos - Detalhamento dos Nao Cumulativos
274 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_imp | integer(4) | PK |  | Imposto |
| data_sim | date(4) | PK |  | Competencia |
| pdic_sim | integer(4) | PK |  | Periodicidade |
| separa | char(1) |  |  | Separa creditos de importacao (S/N) |
| metodo | char(1) |  |  | Metodo de determinacao de creditos (I-somente interno/E-interno e externo) |
| receita_interna | numeric(13) |  |  | Receita do mercado interno |
| receita_externa | numeric(13) |  |  | Receita do mercado externo |
| receita_isenta | numeric(13) |  |  | Receita nao tributada |
| receita_total | numeric(13) |  |  | Receita total |
| percentual_interno | numeric(13) |  |  | Percentual de receita do mercado interno |
| percentual_externo | numeric(13) |  |  | Percentual de receita do mercado externo |
| percentual_isento | numeric(13) |  |  | Percentual de receita nao tributada |
| base_total_interna | numeric(13) |  |  | Base total do mercado interno |
| credito_total_interno | numeric(13) |  |  | Credito total do mercado interno |
| base_total_externa | numeric(13) |  |  | Base total do mercado externo |
| credito_total_externo | numeric(13) |  |  | Credito total do mercado externo |
| credito_dif_total_interno | numeric(13) |  |  | Credito total do mercado interno com aliquota diferenciada |
| credito_dif_total_externo | numeric(13) |  |  | Credito total do mercado externo com aliquota diferenciada |
| base_interna_vi | numeric(13) |  |  | Base do mercado interno vinculada a receita do mercado interno |
| credito_interno_vi | numeric(13) |  |  | Credito do mercado interno vinculado a receita do mercado interno |
| base_externa_vi | numeric(13) |  |  | Base do mercado externo vinculada a receita do mercado interno |
| credito_externo_vi | numeric(13) |  |  | Credito do mercado interno vinculado a receita do mercado interno |
| credito_dif_interno_vi | numeric(13) |  |  | Credito do mercado interno com aliquota diferenciada vinculado a receita do mercado interno |
| credito_dif_externo_vi | numeric(13) |  |  | Credito do mercado externo com aliquota diferenciada vinculado a receita do mercado interno |
| base_interna_vn | numeric(13) |  |  | Base do mercado interno vinculada a receita nao tributada |
| credito_interno_vn | numeric(13) |  |  | Credito do mercado interno vinculado a receita nao tributada |
| base_externa_vn | numeric(13) |  |  | Base do mercado externo vinculada a receita nao tributada |
| credito_externo_vn | numeric(13) |  |  | Credito do mercado externo vinculado a receita nao tributada |
| credito_dif_interno_vn | numeric(13) |  |  | Credito do mercado interno com aliquota diferenciada vinculado a receita nao tributada |
| credito_dif_externo_vn | numeric(13) |  |  | Credito do mercado externo com aliquota diferenciada vinculado a receita nao tributada |
| base_interna_ve | numeric(13) |  |  | Base do mercado interno vinculada a receita do mercado externo |
| credito_interno_ve | numeric(13) |  |  | Credito do mercado interno vinculado a receita do mercado externo |
| base_externa_ve | numeric(13) |  |  | Base do mercado externo vinculada a receita do mercado externo |
| credito_externo_ve | numeric(13) |  |  | Credito do mercado externo vinculado a receita do mercado externo |
| credito_dif_interno_ve | numeric(13) |  |  | Credito do mercado interno com aliquota diferenciada vinculado a receita do mercado externo |
| credito_dif_externo_ve | numeric(13) |  |  | Credito do mercado externo com aliquota diferenciada vinculado a receita do mercado externo |
| outros_interno_total | numeric(13) |  |  | Total de outros creditos do mercado interno |
| outros_externo_total | numeric(13) |  |  | Total de outros creditos do mercado externo |
| outros_interno_vi | numeric(13) |  |  | Outros creditos do mercado interno vinculado a receita do mercado interno |
| outros_externo_vi | numeric(13) |  |  | Outros creditos do mercado externo vinculado a receita do mercado interno |
| outros_interno_vn | numeric(13) |  |  | Outros creditos do mercado interno vinculado a receita nao tributada |
| outros_externo_vn | numeric(13) |  |  | Outros creditos do mercado externo vinculado a receita nao tributada |
| outros_interno_ve | numeric(13) |  |  | Outros creditos do mercado interno vinculado a receita do mercado externo |
| outros_externo_ve | numeric(13) |  |  | Outros creditos do mercado externo vinculado a receita do mercado externo |
| CREDITO_NEGATIVO_INTERNO_TOTAL | numeric(13) |  |  | Crédito negativo do mercado interno |
| CREDITO_NEGATIVO_EXTERNO_TOTAL | numeric(13) |  |  | Crédito negativo do mercado externo |
| CREDITO_NEGATIVO_INTERNO_VI | numeric(13) |  |  | Crédito negativo do mercado interno vinculado a receita do mercado interno |
| CREDITO_NEGATIVO_INTERNO_VN | numeric(13) |  |  | Crédito negativo do mercado interno vinculado a receita nAo tributada |
| CREDITO_NEGATIVO_INTERNO_VE | numeric(13) |  |  | Crédito negativo do mercado interno vinculado a receita do mercado externo |
| CREDITO_NEGATIVO_EXTERNO_VI | numeric(13) |  |  | Crédito negativo do mercado externo vinculado a receita do mercado interno |
| CREDITO_NEGATIVO_EXTERNO_VN | numeric(13) |  |  | Crédito negativo do mercado externo vinculado a receita nAo tributada |
| CREDITO_NEGATIVO_EXTERNO_VE | numeric(13) |  |  | Crédito negativo do mercado externo vinculado a receita do mercado externo |
| ESTOQUE_ABERTURA_INTERNO_TOTAL | numeric(13) |  |  | Crédito relativo ao estoque de abertura do mercado interno |
| ESTOQUE_ABERTURA_EXTERNO_TOTAL | numeric(13) |  |  | Crédito relativo ao estoque de abertura do mercado externo |
| ESTOQUE_ABERTURA_INTERNO_VI | numeric(13) |  |  | Crédito relativo ao estoque de abertura do mercado interno vinculado a receita do mercado interno |
| ESTOQUE_ABERTURA_INTERNO_VN | numeric(13) |  |  | Crédito relativo ao estoque de abertura do mercado interno vinculado a receita não tributada |
| ESTOQUE_ABERTURA_INTERNO_VE | numeric(13) |  |  | Crédito relativo ao estoque de abertura do mercado interno vinculado a receita do mercado externo |
| ESTOQUE_ABERTURA_EXTERNO_VI | numeric(13) |  |  | Crédito relativo ao estoque de abertura do mercado externo vinculado a receita do mercado interno |
| ESTOQUE_ABERTURA_EXTERNO_VN | numeric(13) |  |  | Crédito relativo ao estoque de abertura do mercado externo vinculado a receita não tributada |
| ESTOQUE_ABERTURA_EXTERNO_VE | numeric(13) |  |  | Crédito relativo ao estoque de abertura do mercado externo vinculado a receita do mercado externo |
