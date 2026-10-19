# GECNAE_CLASSIFICACAO_TRIBUTARIA — Classificação de códigos CNAE quanto à elegibilidade ao Simples Nacional: impeditivos, híbridos ou fator R
185 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CNAE20 | char(15) | PK |  | Código CNAE 20 |
| DESCRICAO | varchar(300) |  |  | Descricao |
| TIPO_IMPEDITIVO | integer(4) |  |  | 0 = sem impeditivo / 1 = Impeditivo Simples Nacional / 2 = Impeditivo atividade hibrida / 3 = Impeditivo sujeito ao Fator R |
