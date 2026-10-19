# EFSDOIMP_PIS_COFINS_DETALHAMENTO — Saldo do Impostos - Detalhamentos do PIS/COFINS
10.242 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| RECEITA_TRIBUTADA | numeric(13) |  |  | Receita tributada do mercado interno |
| RECEITA_EXPORTACAO | numeric(13) |  |  | Receita do mercado externo |
| RECEITA_ISENTA | numeric(13) |  |  | Receita não tributada |
| RECEITA_CUMULATIVA | numeric(13) |  |  | Receita cumulativa |
| RECEITA_TOTAL | numeric(13) |  |  | Receita total |
| TEM_RECEITA_CUM_NCUM | char(1) |  |  | Tem Receita Cumulativa e Não Cumulativa - Marcação Produto |
| I_SCP | integer(4) | PK |  | Sequencial do SCP |
| I_RECOLHIMENTO | integer(4) | PK |  | Sequencial do Recolhimento |
