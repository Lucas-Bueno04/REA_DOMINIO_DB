# EFSDOIMP_ESTADUAL_ES — Saldo dos Impostos - Estadual ES
67 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| CREDITO_PRESUMIDO_TRANSPORTE | numeric(13) |  |  | Valor Crédito Presumido Transporte |
| ESTORNO_DEBITO_APURACAO_PROPRIA_FUNDAP | numeric(13) |  |  | Estorno de débito da apuração própria para apuração em separado-ICMS FUNDAP Art. 757 RICMS |
| CREDITO_PRESUMIDO_BENEFICIO_ART_530_LRI_RICMS | numeric(13) |  |  | Crédito Presumido - Benefício Art. 530-LRI RICMS |
| ESTORNO_ICMS_OPE_BENEFICIADAS_ART_530_LRI_RICMS | numeric(13) |  |  | Estorno do ICMS das ope. Beneficiadas - Art. 530-LRI RICMS |
| ESTORNO_CREDITO_PRESUMIDO_BENEFICIO_ART_530_LRI_RICMS_DEVOLUCAO | numeric(13) |  |  | Estorno Crédito Presumido - Benefício Art. 530-LRI RICMS - Devolução |
| ESTORNO_ICMS_RECOLHER_OPER_BENEFICIADAS_ART_530_LRI_ICMS | numeric(13) |  |  | Estorno do ICMS a recolher das Oper. beneficiadas Art.530-LRI RICMS |
| DEBITO_DIFERENCIAL_ALIQUOTA_PARECER_NORM_003_2013 | numeric(13) |  |  | Débito de diferencial de alíquota - Parecer Norm. Nº 003/2013 |
| ESTORNO_CREDITO_OPERACAO_APURACAO_PROPRIA_FUNDAP | numeric(13) |  |  | Est. crédito operação da apuração própria para apuração em separado - ICMS FUNDAP |
| ESTORNO_CREDITO_PRESTACAO_APURACAO_PROPRIA_FUNDAP | numeric(13) |  |  | Est. crédito prestação da apuração própria para apuração em separado - ICMS FUNDAP |
| DEBITO_FUNCOP_ICMS | numeric(13) |  |  | FUNCOP-ES - Débitos pelas saídas |
| CREDITO_PRESUMIDO_INTERESTADUAIS_IND_METALMECANICA_BENEFICIO_ART_530_LFII_RICMS | numeric(13) |  |  | Crédito presumido nas saídas interestaduais - Art. 530-LF, II RICMS |
| ESTORNO_DEVOLUCAO_CREDITO_PRESUMIDO_INTERESTADUAIS_IND_METALMECANICA_BENEFICIO_ART_530_LFII_RICMS | numeric(13) |  |  | Estorno devolução créd. presumido - Benefício Art. 530-LF, II RICMS |
| ESTORNO_ICMS_SAIDAS_INTERESTADUAIS_IND_METALMECANICA_BENEFICIO_ART_530_LFII_RICMS | numeric(13) |  |  | Estorno do ICMS saídas interestaduais - Art. 530-LF, § 1º, III RICMS |
| ESTORNO_ICMS_SAIDAS_INTERNAS_IND_METALMECANICA_BENEFICIO_ART_530_LFII_RICMS | numeric(13) |  |  | Estorno do ICMS saídas internas - Art. 530-LF, § 1º, II RICMS |
| ESTORNO_ICMS_RECOLHER_OPER_BENEFICIO_ART_530_LF_RICMS | numeric(13) |  |  | Estorno do ICMS a recolher das Oper. beneficiadas - Art. 530-LF, § 1º RICMS |
| ESTORNO_DEBITO_OPERACOES_CTE_SUBSTITUTO | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |
