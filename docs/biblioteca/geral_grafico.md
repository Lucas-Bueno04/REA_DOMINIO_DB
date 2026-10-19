# Módulo `geral_grafico`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `gegrafico_configuracao_contas_contabeis_consultar` | consultar | gegrafico_configuracao_contas_contabeis | — | ✔ |
| `gegrafico_configuracao_contas_contabeis_obter` | obter | gegrafico_configuracao_contas_contabeis | codigo, codigo_do_modulo_que_o_grafico_pertence | ✔ |
| `gegrafico_configuracao_contas_contabeis_totais` | totais | gegrafico_configuracao_contas_contabeis | — | ✔ |
| `gegrafico_contas_contabeis_consultar` | consultar | gegrafico_contas_contabeis | — | ✔ |
| `gegrafico_contas_contabeis_obter` | obter | gegrafico_contas_contabeis | codigo_do_grafico, empresa_selecionado, codigo_da_conta_contabil | ✔ |
| `gegrafico_emitir_consultar` | consultar | gegrafico_emitir | — | ✔ |
| `gegrafico_emitir_obter` | obter | gegrafico_emitir | codigo | ✔ |
| `gegrafico_graficos_selecionados_emissao_consultar` | consultar | gegrafico_graficos_selecionados_emissao | — | ✔ |
| `gegrafico_graficos_selecionados_emissao_obter` | obter | gegrafico_graficos_selecionados_emissao | codigo | ✔ |
| `gegrafico_graficos_selecionados_emissao_empresas_consultar` | consultar | gegrafico_graficos_selecionados_emissao_empresas | empresa | ✔ |
| `gegrafico_graficos_selecionados_emissao_empresas_obter` | obter | gegrafico_graficos_selecionados_emissao_empresas | empresa, codigo | ✔ |
| `gegrafico_graficos_selecionados_emissao_usuarios_consultar` | consultar | gegrafico_graficos_selecionados_emissao_usuarios | — | ✔ |
| `gegrafico_graficos_selecionados_emissao_usuarios_obter` | obter | gegrafico_graficos_selecionados_emissao_usuarios | codigo | ✔ |
| `gegrafico_legenda_consultar` | consultar | gegrafico_legenda | — | ✔ |
| `gegrafico_legenda_obter` | obter | gegrafico_legenda | chave_primaria | ✔ |
| `gegrafico_permissao_tipo_grafico_consultar` | consultar | gegrafico_permissao_tipo_grafico | — | ✔ |
| `gegrafico_permissao_tipo_grafico_obter` | obter | gegrafico_permissao_tipo_grafico | codigo_do_grafico_referencia_a_tabela_ge, codigo_do_modulo_referencia_aos_codigos, tipo_do_grafico_referencia_a_tabela_gegr | ✔ |
| `gegrafico_plano_contas_empresa_consultar` | consultar | gegrafico_plano_contas_empresa | — | ✔ |
| `gegrafico_plano_contas_empresa_obter` | obter | gegrafico_plano_contas_empresa | codigo_do_grafico, empresa_selecionado | ✔ |
| `gegrafico_plano_contas_empresa_totais` | totais | gegrafico_plano_contas_empresa | — | ✔ |
| `gegrafico_tipo_consultar` | consultar | gegrafico_tipo | — | ✔ |
| `gegrafico_tipo_obter` | obter | gegrafico_tipo | chave_primaria | ✔ |
| `gegrafico_vinculo_consultar` | consultar | gegrafico_vinculo | — | ✔ |
| `gegrafico_vinculo_obter` | obter | gegrafico_vinculo | codigo | ✔ |
