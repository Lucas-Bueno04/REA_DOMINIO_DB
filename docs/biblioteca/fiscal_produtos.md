# Módulo `fiscal_produtos`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `efprodutos_alteracao_consultar` | consultar | efprodutos_alteracao | empresa | ✔ |
| `efprodutos_alteracao_obter` | obter | efprodutos_alteracao | empresa, produto, data_da_alteracao, campo_alterado | ✔ |
| `efprodutos_dam_am_consultar` | consultar | efprodutos_dam_am | — | ✔ |
| `efprodutos_dam_am_obter` | obter | efprodutos_dam_am | codigo_do_produto | ✔ |
| `efprodutos_fator_conversao_consultar` | consultar | efprodutos_fator_conversao | empresa | ✔ |
| `efprodutos_fator_conversao_obter` | obter | efprodutos_fator_conversao | empresa, produto, codigo | ✔ |
| `efprodutos_importacao_cfops_consultar` | consultar | efprodutos_importacao_cfops | empresa | ✔ |
| `efprodutos_importacao_cfops_obter` | obter | efprodutos_importacao_cfops | empresa, produto, sequencial_do_cfop_de_entrada | ✔ |
| `efprodutos_importacao_cfops_cfop_saida_consultar` | consultar | efprodutos_importacao_cfops_cfop_saida | empresa | ✔ |
| `efprodutos_importacao_cfops_cfop_saida_obter` | obter | efprodutos_importacao_cfops_cfop_saida | empresa, produto, sequencial_do_cfop_de_entrada, sequencial_do_cfop_de_saida | ✔ |
| `efprodutos_importacao_entradas_consultar` | consultar | efprodutos_importacao_entradas | empresa | ✔ |
| `efprodutos_importacao_entradas_obter` | obter | efprodutos_importacao_entradas | empresa, produto, sequencial | ✔ |
| `efprodutos_importacao_entradas_produtos_consultar` | consultar | efprodutos_importacao_entradas_produtos | empresa | ✔ |
| `efprodutos_importacao_entradas_produtos_obter` | obter | efprodutos_importacao_entradas_produtos | empresa, produto, sequencial, produto_importacao | ✔ |
| `efprodutos_importacao_saidas_consultar` | consultar | efprodutos_importacao_saidas | empresa | ✔ |
| `efprodutos_importacao_saidas_obter` | obter | efprodutos_importacao_saidas | empresa, produto, produto_importacao | ✔ |
| `efprodutos_inss_folha_consultar` | consultar | efprodutos_inss_folha | empresa | ✔ |
| `efprodutos_inss_folha_obter` | obter | efprodutos_inss_folha | empresa, codigo_do_produto, codigo_da_atividade | ✔ |
| `efprodutos_mssefaz_consultar` | consultar | efprodutos_mssefaz | — | ✔ |
| `efprodutos_mssefaz_obter` | obter | efprodutos_mssefaz | codigo | ✔ |
| `efprodutos_pasefa_consultar` | consultar | efprodutos_pasefa | — | ✔ |
| `efprodutos_pasefa_obter` | obter | efprodutos_pasefa | codigo | ✔ |
| `efprodutos_saldos_consultar` | consultar | efprodutos_saldos | empresa | ✔ |
| `efprodutos_saldos_obter` | obter | efprodutos_saldos | empresa, produto, data_do_saldo | ✔ |
| `efprodutos_saldos_totais` | totais | efprodutos_saldos | empresa | ✔ |
| `efprodutos_valor_unitario_consultar` | consultar | efprodutos_valor_unitario | empresa | ✔ |
| `efprodutos_valor_unitario_obter` | obter | efprodutos_valor_unitario | empresa, codigo_do_produto, sequencial | ✔ |
| `efprodutos_valor_unitario_totais` | totais | efprodutos_valor_unitario | empresa | ✔ |
