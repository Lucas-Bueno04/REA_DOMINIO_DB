# CTCONTAS_ANS — Plano de contas ANS
21.970 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO_CTA_ANS | integer(4) | PK |  | Código |
| CLASSIFICACAO_ANS | varchar(20) |  |  | Classificação |
| DESCRICAO | varchar(512) |  |  | Descrição |
| VALIDADE_INICIO | date(4) |  | S | Início validade |
| VALIDADE_FIM | date(4) |  | S | Fim validade |
| NATUREZA | char(1) |  |  | Natureza (S=Sintética / A=Analítica) |
| TIPO_REGISTRO | char(1) |  |  | Tipo de registro (P = Padrão / M = Manual) |
| CODI_EMP | integer(4) | PK |  | Empresa |
