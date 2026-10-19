# CTDERE_CODTRIB — Catalogo oficial de codigos de tributacao (codTrib) da Tabela 11 da DeRE
1.405 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_TRIB | integer(4) | PK |  | Identificador interno do codigo de tributacao |
| CODTRIB | varchar(20) |  |  | Codigo de tributacao (codTrib) divulgado pela Receita Federal |
| TITULO | varchar(250) |  |  | Titulo do codigo de tributacao |
| DESCRICAO | varchar(1000) |  | S | Descricao do codigo de tributacao |
| DISPOSITIVO_LEGAL | varchar(60) |  | S | Dispositivo legal do codigo de tributacao |
| TIPO_REGISTRO | char(1) |  |  | Tipo do registro (F-Folha, selecionavel / A-Agrupamento, apenas hierarquia) |
