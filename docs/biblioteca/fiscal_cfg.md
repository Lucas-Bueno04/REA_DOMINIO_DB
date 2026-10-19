# Módulo `fiscal_cfg`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `efcfg_importacao_nfe_consultar` | consultar | efcfg_importacao_nfe | empresa | ✔ |
| `efcfg_importacao_nfe_obter` | obter | efcfg_importacao_nfe | empresa, tipo_de_nota_1_entradas_2_saidas_3_servi | ✔ |
| `efcfg_importacao_nfe_acumuladores_entradas_consultar` | consultar | efcfg_importacao_nfe_acumuladores_entradas | empresa | ✔ |
| `efcfg_importacao_nfe_acumuladores_entradas_obter` | obter | efcfg_importacao_nfe_acumuladores_entradas | empresa, sequencial_do_acumulador | ✔ |
| `efcfg_importacao_nfe_acumuladores_entradas_fornec_cf6d_consultar` | consultar | efcfg_importacao_nfe_acumuladores_entradas_fornecedores_selecionados | empresa | ✔ |
| `efcfg_importacao_nfe_acumuladores_entradas_fornecedor_cf6d_obter` | obter | efcfg_importacao_nfe_acumuladores_entradas_fornecedores_selecionados | empresa, sequencial_do_acumulador, sequencial_do_fornecedor | ✔ |
| `efcfg_importacao_nfe_acumuladores_entradas_item_s_01fe_consultar` | consultar | efcfg_importacao_nfe_acumuladores_entradas_item_servico | empresa | ✔ |
| `efcfg_importacao_nfe_acumuladores_entradas_item_servico_obter` | obter | efcfg_importacao_nfe_acumuladores_entradas_item_servico | empresa, sequencial_do_acumulador, sequencial_do_item_do_servico | ✔ |
| `efcfg_importacao_nfe_acumuladores_entradas_situac_5bf9_consultar` | consultar | efcfg_importacao_nfe_acumuladores_entradas_situacao_nota | empresa | ✔ |
| `efcfg_importacao_nfe_acumuladores_entradas_situacao_nota_obter` | obter | efcfg_importacao_nfe_acumuladores_entradas_situacao_nota | empresa, sequencial_do_acumulador, sequencial_da_situacao_da_nota | ✔ |
| `efcfg_importacao_nfe_acumuladores_saidas_consultar` | consultar | efcfg_importacao_nfe_acumuladores_saidas | empresa | ✔ |
| `efcfg_importacao_nfe_acumuladores_saidas_obter` | obter | efcfg_importacao_nfe_acumuladores_saidas | empresa, sequencial_do_acumulador | ✔ |
| `efcfg_importacao_nfe_acumuladores_saidas_situacao_nota_consultar` | consultar | efcfg_importacao_nfe_acumuladores_saidas_situacao_nota | empresa | ✔ |
| `efcfg_importacao_nfe_acumuladores_saidas_situacao_nota_obter` | obter | efcfg_importacao_nfe_acumuladores_saidas_situacao_nota | empresa, sequencial_do_acumulador, sequencial_da_situacao_da_nota | ✔ |
| `efcfg_importacao_nfe_acumuladores_servicos_consultar` | consultar | efcfg_importacao_nfe_acumuladores_servicos | empresa | ✔ |
| `efcfg_importacao_nfe_acumuladores_servicos_obter` | obter | efcfg_importacao_nfe_acumuladores_servicos | empresa, sequencial_do_acumulador | ✔ |
| `efcfg_importacao_nfe_acumuladores_servicos_client_a0f0_consultar` | consultar | efcfg_importacao_nfe_acumuladores_servicos_clientes_selecionados | empresa | ✔ |
| `efcfg_importacao_nfe_acumuladores_servicos_clientes_s_a0f0_obter` | obter | efcfg_importacao_nfe_acumuladores_servicos_clientes_selecionados | empresa, sequencial_do_acumulador, sequencial_do_cliente | ✔ |
| `efcfg_importacao_nfe_acumuladores_servicos_item_s_a3e1_consultar` | consultar | efcfg_importacao_nfe_acumuladores_servicos_item_servico | empresa | ✔ |
| `efcfg_importacao_nfe_acumuladores_servicos_item_servico_obter` | obter | efcfg_importacao_nfe_acumuladores_servicos_item_servico | empresa, sequencial_do_acumulador, sequencial_do_item_do_servico | ✔ |
| `efcfg_importacao_nfe_acumuladores_servicos_situac_a82f_consultar` | consultar | efcfg_importacao_nfe_acumuladores_servicos_situacao_nota | empresa | ✔ |
| `efcfg_importacao_nfe_acumuladores_servicos_situacao_nota_obter` | obter | efcfg_importacao_nfe_acumuladores_servicos_situacao_nota | empresa, sequencial_do_acumulador, sequencial_da_situacao_da_nota | ✔ |
| `efcfg_importacao_nfe_entradas_parcelas_consultar` | consultar | efcfg_importacao_nfe_entradas_parcelas | empresa | ✔ |
| `efcfg_importacao_nfe_entradas_parcelas_obter` | obter | efcfg_importacao_nfe_entradas_parcelas | empresa, tipo_de_nota_1_entradas_2_saidas_3_servi | ✔ |
| `efcfg_importacao_nfe_entradas_parcelas_totais` | totais | efcfg_importacao_nfe_entradas_parcelas | empresa | ✔ |
| `efcfg_importacao_nfe_itens_entradas_consultar` | consultar | efcfg_importacao_nfe_itens_entradas | empresa | ✔ |
| `efcfg_importacao_nfe_itens_entradas_obter` | obter | efcfg_importacao_nfe_itens_entradas | empresa, sequencial_do_produto | ✔ |
| `efcfg_importacao_nfe_itens_selecionar_entradas_consultar` | consultar | efcfg_importacao_nfe_itens_selecionar_entradas | empresa | ✔ |
| `efcfg_importacao_nfe_itens_selecionar_entradas_obter` | obter | efcfg_importacao_nfe_itens_selecionar_entradas | empresa, sequencial_do_pai, sequencial_do_item_servico | ✔ |
| `efcfg_importacao_nfe_itens_selecionar_servicos_consultar` | consultar | efcfg_importacao_nfe_itens_selecionar_servicos | empresa | ✔ |
| `efcfg_importacao_nfe_itens_selecionar_servicos_obter` | obter | efcfg_importacao_nfe_itens_selecionar_servicos | empresa, sequencial_do_pai, sequencial_do_item_servico | ✔ |
| `efcfg_importacao_nfe_itens_servicos_consultar` | consultar | efcfg_importacao_nfe_itens_servicos | empresa | ✔ |
| `efcfg_importacao_nfe_itens_servicos_obter` | obter | efcfg_importacao_nfe_itens_servicos | empresa, sequencial_do_produto | ✔ |
| `efcfg_importacao_nfe_saidas_parcelas_consultar` | consultar | efcfg_importacao_nfe_saidas_parcelas | empresa | ✔ |
| `efcfg_importacao_nfe_saidas_parcelas_obter` | obter | efcfg_importacao_nfe_saidas_parcelas | empresa, tipo_de_nota_1_entradas_2_saidas_3_servi | ✔ |
| `efcfg_importacao_nfe_saidas_parcelas_totais` | totais | efcfg_importacao_nfe_saidas_parcelas | empresa | ✔ |
| `efcfg_importacao_nfe_servicos_parcelas_consultar` | consultar | efcfg_importacao_nfe_servicos_parcelas | empresa | ✔ |
| `efcfg_importacao_nfe_servicos_parcelas_obter` | obter | efcfg_importacao_nfe_servicos_parcelas | empresa, tipo_de_nota_1_entradas_2_saidas_3_servi | ✔ |
| `efcfg_importacao_nfe_servicos_parcelas_totais` | totais | efcfg_importacao_nfe_servicos_parcelas | empresa | ✔ |
