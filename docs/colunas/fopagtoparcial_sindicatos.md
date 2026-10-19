# FOPAGTOPARCIAL_SINDICATOS — Informações dos valores de contribuição dos sindicatos
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_PAGTO | integer(4) | PK |  | SEQUENCIA DE PAGAMENTO |
| I_PAGTOITEM | integer(4) | PK |  | SEQUENCIAL DE PAGAMENTOS |
| I_SINDICATOS | integer(4) | PK |  | CODIGO DO SINDICATO |
| CODI_EMP | integer(4) | PK |  | CODIGO DA EMPRESA |
| CODI_EMP_LAN | integer(4) |  | S | CODIGO DA EMPRESA LANCAMENTO |
| NUME_LAN | integer(4) |  | S | NUMERO DO LANCAMENTO |
| VALOR | numeric(13) |  |  | VALOR PAGO |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
