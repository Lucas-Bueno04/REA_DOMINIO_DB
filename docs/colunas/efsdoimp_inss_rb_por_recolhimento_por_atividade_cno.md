# EFSDOIMP_INSS_RB_POR_RECOLHIMENTO_POR_ATIVIDADE_CNO — Saldo dos Impostos - INSS Receita Bruta - Por Recolhimento - Por Atividade - CNO
111 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| CODIGO_RECOLHIMENTO | char(6) | PK |  | Código do Recolhimento |
| I_FILIAL | integer(4) | PK |  | Código da Filial |
| I_ATIVIDADE | char(8) | PK |  | Atividade INSS Receita Bruta |
| RECEITA_BRUTA_TOTAL | numeric(13) |  |  | Valor da Receita Bruta Total do Estabelecimento no Período |
| RECEITA_BRUTA_NAO_RELACIONADA | numeric(13) |  |  | Valor da Receita Bruta Real - Não Relacionada |
| RECEITA_BRUTA_REAL | numeric(13) |  |  | Valor da Receita Bruta Real |
| VALOR_DEVOLUCAO | numeric(13) |  |  | Valor das Devoluções |
| VALOR_DEVOLUCAO_RESTO | numeric(13) |  |  | Valor das Devoluções - Resto |
| RECEITA_BRUTA | numeric(13) |  |  | Valor da Receita Bruta do Estabelecimento, correspondente às atividades/produtos |
| VALOR_EXPORTACAO | numeric(13) |  |  | Valor das Exportações |
| VALOR_EXPORTACAO_DEVOLUCAO | numeric(13) |  |  | Valor das Exportações de Devolução |
| VALOR_EXCLUSAO | numeric(13) |  |  | Valor das Exclusões da Receita Bruta |
| BASE_CALCULO | numeric(13) |  |  | Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta |
| ALIQUOTA | numeric(8) |  |  | Alíquota da Contribuição Previdenciária sobre a Receita Bruta |
| VALOR_CONTRIBUICAO_APURADA | numeric(13) |  |  | Valor da Contribuição Previdenciária Apurada sobre a Receita Bruta |
| VALOR_DEVOLUCAO_RELACIONADA | numeric(13) |  |  | Valor das Devoluções - Relacionada |
| VALOR_DEVOLUCAO_RESTO_RELACIONADA | numeric(13) |  |  | Valor das Devoluções - Resto - Relacionada |
| VALOR_DEVOLUCAO_NAO_RELACIONADA | numeric(13) |  |  | Valor das Devoluções - Não Relacionada |
| VALOR_DEVOLUCAO_RESTO_NAO_RELACIONADA | numeric(13) |  |  | Valor das Devoluções - Resto - Não Relacionada |
| VALOR_EXCLUSAO_RELACIONADA | numeric(13) |  |  | Valor das Exclusões da Receita Bruta - Relacionada |
| VALOR_EXCLUSAO_NAO_RELACIONADA | numeric(13) |  |  | Valor das Exclusões da Receita Bruta - Não Relacionada |
| VALOR_EXPORTACAO_RELACIONADA | numeric(13) |  |  | Valor das Exportações - Relacionada |
| VALOR_EXPORTACAO_NAO_RELACIONADA | numeric(13) |  |  | Valor das Exportações - Não Relacionada |
| VALOR_EXPORTACAO_DEVOLUCAO_RELACIONADA | numeric(13) |  |  | Valor das Exportações de Devolução - Relacionada |
| VALOR_EXPORTACAO_DEVOLUCAO_NAO_RELACIONADA | numeric(13) |  |  | Valor das Exportações de Devolução - Não Relacionada |
| I_SCP | integer(4) | PK |  | Sequencial SCP |
| VALOR_EXPORTACAO_DEVOLUCAO_RESTO | numeric(13) |  |  | Valor das Exportações de Devolução - Resto |
| VALOR_EXPORTACAO_DEVOLUCAO_RESTO_NAO_RELACIONADA | numeric(13) |  |  | Valor das Exportações de Devolução - Resto - Não Relacionada |
| VALOR_EXPORTACAO_DEVOLUCAO_RESTO_RELACIONADA | numeric(13) |  |  | Valor das Exportações de Devolução - Resto - Relacionada |
| RECEITA_BRUTA_TOTAL_REINF | numeric(13) |  |  | Valor da Receita Bruta Total do Estabelecimento no Período REINF |
| RECEITA_BRUTA_REINF | numeric(13) |  |  | Valor da Receita Bruta do Estabelecimento, correspondente às atividades/produtos REINF |
| VALOR_EXCLUSAO_RECEITA_BRUTA_REINF | numeric(13) |  |  | Valor das Exclusões da Receita Bruta - REINF |
| ACRESCIMO_RECEITA_BRUTA_REINF | numeric(13) |  |  | Acréscimo da Receita Bruta - REINF |
| REDUCAO_RECEITA_BRUTA_REINF | numeric(13) |  |  | Redução da Receita Bruta - REINF |
| BASE_CALCULO_REINF | numeric(13) |  |  | Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta REINF |
| VALOR_CONTRIBUICAO_APURADA_REINF | numeric(13) |  |  | Valor Contribuição Apurada REINF |
| DESCONTO_REINF | numeric(13) |  |  | Valor Desconto REINF |
| IPI_REINF | numeric(13) |  |  | Valor IPI REINF |
| ICMS_ST_REINF | numeric(13) |  |  | Valor ICMS ST REINF |
| RECEITA_BRUTA_REAL_REINF | numeric(13) |  |  | Valor da Receita Bruta Real REINF |
| VALOR_DEVOLUCAO_REINF | numeric(13) |  |  | Valor das Devoluções REINF |
| VALOR_EXPORTACAO_REINF | numeric(13) |  |  | Valor das Exportações REEINF |
| VALOR_EXPORTACAO_DEVOLUCAO_REINF | numeric(13) |  |  | Valor das Exportações de Devolução REINF |
| VALOR_DEVOLUCAO_RESTO_REINF | numeric(13) |  |  | Valor das Devolução Resto REINF |
| VALOR_DEVOLUCAO_RELACIONADA_REINF | numeric(13) |  |  | Valor das Devoluções - Relacionada REINF |
| VALOR_DEVOLUCAO_RESTO_RELACIONADA_REINF | numeric(13) |  |  | Valor das Devoluções - Resto - Relacionada REINF |
| VALOR_DEVOLUCAO_NAO_RELACIONADA_REINF | numeric(13) |  |  | Valor das Devoluções - Não Relacionada REINF |
| VALOR_DEVOLUCAO_RESTO_NAO_RELACIONADA_REINF | numeric(13) |  |  | Valor das Devoluções - Resto - Não Relacionada REINF |
| VALOR_EXCLUSAO_RELACIONADA_REINF | numeric(13) |  |  | Valor das Exclusões da Receita Bruta - Relacionada REINF |
| VALOR_EXCLUSAO_NAO_RELACIONADA_REINF | numeric(13) |  |  | Valor das Exclusões da Receita Bruta - Não Relacionada REINF |
| VALOR_EXPORTACAO_RELACIONADA_REINF | numeric(13) |  |  | Valor das Exportações - Relacionada REINF |
| VALOR_EXPORTACAO_NAO_RELACIONADA_REINF | numeric(13) |  |  | Valor das Exportações de Devoluções - Resto REINF |
| VALOR_EXPORTACAO_DEVOLUCAO_RESTO_REINF | numeric(13) |  |  | Valor das Exportações - Não Relacionada REINF |
| VALOR_EXPORTACAO_DEVOLUCAO_RELACIONADA_REINF | numeric(13) |  |  | Valor das Exportações de Devolução - Relacionada REINF |
| VALOR_EXPORTACAO_DEVOLUCAO_NAO_RELACIONADA_REINF | numeric(13) |  |  | Valor das Exportações de Devolução - Não Relacionada REINF |
| RECEITA_BRUTA_NAO_RELACIONADA_REINF | numeric(13) |  |  | Valor da Receita Bruta Real - Não Relacionada REINF |
| VALOR_EXPORTACAO_DEVOLUCAO_RESTO_NAO_RELACIONADA_REINF | numeric(13) |  |  | Valor das Exportações de Devolução - Resto - Não Relacionada REINF |
| VALOR_EXPORTACAO_DEVOLUCAO_RESTO_RELACIONADA_REINF | numeric(13) |  |  | Valor das Exportações de Devolução - Resto - Relacionada REINF |
| VALOR_EXPORTACAO_TRANSPORTE_CARGAS_REINF | numeric(13) |  |  | Valor das Exportações de Transporte de cargas REEINF |
| I_CNO | integer(4) | PK |  | Código CNO |
| DESCONTO_RELACIONADA_REINF | numeric(13) |  |  | Valor Desconto Relacionada REINF |
| IPI_RELACIONADA_REINF | numeric(13) |  |  | Valor IPI Relacionada REINF |
| ICMS_ST_RELACIONADA_REINF | numeric(13) |  |  | Valor ICMS ST Relacionada REINF |
| DESCONTO_NAO_RELACIONADA_REINF | numeric(13) |  |  | Valor Desconto Não Relacionada REINF |
| IPI_NAO_RELACIONADA_REINF | numeric(13) |  |  | Valor IPI Não Relacionada REINF |
| ICMS_ST_NAO_RELACIONADA_REINF | numeric(13) |  |  | Valor ICMS ST Não Relacionada REINF |
| DESCONTO_EXPORTACAO_RELACIONADA_REINF | numeric(13) |  |  | Valor Desconto Exportação Relacionada REINF |
| IPI_EXPORTACAO_RELACIONADA_REINF | numeric(13) |  |  | Valor IPI Exportação Relacionada REINF |
| ICMS_ST_EXPORTACAO_RELACIONADA_REINF | numeric(13) |  |  | Valor ICMS ST Exportação Relacionada REINF |
| DESCONTO_EXPORTACAO_NAO_RELACIONADA_REINF | numeric(13) |  |  | Valor Desconto Exportação Não Relacionada REINF |
| IPI_EXPORTACAO_NAO_RELACIONADA_REINF | numeric(13) |  |  | Valor IPI Exportação Não Relacionada REINF |
| ICMS_ST_EXPORTACAO_NAO_RELACIONADA_REINF | numeric(13) |  |  | Valor ICMS ST Exportação Não Relacionada REINF |
| VALOR_CTE_SUBSTITUTO_REINF | numeric(13) |  |  | Valor CTE Substituto REINF |
| ALIQUOTA_TRANSICAO | numeric(8) |  |  | Alíquota de Transição da Contribuição Previdenciária sobre a Receita Bruta |
