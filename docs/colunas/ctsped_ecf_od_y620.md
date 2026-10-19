# CTSPED_ECF_OD_Y620 — SPED ECF - Outros Dados - Registro Y620
16 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_OUTROS_DADOS | integer(4) | PK |  | Sequencial Outros Dados |
| I_PARTICIPACAO | integer(4) | PK |  | Sequencial Interno |
| DATA_EVENTO | date(4) |  | S | Data do evento |
| TIPO_RELACIONAMENTO | integer(4) |  |  | Tipo de relacionamento (1-Controle / 2-Controle Conjunto / 3-Influência Significativa / 4-Outras causas para aplicar MEP / 5-Exclusão do MEP) |
| CODIGO_PAIS | integer(4) |  | S | País |
| CNPJ_COLIGADA | varchar(14) |  |  | CNPJ da coligada |
| NOME_EMPRESARIAL | varchar(255) |  |  | Nome empresarial |
| VALOR_PARTICIPACAO_REAL | numeric(14) |  |  | Valor da participação em Reais |
| VALOR_PARTICIPACAO_MOEDA_ORIGINAL | numeric(14) |  |  | Valor da participação em moeda original |
| VALOR_PERCENTUAL_CAPITAL_TOTAL | numeric(8) |  |  | Percentual no capital total |
| VALOR_PERCENTUAL_CAPITAL_VOLANTE | numeric(8) |  |  | Percentual no capital votante |
| VALOR_RESULTADO_EQUIVALENCIA_PATRIMONIAL | numeric(14) |  |  | Resultado da equivalência patrimonial |
| DATA_PRIMEIRA_AQUISICAO | date(4) |  | S | Data da primeira aquisição |
| REGISTRADO_CARTORIO | char(1) |  |  | Registrado em cartório |
| NUMERO_REGISTRO | varchar(255) |  |  | Número do registro |
| NOME_CARTORIO | varchar(255) |  |  | Nome do cartório |
| VALOR_JUSTO | char(1) |  |  | Valor justo |
| NUMERO_AVALIACAO_VALOR_JUSTO | varchar(255) |  |  | Número da avaliação do valor justo |
