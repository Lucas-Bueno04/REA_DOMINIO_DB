# LRIRPJ_REAL_EXCLUSAO_ITEM — Lançamentos de Exclusões do Imposto de Renda - Exclusões
119 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_IRPJ_REAL_EXCLUSAO | integer(4) | PK |  | Código do Lançamento de Exclusões da IRPJ |
| I_ITEM | integer(4) | PK |  | Sequencial |
| I_EXCLUSAO | integer(4) |  |  | Exclusão |
| DESCRICAO | varchar(520) |  |  | Descrição |
| VALOR | numeric(13) |  |  | Valor |
| VALOR_GERAL | numeric(13) |  |  | Valor - Geral |
| VALOR_RURAL | numeric(13) |  |  | Valor - Rural |
| I_CSLL_REAL_EXCLUSAO | integer(4) |  | S | Código do Lançamento de Exclusões da CSLL |
| TIPO_SALDO | char(1) |  | S | Tipo Saldo:  D-Devedor ou C-Credor. |
