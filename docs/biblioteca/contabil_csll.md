# Módulo `contabil_csll`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `lrcsll_estimado_deducao_consultar` | consultar | lrcsll_estimado_deducao | empresa | ✔ |
| `lrcsll_estimado_deducao_obter` | obter | lrcsll_estimado_deducao | empresa, codigo | ✔ |
| `lrcsll_estimado_deducao_totais` | totais | lrcsll_estimado_deducao | empresa | ✔ |
| `lrcsll_estimado_ganho_consultar` | consultar | lrcsll_estimado_ganho | empresa | ✔ |
| `lrcsll_estimado_ganho_obter` | obter | lrcsll_estimado_ganho | empresa, codigo | ✔ |
| `lrcsll_estimado_ganho_item_consultar` | consultar | lrcsll_estimado_ganho_item | empresa | ✔ |
| `lrcsll_estimado_ganho_item_obter` | obter | lrcsll_estimado_ganho_item | empresa, codigo_do_lancamento_de_ganho_da_csll, sequencial | ✔ |
| `lrcsll_estimado_ganho_item_totais` | totais | lrcsll_estimado_ganho_item | empresa | ✔ |
| `lrcsll_real_adicao_consultar` | consultar | lrcsll_real_adicao | empresa | ✔ |
| `lrcsll_real_adicao_obter` | obter | lrcsll_real_adicao | empresa, codigo | ✔ |
| `lrcsll_real_adicao_item_consultar` | consultar | lrcsll_real_adicao_item | empresa | ✔ |
| `lrcsll_real_adicao_item_obter` | obter | lrcsll_real_adicao_item | empresa, codigo_do_lancamento_de_adicao_da_csll, sequencial | ✔ |
| `lrcsll_real_adicao_item_totais` | totais | lrcsll_real_adicao_item | empresa | ✔ |
| `lrcsll_real_adicao_lancamento_consultar` | consultar | lrcsll_real_adicao_lancamento | empresa | ✔ |
| `lrcsll_real_adicao_lancamento_obter` | obter | lrcsll_real_adicao_lancamento | empresa, codigo_do_lancamento_de_adicao_da_csll, sequencial_da_adicao, sequencial | ✔ |
| `lrcsll_real_adicao_lancamento_totais` | totais | lrcsll_real_adicao_lancamento | empresa | ✔ |
| `lrcsll_real_base_negativa_consultar` | consultar | lrcsll_real_base_negativa | empresa | ✔ |
| `lrcsll_real_base_negativa_obter` | obter | lrcsll_real_base_negativa | empresa, codigo | ✔ |
| `lrcsll_real_base_negativa_totais` | totais | lrcsll_real_base_negativa | empresa | ✔ |
| `lrcsll_real_deducao_consultar` | consultar | lrcsll_real_deducao | empresa | ✔ |
| `lrcsll_real_deducao_obter` | obter | lrcsll_real_deducao | empresa, codigo | ✔ |
| `lrcsll_real_deducao_totais` | totais | lrcsll_real_deducao | empresa | ✔ |
| `lrcsll_real_exclusao_consultar` | consultar | lrcsll_real_exclusao | empresa | ✔ |
| `lrcsll_real_exclusao_obter` | obter | lrcsll_real_exclusao | empresa, codigo | ✔ |
| `lrcsll_real_exclusao_item_consultar` | consultar | lrcsll_real_exclusao_item | empresa | ✔ |
| `lrcsll_real_exclusao_item_obter` | obter | lrcsll_real_exclusao_item | empresa, codigo_do_lancamento_de_exclusoes_da_csl, sequencial | ✔ |
| `lrcsll_real_exclusao_item_totais` | totais | lrcsll_real_exclusao_item | empresa | ✔ |
| `lrcsll_real_exclusao_lancamento_consultar` | consultar | lrcsll_real_exclusao_lancamento | empresa | ✔ |
| `lrcsll_real_exclusao_lancamento_obter` | obter | lrcsll_real_exclusao_lancamento | empresa, codigo_do_lancamento_de_exclusao_da_csll, sequencial_da_exclusao, sequencial | ✔ |
| `lrcsll_real_exclusao_lancamento_totais` | totais | lrcsll_real_exclusao_lancamento | empresa | ✔ |
