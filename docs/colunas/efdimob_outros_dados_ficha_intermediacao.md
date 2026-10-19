# EFDIMOB_OUTROS_DADOS_FICHA_INTERMEDIACAO — DIMOB - Outras Dados - Ficha de Intermediação
229 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| PERIODO | date(4) | PK |  | Período |
| I_INTERMEDIACAO | integer(4) | PK |  | Código de Intermediação |
| NUMERO_CONTRATO_INTERMEDIACAO | varchar(6) |  |  | Número Contrato da Locação |
| DATA_CONTRATO_INTERMEDIACAO | date(4) |  |  | Data Contrato da Locação |
| I_IMOVEL | integer(4) |  |  | Código do Imóvel |
| I_LOCATARIO | integer(4) |  |  | Código do Locatório/Compradores |
| VALOR_VENDA | numeric(13) |  |  | Valor Venda |
| VALOR_COMISSAO | numeric(13) |  |  | Valor Comissão |
