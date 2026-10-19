# Módulo `pessoal_nucleo`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `foavisosconf_consultar` | consultar | foavisosconf | — | ✔ |
| `foavisosconf_obter` | obter | foavisosconf | i_avisosconf | ✔ |
| `foavisosconf_totais` | totais | foavisosconf | — | ✔ |
| `foavisosvencimentos_consultar` | consultar | foavisosvencimentos | empresa | ✔ |
| `foavisosvencimentos_obter` | obter | foavisosvencimentos | empresa, codigo_do_empregado, codigo_sequencial_para_chave_primaria | ✔ |
| `fobancos_consultar` | consultar | fobancos | — | ✔ |
| `fobancos_obter` | obter | fobancos | codigo | ✔ |
| `fobasesirrf_consultar` | consultar | fobasesirrf | — | ✔ |
| `fobasesirrf_obter` | obter | fobasesirrf | numero_sequencial_que_identifica_a_base | ✔ |
| `fobasesirrf_totais` | totais | fobasesirrf | — | ✔ |
| `fobasesservirrf_consultar` | consultar | fobasesservirrf | empresa | ✔ |
| `fobasesservirrf_obter` | obter | fobasesservirrf | empresa, codigo_do_empregado, competencia, tipo_da_folha, codigo_do_servico, indica_se_a_linha_e_resultado_de_um_rate, codigo_do_calculo, numero_sequencia_que_identifica_a_base | ✔ |
| `focalcgrci_consultar` | consultar | focalcgrci | empresa | ✔ |
| `focalcgrci_obter` | obter | focalcgrci | empresa, empregado, competencia, tipo_folha, tipo_da_gps_individual_1_gps_normal_2_gp | ✔ |
| `focalcgrci_totais` | totais | focalcgrci | empresa | ✔ |
| `focalcirrf_consultar` | consultar | focalcirrf | empresa | ✔ |
| `focalcirrf_obter` | obter | focalcirrf | empresa, inicio_periodo, codigo_recolhimento, tipo_de_guia_1_empregados_e_contribuinte | ✔ |
| `focalcirrf_totais` | totais | focalcirrf | empresa | ✔ |
| `focalculando_consultar` | consultar | focalculando | empresa | ✔ |
| `focalculando_obter` | obter | focalculando | empresa, codigo_sequencial | ✔ |
| `focalculos_consultar` | consultar | focalculos | — | ✔ |
| `focalculos_obter` | obter | focalculos | codigo_do_calculo | ✔ |
| `focat_consultar` | consultar | focat | empresa | ✔ |
| `focat_obter` | obter | focat | empresa, codigo_do_empregado, codigo_da_cat | ✔ |
| `focat_totais` | totais | focat | empresa | ✔ |
| `focbo_consultar` | consultar | focbo | — | ✔ |
| `focbo_obter` | obter | focbo | codigo | ✔ |
| `focbo2002_consultar` | consultar | focbo2002 | — | ✔ |
| `focbo2002_obter` | obter | focbo2002 | i_cbo2002 | ✔ |
| `foccustosct_consultar` | consultar | foccustosct | empresa | ✔ |
| `foccustosct_obter` | obter | foccustosct | empresa, codigo_do_c_c, codigo_da_empresa_da_contabilidade, codigo_do_centro_de_custo_contabilidade | ✔ |
| `foconfarquivo_consultar` | consultar | foconfarquivo | empresa | ✔ |
| `foconfarquivo_obter` | obter | foconfarquivo | empresa, codigo_arquivo, codigo | ✔ |
| `foconfarquivocols_consultar` | consultar | foconfarquivocols | — | ✔ |
| `foconfarquivocols_obter` | obter | foconfarquivocols | codigo_arquivo, codigo, tipo_registro, sequencia | ✔ |
| `focontrrpa_consultar` | consultar | focontrrpa | empresa | ✔ |
| `focontrrpa_obter` | obter | focontrrpa | empresa, empregado, numero | ✔ |
| `focontrrpa_totais` | totais | focontrrpa | empresa | ✔ |
| `focontrrpairrf_consultar` | consultar | focontrrpairrf | empresa | ✔ |
| `focontrrpairrf_obter` | obter | focontrrpairrf | empresa, codigo_do_empregado, numero_rpa, numero_sequencia_que_identifica_a_base | ✔ |
| `focontrrpaserv_consultar` | consultar | focontrrpaserv | empresa | ✔ |
| `focontrrpaserv_obter` | obter | focontrrpaserv | empresa, codigo_do_empregado, numero_rpa, codigo_do_servico | ✔ |
| `focontrrpaserv_totais` | totais | focontrrpaserv | empresa | ✔ |
| `fodadoutraemp_consultar` | consultar | fodadoutraemp | empresa | ✔ |
| `fodadoutraemp_obter` | obter | fodadoutraemp | empresa, empregado, competencia, tipo_folha, sequencial | ✔ |
| `fodadoutraemp_totais` | totais | fodadoutraemp | empresa | ✔ |
| `foemponi_consultar` | consultar | foemponi | — | ✔ |
| `foemponi_obter` | obter | foemponi | codigo | ✔ |
| `foeprfoto_consultar` | consultar | foeprfoto | empresa | ✔ |
| `foeprfoto_obter` | obter | foeprfoto | empresa, codigo_empregado | ✔ |
| `foeventosbasesdef_consultar` | consultar | foeventosbasesdef | — | ✔ |
| `foeventosbasesdef_obter` | obter | foeventosbasesdef | codigo_do_evento, codigo_da_base | ✔ |
| `foexparquivo_consultar` | consultar | foexparquivo | — | ✔ |
| `foexparquivo_obter` | obter | foexparquivo | numero_banco, codigo_arquivo, posicao, sequencia, codigo_do_banco | ✔ |
| `fofgtsfilial_consultar` | consultar | fofgtsfilial | empresa | ✔ |
| `fofgtsfilial_obter` | obter | fofgtsfilial | empresa, sequencial | ✔ |
| `fofgtsfilial_totais` | totais | fofgtsfilial | empresa | ✔ |
| `fofilhos_consultar` | consultar | fofilhos | empresa | ✔ |
| `fofilhos_obter` | obter | fofilhos | empresa, codigo_empregado, codigo_do_dependente | ✔ |
| `foformulas_consultar` | consultar | foformulas | empresa | ✔ |
| `foformulas_obter` | obter | foformulas | empresa, evento | ✔ |
| `foformulasdef_consultar` | consultar | foformulasdef | — | ✔ |
| `foformulasdef_obter` | obter | foformulasdef | evento | ✔ |
| `fofpas_consultar` | consultar | fofpas | — | ✔ |
| `fofpas_obter` | obter | fofpas | sequencial_tabela_fpas | ✔ |
| `fofuncoes_consultar` | consultar | fofuncoes | empresa | ✔ |
| `fofuncoes_obter` | obter | fofuncoes | empresa, codigo_da_funcao | ✔ |
| `foguiagrfc_consultar` | consultar | foguiagrfc | empresa | ✔ |
| `foguiagrfc_obter` | obter | foguiagrfc | empresa, codigo_do_empregado, tipo_de_calculo_de_rescisao_1_normal_2_c, codigo_do_calculo | ✔ |
| `foguiagrfc_totais` | totais | foguiagrfc | empresa | ✔ |
| `foguiainss_consultar` | consultar | foguiainss | empresa | ✔ |
| `foguiainss_obter` | obter | foguiainss | empresa, sequencial_da_guia | ✔ |
| `foguiainss_totais` | totais | foguiainss | empresa | ✔ |
| `foguiainssemissao_consultar` | consultar | foguiainssemissao | — | ✔ |
| `foguiainssemissao_obter` | obter | foguiainssemissao | sequencial_da_guia, sequencial_da_guia_que_pagou_em_caso_de | ✔ |
| `foguiainssserv_consultar` | consultar | foguiainssserv | empresa | ✔ |
| `foguiainssserv_obter` | obter | foguiainssserv | empresa, codigo_do_servico, sequencial_da_guia | ✔ |
| `foguiapis_consultar` | consultar | foguiapis | empresa | ✔ |
| `foguiapis_obter` | obter | foguiapis | empresa, sequencial_de_guias | ✔ |
| `foguiapis_totais` | totais | foguiapis | empresa | ✔ |
| `foguiapisemissao_consultar` | consultar | foguiapisemissao | — | ✔ |
| `foguiapisemissao_obter` | obter | foguiapisemissao | sequencial_de_guias, i_guiapis_emissao | ✔ |
| `foguiapisfiliais_consultar` | consultar | foguiapisfiliais | empresa | ✔ |
| `foguiapisfiliais_obter` | obter | foguiapisfiliais | empresa, sequencial_de_guias | ✔ |
| `foguiapisfiliais_totais` | totais | foguiapisfiliais | empresa | ✔ |
| `fohistemprant_consultar` | consultar | fohistemprant | empresa | ✔ |
| `fohistemprant_obter` | obter | fohistemprant | empresa, codigo_empregado, tipo_do_historico, data, inicio_gozo, sequencial_do_historico | ✔ |
| `fohistemprant_totais` | totais | fohistemprant | empresa | ✔ |
| `fohistempregados_consultar` | consultar | fohistempregados | empresa | ✔ |
| `fohistempregados_obter` | obter | fohistempregados | empresa, codigo_empregado, sequencial | ✔ |
| `fohorarios_consultar` | consultar | fohorarios | empresa | ✔ |
| `fohorarios_obter` | obter | fohorarios | empresa, codigo_do_horario | ✔ |
| `fohorasaula_consultar` | consultar | fohorasaula | empresa | ✔ |
| `fohorasaula_obter` | obter | fohorasaula | empresa, codigo_das_horas_aula | ✔ |
| `foidentificadores_consultar` | consultar | foidentificadores | — | ✔ |
| `foidentificadores_obter` | obter | foidentificadores | tipo, valor_do_identificador | ✔ |
| `foinssdata_consultar` | consultar | foinssdata | empresa | ✔ |
| `foinssdata_obter` | obter | foinssdata | empresa, empregado, competencia, is_tipo_da_folha | ✔ |
| `fointegcontitens_consultar` | consultar | fointegcontitens | — | ✔ |
| `fointegcontitens_obter` | obter | fointegcontitens | codigo_do_item, tipo_de_configuracao | ✔ |
| `fojornadas_consultar` | consultar | fojornadas | empresa | ✔ |
| `fojornadas_obter` | obter | fojornadas | empresa, codigo_do_jornada | ✔ |
| `folanctomedias_consultar` | consultar | folanctomedias | empresa | ✔ |
| `folanctomedias_obter` | obter | folanctomedias | empresa, codigo_do_empregado, competencia, codigo_do_evento, c_1_usuario_2_ferias_3_afastamentos | ✔ |
| `folanctomedias_totais` | totais | folanctomedias | empresa | ✔ |
| `folanctosauto_consultar` | consultar | folanctosauto | empresa | ✔ |
| `folanctosauto_obter` | obter | folanctosauto | empresa, sequencial | ✔ |
| `folanctosauto_totais` | totais | folanctosauto | empresa | ✔ |
| `folinhas_consultar` | consultar | folinhas | — | ✔ |
| `folinhas_obter` | obter | folinhas | linha | ✔ |
| `folinhas_totais` | totais | folinhas | — | ✔ |
| `foliquidosfil_consultar` | consultar | foliquidosfil | empresa | ✔ |
| `foliquidosfil_obter` | obter | foliquidosfil | empresa, sequencial | ✔ |
| `foliquidosfil_totais` | totais | foliquidosfil | empresa | ✔ |
| `fomediascalc_consultar` | consultar | fomediascalc | empresa | ✔ |
| `fomediascalc_obter` | obter | fomediascalc | empresa, empregado, tipo_informado, tipo_calculo, tipo_de_calculo_de_rescisao_1_normal_2_c, codigo_do_calculo | ✔ |
| `fomediascalc_totais` | totais | fomediascalc | empresa | ✔ |
| `fomedicos_consultar` | consultar | fomedicos | — | ✔ |
| `fomedicos_obter` | obter | fomedicos | codigo_do_medico_dentista | ✔ |
| `fooperadoraplanosaude_consultar` | consultar | fooperadoraplanosaude | — | ✔ |
| `fooperadoraplanosaude_obter` | obter | fooperadoraplanosaude | codigo_da_operadora_de_plano_de_saude | ✔ |
| `fopagto_consultar` | consultar | fopagto | — | ✔ |
| `fopagto_obter` | obter | fopagto | sequencia_de_pagamento | ✔ |
| `fopagto_totais` | totais | fopagto | — | ✔ |
| `fopagtogrupo_consultar` | consultar | fopagtogrupo | — | ✔ |
| `fopagtogrupo_obter` | obter | fopagtogrupo | sequencial | ✔ |
| `fopagtoparcial_consultar` | consultar | fopagtoparcial | — | ✔ |
| `fopagtoparcial_obter` | obter | fopagtoparcial | sequencia_de_pagamento, sequencial_de_pagamentos | ✔ |
| `fopagtoparcial_totais` | totais | fopagtoparcial | — | ✔ |
| `fopagtoparcialepr_consultar` | consultar | fopagtoparcialepr | empresa | ✔ |
| `fopagtoparcialepr_obter` | obter | fopagtoparcialepr | empresa, sequencia_de_pagamento, sequencial_de_pagamentos, codigo_do_empregado | ✔ |
| `fopagtoparcialepr_totais` | totais | fopagtoparcialepr | empresa | ✔ |
| `fopagtoparciallancto_consultar` | consultar | fopagtoparciallancto | empresa | ✔ |
| `fopagtoparciallancto_obter` | obter | fopagtoparciallancto | empresa, nume_lan, sequencia_de_pagamento, sequencial_de_pagamentos | ✔ |
| `foparmtofil_consultar` | consultar | foparmtofil | empresa | ✔ |
| `foparmtofil_obter` | obter | foparmtofil | empresa, codigo_filial_folha | ✔ |
| `foparsit_consultar` | consultar | foparsit | empresa | ✔ |
| `foparsit_obter` | obter | foparsit | empresa, situacao_de_afastamento | ✔ |
| `foparsit_totais` | totais | foparsit | empresa | ✔ |
| `fopppatividades_consultar` | consultar | fopppatividades | empresa | ✔ |
| `fopppatividades_obter` | obter | fopppatividades | empresa, codigo_do_empregado, inicio_da_atividade | ✔ |
| `fopppresp_consultar` | consultar | fopppresp | empresa | ✔ |
| `fopppresp_obter` | obter | fopppresp | empresa, codigo_da_filial, tipo_do_responsavel_1_ambiental_2_biolog, codigo | ✔ |
| `foprovisoes_consultar` | consultar | foprovisoes | empresa | ✔ |
| `foprovisoes_obter` | obter | foprovisoes | empresa, empregado, competencia, tipo_provisao | ✔ |
| `foprovisoes_totais` | totais | foprovisoes | empresa | ✔ |
| `forais_consultar` | consultar | forais | empresa | ✔ |
| `forais_obter` | obter | forais | empresa, filial | ✔ |
| `forais_totais` | totais | forais | empresa | ✔ |
| `foraismunic_consultar` | consultar | foraismunic | — | ✔ |
| `foraismunic_obter` | obter | foraismunic | codigo | ✔ |
| `forescisoesaviso_consultar` | consultar | forescisoesaviso | empresa | ✔ |
| `forescisoesaviso_obter` | obter | forescisoesaviso | empresa, empregado, sequencial_do_aviso_previo | ✔ |
| `forescisoesaviso_totais` | totais | forescisoesaviso | empresa | ✔ |
| `fosaldosimp_consultar` | consultar | fosaldosimp | empresa | ✔ |
| `fosaldosimp_obter` | obter | fosaldosimp | empresa, codigo | ✔ |
| `fosaldosimp_totais` | totais | fosaldosimp | empresa | ✔ |
| `fosindicatosadicfer_consultar` | consultar | fosindicatosadicfer | — | ✔ |
| `fosindicatosadicfer_obter` | obter | fosindicatosadicfer | codigo_do_sindicato, numero_de_meses | ✔ |
| `fosindicatosaviso_consultar` | consultar | fosindicatosaviso | — | ✔ |
| `fosindicatosaviso_obter` | obter | fosindicatosaviso | codigo_sindicato, meses_trabalhados, idade | ✔ |
| `fosindicatosaviso_totais` | totais | fosindicatosaviso | — | ✔ |
| `fosindicatospatronal_consultar` | consultar | fosindicatospatronal | — | ✔ |
| `fosindicatospatronal_obter` | obter | fosindicatospatronal | codigo_do_sindicato_patronal | ✔ |
| `fosindicatospisosal_consultar` | consultar | fosindicatospisosal | — | ✔ |
| `fosindicatospisosal_obter` | obter | fosindicatospisosal | codigo, a_partir_de | ✔ |
| `fosindicatospisosal_totais` | totais | fosindicatospisosal | — | ✔ |
| `fosindpiso_consultar` | consultar | fosindpiso | — | ✔ |
| `fosindpiso_obter` | obter | fosindpiso | codigo_do_sindicato, codigo_do_piso_do_sindicato | ✔ |
| `fosindpisovalor_consultar` | consultar | fosindpisovalor | — | ✔ |
| `fosindpisovalor_obter` | obter | fosindpisovalor | codigo_do_sindicato, codigo_do_piso_do_sindicato, competencia | ✔ |
| `fosindpisovalor_totais` | totais | fosindpisovalor | — | ✔ |
| `fostatus_consultar` | consultar | fostatus | — | ✔ |
| `fostatus_obter` | obter | fostatus | nome_do_status | ✔ |
| `fotabcalc_consultar` | consultar | fotabcalc | — | ✔ |
| `fotabcalc_obter` | obter | fotabcalc | mes_ano | ✔ |
| `fotabcalc_totais` | totais | fotabcalc | — | ✔ |
| `fotabcalcfap_consultar` | consultar | fotabcalcfap | empresa | ✔ |
| `fotabcalcfap_obter` | obter | fotabcalcfap | empresa, competencia | ✔ |
| `fotabcalcinss_consultar` | consultar | fotabcalcinss | — | ✔ |
| `fotabcalcinss_obter` | obter | fotabcalcinss | competencia | ✔ |
| `fotabcalcinss_totais` | totais | fotabcalcinss | — | ✔ |
| `fotabcalcirrf_consultar` | consultar | fotabcalcirrf | — | ✔ |
| `fotabcalcirrf_obter` | obter | fotabcalcirrf | competencia | ✔ |
| `fotabcalcirrf_totais` | totais | fotabcalcirrf | — | ✔ |
| `fotabcalcsalminimo_consultar` | consultar | fotabcalcsalminimo | — | ✔ |
| `fotabcalcsalminimo_obter` | obter | fotabcalcsalminimo | competencia | ✔ |
| `fotabcalcsalminimo_totais` | totais | fotabcalcsalminimo | — | ✔ |
| `fotabelas_consultar` | consultar | fotabelas | — | ✔ |
| `fotabelas_obter` | obter | fotabelas | tipo_de_tabela_1_estabilidades_2_locais, sequencial | ✔ |
| `fotreinamentos_consultar` | consultar | fotreinamentos | — | ✔ |
| `fotreinamentos_obter` | obter | fotreinamentos | codigo_do_treinamento | ✔ |
| `fovaletrp_consultar` | consultar | fovaletrp | empresa | ✔ |
| `fovaletrp_obter` | obter | fovaletrp | empresa, linha, empregado, competencia_inicio | ✔ |
| `fovaletrp_totais` | totais | fovaletrp | empresa | ✔ |
| `fovaletrplanctos_consultar` | consultar | fovaletrplanctos | empresa | ✔ |
| `fovaletrplanctos_obter` | obter | fovaletrplanctos | empresa, codigo_da_linha, codigo_do_empregado, competencia, tipo_de_processo, tipo_do_lancamento_1_mensal_2_fixo, sequencial | ✔ |
| `fovaletrplanctos_totais` | totais | fovaletrplanctos | empresa | ✔ |
| `poafastamentos_consultar` | consultar | poafastamentos | empresa | ✔ |
| `poafastamentos_obter` | obter | poafastamentos | empresa, i_empregados, data | ✔ |
| `poafastamentos_totais` | totais | poafastamentos | empresa | ✔ |
| `poafastamentosoco_consultar` | consultar | poafastamentosoco | empresa | ✔ |
| `poafastamentosoco_obter` | obter | poafastamentosoco | empresa, situacao | ✔ |
| `poeventos_consultar` | consultar | poeventos | empresa | ✔ |
| `poeventos_obter` | obter | poeventos | empresa, i_eventos | ✔ |
| `poferiados_consultar` | consultar | poferiados | empresa | ✔ |
| `poferiados_obter` | obter | poferiados | empresa, filial, data | ✔ |
| `pohorarios_consultar` | consultar | pohorarios | empresa | ✔ |
| `pohorarios_obter` | obter | pohorarios | empresa, i_horarios | ✔ |
| `pohorsper_consultar` | consultar | pohorsper | empresa | ✔ |
| `pohorsper_obter` | obter | pohorsper | empresa, i_periodos, i_sequencia | ✔ |
| `pomarcacao_consultar` | consultar | pomarcacao | empresa | ✔ |
| `pomarcacao_obter` | obter | pomarcacao | empresa, i_empregados, data_apu, data_mar, hora | ✔ |
| `pomarchor_consultar` | consultar | pomarchor | empresa | ✔ |
| `pomarchor_obter` | obter | pomarchor | empresa, i_horarios, i_sequencia | ✔ |
| `poocoger_consultar` | consultar | poocoger | empresa | ✔ |
| `poocoger_obter` | obter | poocoger | empresa, i_empregados, data, i_ocorrencias | ✔ |
| `poocoger_totais` | totais | poocoger | empresa | ✔ |
| `poocorrencias_consultar` | consultar | poocorrencias | empresa | ✔ |
| `poocorrencias_obter` | obter | poocorrencias | empresa, i_ocorrencias | ✔ |
| `poocorrencias_totais` | totais | poocorrencias | empresa | ✔ |
| `poocorrenciasdef_consultar` | consultar | poocorrenciasdef | — | ✔ |
| `poocorrenciasdef_obter` | obter | poocorrenciasdef | i_ocorrencias | ✔ |
| `poparmto_consultar` | consultar | poparmto | empresa | ✔ |
| `poparmto_obter` | obter | poparmto | empresa, i_codigo | ✔ |
| `poparmto_totais` | totais | poparmto | empresa | ✔ |
| `poperiodos_consultar` | consultar | poperiodos | empresa | ✔ |
| `poperiodos_obter` | obter | poperiodos | empresa, i_periodos | ✔ |
| `poprocedim_consultar` | consultar | poprocedim | empresa | ✔ |
| `poprocedim_obter` | obter | poprocedim | empresa, i_procedimentos | ✔ |
| `porelogios_consultar` | consultar | porelogios | — | ✔ |
| `porelogios_obter` | obter | porelogios | i_relogios | ✔ |
| `postatemp_consultar` | consultar | postatemp | empresa | ✔ |
| `postatemp_obter` | obter | postatemp | empresa, i_empregados, data | ✔ |
| `poturmas_consultar` | consultar | poturmas | empresa | ✔ |
| `poturmas_obter` | obter | poturmas | empresa, i_turmas | ✔ |
