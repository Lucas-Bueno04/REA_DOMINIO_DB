# CTCONTAS_SPED_ECF_PARTIDO_POLITICO — Plano de contas SPED ECF Partidos Políticos
2.657 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO_CTA_SPED_ECF_PARTIDO_POLITICO | integer(4) | PK |  | Código |
| CLASSIFICACAO_SPED_ECF_PARTIDO_POLITICO | varchar(20) |  |  | Classificação |
| DESCRICAO | varchar(255) |  |  | Descrição |
| VALIDADE_INICIO | date(4) |  |  | Início validade |
| VALIDADE_FIM | date(4) |  | S | Fim validade |
| TIPO | char(1) |  |  | Tipo (A = Analítica / S = Sintética) |
| CONTA_SUPERIOR | varchar(20) |  |  | Conta pai (superior) |
| NIVEL | integer(4) |  |  | Nível |
| NATUREZA | integer(4) |  |  | NATUREZA (1 - ATIVO / 2 - PASSIVO / 3 - PATRIMÔNIO LÍQUIDO / 4 - RESULTADO / 5 - OUTRAS) |
| VALIDADE_INICIO_BUSCA | integer(4) |  | S | DATA EM FORMATO INTEGER PARA OTIMIZAR INFORMATIVO ECF |
| VALIDADE_FIM_BUSCA | integer(4) |  | S | DATA EM FORMATO INTEGER PARA OTIMIZAR INFORMATIVO ECF |
