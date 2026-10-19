# CTCONTAS_SPED_ECF_TEF — Plano de contas SPED ECF - TEF Tributação Específica do Futebol
324 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO_CTA_SPED_ECF_TEF | integer(4) | PK |  | Código |
| CLASSIFICACAO_SPED_ECF_TEF | varchar(20) |  |  | Classificação |
| DESCRICAO | varchar(255) |  |  | Descrição |
| VALIDADE_INICIO | date(4) |  |  | Início validade |
| VALIDADE_FIM | date(4) |  | S | Fim validade |
| TIPO | char(1) |  |  | Tipo (A = Analítica / S = Sintética) |
| CONTA_SUPERIOR | varchar(20) |  |  | Conta pai (superior) |
| NIVEL | integer(4) |  |  | Nível |
| NATUREZA | integer(4) |  |  | Natureza (1 - Ativo / 2 - Passivo / 3 - Patrimônio Líquido / 4 - Resultado) |
| VALIDADE_INICIO_BUSCA | integer(4) |  | S | Data em formato integer para otimizar informatico ecf |
| VALIDADE_FIM_BUSCA | integer(4) |  | S | Data em formato integer para otimizar informatico ecf |
| MASCARA_CONTA | varchar(15) |  |  | Mascara da conta |
