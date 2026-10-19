# EFSDOIMP_INSS_RB_POR_RECOLHIMENTO — Saldo dos Impostos - INSS Receita Bruta - Por Recolhimento
338 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| CODIGO_RECOLHIMENTO | char(6) | PK |  | Código do Recolhimento |
| RECEITA_BRUTA_TOTAL | numeric(13) |  |  | Valor da Receita Bruta Total do Estabelecimento no Período |
| RECEITA_BRUTA_REAL | numeric(13) |  |  | Valor da Receita Bruta Real |
| VALOR_DEVOLUCAO | numeric(13) |  |  | Valor das Devoluções |
| VALOR_DEVOLUCAO_RESTO | numeric(13) |  |  | Valor das Devoluções - Resto |
| RECEITA_BRUTA | numeric(13) |  |  | Valor da Receita Bruta do Estabelecimento, correspondente às atividades/produtos por Recolhimento |
| VALOR_EXPORTACAO | numeric(13) |  |  | Valor das Exportações |
| VALOR_EXPORTACAO_DEVOLUCAO | numeric(13) |  |  | Valor das Exportações de Devolução |
| VALOR_EXCLUSAO | numeric(13) |  |  | Valor das Exclusões da Receita Bruta |
| BASE_CALCULO | numeric(13) |  |  | Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta |
| ALIQUOTA | numeric(8) |  |  | Alíquota da Contribuição Previdenciária sobre a Receita Bruta |
| VALOR_CONTRIBUICAO_APURADA | numeric(13) |  |  | Valor da Contribuição Previdenciária Apurada sobre a Receita Bruta |
| VALOR_DIFERIDO | numeric(13) |  |  | Valor diferido |
| VALOR_DIFERIDO_ANTERIOR | numeric(13) |  |  | Valor diferido - Período anterior |
| VALOR_CONTRIBUICAO_A_PAGAR | numeric(13) |  |  | Valor da Contribuição Previdenciária a Pagar |
| PARCELA | integer(4) |  |  | Parcela |
| VALOR_PAGO | numeric(13) |  |  | Valor Pago |
| DATA_VENCIMENTO | date(4) |  |  | Data do vencimento |
| VALOR_DEVOLUCAO_RELACIONADA | numeric(13) |  |  | Valor das Devoluções - Relacionada |
| VALOR_DEVOLUCAO_RESTO_RELACIONADA | numeric(13) |  |  | Valor das Devoluções - Resto - Relacionada |
| VALOR_DEVOLUCAO_NAO_RELACIONADA | numeric(13) |  |  | Valor das Devoluções - Não Relacionada |
| VALOR_DEVOLUCAO_RESTO_NAO_RELACIONADA | numeric(13) |  |  | Valor das Devoluções - Resto - Não Relacionada |
| VALOR_AJUSTE_REDUCAO | numeric(13) |  |  | Valor Ajuste Redução |
| VALOR_AJUSTE_ACRESCIMO | numeric(13) |  |  | Valor Ajuste Acréscimo |
| VALOR_EXCLUSAO_RELACIONADA | numeric(13) |  |  | Valor das Exclusões da Receita Bruta - Relacionada |
| VALOR_EXCLUSAO_NAO_RELACIONADA | numeric(13) |  |  | Valor das Exclusões da Receita Bruta - Não Relacionada |
| VALOR_EXPORTACAO_RELACIONADA | numeric(13) |  |  | Valor das Exportações - Relacionada |
| VALOR_EXPORTACAO_NAO_RELACIONADA | numeric(13) |  |  | Valor das Exportações - Não Relacionada |
| VALOR_EXPORTACAO_DEVOLUCAO_RELACIONADA | numeric(13) |  |  | Valor das Exportações de Devolução - Relacionada |
| VALOR_EXPORTACAO_DEVOLUCAO_NAO_RELACIONADA | numeric(13) |  |  | Valor das Exportações de Devolução - Não Relacionada |
| COMPENSACAO_PAGAMENTO_INDEVIDO_MAIOR | numeric(13) |  |  | Compensação de pagamento indevido ou a maior |
| I_SCP | integer(4) | PK |  | Sequencial SCP |
| VALOR_EXPORTACAO_DEVOLUCAO_RESTO | numeric(13) |  |  | Valor das Exportações de Devolução - Resto |
| VALOR_EXPORTACAO_DEVOLUCAO_RESTO_NAO_RELACIONADA | numeric(13) |  |  | Valor das Exportações de Devolução - Resto - Não Relacionada |
| VALOR_EXPORTACAO_DEVOLUCAO_RESTO_RELACIONADA | numeric(13) |  |  | Valor das Exportações de Devolução - Resto - Relacionada |
| OUTRAS_COMPENSACOES | numeric(13) |  |  | Outras Compensações |
| VALOR_CTE_SUBSTITUTO_REINF | numeric(13) |  |  | Valor CTE Substituto REINF |
| ALIQUOTA_TRANSICAO | numeric(8) |  |  | Alíquota de Transição da Contribuição Previdenciária sobre a Receita Bruta |
