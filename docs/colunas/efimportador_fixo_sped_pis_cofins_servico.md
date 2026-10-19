# EFIMPORTADOR_FIXO_SPED_PIS_COFINS_SERVICO — Configuração do leiaute SPED PIS/COFINS do Importador Fixo - Entrada
19 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_ACU_A_VISTA | integer(4) |  |  | Código do acumulador para pagamento à vista |
| CODI_ACU_A_PRAZO | integer(4) |  |  | Código do acumulador para pagamento à prazo |
| CODI_ACU_OUTROS | integer(4) |  |  | Código do acumulador para outros tipos de pagamento |
| CODI_ESP | integer(4) |  |  | Código da espécie do serviço |
| GERAR_LANCAMENTOS_CONTABEIS | char(1) |  |  | Gerar lançamentos contábeis |
