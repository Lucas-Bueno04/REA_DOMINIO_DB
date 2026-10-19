# EFSDOIMP_PIS_COFINS_DETALHAMENTO_EXTEMPORANEO_CTB — Saldo do Impostos - Detalhamentos do PIS/COFINS - Créditos - Extemporâneo - Contabilização
8 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| CODIGO_CREDITO | integer(4) | PK |  | Código do crédito |
| ALIQUOTA_PERCENTUAL | numeric(7) | PK |  | Valor da alíquota do imposto |
| ALIQUOTA_VALOR | numeric(13) | PK |  | Alíquota em moeda (quando o cálculo é por unidade de medida) |
| VALOR_APURADO | numeric(13) |  |  | Valor apurado |
| I_SCP | integer(4) | PK |  | Sequencial do SCP |
| I_RECOLHIMENTO | integer(4) | PK |  | Sequencial do Recolhimento |
