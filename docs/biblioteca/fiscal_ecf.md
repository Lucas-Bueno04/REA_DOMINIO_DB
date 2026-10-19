# Módulo `fiscal_ecf`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `efecf_configuracao_consultar` | consultar | efecf_configuracao | empresa | ✔ |
| `efecf_configuracao_obter` | obter | efecf_configuracao | empresa, codigo_da_configuracao | ✔ |
| `efecf_configuracao_acumuladores_consultar` | consultar | efecf_configuracao_acumuladores | empresa | ✔ |
| `efecf_configuracao_acumuladores_obter` | obter | efecf_configuracao_acumuladores | empresa, codigo_da_configuracao, sequencial_da_situacao, sequencial | ✔ |
| `efecf_configuracao_situacoes_consultar` | consultar | efecf_configuracao_situacoes | empresa | ✔ |
| `efecf_configuracao_situacoes_obter` | obter | efecf_configuracao_situacoes | empresa, codigo_da_configuracao, sequencial_da_situacao | ✔ |
| `efecf_cupom_fiscal_consultar` | consultar | efecf_cupom_fiscal | empresa | ✔ |
| `efecf_cupom_fiscal_obter` | obter | efecf_cupom_fiscal | empresa, codigo_da_reducao_z, sequencial_do_cupom_fiscal | ✔ |
| `efecf_cupom_fiscal_totais` | totais | efecf_cupom_fiscal | empresa | ✔ |
| `efecf_cupom_fiscal_estoque_consultar` | consultar | efecf_cupom_fiscal_estoque | empresa | ✔ |
| `efecf_cupom_fiscal_estoque_obter` | obter | efecf_cupom_fiscal_estoque | empresa, codigo_da_reducao_z, sequencial_do_cupom_fiscal, sequencial_do_estoque | ✔ |
| `efecf_cupom_fiscal_estoque_totais` | totais | efecf_cupom_fiscal_estoque | empresa | ✔ |
| `efecf_cupom_fiscal_pis_cofins_consultar` | consultar | efecf_cupom_fiscal_pis_cofins | empresa | ✔ |
| `efecf_cupom_fiscal_pis_cofins_obter` | obter | efecf_cupom_fiscal_pis_cofins | empresa, codigo_da_reducao_z, sequencial_do_cupom_fiscal, sequencial | ✔ |
| `efecf_cupom_fiscal_pis_cofins_totais` | totais | efecf_cupom_fiscal_pis_cofins | empresa | ✔ |
| `efecf_reducao_z_consultar` | consultar | efecf_reducao_z | empresa | ✔ |
| `efecf_reducao_z_obter` | obter | efecf_reducao_z | empresa, codigo_da_reducao_z | ✔ |
| `efecf_reducao_z_totais` | totais | efecf_reducao_z | empresa | ✔ |
| `efecf_reducao_z_estoque_consultar` | consultar | efecf_reducao_z_estoque | empresa | ✔ |
| `efecf_reducao_z_estoque_obter` | obter | efecf_reducao_z_estoque | empresa, codigo_da_reducao_z, sequencial_do_estoque | ✔ |
| `efecf_reducao_z_estoque_totais` | totais | efecf_reducao_z_estoque | empresa | ✔ |
| `efecf_reducao_z_estoque_apuracao_estoque_consultar` | consultar | efecf_reducao_z_estoque_apuracao_estoque | empresa | ✔ |
| `efecf_reducao_z_estoque_apuracao_estoque_obter` | obter | efecf_reducao_z_estoque_apuracao_estoque | empresa, sequencial_da_reducao_z, sequencial_do_estoque | ✔ |
| `efecf_reducao_z_estoque_apuracao_estoque_totais` | totais | efecf_reducao_z_estoque_apuracao_estoque | empresa | ✔ |
| `efecf_reducao_z_impostos_consultar` | consultar | efecf_reducao_z_impostos | empresa | ✔ |
| `efecf_reducao_z_impostos_obter` | obter | efecf_reducao_z_impostos | empresa, codigo_da_reducao_z, sequencial_do_imposto | ✔ |
| `efecf_reducao_z_impostos_totais` | totais | efecf_reducao_z_impostos | empresa | ✔ |
| `efecf_reducao_z_lancto_consultar` | consultar | efecf_reducao_z_lancto | empresa | ✔ |
| `efecf_reducao_z_lancto_obter` | obter | efecf_reducao_z_lancto | empresa, numero_do_lancamento, empresa_da_reducao, codigo_da_reducao_z | ✔ |
| `efecf_reducao_z_pis_cofins_consultar` | consultar | efecf_reducao_z_pis_cofins | empresa | ✔ |
| `efecf_reducao_z_pis_cofins_obter` | obter | efecf_reducao_z_pis_cofins | empresa, codigo_da_reducao_z, sequencial | ✔ |
| `efecf_reducao_z_pis_cofins_totais` | totais | efecf_reducao_z_pis_cofins | empresa | ✔ |
| `efecf_reducao_z_situacao_tributaria_consultar` | consultar | efecf_reducao_z_situacao_tributaria | empresa | ✔ |
| `efecf_reducao_z_situacao_tributaria_obter` | obter | efecf_reducao_z_situacao_tributaria | empresa, codigo_da_reducao_z, sequencial_da_situacao_tributaria | ✔ |
| `efecf_reducao_z_situacao_tributaria_totais` | totais | efecf_reducao_z_situacao_tributaria | empresa | ✔ |
| `efecf_reducao_z_situacao_tributaria_detalhamento_consultar` | consultar | efecf_reducao_z_situacao_tributaria_detalhamento | empresa | ✔ |
| `efecf_reducao_z_situacao_tributaria_detalhamento_obter` | obter | efecf_reducao_z_situacao_tributaria_detalhamento | empresa, codigo_da_reducao_z, sequencial_da_situacao_tributaria, sequencial_do_detalhamento | ✔ |
| `efecf_reducao_z_situacao_tributaria_detalhamento_totais` | totais | efecf_reducao_z_situacao_tributaria_detalhamento | empresa | ✔ |
