# EFSDOIMP_POR_UF_POR_NOTA — Saldo dos Impostos - Por UF - Por Nota
19.146 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| SIGLA_UF | char(2) | PK |  | Sigla da UF |
| CODIGO_NOTA | integer(4) | PK |  | Código Nota |
| SALDO_DEVEDOR | numeric(15) |  |  | Saldo Devedor |
| VALOR_DEBITO_SAIDAS | numeric(15) |  |  | Débitos Saídas |
| VALOR_PAGO | numeric(15) |  |  | Valor Pago |
| PARCELA | integer(4) |  |  | Parcela |
| VENCIMENTO | date(4) |  |  | Vencimento |
| DEBITO_SERVICOS_TRANSPORTE_ORIGEM | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF origem |
| DEBITO_SERVICOS_TRANSPORTE_DESTINO | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF destino |
| DEBITO_SERVICOS_TRANSPORTE_ORIGEM_UF_EMPRESA | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF origem (UF da empresa ativa) |
| DEBITO_SERVICOS_TRANSPORTE_DESTINO_UF_CLIENTE | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF destino (UF do cliente) |
| DEBITO_SERVICOS_TRANSPORTE_ORIGEM_UF_EMPRESA_IGUAL | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF origem (UF da empresa ativa nota com UF do cliente igual empresa) |
| DEBITO_SERVICOS_TRANSPORTE_ORIGEM_UF_EMPRESA_DIFERENTE | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF origem (UF da empresa ativa nota com UF do cliente diferente empresa) |
| DEBITO_SERVICOS_TRANSPORTE_DESTINO_UF_CLIENTE_IGUAL | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF destino (UF do cliente com UF do cliente igual empresa) |
| DEBITO_SERVICOS_TRANSPORTE_DESTINO_UF_CLIENTE_DIFERENTE | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF destino (UF do cliente com UF do cliente diferente empresa) |
| VALOR_DEBITOS_ENTRADAS | numeric(13) |  |  | Débitos Entradas |
| TIPO_DOCUMENTO | char(1) | PK |  | Tipo do Documento |
| ESTORNO_DEBITO_RECOLHIMENTO_JUNTO_ICMS_ST | numeric(13) |  |  | Estorno de débitos recolhimento junto ao ICMS ST |
