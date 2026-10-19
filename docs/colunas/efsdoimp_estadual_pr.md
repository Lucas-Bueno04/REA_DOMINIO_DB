# EFSDOIMP_ESTADUAL_PR — Saldo dos Impostos - Estadual PR
281 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| CREDITO_TRANSFERIDO_CONSOLIDADO | numeric(13) |  |  | Crédito transferido ao estabelecimento consolidador |
| DEBITO_TRANSFERIDO_CONSOLIDADO | numeric(13) |  |  | Débito transferido ao estabelecimento consolidador |
| CREDITO_RECEBIDO_CONSOLIDADO | numeric(13) |  |  | Crédito recebido de estabelecimento consolidado |
| DEBITO_RECEBIDO_CONSOLIDADO | numeric(13) |  |  | Débito recebido de estabelecimento consolidado |
| CREDITO_TRANSFERIDO_APURACAO_CONSOLIDADA | numeric(13) |  |  | Crédito transferido - apuração consolidada |
| DEBITO_TRANSFERIDO_APURACAO_CONSOLIDADA | numeric(13) |  |  | Débito transferido - apuração consolidada |
| CREDITO_MATERIAL_DE_USO_E_CONSUMO | numeric(13) |  |  | Crédito material de uso e consumo |
| SAIDAS_COM_REDUCAO_BASE_CALCULO_ART_71_SAIDAS | numeric(13) |  |  | Saídas com Redução de BC Art. 71 - Saídas |
| SAIDAS_COM_REDUCAO_BASE_CALCULO_ART_71_REDUCAO_Z | numeric(13) |  |  | Saídas com Redução de BC Art. 71 - ReduçãoZ |
| CREDITO_ATIVO_IMOBILIZADO | numeric(13) |  |  | Crédito Ativo Imobilizado |
| CREDITO_ICMS_SOBRE_INSUMOS_PREST_SERV_TRANSP | numeric(13) |  |  | Crédito ICMS sobre insumos |
| ICMSA_RECOLHIMENTO_ANTECIPADO | numeric(13) |  |  | ICMSA - Recolhimento antecipado |
| ICMSA_ICMS_RECOLHIDO_ANTECIPADAMENTE | numeric(13) |  |  | ICMSA - ICMS recolhido antecipadamente |
| CREDITO_PRESUMIDO_20_TRANSPORTADORAS_ICMS | numeric(13) |  |  | Crédito presumido de 20% para transportadoras - Item 48, Anexo III do RICMS |
| RESSARCIMENTO_DE_ICMS_SUBTRI | numeric(13) |  |  | Ressarcimento de ICMS ST |
| OUTROS_CREDITOS_VENDA_EFETUADA_FORA_ESTABELECIMENTO | numeric(13) |  |  | Outros créditos de venda efetuada fora do estabelecimento |
| DEBITO_FECOP_ICMS | numeric(13) |  |  | Débito referente ao FECOP-PR - ICMS Próprio |
| DEVOLUCAO_FECOP_ICMS | numeric(13) |  |  | Devolução referente ao FECOP-PR - ICMS Próprio |
| CREDITO_PRESUMIDO_TEXTIL_SAIDAS | numeric(13) |  |  | Crédito presumido têxtil - Saídas |
| CREDITO_PRESUMIDO_TEXTIL_REDUCAO_Z | numeric(13) |  |  | Crédito presumido têxtil - Redução Z |
| CREDITO_EXTEMPORANEO_INCISO_I_ART_23 | numeric(13) |  |  | Crédito extemporâneo - inciso I do § 5º do art. 23 do RICMS |
| CREDITO_ICMS_PROPRIO_CFE | numeric(13) |  |  | Crédito de ICMS Próprio |
| ICMS_TRANSPORTE_PAGO_ANTECIPADAMENTE | numeric(13) |  |  | ICMS transporte pago antecipadamente |
| CREDITO_PRESUMIDO_LEITE_CRU_SAIDAS_TRIBUTADAS | numeric(13) |  |  | Crédito presumido Leite Cru - Saídas |
| CREDITO_PRESUMIDO_LEITE_CRU_TOTAL_SAIDAS | numeric(13) |  |  | Crédito presumido Leite Cru - Total Saídas |
| CREDITO_PRESUMIDO_LEITE_CRU_PROPORCAO_SAIDAS_TRIBUTADAS | numeric(13) |  |  | Crédito presumido Leite Cru - Proporção Saídas |
| CREDITO_PRESUMIDO_LEITE_CRU_ENTRADAS | numeric(13) |  |  | Crédito presumido Leite Cru - Entradas |
| CREDITO_PRESUMIDO_LEITE_CRU_VALOR_UTILIZADO | numeric(13) |  |  | Crédito presumido Leite Cru - Valor Utilizado |
| CREDITO_PRESUMIDO_LEITE_CRU_ESTORNO | numeric(13) |  |  | Crédito presumido Leite Cru - Estorno |
| ICMS_ST_RECUP_RESSARC_SAIDAS_INTERNAS_CONSU_FINAL | numeric(13) |  |  | ICMS ST a recuperar/ressarcir referente saídas internas a consumidor final |
| ICMS_ST_COMP_SAIDAS_INTERNAS_CONSU_FINAL | numeric(13) |  |  | ICMS ST a complementar referente saídas internas a consumidor final |
| ICMS_ST_RECUP_RESSARC_SAIDAS_INTERESTADUAIS | numeric(13) |  |  | ICMS ST a recuperar/ressarcir referente saídas interestaduais |
| ICMS_ST_RECUP_RESSARC_SAIDAS_INTERNAS_ART_119_RICMS | numeric(13) |  |  | ICMS ST a recuperar/ressarcir referente saídas internas que trata o art. 119 do RICMS/17 |
| ICMS_ST_RECUP_RESSARC_SAIDAS_INTERNAS_CONTRIB_SN | numeric(13) |  |  | ICMS ST a recuperar/ressarcir referente saídas internas a contribuinte do Simples Nacional |
| ESTORNO_DEBITO_ANEXO_IX_RICMS | numeric(13) |  |  | Estorno de débito conforme 2 art 6 do Anexo IX do RICMS/2017 |
| CREDITO_ICMS_ST_ART_25_RICMS | numeric(13) |  |  | Crédito de ICMS Substituição Tributária - Art. 25 § 11 do RICMS/PR |
| ESTORNO_DEBITO_OPERACOES_CTE_SUBSTITUTO | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |
| CREDITO_AQUISICAO_COMBUSTIVEL_INSUMO | numeric(13) |  |  | Crédito aquisição combustíveis para insumos - Art. 25, III do § 4º do RICMS |
| ESTORNO_CREDITO_AQUISICAO_COMBUSTIVEL_INSUMO | numeric(13) |  |  | Estorno crédito aquisição combustíveis p/ insumos - Art. 25, IV do § 4º e § 5º do RICMS |
| ESTORNO_CREDITO_AQUISICAO_COMBUSTIVEL_INSUMO_OP_TRANSP_NAO_TRIBUTADA | numeric(13) |  |  | Estorno crédito aquisição combustíveis p/ insumos - Art. 25, IV do § 4º e § 5º do RICMS - Operações de transporte - Não tributadas |
| ESTORNO_CREDITO_AQUISICAO_COMBUSTIVEL_INSUMO_OP_TRANSP_TOTAL | numeric(13) |  |  | Estorno crédito aquisição combustíveis p/ insumos - Art. 25, IV do § 4º e § 5º do RICMS - Operações de transporte - Total |
| ESTORNO_CREDITO_AQUISICAO_COMBUSTIVEL_INSUMO_PROPORCAO | numeric(13) |  |  | Estorno crédito aquisição combustíveis p/ insumos - Art. 25, IV do § 4º e § 5º do RICMS - Proporção |
| ESTORNO_CREDITO_PRESUMIDO_COM_ELETRONICO_ART_11_A_DECRETO_6434_17 | numeric(13) |  |  | Estorno de crédito presumido com. eletrônico - Art. 11-A Decreto 6434/17 |
| CREDITO_PRESUMIDO_COMERCIO_ELETRONICO_ART_11_A_DECRETO_6434_17 | numeric(13) |  |  | Crédito presumido comércio eletrônico - Art. 11-A Decreto 6.434/17 |
| EXCLUSAO_MERCADORIA_SUBTRI_ART_19_ANEXO_IX_RICMS | numeric(13) |  |  | Exclusão de mercadoria da substituição tributária  - Art. 19, anexo IX do RICMS |
| CREDITO_AQUISICAO_COMBUSTIVEL_INSUMO_FROTA | numeric(13) |  |  | Crédito aquisição combustíveis para insumos - frota própria - Art. 25, §13º e §14º RICMS |
| ESTORNO_CREDITO_AQUISICAO_COMBUSTIVEL_INSUMO_FROTA | numeric(13) |  |  | Estorno crédito combust. p/ insumos - frota própria - Art. 25, §13º e §14º RICMS |
| ESTORNO_CREDITO_AQUISICAO_COMBUSTIVEL_INSUMO_OP_FROTA_NAO_TRIBUTADA | numeric(13) |  |  | Estorno crédito combust. p/ insumos - frota própria - Art. 25, §13º e §14º RICMS - Operações de frota - Não tributadas |
| ESTORNO_CREDITO_AQUISICAO_COMBUSTIVEL_INSUMO_OP_FROTA_TOTAL | numeric(13) |  |  | Estorno crédito combust. p/ insumos - frota própria - Art. 25, §13º e §14º RICMS - Operações de frota - Total |
| ESTORNO_CREDITO_AQUISICAO_COMBUSTIVEL_INSUMO_PROPORCAO_FROTA | numeric(13) |  |  | Estorno crédito combust. p/ insumos - frota própria - Art. 25, §13º e §14º RICMS - Proporção |
