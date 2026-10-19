# CTCONTAS_ANEEL — Plano de contas referencial da ANEEL
8.998 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO_CTA_ANEEL | integer(4) | PK |  | Código sequencial |
| CLASSIFICACAO_ANEEL | char(20) |  |  | Classificação |
| DESCRICAO_ANEEL | varchar(200) |  |  | Descrição |
| PERMITE_LANCAMENTO_ANEEL | char(1) |  |  | Permite lançamento (S/N) |
| VIGENCIA | date(4) | PK |  | Vigência |
| INICIO_VALIDADE | date(4) |  | S | Início da validade |
| FIM_VALIDADE | date(4) |  | S | Fim da validade |
