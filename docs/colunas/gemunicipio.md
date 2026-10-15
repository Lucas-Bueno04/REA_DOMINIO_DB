# gemunicipio — Cadastro de municipios
5.576 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codigo_municipio | integer(4) | PK |  | Codigo sequencial |
| codigo_uf | integer(4) |  |  | Codigo do estado |
| nome_municipio | char(255) |  |  | Nome do municipio |
| codigo_srf | integer(4) |  | S | Codigo da Secretaria da Receita Federal |
| codigo_ibge | integer(4) |  | S | Codigo do IBGE/RAIS |
| codigo_estado | integer(4) |  | S | Codigo estadual do municipio |
| simplesn_tabela_iss | char(1) |  | S | Simples Nacional - Tabela do ISS(G - Tabela geral/P - Tabela do proprio municipio) |
| simplesn_permite_iss_fixo | char(1) |  | S | Simples Nacional - Permite ISS fixo (S/N) |
| simplesn_iss_fixo_por | char(1) |  | S | Simples Nacional - ISS fixo por (E - empresa/M - município) |
| SIMPLESN_ISS_FIXO_TIPO | char(1) |  | S | Tipo de calculo do ISS fixo por município(F - faixa/U - único) |
| CODIGO_ANP | integer(4) |  | S | Código ANP |
| CODIGO_NFSE_NET | integer(4) |  | S | Código do programa NFSE NET |
| CODIGO_ES_DOT | integer(4) |  | S | Código do Município ES - DOT |
| CODIGO_NFSE_GOIANIA | integer(4) |  | S | Código do programa NFSE GOIANIA |
| CODIGO_INTEGRA | varchar(6) |  | S | Código para Thomson Reuters INTEGRA |
| CODIGO_SRF_2016 | integer(4) |  | S | Codigo da Secretaria da Receita Federal 2016 |
| NOME_MUNICIPIO_ACENTUADO_MINUSCULO | varchar(255) |  | S | Nome do município com acentuação e variação de letras minúsculas/maiúsculas |
| CODIGO_NFSE_MGM | integer(4) |  | S | Código do fornecedor MGM |
| CODIGO_ES_DIEF | integer(4) |  | S | Código do Município ES - DIEF |
