# Módulo `contabil_calculo`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `lrcalculo_csll_estimado_consultar` | consultar | lrcalculo_csll_estimado | empresa | ✔ |
| `lrcalculo_csll_estimado_obter` | obter | lrcalculo_csll_estimado | empresa, codigo_do_calculo | ✔ |
| `lrcalculo_csll_estimado_totais` | totais | lrcalculo_csll_estimado | empresa | ✔ |
| `lrcalculo_csll_estimado_deducao_consultar` | consultar | lrcalculo_csll_estimado_deducao | empresa | ✔ |
| `lrcalculo_csll_estimado_deducao_obter` | obter | lrcalculo_csll_estimado_deducao | empresa, codigo_do_calculo, ajuste_anual, deducao | ✔ |
| `lrcalculo_csll_estimado_deducao_totais` | totais | lrcalculo_csll_estimado_deducao | empresa | ✔ |
| `lrcalculo_csll_estimado_operacao_receita_consultar` | consultar | lrcalculo_csll_estimado_operacao_receita | empresa | ✔ |
| `lrcalculo_csll_estimado_operacao_receita_obter` | obter | lrcalculo_csll_estimado_operacao_receita | empresa, codigo_do_calculo, operacao_de_receita_vendas_ou_servicos | ✔ |
| `lrcalculo_csll_estimado_operacao_receita_totais` | totais | lrcalculo_csll_estimado_operacao_receita | empresa | ✔ |
| `lrcalculo_csll_real_adicao_consultar` | consultar | lrcalculo_csll_real_adicao | empresa | ✔ |
| `lrcalculo_csll_real_adicao_obter` | obter | lrcalculo_csll_real_adicao | empresa, codigo_do_calculo, adicao, ajuste_anual | ✔ |
| `lrcalculo_csll_real_adicao_totais` | totais | lrcalculo_csll_real_adicao | empresa | ✔ |
| `lrcalculo_csll_real_deducao_consultar` | consultar | lrcalculo_csll_real_deducao | empresa | ✔ |
| `lrcalculo_csll_real_deducao_obter` | obter | lrcalculo_csll_real_deducao | empresa, codigo_do_calculo, ajuste_anual, deducao | ✔ |
| `lrcalculo_csll_real_deducao_totais` | totais | lrcalculo_csll_real_deducao | empresa | ✔ |
| `lrcalculo_csll_real_exclusao_consultar` | consultar | lrcalculo_csll_real_exclusao | empresa | ✔ |
| `lrcalculo_csll_real_exclusao_obter` | obter | lrcalculo_csll_real_exclusao | empresa, codigo_do_calculo, exclusao, ajuste_anual | ✔ |
| `lrcalculo_csll_real_exclusao_totais` | totais | lrcalculo_csll_real_exclusao | empresa | ✔ |
| `lrcalculo_irpj_estimado_consultar` | consultar | lrcalculo_irpj_estimado | empresa | ✔ |
| `lrcalculo_irpj_estimado_obter` | obter | lrcalculo_irpj_estimado | empresa, codigo_do_calculo | ✔ |
| `lrcalculo_irpj_estimado_totais` | totais | lrcalculo_irpj_estimado | empresa | ✔ |
| `lrcalculo_irpj_estimado_deducao_consultar` | consultar | lrcalculo_irpj_estimado_deducao | empresa | ✔ |
| `lrcalculo_irpj_estimado_deducao_obter` | obter | lrcalculo_irpj_estimado_deducao | empresa, codigo_do_calculo, ajuste_anual, deducao | ✔ |
| `lrcalculo_irpj_estimado_deducao_totais` | totais | lrcalculo_irpj_estimado_deducao | empresa | ✔ |
| `lrcalculo_irpj_estimado_operacao_receita_consultar` | consultar | lrcalculo_irpj_estimado_operacao_receita | empresa | ✔ |
| `lrcalculo_irpj_estimado_operacao_receita_obter` | obter | lrcalculo_irpj_estimado_operacao_receita | empresa, codigo_do_calculo, operacao_de_receita_vendas_servicos_ou_n | ✔ |
| `lrcalculo_irpj_estimado_operacao_receita_totais` | totais | lrcalculo_irpj_estimado_operacao_receita | empresa | ✔ |
| `lrcalculo_irpj_incentivo_fiscal_consultar` | consultar | lrcalculo_irpj_incentivo_fiscal | empresa | ✔ |
| `lrcalculo_irpj_incentivo_fiscal_obter` | obter | lrcalculo_irpj_incentivo_fiscal | empresa, codigo_do_calculo, codigo_do_movimento_do_incentivo_fiscal, ajuste_anual | ✔ |
| `lrcalculo_irpj_incentivo_fiscal_totais` | totais | lrcalculo_irpj_incentivo_fiscal | empresa | ✔ |
| `lrcalculo_irpj_real_adicao_consultar` | consultar | lrcalculo_irpj_real_adicao | empresa | ✔ |
| `lrcalculo_irpj_real_adicao_obter` | obter | lrcalculo_irpj_real_adicao | empresa, codigo_do_calculo, adicao, ajuste_anual | ✔ |
| `lrcalculo_irpj_real_adicao_totais` | totais | lrcalculo_irpj_real_adicao | empresa | ✔ |
| `lrcalculo_irpj_real_deducao_consultar` | consultar | lrcalculo_irpj_real_deducao | empresa | ✔ |
| `lrcalculo_irpj_real_deducao_obter` | obter | lrcalculo_irpj_real_deducao | empresa, codigo_do_calculo, ajuste_anual, deducao | ✔ |
| `lrcalculo_irpj_real_deducao_totais` | totais | lrcalculo_irpj_real_deducao | empresa | ✔ |
| `lrcalculo_irpj_real_exclusao_consultar` | consultar | lrcalculo_irpj_real_exclusao | empresa | ✔ |
| `lrcalculo_irpj_real_exclusao_obter` | obter | lrcalculo_irpj_real_exclusao | empresa, codigo_do_calculo, exclusao, ajuste_anual | ✔ |
| `lrcalculo_irpj_real_exclusao_totais` | totais | lrcalculo_irpj_real_exclusao | empresa | ✔ |
| `pmcalculo_credito_icms_consultar` | consultar | pmcalculo_credito_icms | empresa | ✔ |
| `pmcalculo_credito_icms_obter` | obter | pmcalculo_credito_icms | empresa, codigo, periodicidade_0_mensal_1_primeira_quinze | ✔ |
| `pmcalculo_credito_icms_totais` | totais | pmcalculo_credito_icms | empresa | ✔ |
| `pmcalculo_credito_icms_lancto_consultar` | consultar | pmcalculo_credito_icms_lancto | empresa | ✔ |
| `pmcalculo_credito_icms_lancto_obter` | obter | pmcalculo_credito_icms_lancto | empresa, codigo, empresa_do_lancamento_contabil, numero_do_lancamento_contabil | ✔ |
| `pmcalculo_credito_piscofins_consultar` | consultar | pmcalculo_credito_piscofins | empresa | ✔ |
| `pmcalculo_credito_piscofins_obter` | obter | pmcalculo_credito_piscofins | empresa, codigo | ✔ |
| `pmcalculo_credito_piscofins_totais` | totais | pmcalculo_credito_piscofins | empresa | ✔ |
| `pmcalculo_credito_piscofins_lancto_consultar` | consultar | pmcalculo_credito_piscofins_lancto | empresa | ✔ |
| `pmcalculo_credito_piscofins_lancto_obter` | obter | pmcalculo_credito_piscofins_lancto | empresa, codigo, empresa_do_lancamento_contabil, numero_do_lancamento_contabil | ✔ |
| `pmcalculo_depreciacao_fiscal_consultar` | consultar | pmcalculo_depreciacao_fiscal | empresa | ✔ |
| `pmcalculo_depreciacao_fiscal_obter` | obter | pmcalculo_depreciacao_fiscal | empresa, codigo | ✔ |
| `pmcalculo_depreciacao_fiscal_totais` | totais | pmcalculo_depreciacao_fiscal | empresa | ✔ |
| `pmcalculo_depreciacao_lancto_consultar` | consultar | pmcalculo_depreciacao_lancto | empresa | ✔ |
| `pmcalculo_depreciacao_lancto_obter` | obter | pmcalculo_depreciacao_lancto | empresa, codigo, empresa_do_lancamento_contabil, numero_do_lancamento_contabil | ✔ |
| `pmcalculo_depreciacao_societaria_consultar` | consultar | pmcalculo_depreciacao_societaria | empresa | ✔ |
| `pmcalculo_depreciacao_societaria_obter` | obter | pmcalculo_depreciacao_societaria | empresa, codigo | ✔ |
| `pmcalculo_depreciacao_societaria_totais` | totais | pmcalculo_depreciacao_societaria | empresa | ✔ |
