# FOPAGTO_DADOS_PAGAMENTO — Pagamentos de Impostos - Publicação
4.928 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_PAGAMENTO_DOCUMENTO | integer(4) | PK |  | Sequencial |
| TIPO_PAGTO | integer(4) |  |  | Tipo pagamento que gerou a guia |
| COMPETENCIA | date(4) |  |  | Competencia |
| VALOR | numeric(13) |  |  | Valor gerado na emissão da guia. |
| CODIGO_REC | integer(4) |  | S | Código Recolhimento IRRF |
| PIX | varchar(2048) |  | S | Pix do PDF |
| LINHA_DIGITAVEL | varchar(2048) |  | S | Linha Digitavel do PDF |
| VENCIMENTO | date(4) |  | S | Vencimento gerado na emissão da guia |
