# Módulo `fiscal_importador`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `efimportador_fixo_cat52_consultar` | consultar | efimportador_fixo_cat52 | empresa | ✔ |
| `efimportador_fixo_cat52_situacao_tributaria_consultar` | consultar | efimportador_fixo_cat52_situacao_tributaria | empresa | ✔ |
| `efimportador_fixo_cat52_situacao_tributaria_obter` | obter | efimportador_fixo_cat52_situacao_tributaria | empresa, sequencial_da_situacao_tributaria | ✔ |
| `efimportador_fixo_cat52_situacao_tributaria_totais` | totais | efimportador_fixo_cat52_situacao_tributaria | empresa | ✔ |
| `efimportador_fixo_cfe_consultar` | consultar | efimportador_fixo_cfe | empresa | ✔ |
| `efimportador_fixo_cfe_saida_consultar` | consultar | efimportador_fixo_cfe_saida | empresa | ✔ |
| `efimportador_fixo_cfe_saida_acumulador_consultar` | consultar | efimportador_fixo_cfe_saida_acumulador | empresa | ✔ |
| `efimportador_fixo_cfe_saida_acumulador_obter` | obter | efimportador_fixo_cfe_saida_acumulador | empresa, sequencial_do_acumulador | ✔ |
| `efimportador_fixo_cfe_saida_acumulador_cfop_consultar` | consultar | efimportador_fixo_cfe_saida_acumulador_cfop | empresa | ✔ |
| `efimportador_fixo_cfe_saida_acumulador_cfop_obter` | obter | efimportador_fixo_cfe_saida_acumulador_cfop | empresa, sequencial_do_acumulador, sequencial_do_cfop | ✔ |
| `efimportador_fixo_cfe_saida_acumulador_cst_consultar` | consultar | efimportador_fixo_cfe_saida_acumulador_cst | empresa | ✔ |
| `efimportador_fixo_cfe_saida_acumulador_cst_obter` | obter | efimportador_fixo_cfe_saida_acumulador_cst | empresa, sequencial_do_acumulador, sequencial_do_cst | ✔ |
| `efimportador_fixo_cfe_saida_acumulador_produto_consultar` | consultar | efimportador_fixo_cfe_saida_acumulador_produto | empresa | ✔ |
| `efimportador_fixo_cfe_saida_acumulador_produto_obter` | obter | efimportador_fixo_cfe_saida_acumulador_produto | empresa, sequencial_do_acumulador, sequencial_do_produto | ✔ |
| `efimportador_fixo_cfe_saida_diferenca_bc_icms_consultar` | consultar | efimportador_fixo_cfe_saida_diferenca_bc_icms | empresa | ✔ |
| `efimportador_fixo_cfe_saida_diferenca_bc_icms_obter` | obter | efimportador_fixo_cfe_saida_diferenca_bc_icms | empresa, sequencial_da_diferenca | ✔ |
| `efimportador_fixo_convenio_icms115_consultar` | consultar | efimportador_fixo_convenio_icms115 | empresa | ✔ |
| `efimportador_fixo_convenio_icms115_acumulador_consultar` | consultar | efimportador_fixo_convenio_icms115_acumulador | empresa | ✔ |
| `efimportador_fixo_convenio_icms115_acumulador_obter` | obter | efimportador_fixo_convenio_icms115_acumulador | empresa, sequencial_do_acumulador | ✔ |
| `efimportador_fixo_convenio_icms115_acumulador_cfop_consultar` | consultar | efimportador_fixo_convenio_icms115_acumulador_cfop | empresa | ✔ |
| `efimportador_fixo_convenio_icms115_acumulador_cfop_obter` | obter | efimportador_fixo_convenio_icms115_acumulador_cfop | empresa, sequencial_do_acumulador, sequencial_do_cfop | ✔ |
| `efimportador_fixo_convenio_icms115_especie_consultar` | consultar | efimportador_fixo_convenio_icms115_especie | empresa | ✔ |
| `efimportador_fixo_convenio_icms115_especie_obter` | obter | efimportador_fixo_convenio_icms115_especie | empresa, sequencial_do_relacionamento_de_modelos | ✔ |
| `efimportador_fixo_cte_consultar` | consultar | efimportador_fixo_cte | empresa | ✔ |
| `efimportador_fixo_cte_entrada_consultar` | consultar | efimportador_fixo_cte_entrada | empresa | ✔ |
| `efimportador_fixo_cte_entrada_acumulador_consultar` | consultar | efimportador_fixo_cte_entrada_acumulador | empresa | ✔ |
| `efimportador_fixo_cte_entrada_acumulador_obter` | obter | efimportador_fixo_cte_entrada_acumulador | empresa, sequencial_do_acumulador | ✔ |
| `efimportador_fixo_cte_entrada_acumulador_cfop_consultar` | consultar | efimportador_fixo_cte_entrada_acumulador_cfop | empresa | ✔ |
| `efimportador_fixo_cte_entrada_acumulador_cfop_obter` | obter | efimportador_fixo_cte_entrada_acumulador_cfop | empresa, sequencial_do_acumulador, sequencial_do_cfop | ✔ |
| `efimportador_fixo_cte_entrada_cfop_consultar` | consultar | efimportador_fixo_cte_entrada_cfop | empresa | ✔ |
| `efimportador_fixo_cte_entrada_cfop_obter` | obter | efimportador_fixo_cte_entrada_cfop | empresa, sequencial_do_cfop_de_entrada | ✔ |
| `efimportador_fixo_cte_entrada_cfop_saida_consultar` | consultar | efimportador_fixo_cte_entrada_cfop_saida | empresa | ✔ |
| `efimportador_fixo_cte_entrada_cfop_saida_obter` | obter | efimportador_fixo_cte_entrada_cfop_saida | empresa, sequencial_do_cfop_de_entrada, sequencial_do_cfop_de_saida | ✔ |
| `efimportador_fixo_cte_entrada_diferenca_bc_icms_consultar` | consultar | efimportador_fixo_cte_entrada_diferenca_bc_icms | empresa | ✔ |
| `efimportador_fixo_cte_entrada_diferenca_bc_icms_obter` | obter | efimportador_fixo_cte_entrada_diferenca_bc_icms | empresa, sequencial_da_diferenca | ✔ |
| `efimportador_fixo_cte_entrada_diferenca_bc_icms_totais` | totais | efimportador_fixo_cte_entrada_diferenca_bc_icms | empresa | ✔ |
| `efimportador_fixo_cte_saida_consultar` | consultar | efimportador_fixo_cte_saida | empresa | ✔ |
| `efimportador_fixo_cte_saida_acumulador_consultar` | consultar | efimportador_fixo_cte_saida_acumulador | empresa | ✔ |
| `efimportador_fixo_cte_saida_acumulador_obter` | obter | efimportador_fixo_cte_saida_acumulador | empresa, sequencial_do_acumulador | ✔ |
| `efimportador_fixo_cte_saida_acumulador_cfop_consultar` | consultar | efimportador_fixo_cte_saida_acumulador_cfop | empresa | ✔ |
| `efimportador_fixo_cte_saida_acumulador_cfop_obter` | obter | efimportador_fixo_cte_saida_acumulador_cfop | empresa, sequencial_do_acumulador, sequencial_do_cfop | ✔ |
| `efimportador_fixo_cte_saida_diferenca_bc_icms_consultar` | consultar | efimportador_fixo_cte_saida_diferenca_bc_icms | empresa | ✔ |
| `efimportador_fixo_cte_saida_diferenca_bc_icms_obter` | obter | efimportador_fixo_cte_saida_diferenca_bc_icms | empresa, sequencial_da_diferenca | ✔ |
| `efimportador_fixo_cte_saida_diferenca_bc_icms_totais` | totais | efimportador_fixo_cte_saida_diferenca_bc_icms | empresa | ✔ |
| `efimportador_fixo_nf3e_consultar` | consultar | efimportador_fixo_nf3e | empresa | ✔ |
| `efimportador_fixo_nf3e_entrada_consultar` | consultar | efimportador_fixo_nf3e_entrada | empresa | ✔ |
| `efimportador_fixo_nf3e_entrada_acumulador_consultar` | consultar | efimportador_fixo_nf3e_entrada_acumulador | empresa | ✔ |
| `efimportador_fixo_nf3e_entrada_acumulador_obter` | obter | efimportador_fixo_nf3e_entrada_acumulador | empresa, sequencial_do_acumulador | ✔ |
| `efimportador_fixo_nf3e_entrada_acumulador_cfop_consultar` | consultar | efimportador_fixo_nf3e_entrada_acumulador_cfop | empresa | ✔ |
| `efimportador_fixo_nf3e_entrada_acumulador_cfop_obter` | obter | efimportador_fixo_nf3e_entrada_acumulador_cfop | empresa, sequencial_do_acumulador, sequencial_do_cfop | ✔ |
| `efimportador_fixo_nf3e_entrada_cfop_consultar` | consultar | efimportador_fixo_nf3e_entrada_cfop | empresa | ✔ |
| `efimportador_fixo_nf3e_entrada_cfop_obter` | obter | efimportador_fixo_nf3e_entrada_cfop | empresa, sequencial_do_cfop_de_entrada | ✔ |
| `efimportador_fixo_nf3e_entrada_cfop_saida_consultar` | consultar | efimportador_fixo_nf3e_entrada_cfop_saida | empresa | ✔ |
| `efimportador_fixo_nf3e_entrada_cfop_saida_obter` | obter | efimportador_fixo_nf3e_entrada_cfop_saida | empresa, sequencial_do_cfop_de_entrada, sequencial_do_cfop_de_saida | ✔ |
| `efimportador_fixo_nf3e_entrada_cst_csosn_consultar` | consultar | efimportador_fixo_nf3e_entrada_cst_csosn | empresa | ✔ |
| `efimportador_fixo_nf3e_entrada_cst_csosn_obter` | obter | efimportador_fixo_nf3e_entrada_cst_csosn | empresa, sequencial_do_cst_csosn | ✔ |
| `efimportador_fixo_nf3e_entrada_cst_csosn_cfop_consultar` | consultar | efimportador_fixo_nf3e_entrada_cst_csosn_cfop | empresa | ✔ |
| `efimportador_fixo_nf3e_entrada_cst_csosn_cfop_obter` | obter | efimportador_fixo_nf3e_entrada_cst_csosn_cfop | empresa, sequencial_do_cst_csosn, sequencial_do_cfop | ✔ |
| `efimportador_fixo_nf3e_entrada_dados_pis_cofins_consultar` | consultar | efimportador_fixo_nf3e_entrada_dados_pis_cofins | empresa | ✔ |
| `efimportador_fixo_nf3e_entrada_dados_pis_cofins_obter` | obter | efimportador_fixo_nf3e_entrada_dados_pis_cofins | empresa, sequencial_dos_dados_de_pis_cofins | ✔ |
| `efimportador_fixo_nf3e_saida_consultar` | consultar | efimportador_fixo_nf3e_saida | empresa | ✔ |
| `efimportador_fixo_nfce_consultar` | consultar | efimportador_fixo_nfce | empresa | ✔ |
| `efimportador_fixo_nfce_entrada_consultar` | consultar | efimportador_fixo_nfce_entrada | empresa | ✔ |
| `efimportador_fixo_nfce_entrada_acumulador_consultar` | consultar | efimportador_fixo_nfce_entrada_acumulador | empresa | ✔ |
| `efimportador_fixo_nfce_entrada_acumulador_obter` | obter | efimportador_fixo_nfce_entrada_acumulador | empresa, sequencial_do_acumulador | ✔ |
| `efimportador_fixo_nfce_entrada_acumulador_cfop_consultar` | consultar | efimportador_fixo_nfce_entrada_acumulador_cfop | empresa | ✔ |
| `efimportador_fixo_nfce_entrada_acumulador_cfop_obter` | obter | efimportador_fixo_nfce_entrada_acumulador_cfop | empresa, sequencial_do_acumulador, sequencial_do_cfop | ✔ |
| `efimportador_fixo_nfce_entrada_cfop_consultar` | consultar | efimportador_fixo_nfce_entrada_cfop | empresa | ✔ |
| `efimportador_fixo_nfce_entrada_cfop_obter` | obter | efimportador_fixo_nfce_entrada_cfop | empresa, sequencial_do_cfop_de_entrada | ✔ |
| `efimportador_fixo_nfce_entrada_cfop_saida_consultar` | consultar | efimportador_fixo_nfce_entrada_cfop_saida | empresa | ✔ |
| `efimportador_fixo_nfce_entrada_cfop_saida_obter` | obter | efimportador_fixo_nfce_entrada_cfop_saida | empresa, sequencial_do_cfop_de_entrada, sequencial_do_cfop_de_saida | ✔ |
| `efimportador_fixo_nfce_formas_pagamento_consultar` | consultar | efimportador_fixo_nfce_formas_pagamento | — | ✔ |
| `efimportador_fixo_nfce_formas_pagamento_obter` | obter | efimportador_fixo_nfce_formas_pagamento | codigo_da_forma_de_pagamento | ✔ |
| `efimportador_fixo_nfce_saida_consultar` | consultar | efimportador_fixo_nfce_saida | empresa | ✔ |
| `efimportador_fixo_nfce_saida_acumulador_consultar` | consultar | efimportador_fixo_nfce_saida_acumulador | empresa | ✔ |
| `efimportador_fixo_nfce_saida_acumulador_obter` | obter | efimportador_fixo_nfce_saida_acumulador | empresa, sequencial_do_acumulador | ✔ |
| `efimportador_fixo_nfce_saida_acumulador_cfop_consultar` | consultar | efimportador_fixo_nfce_saida_acumulador_cfop | empresa | ✔ |
| `efimportador_fixo_nfce_saida_acumulador_cfop_obter` | obter | efimportador_fixo_nfce_saida_acumulador_cfop | empresa, sequencial_do_acumulador, sequencial_do_cfop | ✔ |
| `efimportador_fixo_nfce_saida_acumulador_forma_pag_3bf3_consultar` | consultar | efimportador_fixo_nfce_saida_acumulador_forma_pagamento | empresa | ✔ |
| `efimportador_fixo_nfce_saida_acumulador_forma_pagamento_obter` | obter | efimportador_fixo_nfce_saida_acumulador_forma_pagamento | empresa, sequencial_do_acumulador, sequencial_da_forma_de_pagamento | ✔ |
| `efimportador_fixo_nfce_saida_diferenca_bc_icms_consultar` | consultar | efimportador_fixo_nfce_saida_diferenca_bc_icms | empresa | ✔ |
| `efimportador_fixo_nfce_saida_diferenca_bc_icms_obter` | obter | efimportador_fixo_nfce_saida_diferenca_bc_icms | empresa, sequencial_da_diferenca | ✔ |
| `efimportador_fixo_nfce_saida_diferenca_bc_icms_totais` | totais | efimportador_fixo_nfce_saida_diferenca_bc_icms | empresa | ✔ |
| `efimportador_fixo_nfe_consultar` | consultar | efimportador_fixo_nfe | empresa | ✔ |
| `efimportador_fixo_nfe_entrada_consultar` | consultar | efimportador_fixo_nfe_entrada | empresa | ✔ |
| `efimportador_fixo_nfe_entrada_acumulador_consultar` | consultar | efimportador_fixo_nfe_entrada_acumulador | empresa | ✔ |
| `efimportador_fixo_nfe_entrada_acumulador_obter` | obter | efimportador_fixo_nfe_entrada_acumulador | empresa, sequencial_do_acumulador | ✔ |
| `efimportador_fixo_nfe_entrada_acumulador_cfop_consultar` | consultar | efimportador_fixo_nfe_entrada_acumulador_cfop | empresa | ✔ |
| `efimportador_fixo_nfe_entrada_acumulador_cfop_obter` | obter | efimportador_fixo_nfe_entrada_acumulador_cfop | empresa, sequencial_do_acumulador, sequencial_do_cfop | ✔ |
| `efimportador_fixo_nfe_entrada_acumulador_cst_consultar` | consultar | efimportador_fixo_nfe_entrada_acumulador_cst | empresa | ✔ |
| `efimportador_fixo_nfe_entrada_acumulador_cst_obter` | obter | efimportador_fixo_nfe_entrada_acumulador_cst | empresa, sequencial_do_acumulador, sequencial_do_cst | ✔ |
| `efimportador_fixo_nfe_entrada_acumulador_forma_pa_b761_consultar` | consultar | efimportador_fixo_nfe_entrada_acumulador_forma_pagamento | empresa | ✔ |
| `efimportador_fixo_nfe_entrada_acumulador_forma_pagamento_obter` | obter | efimportador_fixo_nfe_entrada_acumulador_forma_pagamento | empresa, sequencial_do_acumulador, sequencial_da_forma_de_pagamento | ✔ |
| `efimportador_fixo_nfe_entrada_acumulador_fornecedor_consultar` | consultar | efimportador_fixo_nfe_entrada_acumulador_fornecedor | empresa | ✔ |
| `efimportador_fixo_nfe_entrada_acumulador_fornecedor_obter` | obter | efimportador_fixo_nfe_entrada_acumulador_fornecedor | empresa, sequencial_do_acumulador, sequencial_do_fornecedor | ✔ |
| `efimportador_fixo_nfe_entrada_acumulador_ncm_consultar` | consultar | efimportador_fixo_nfe_entrada_acumulador_ncm | empresa | ✔ |
| `efimportador_fixo_nfe_entrada_acumulador_ncm_obter` | obter | efimportador_fixo_nfe_entrada_acumulador_ncm | empresa, sequencial_do_acumulador, sequencial_do_ncm | ✔ |
| `efimportador_fixo_nfe_entrada_cfop_consultar` | consultar | efimportador_fixo_nfe_entrada_cfop | empresa | ✔ |
| `efimportador_fixo_nfe_entrada_cfop_obter` | obter | efimportador_fixo_nfe_entrada_cfop | empresa, sequencial_do_cfop_de_entrada | ✔ |
| `efimportador_fixo_nfe_entrada_cfop_cst_consultar` | consultar | efimportador_fixo_nfe_entrada_cfop_cst | empresa | ✔ |
| `efimportador_fixo_nfe_entrada_cfop_cst_obter` | obter | efimportador_fixo_nfe_entrada_cfop_cst | empresa, sequencial_do_cfop_de_entrada, sequencial_do_cst | ✔ |
| `efimportador_fixo_nfe_entrada_cfop_excecao_por_fo_2523_consultar` | consultar | efimportador_fixo_nfe_entrada_cfop_excecao_por_fornecedor_cfop_entrada | empresa | ✔ |
| `efimportador_fixo_nfe_entrada_cfop_excecao_por_fornec_2523_obter` | obter | efimportador_fixo_nfe_entrada_cfop_excecao_por_fornecedor_cfop_entrada | empresa, sequencial_do_cfop_de_entrada, sequencial_do_cfop_de_entrada_da_excecao | ✔ |
| `efimportador_fixo_nfe_entrada_cfop_excecao_por_fo_7fca_consultar` | consultar | efimportador_fixo_nfe_entrada_cfop_excecao_por_fornecedor_cfop_entrada_fornecedor | empresa | ✔ |
| `efimportador_fixo_nfe_entrada_cfop_excecao_por_fornec_7fca_obter` | obter | efimportador_fixo_nfe_entrada_cfop_excecao_por_fornecedor_cfop_entrada_fornecedor | empresa, sequencial_do_cfop_de_entrada, sequencial_do_cfop_de_entrada_da_excecao, sequencial_do_fornecedor | ✔ |
| `efimportador_fixo_nfe_entrada_cfop_saida_consultar` | consultar | efimportador_fixo_nfe_entrada_cfop_saida | empresa | ✔ |
| `efimportador_fixo_nfe_entrada_cfop_saida_obter` | obter | efimportador_fixo_nfe_entrada_cfop_saida | empresa, sequencial_do_cfop_de_entrada, sequencial_do_cfop_de_saida | ✔ |
| `efimportador_fixo_nfe_entrada_cst_csosn_consultar` | consultar | efimportador_fixo_nfe_entrada_cst_csosn | empresa | ✔ |
| `efimportador_fixo_nfe_entrada_cst_csosn_obter` | obter | efimportador_fixo_nfe_entrada_cst_csosn | empresa, sequencial_do_cst_csosn | ✔ |
| `efimportador_fixo_nfe_entrada_cst_csosn_cfop_consultar` | consultar | efimportador_fixo_nfe_entrada_cst_csosn_cfop | empresa | ✔ |
| `efimportador_fixo_nfe_entrada_cst_csosn_cfop_obter` | obter | efimportador_fixo_nfe_entrada_cst_csosn_cfop | empresa, sequencial_do_cst_csosn, sequencial_do_cfop | ✔ |
| `efimportador_fixo_nfe_entrada_dados_pis_cofins_consultar` | consultar | efimportador_fixo_nfe_entrada_dados_pis_cofins | empresa | ✔ |
| `efimportador_fixo_nfe_entrada_dados_pis_cofins_obter` | obter | efimportador_fixo_nfe_entrada_dados_pis_cofins | empresa, sequencial_dos_dados_de_pis_cofins | ✔ |
| `efimportador_fixo_nfe_entrada_diferenca_bc_icms_consultar` | consultar | efimportador_fixo_nfe_entrada_diferenca_bc_icms | empresa | ✔ |
| `efimportador_fixo_nfe_entrada_diferenca_bc_icms_obter` | obter | efimportador_fixo_nfe_entrada_diferenca_bc_icms | empresa, sequencial_da_diferenca | ✔ |
| `efimportador_fixo_nfe_entrada_diferenca_bc_icms_totais` | totais | efimportador_fixo_nfe_entrada_diferenca_bc_icms | empresa | ✔ |
| `efimportador_fixo_nfe_entrada_diferenca_bc_ipi_consultar` | consultar | efimportador_fixo_nfe_entrada_diferenca_bc_ipi | empresa | ✔ |
| `efimportador_fixo_nfe_entrada_diferenca_bc_ipi_obter` | obter | efimportador_fixo_nfe_entrada_diferenca_bc_ipi | empresa, sequencial_da_diferenca | ✔ |
| `efimportador_fixo_nfe_entrada_impostos_gerados_consultar` | consultar | efimportador_fixo_nfe_entrada_impostos_gerados | empresa | ✔ |
| `efimportador_fixo_nfe_entrada_impostos_gerados_obter` | obter | efimportador_fixo_nfe_entrada_impostos_gerados | empresa, sequencial_do_imposto_gerado | ✔ |
| `efimportador_fixo_nfe_entrada_impostos_notas_op_n_0fbb_consultar` | consultar | efimportador_fixo_nfe_entrada_impostos_notas_op_nacional | empresa | ✔ |
| `efimportador_fixo_nfe_entrada_produto_mov_fisica_consultar` | consultar | efimportador_fixo_nfe_entrada_produto_mov_fisica | empresa | ✔ |
| `efimportador_fixo_nfe_entrada_produto_mov_fisica_obter` | obter | efimportador_fixo_nfe_entrada_produto_mov_fisica | empresa, sequencial_movimentacao_fisica | ✔ |
| `efimportador_fixo_nfe_formas_pagamento_consultar` | consultar | efimportador_fixo_nfe_formas_pagamento | — | ✔ |
| `efimportador_fixo_nfe_formas_pagamento_obter` | obter | efimportador_fixo_nfe_formas_pagamento | codigo_da_forma_de_pagamento | ✔ |
| `efimportador_fixo_nfe_saida_consultar` | consultar | efimportador_fixo_nfe_saida | empresa | ✔ |
| `efimportador_fixo_nfe_saida_acumulador_consultar` | consultar | efimportador_fixo_nfe_saida_acumulador | empresa | ✔ |
| `efimportador_fixo_nfe_saida_acumulador_obter` | obter | efimportador_fixo_nfe_saida_acumulador | empresa, sequencial_do_acumulador | ✔ |
| `efimportador_fixo_nfe_saida_acumulador_cfop_consultar` | consultar | efimportador_fixo_nfe_saida_acumulador_cfop | empresa | ✔ |
| `efimportador_fixo_nfe_saida_acumulador_cfop_obter` | obter | efimportador_fixo_nfe_saida_acumulador_cfop | empresa, sequencial_do_acumulador, sequencial_do_cfop | ✔ |
| `efimportador_fixo_nfe_saida_acumulador_cliente_consultar` | consultar | efimportador_fixo_nfe_saida_acumulador_cliente | empresa | ✔ |
| `efimportador_fixo_nfe_saida_acumulador_cliente_obter` | obter | efimportador_fixo_nfe_saida_acumulador_cliente | empresa, sequencial_do_acumulador, sequencial_do_cliente | ✔ |
| `efimportador_fixo_nfe_saida_acumulador_cst_consultar` | consultar | efimportador_fixo_nfe_saida_acumulador_cst | empresa | ✔ |
| `efimportador_fixo_nfe_saida_acumulador_cst_obter` | obter | efimportador_fixo_nfe_saida_acumulador_cst | empresa, sequencial_do_acumulador, sequencial_do_cst | ✔ |
| `efimportador_fixo_nfe_saida_acumulador_cst_pis_consultar` | consultar | efimportador_fixo_nfe_saida_acumulador_cst_pis | empresa | ✔ |
| `efimportador_fixo_nfe_saida_acumulador_cst_pis_obter` | obter | efimportador_fixo_nfe_saida_acumulador_cst_pis | empresa, sequencial_do_acumulador, sequencial_do_cst | ✔ |
| `efimportador_fixo_nfe_saida_acumulador_forma_pagamento_consultar` | consultar | efimportador_fixo_nfe_saida_acumulador_forma_pagamento | empresa | ✔ |
| `efimportador_fixo_nfe_saida_acumulador_forma_pagamento_obter` | obter | efimportador_fixo_nfe_saida_acumulador_forma_pagamento | empresa, sequencial_do_acumulador, sequencial_da_forma_de_pagamento | ✔ |
| `efimportador_fixo_nfe_saida_acumulador_ncm_consultar` | consultar | efimportador_fixo_nfe_saida_acumulador_ncm | empresa | ✔ |
| `efimportador_fixo_nfe_saida_acumulador_ncm_obter` | obter | efimportador_fixo_nfe_saida_acumulador_ncm | empresa, sequencial_do_acumulador, sequencial_do_ncm | ✔ |
| `efimportador_fixo_nfe_saida_cfop_consultar` | consultar | efimportador_fixo_nfe_saida_cfop | empresa | ✔ |
| `efimportador_fixo_nfe_saida_cfop_obter` | obter | efimportador_fixo_nfe_saida_cfop | empresa, sequencial_do_cfop_de_entrada | ✔ |
| `efimportador_fixo_nfe_saida_cfop_cst_consultar` | consultar | efimportador_fixo_nfe_saida_cfop_cst | empresa | ✔ |
| `efimportador_fixo_nfe_saida_cfop_cst_obter` | obter | efimportador_fixo_nfe_saida_cfop_cst | empresa, sequencial_do_cfop_de_entrada, sequencial_do_cst | ✔ |
| `efimportador_fixo_nfe_saida_cfop_entrada_consultar` | consultar | efimportador_fixo_nfe_saida_cfop_entrada | empresa | ✔ |
| `efimportador_fixo_nfe_saida_cfop_entrada_obter` | obter | efimportador_fixo_nfe_saida_cfop_entrada | empresa, sequencial_do_cfop_de_saida, sequencial_do_cfop_de_entrada | ✔ |
| `efimportador_fixo_nfe_saida_cst_csosn_consultar` | consultar | efimportador_fixo_nfe_saida_cst_csosn | empresa | ✔ |
| `efimportador_fixo_nfe_saida_cst_csosn_obter` | obter | efimportador_fixo_nfe_saida_cst_csosn | empresa, sequencial_do_cst_csosn | ✔ |
| `efimportador_fixo_nfe_saida_cst_csosn_cfop_consultar` | consultar | efimportador_fixo_nfe_saida_cst_csosn_cfop | empresa | ✔ |
| `efimportador_fixo_nfe_saida_cst_csosn_cfop_obter` | obter | efimportador_fixo_nfe_saida_cst_csosn_cfop | empresa, sequencial_do_cst_csosn, sequencial_do_cfop | ✔ |
| `efimportador_fixo_nfe_saida_dados_pis_cofins_consultar` | consultar | efimportador_fixo_nfe_saida_dados_pis_cofins | empresa | ✔ |
| `efimportador_fixo_nfe_saida_dados_pis_cofins_obter` | obter | efimportador_fixo_nfe_saida_dados_pis_cofins | empresa, sequencial_dos_dados_de_pis_cofins | ✔ |
| `efimportador_fixo_nfe_saida_dados_pis_cofins_cfop_consultar` | consultar | efimportador_fixo_nfe_saida_dados_pis_cofins_cfop | empresa | ✔ |
| `efimportador_fixo_nfe_saida_dados_pis_cofins_cfop_obter` | obter | efimportador_fixo_nfe_saida_dados_pis_cofins_cfop | empresa, sequencial_dos_dados_de_pis_cofins, sequencial_do_cfop | ✔ |
| `efimportador_fixo_nfe_saida_dados_pis_cofins_dados_consultar` | consultar | efimportador_fixo_nfe_saida_dados_pis_cofins_dados | empresa | ✔ |
| `efimportador_fixo_nfe_saida_dados_pis_cofins_dados_obter` | obter | efimportador_fixo_nfe_saida_dados_pis_cofins_dados | empresa, sequencial_dos_dados_de_pis_cofins | ✔ |
| `efimportador_fixo_nfe_saida_dados_pis_cofins_dados_totais` | totais | efimportador_fixo_nfe_saida_dados_pis_cofins_dados | empresa | ✔ |
| `efimportador_fixo_nfe_saida_diferenca_bc_icms_consultar` | consultar | efimportador_fixo_nfe_saida_diferenca_bc_icms | empresa | ✔ |
| `efimportador_fixo_nfe_saida_diferenca_bc_icms_obter` | obter | efimportador_fixo_nfe_saida_diferenca_bc_icms | empresa, sequencial_da_diferenca | ✔ |
| `efimportador_fixo_nfe_saida_diferenca_bc_icms_totais` | totais | efimportador_fixo_nfe_saida_diferenca_bc_icms | empresa | ✔ |
| `efimportador_fixo_nfe_saida_diferenca_bc_ipi_consultar` | consultar | efimportador_fixo_nfe_saida_diferenca_bc_ipi | empresa | ✔ |
| `efimportador_fixo_nfe_saida_diferenca_bc_ipi_obter` | obter | efimportador_fixo_nfe_saida_diferenca_bc_ipi | empresa, sequencial_da_diferenca | ✔ |
| `efimportador_fixo_nfe_saida_produto_mov_fisica_consultar` | consultar | efimportador_fixo_nfe_saida_produto_mov_fisica | empresa | ✔ |
| `efimportador_fixo_nfe_saida_produto_mov_fisica_obter` | obter | efimportador_fixo_nfe_saida_produto_mov_fisica | empresa, sequencial_movimentacao_fisica | ✔ |
| `efimportador_fixo_nfse_consultar` | consultar | efimportador_fixo_nfse | empresa | ✔ |
| `efimportador_fixo_nfse_entrada_consultar` | consultar | efimportador_fixo_nfse_entrada | empresa | ✔ |
| `efimportador_fixo_nfse_entrada_acumulador_consultar` | consultar | efimportador_fixo_nfse_entrada_acumulador | empresa | ✔ |
| `efimportador_fixo_nfse_entrada_acumulador_obter` | obter | efimportador_fixo_nfse_entrada_acumulador | empresa, sequencial_do_acumulador | ✔ |
| `efimportador_fixo_nfse_entrada_acumulador_item_servico_consultar` | consultar | efimportador_fixo_nfse_entrada_acumulador_item_servico | empresa | ✔ |
| `efimportador_fixo_nfse_entrada_acumulador_item_servico_obter` | obter | efimportador_fixo_nfse_entrada_acumulador_item_servico | empresa, sequencial_do_acumulador, sequencial_do_item_de_servico | ✔ |
| `efimportador_fixo_nfse_nacional_consultar` | consultar | efimportador_fixo_nfse_nacional | empresa | ✔ |
| `efimportador_fixo_nfse_nacional_entrada_consultar` | consultar | efimportador_fixo_nfse_nacional_entrada | empresa | ✔ |
| `efimportador_fixo_nfse_nacional_entrada_acumulador_consultar` | consultar | efimportador_fixo_nfse_nacional_entrada_acumulador | empresa | ✔ |
| `efimportador_fixo_nfse_nacional_entrada_acumulador_obter` | obter | efimportador_fixo_nfse_nacional_entrada_acumulador | empresa, sequencial_do_acumulador | ✔ |
| `efimportador_fixo_nfse_nacional_servico_consultar` | consultar | efimportador_fixo_nfse_nacional_servico | empresa | ✔ |
| `efimportador_fixo_nfse_nacional_servico_acumulador_consultar` | consultar | efimportador_fixo_nfse_nacional_servico_acumulador | empresa | ✔ |
| `efimportador_fixo_nfse_nacional_servico_acumulador_obter` | obter | efimportador_fixo_nfse_nacional_servico_acumulador | empresa, sequencial_do_acumulador | ✔ |
| `efimportador_fixo_nfse_nacional_servico_acumulado_ec29_consultar` | consultar | efimportador_fixo_nfse_nacional_servico_acumulador_item_servico | empresa | ✔ |
| `efimportador_fixo_nfse_nacional_servico_acumulador_it_ec29_obter` | obter | efimportador_fixo_nfse_nacional_servico_acumulador_item_servico | empresa, sequencial_do_acumulador, sequencial_do_item_de_servico | ✔ |
| `efimportador_fixo_nfse_servico_consultar` | consultar | efimportador_fixo_nfse_servico | empresa | ✔ |
| `efimportador_fixo_nfse_servico_acumulador_consultar` | consultar | efimportador_fixo_nfse_servico_acumulador | empresa | ✔ |
| `efimportador_fixo_nfse_servico_acumulador_obter` | obter | efimportador_fixo_nfse_servico_acumulador | empresa, sequencial_do_acumulador | ✔ |
| `efimportador_fixo_nfse_servico_acumulador_cliente_consultar` | consultar | efimportador_fixo_nfse_servico_acumulador_cliente | empresa | ✔ |
| `efimportador_fixo_nfse_servico_acumulador_cliente_obter` | obter | efimportador_fixo_nfse_servico_acumulador_cliente | empresa, sequencial_do_acumulador, sequencial_do_cliente | ✔ |
| `efimportador_fixo_nfse_servico_acumulador_item_servico_consultar` | consultar | efimportador_fixo_nfse_servico_acumulador_item_servico | empresa | ✔ |
| `efimportador_fixo_nfse_servico_acumulador_item_servico_obter` | obter | efimportador_fixo_nfse_servico_acumulador_item_servico | empresa, sequencial_do_acumulador, sequencial_do_item_de_servico | ✔ |
| `efimportador_fixo_sintegra_consultar` | consultar | efimportador_fixo_sintegra | empresa | ✔ |
| `efimportador_fixo_sintegra_situacao_tributaria_consultar` | consultar | efimportador_fixo_sintegra_situacao_tributaria | empresa | ✔ |
| `efimportador_fixo_sintegra_situacao_tributaria_obter` | obter | efimportador_fixo_sintegra_situacao_tributaria | empresa, sequencial_da_situacao_tributaria | ✔ |
| `efimportador_fixo_sintegra_situacao_tributaria_totais` | totais | efimportador_fixo_sintegra_situacao_tributaria | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_consultar` | consultar | efimportador_fixo_sped_fiscal | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_bilhete_passagem_consultar` | consultar | efimportador_fixo_sped_fiscal_bilhete_passagem | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_cfe_saida_consultar` | consultar | efimportador_fixo_sped_fiscal_cfe_saida | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_cfe_saida_acumulador_consultar` | consultar | efimportador_fixo_sped_fiscal_cfe_saida_acumulador | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_cfe_saida_acumulador_obter` | obter | efimportador_fixo_sped_fiscal_cfe_saida_acumulador | empresa, sequencial_do_acumulador | ✔ |
| `efimportador_fixo_sped_fiscal_cfe_saida_acumulado_10e8_consultar` | consultar | efimportador_fixo_sped_fiscal_cfe_saida_acumulador_cfop | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_cfe_saida_acumulador_cfop_obter` | obter | efimportador_fixo_sped_fiscal_cfe_saida_acumulador_cfop | empresa, sequencial_do_acumulador, sequencial_do_cfop | ✔ |
| `efimportador_fixo_sped_fiscal_cfe_saida_diferenca_ceb5_consultar` | consultar | efimportador_fixo_sped_fiscal_cfe_saida_diferenca_bc_icms | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_cfe_saida_diferenca_bc_icms_obter` | obter | efimportador_fixo_sped_fiscal_cfe_saida_diferenca_bc_icms | empresa, sequencial_da_diferenca | ✔ |
| `efimportador_fixo_sped_fiscal_entrada_consultar` | consultar | efimportador_fixo_sped_fiscal_entrada | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_entrada_acumulador_consultar` | consultar | efimportador_fixo_sped_fiscal_entrada_acumulador | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_entrada_acumulador_obter` | obter | efimportador_fixo_sped_fiscal_entrada_acumulador | empresa, sequencial_do_acumulador | ✔ |
| `efimportador_fixo_sped_fiscal_entrada_acumulador_cfop_consultar` | consultar | efimportador_fixo_sped_fiscal_entrada_acumulador_cfop | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_entrada_acumulador_cfop_obter` | obter | efimportador_fixo_sped_fiscal_entrada_acumulador_cfop | empresa, sequencial_do_acumulador, sequencial_do_cfop | ✔ |
| `efimportador_fixo_sped_fiscal_entrada_diferenca_b_5171_consultar` | consultar | efimportador_fixo_sped_fiscal_entrada_diferenca_bc_icms | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_entrada_diferenca_bc_icms_obter` | obter | efimportador_fixo_sped_fiscal_entrada_diferenca_bc_icms | empresa, sequencial_da_diferenca | ✔ |
| `efimportador_fixo_sped_fiscal_entrada_diferenca_bc_icms_totais` | totais | efimportador_fixo_sped_fiscal_entrada_diferenca_bc_icms | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_especie_consultar` | consultar | efimportador_fixo_sped_fiscal_especie | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_especie_obter` | obter | efimportador_fixo_sped_fiscal_especie | empresa, sequencial_do_relacionamento_de_modelos | ✔ |
| `efimportador_fixo_sped_fiscal_grupo_produtos_consultar` | consultar | efimportador_fixo_sped_fiscal_grupo_produtos | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_grupo_produtos_obter` | obter | efimportador_fixo_sped_fiscal_grupo_produtos | empresa, sequencial_do_grupo_dos_produtos | ✔ |
| `efimportador_fixo_sped_fiscal_produto_mov_fisica_consultar` | consultar | efimportador_fixo_sped_fiscal_produto_mov_fisica | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_produto_mov_fisica_obter` | obter | efimportador_fixo_sped_fiscal_produto_mov_fisica | empresa, sequencial_movimentacao_fisica | ✔ |
| `efimportador_fixo_sped_fiscal_reducao_z_consultar` | consultar | efimportador_fixo_sped_fiscal_reducao_z | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_reducao_z_saidas_si_8034_consultar` | consultar | efimportador_fixo_sped_fiscal_reducao_z_saidas_situacao_tributaria | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_reducao_z_saidas_situac_8034_obter` | obter | efimportador_fixo_sped_fiscal_reducao_z_saidas_situacao_tributaria | empresa, sequencial_da_situacao_tributaria | ✔ |
| `efimportador_fixo_sped_fiscal_reducao_z_saidas_situa_8034_totais` | totais | efimportador_fixo_sped_fiscal_reducao_z_saidas_situacao_tributaria | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_reducao_z_saidas_si_8b3b_consultar` | consultar | efimportador_fixo_sped_fiscal_reducao_z_saidas_situacao_tributaria_cfop | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_reducao_z_saidas_situac_8b3b_obter` | obter | efimportador_fixo_sped_fiscal_reducao_z_saidas_situacao_tributaria_cfop | empresa, sequencial_da_situacao_tributaria, sequencial_do_cfop | ✔ |
| `efimportador_fixo_sped_fiscal_reducao_z_saidas_si_9184_consultar` | consultar | efimportador_fixo_sped_fiscal_reducao_z_saidas_situacao_tributaria_cfop_fixo | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_reducao_z_saidas_situac_9184_obter` | obter | efimportador_fixo_sped_fiscal_reducao_z_saidas_situacao_tributaria_cfop_fixo | empresa, sequencial_da_situacao_tributaria | ✔ |
| `efimportador_fixo_sped_fiscal_reducao_z_saidas_situa_9184_totais` | totais | efimportador_fixo_sped_fiscal_reducao_z_saidas_situacao_tributaria_cfop_fixo | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_saida_consultar` | consultar | efimportador_fixo_sped_fiscal_saida | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_saida_acumulador_consultar` | consultar | efimportador_fixo_sped_fiscal_saida_acumulador | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_saida_acumulador_obter` | obter | efimportador_fixo_sped_fiscal_saida_acumulador | empresa, sequencial_do_acumulador | ✔ |
| `efimportador_fixo_sped_fiscal_saida_acumulador_cfop_consultar` | consultar | efimportador_fixo_sped_fiscal_saida_acumulador_cfop | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_saida_acumulador_cfop_obter` | obter | efimportador_fixo_sped_fiscal_saida_acumulador_cfop | empresa, sequencial_do_acumulador, sequencial_do_cfop | ✔ |
| `efimportador_fixo_sped_fiscal_saida_diferenca_bc_icms_consultar` | consultar | efimportador_fixo_sped_fiscal_saida_diferenca_bc_icms | empresa | ✔ |
| `efimportador_fixo_sped_fiscal_saida_diferenca_bc_icms_obter` | obter | efimportador_fixo_sped_fiscal_saida_diferenca_bc_icms | empresa, sequencial_da_diferenca | ✔ |
| `efimportador_fixo_sped_fiscal_saida_diferenca_bc_icms_totais` | totais | efimportador_fixo_sped_fiscal_saida_diferenca_bc_icms | empresa | ✔ |
| `efimportador_fixo_sped_pis_cofins_consultar` | consultar | efimportador_fixo_sped_pis_cofins | empresa | ✔ |
| `efimportador_fixo_sped_pis_cofins_entrada_consultar` | consultar | efimportador_fixo_sped_pis_cofins_entrada | empresa | ✔ |
| `efimportador_fixo_sped_pis_cofins_entrada_acumulador_consultar` | consultar | efimportador_fixo_sped_pis_cofins_entrada_acumulador | empresa | ✔ |
| `efimportador_fixo_sped_pis_cofins_entrada_acumulador_obter` | obter | efimportador_fixo_sped_pis_cofins_entrada_acumulador | empresa, sequencial_do_acumulador | ✔ |
| `efimportador_fixo_sped_pis_cofins_entrada_acumula_11f4_consultar` | consultar | efimportador_fixo_sped_pis_cofins_entrada_acumulador_cfop | empresa | ✔ |
| `efimportador_fixo_sped_pis_cofins_entrada_acumulador_cfop_obter` | obter | efimportador_fixo_sped_pis_cofins_entrada_acumulador_cfop | empresa, sequencial_do_acumulador, sequencial_do_cfop | ✔ |
| `efimportador_fixo_sped_pis_cofins_entrada_diferen_092d_consultar` | consultar | efimportador_fixo_sped_pis_cofins_entrada_diferenca_bc_icms | empresa | ✔ |
| `efimportador_fixo_sped_pis_cofins_entrada_diferenca_b_092d_obter` | obter | efimportador_fixo_sped_pis_cofins_entrada_diferenca_bc_icms | empresa, sequencial_da_diferenca | ✔ |
| `efimportador_fixo_sped_pis_cofins_entrada_diferenca__092d_totais` | totais | efimportador_fixo_sped_pis_cofins_entrada_diferenca_bc_icms | empresa | ✔ |
| `efimportador_fixo_sped_pis_cofins_especie_consultar` | consultar | efimportador_fixo_sped_pis_cofins_especie | empresa | ✔ |
| `efimportador_fixo_sped_pis_cofins_especie_obter` | obter | efimportador_fixo_sped_pis_cofins_especie | empresa, sequencial_do_relacionamento_de_modelos | ✔ |
| `efimportador_fixo_sped_pis_cofins_grupo_produtos_consultar` | consultar | efimportador_fixo_sped_pis_cofins_grupo_produtos | empresa | ✔ |
| `efimportador_fixo_sped_pis_cofins_grupo_produtos_obter` | obter | efimportador_fixo_sped_pis_cofins_grupo_produtos | empresa, sequencial_do_grupo_dos_produtos | ✔ |
| `efimportador_fixo_sped_pis_cofins_saida_consultar` | consultar | efimportador_fixo_sped_pis_cofins_saida | empresa | ✔ |
| `efimportador_fixo_sped_pis_cofins_saida_acumulador_consultar` | consultar | efimportador_fixo_sped_pis_cofins_saida_acumulador | empresa | ✔ |
| `efimportador_fixo_sped_pis_cofins_saida_acumulador_obter` | obter | efimportador_fixo_sped_pis_cofins_saida_acumulador | empresa, sequencial_do_acumulador | ✔ |
| `efimportador_fixo_sped_pis_cofins_saida_acumulado_3d8e_consultar` | consultar | efimportador_fixo_sped_pis_cofins_saida_acumulador_cfop | empresa | ✔ |
| `efimportador_fixo_sped_pis_cofins_saida_acumulador_cfop_obter` | obter | efimportador_fixo_sped_pis_cofins_saida_acumulador_cfop | empresa, sequencial_do_acumulador, sequencial_do_cfop | ✔ |
| `efimportador_fixo_sped_pis_cofins_servico_consultar` | consultar | efimportador_fixo_sped_pis_cofins_servico | empresa | ✔ |
| `efimportador_sefaz_es_campos_pagina_consultar` | consultar | efimportador_sefaz_es_campos_pagina | — | ✔ |
| `efimportador_sefaz_es_campos_pagina_obter` | obter | efimportador_sefaz_es_campos_pagina | campo_da_pagina | ✔ |
| `efimportador_sefaz_ms_campos_pagina_consultar` | consultar | efimportador_sefaz_ms_campos_pagina | — | ✔ |
| `efimportador_sefaz_ms_campos_pagina_obter` | obter | efimportador_sefaz_ms_campos_pagina | campo_da_pagina | ✔ |
| `efimportador_sefaz_mt_campos_pagina_consultar` | consultar | efimportador_sefaz_mt_campos_pagina | — | ✔ |
| `efimportador_sefaz_mt_campos_pagina_obter` | obter | efimportador_sefaz_mt_campos_pagina | campo_da_pagina | ✔ |
| `efimportador_sefaz_rs_campos_pagina_consultar` | consultar | efimportador_sefaz_rs_campos_pagina | — | ✔ |
| `efimportador_sefaz_rs_campos_pagina_obter` | obter | efimportador_sefaz_rs_campos_pagina | campo_da_pagina | ✔ |
| `efimportador_sefaz_sc_campos_pagina_consultar` | consultar | efimportador_sefaz_sc_campos_pagina | — | ✔ |
| `efimportador_sefaz_sc_campos_pagina_obter` | obter | efimportador_sefaz_sc_campos_pagina | campo_da_pagina | ✔ |
| `efimportador_site_cad_cpf_campos_pagina_consultar` | consultar | efimportador_site_cad_cpf_campos_pagina | — | ✔ |
| `efimportador_site_cad_cpf_campos_pagina_obter` | obter | efimportador_site_cad_cpf_campos_pagina | campo_da_pagina | ✔ |
| `efimportador_site_cadastros_campos_pagina_consultar` | consultar | efimportador_site_cadastros_campos_pagina | — | ✔ |
| `efimportador_site_cadastros_campos_pagina_obter` | obter | efimportador_site_cadastros_campos_pagina | campo_da_pagina | ✔ |
| `efimportador_site_cte_consultar` | consultar | efimportador_site_cte | empresa | ✔ |
| `efimportador_site_cte_campos_pagina_consultar` | consultar | efimportador_site_cte_campos_pagina | — | ✔ |
| `efimportador_site_cte_campos_pagina_obter` | obter | efimportador_site_cte_campos_pagina | campo_da_pagina | ✔ |
| `efimportador_site_cte_entrada_consultar` | consultar | efimportador_site_cte_entrada | empresa | ✔ |
| `efimportador_site_cte_entrada_acumulador_consultar` | consultar | efimportador_site_cte_entrada_acumulador | empresa | ✔ |
| `efimportador_site_cte_entrada_acumulador_obter` | obter | efimportador_site_cte_entrada_acumulador | empresa, sequencial_do_acumulador | ✔ |
| `efimportador_site_cte_entrada_acumulador_cfop_consultar` | consultar | efimportador_site_cte_entrada_acumulador_cfop | empresa | ✔ |
| `efimportador_site_cte_entrada_acumulador_cfop_obter` | obter | efimportador_site_cte_entrada_acumulador_cfop | empresa, sequencial_do_acumulador, sequencial_do_cfop | ✔ |
| `efimportador_site_cte_entrada_cfop_consultar` | consultar | efimportador_site_cte_entrada_cfop | empresa | ✔ |
| `efimportador_site_cte_entrada_cfop_obter` | obter | efimportador_site_cte_entrada_cfop | empresa, sequencial_do_cfop_de_entrada | ✔ |
| `efimportador_site_cte_entrada_cfop_saida_consultar` | consultar | efimportador_site_cte_entrada_cfop_saida | empresa | ✔ |
| `efimportador_site_cte_entrada_cfop_saida_obter` | obter | efimportador_site_cte_entrada_cfop_saida | empresa, sequencial_do_cfop_de_entrada, sequencial_do_cfop_de_saida | ✔ |
| `efimportador_site_cte_entrada_diferenca_bc_icms_consultar` | consultar | efimportador_site_cte_entrada_diferenca_bc_icms | empresa | ✔ |
| `efimportador_site_cte_entrada_diferenca_bc_icms_obter` | obter | efimportador_site_cte_entrada_diferenca_bc_icms | empresa, sequencial_da_diferenca | ✔ |
| `efimportador_site_cte_entrada_diferenca_bc_icms_totais` | totais | efimportador_site_cte_entrada_diferenca_bc_icms | empresa | ✔ |
| `efimportador_site_cte_nfe_campos_pagina_consultar` | consultar | efimportador_site_cte_nfe_campos_pagina | — | ✔ |
| `efimportador_site_cte_nfe_campos_pagina_obter` | obter | efimportador_site_cte_nfe_campos_pagina | campo_da_pagina | ✔ |
| `efimportador_site_cte_saida_consultar` | consultar | efimportador_site_cte_saida | empresa | ✔ |
| `efimportador_site_cte_saida_acumulador_consultar` | consultar | efimportador_site_cte_saida_acumulador | empresa | ✔ |
| `efimportador_site_cte_saida_acumulador_obter` | obter | efimportador_site_cte_saida_acumulador | empresa, sequencial_do_acumulador | ✔ |
| `efimportador_site_cte_saida_acumulador_cfop_consultar` | consultar | efimportador_site_cte_saida_acumulador_cfop | empresa | ✔ |
| `efimportador_site_cte_saida_acumulador_cfop_obter` | obter | efimportador_site_cte_saida_acumulador_cfop | empresa, sequencial_do_acumulador, sequencial_do_cfop | ✔ |
| `efimportador_site_cte_saida_diferenca_bc_icms_consultar` | consultar | efimportador_site_cte_saida_diferenca_bc_icms | empresa | ✔ |
| `efimportador_site_cte_saida_diferenca_bc_icms_obter` | obter | efimportador_site_cte_saida_diferenca_bc_icms | empresa, sequencial_da_diferenca | ✔ |
| `efimportador_site_cte_saida_diferenca_bc_icms_totais` | totais | efimportador_site_cte_saida_diferenca_bc_icms | empresa | ✔ |
| `efimportador_site_portal_nfe_campos_pagina_consultar` | consultar | efimportador_site_portal_nfe_campos_pagina | — | ✔ |
| `efimportador_site_portal_nfe_campos_pagina_obter` | obter | efimportador_site_portal_nfe_campos_pagina | campo_da_pagina | ✔ |
| `efimportador_xml_portal_federal_consultar` | consultar | efimportador_xml_portal_federal | empresa | ✔ |
| `efimportador_xml_portal_federal_alteracao_consultar` | consultar | efimportador_xml_portal_federal_alteracao | — | ✔ |
| `efimportador_xml_portal_federal_alteracao_obter` | obter | efimportador_xml_portal_federal_alteracao | possui_alteracao | ✔ |
