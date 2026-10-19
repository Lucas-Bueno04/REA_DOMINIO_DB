# EFSDOIMP_SUBTRI_POR_UF — Saldo dos Impostos - Substituição Tributária Por UF
706.131 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| SIGLA_UF | char(2) | PK |  | Sigla da UF |
| SALDO_DEVEDOR | numeric(13) |  |  | Saldo devedor |
| SALDO_CREDOR | numeric(13) |  |  | Saldo credor |
| VALOR_CONTABIL_ENTRADAS | numeric(13) |  |  | Valor contábil entradas |
| BASE_CALCULO_ENTRADAS | numeric(13) |  |  | Base cálculo entradas |
| VALOR_IMPOSTO_ENTRADAS | numeric(13) |  |  | Valor imposto entradas |
| VALOR_CONTABIL_SAIDAS | numeric(13) |  |  | Valor contábil saídas |
| BASE_CALCULO_SAIDAS | numeric(13) |  |  | Base cálculo saídas |
| VALOR_IMPOSTO_SAIDAS | numeric(13) |  |  | Valor imposto saídas |
| RESSARCIMENTO_CFOP_1603_2603 | numeric(13) |  |  | Ressarcimento CFOP 1603 2603 |
| RESSARCIMENTO_CFOP_5603_6603 | numeric(13) |  |  | Ressarcimento CFOP 5603 6603 |
| SALDO_CREDOR_ANTERIOR | numeric(13) |  |  | Saldo Credor Anterior |
| SALDO_DIFERIDO_ANTERIOR | numeric(13) |  |  | Saldo Diferido Anterior |
| OUTROS_DEBITOS | numeric(13) |  |  | Outros Débitos |
| ESTORNO_CREDITOS | numeric(13) |  |  | Estorno de Créditos |
| OUTROS_CREDITOS | numeric(13) |  |  | Outros Créditos |
| ESTORNO_DEBITOS | numeric(13) |  |  | Estorno de Debitos |
| ACRESCIMOS | numeric(13) |  |  | Acréscimos |
| DEDUCOES | numeric(13) |  |  | Deduções |
| SALDO_DIFERIDO | numeric(13) |  |  | Saldo Diferido |
| OUTROS_RECOLHIMENTOS | numeric(13) |  |  | Outros Recolhimentos |
| VALOR_PAGO | numeric(13) |  |  | Valor Pago |
| ESTORNO_FCP_INTERESTADUAL | numeric(13) |  |  | Estorno do Fundo de Comabte a Pobreza Interestadual |
| SALDO_DEVEDOR_COMPLEMENTACAO | numeric(13) |  |  | Saldo devedor Complementação |
| DATA_VENCIMENTO | date(4) |  |  | Data de vencimento |
| ESTORNO_DEVOLUCOES_FCP_INTERESTADUAL | numeric(13) |  |  | Estorno devolucoes FCP interestadual |
| I_RECOLHIMENTO | integer(4) | PK |  | Recolhimento |
| DEDUCAO_REF_FCP_INTERESTADUAL | numeric(13) |  |  | Dedução ref. ao Fundo de Combate a Pobreza Interestadual |
| VALOR_ICMS_RESSARCIMENTO_ST | numeric(13) |  |  | Valor Icms ressarcimento ST |
