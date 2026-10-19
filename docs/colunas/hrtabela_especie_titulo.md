# HRTABELA_ESPECIE_TITULO — Tabela de especie de titulos - cobrança registrada - conta financeira
378 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Codigo |
| DESCRICAO | varchar(128) |  |  | Descricao |
| SOMENTE_BANCO | integer(4) | PK |  | Somente para o banco (0 = Banco padrão) |
| COOPERATIVA_CREDITO | char(1) | PK |  | Cooperativa de crédito (S/N) |
| TIPO_REMESSA | integer(4) | PK |  | Tipo de remessa (0 = Ambos / 1 = 240 posições / 2 = 400 posições |
| CARTEIRA | integer(4) | PK |  | Carteira |
| COOPERATIVA_CREDITO_BANCO | char(1) | PK |  | Banco da cooperativa (U=Unicred/S=Sicoob/N=Uniprime) |
| VERSAO_ARQUIVO | integer(4) | PK |  | Versão |
