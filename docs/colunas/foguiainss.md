# foguiainss — Guia de INSS
20.627 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_GUIAINSS_OLD | integer(4) |  | S | Sequencial da Guia - Renomeado |
| codi_emp | integer(4) |  |  | Codigo da empresa |
| competencia | date(4) |  |  | Competencia da Guia |
| tipo_servico | integer(4) |  |  | tipo_servico |
| tipo_guia | integer(4) |  |  | Tipo da guia: 1=Normal/2=Apenas terceiros/3=Normal CCT/4=Apenas terceiros CCT |
| i_filiais | integer(4) |  |  | Código da filial |
| tipo_process | integer(4) |  |  | Tipo de calculo: 11=Mensal/42=Complementar/52=13o. salario/91=Resilicao Professor |
| vencimento | date(4) |  |  | Data de vencimento |
| I_GUIAINSS_INI_ACUM_OLD | integer(4) |  | S | Inicio do acumulo - Renomeado |
| situacao | tinyint(1) |  |  | Se a guia esta acumulada(1=Emitida, 2=Acumulada) |
| valor_inss | numeric(13) |  |  | Valor do Inss(campo 6 da GPS) |
| terceiros_guia | numeric(13) |  |  | Valor outras entidades(campo 9 da GPS) |
| multa | numeric(13) |  |  | Valor da multa |
| total_guia | numeric(13) |  |  | Total da guia(campo 11 da GPS) |
| empresa | numeric(13) |  |  | Valor inss empresa |
| segurados | numeric(13) |  |  | Valor INSS segurados |
| acid_trab | numeric(13) |  |  | Valor RAT |
| terceiros | numeric(13) |  |  | Valor de terceiros do mes |
| deducoes_comp | numeric(13) |  |  | Valor deduções compensado (sem uso após a separação do SF e SM) |
| deducoes_acomp | numeric(13) |  |  | Valor deduções a compensar (sem uso após a separação do SF e SM) |
| cooperativas | numeric(13) |  |  | Valor pagos a cooperativas |
| retencao_mes_acomp | numeric(13) |  |  | Valor de INSS retido do mes |
| retencao_mes_comp | numeric(13) |  |  | Valor de INSS retido compensado no proprio mês |
| retencao_comp_100 | numeric(13) |  |  | Valor de INSS retido compensado 100% de outros mes |
| retencao_comp_30 | numeric(13) |  |  | Valor de INSS retido compensado 30% de outros mes |
| acompensar_mes | numeric(13) |  |  | Valor do mes a compesar |
| acomp_100 | numeric(13) |  |  | Valores de outras competencias a 100% compensar no mes |
| acomp_30 | numeric(13) |  |  | Valores de outras competencias a 30% compensar no mes |
| acomp_inicio | date(4) |  | S | Data inicio compencacao |
| acomp_fim | date(4) |  | S | Data fim compensacao |
| i_pagto | integer(4) |  | S | Sequencial de pagamento |
| DEDUCOES_COMP_SF | numeric(13) |  |  | Valor deduçõs salário família compensado |
| DEDUCOES_COMP_SM | numeric(13) |  |  | Valor deduções salário maternidade compensado |
| DEDUCOES_ACOMP_SF | numeric(13) |  |  | Valor deduçõs salário família a compensar |
| DEDUCOES_ACOMP_SM | numeric(13) |  |  | Valor deduções salário maternidade a compensar |
| COMPETENCIA_RETROATIVA | date(4) |  | S | Competência retroativa (Alteração salarial CCT) |
| DED_COMP_DIF_INSS_13_DESC_MAIOR | numeric(13) |  |  | Valor deduções diferença INSS 13º descontado a maior compensado |
| DED_ACOMP_DIF_INSS_13_DESC_MAIOR | numeric(13) |  |  | Valor deduções diferença INSS 13º descontado a maior a compensar |
| INSENCAO_FILANTROPIA_EMPRESA | numeric(13) |  | S | Isenção Filantropia INSS Empresa |
| INSENCAO_FILANTROPIA_RAT | numeric(13) |  | S | Isenção Filantropia INSS RAT |
| SOMOU_ENCARGOS_NA_FOLHA_MENSAL | smallint(2) |  |  | Somou encargos da folha complementar na folha mensal quando forem inferiores ao mínimo de recolhimento. (0=Não/1=Sim) |
| I_PARCELAMENTO_ENCARGO_PAGAMENTO | integer(4) |  | S | Código do parcelamento. |
| I_PARCELAMENTO_ITEM | integer(4) |  | S | Código do item do parcelamento. |
| VALOR_PARCELADO | numeric(13) |  | S | Valor parcelado no parcelamento. |
| DEDUCOES_COMP_SF_RETROATIVO | numeric(13) |  | S | Valor deduções salário família retroativo compensado |
| DEDUCOES_ACOMP_SF_RETROATIVO | numeric(13) |  | S | Valor deduções salário família retroativo a compensar |
| SALDO_RETENCAO_ACOMP | numeric(13) |  |  | Saldo de retenção para ser compensado em meses posteriores. |
| VALOR_COMPENSADO_RETENCAO_MESES_ANTERIORES | numeric(13) |  |  | Valor compensado do saldo de retenção dos meses anteriores. |
| VALOR_COMPENSADO_RETENCAO_13 | numeric(13) |  |  | Valor compensado do lançamento de compensação no mês devido à retenção de 13º salário. |
| EMPRESA_AVISO_PREVIO | numeric(13) |  |  | Valor inss empresa Aviso Prévio |
| SEGURADOS_AVISO_PREVIO | numeric(13) |  |  | Valor INSS segurados Aviso Prévio |
| ACID_TRAB_AVISO_PREVIO | numeric(13) |  |  | Valor RAT Aviso Prévio |
| TERCEIROS_AVISO_PREVIO | numeric(13) |  |  | Valor de terceiros do mês Aviso Prévio |
| ISENCAO_FILANTROPIA_EMPRESA_AVISO_PREVIO | numeric(13) |  |  | Isenção Filantropia INSS Empresa Aviso Prévio |
| ISENCAO_FILANTROPIA_RAT_AVISO_PREVIO | numeric(13) |  |  | Isenção Filantropia INSS RAT Aviso Prévio |
| DEDUCOES_COMP_DIF_SM | numeric(13) |  | S | Deduções compensação de diferença de salário maternidade. |
| DEDUCOES_ACOMP_DIF_SM | numeric(13) |  | S | Deduções a compensar de diferença de salário maternidade. |
| GUIA_APENAS_PATRONAL | integer(4) |  |  | Campo para identificar que a guia esta considerando apenas os valores patronais recolhimento portaria 139/2020 |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_GUIAINSS | uniqueidentifier(16) | PK |  | Sequencial da Guia |
| I_GUIAINSS_INI_ACUM | uniqueidentifier(16) |  | S | Inicio do acumulo |
| I_GUIAINSS_EXPORTA_IMPORTA | uniqueidentifier(16) |  | S | Coluna utilizada durante o exporta/importa |
| GUIA_DATA_HORA | timestamp(8) |  | S | Data e hora da gravação da guia |
