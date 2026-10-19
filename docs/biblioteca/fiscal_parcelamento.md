# Módulo `fiscal_parcelamento`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `efparcelamento_imposto_sn_consultar` | consultar | efparcelamento_imposto_sn | empresa | ✔ |
| `efparcelamento_imposto_sn_obter` | obter | efparcelamento_imposto_sn | empresa, sequencial_do_parcelamento_simples_nacin | ✔ |
| `efparcelamento_imposto_sn_historico_consultar` | consultar | efparcelamento_imposto_sn_historico | empresa | ✔ |
| `efparcelamento_imposto_sn_historico_obter` | obter | efparcelamento_imposto_sn_historico | empresa, sequencial_do_parcelamento_simples_nacio | ✔ |
| `efparcelamento_imposto_sn_lancto_consultar` | consultar | efparcelamento_imposto_sn_lancto | empresa | ✔ |
| `efparcelamento_imposto_sn_lancto_obter` | obter | efparcelamento_imposto_sn_lancto | empresa, numero_do_lancamento, empresa_do_parcelamento, sequencial_do_parcelamento_simples_nacin | ✔ |
| `efparcelamento_imposto_sn_parcela_dados_consultar` | consultar | efparcelamento_imposto_sn_parcela_dados | empresa | ✔ |
| `efparcelamento_imposto_sn_parcela_dados_obter` | obter | efparcelamento_imposto_sn_parcela_dados | empresa, sequencial_do_parcelamento_simples_nacin, tipo_parcela_1_parcela_2_parcela_da_entr | ✔ |
| `efparcelamento_imposto_sn_parcela_dados_totais` | totais | efparcelamento_imposto_sn_parcela_dados | empresa | ✔ |
| `efparcelamento_imposto_sn_parcela_parcela_consultar` | consultar | efparcelamento_imposto_sn_parcela_parcela | empresa | ✔ |
| `efparcelamento_imposto_sn_parcela_parcela_obter` | obter | efparcelamento_imposto_sn_parcela_parcela | empresa, sequencial_do_parcelamento_simples_nacin, sequencial_da_parcela_do_parcelamento_si, tipo_parcela_1_parcela_2_parcela_da_entr | ✔ |
| `efparcelamento_imposto_sn_parcela_parcela_totais` | totais | efparcelamento_imposto_sn_parcela_parcela | empresa | ✔ |
| `efparcelamento_imposto_sn_parcela_parcelamento_consultar` | consultar | efparcelamento_imposto_sn_parcela_parcelamento | empresa | ✔ |
| `efparcelamento_imposto_sn_parcela_parcelamento_obter` | obter | efparcelamento_imposto_sn_parcela_parcelamento | empresa, sequencial_do_parcelamento_simples_nacin, sequencial_da_parcela_do_parcelamento_si, tipo_parcela_1_parcela_2_parcela_da_entr | ✔ |
| `efparcelamento_imposto_sn_parcela_parcelamento_totais` | totais | efparcelamento_imposto_sn_parcela_parcelamento | empresa | ✔ |
| `efparcelamento_imposto_sn_selecao_consultar` | consultar | efparcelamento_imposto_sn_selecao | empresa | ✔ |
| `efparcelamento_imposto_sn_selecao_obter` | obter | efparcelamento_imposto_sn_selecao | empresa, sequencial_do_parcelamento_simples_nacin, sequencial_da_selecao_do_parcelamento_si | ✔ |
| `efparcelamento_imposto_sn_selecao_totais` | totais | efparcelamento_imposto_sn_selecao | empresa | ✔ |
