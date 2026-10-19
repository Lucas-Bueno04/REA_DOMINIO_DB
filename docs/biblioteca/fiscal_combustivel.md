# Módulo `fiscal_combustivel`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `efcombustivel_bico_consultar` | consultar | efcombustivel_bico | empresa | ✔ |
| `efcombustivel_bico_obter` | obter | efcombustivel_bico | empresa, sequencial | ✔ |
| `efcombustivel_bico_vigencia_consultar` | consultar | efcombustivel_bico_vigencia | empresa | ✔ |
| `efcombustivel_bico_vigencia_obter` | obter | efcombustivel_bico_vigencia | empresa, sequencial, vigencia | ✔ |
| `efcombustivel_tabela_anp_consultar` | consultar | efcombustivel_tabela_anp | — | ✔ |
| `efcombustivel_tabela_anp_obter` | obter | efcombustivel_tabela_anp | codigo | ✔ |
| `efcombustivel_tabela_df_consultar` | consultar | efcombustivel_tabela_df | — | ✔ |
| `efcombustivel_tabela_df_obter` | obter | efcombustivel_tabela_df | codigo | ✔ |
| `efcombustivel_tanque_consultar` | consultar | efcombustivel_tanque | empresa | ✔ |
| `efcombustivel_tanque_obter` | obter | efcombustivel_tanque | empresa, sequencial | ✔ |
| `efcombustivel_tanque_vigencia_consultar` | consultar | efcombustivel_tanque_vigencia | empresa | ✔ |
| `efcombustivel_tanque_vigencia_obter` | obter | efcombustivel_tanque_vigencia | empresa, sequencial, sequencial_da_vigencia | ✔ |
| `efcombustivel_tanque_vigencia_totais` | totais | efcombustivel_tanque_vigencia | empresa | ✔ |
| `efcombustivel_tanque_vigencia_codigo_arquivo_consultar` | consultar | efcombustivel_tanque_vigencia_codigo_arquivo | empresa | ✔ |
| `efcombustivel_tanque_vigencia_codigo_arquivo_obter` | obter | efcombustivel_tanque_vigencia_codigo_arquivo | empresa, sequencial_tanque, sequencial_da_vigencia, sequencial_codigo_do_tanque_no_arquivo | ✔ |
