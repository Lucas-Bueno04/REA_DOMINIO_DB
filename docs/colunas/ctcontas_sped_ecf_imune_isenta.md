# CTCONTAS_SPED_ECF_IMUNE_ISENTA — Plano de contas SPED ECF Imunes e Isentas
515 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO_CTA_SPED_ECF_IMUNE_ISENTA | integer(4) | PK |  | Código |
| CLASSIFICACAO_SPED_ECF_IMUNE_ISENTA | varchar(20) |  |  | Classificação |
| DESCRICAO | varchar(255) |  |  | Descrição |
| VALIDADE_INICIO | date(4) |  |  | Início validade |
| VALIDADE_FIM | date(4) |  | S | Fim validade |
| TIPO | char(1) |  |  | Tipo (A = Analítica / S = Sintética) |
| CONTA_SUPERIOR | varchar(20) |  |  | Conta pai (superior) |
| NIVEL | integer(4) |  |  | Nível |
| NATUREZA | integer(4) |  |  | Natureza (1 - Ativo / 2 - Passivo / 3 - Patrimônio Líquido / 4 - Resultado) |
| ORDEM | integer(4) |  |  | Ordem |
| VALIDADE_INICIO_BUSCA | integer(4) |  | S | DATA EM FORMATO INTEGER PARA OTIMIZAR INFORMATIVO ECF |
| VALIDADE_FIM_BUSCA | integer(4) |  | S | DATA EM FORMATO INTEGER PARA OTIMIZAR INFORMATIVO ECF |
