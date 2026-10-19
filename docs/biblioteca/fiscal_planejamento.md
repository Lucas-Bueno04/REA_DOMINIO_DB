# Módulo `fiscal_planejamento`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `efplanejamento_tributario_consultar` | consultar | efplanejamento_tributario | empresa | ✔ |
| `efplanejamento_tributario_obter` | obter | efplanejamento_tributario | empresa, regime_de_planejamento_p_presumido_r_rea | ✔ |
| `efplanejamento_tributario_impostos_consultar` | consultar | efplanejamento_tributario_impostos | empresa | ✔ |
| `efplanejamento_tributario_impostos_obter` | obter | efplanejamento_tributario_impostos | empresa, regime_de_planejamento_p_presumido_r_rea, periodo_planejamento, imposto | ✔ |
| `efplanejamento_tributario_impostos_totais` | totais | efplanejamento_tributario_impostos | empresa | ✔ |
| `efplanejamento_tributario_impostos_simples_consultar` | consultar | efplanejamento_tributario_impostos_simples | empresa | ✔ |
| `efplanejamento_tributario_impostos_simples_obter` | obter | efplanejamento_tributario_impostos_simples | empresa, regime_de_planejamento_p_presumido_r_rea, periodo_planejamento, imposto, anexo, secao, tabela, tipo_a_ambos_i_interno_e_externo, imposto_reparticao | ✔ |
| `efplanejamento_tributario_impostos_simples_totais` | totais | efplanejamento_tributario_impostos_simples | empresa | ✔ |
| `efplanejamento_tributario_receitas_consultar` | consultar | efplanejamento_tributario_receitas | empresa | ✔ |
| `efplanejamento_tributario_receitas_obter` | obter | efplanejamento_tributario_receitas | empresa, regime_de_planejamento_p_presumido_r_rea, periodo_planejamento, tipo_receita_rbc_rbs_rbi_cc_ci_ed_dvc_dv | ✔ |
| `efplanejamento_tributario_receitas_totais` | totais | efplanejamento_tributario_receitas | empresa | ✔ |
| `efplanejamento_tributario_receitas_uf_consultar` | consultar | efplanejamento_tributario_receitas_uf | empresa | ✔ |
| `efplanejamento_tributario_receitas_uf_obter` | obter | efplanejamento_tributario_receitas_uf | empresa, regime_de_planejamento_p_presumido_r_rea, periodo_planejamento, tipo_receita_rbc_rbs_rbi_cc_ci_ed_dvc_dv, estado_origem, estado_destino | ✔ |
| `efplanejamento_tributario_receitas_uf_totais` | totais | efplanejamento_tributario_receitas_uf | empresa | ✔ |
| `efplanejamento_tributario_tabela_simples_consultar` | consultar | efplanejamento_tributario_tabela_simples | — | ✔ |
| `efplanejamento_tributario_tabela_simples_obter` | obter | efplanejamento_tributario_tabela_simples | anexo, tipo_normal_exportacao, vigencia | ✔ |
| `efplanejamento_tributario_tabela_simples_faixas_consultar` | consultar | efplanejamento_tributario_tabela_simples_faixas | — | ✔ |
| `efplanejamento_tributario_tabela_simples_faixas_obter` | obter | efplanejamento_tributario_tabela_simples_faixas | anexo, tipo_normal_exportacao, vigencia, faixa | ✔ |
| `efplanejamento_tributario_tabela_simples_faixas_totais` | totais | efplanejamento_tributario_tabela_simples_faixas | — | ✔ |
| `efplanejamento_tributario_valor_despesa_consultar` | consultar | efplanejamento_tributario_valor_despesa | empresa | ✔ |
| `efplanejamento_tributario_valor_despesa_obter` | obter | efplanejamento_tributario_valor_despesa | empresa, regime_de_planejamento_p_presumido_r_rea, periodo_planejamento | ✔ |
| `efplanejamento_tributario_valor_despesa_totais` | totais | efplanejamento_tributario_valor_despesa | empresa | ✔ |
| `efplanejamento_tributario_valor_folha_consultar` | consultar | efplanejamento_tributario_valor_folha | empresa | ✔ |
| `efplanejamento_tributario_valor_folha_obter` | obter | efplanejamento_tributario_valor_folha | empresa, regime_de_planejamento_p_presumido_r_rea, periodo_planejamento | ✔ |
| `efplanejamento_tributario_valor_folha_totais` | totais | efplanejamento_tributario_valor_folha | empresa | ✔ |
