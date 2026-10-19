# EFSDOIMP_SIMPLES_NACIONAL_PRORROGACAO — Saldo dos Impostos - Simples Nacional Prorrogação
640 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Período |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| TIPO_PRORROGACAO | integer(4) | PK |  | Tipo Prorrogação (1-FEDERAIS / 2-ESTADUAIS / 3-MUNICIPAIS / 4-OUTROS) |
| VENCIMENTO | date(4) | PK |  | Vencimento |
| PRORROGACAO | char(3) | PK |  | Prorrogação (F-Federais / E-Estaduais / M-Municipais) |
| FILIAL | integer(4) | PK |  | Filial |
| SALDO_DEVEDOR | numeric(13) |  |  | Saldo devedor |
| VALOR_PAGO | numeric(13) |  |  | Valor Pago |
| SALDO_DIFERIDO | numeric(13) |  |  | Saldo diferido |
| SALDO_DIFERIDO_ANTERIOR | numeric(13) |  |  | Saldo diferido anterior |
