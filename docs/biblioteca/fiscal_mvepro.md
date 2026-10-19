# Módulo `fiscal_mvepro`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `efmvepro_apuracao_estoque_consultar` | consultar | efmvepro_apuracao_estoque | empresa | ✔ |
| `efmvepro_apuracao_estoque_obter` | obter | efmvepro_apuracao_estoque | empresa, codigo_sequencial_da_nota_de_entrada, codigo_sequencial_do_estoque | ✔ |
| `efmvepro_apuracao_estoque_totais` | totais | efmvepro_apuracao_estoque | empresa | ✔ |
| `efmvepro_base_piscofins_consultar` | consultar | efmvepro_base_piscofins | empresa | ✔ |
| `efmvepro_base_piscofins_obter` | obter | efmvepro_base_piscofins | empresa, sequencial, imposto, tipo_de_credito, entrada | ✔ |
| `efmvepro_base_piscofins_totais` | totais | efmvepro_base_piscofins | empresa | ✔ |
| `efmvepro_cbs_iva_consultar` | consultar | efmvepro_cbs_iva | empresa | ✔ |
| `efmvepro_cbs_iva_obter` | obter | efmvepro_cbs_iva | empresa, codigo_entrada, codigo_sequencial_do_estoque | ✔ |
| `efmvepro_cbs_iva_totais` | totais | efmvepro_cbs_iva | empresa | ✔ |
| `efmvepro_difal_nc_consultar` | consultar | efmvepro_difal_nc | empresa | ✔ |
| `efmvepro_difal_nc_obter` | obter | efmvepro_difal_nc | empresa, codigo_sequencial_da_nota_de_entrada, codigo_sequencial_do_estoque | ✔ |
| `efmvepro_difal_nc_totais` | totais | efmvepro_difal_nc | empresa | ✔ |
| `efmvepro_difali_consultar` | consultar | efmvepro_difali | empresa | ✔ |
| `efmvepro_difali_obter` | obter | efmvepro_difali | empresa, codigo_sequencial_da_nota_de_entrada, codigo_sequencial_do_estoque | ✔ |
| `efmvepro_difali_totais` | totais | efmvepro_difali | empresa | ✔ |
| `efmvepro_estadual_am_consultar` | consultar | efmvepro_estadual_am | empresa | ✔ |
| `efmvepro_estadual_am_obter` | obter | efmvepro_estadual_am | empresa, codigo_sequencial_da_nota_de_entrada, codigo_sequencial_do_estoque | ✔ |
| `efmvepro_estadual_am_totais` | totais | efmvepro_estadual_am | empresa | ✔ |
| `efmvepro_estadual_es_consultar` | consultar | efmvepro_estadual_es | empresa | ✔ |
| `efmvepro_estadual_es_obter` | obter | efmvepro_estadual_es | empresa, codigo_sequencial_da_nota_de_entrada, codigo_sequencial_do_estoque | ✔ |
| `efmvepro_estadual_es_totais` | totais | efmvepro_estadual_es | empresa | ✔ |
| `efmvepro_estadual_mg_consultar` | consultar | efmvepro_estadual_mg | empresa | ✔ |
| `efmvepro_estadual_mg_obter` | obter | efmvepro_estadual_mg | empresa, codigo_sequencial_da_nota_de_entrada, codigo_sequencial_do_estoque | ✔ |
| `efmvepro_estadual_mg_totais` | totais | efmvepro_estadual_mg | empresa | ✔ |
| `efmvepro_estadual_mt_consultar` | consultar | efmvepro_estadual_mt | empresa | ✔ |
| `efmvepro_estadual_mt_obter` | obter | efmvepro_estadual_mt | empresa, codigo_sequencial_da_nota_de_entrada, codigo_sequencial_do_estoque | ✔ |
| `efmvepro_estadual_mt_totais` | totais | efmvepro_estadual_mt | empresa | ✔ |
| `efmvepro_estadual_rj_consultar` | consultar | efmvepro_estadual_rj | empresa | ✔ |
| `efmvepro_estadual_rj_obter` | obter | efmvepro_estadual_rj | empresa, codigo_sequencial_da_nota_de_entrada, codigo_sequencial_do_estoque | ✔ |
| `efmvepro_estadual_rj_totais` | totais | efmvepro_estadual_rj | empresa | ✔ |
| `efmvepro_estadual_ro_consultar` | consultar | efmvepro_estadual_ro | empresa | ✔ |
| `efmvepro_estadual_ro_obter` | obter | efmvepro_estadual_ro | empresa, codigo_sequencial_da_nota_de_saida, codigo_sequencial_do_estoque | ✔ |
| `efmvepro_estadual_ro_totais` | totais | efmvepro_estadual_ro | empresa | ✔ |
| `efmvepro_estadual_sp_consultar` | consultar | efmvepro_estadual_sp | empresa | ✔ |
| `efmvepro_estadual_sp_obter` | obter | efmvepro_estadual_sp | empresa, codigo_sequencial_da_nota_de_entrada, codigo_sequencial_do_estoque | ✔ |
| `efmvepro_estadual_sp_totais` | totais | efmvepro_estadual_sp | empresa | ✔ |
| `efmvepro_extemporaneo_piscofins_consultar` | consultar | efmvepro_extemporaneo_piscofins | empresa | ✔ |
| `efmvepro_extemporaneo_piscofins_obter` | obter | efmvepro_extemporaneo_piscofins | empresa, entrada, sequencial, imposto, tipo_de_credito | ✔ |
| `efmvepro_extemporaneo_piscofins_totais` | totais | efmvepro_extemporaneo_piscofins | empresa | ✔ |
| `efmvepro_federal_consultar` | consultar | efmvepro_federal | empresa | ✔ |
| `efmvepro_federal_obter` | obter | efmvepro_federal | empresa, codigo_sequencial_da_nota_de_entrada, codigo_sequencial_do_estoque | ✔ |
| `efmvepro_federal_totais` | totais | efmvepro_federal | empresa | ✔ |
| `efmvepro_fem_st_mg_consultar` | consultar | efmvepro_fem_st_mg | empresa | ✔ |
| `efmvepro_fem_st_mg_obter` | obter | efmvepro_fem_st_mg | empresa, entrada, sequencial | ✔ |
| `efmvepro_fem_st_mg_totais` | totais | efmvepro_fem_st_mg | empresa | ✔ |
| `efmvepro_ibs_iva_consultar` | consultar | efmvepro_ibs_iva | empresa | ✔ |
| `efmvepro_ibs_iva_obter` | obter | efmvepro_ibs_iva | empresa, codigo_entrada, codigo_sequencial_do_estoque | ✔ |
| `efmvepro_ibs_iva_totais` | totais | efmvepro_ibs_iva | empresa | ✔ |
| `efmvepro_icms_st_retido_consultar` | consultar | efmvepro_icms_st_retido | empresa | ✔ |
| `efmvepro_icms_st_retido_obter` | obter | efmvepro_icms_st_retido | empresa, codigo_sequencial_da_nota_de_entrada, codigo_sequencial_do_estoque, codigo_do_produto | ✔ |
| `efmvepro_icms_st_retido_totais` | totais | efmvepro_icms_st_retido | empresa | ✔ |
| `efmvepro_icms_stat_consultar` | consultar | efmvepro_icms_stat | empresa | ✔ |
| `efmvepro_icms_stat_obter` | obter | efmvepro_icms_stat | empresa, codigo_sequencial_da_nota_de_entrada, codigo_sequencial_do_estoque | ✔ |
| `efmvepro_icms_stat_totais` | totais | efmvepro_icms_stat | empresa | ✔ |
| `efmvepro_icmsa_consultar` | consultar | efmvepro_icmsa | empresa | ✔ |
| `efmvepro_icmsa_obter` | obter | efmvepro_icmsa | empresa, codigo_sequencial_da_nota_de_entrada, codigo_sequencial_do_estoque | ✔ |
| `efmvepro_icmsa_totais` | totais | efmvepro_icmsa | empresa | ✔ |
| `efmvepro_icmsi_consultar` | consultar | efmvepro_icmsi | empresa | ✔ |
| `efmvepro_icmsi_obter` | obter | efmvepro_icmsi | empresa, codigo_sequencial_da_nota_de_entrada, codigo_sequencial_do_estoque | ✔ |
| `efmvepro_icmsi_totais` | totais | efmvepro_icmsi | empresa | ✔ |
| `efmvepro_medicamento_lote_consultar` | consultar | efmvepro_medicamento_lote | empresa | ✔ |
| `efmvepro_medicamento_lote_obter` | obter | efmvepro_medicamento_lote | empresa, codigo_sequencial_da_nota_de_entrada, codigo_sequencial_do_estoque, codigo_sequencial_do_lote | ✔ |
| `efmvepro_medicamento_lote_totais` | totais | efmvepro_medicamento_lote | empresa | ✔ |
| `efmvepro_mg_sub_apuracao_consultar` | consultar | efmvepro_mg_sub_apuracao | empresa | ✔ |
| `efmvepro_mg_sub_apuracao_obter` | obter | efmvepro_mg_sub_apuracao | empresa, codigo_sequencial_da_nota_de_entrada, codigo_sequencial_do_estoque, sequencial | ✔ |
| `efmvepro_mg_sub_apuracao_totais` | totais | efmvepro_mg_sub_apuracao | empresa | ✔ |
