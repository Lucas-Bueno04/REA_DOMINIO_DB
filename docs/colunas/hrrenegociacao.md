# HRRENEGOCIACAO — Renegociacoes
1.031 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_RENEGOCIACAO | integer(4) | PK |  | Codigo |
| I_CLIENTE | integer(4) |  |  | Cliente |
| DATA_RENEGOCIACAO | date(4) |  |  | Data |
| I_HISTORICO | integer(4) |  | S | Codigo do historico |
| HISTORICO | varchar(512) |  |  | Historico |
| VALOR_RECEBIDO | numeric(13) |  | S | Valor recebido |
| GERAR_NOVO | char(1) |  |  | Gerar novo faturamento S N |
| NOVO_VALOR | numeric(13) |  | S | Valor do novo faturamento |
| NOVO_COMPETENCIA | date(4) |  | S | Competencia do novo faturamento |
| NOVO_VENCIMENTO | date(4) |  | S | Vencimento do novo faturamento |
| REPARCELAR | char(1) |  |  | Reparcelar gerando novo faturamento S N |
| REPARCELAR_VALOR | numeric(13) |  | S | Valor do reparcelar gerando novo faturamento |
| QUITAR | char(1) |  |  | Quitar sem recebimento S N |
| QUITAR_VALOR | numeric(13) |  | S | Valor do quitar sem recebimento |
| REPARCELAR_QUANTIDADE | integer(4) |  | S | Quantidade de parcelas do reparcelar |
| REPARCELAR_INTERVALO | integer(4) |  | S | Intervalo de dias do reparcelar |
| REPARCELAR_COMPETENCIA | date(4) |  | S | Competencia do reparcelar |
| REPARCELAR_MES_VENCIMENTO | char(1) |  | S | Mes do vencimento do reparcelar N No mesmo mes A Apos o mes S No segundo mes |
| REPARCELAR_DIA_VENCIMENTO | tinyint(1) |  | S | Dia vencimento do reparcelar |
| GERAR_EVENTO | char(1) |  |  | Gerar eventos M Mesmos eventos U Unico evento |
| I_EVENTO | integer(4) |  | S | Novo evento |
| ALTERAR_VENCIMENTO | char(1) |  |  | Alterar vencimento S N |
| VENCIMENTO_ORIGEM | date(4) |  | S | Vencimento original da parcela |
| VENCIMENTO_DESTINO | date(4) |  | S | Vencimento alterado |
| I_FATURAMENTO | integer(4) |  | S | Faturamento do vencimento alterado |
| I_PARCELA | integer(4) |  | S | Parcela do vencimento alterado |
| ORIGEM | char(1) |  |  | Origem R Recebida e renegociada N Renegociada A Alterado o vencimento |
| USUARIO | varchar(128) |  |  | Usuario que efetuou a renegociaCAo |
| DATA_HORA | timestamp(8) |  |  | Data e hora da renegociaCAo |
| COBRAR_JUROS | char(1) |  |  | Cobrar juros (S/N) |
| JUROS_VALOR | numeric(13) |  | S | Valor do juros |
| JUROS_EVENTO | integer(4) |  | S | Evento de juros |
| COBRAR_MULTA | char(1) |  |  | Cobrar multa (S/N) |
| MULTA_VALOR | numeric(13) |  | S | Valor da multa |
| MULTA_EVENTO | integer(4) |  | S | Evento de multa |
| VALOR_JUROS_REFATURADO | numeric(13) |  | S | Valor do juros utilizado no novo faturamento |
| VALOR_JUROS_REPARCELADO | numeric(13) |  | S | Valor do juros utilizado no reparcelamento |
| VALOR_MULTA_REFATURADO | numeric(13) |  | S | Valor da multa utilizado no novo faturamento |
| VALOR_MULTA_REPARCELADO | numeric(13) |  | S | Valor da multa utilizado no reparcelamento |
| DESCONTO_VALOR | numeric(13) |  | S | Desconto da RenegociaÃ§Ã£o |
