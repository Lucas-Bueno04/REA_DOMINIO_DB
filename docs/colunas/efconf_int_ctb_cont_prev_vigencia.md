# EFCONF_INT_CTB_CONT_PREV_VIGENCIA — Configuração Integração Contábil das Contribuições Previdenciárias - Vigência
2.522 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_CONF_INT_CTB_CONT_PREV | integer(4) | PK |  | Código da configuração |
| VIGENCIA | date(4) | PK |  | Vigência |
| DESCRICAO | varchar(80) |  |  | Descrição |
| CT_INSS_RECOLHER | integer(4) |  | S | Conta INSS a recolher |
| CT_INSS_COMPENSAR | integer(4) |  | S | Conta INSS a compensar |
| CONTABILIZA_AGRUPADA_INSS_FOLHA_MENSAL | char(1) |  |  | INSS Folha Mensal - Contabilizar de forma agrupada conforme apuração previdenciária |
| CTB_INSS_FOLHA_MENSAL_SEGURADOS | integer(4) |  | S | INSS Folha Mensal - Segurados - Conta débito |
| CH_INSS_FOLHA_MENSAL_SEGURADOS | integer(4) |  | S | INSS Folha Mensal - Segurados - Histórico |
| CTB_INSS_FOLHA_MENSAL_CONTRIBUINTES | integer(4) |  | S | INSS Folha Mensal - Contribuintes - Conta débito |
| CH_INSS_FOLHA_MENSAL_CONTRIBUINTES | integer(4) |  | S | INSS Folha Mensal - Contribuintes - Histórico |
| CTB_INSS_FOLHA_MENSAL_RAT_EMP_TERC | integer(4) |  | S | INSS Folha Mensal - RAT/Empresa/Terceiros - Conta débito |
| CH_INSS_FOLHA_MENSAL_RAT_EMP_TERC | integer(4) |  | S | INSS Folha Mensal - RAT/Empresa/Terceiros - Histórico |
| CONTABILIZA_AGRUPADA_INSS_FOLHA_13_SAL | char(1) |  |  | INSS Folha 13 Salario - Contabilizar de forma agrupada conforme apuração previdenciária |
| CTB_INSS_FOLHA_13_SAL_SEGURADOS | integer(4) |  | S | INSS Folha 13 Salario - Segurados - Conta débito |
| CH_INSS_FOLHA_13_SAL_SEGURADOS | integer(4) |  | S | INSS Folha 13 Salario - Segurados - Histórico |
| CTB_INSS_FOLHA_13_SAL_CONTRIBUINTES | integer(4) |  | S | INSS Folha 13 Salario - Contribuintes - Conta débito |
| CH_INSS_FOLHA_13_SAL_CONTRIBUINTES | integer(4) |  | S | INSS Folha 13 Salario - Contribuintes - Histórico |
| CTB_INSS_FOLHA_13_SAL_RAT_EMP_TERC | integer(4) |  | S | INSS Folha 13 Salario - RAT/Empresa/Terceiros - Conta débito |
| CH_INSS_FOLHA_13_SAL_RAT_EMP_TERC | integer(4) |  | S | INSS Folha 13 Salario - RAT/Empresa/Terceiros - Histórico |
| CONTABILIZA_AGRUPADA_INSS_RET | char(1) |  |  | INSS Retido - Contabilizar de forma agrupada conforme apuração previdenciária |
| CTB_INSS_RET_RECOLHER | integer(4) |  | S | INSS Retido - Encargo a Recolher - Conta débito |
| CH_INSS_RET_RECOLHER | integer(4) |  | S | INSS Retido - Encargo a Recolher - Histórico |
| CONTABILIZA_AGRUPADA_FUNRURAL | char(1) |  |  | FUNRURAL - Contabilizar de forma agrupada conforme apuração previdenciária |
| CTB_FUNRURAL_RECOLHER | integer(4) |  | S | FUNRURAL - Encargo a Recolher - Conta débito |
| CH_FUNRURAL_RECOLHER | integer(4) |  | S | FUNRURAL - Encargo a Recolher - Histórico |
| CONTABILIZA_AGRUPADA_INSS_RB | char(1) |  |  | INSS RB - Contabilizar de forma agrupada conforme apuração previdenciária |
| CTB_INSS_RB_RECOLHER | integer(4) |  | S | INSS RB - Encargo a Recolher - Conta débito |
| CH_INSS_RB_RECOLHER | integer(4) |  | S | INSS RB - Encargo a Recolher - Histórico |
| CONTABILIZA_AGRUPADA_SALDO_COMPENSAR | char(1) |  |  | Saldo a compensar - Contabilizar de forma agrupada conforme apuração previdenciária |
| CTC_SALDO_COMPENSAR_DCOMP | integer(4) |  | S | Saldo a compensar - Compensação DCOMP - Conta crédito |
| CH_SALDO_COMPENSAR_DCOMP | integer(4) |  | S | Saldo a compensar - Compensação DCOMP - Histórico |
| CTC_SALDO_COMPENSAR_SAL_FAMILIA | integer(4) |  | S | Saldo a compensar - Salário Família - Conta crédito |
| CH_SALDO_COMPENSAR_SAL_FAMILIA | integer(4) |  | S | Saldo a compensar - Salário Família - Histórico |
| CTC_SALDO_COMPENSAR_SAL_MATERNIDADE | integer(4) |  | S | Saldo a compensar - Salário Maternidade - Conta crédito |
| CH_SALDO_COMPENSAR_SAL_MATERNIDADE | integer(4) |  | S | Saldo a compensar - Salário Maternidade - Histórico |
| CTC_SALDO_COMPENSAR_RETENCOES | integer(4) |  | S | Saldo a compensar - Retenções - Conta crédito |
| CH_SALDO_COMPENSAR_RETENCOES | integer(4) |  | S | Saldo a compensar - Retenções - Histórico |
| CTC_PAGAMENTO_VALOR_PRINCIPAL | integer(4) |  | S | Pagamento - Valor Principal - Conta crédito |
| CH_PAGAMENTO_VALOR_PRINCIPAL | integer(4) |  | S | Pagamento - Valor Principal - Histórico |
| CTB_PAGAMENTO_MULTA | integer(4) |  | S | Pagamento - Multa - Conta débito |
| CTC_PAGAMENTO_MULTA | integer(4) |  | S | Pagamento - Multa - Conta crédito |
| CH_PAGAMENTO_MULTA | integer(4) |  | S | Pagamento - Multa - Histórico |
| CTB_PAGAMENTO_JUROS | integer(4) |  | S | Pagamento - Juros - Conta débito |
| CTC_PAGAMENTO_JUROS | integer(4) |  | S | Pagamento - Juros - Conta crédito |
| CH_PAGAMENTO_JUROS | integer(4) |  | S | Pagamento - Juros - Histórico |
| CTB_PAGAMENTO_VALOR_PAGO_MAIOR | integer(4) |  | S | Pagamento - Valor pago a maior - Conta débito |
| CTC_PAGAMENTO_VALOR_PAGO_MAIOR | integer(4) |  | S | Pagamento - Valor pago a maior - Conta crédito |
| CH_PAGAMENTO_VALOR_PAGO_MAIOR | integer(4) |  | S | Pagamento - Valor pago a maior - Histórico |
| CTB_IRRF_FOLHA_ENCARGO_RECOLHER | integer(4) |  | S | IRRF Folha - Encargo a recolher - Conta débito |
| CTC_IRRF_FOLHA_ENCARGO_RECOLHER | integer(4) |  | S | IRRF Folha - Encargo a recolher - Conta crédito |
| CH_IRRF_FOLHA_ENCARGO_RECOLHER | integer(4) |  | S | IRRF Folha - Encargo a recolher - Histórico |
| CTB_INSS_FOLHA_MENSAL_SEST_SENAT | integer(4) |  | S | INSS Folha Mensal - INSS SEST/SENAT Folha - Conta débito |
| CH_INSS_FOLHA_MENSAL_SEST_SENAT | integer(4) |  | S | INSS Folha Mensal - INSS SEST/SENAT Folha - Histórico |
| CTB_INSS_FOLHA_MENSAL_EMPRESAS_RAT | integer(4) |  | S | INSS Folha Mensal - INSS Empresas e RAT Folha - Conta débito |
| CH_INSS_FOLHA_MENSAL_EMPRESAS_RAT | integer(4) |  | S | INSS Folha Mensal - INSS Empresas e RAT Folha - Histórico |
| CTB_INSS_FOLHA_MENSAL_TERCEIROS | integer(4) |  | S | INSS Folha Mensal - INSS Terceiros - Conta débito |
| CH_INSS_FOLHA_MENSAL_TERCEIROS | integer(4) |  | S | INSS Folha Mensal - INSS Terceiros - Histórico |
| CONTABILIZA_AGRUPADA_IRRF_FOLHA | char(1) |  |  | IRRF Folha - Contabilizar de forma agrupada conforme apuração dos Tributos Federais |
| CTB_INSS_FOLHA_13_SAL_EMPRESAS_RAT | integer(4) |  | S | INSS Folha 13 Salario - INSS Empresas e RAT Folha - Conta débito |
| CH_INSS_FOLHA_13_SAL_EMPRESAS_RAT | integer(4) |  | S | INSS Folha 13 Salario - INSS Empresas e RAT Folha - Histórico |
| CTB_INSS_FOLHA_13_SAL_TERCEIROS | integer(4) |  | S | INSS Folha 13 Salario - INSS Terceiros - Conta débito |
| CH_INSS_FOLHA_13_SAL_TERCEIROS | integer(4) |  | S | INSS Folha 13 Salario - INSS Terceiros - Histórico |
| CONTABILIZA_AGRUPADA_IRRF_ESCRITA | char(1) |  | S | CONTABILIZA_AGRUPADA_IRRF_ESCRITA (S-Sim/N=Não) |
| CTB_TRIBUTOS_IRRF_ESCRITA | integer(4) |  | S | Tributos - IRRF Escrita - Conta Débito |
| CH_TRIBUTOS_IRRF_ESCRITA | integer(4) |  | S | Tributos - IRRF Escrita - HIstórico |
| CONTABILIZA_AGRUPADA_PIS_RETIDO | char(1) |  | S | CONTABILIZA_AGRUPADA_PIS_RETIDO (S-Sim/N=Não) |
| CTB_TRIBUTOS_PIS_RETIDO | integer(4) |  | S | Tributos - PIS Retido - Conta Débito |
| CH_TRIBUTOS_PIS_RETIDO | integer(4) |  | S | Tributos - PIS Retido - Histórico |
| CONTABILIZA_AGRUPADA_COFINS_RETIDO | char(1) |  | S | CONTABILIZA_AGRUPADA_COFINS_RETIDO (S-Sim/N=Não) |
| CTB_TRIBUTOS_COFINS_RETIDO | integer(4) |  | S | Tributos - COFINS Retido - Conta Débito |
| CH_TRIBUTOS_COFINS_RETIDO | integer(4) |  | S | Tributos - COFINS Retido - Histórico |
| CONTABILIZA_AGRUPADA_CSOC_RETIDO | char(1) |  | S | CONTABILIZA_AGRUPADA_CSOC_RETIDO (S-Sim/N=Não) |
| CTB_TRIBUTOS_CSOC_RETIDO | integer(4) |  | S | Tributos - CSOC Retido - Conta Débito |
| CH_TRIBUTOS_CSOC_RETIDO | integer(4) |  | S | Tributos - CSOC Retido - HIstórico |
| CONTABILIZA_AGRUPADA_CRF | char(1) |  | S | CONTABILIZA_AGRUPADA_CRF (S-Sim/N=Não) |
| CTB_TRIBUTOS_CRF | integer(4) |  | S | Tributos - CRF - Conta Débito |
| CH_TRIBUTOS_CRF | integer(4) |  | S | Tributos - CRF - Histórico |
| CONTABILIZA_AGRUPADA_COSIRF | char(1) |  | S | CONTABILIZA_AGRUPADA_COSIRF (S-Sim/N=Não) |
| CTB_TRIBUTOS_COSIRF | integer(4) |  | S | Tributos - COSIRF - Conta Débito |
| CH_TRIBUTOS_COSIRF | integer(4) |  | S | Tributos - COSIRF - Histórico |
| CONTABILIZA_AGRUPADA_IRRFP | char(1) |  | S | CONTABILIZA_AGRUPADA_IRRFP (S-Sim/N=Não) |
| CTB_TRIBUTOS_IRRFP | integer(4) |  | S | Tributos - IRRFP - Conta Débito |
| CH_TRIBUTOS_IRRFP | integer(4) |  | S | Tributos - IRRFP - Histórico |
| CONTABILIZA_AGRUPADA_IRRFAPF | char(1) |  | S | CONTABILIZA_AGRUPADA_IRRFAPF (S-Sim/N=Não) |
| CTB_TRIBUTOS_IRRF_APF | integer(4) |  | S | Tributos - IRRFAPF - Conta Débito |
| CH_TRIBUTOS_IRRF_APF | integer(4) |  | S | Tributos - IRRFAPF - Histórico |
| CONTABILIZA_AGRUPADA_PIS_FOLHA | char(1) |  | S | CONTABILIZA_AGRUPADA_PIS_FOLHA (S-Sim/N=Não) |
| CTB_TRIBUTOS_PIS_FOLHA | integer(4) |  | S | Tributos - PIS Folha - Conta Débito |
| CH_TRIBUTOS_PIS_FOLHA | integer(4) |  | S | Tributos - PIS Folha - Histórico |
| CONTABILIZA_AGRUPADA_IPI | char(1) |  |  | IPI - Contabilizar de forma agrupada conforme apuração dos Tributos federais |
| CTB_TRIBUTOS_IPI | integer(4) |  | S | Tributos - IPI - Conta Débito |
| CH_TRIBUTOS_IPI | integer(4) |  | S | Tributos - IPI - Histórico |
| CONTABILIZA_AGRUPADA_CSLL | char(1) |  |  | CSLL - Contabilizar de forma agrupada conforme apuração dos Tributos federais |
| CTB_TRIBUTOS_CSLL | integer(4) |  | S | Tributos - CSLL - Conta Débito |
| CH_TRIBUTOS_CSLL | integer(4) |  | S | Tributos - CSLL - Histórico |
| CONTABILIZA_AGRUPADA_IRPJ | char(1) |  |  | IRPJ - Contabilizar de forma agrupada conforme apuração dos Tributos federais |
| CTB_TRIBUTOS_IRPJ | integer(4) |  | S | Tributos - IRPJ - Conta Débito |
| CH_TRIBUTOS_IRPJ | integer(4) |  | S | Tributos - IRPJ - Histórico |
| CONTABILIZA_AGRUPADA_PIS | char(1) |  |  | PIS - Contabilizar de forma agrupada conforme apuração dos Tributos federais |
| CTB_TRIBUTOS_PIS | integer(4) |  | S | Tributos - PIS - Conta Débito |
| CH_TRIBUTOS_PIS | integer(4) |  | S | Tributos - PIS - Histórico |
| CTB_TRIBUTOS_PIS_NC | integer(4) |  | S | Tributos - PIS_NC - Conta Débito |
| CH_TRIBUTOS_PIS_NC | integer(4) |  | S | Tributos - PIS_NC - Histórico |
| CTB_TRIBUTOS_PIS_SUBTRI | integer(4) |  | S | Tributos - PIS_SUBTRI - Conta Débito |
| CH_TRIBUTOS_PIS_SUBTRI | integer(4) |  | S | Tributos - PIS_SUBTRI - Histórico |
| CTB_TRIBUTOS_PIS_ENTIDADES_FINANCEIRAS | integer(4) |  | S | Tributos - PIS_ENTIDADES_FINANCEIRAS - Conta Débito |
| CH_TRIBUTOS_PIS_ENTIDADES_FINANCEIRAS | integer(4) |  | S | Tributos - PIS_ENTIDADES_FINANCEIRAS - Histórico |
| CTB_TRIBUTOS_PIS_IMPORTACAO | integer(4) |  | S | Tributos - PIS_IMPORTACAO - Conta Débito |
| CH_TRIBUTOS_PIS_IMPORTACAO | integer(4) |  | S | Tributos - PIS_IMPORTACAO - Histórico |
| CTB_TRIBUTOS_PIS_CODIGO_RECOLHIMENTO | integer(4) |  | S | Tributos - PIS_CODIGO_RECOLHIMENTO - Conta Débito |
| CH_TRIBUTOS_PIS_CODIGO_RECOLHIMENTO | integer(4) |  | S | Tributos - PIS_CODIGO_RECOLHIMENTO - Histórico |
| CTB_TRIBUTOS_PIS_NC_CODIGO_RECOLHIMENTO | integer(4) |  | S | Tributos - PIS_NC_CODIGO_RECOLHIMENTO - Conta Débito |
| CH_TRIBUTOS_PIS_NC_CODIGO_RECOLHIMENTO | integer(4) |  | S | Tributos - PIS_NC_CODIGO_RECOLHIMENTO - Histórico |
| CONTABILIZA_AGRUPADA_COFINS | char(1) |  |  | COFINS - Contabilizar de forma agrupada conforme apuração dos Tributos federais |
| CTB_TRIBUTOS_COFINS | integer(4) |  | S | Tributos - COFINS - Conta Débito |
| CH_TRIBUTOS_COFINS | integer(4) |  | S | Tributos - COFINS - Histórico |
| CTB_TRIBUTOS_COFINS_NC | integer(4) |  | S | Tributos - COFINS_NC - Conta Débito |
| CH_TRIBUTOS_COFINS_NC | integer(4) |  | S | Tributos - COFINS_NC - Histórico |
| CTB_TRIBUTOS_COFINS_SUBTRI | integer(4) |  | S | Tributos - COFINS_SUBTRI - Conta Débito |
| CH_TRIBUTOS_COFINS_SUBTRI | integer(4) |  | S | Tributos - COFINS_SUBTRI - Histórico |
| CTB_TRIBUTOS_COFINS_ENTIDADES_FINANCEIRAS | integer(4) |  | S | Tributos - COFINS_ENTIDADES_FINANCEIRAS - Conta Débito |
| CH_TRIBUTOS_COFINS_ENTIDADES_FINANCEIRAS | integer(4) |  | S | Tributos - COFINS_ENTIDADES_FINANCEIRAS - Histórico |
| CTB_TRIBUTOS_COFINS_IMPORTACAO | integer(4) |  | S | Tributos - COFINS_IMPORTACAO - Conta Débito |
| CH_TRIBUTOS_COFINS_IMPORTACAO | integer(4) |  | S | Tributos - COFINS_IMPORTACAO - Histórico |
| CTB_TRIBUTOS_COFINS_CODIGO_RECOLHIMENTO | integer(4) |  | S | Tributos - COFINS_CODIGO_RECOLHIMENTO - Conta Débito |
| CH_TRIBUTOS_COFINS_CODIGO_RECOLHIMENTO | integer(4) |  | S | Tributos - COFINS_CODIGO_RECOLHIMENTO - Histórico |
| CTB_TRIBUTOS_COFINS_NC_CODIGO_RECOLHIMENTO | integer(4) |  | S | Tributos - COFINS_NC_CODIGO_RECOLHIMENTO - Conta Débito |
| CH_TRIBUTOS_COFINS_NC_CODIGO_RECOLHIMENTO | integer(4) |  | S | Tributos - COFINS_NC_CODIGO_RECOLHIMENTO - Histórico |
| CONTABILIZA_AGRUPADA_IOF | char(1) |  |  | IOF - Contabilizar de forma agrupada conforme apuração dos Tributos federais |
| CTB_TRIBUTOS_IOF | integer(4) |  | S | Tributos - IOF - Conta Débito |
| CH_TRIBUTOS_IOF | integer(4) |  | S | Tributos - IOF - Histórico |
| CONTABILIZA_AGRUPADA_CIDE | char(1) |  |  | CIDE - Contabilizar de forma agrupada conforme apuração dos Tributos federais |
| CTB_TRIBUTOS_CIDE | integer(4) |  | S | Tributos - CIDE - Conta Débito |
| CH_TRIBUTOS_CIDE | integer(4) |  | S | Tributos - CIDE - Histórico |
| CONTABILIZA_AGRUPADA_RET_PAG_UNIF | char(1) |  |  | RET_PAG_UNIF - Contabilizar de forma agrupada conforme apuração dos Tributos federais |
| CTB_TRIBUTOS_RET_PAG_UNIF | integer(4) |  | S | Tributos - RET_PAG_UNIF - Conta Débito |
| CH_TRIBUTOS_RET_PAG_UNIF | integer(4) |  | S | Tributos - RET_PAG_UNIF - Histórico |
| CTB_TRIBUTOS_RET_PIS | integer(4) |  | S | Tributos - RET_PIS - Conta Débito |
| CH_TRIBUTOS_RET_PIS | integer(4) |  | S | Tributos - RET_PIS - Histórico |
| CTB_TRIBUTOS_RET_COFINS | integer(4) |  | S | Tributos - RET_COFINS - Conta Débito |
| CH_TRIBUTOS_RET_COFINS | integer(4) |  | S | Tributos - RET_COFINS - Histórico |
| CTB_TRIBUTOS_RET_IRPJ | integer(4) |  | S | Tributos - RET_IRPJ - Conta Débito |
| CH_TRIBUTOS_RET_IRPJ | integer(4) |  | S | Tributos - RET_IRPJ - Histórico |
| CTB_TRIBUTOS_RET_CSLL | integer(4) |  | S | Tributos - RET_CSLL - Conta Débito |
| CH_TRIBUTOS_RET_CSLL | integer(4) |  | S | Tributos - RET_CSLL - Histórico |
| CTB_TRIBUTOS_RET_PMCMV | integer(4) |  | S | Tributos - RET_PMCMV - Conta Débito |
| CH_TRIBUTOS_RET_PMCMV | integer(4) |  | S | Tributos - RET_PMCMV - Histórico |
| CTB_TRIBUTOS_RET_PIS_PMCMV | integer(4) |  | S | Tributos - RET_PIS_PMCMV - Conta Débito |
| CH_TRIBUTOS_RET_PIS_PMCMV | integer(4) |  | S | Tributos - RET_PIS_PMCMV - Histórico |
| CTB_TRIBUTOS_RET_COFINS_PMCMV | integer(4) |  | S | Tributos - RET_COFINS_PMCMV - Conta Débito |
| CH_TRIBUTOS_RET_COFINS_PMCMV | integer(4) |  | S | Tributos - RET_COFINS_PMCMV - Histórico |
| CTB_TRIBUTOS_RET_IRPJ_PMCMV | integer(4) |  | S | Tributos - RET_IRPJ_PMCMV - Conta Débito |
| CH_TRIBUTOS_RET_IRPJ_PMCMV | integer(4) |  | S | Tributos - RET_IRPJ_PMCMV - Histórico |
| CTB_TRIBUTOS_RET_CSLL_PMCMV | integer(4) |  | S | Tributos - RET_CSLL_PMCMV - Conta Débito |
| CH_TRIBUTOS_RET_CSLL_PMCMV | integer(4) |  | S | Tributos - RET_CSLL_PMCMV - Histórico |
