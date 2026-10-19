# EFSDOIMP_ESTADUAL_MG — Saldo dos Impostos - Estadual MG
535 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| CREDITO_PRESUMIDO_TRANSPORTE_RODOVIARIO | numeric(13) |  |  | Crédito presumido transporte rodoviário de passageiros - Art. 75, XXXI |
| CTRC_EMITIDO_PELO_TRANSPORTADOR | numeric(13) |  |  | CTRC emitido pelo transportador, c/ ICMS responsabilidade do remetente/alienante |
| CREDITO_PRESUMIDO_BAR_REST_FORNEC_REFEICOES | numeric(13) |  |  | Crédito presumido bares, rest. e similares no fornec. de refeições - Art. 75, XXXIX |
| CREDITO_PRESUMIDO_BAR_REST_DEMAIS_OPERACOES | numeric(13) |  |  | Crédito presumido bares, rest. e similares nas demais operações - Art. 75, XXXIX |
| DEVOLUCAO_CRED_PRESU_BAR_REST_FORNEC_REFEICOES | numeric(13) |  |  | Devolução créd. pres. bares, rest. e similares fornec. de refeições - Art. 75, XXXIX |
| DEVOLUCAO_CRED_PRESU_BAR_REST_DEMAIS_OPERACOES | numeric(13) |  |  | Devolução créd. pres. bares, rest. e similares demais operações - Art. 75, XXXIX |
| CREDITO_CONFORME_ALIQUOTA_SN | numeric(13) |  |  | Crédito de ICMS conf. alíquota do Simples Nacional - Art. 23, LC 123/06 |
| DEVOLUCAO_MERCADORIA_ADQUIRIDA_SN | numeric(13) |  |  | Devolução de mercadoria adquirida de Simples Nacional |
| CREDITO_ICMS_RECEBIDO_PRODUTOR_RURAL | numeric(13) |  |  | Crédito de ICMS recebido de Produtor Rural em transferência - Art. 75, XXXIII |
| ESTORNO_CREDITO_ICMS_RECEBIDO_PRODUTOR_RURAL | numeric(13) |  |  | Estorno Crédito de ICMS recebido de Produtor Rural em transferência - Art. 75, XXXIII |
| CREDITO_PRESUMIDO_CARNES | numeric(13) |  |  | Crédito presumido de peixes, abate ou proces. de aves e de gado - Art. 75, IV RICMS |
| CREDITO_PRESUMIDO_CARNES_DEVOLUCAO | numeric(13) |  |  | Devolução créd. pres. peixes, abate ou proces. de aves e de gado - Art. 75, IV RICMS |
| CREDITO_PRESUMIDO_CARGA_TRIBUTARIA | numeric(13) |  |  | Crédito presumido com carga tributária equivalente a 3% - Art. 75, XIV |
| CREDITO_PRESUMIDO_CARGA_TRIBUTARIA_DEVOLUCAO | numeric(13) |  |  | Devolução de crédito presumido com carga tributária equivalente a 3% - Art. 75, XIV |
| CREDITO_PRESUMIDO_CARGA_TRIBUTARIA_ESTORNO | numeric(13) |  |  | Estorno do ICMS nas operações com carga tributária equivalente a 3% - Art. 75, XIV |
| CREDITO_PRESUMIDO_ACUCAR_ALCOOL | numeric(13) |  |  | Crédito presumido ao fabricante de álcool ou açúcar - Art.75, XXXII |
| CREDITO_PRESUMIDO_ACUCAR_ALCOOL_DEVOLUCAO | numeric(13) |  |  | Devolução do crédito presumido ao fabricante de álcool ou açúcar - Art.75, XXXII |
| CREDITO_PRESUMIDO_ACUCAR_ALCOOL_ESTORNO | numeric(13) |  |  | Estorno do ICMS nas operações do fabricante de álcool ou açúcar - Art.75, XXXII |
| CREDITO_PRESUMIDO_DOCES | numeric(13) |  |  | Crédito presumido de polpas, doces, conservas, molhos e outros - Art.75, XII |
| CREDITO_PRESUMIDO_DOCES_DEVOLUCAO | numeric(13) |  |  | Devolução do crédito pres. de polpas, doces, conservas, molhos e outros - Art.75, XII |
| CREDITO_PRESUMIDO_DOCES_ESTORNO | numeric(13) |  |  | Estorno do ICMS nas operações de polpas, doces, conservas, molhos e outros - Art.75, XII |
| CREDITO_ICMS_ANTECIPADO_AQUISICAO_ARROZ | numeric(13) |  |  | Crédito ICMS antecipado aquisição de arroz |
| CREDITO_ICMS_ANTECIPADO_OUTRAS_ANTECIPACOES | numeric(13) |  |  | Crédito ICMS antecipado outras antecipações |
| UTILIZACAO_SALDO_CREDOR_ICMS_EXTINCAO_DEBITOS_FISCAIS | numeric(13) |  |  | Utilização de saldo credor de ICMS para extinção de débitos fiscais |
| VALOR_DEDUZIDO_ICMS_ST_ESTOQUE | numeric(13) |  |  | Valor a ser deduzido do ICMS ST sobre estoques - Art. 7° da Resolução 4.855/15 |
| CREDITO_ICMS_ST_ESTOQUE_EXCLUSAO | numeric(13) |  |  | Crédito de ICMS sobre estoques na exclusão merc. da ST - Art. 23 da Res. 4.855/15 |
| CREDITO_ICMS_ST_ESTOQUE_EXCLUSAO_DISPONIVEL | numeric(13) |  |  | Crédito de ICMS sobre estoques na exclusão merc. da ST - Art. 23 da Res. 4.855/15 para mês seguinte |
| CREDITO_ICMS_ST_ESTOQUE_EXCLUSAO_ANTERIOR | numeric(13) |  |  | Crédito de ICMS sobre estoques na exclusão merc. da ST - Art. 23 da Res. 4.855/15 anterior |
| CREDITO_PRESUMIDO_ARTEFATOS_JOALHERIA_SAIDA | numeric(13) |  |  | Crédito presumido artefatos joalheria com carga tributária de 5%-Art.75,XXVIII,RICMS - Saída |
| CREDITO_PRESUMIDO_ARTEFATOS_JOALHERIA_REDUCAO_Z | numeric(13) |  |  | Crédito presumido artefatos joalheria com carga tributária de 5%-Art.75,XXVIII,RICMS - Redução Z |
| CREDITO_PRESUMIDO_ARTEFATOS_JOALHERIA_DEVOLUCAO | numeric(13) |  |  | Crédito presumido artefatos joalheria com carga tributária de 5%-Art.75,XXVIII,RICMS - Devolução |
| VALOR_ESTORNO_CREDITO_ESTIMULO | numeric(13) |  |  | Estorno do Crédito Estímulo (Devolução da compra) |
| CREDITO_ATIVO_IMOBILIZADO_ANTERIOR | numeric(13) |  |  | Crédito Ativo Imobilizado de períodos anteriores |
| DESCONTO_CONFORME_TERMO_ACEITE_LEI_22549_17 | numeric(13) |  |  | Desconto conforme Termo de Aceite da Lei 22.549/17 e Decreto 47.226/17 |
| OUTROS_CREDITOS_DEVOLUCAO_DIFALI | numeric(13) |  |  | Outros créditos devolução DIFALI |
| ESTORNO_DEBITO_DEVOLUCAO_COMPRA | numeric(13) |  |  | Estorno debitos devolução compra |
| NCAL_BARES_RESTAURANTES_E_SIMILARES | char(1) |  |  | (N = Apurado antes da SAI 56215 / S = Apurado depois da SAI 56215) |
| ESTORNO_FEM_MERCADORIAS_CREDITO_PRESUMIDO | numeric(13) |  |  | Estorno do FEM de mercadorias alcançadas pelo crédito presumido |
| RECEBIMENTO_CREDITO_POR_TRANSFERENCIA | numeric(13) |  |  | Recebimento de crédito por Transferência |
| ESTORNO_CREDITO_ICMS_ART_71_RICMS | numeric(13) |  |  | Estorno de crédito de ICMS conforme Art. 71 do RICMS |
| RESTITUICAO_ICMS_OP_ART_66 | numeric(13) |  |  | Restituição de ICMS OP - §10 Art. 66 do RIMCS |
| RESTITUICAO_ICMS_ST_ART_23 | numeric(13) |  |  | Restituição de ICMS ST - Art. 23, Anexo XV do RICMS |
| ESTORNO_DEBITO_OPERACOES_CTE_SUBSTITUTO | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |
| CREDITO_AQUISICAO_COMBUSTIVEL_INSUMO | numeric(13) |  |  | Crédito na aquisição de combustíveis para insumo - Conv. ICMS nº 199/22 e 15/23 |
| ESTORNO_FEM_MERCADORIAS_CREDITO_PRESUMIDO_DEVOLUCAO | numeric(13) |  |  | Estorno do FEM de mercadorias devolvidas alcançadas pelo crédito presumido |
| ESTORNO_CREDITO_FEM_ICMS_DEVOLUCAO | numeric(13) |  |  | Estorno do FEM - Fundo de Erradicação da Miséria - devolução |
