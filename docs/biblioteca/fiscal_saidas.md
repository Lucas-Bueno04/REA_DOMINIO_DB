# Módulo `fiscal_saidas`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `efsaidas_detalhamento_mg_consultar` | consultar | efsaidas_detalhamento_mg | empresa | ✔ |
| `efsaidas_detalhamento_mg_obter` | obter | efsaidas_detalhamento_mg | empresa, nota | ✔ |
| `efsaidas_detalhamento_mg_totais` | totais | efsaidas_detalhamento_mg | empresa | ✔ |
| `efsaidas_difal_nc_consultar` | consultar | efsaidas_difal_nc | empresa | ✔ |
| `efsaidas_difal_nc_obter` | obter | efsaidas_difal_nc | empresa, codigo | ✔ |
| `efsaidas_difal_nc_totais` | totais | efsaidas_difal_nc | empresa | ✔ |
| `efsaidas_documentos_fiscais_referenciados_consultar` | consultar | efsaidas_documentos_fiscais_referenciados | empresa | ✔ |
| `efsaidas_documentos_fiscais_referenciados_obter` | obter | efsaidas_documentos_fiscais_referenciados | empresa, codigo, sequencial | ✔ |
| `efsaidas_documentos_fiscais_referenciados_totais` | totais | efsaidas_documentos_fiscais_referenciados | empresa | ✔ |
| `efsaidas_efd_reinf_consultar` | consultar | efsaidas_efd_reinf | empresa | ✔ |
| `efsaidas_efd_reinf_obter` | obter | efsaidas_efd_reinf | empresa, codigo | ✔ |
| `efsaidas_estadual_ac_consultar` | consultar | efsaidas_estadual_ac | empresa | ✔ |
| `efsaidas_estadual_ac_obter` | obter | efsaidas_estadual_ac | empresa, codigo | ✔ |
| `efsaidas_estadual_ac_totais` | totais | efsaidas_estadual_ac | empresa | ✔ |
| `efsaidas_estadual_ba_consultar` | consultar | efsaidas_estadual_ba | empresa | ✔ |
| `efsaidas_estadual_ba_obter` | obter | efsaidas_estadual_ba | empresa, codigo_da_saida | ✔ |
| `efsaidas_estadual_ba_totais` | totais | efsaidas_estadual_ba | empresa | ✔ |
| `efsaidas_estadual_mg_consultar` | consultar | efsaidas_estadual_mg | empresa | ✔ |
| `efsaidas_estadual_mg_obter` | obter | efsaidas_estadual_mg | empresa, codigo_da_saida | ✔ |
| `efsaidas_estadual_mg_totais` | totais | efsaidas_estadual_mg | empresa | ✔ |
| `efsaidas_estadual_pe_consultar` | consultar | efsaidas_estadual_pe | empresa | ✔ |
| `efsaidas_estadual_pe_obter` | obter | efsaidas_estadual_pe | empresa, codigo_da_nota | ✔ |
| `efsaidas_estadual_rj_consultar` | consultar | efsaidas_estadual_rj | empresa | ✔ |
| `efsaidas_estadual_rj_obter` | obter | efsaidas_estadual_rj | empresa, codigo_da_saida | ✔ |
| `efsaidas_estadual_rj_totais` | totais | efsaidas_estadual_rj | empresa | ✔ |
| `efsaidas_estadual_ro_consultar` | consultar | efsaidas_estadual_ro | empresa | ✔ |
| `efsaidas_estadual_ro_obter` | obter | efsaidas_estadual_ro | empresa, codigo | ✔ |
| `efsaidas_estadual_ro_totais` | totais | efsaidas_estadual_ro | empresa | ✔ |
| `efsaidas_estadual_sc_consultar` | consultar | efsaidas_estadual_sc | empresa | ✔ |
| `efsaidas_estadual_sc_obter` | obter | efsaidas_estadual_sc | empresa, codigo_da_saida | ✔ |
| `efsaidas_estadual_sc_totais` | totais | efsaidas_estadual_sc | empresa | ✔ |
| `efsaidas_estadual_sp_consultar` | consultar | efsaidas_estadual_sp | empresa | ✔ |
| `efsaidas_estadual_sp_obter` | obter | efsaidas_estadual_sp | empresa, codigo | ✔ |
| `efsaidas_estadual_sp_totais` | totais | efsaidas_estadual_sp | empresa | ✔ |
| `efsaidas_exportacao_consultar` | consultar | efsaidas_exportacao | empresa | ✔ |
| `efsaidas_exportacao_obter` | obter | efsaidas_exportacao | empresa, saida | ✔ |
| `efsaidas_exportacao_totais` | totais | efsaidas_exportacao | empresa | ✔ |
| `efsaidas_frete_consultar` | consultar | efsaidas_frete | empresa | ✔ |
| `efsaidas_frete_obter` | obter | efsaidas_frete | empresa, codigo | ✔ |
| `efsaidas_frete_totais` | totais | efsaidas_frete | empresa | ✔ |
| `efsaidas_icms_desonerado_consultar` | consultar | efsaidas_icms_desonerado | empresa | ✔ |
| `efsaidas_icms_desonerado_obter` | obter | efsaidas_icms_desonerado | empresa, codigo_da_nota, sequencial | ✔ |
| `efsaidas_icms_desonerado_totais` | totais | efsaidas_icms_desonerado | empresa | ✔ |
| `efsaidas_info_comp_contrib_consultar` | consultar | efsaidas_info_comp_contrib | empresa | ✔ |
| `efsaidas_info_comp_contrib_obter` | obter | efsaidas_info_comp_contrib | empresa, codigo, sequencial | ✔ |
| `efsaidas_info_comp_fisco_consultar` | consultar | efsaidas_info_comp_fisco | empresa | ✔ |
| `efsaidas_info_comp_fisco_obter` | obter | efsaidas_info_comp_fisco | empresa, codigo, sequencial | ✔ |
| `efsaidas_info_pag_consultar` | consultar | efsaidas_info_pag | empresa | ✔ |
| `efsaidas_info_pag_obter` | obter | efsaidas_info_pag | empresa, codigo, sequencial | ✔ |
| `efsaidas_info_pag_totais` | totais | efsaidas_info_pag | empresa | ✔ |
| `efsaidas_inss_rb_consultar` | consultar | efsaidas_inss_rb | empresa | ✔ |
| `efsaidas_inss_rb_obter` | obter | efsaidas_inss_rb | empresa, codigo | ✔ |
| `efsaidas_inss_rb_totais` | totais | efsaidas_inss_rb | empresa | ✔ |
| `efsaidas_nota_devolvida_consultar` | consultar | efsaidas_nota_devolvida | empresa | ✔ |
| `efsaidas_nota_devolvida_obter` | obter | efsaidas_nota_devolvida | empresa, codigo_da_saida, sequencial | ✔ |
| `efsaidas_nota_devolvida_totais` | totais | efsaidas_nota_devolvida | empresa | ✔ |
| `efsaidas_observacao_contrib_consultar` | consultar | efsaidas_observacao_contrib | empresa | ✔ |
| `efsaidas_observacao_contrib_obter` | obter | efsaidas_observacao_contrib | empresa, codigo, sequencial | ✔ |
| `efsaidas_observacao_fisco_consultar` | consultar | efsaidas_observacao_fisco | empresa | ✔ |
| `efsaidas_observacao_fisco_obter` | obter | efsaidas_observacao_fisco | empresa, codigo, sequencial | ✔ |
| `efsaidas_pis_cofins_consultar` | consultar | efsaidas_pis_cofins | empresa | ✔ |
| `efsaidas_pis_cofins_obter` | obter | efsaidas_pis_cofins | empresa, codigo_da_saida, sequencial | ✔ |
| `efsaidas_pis_cofins_totais` | totais | efsaidas_pis_cofins | empresa | ✔ |
| `efsaidas_valor_presente_provisao_consultar` | consultar | efsaidas_valor_presente_provisao | empresa | ✔ |
| `efsaidas_valor_presente_provisao_obter` | obter | efsaidas_valor_presente_provisao | empresa, codigo_da_nota_de_saida, data_da_provisao | ✔ |
| `efsaidas_valor_presente_provisao_totais` | totais | efsaidas_valor_presente_provisao | empresa | ✔ |
