# Módulo `contabil_irpj`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `lrirpj_estimado_deducao_consultar` | consultar | lrirpj_estimado_deducao | empresa | ✔ |
| `lrirpj_estimado_deducao_obter` | obter | lrirpj_estimado_deducao | empresa, codigo | ✔ |
| `lrirpj_estimado_deducao_totais` | totais | lrirpj_estimado_deducao | empresa | ✔ |
| `lrirpj_incentivo_fiscal_consultar` | consultar | lrirpj_incentivo_fiscal | empresa | ✔ |
| `lrirpj_incentivo_fiscal_obter` | obter | lrirpj_incentivo_fiscal | empresa, codigo | ✔ |
| `lrirpj_incentivo_fiscal_totais` | totais | lrirpj_incentivo_fiscal | empresa | ✔ |
| `lrirpj_real_adicao_consultar` | consultar | lrirpj_real_adicao | empresa | ✔ |
| `lrirpj_real_adicao_obter` | obter | lrirpj_real_adicao | empresa, codigo | ✔ |
| `lrirpj_real_adicao_item_consultar` | consultar | lrirpj_real_adicao_item | empresa | ✔ |
| `lrirpj_real_adicao_item_obter` | obter | lrirpj_real_adicao_item | empresa, codigo_do_lancamento_de_adicao_da_irpj, sequencial | ✔ |
| `lrirpj_real_adicao_item_totais` | totais | lrirpj_real_adicao_item | empresa | ✔ |
| `lrirpj_real_adicao_item_ajuste_anual_consultar` | consultar | lrirpj_real_adicao_item_ajuste_anual | empresa | ✔ |
| `lrirpj_real_adicao_item_ajuste_anual_obter` | obter | lrirpj_real_adicao_item_ajuste_anual | empresa, codigo_do_lancamento_de_adicao_da_irpj, sequencial | ✔ |
| `lrirpj_real_adicao_item_ajuste_anual_totais` | totais | lrirpj_real_adicao_item_ajuste_anual | empresa | ✔ |
| `lrirpj_real_adicao_lancamento_consultar` | consultar | lrirpj_real_adicao_lancamento | empresa | ✔ |
| `lrirpj_real_adicao_lancamento_obter` | obter | lrirpj_real_adicao_lancamento | empresa, codigo_do_lancamento_de_adicao_da_irpj, sequencial_da_adicao, sequencial | ✔ |
| `lrirpj_real_adicao_lancamento_totais` | totais | lrirpj_real_adicao_lancamento | empresa | ✔ |
| `lrirpj_real_deducao_consultar` | consultar | lrirpj_real_deducao | empresa | ✔ |
| `lrirpj_real_deducao_obter` | obter | lrirpj_real_deducao | empresa, codigo | ✔ |
| `lrirpj_real_deducao_totais` | totais | lrirpj_real_deducao | empresa | ✔ |
| `lrirpj_real_exclusao_consultar` | consultar | lrirpj_real_exclusao | empresa | ✔ |
| `lrirpj_real_exclusao_obter` | obter | lrirpj_real_exclusao | empresa, codigo | ✔ |
| `lrirpj_real_exclusao_item_consultar` | consultar | lrirpj_real_exclusao_item | empresa | ✔ |
| `lrirpj_real_exclusao_item_obter` | obter | lrirpj_real_exclusao_item | empresa, codigo_do_lancamento_de_exclusoes_da_irp, sequencial | ✔ |
| `lrirpj_real_exclusao_item_totais` | totais | lrirpj_real_exclusao_item | empresa | ✔ |
| `lrirpj_real_exclusao_lancamento_consultar` | consultar | lrirpj_real_exclusao_lancamento | empresa | ✔ |
| `lrirpj_real_exclusao_lancamento_obter` | obter | lrirpj_real_exclusao_lancamento | empresa, codigo_do_lancamento_de_exclusao_da_irpj, sequencial_da_exclusao, sequencial | ✔ |
| `lrirpj_real_exclusao_lancamento_totais` | totais | lrirpj_real_exclusao_lancamento | empresa | ✔ |
| `lrirpj_real_parte_b_consultar` | consultar | lrirpj_real_parte_b | empresa | ✔ |
| `lrirpj_real_parte_b_obter` | obter | lrirpj_real_parte_b | empresa, codigo | ✔ |
| `lrirpj_real_parte_b_totais` | totais | lrirpj_real_parte_b | empresa | ✔ |
