# Módulo `fiscal_entradas`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `efentradas_detalhamento_mg_consultar` | consultar | efentradas_detalhamento_mg | empresa | ✔ |
| `efentradas_detalhamento_mg_obter` | obter | efentradas_detalhamento_mg | empresa, nota | ✔ |
| `efentradas_detalhamento_mg_totais` | totais | efentradas_detalhamento_mg | empresa | ✔ |
| `efentradas_difal_nc_consultar` | consultar | efentradas_difal_nc | empresa | ✔ |
| `efentradas_difal_nc_obter` | obter | efentradas_difal_nc | empresa, codigo | ✔ |
| `efentradas_difal_nc_totais` | totais | efentradas_difal_nc | empresa | ✔ |
| `efentradas_efd_reinf_consultar` | consultar | efentradas_efd_reinf | empresa | ✔ |
| `efentradas_efd_reinf_obter` | obter | efentradas_efd_reinf | empresa, codigo | ✔ |
| `efentradas_estadual_ac_consultar` | consultar | efentradas_estadual_ac | empresa | ✔ |
| `efentradas_estadual_ac_obter` | obter | efentradas_estadual_ac | empresa, codigo | ✔ |
| `efentradas_estadual_ac_totais` | totais | efentradas_estadual_ac | empresa | ✔ |
| `efentradas_estadual_ba_consultar` | consultar | efentradas_estadual_ba | empresa | ✔ |
| `efentradas_estadual_ba_obter` | obter | efentradas_estadual_ba | empresa, codigo_da_entrada | ✔ |
| `efentradas_estadual_ba_totais` | totais | efentradas_estadual_ba | empresa | ✔ |
| `efentradas_estadual_mg_consultar` | consultar | efentradas_estadual_mg | empresa | ✔ |
| `efentradas_estadual_mg_obter` | obter | efentradas_estadual_mg | empresa, codigo | ✔ |
| `efentradas_estadual_mg_totais` | totais | efentradas_estadual_mg | empresa | ✔ |
| `efentradas_estadual_pe_consultar` | consultar | efentradas_estadual_pe | empresa | ✔ |
| `efentradas_estadual_pe_obter` | obter | efentradas_estadual_pe | empresa, codigo_da_nota | ✔ |
| `efentradas_estadual_rj_consultar` | consultar | efentradas_estadual_rj | empresa | ✔ |
| `efentradas_estadual_rj_obter` | obter | efentradas_estadual_rj | empresa, codigo_da_entrada | ✔ |
| `efentradas_estadual_rj_totais` | totais | efentradas_estadual_rj | empresa | ✔ |
| `efentradas_estadual_ro_consultar` | consultar | efentradas_estadual_ro | empresa | ✔ |
| `efentradas_estadual_ro_obter` | obter | efentradas_estadual_ro | empresa, codigo_da_nota_de_entrada | ✔ |
| `efentradas_estadual_ro_totais` | totais | efentradas_estadual_ro | empresa | ✔ |
| `efentradas_estadual_rs_consultar` | consultar | efentradas_estadual_rs | empresa | ✔ |
| `efentradas_estadual_rs_obter` | obter | efentradas_estadual_rs | empresa, codigo | ✔ |
| `efentradas_estadual_rs_totais` | totais | efentradas_estadual_rs | empresa | ✔ |
| `efentradas_estadual_sc_consultar` | consultar | efentradas_estadual_sc | empresa | ✔ |
| `efentradas_estadual_sc_obter` | obter | efentradas_estadual_sc | empresa, codigo_da_nota | ✔ |
| `efentradas_estadual_sc_totais` | totais | efentradas_estadual_sc | empresa | ✔ |
| `efentradas_estadual_sp_consultar` | consultar | efentradas_estadual_sp | empresa | ✔ |
| `efentradas_estadual_sp_obter` | obter | efentradas_estadual_sp | empresa, codigo | ✔ |
| `efentradas_estadual_sp_totais` | totais | efentradas_estadual_sp | empresa | ✔ |
| `efentradas_info_comp_contrib_consultar` | consultar | efentradas_info_comp_contrib | empresa | ✔ |
| `efentradas_info_comp_contrib_obter` | obter | efentradas_info_comp_contrib | empresa, codigo, sequencial | ✔ |
| `efentradas_info_comp_fisco_consultar` | consultar | efentradas_info_comp_fisco | empresa | ✔ |
| `efentradas_info_comp_fisco_obter` | obter | efentradas_info_comp_fisco | empresa, codigo, sequencial | ✔ |
| `efentradas_info_pag_consultar` | consultar | efentradas_info_pag | empresa | ✔ |
| `efentradas_info_pag_obter` | obter | efentradas_info_pag | empresa, codigo, sequencial | ✔ |
| `efentradas_info_pag_totais` | totais | efentradas_info_pag | empresa | ✔ |
| `efentradas_inss_rb_consultar` | consultar | efentradas_inss_rb | empresa | ✔ |
| `efentradas_inss_rb_obter` | obter | efentradas_inss_rb | empresa, codigo | ✔ |
| `efentradas_inss_rb_totais` | totais | efentradas_inss_rb | empresa | ✔ |
| `efentradas_irrf_apf_consultar` | consultar | efentradas_irrf_apf | empresa | ✔ |
| `efentradas_irrf_apf_obter` | obter | efentradas_irrf_apf | empresa, codigo_nota, imposto | ✔ |
| `efentradas_irrf_apf_totais` | totais | efentradas_irrf_apf | empresa | ✔ |
| `efentradas_mva_consultar` | consultar | efentradas_mva | empresa | ✔ |
| `efentradas_mva_obter` | obter | efentradas_mva | empresa, nota, imposto, sequencial | ✔ |
| `efentradas_mva_totais` | totais | efentradas_mva | empresa | ✔ |
| `efentradas_nota_devolvida_consultar` | consultar | efentradas_nota_devolvida | empresa | ✔ |
| `efentradas_nota_devolvida_obter` | obter | efentradas_nota_devolvida | empresa, codigo_da_entrada, sequencial | ✔ |
| `efentradas_nota_devolvida_totais` | totais | efentradas_nota_devolvida | empresa | ✔ |
| `efentradas_nota_devolvida_csoc_irpj_consultar` | consultar | efentradas_nota_devolvida_csoc_irpj | empresa | ✔ |
| `efentradas_nota_devolvida_csoc_irpj_obter` | obter | efentradas_nota_devolvida_csoc_irpj | empresa, codigo_da_nota_de_entrada, sequencial_da_nota_devolvida, sequencial_do_csoc_irpj | ✔ |
| `efentradas_nota_devolvida_csoc_irpj_totais` | totais | efentradas_nota_devolvida_csoc_irpj | empresa | ✔ |
| `efentradas_nota_devolvida_pis_cofins_consultar` | consultar | efentradas_nota_devolvida_pis_cofins | empresa | ✔ |
| `efentradas_nota_devolvida_pis_cofins_obter` | obter | efentradas_nota_devolvida_pis_cofins | empresa, codigo_da_entrada, sequencial_da_nota_devolvida, sequencial | ✔ |
| `efentradas_nota_devolvida_pis_cofins_totais` | totais | efentradas_nota_devolvida_pis_cofins | empresa | ✔ |
| `efentradas_observacao_contrib_consultar` | consultar | efentradas_observacao_contrib | empresa | ✔ |
| `efentradas_observacao_contrib_obter` | obter | efentradas_observacao_contrib | empresa, codigo, sequencial | ✔ |
| `efentradas_observacao_fisco_consultar` | consultar | efentradas_observacao_fisco | empresa | ✔ |
| `efentradas_observacao_fisco_obter` | obter | efentradas_observacao_fisco | empresa, codigo, sequencial | ✔ |
| `efentradas_pis_cofins_consultar` | consultar | efentradas_pis_cofins | empresa | ✔ |
| `efentradas_pis_cofins_obter` | obter | efentradas_pis_cofins | empresa, codigo_da_entrada, sequencial | ✔ |
| `efentradas_pis_cofins_totais` | totais | efentradas_pis_cofins | empresa | ✔ |
| `efentradas_pis_cofins_base_piscofins_consultar` | consultar | efentradas_pis_cofins_base_piscofins | empresa | ✔ |
| `efentradas_pis_cofins_base_piscofins_obter` | obter | efentradas_pis_cofins_base_piscofins | empresa, codigo_da_entrada, sequencial, imposto, tipo_de_credito | ✔ |
| `efentradas_pis_cofins_base_piscofins_totais` | totais | efentradas_pis_cofins_base_piscofins | empresa | ✔ |
| `efentradas_valor_presente_provisao_consultar` | consultar | efentradas_valor_presente_provisao | empresa | ✔ |
| `efentradas_valor_presente_provisao_obter` | obter | efentradas_valor_presente_provisao | empresa, codigo_da_nota_de_entrada, data_da_provisao | ✔ |
| `efentradas_valor_presente_provisao_totais` | totais | efentradas_valor_presente_provisao | empresa | ✔ |
