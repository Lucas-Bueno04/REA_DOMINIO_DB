# Módulo `fiscal_outrosdados`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `efoutrosdados_dirf_scp_consultar` | consultar | efoutrosdados_dirf_scp | empresa | ✔ |
| `efoutrosdados_dirf_scp_obter` | obter | efoutrosdados_dirf_scp | empresa, competencia, informativo, sequencial | ✔ |
| `efoutrosdados_efd_contas_consultar` | consultar | efoutrosdados_efd_contas | empresa | ✔ |
| `efoutrosdados_efd_contas_obter` | obter | efoutrosdados_efd_contas | empresa, competencia, informativo, registro_1_c481_c485_2_m400_m800_3_f500, sequencial_da_conta | ✔ |
| `efoutrosdados_efd_contas_acumulador_consultar` | consultar | efoutrosdados_efd_contas_acumulador | empresa | ✔ |
| `efoutrosdados_efd_contas_acumulador_obter` | obter | efoutrosdados_efd_contas_acumulador | empresa, competencia, informativo, registro_1_c481_c485_2_m400_m800_3_f500, sequencial_da_conta, sequencial_do_acumulador | ✔ |
| `efoutrosdados_efd_contas_cfop_consultar` | consultar | efoutrosdados_efd_contas_cfop | empresa | ✔ |
| `efoutrosdados_efd_contas_cfop_obter` | obter | efoutrosdados_efd_contas_cfop | empresa, competencia, informativo, registro_1_c481_c485_2_m400_m800_3_f500, sequencial_da_conta, sequencial_do_cfop | ✔ |
| `efoutrosdados_efd_contas_cst_consultar` | consultar | efoutrosdados_efd_contas_cst | empresa | ✔ |
| `efoutrosdados_efd_contas_cst_obter` | obter | efoutrosdados_efd_contas_cst | empresa, competencia, informativo, registro_1_c481_c485_2_m400_m800_3_f500, sequencial_da_conta, sequencial_do_cst | ✔ |
| `efoutrosdados_efd_evento_scp_consultar` | consultar | efoutrosdados_efd_evento_scp | empresa | ✔ |
| `efoutrosdados_efd_evento_scp_obter` | obter | efoutrosdados_efd_evento_scp | empresa, competaancia, informativo, scp | ✔ |
| `efoutrosdados_efd_recibo_scp_consultar` | consultar | efoutrosdados_efd_recibo_scp | empresa | ✔ |
| `efoutrosdados_efd_recibo_scp_obter` | obter | efoutrosdados_efd_recibo_scp | empresa, competencia, informativo, scp | ✔ |
| `efoutrosdados_efd_reinf_servicos_prestados_consultar` | consultar | efoutrosdados_efd_reinf_servicos_prestados | empresa | ✔ |
| `efoutrosdados_efd_reinf_servicos_prestados_obter` | obter | efoutrosdados_efd_reinf_servicos_prestados | empresa, competencia, codi_emp_prestados, tipo_inscricao_prestados, inscricao_prestados, codigo_de_recolhimento, tipo_inscricao_valor_apurado, inscricao_valor_apurado, numero_do_documento, tipo_da_nota_s_saida_v_servico, indicativo_de_prestacao_de_servicos | ✔ |
| `efoutrosdados_efd_reinf_servicos_prestados_totais` | totais | efoutrosdados_efd_reinf_servicos_prestados | empresa | ✔ |
| `efoutrosdados_efd_reinf_servicos_tomados_consultar` | consultar | efoutrosdados_efd_reinf_servicos_tomados | empresa | ✔ |
| `efoutrosdados_efd_reinf_servicos_tomados_obter` | obter | efoutrosdados_efd_reinf_servicos_tomados | empresa, competencia, empresa_tomador, tipo_inscricao_tomador, inscricao_tomador, codigo_de_recolhimento, tipo_inscricao_valor_apurado, inscricao_valor_apurado, numero_do_documento, indicativo_de_prestacao_de_servicos | ✔ |
| `efoutrosdados_efd_reinf_servicos_tomados_totais` | totais | efoutrosdados_efd_reinf_servicos_tomados | empresa | ✔ |
| `efoutrosdados_planejamento_tributario_aliquota_im_a257_consultar` | consultar | efoutrosdados_planejamento_tributario_aliquota_impostos | empresa | ✔ |
| `efoutrosdados_planejamento_tributario_aliquota_impostos_obter` | obter | efoutrosdados_planejamento_tributario_aliquota_impostos | empresa, competencia, informativo | ✔ |
| `efoutrosdados_planejamento_tributario_cfops_consi_4652_consultar` | consultar | efoutrosdados_planejamento_tributario_cfops_considerados | empresa | ✔ |
| `efoutrosdados_planejamento_tributario_cfops_considerados_obter` | obter | efoutrosdados_planejamento_tributario_cfops_considerados | empresa, competencia, informativo, tipo_d_debito_c_credito, sequencial, atividade_1_comercio_2_industria_3_servi | ✔ |
| `efoutrosdados_planejamento_tributario_custos_desp_88cd_consultar` | consultar | efoutrosdados_planejamento_tributario_custos_despesas_lucro_real | empresa | ✔ |
| `efoutrosdados_planejamento_tributario_custos_despesas_88cd_obter` | obter | efoutrosdados_planejamento_tributario_custos_despesas_lucro_real | empresa, competencia, informativo | ✔ |
| `efoutrosdados_planejamento_tributario_custos_desp_b785_consultar` | consultar | efoutrosdados_planejamento_tributario_custos_despesas_lucro_real_empresas | empresa | ✔ |
| `efoutrosdados_planejamento_tributario_custos_despesas_b785_obter` | obter | efoutrosdados_planejamento_tributario_custos_despesas_lucro_real_empresas | empresa, competencia, informativo, empresa_importar_saldo_das_contas_contab | ✔ |
| `efoutrosdados_planejamento_tributario_custos_desp_2965_consultar` | consultar | efoutrosdados_planejamento_tributario_custos_despesas_lucro_real_empresas_contas | empresa | ✔ |
| `efoutrosdados_planejamento_tributario_custos_despesas_2965_obter` | obter | efoutrosdados_planejamento_tributario_custos_despesas_lucro_real_empresas_contas | empresa, competencia, informativo, empresa_importar_saldo_das_contas_contab, conta_contabil | ✔ |
| `efoutrosdados_planejamento_tributario_custos_desp_83d1_consultar` | consultar | efoutrosdados_planejamento_tributario_custos_despesas_lucro_real_saldo_conta_acumulador_empresas | empresa | ✔ |
| `efoutrosdados_planejamento_tributario_custos_despesas_83d1_obter` | obter | efoutrosdados_planejamento_tributario_custos_despesas_lucro_real_saldo_conta_acumulador_empresas | empresa, competencia, informativo, empresa_importar_saldo_das_contas_contab | ✔ |
| `efoutrosdados_planejamento_tributario_percentual__9fd0_consultar` | consultar | efoutrosdados_planejamento_tributario_percentual_rb_simples_nacional | empresa | ✔ |
| `efoutrosdados_planejamento_tributario_percentual_rb_s_9fd0_obter` | obter | efoutrosdados_planejamento_tributario_percentual_rb_simples_nacional | empresa, competencia, informativo, sequencial | ✔ |
| `efoutrosdados_planejamento_tributario_presuncao_consultar` | consultar | efoutrosdados_planejamento_tributario_presuncao | empresa | ✔ |
| `efoutrosdados_planejamento_tributario_presuncao_obter` | obter | efoutrosdados_planejamento_tributario_presuncao | empresa, competencia, informativo, sequencial | ✔ |
| `efoutrosdados_reinf_rendimentos_isentos_consultar` | consultar | efoutrosdados_reinf_rendimentos_isentos | empresa | ✔ |
| `efoutrosdados_reinf_rendimentos_isentos_obter` | obter | efoutrosdados_reinf_rendimentos_isentos | empresa, competencia, informativo, sequencial_rendimento | ✔ |
| `efoutrosdados_reinf_rendimentos_isentos_totais` | totais | efoutrosdados_reinf_rendimentos_isentos | empresa | ✔ |
| `efoutrosdados_reinf_rendimentos_isentos_contas_consultar` | consultar | efoutrosdados_reinf_rendimentos_isentos_contas | empresa | ✔ |
| `efoutrosdados_reinf_rendimentos_isentos_contas_obter` | obter | efoutrosdados_reinf_rendimentos_isentos_contas | empresa, competencia, informativo, sequencial_rendimento, conta | ✔ |
| `efoutrosdados_reinf_rendimentos_isentos_contas_param_consultar` | consultar | efoutrosdados_reinf_rendimentos_isentos_contas_param | empresa | ✔ |
| `efoutrosdados_reinf_rendimentos_isentos_contas_param_obter` | obter | efoutrosdados_reinf_rendimentos_isentos_contas_param | empresa, competencia, informativo, sequencial_rendimento | ✔ |
| `efoutrosdados_reinf_rendimentos_isentos_contas_param_totais` | totais | efoutrosdados_reinf_rendimentos_isentos_contas_param | empresa | ✔ |
