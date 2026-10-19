# HRURL_NFSE — Armazena as RULs usadas na nota fiscal de servico eletronica
3.288 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO_MUNICIPIO_SRF | integer(4) | PK |  | Codigo do municipio da Secretaria da Receita Federal |
| ACAO | tinyint(1) | PK |  | ACAO (1=CONSULTA SITUACAO NFSE/ 2=CONSULTA SITUACAO LOTE/ 3=CONSULTA NFSE RPS/ 4=CONSULTA LOTE RPS/ 5=CONSULTA NFSE/ 6=ENVIO LOTE / 7=CANCELAR NFSE/ 8=CANCELAR LOTE / 9=GERAR TOKEN / 10=INUTILIZAR INTERVALO / 12=BAIXAR ARQUIVO DE RETORNO) |
| OFICIAL_TESTE | char(1) | PK |  | Tipo da URL (O=Oficial/ T=Teste) |
| URL | varchar(500) |  |  | URL |
| URL_ACAO | varchar(500) |  |  | URL usada para determinar uma ação |
| URL_LOGAR | char(500) |  | S | URL usada para logar |
| VIGENCIA | date(4) | PK |  | Vigência da URL |
