# EFPARCELAMENTO_IMPOSTO_SN — Parcelamento de Impostos Simples Nacional
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_PARCELAMENTO_SN | integer(4) | PK |  | Sequencial do parcelamento Simples Nacinal |
| DESCRICAO | varchar(255) |  |  | Descrição |
| DATA_PARCELAMENTO | date(4) |  |  | Data do parcelamento |
| PARCELAR_SOMENTE_IMPOSTO | integer(4) |  |  | PARCELAR SOMENTE OS IMPOSTOS (1/ 2/ 3/ 4/ 5/ 6) |
| CODIGO_UF | integer(4) |  | S | Estado |
| CODIGO_MUNICIPIO | integer(4) |  | S | Munícipio |
| SITUACAO | tinyint(1) |  |  | 1-EM PARCELAMENTO/2-ENCERRADO A PEDIDO DO CONTRIBUINTE/3-ENCERRADO POR RESCISÃO/4-PARCELAMENTO QUITADO/5-ENCERRADO POR LIQUIDAÇÃO |
| DATA_SITUACAO | date(4) |  | S |  |
| TIPO_PARCELAMENTO | tinyint(1) |  | S | 1-NORMAL-ATÉ 60 PARCELAS/2-ESPECIAL-ATÉ 120 PARCELAS/3-ESPECIAL-ATÉ 175 PARCELAS/4-ESPECIAL-ATÉ 145 PARCELAS/5-GERAL - DÍVIDA ATIVA PGFN |
