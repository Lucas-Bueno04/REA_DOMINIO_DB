# HRFATURAMENTO_PARCELA_EMISSAO — Faturamento - Parcelas - Emissoes e exclusoes de boletos e documento de cobranca
38.631 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_FATURAMENTO | integer(4) | PK |  | Faturamento |
| I_PARCELA | integer(4) | PK |  | Parcela |
| TIPO | char(1) | PK |  | Tipo do relatorio B Boleto D Documento de cobranca |
| DATA_HORA | timestamp(8) | PK |  | Data e hora da emissao ou da exclusao |
| ACAO | char(1) | PK |  | Acao E Emissao X Exclusao |
| USUARIO | varchar(128) |  |  | Usuario que emitiu ou excluiu |
