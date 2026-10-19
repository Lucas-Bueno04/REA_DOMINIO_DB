# FOENCARGOS_EMPRESTIMO_CREDITO_TRABALHADOR_RESCISAO — Encargos do empréstimo do crédito do trabalhador rescisões
28 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_EMPREGADOS | integer(4) | PK |  | Empregado |
| COMPETENCIA | date(4) | PK |  | Competência |
| TIPO_PROCESSO | smallint(2) | PK |  | Tipo cálculo folha |
| VALOR | numeric(13) |  |  | Valor do encargo |
| VENCIMENTO | date(4) |  |  | Data de vencimento |
| I_FILIAIS | integer(4) | PK |  | Sequêncial da filial |
| I_PAGTO | integer(4) |  | S | Sequêncial de pagamento |
| I_CALCULOS | uniqueidentifier(16) |  |  | Sequêncial de cálculo |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
