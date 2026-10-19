# CTCMV_APURACAO_ESTOQUE — CMV - Apuração do Custo das Mercadorias Vendidas - Estoque
36 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_APURACAO | integer(4) | PK |  | Código apuração |
| I_ESTOQUE | integer(4) | PK |  | Sequencial |
| CODI_CTA | integer(4) |  |  | Conta contábil |
| VALOR_ESTOQUE_INICIAL | numeric(13) |  |  | Valor estoque inicial |
| VALOR_COMPRA | numeric(13) |  |  | Valor compras |
| VALOR_ESTOQUE_FINAL | numeric(13) |  |  | Valor estoque final |
| VALOR_CMV | numeric(13) |  |  | Valor CMV |
