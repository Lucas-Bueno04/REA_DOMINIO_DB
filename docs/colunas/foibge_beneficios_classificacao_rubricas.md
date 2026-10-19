# FOIBGE_BENEFICIOS_CLASSIFICACAO_RUBRICAS — Configuração de rúbricas para lançamento do IBGE
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da Empresa |
| COMPETENCIA | date(4) | PK |  | Competencia da tela de outros dados - IBGE |
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| CLASSIFICACAO_RUBRICA | integer(4) |  |  | Classificação da rúbrica |
| TIPO_PESQUISA | integer(4) | PK |  | 1= PAC, 2 = PAS, 3 = PIA, 4 = PAIC |
