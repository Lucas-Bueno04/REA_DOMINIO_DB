# Módulo `fiscal_importacao`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `efimportacao_site_nfe_acumuladores_consultar` | consultar | efimportacao_site_nfe_acumuladores | empresa | ✔ |
| `efimportacao_site_nfe_acumuladores_obter` | obter | efimportacao_site_nfe_acumuladores | empresa, tipo_da_nota, sequencial_do_acumulador | ✔ |
| `efimportacao_site_nfe_acumuladores_cfops_consultar` | consultar | efimportacao_site_nfe_acumuladores_cfops | empresa | ✔ |
| `efimportacao_site_nfe_acumuladores_cfops_obter` | obter | efimportacao_site_nfe_acumuladores_cfops | empresa, tipo_da_nota, cfop, versao_cfop, sequencial_do_acumulador | ✔ |
| `efimportacao_site_nfe_acumuladores_ncm_consultar` | consultar | efimportacao_site_nfe_acumuladores_ncm | empresa | ✔ |
| `efimportacao_site_nfe_acumuladores_ncm_obter` | obter | efimportacao_site_nfe_acumuladores_ncm | empresa, tipo_da_nota, sequencial_do_ncm, sequencial_do_acumulador | ✔ |
| `efimportacao_site_nfe_campos_consultar` | consultar | efimportacao_site_nfe_campos | — | ✔ |
| `efimportacao_site_nfe_campos_obter` | obter | efimportacao_site_nfe_campos | campo_da_pagina | ✔ |
| `efimportacao_site_nfe_cfop_consultar` | consultar | efimportacao_site_nfe_cfop | empresa | ✔ |
| `efimportacao_site_nfe_cfop_obter` | obter | efimportacao_site_nfe_cfop | empresa, cfop, versao_cfop | ✔ |
| `efimportacao_site_nfe_cfop_cfops_consultar` | consultar | efimportacao_site_nfe_cfop_cfops | empresa | ✔ |
| `efimportacao_site_nfe_cfop_cfops_obter` | obter | efimportacao_site_nfe_cfop_cfops | empresa, cfop, versao_cfop, cfop_saida, versao_cfop_saida | ✔ |
| `efimportacao_site_nfe_configuracao_consultar` | consultar | efimportacao_site_nfe_configuracao | empresa | ✔ |
| `efimportacao_site_nfe_entrada_consultar` | consultar | efimportacao_site_nfe_entrada | empresa | ✔ |
| `efimportacao_site_nfe_entrada_cst_csosn_consultar` | consultar | efimportacao_site_nfe_entrada_cst_csosn | empresa | ✔ |
| `efimportacao_site_nfe_entrada_cst_csosn_obter` | obter | efimportacao_site_nfe_entrada_cst_csosn | empresa, sequencial_do_cst_csosn | ✔ |
| `efimportacao_site_nfe_entrada_cst_csosn_cfop_consultar` | consultar | efimportacao_site_nfe_entrada_cst_csosn_cfop | empresa | ✔ |
| `efimportacao_site_nfe_entrada_cst_csosn_cfop_obter` | obter | efimportacao_site_nfe_entrada_cst_csosn_cfop | empresa, sequencial_do_cst_csosn, sequencial_do_cfop | ✔ |
| `efimportacao_site_nfe_entrada_dados_pis_cofins_consultar` | consultar | efimportacao_site_nfe_entrada_dados_pis_cofins | empresa | ✔ |
| `efimportacao_site_nfe_entrada_dados_pis_cofins_obter` | obter | efimportacao_site_nfe_entrada_dados_pis_cofins | empresa, sequencial_dos_dados_de_pis_cofins | ✔ |
| `efimportacao_site_nfe_entrada_diferenca_bc_icms_consultar` | consultar | efimportacao_site_nfe_entrada_diferenca_bc_icms | empresa | ✔ |
| `efimportacao_site_nfe_entrada_diferenca_bc_icms_obter` | obter | efimportacao_site_nfe_entrada_diferenca_bc_icms | empresa, sequencial_da_diferenca | ✔ |
| `efimportacao_site_nfe_entrada_diferenca_bc_icms_totais` | totais | efimportacao_site_nfe_entrada_diferenca_bc_icms | empresa | ✔ |
| `efimportacao_site_nfe_entrada_diferenca_bc_ipi_consultar` | consultar | efimportacao_site_nfe_entrada_diferenca_bc_ipi | empresa | ✔ |
| `efimportacao_site_nfe_entrada_diferenca_bc_ipi_obter` | obter | efimportacao_site_nfe_entrada_diferenca_bc_ipi | empresa, sequencial_da_diferenca | ✔ |
| `efimportacao_site_nfe_entrada_impostos_gerados_consultar` | consultar | efimportacao_site_nfe_entrada_impostos_gerados | empresa | ✔ |
| `efimportacao_site_nfe_entrada_impostos_gerados_obter` | obter | efimportacao_site_nfe_entrada_impostos_gerados | empresa, sequencial_do_imposto_gerado | ✔ |
| `efimportacao_site_nfe_saida_consultar` | consultar | efimportacao_site_nfe_saida | empresa | ✔ |
| `efimportacao_site_nfe_saida_cfop_consultar` | consultar | efimportacao_site_nfe_saida_cfop | empresa | ✔ |
| `efimportacao_site_nfe_saida_cfop_obter` | obter | efimportacao_site_nfe_saida_cfop | empresa, sequencial_do_cfop_de_entrada | ✔ |
| `efimportacao_site_nfe_saida_cfop_entrada_consultar` | consultar | efimportacao_site_nfe_saida_cfop_entrada | empresa | ✔ |
| `efimportacao_site_nfe_saida_cfop_entrada_obter` | obter | efimportacao_site_nfe_saida_cfop_entrada | empresa, sequencial_do_cfop_de_saida, sequencial_do_cfop_de_entrada | ✔ |
| `efimportacao_site_nfe_saida_dados_pis_cofins_consultar` | consultar | efimportacao_site_nfe_saida_dados_pis_cofins | empresa | ✔ |
| `efimportacao_site_nfe_saida_dados_pis_cofins_obter` | obter | efimportacao_site_nfe_saida_dados_pis_cofins | empresa, sequencial_dos_dados_de_pis_cofins | ✔ |
| `efimportacao_site_nfe_saida_diferenca_bc_icms_consultar` | consultar | efimportacao_site_nfe_saida_diferenca_bc_icms | empresa | ✔ |
| `efimportacao_site_nfe_saida_diferenca_bc_icms_obter` | obter | efimportacao_site_nfe_saida_diferenca_bc_icms | empresa, sequencial_da_diferenca | ✔ |
| `efimportacao_site_nfe_saida_diferenca_bc_icms_totais` | totais | efimportacao_site_nfe_saida_diferenca_bc_icms | empresa | ✔ |
| `efimportacao_site_nfe_saida_diferenca_bc_ipi_consultar` | consultar | efimportacao_site_nfe_saida_diferenca_bc_ipi | empresa | ✔ |
| `efimportacao_site_nfe_saida_diferenca_bc_ipi_obter` | obter | efimportacao_site_nfe_saida_diferenca_bc_ipi | empresa, sequencial_da_diferenca | ✔ |
