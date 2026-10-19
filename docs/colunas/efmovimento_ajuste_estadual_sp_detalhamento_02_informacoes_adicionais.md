# EFMOVIMENTO_AJUSTE_ESTADUAL_SP_DETALHAMENTO_02_INFORMACOES_ADICIONAIS — SP - Ajuste Impostos lançados estaduais - Detalhamento 02 - Adicionais
8 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_AJUSTE | integer(4) | PK |  | Sequencial do movimento do ajuste |
| CODI_ESP | integer(4) |  | S | Espécie |
| TIPO_CLIENTE_FORNECEDOR | char(1) |  | S | Participante |
| CODIGO_CLIENTE_FORNECEDOR | integer(4) |  | S | Cliente/Fornecedor |
| NUMERO_DOCUMENTO | integer(4) |  | S | Numero documento |
| SERIE | varchar(7) |  | S | Série |
| SUBSERIE | integer(4) |  | S | Subsérie |
| CHAVE_NFE_CTE | varchar(44) |  | S | Chave NFe, NFCe ou CTe |
| NUMERO_DOCUMENTO_ARRECADACAO | char(10) |  | S | Número do documento de arrecadação |
| NUMERO_PROCESSO | char(60) |  | S | Número do processo |
| ORIGEM | char(1) |  | S | Origem |
| DESCRICAO | char(255) |  | S | Descrição |
