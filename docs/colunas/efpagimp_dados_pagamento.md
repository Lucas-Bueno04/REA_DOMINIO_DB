# EFPAGIMP_DADOS_PAGAMENTO — Pagamentos de Impostos - guia
5.589 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_PAGAMENTO_DOCUMENTO | integer(4) | PK |  | Sequencial |
| CODI_IMP | integer(4) |  |  | Imposto |
| COMPETENCIA | date(4) |  |  | Competencia |
| PERIODICIDADE | integer(4) |  |  | Periodicidade |
| PARCELA | integer(4) |  |  | Parcela |
| VALOR | numeric(13) |  |  | Valor |
| I_SCP | integer(4) |  |  | Sequencial SCP |
| CODIGO_RECOLHIMENTO | varchar(6) |  |  | Codigo recolhimento |
| PIX | varchar(2048) |  | S | Codigo PIX |
| LINHA_DIGITAVEL | varchar(2048) |  | S | Codigo de barras |
| VALOR_GUIA | decimal(13) |  | S | Valor gerado na emissão da guia. |
| VENCIMENTO_GUIA | date(4) |  | S | Vencimento gerado na emissão da guia |
