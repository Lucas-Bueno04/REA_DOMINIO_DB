# EFPAGIMP_PUBLICAR_DOCUMENTO — Pagamentos de Impostos - Publicação
192 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_PAGAMENTO_DOCUMENTO | integer(4) | PK |  | Sequencial |
| CODI_IMP | integer(4) |  |  | Imposto |
| COMPETENCIA | date(4) |  |  | Competencia |
| PERIODICIDADE | integer(4) |  |  | Periodicidade |
| PARCELA | integer(4) |  |  | Parcela |
| VALOR | numeric(13) |  |  | Valor |
| I_DOCUMENTO | integer(4) |  |  | Sequencial da publicação do documento |
| I_SCP | integer(4) |  |  | Sequencial SCP |
| CODIGO_RECOLHIMENTO | varchar(6) |  |  | Codigo recolhimento |
