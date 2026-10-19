# LRCSLL_REAL_ADICAO_LANCAMENTO — Lançamentos de Adições da Contribuição Social - Lancamentos Contábeis
2.569 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CSLL_REAL_ADICAO | integer(4) | PK |  | Código do Lançamento de Adição da CSLL |
| I_ITEM | integer(4) | PK |  | Sequencial da adição |
| I_LANCAMENTO | integer(4) | PK |  | Sequencial |
| NUMERO_LOTE | integer(4) |  |  | Número lote/lançamento |
| DATA_LANCAMENTO | date(4) |  |  | Data |
| CONTA | integer(4) |  |  | Conta |
| VALOR | numeric(13) |  |  | Valor |
| VALOR_GERAL | numeric(13) |  |  | Valor - Geral |
| VALOR_RURAL | numeric(13) |  |  | Valor - Rural |
| CODIGO_HISTORICO | integer(4) |  |  | Código do histórico |
| HISTORICO | varchar(512) |  |  | Histórico |
| TIPO_SALDO | char(1) |  | S | Tipo Saldo:  D-Devedor ou C-Credor. |
