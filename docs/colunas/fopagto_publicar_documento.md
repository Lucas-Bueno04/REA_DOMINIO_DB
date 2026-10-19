# FOPAGTO_PUBLICAR_DOCUMENTO — Pagamentos de Impostos - Publicação
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_PAGAMENTO_DOCUMENTO | integer(4) | PK |  | Sequencial |
| TIPO_PAGTO | integer(4) |  |  | 6-IRRF, 7-PIS |
| COMPETENCIA | date(4) |  |  | Competencia |
| VALOR | numeric(13) |  |  | Valor |
| I_DOCUMENTO | integer(4) |  |  | Sequencial da publicação do documento |
| CODIGO_REC | integer(4) |  | S | Código Recolhimento IRRF |
