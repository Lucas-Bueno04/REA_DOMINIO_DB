# Módulo `fiscal_movimento`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `efmovimento_ajuste_estadual_ce_consultar` | consultar | efmovimento_ajuste_estadual_ce | empresa | ✔ |
| `efmovimento_ajuste_estadual_ce_obter` | obter | efmovimento_ajuste_estadual_ce | empresa, sequencial_do_movimento_do_ajuste | ✔ |
| `efmovimento_ajuste_estadual_ce_totais` | totais | efmovimento_ajuste_estadual_ce | empresa | ✔ |
| `efmovimento_ajuste_estadual_ce_complementar_consultar` | consultar | efmovimento_ajuste_estadual_ce_complementar | empresa | ✔ |
| `efmovimento_ajuste_estadual_ce_complementar_obter` | obter | efmovimento_ajuste_estadual_ce_complementar | empresa, sequencial_do_movimento_do_ajuste | ✔ |
| `efmovimento_ajuste_estadual_ce_lancto_consultar` | consultar | efmovimento_ajuste_estadual_ce_lancto | empresa | ✔ |
| `efmovimento_ajuste_estadual_ce_lancto_obter` | obter | efmovimento_ajuste_estadual_ce_lancto | empresa, empresa_do_movimento, sequencial_do_movimento_do_ajuste, numero_do_lancamento | ✔ |
| `efmovimento_ajuste_estadual_mg_consultar` | consultar | efmovimento_ajuste_estadual_mg | empresa | ✔ |
| `efmovimento_ajuste_estadual_mg_obter` | obter | efmovimento_ajuste_estadual_mg | empresa, sequencial_do_movimento_do_ajuste | ✔ |
| `efmovimento_ajuste_estadual_mg_totais` | totais | efmovimento_ajuste_estadual_mg | empresa | ✔ |
| `efmovimento_ajuste_estadual_mg_detalhamento_09_consultar` | consultar | efmovimento_ajuste_estadual_mg_detalhamento_09 | empresa | ✔ |
| `efmovimento_ajuste_estadual_mg_detalhamento_09_obter` | obter | efmovimento_ajuste_estadual_mg_detalhamento_09 | empresa, sequencial_do_movimento_do_ajuste | ✔ |
| `efmovimento_ajuste_estadual_mg_detalhamento_11_consultar` | consultar | efmovimento_ajuste_estadual_mg_detalhamento_11 | empresa | ✔ |
| `efmovimento_ajuste_estadual_mg_detalhamento_11_obter` | obter | efmovimento_ajuste_estadual_mg_detalhamento_11 | empresa, sequencial_do_movimento_do_ajuste | ✔ |
| `efmovimento_ajuste_estadual_mg_lancto_consultar` | consultar | efmovimento_ajuste_estadual_mg_lancto | empresa | ✔ |
| `efmovimento_ajuste_estadual_mg_lancto_obter` | obter | efmovimento_ajuste_estadual_mg_lancto | empresa, empresa_do_movimento, sequencial_do_movimento_do_ajuste, numero_do_lancamento | ✔ |
| `efmovimento_ajuste_estadual_pe_consultar` | consultar | efmovimento_ajuste_estadual_pe | empresa | ✔ |
| `efmovimento_ajuste_estadual_pe_obter` | obter | efmovimento_ajuste_estadual_pe | empresa, sequencial_do_movimento_do_ajuste | ✔ |
| `efmovimento_ajuste_estadual_pe_totais` | totais | efmovimento_ajuste_estadual_pe | empresa | ✔ |
| `efmovimento_ajuste_estadual_pr_consultar` | consultar | efmovimento_ajuste_estadual_pr | empresa | ✔ |
| `efmovimento_ajuste_estadual_pr_obter` | obter | efmovimento_ajuste_estadual_pr | empresa, sequencial_do_movimento_do_ajuste | ✔ |
| `efmovimento_ajuste_estadual_pr_totais` | totais | efmovimento_ajuste_estadual_pr | empresa | ✔ |
| `efmovimento_ajuste_estadual_rj_consultar` | consultar | efmovimento_ajuste_estadual_rj | empresa | ✔ |
| `efmovimento_ajuste_estadual_rj_obter` | obter | efmovimento_ajuste_estadual_rj | empresa, sequencial_do_movimento_do_ajuste | ✔ |
| `efmovimento_ajuste_estadual_rj_totais` | totais | efmovimento_ajuste_estadual_rj | empresa | ✔ |
| `efmovimento_ajuste_estadual_rj_detalhamento_02_consultar` | consultar | efmovimento_ajuste_estadual_rj_detalhamento_02 | empresa | ✔ |
| `efmovimento_ajuste_estadual_rj_detalhamento_02_obter` | obter | efmovimento_ajuste_estadual_rj_detalhamento_02 | empresa, sequencial_do_movimento_do_ajuste | ✔ |
| `efmovimento_ajuste_estadual_sp_consultar` | consultar | efmovimento_ajuste_estadual_sp | empresa | ✔ |
| `efmovimento_ajuste_estadual_sp_obter` | obter | efmovimento_ajuste_estadual_sp | empresa, sequencial_do_movimento_do_ajuste | ✔ |
| `efmovimento_ajuste_estadual_sp_totais` | totais | efmovimento_ajuste_estadual_sp | empresa | ✔ |
| `efmovimento_ajuste_estadual_sp_detalhamento_02_do_bccf_consultar` | consultar | efmovimento_ajuste_estadual_sp_detalhamento_02_documentos | empresa | ✔ |
| `efmovimento_ajuste_estadual_sp_detalhamento_02_documentos_obter` | obter | efmovimento_ajuste_estadual_sp_detalhamento_02_documentos | empresa, sequencial_do_movimento_do_ajuste, sequencial_do_detalhamento_do_movimento | ✔ |
| `efmovimento_ajuste_estadual_sp_detalhamento_02_documentos_totais` | totais | efmovimento_ajuste_estadual_sp_detalhamento_02_documentos | empresa | ✔ |
| `efmovimento_ajuste_estadual_sp_detalhamento_02_in_2f28_consultar` | consultar | efmovimento_ajuste_estadual_sp_detalhamento_02_informacoes_adicionais | empresa | ✔ |
| `efmovimento_ajuste_estadual_sp_detalhamento_02_inform_2f28_obter` | obter | efmovimento_ajuste_estadual_sp_detalhamento_02_informacoes_adicionais | empresa, sequencial_do_movimento_do_ajuste | ✔ |
| `efmovimento_ajuste_estadual_sp_detalhamento_02_oc_8d7d_consultar` | consultar | efmovimento_ajuste_estadual_sp_detalhamento_02_ocorrencia | empresa | ✔ |
| `efmovimento_ajuste_estadual_sp_detalhamento_02_ocorrencia_obter` | obter | efmovimento_ajuste_estadual_sp_detalhamento_02_ocorrencia | empresa, sequencial_do_movimento_do_ajuste | ✔ |
| `efmovimento_ajuste_estadual_sp_lancto_consultar` | consultar | efmovimento_ajuste_estadual_sp_lancto | empresa | ✔ |
| `efmovimento_ajuste_estadual_sp_lancto_obter` | obter | efmovimento_ajuste_estadual_sp_lancto | empresa, empresa_do_movimento, sequencial_do_movimento_do_ajuste, numero_do_lancamento | ✔ |
| `efmovimento_ajuste_federal_consultar` | consultar | efmovimento_ajuste_federal | empresa | ✔ |
| `efmovimento_ajuste_federal_obter` | obter | efmovimento_ajuste_federal | empresa, sequencial_do_movimento_do_ajuste | ✔ |
| `efmovimento_ajuste_federal_totais` | totais | efmovimento_ajuste_federal | empresa | ✔ |
| `efmovimento_ajuste_federal_detalhamento_03_consultar` | consultar | efmovimento_ajuste_federal_detalhamento_03 | empresa | ✔ |
| `efmovimento_ajuste_federal_detalhamento_03_obter` | obter | efmovimento_ajuste_federal_detalhamento_03 | empresa, sequencial_do_movimento_do_ajuste | ✔ |
