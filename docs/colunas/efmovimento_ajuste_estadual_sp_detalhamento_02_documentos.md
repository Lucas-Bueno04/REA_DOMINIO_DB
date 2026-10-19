# EFMOVIMENTO_AJUSTE_ESTADUAL_SP_DETALHAMENTO_02_DOCUMENTOS — SP - Ajuste Impostos lançados estaduais - Detalhamento 2 - Documentos
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_AJUSTE | integer(4) | PK |  | Sequencial do movimento do ajuste |
| I_DETALHAMENTO | integer(4) | PK |  | Sequencial do detalhamento do movimento do ajuste |
| CODI_ESP | integer(4) |  | S | Espécie |
| SERIE | varchar(7) |  | S | Série |
| SUBSERIE | integer(4) |  | S | Subsérie |
| DATA_NOTA | date(4) |  | S | Data |
| NUMERO_DOCUMENTO | numeric(15) |  | S | Número do documento |
| TIPO_CLIENTE_FORNECEDOR | char(1) |  |  | Participante |
| CODIGO_CLIENTE_FORNECEDOR | integer(4) |  | S | Cliente/Fornecedor |
| VALOR_DOCUMENTO | numeric(13) |  |  | Valor documento |
| CHAVE_NFE_CTE | varchar(44) |  | S | Chave NFe ou CTe |
| CODIGO_PRODUTO | char(14) |  | S | Código do produto |
