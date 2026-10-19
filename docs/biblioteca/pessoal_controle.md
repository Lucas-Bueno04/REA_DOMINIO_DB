# Módulo `pessoal_controle`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `focontrole_atualiza_dados_rais_consultar` | consultar | focontrole_atualiza_dados_rais | empresa | ✔ |
| `focontrole_atualiza_dados_rais_obter` | obter | focontrole_atualiza_dados_rais | empresa, codigo_do_controle | ✔ |
| `focontrole_atualizacao_tabelas_calculo_sgd_consultar` | consultar | focontrole_atualizacao_tabelas_calculo_sgd | — | ✔ |
| `focontrole_atualizacao_tabelas_calculo_sgd_obter` | obter | focontrole_atualizacao_tabelas_calculo_sgd | tipo_da_tabela_de_calculo_1_irrf_progres | ✔ |
| `focontrole_busca_tabelas_calculo_sgd_consultar` | consultar | focontrole_busca_tabelas_calculo_sgd | — | ✔ |
| `focontrole_busca_tabelas_calculo_sgd_obter` | obter | focontrole_busca_tabelas_calculo_sgd | data_da_busca, horario_da_busca, tipo_da_tabela_de_calculo_1_irrf_progres | ✔ |
| `focontrole_entrega_equipamentos_protecao_individual_consultar` | consultar | focontrole_entrega_equipamentos_protecao_individual | empresa | ✔ |
| `focontrole_entrega_equipamentos_protecao_individual_obter` | obter | focontrole_entrega_equipamentos_protecao_individual | empresa, codigo_do_empregado, codigo_do_epi, data_da_entrega | ✔ |
| `focontrole_entrega_equipamentos_protecao_individual_totais` | totais | focontrole_entrega_equipamentos_protecao_individual | empresa | ✔ |
| `focontrole_recalculo_consultar` | consultar | focontrole_recalculo | empresa | ✔ |
| `focontrole_recalculo_obter` | obter | focontrole_recalculo | empresa, codigo_do_empregado, tipo_de_calculo, competencia | ✔ |
