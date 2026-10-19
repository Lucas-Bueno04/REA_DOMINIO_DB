# EFAJUSTE_PISCOFINS_MOVIMENTO_PRODUTO_DETALHAMENTO — Ajuste no calculo do PIS/COFINS por movimento de produtos - Detalhamento
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_AJUSTE | integer(4) | PK |  | Codigo |
| I_DETALHAMENTO | integer(4) | PK |  | Sequencial |
| DATA_OPERACAO | date(4) |  |  | Data da operacao |
| VALOR | numeric(13) |  |  | Valor |
| TIPO_CONTRIBUICAO | integer(4) |  | S | Tipo de contribuicao |
| BASE_CALCULO | numeric(13) |  |  | Base de calculo |
| ALIQUOTA | numeric(7) |  |  | Aliquota |
| DESCRICAO_OPERACAO | varchar(255) |  |  | Descricao da operacao |
| CODI_CTA | integer(4) |  |  | Codigo da conta |
| INFORMACAO_COMPLEMENTAR | varchar(255) |  |  | Informacao complementar |
| CODIGO_AJUSTE | integer(4) |  | S | Código Ajuste |
| TIPO_INSCRICAO_ESTABELECIMENTO | integer(4) |  | S | Tipo Inscrição Estabelicimento |
| INSCRICAO_ESTABELECIMENTO | varchar(14) |  | S | Inscrição do Estabelicimento |
