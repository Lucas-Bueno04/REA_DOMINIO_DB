# LRIRPJ_REAL_EXCLUSAO_LANCAMENTO — Lançamentos de Exclusões do Imposto de Renda - Lancamentos Contábeis
150 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_IRPJ_REAL_EXCLUSAO | integer(4) | PK |  | Código do Lançamento de Exclusão da IRPJ |
| I_ITEM | integer(4) | PK |  | Sequencial da exclusão |
| I_LANCAMENTO | integer(4) | PK |  | Sequencial |
| NUMERO_LOTE | integer(4) |  |  | Número lote/lançamento |
| DATA_LANCAMENTO | date(4) |  |  | Data |
| CONTA | integer(4) |  |  | Conta |
| VALOR | numeric(13) |  |  | Valor |
| VALOR_GERAL | numeric(13) |  |  | Valor geral |
| VALOR_RURAL | numeric(13) |  |  | Valor rural |
| CODIGO_HISTORICO | integer(4) |  |  | Código do histórico |
| HISTORICO | varchar(512) |  |  | Histórico |
| TIPO_SALDO | char(1) |  | S | Tipo Saldo:  D-Devedor ou C-Credor. |
