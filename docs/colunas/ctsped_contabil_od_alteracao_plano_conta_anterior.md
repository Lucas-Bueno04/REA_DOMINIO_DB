# CTSPED_CONTABIL_OD_ALTERACAO_PLANO_CONTA_ANTERIOR — SPED Contábil - Outros Dados - Alteração plano de contas anterior
7.023 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_OUTROS_DADOS | integer(4) | PK |  | Sequencial dos outros dados |
| I_CONTA | integer(4) | PK |  | Sequencial da tabela pai |
| I_CONTA_ANTERIOR | integer(4) | PK |  | Sequencial |
| CODI_CTA_ANTERIOR | varchar(70) |  |  | Conta contábil anterior |
| CLASSIFICACAO_ANTERIOR | varchar(35) |  |  | Classificação anterior |
| SALDO | numeric(14) |  |  | Saldo |
| NATUREZA | char(1) |  |  | Natureza (C=CREDORA/D=DEVEDORA) |
| CODI_CCU_ANTERIOR | varchar(20) |  | S | CÃ³digo Centro de Custo |
| CODI_CCU_ATUAL | varchar(20) |  | S | Código Centro de Custo Atual |
