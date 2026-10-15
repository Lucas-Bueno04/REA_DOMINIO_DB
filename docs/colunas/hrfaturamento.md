# HRFATURAMENTO — Faturamento
43.194 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_FATURAMENTO | integer(4) | PK |  | Codigo |
| I_CLIENTE | integer(4) |  |  | Cliente |
| COMPETENCIA | date(4) |  |  | Compentecia |
| DATA_FATURAMENTO | date(4) |  |  | Data do faturamento |
| SOMENTE_VENCIMENTO | char(1) |  |  | Faturar somente o vencimento S N |
| NO_VENCIMENTO | date(4) |  |  | Vencimento quando marcado somente o vecimento |
| TIPO_FATURAMENTO | char(1) |  |  | Tipo de faturamento T Todos C Contratos e eventos com contrato E Eventos sem contrato |
| GERAR_PARCELADO | char(1) |  |  | Gerar faturamento parcelado S N |
| QUANTIDADE_PARCELA | integer(4) |  |  | Quantidade de parcelas |
| INTERVALO_DIAS | integer(4) |  |  | Intervalo de dias entre os vencimentos |
| I_NOTA_FISCAL | integer(4) |  | S | Nota fiscal |
| USUARIO | varchar(128) |  |  | Usuario que efetuou o faturamento |
| DATA_HORA | timestamp(8) |  |  | Data e hora do faturamento |
| I_NOTA_NFSE | integer(4) |  | S | Nota fiscal de servico eletronica |
| UTILIZAR_ALIQUOTA_CALCULO_ISS | varchar(1) |  |  | Utilizar aliquota para cálculo do ISS(E=Eventos/C=Tabela de Alíquota para Cálculo do ISS |
