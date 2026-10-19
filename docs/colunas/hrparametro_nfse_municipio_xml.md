# HRPARAMETRO_NFSE_MUNICIPIO_XML — Parâmetro Honorarios - Tabela utilizada para montar o XML de envio de RPS para municípios específicos
1.224 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_MUNICIPIO | integer(4) | PK |  | Código Municipio |
| I_SEQUENCIAL_TAG | integer(4) | PK |  | Sequencial tags |
| TIPO_XML | integer(4) | PK |  | TIPO DE XML (0 - Envio, 2 - Consulta Lote, 3 - Consulta Situação, 4 - Cancelamento) |
| TAG | varchar(128) |  |  | Tag Atual |
| MASCARA_VALOR | varchar(128) |  |  | Valor da mascara |
| TAG_PAI | varchar(150) |  |  | Tag Pai |
| CHAVE_CAMPO_DW | varchar(128) |  | S | Campo da DW de dados |
| CAMPO_OBRIGATORIO | char(1) |  | S | Campo obrigatorio |
| ATRIBUTO_CHAVE_1 | varchar(128) |  | S | Chave do Atributo |
| ATRIBUTO_VALOR_1 | varchar(128) |  | S | Valor do Atributo |
| ATRIBUTO_CHAVE_2 | varchar(128) |  | S | Chave do Atributo |
| ATRIBUTO_VALOR_2 | varchar(128) |  | S | Valor do Atributo |
| ATRIBUTO_CHAVE_3 | varchar(128) |  | S | Chave do Atributo |
| ATRIBUTO_VALOR_3 | varchar(128) |  | S | Valor do Atributo |
| ORIGEM_INFORMACAO | integer(4) |  |  | Constante origem informação ( 0 - Sem Valor, 1 - DW Faturamento, 2 - DW Evento, 3 - Fixo Conforme mascara, 4 - Customizado na função, 5 - Tag Principal para Assinatura) |
| ATRIBUTO_CHAVE_4 | varchar(128) |  | S | Chave do Atributo |
| ATRIBUTO_VALOR_4 | varchar(128) |  | S | Valor do Atributo |
| ATRIBUTO_CHAVE_5 | varchar(128) |  | S | Chave do Atributo |
| ATRIBUTO_VALOR_5 | varchar(128) |  | S | Valor do Atributo |
