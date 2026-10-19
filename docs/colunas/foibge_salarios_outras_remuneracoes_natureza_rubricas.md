# FOIBGE_SALARIOS_OUTRAS_REMUNERACOES_NATUREZA_RUBRICAS — Configuração de rúbricas para lançamento do IBGE
46 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da Empresa |
| COMPETENCIA | date(4) | PK |  | Competência da tela de outros dados - IBGE |
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| NATUREZA_RUBRICA | integer(4) |  |  | Natureza da rubrica |
| TIPO_PESQUISA | integer(4) | PK |  | (1 = PAC, 2 = PAS, 3 = PIA, 4 = PAIC) |
