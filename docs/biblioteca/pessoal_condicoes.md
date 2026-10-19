# Módulo `pessoal_condicoes`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `focondicoes_ambientais_trabalho_consultar` | consultar | focondicoes_ambientais_trabalho | empresa | ✔ |
| `focondicoes_ambientais_trabalho_obter` | obter | focondicoes_ambientais_trabalho | empresa, codigo_do_empregado, data_inicio_da_condicao | ✔ |
| `focondicoes_ambientais_trabalho_envios_esocial_consultar` | consultar | focondicoes_ambientais_trabalho_envios_esocial | empresa | ✔ |
| `focondicoes_ambientais_trabalho_envios_esocial_obter` | obter | focondicoes_ambientais_trabalho_envios_esocial | empresa, codigo_do_empregado, data_de_inicio, codigo_da_empresa_referente_a_foesocial, codigo_do_evento_referente_a_foesocial_d | ✔ |
| `focondicoes_ambientais_trabalho_fator_risco_consultar` | consultar | focondicoes_ambientais_trabalho_fator_risco | empresa | ✔ |
| `focondicoes_ambientais_trabalho_fator_risco_obter` | obter | focondicoes_ambientais_trabalho_fator_risco | empresa, codigo_do_empregado, data_inicio_da_condicao, fator_de_risco, sequencial | ✔ |
| `focondicoes_ambientais_trabalho_informacoes_consultar` | consultar | focondicoes_ambientais_trabalho_informacoes | empresa | ✔ |
| `focondicoes_ambientais_trabalho_informacoes_obter` | obter | focondicoes_ambientais_trabalho_informacoes | empresa, codigo_do_empregado, data_inicio_da_condicao, codigo_do_ambiente_de_trabalho | ✔ |
| `focondicoes_ambientais_trabalho_lista_atividades_consultar` | consultar | focondicoes_ambientais_trabalho_lista_atividades | — | ✔ |
| `focondicoes_ambientais_trabalho_lista_atividades_obter` | obter | focondicoes_ambientais_trabalho_lista_atividades | codigo_da_atividade | ✔ |
| `focondicoes_ambientais_trabalho_lista_fatores_risco_consultar` | consultar | focondicoes_ambientais_trabalho_lista_fatores_risco | — | ✔ |
| `focondicoes_ambientais_trabalho_lista_fatores_risco_obter` | obter | focondicoes_ambientais_trabalho_lista_fatores_risco | codigo_sequencial_do_fator_de_risco | ✔ |
| `focondicoes_ambientais_trabalho_responsavel_consultar` | consultar | focondicoes_ambientais_trabalho_responsavel | empresa | ✔ |
| `focondicoes_ambientais_trabalho_responsavel_obter` | obter | focondicoes_ambientais_trabalho_responsavel | empresa, codigo_do_empregado, data_inicio_da_condicao, codigo_sequencial | ✔ |
| `focondicoes_ambientais_trabalho_unidade_medida_fa_7902_consultar` | consultar | focondicoes_ambientais_trabalho_unidade_medida_fator_risco | — | ✔ |
| `focondicoes_ambientais_trabalho_unidade_medida_fator_risco_obter` | obter | focondicoes_ambientais_trabalho_unidade_medida_fator_risco | codigo_da_unidade_de_medida | ✔ |
