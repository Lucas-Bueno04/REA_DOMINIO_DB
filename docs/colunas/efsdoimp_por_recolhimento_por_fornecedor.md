# EFSDOIMP_POR_RECOLHIMENTO_POR_FORNECEDOR — Saldo dos Impostos - Detalhamento por Recolhimento - Por Fornecedor
46.930 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| CODIGO_RECOLHIMENTO | char(6) | PK |  | Código do recolhimento |
| TIPO_INSCRICAO | integer(4) | PK |  | Tipo da inscrição do fornecedor |
| INSCRICAO | char(14) | PK |  | Inscrição do fornecedor |
| VALOR_CONTABIL_ENTRADA | numeric(13) |  |  | Valor Contábil Entrada |
| BASE_CALCULO_ENTRADA | numeric(13) |  |  | Base Cálculo Entrada |
| VALOR_IMPOSTO_ENTRADA | numeric(13) |  |  | Valor Imposto Entrada |
| VALOR_ISENTAS_ENTRADA | numeric(13) |  |  | Valor Isentas Entrada |
| VALOR_OUTRAS_ENTRADA | numeric(13) |  |  | Valor Outras Entrada |
| BASE_CALCULO | numeric(13) |  |  | Base Cálculo |
| SALDO_DEVEDOR | numeric(13) |  |  | Saldo Devedor |
| VALOR_A_RECOLHER | numeric(13) |  |  | Valor a Recolher |
| VALOR_DIFERIDO | numeric(13) |  |  | Valor Diferido |
| VALOR_DIFERIDO_ANTERIOR | numeric(13) |  |  | Valor Diferido Anterior |
| PARCELA | integer(4) |  |  | Parcela |
| VALOR_PAGO | numeric(13) |  |  | Valor pago |
| DATA_VENCIMENTO | date(4) |  |  | Data do vencimento |
| VALOR_ADICIONAL_RETENCAO_ENTRADA | numeric(13) |  |  | Débito adicional retenção pelas entradas - Lei 9.711/98 |
| VALOR_DEDUCAO_RETENCAO_ENTRADA | numeric(13) |  |  | Débito retenção pelas entradas |
