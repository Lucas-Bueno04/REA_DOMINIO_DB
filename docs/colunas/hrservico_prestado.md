# HRSERVICO_PRESTADO — Codigo do servico prestado
3 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_SEQUENCIAL | integer(4) | PK |  | Sequencial |
| I_SERVICO_PRESTADO | char(10) |  |  | Codigo |
| DESCRICAO | varchar(660) |  |  | Descricao |
| CODIGO_TRIBUTACAO | char(20) |  | S | Código de tributação municipal |
| I_ALIQUOTA_IBPT | integer(4) |  | S | Alíquota de impostos conforme IBPT |
| ALIQUOTA_IBPT_2015 | numeric(5) |  |  | Alíquota IBPT a partir de 2015 |
| ALIQUOTA_IBPT_MUNICIPAL | numeric(5) |  |  | Alíquota IBPT - Municipal |
| MODELO_NOTA_FISCAL | char(1) |  | S | E - NFSE / N - NFSE NACIONAL |
