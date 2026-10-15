# foeventos — Eventos - Cadastro
1.306.923 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_eventos | integer(4) | PK |  | Codigo |
| nome | char(50) |  |  | Nome |
| prov_desc | varchar(2) |  |  | Tipo |
| tipo_inf | char(1) |  |  | Unidade |
| tipo_base | char(1) |  | S | Tipo base |
| base_irrf | char(1) |  | S | IRRF |
| base_inss | char(1) |  | S | INSS |
| base_fgts | char(1) |  | S | FGTS |
| base_sindicato | char(1) |  | S | Sindicato |
| base_hextra | char(1) |  | S | Horas extras |
| base_periculosidade | char(1) |  | S | Periculosidade |
| base_aux1 | char(1) |  | S | Auxiliar 1 |
| base_aux2 | char(1) |  | S | Auxiliar 2 |
| base_aux3 | char(1) |  | S | Auxiliar 3 |
| horas_mes | char(1) |  |  | Compoe horas mes |
| soma_med_13 | char(1) |  |  | Soma media 13 |
| soma_med_fer | char(1) |  |  | Soma media ferias |
| comp_13fer | char(1) |  |  | Computa 13/Ferias |
| soma_fic_fin | char(1) |  |  | Ficha financeira |
| soma_rais | char(1) |  |  | Sai na RAIS |
| soma_inf_ren | char(1) |  |  | Comprovante de rendimento |
| paga_prop | char(1) |  |  | Paga proporcional |
| aparece_recibo | char(1) |  |  | Aparece no Recibo |
| soma_sal_base | char(1) |  |  | Salario Base |
| taxa | numeric(7) |  |  | Taxa/Valor |
| ordem_calculo | integer(4) |  |  | Ordem calculo |
| classificacao | integer(4) |  |  | Classificacao |
| rend_tributaveis | tinyint(1) |  |  | Rendimentos tributaveis |
| rend_isentos | tinyint(1) |  |  | rendimentos isentos e nao tributaveis |
| rend_sujeitos | tinyint(1) |  |  | Rendimento sujeito a tributação exclusiva. (0=Não informar/1=Décimo terceiro salário/2=Outros/3=Participação de lucros/4=Juros sobre o Capital Próprio) |
| base_pis | char(1) |  | S | PIS |
| rend_adicionais | tinyint(1) |  | S | informacoes complementares |
| base_rdsr | char(1) |  | S | Reflexo DSR |
| base_rdsr_eve | integer(4) |  | S | Evento para base DSR |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| soma_med_afast | char(1) |  |  | Se soma média quando o empregado esta afastado |
| soma_med_afast_02 | char(1) |  |  | Soma media afast. direitos integrais |
| soma_med_afast_03 | char(1) |  |  | Soma media afast. Acidente de Trabalho |
| soma_med_afast_04 | char(1) |  |  | Soma media afast. Serviço Militar |
| soma_med_afast_05 | char(1) |  |  | Soma media afast. Auxílio maternidade |
| soma_med_afast_06 | char(1) |  |  | Soma media afast. Auxílio doença |
| soma_med_afast_07 | char(1) |  |  | Soma media afast. Licença sem vencimentos |
| soma_med_afast_13 | char(1) |  |  | Soma media afast. Exerc  Mandato Sindical |
| soma_med_afast_14 | char(1) |  |  | Soma media afast. Aposent  invalidez |
| soma_med_afast_24 | char(1) |  |  | Soma media afast. Outros motivos afastamentos |
| i_cadbases | integer(4) |  | S | Codigo da base |
| calc_afast | char(1) |  |  | Calcular durante o afastamento |
| adic_afast | char(1) |  |  | Adicional no afastamento |
| i_horasaula | integer(4) |  | S | Horas-aula |
| CALC_AFAST_02 | char(1) |  |  | CALCULA DURANTE O AFAST. DIREITOS INTEGRAIS |
| CALC_AFAST_03 | char(1) |  |  | CALCULA DURANTE O AFAST. ACIDENTE DE TRABALHO |
| CALC_AFAST_04 | char(1) |  |  | CALCULA DURANTE O AFAST. SERVIÇO MILITAR |
| CALC_AFAST_05 | char(1) |  |  | CALCULA DURANTE O AFAST. LICENÇA MATERNIDADE |
| CALC_AFAST_06 | char(1) |  |  | CALCULA DURANTE O AFAST. AUXÍLIO DOENÇA |
| CALC_AFAST_07 | char(1) |  |  | CALCULA DURANTE O AFAST. LICENÇA SEM VENCIMENTOS |
| CALC_AFAST_13 | char(1) |  |  | CALCULA DURANTE O AFAST. EXERC MANDATO SINDICAL |
| CALC_AFAST_14 | char(1) |  |  | CALCULA DURANTE O AFAST. APOSENT  INVALIDEZ |
| CALC_AFAST_24 | char(1) |  |  | CALCULA DURANTE O AFAST. OUTROS MOTIVOS AFASTAMENTOS |
| CALC_FIXO_FER | tinyint(1) |  |  | Calcula evento fixo nas ferias.(0-Nao/1-Sim) |
| CALC_FIXO_FER_EVE | integer(4) |  | S | Evento para calcular fixo nas ferias. |
| CALC_FIXO_FER_PROP_MES | tinyint(1) |  |  | Calcula evento proporcional aos dias trabalhados no mes que teve ferias.(0-Nao/1-Sim) |
| CALC_FIXO_FER_PROP_FER | tinyint(1) |  |  | Calcula evento proporcional aos dias de ferias.(0-Nao/1-Sim) |
| CALC_FIXO_13 | tinyint(1) |  |  | Calcula evento fixo no 13o.(0-Nao/1-Sim) |
| CALC_FIXO_13_EVE | integer(4) |  | S | Evento para calcular fixo no 13o. |
| HOMOLOGNET | smallint(2) |  |  | Gerar para o Homolognet 0 nao 1 sim 2 NAo DisponIvel para homolognet |
| RUBRICA | smallint(2) |  | S | Rubrica |
| CODI_RUBRICA | integer(4) |  | S | Rubrica |
| EMITIR_TERMO_RESCISAO | smallint(2) |  |  | Emitir no Termo de Rescisão |
| CAMPO_TERMO_RESCISAO | char(5) |  | S | Campo para relacionamento no Termo de Rescisão |
| REND_ISENTOS_DESCRICAO | char(60) |  | S | Descrição de Outros Rendimentos Isentos e Não Tributáveis |
| REND_SUJEITOS_DESCRICAO | char(60) |  | S | Descrição de Outros Rendimentos sujeitos à tributação exclusiva(rendimento líquido) |
| SOMA_MED_AFAST_26 | char(1) |  |  | Soma média prorrogação licença maternidade |
| CALC_AFAST_26 | char(1) |  |  | Calcula durante o afastamento prorrogação licença maternidade |
| CORRIGE_MEDIA | smallint(2) |  |  | Corrige média: 0=Não/1=Sim |
| TIPO_CALCULO | smallint(2) |  |  | Tipo do cálculo: 1=Automático/2=Lançado |
| CALC_FIXO_13_DESC_ADIANT_13 | smallint(2) |  |  | Descontar o valor calculado no adiantamento de 13º: (0=Não/1=Sim) |
| CALC_FIXO_ADIANT_13 | smallint(2) |  |  | Calcula evento fixo no adiantamento de 13º: (0=Não/1=Sim) |
| CALC_FIXO_ADIANT_13_EVE | integer(4) |  | S | Evento para calcular fixo no adiantamento de 13º |
| CALC_FIXO_ADIANT_13_PROP | smallint(2) |  |  | Calcular o evento fixo de adiantamento de 13º proporcional ao percentual do 13º adiantado: (0=Não/1=Sim) |
| SOMA_MEDIA_AVISO_PREVIO | smallint(2) |  |  | Soma média aviso prévio: (0=Não/1=Sim) |
| SOMA_ADICIONAL_AVISO_PREVIO | smallint(2) |  |  | Soma adicional aviso prévio: (0=Não/1=Sim) |
| SOMA_MED_AFAST_32 | char(1) |  |  | Soma média afastamento licença paternidade |
| COMPOE_CAMPO_23_TERMO_RESCISAO | smallint(2) |  |  | Compõe o valor do campo 23 - Remuneração mês anterior: (0=Não/1=Sim) |
| SOMA_MEDIA_SALDO_SALARIO | smallint(2) |  |  | Soma para média de saldo de salário: (0=Não/1=Sim) |
| DESCONTA_DSR | smallint(2) |  |  | Desconta no DSR. (0=Não/1=Sim) |
| DESCONTA_DSR_EVENTO | integer(4) |  | S | Evento para desconto no DSR. |
| COMPOE_ADIANTAMENTO_SALARIAL | smallint(2) |  |  | Compõe o adiantamento salarial. (0=Não/1=Sim) |
| COMPOE_LIQUIDO | smallint(2) |  |  | Compõe o líquido: (0=Não/1=Sim) |
| TIPO_CONSIDERACAO_CAMPO_23_TERMO_RESCISAO | smallint(2) |  |  | Tipo de consideração para o campo 23 do recibo de rescisão. ( 0 - Não considerar / 1 - Considerar para remuneração e projeção / 2 - Considerar somente para remuneração  / 3 - Considerar somente para projeção ) |
| CALC_AFAST_35 | char(1) |  | S | Calcula durante o afastamento cárcere. |
| DATA_INICIO | date(4) |  |  | Data de início do evento. |
| SITUACAO | smallint(2) |  |  | Situação do evento. (0=Inativo/1=Ativo) |
| DATA_INATIVACAO | date(4) |  | S | Data de inativação do evento. |
| NATUREZA_FOLHA_MENSAL | integer(4) |  | S | Natureza do evento para a folha mensal. |
| NATUREZA_13_INTEGRAL | integer(4) |  | S | Natureza do evento para o 13º integral. |
| POSSUI_PROCESSO_REFERENTE_SUSPENSAO_INCIDENCIA_ENCARGOS | smallint(2) |  |  | Possui processo administrativo/judicial referente a suspensão de incidência de encargos. (0=Não/1=Sim) |
| POSSUI_PROCESSO_SUSPENSAO_INCIDENCIA_INSS_PATRONAL | smallint(2) |  |  | Possui processo administrativo/judicial referente a suspensão de incidência de INSS Patronal. (0=Não/1=Sim) |
| CODIGO_PROCESSO_SUSPENSAO_INCIDENCIA_INSS_PATRONAL | integer(4) |  | S | Código do processo administrativo/judicial referente a suspensão de incidência de INSS Patronal. |
| POSSUI_PROCESSO_SUSPENSAO_INCIDENCIA_INSS_EMPREGADOS | smallint(2) |  |  | Possui processo administrativo/judicial referente a suspensão de incidência de INSS Empregados. (0=Não/1=Sim) |
| CODIGO_PROCESSO_SUSPENSAO_INCIDENCIA_INSS_EMPREGADOS | integer(4) |  | S | Código do processo administrativo/judicial referente a suspensão de incidência de INSS Empregados. |
| POSSUI_PROCESSO_SUSPENSAO_INCIDENCIA_FGTS | smallint(2) |  |  | Possui processo administrativo/judicial referente a suspensão de incidência de FGTS. (0=Não/1=Sim) |
| CODIGO_PROCESSO_SUSPENSAO_INCIDENCIA_FGTS | integer(4) |  | S | Código do processo administrativo/judicial referente a suspensão de incidência de FGTS. |
| POSSUI_PROCESSO_SUSPENSAO_INCIDENCIA_IRRF | smallint(2) |  |  | Possui processo administrativo/judicial referente a suspensão de incidência de IRRF. (0=Não/1=Sim) |
| CODIGO_PROCESSO_SUSPENSAO_INCIDENCIA_IRRF | integer(4) |  | S | Código do processo administrativo/judicial referente a suspensão de incidência de IRRF. |
| POSSUI_PROCESSO_SUSPENSAO_INCIDENCIA_SINDICAL | smallint(2) |  |  | Possui processo administrativo/judicial referente a suspensão de incidência sindical. (0=Não/1=Sim) |
| CODIGO_PROCESSO_SUSPENSAO_INCIDENCIA_SINDICAL | integer(4) |  | S | Código do processo administrativo/judicial referente a suspensão de incidência sindical. |
| PERMITE_INFORMAR_NATUREZA_FOLHA_MENSAL | smallint(2) |  |  | Permite informar a natureza para a folha mensal. (0=Não/1=Sim) |
| PERMITE_INFORMAR_NATUREZA_13_INTEGRAL | smallint(2) |  |  | Permite informar a natureza para o 13º integral. (0=Não/1=Sim) |
| CODIGO_ESOCIAL | varchar(30) |  | S | Código no eSocial. |
| CONSIDERAR_FALTAS_PAGAMENTO_PROPORCIONAL | smallint(2) |  | S | Considerar as faltas para o pagamento proporcional. (0=Não/1=Sim) |
| CALCULA_DIFERENCA_ALTERACAO_PISO_SALARIAL | smallint(2) |  |  | Calcula diferença devido alteração piso salarial. (0=Não/1=Sim) |
| I_EVENTOS_DIFERENCA_PISO_SALARIAL | integer(4) |  | S | Código do evento para pagamento da diferença do piso salarial. |
| PERMITE_CALCULAR_DIFERENCA_PISO_SALARIAL | smallint(2) |  |  | Permite calcular a diferença devido alteração piso salarial. (0=Não/1=Sim) |
| CALC_AFAST_39 | char(1) |  | S | CALCULA DURANTE O AFAST. AUSENCIA JUSTIFICADA |
| TIPO_VALOR_CONSIDERAR_CALCULO_MEDIAS | smallint(2) |  | S | Tipo de valor a considerar para o cálculo de médias. (1=Valor informado/2=Valor calculado) |
| DETALHAR_LANCAMENTO_POR_SERVICO | smallint(2) |  |  | Detalhar lançamentos por serviço. (0=Não/1=Sim) |
| CALC_FIXO_ADIANT_13_EVE_MENSAL | integer(4) |  | S | Evento para cálculo do 13º adiantamento na folha mensal. |
| CALC_FIXO_ADIANT_13_MENSAL | smallint(2) |  |  | Calcula evento fixo de adiantamento de 13º salário na folha mensal. (0=Não/1=Sim) |
| CALC_FIXO_ADIANT_13_PROP_MENSAL | smallint(2) |  |  | Calcula evento fixo de adiantamento de 13º salário proporcional ao percentual de 13º adiantado na folha mensal. (0=Não/1=Sim) |
| SOMA_MED_AFAST_41 | char(1) |  |  | Soma média afastamento Licença maternidade por morte da genitora. |
| CALC_AFAST_41 | char(1) |  |  | Calcula durante o afastamento Licença maternidade por morte da genitora. |
| CALCULA_RATEIO_CONFORME_PERIODO_CADA_SERVICO | smallint(2) |  |  | Calcula rateio conforme período em cada serviço. (0=Não/2=Sim) |
| CALCULAR_DIFERENCA_RUBRICA | smallint(2) |  |  | Calcular diferença da rubrica. (0=Não/1=Sim) |
| I_EVENTOS_DIFERENCA_VALOR | integer(4) |  | S | Código da rubrica que irá pagar a diferença. |
| SOMA_MED_AFAST_50 | char(1) |  |  | Soma média afastamento por doença profissional. |
| CALC_AFAST_50 | char(1) |  |  | Calcula durante o afastamento de doença profissional. |
| GERAR_RUBRICA_SALDO_SALARIO_RESCISAO | smallint(2) |  |  | Gerar a rubrica como saldo de salário na rescisão. (0=Não/1=Sim) |
| RUBRICA_SALDO_SALARIO_RESCISAO | integer(4) |  | S | Rubrica de saldo de salário para gerar na rescisão. |
| CODIGO_INCIDENCIA_IRRF_ESOCIAL | integer(4) |  |  | Código da incidência do IRRF para o eSocial. |
| CODIGO_INCIDENCIA_INSS_ESOCIAL | integer(4) |  |  | Código da incidência do INSS para o eSocial. |
| SOMA_MED_AFAST_19 | char(1) |  |  | Soma média afastamento aborto não criminoso. (S=Sim/N=Não) |
| SOMA_MEDIA_LICENCA_PREMIO | smallint(2) |  |  | Soma média licença prêmio: (0=Não/1=Sim) |
| SOMA_ADICIONAL_LICENCA_PREMIO | smallint(2) |  |  | Soma adicional licença prêmio: (0=Não/1=Sim) |
| SOMA_MED_AFAST_35 | char(1) |  | S | Calcular médias durante o afastamento 35. (N=Não/1=Sim) |
| CONSIDERAR_FALTAS_PARCIAIS_CALCULO_PROPORCIONAL | smallint(2) |  |  | Considerar as faltas parciais para o cálculo proporcional. (0=Não/1=Sim) |
| CONSIDERAR_FALTAS_DSR_CALCULO_PROPORCIONAL | smallint(2) |  |  | Considerar as faltas DSR para o cálculo proporcional. (0=Não/1=Sim) |
| CONSIDERAR_FALTAS_NOTURNAS_CALCULO_PROPORCIONAL | smallint(2) |  |  | Considerar as faltas noturnas para o cálculo proporcional. (0=Não/1=Sim) |
| CODIGO_INCIDENCIA_FGTS_ESOCIAL | integer(4) |  | S | Código de incidência do FGTS para o eSocial. |
| SOMA_MED_AFAST_20 | char(1) |  |  | Soma média afastamentos 20, 21, 22, 27, 28 e 29. (N=Não/S=Sim) |
| CODIGO_INCIDENCIA_SINDICAL_ESOCIAL | integer(4) |  | S | Código de incidência sindical para o eSocial. |
| GUID_CONTABIL | uniqueidentifier(16) |  |  | Identificador único do registro no banco do Contábil |
| GUID_ONVIO | uniqueidentifier(16) |  | S | Identificador único do registro no banco do Atendimento Onvio |
| ENDPOINT_EXCLUSAO | varchar(1024) |  | S | Endpoint utilizado para a exclusão do registro. |
| SOMA_MED_AFAST_59 | char(1) |  |  | Soma média afastamento suspensão sem ajuda compensatória. |
| SOMA_MED_AFAST_60 | char(1) |  |  | Soma média afastamento suspensão com ajuda compensatória. |
| CALC_AFAST_59 | char(1) |  |  | Calcula durante o afastamento suspensão sem ajuda compensatória. |
| CALC_AFAST_60 | char(1) |  |  | Calcula durante o afastamento suspensão com ajuda compensatória. |
| UTILIZA_PARA_ESOCIAL_DOMESTICO | smallint(2) |  |  | Utiliza para o eSocial Doméstico |
| CODIGO_ESOCIAL_DOMESTICO | varchar(15) |  | S | Código eSocial Doméstico |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| aparece_relatorio | char(1) |  |  | Aparece no Relatório. |
| CODIGO_INCIDENCIA_RPPS_ESOCIAL | integer(4) |  | S | Código de incidência do RPPS para o eSocial. |
| SOMA_MED_AFAST_39 | char(1) |  |  | Soma média afastamento ausência justificada. |
| CODIGO_INCIDENCIA_PIS_ESOCIAL | integer(4) |  | S | Código de incidência do PIS para o eSocial |
| CALC_FIXO_FER_EVE_RESC | integer(4) |  | S | Evento de férias para calcular na rescisão. |
| CALC_FIXO_13_RESC | tinyint(1) |  | S | Calcula evento fixo de 13o na rescisão.(0-Nao/1-Sim) |
| CALC_FIXO_13_EVE_RESC | integer(4) |  | S | Evento 13o para calcular fixo na rescisão. |
| CALC_AFAST_90 | char(1) |  |  | Calcula durante o afastamento - Suspensão contratual decorrente ação trabalhista por rescisão indireta. |
| CALC_AFAST_91 | char(1) |  |  | Calcula durante o afastamento - Suspensão contratual para inquérito de apuração de falta grave. |
| SOMA_MED_AFAST_90 | char(1) |  |  | Soma Média Afastamento - Suspensão contratual decorrente ação trabalhista por rescisão indireta. |
| SOMA_MED_AFAST_91 | char(1) |  |  | Soma Média Afastamento - Suspensão contratual para inquérito de apuração de falta grave. |
| GERADA_POR_IA | tinyint(1) |  |  | Indica se a rubrica foi gerada por IA (0-Nao/1-Sim) |
