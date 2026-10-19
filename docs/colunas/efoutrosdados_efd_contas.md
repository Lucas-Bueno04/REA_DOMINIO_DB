# EFOUTROSDADOS_EFD_CONTAS — EFD Contribuições - Outros Dados - Contas
3.369 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| COMPETENCIA | date(4) | PK |  | Competencia |
| I_INFORMATIVOS | integer(4) | PK |  | Informativo |
| REGISTRO | integer(4) | PK |  | REGISTRO (1-C481/C485/2-M400/M800/3-F500/F510/4-F550/F560/5-C181/C185/6-C191/C195/7-C491/C495/8-M410/M810/9-C870/C880/10-F100SAI/11-F100ENT) |
| SEQUENCIAL_CTA | integer(4) | PK |  | Sequencial da Conta |
| CODI_CTA | integer(4) |  |  | Conta Contábil |
| TIPO_CST | integer(4) |  |  | Tipo do CST (1 - Todos os CSTs / 2 - Selecionar os CSTs) |
| TIPO_NATUREZA_RECEITA | integer(4) |  |  | Tipo do Natureza Receita (1 - Todas as Naturezas / 2 - Selecionar as Naturezas) |
| TIPO_ACUMULADOR | integer(4) |  |  | Tipo do Acumulador (1 - Todos os acumuladores / 2 - Selecioanr os acumuladores) |
| TIPO_CFOP | integer(4) |  |  | Tipo do CFOP (1 - Todos os CFOPs / 2 - Selecionar os CFOPs) |
| TIPO_LANCAMENTO | char(1) |  |  | TIPO LANÇAMENTO - D(DEMAIS LANÇAMENTOS)/C(CONTRATOS DE FOMENTO MERCANTIL)/E(Empreendimentos Imobiliários) |
