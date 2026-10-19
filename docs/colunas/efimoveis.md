# EFIMOVEIS — Imóveis - Cadastro
612 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_IMOVEL | integer(4) | PK |  | Código do imóvel |
| DESCRICAO_IMOVEL | varchar(250) |  |  | Descrição do imóvel |
| DATA_CADASTRO_IMOVEL | date(4) |  |  | Data do imóvel |
| CODI_CLI | integer(4) |  |  | Cliente do imóvel |
| ENDERECO_IMOVEL | varchar(60) |  |  | Endereço do imóvel |
| NUMERO_IMOVEL | integer(4) |  | S | Número do imóvel |
| COMPLEMENTO_IMOVEL | varchar(250) |  | S | Complemento do imóvel |
| CEP_IMOVEL | char(8) |  | S | CEP do imóvel |
| BAIRRO_IMOVEL | varchar(250) |  | S | Bairro do imóvel |
| TIPO_IMOVEL | char(1) |  |  | Tipo do imóvel (U/R) |
| CODIGO_MUNICIPIO_IMOVEL | integer(4) |  |  | Município do imóvel |
| UF_IMOVEL | char(2) |  |  | UF do imóvel |
