# EFSDOIMP_PIS_COFINS_CONTABILIZACAO_DETALHAMENTO_CREDITO — Saldo do Impostos - Contabilização do PIS/COFINS Crédito
2.339 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| I_SCP | integer(4) | PK |  | SCP |
| I_RECOLHIMENTO | integer(4) | PK |  | Recolhimento |
| CONSOLIDADO | char(1) | PK |  | Consolidado |
| CODIGO_CREDITO | integer(4) | PK |  | Código do crédito |
| CREDITO_PELAS_ENTRADAS | numeric(13) |  |  | Crédito pelas entradas |
| VALOR_CREDITO_EXTEMPORANEO | numeric(13) |  |  | Valor crédito extemporaneo |
| DEVOLUCAO_COMPRAS | numeric(13) |  |  | Devolução compras |
