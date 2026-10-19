# LRCSLL_REAL_ADICAO_ITEM — Lançamentos de Adições da Contribuição Social - Adições
310 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CSLL_REAL_ADICAO | integer(4) | PK |  | Código do Lançamento de Adição da CSLL |
| I_ITEM | integer(4) | PK |  | Sequencial |
| I_ADICAO | integer(4) |  |  | Adição |
| DESCRICAO | varchar(520) |  |  | Descrição |
| VALOR | numeric(13) |  |  | Valor |
| VALOR_GERAL | numeric(13) |  |  | Valor - Geral |
| VALOR_RURAL | numeric(13) |  |  | Valor - Rural |
| I_IRPJ_REAL_ADICAO | integer(4) |  | S | Código do Lançamento de Adição da IRPJ |
| TIPO_SALDO | char(1) |  | S | Tipo Saldo:  D-Devedor ou C-Credor. |
