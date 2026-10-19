# LRPARCELA_IMPOSTO — Parcela dos impostos do Lalur
1.222 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| COMPETENCIA | date(4) | PK |  | Competência |
| IMPOSTO | char(1) | PK |  | Imposto (C=Contribuição Social/ I=IRPJ) |
| TIPO_CALCULO | char(1) | PK |  | Tipo de cálculo (R=Real/ E=Estimado) |
| I_PARCELA | integer(4) | PK |  | Sequencial da parcela |
| NUMERO_PARCELA | integer(4) | PK |  | Número da parcela |
| CODIGO_RECOLHIMENTO | varchar(6) |  |  | Código de recolhimento |
| VENCIMENTO | date(4) |  |  | Vencimento |
| VALOR | numeric(13) |  |  | Valor |
| IMPOSTO_PARCELADO | char(1) |  |  | Imposto parcelado (S/N) |
| I_SCP | integer(4) |  | S | SCP |
| AJUSTE_ANUAL | integer(4) | PK |  | Ajuste Anual |
