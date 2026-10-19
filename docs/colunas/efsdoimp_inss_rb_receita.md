# EFSDOIMP_INSS_RB_RECEITA — Saldo dos Impostos - INSS Receita Bruta - Controle de Receita
169 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| I_FILIAL | integer(4) | PK |  | Código da Filial |
| RECEITA_BRUTA_TOTAL | numeric(13) |  |  | Receita Bruta Total |
| RECEITA_BRUTA_RELACIONADA | numeric(13) |  |  | Receita Bruta Relacionada |
| RECEITA_BRUTA_NAO_RELACIONADA | numeric(13) |  |  | Receita Bruta Não Relacionada |
| RECEITA_BRUTA_RELACIONADA_EXPORTACAO | numeric(13) |  |  | Receita Bruta Relacionada Exportação |
| RECEITA_BRUTA_NAO_RELACIONADA_EXPORTACAO | numeric(13) |  |  | Receita Bruta Não Relacionada Exportação |
| DEVOLUCAO_VENDA_TOTAL | numeric(13) |  |  | Devolução Venda Total |
| DEVOLUCAO_VENDA_RELACIONADA | numeric(13) |  |  | Devolução Venda Relacionada |
| DEVOLUCAO_VENDA_NAO_RELACIONADA | numeric(13) |  |  | Devolução Venda Não Relacionada |
| DEVOLUCAO_VENDA_RELACIONADA_EXPORTACAO | numeric(13) |  |  | Devolução Venda Relacionada Exportação |
| DEVOLUCAO_VENDA_NAO_RELACIONADA_EXPORTACAO | numeric(13) |  |  | Devolução Venda Não Relacionada Exportação |
| RESTO_DEVOLUCAO_VENDA_TOTAL | numeric(13) |  |  | Resto Devolução Venda Total |
| RESTO_DEVOLUCAO_VENDA_RELACIONADA | numeric(13) |  |  | Resto Devolução Venda Relacionada |
| RESTO_DEVOLUCAO_VENDA_NAO_RELACIONADA | numeric(13) |  |  | Resto Devolução Venda Não Relacionada |
| RESTO_DEVOLUCAO_VENDA_RELACIONADA_EXPORTACAO | numeric(13) |  |  | Resto Devolução Venda Relacionada Exportação |
| RESTO_DEVOLUCAO_VENDA_NAO_RELACIONADA_EXPORTACAO | numeric(13) |  |  | Resto Devolução Venda Não Relacionada Exportação |
| I_SCP | integer(4) | PK |  | Sequencial SCP |
| RECEITA_BRUTA_RELACIONADA_EXPORTACAO_PERCENTUAL | numeric(13) |  |  | Receita Bruta Relacionada Exportação para Cálculo do Percentual de Relação |
| RECEITA_BRUTA_NAO_RELACIONADA_EXPORTACAO_PERCENTUAL | numeric(13) |  |  | Receita Bruta Não Relacionada Exportação para Cálculo do Percentual de Relação |
| DEVOLUCAO_VENDA_RELACIONADA_EXPORTACAO_PERCENTUAL | numeric(13) |  |  | Devolução Venda Relacionada Exportação para Cálculo do Percentual de Relação |
| DEVOLUCAO_VENDA_NAO_RELACIONADA_EXPORTACAO_PERCENTUAL | numeric(13) |  |  | Devolução Venda Não Relacionada Exportação para Cálculo do Percentual de Relação |
