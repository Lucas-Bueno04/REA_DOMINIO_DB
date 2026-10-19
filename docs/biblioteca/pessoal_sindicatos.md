# Módulo `pessoal_sindicatos`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `fosindicatos_adicional_ferias_consultar` | consultar | fosindicatos_adicional_ferias | — | ✔ |
| `fosindicatos_adicional_ferias_obter` | obter | fosindicatos_adicional_ferias | codigo_do_sindicato, codigo_da_regra, sequencial_da_regra | ✔ |
| `fosindicatos_adicional_ferias_totais` | totais | fosindicatos_adicional_ferias | — | ✔ |
| `fosindicatos_cadastro_consultar` | consultar | fosindicatos_cadastro | — | ✔ |
| `fosindicatos_cadastro_obter` | obter | fosindicatos_cadastro | codigo_do_sindicato | ✔ |
| `fosindicatos_cct_consultar` | consultar | fosindicatos_cct | — | ✔ |
| `fosindicatos_cct_obter` | obter | fosindicatos_cct | codigo_do_sindicato, data_do_registro | ✔ |
| `fosindicatos_cct_documentos_anexados_consultar` | consultar | fosindicatos_cct_documentos_anexados | — | ✔ |
| `fosindicatos_cct_documentos_anexados_obter` | obter | fosindicatos_cct_documentos_anexados | codigo_do_sindicato, data_de_registro_da_convencao_coletiva, numero_sequencial_do_cadastro_do_arquivo | ✔ |
| `fosindicatos_config_motivos_rescisao_estab_afast_consultar` | consultar | fosindicatos_config_motivos_rescisao_estab_afast | — | ✔ |
| `fosindicatos_config_motivos_rescisao_estab_afast_obter` | obter | fosindicatos_config_motivos_rescisao_estab_afast | codigo_do_sindicato, codigo_do_motivo_de_rescisao | ✔ |
| `fosindicatos_diasaviso_consultar` | consultar | fosindicatos_diasaviso | — | ✔ |
| `fosindicatos_diasaviso_obter` | obter | fosindicatos_diasaviso | codigo_do_sindicato, numero_da_regra, sequencial_de_expressoes_da_regra | ✔ |
| `fosindicatos_diasaviso_totais` | totais | fosindicatos_diasaviso | — | ✔ |
| `fosindicatos_empresas_consultar` | consultar | fosindicatos_empresas | empresa | ✔ |
| `fosindicatos_empresas_obter` | obter | fosindicatos_empresas | empresa, codigo_do_sindicato | ✔ |
| `fosindicatos_estabilidade_afastamentos_consultar` | consultar | fosindicatos_estabilidade_afastamentos | — | ✔ |
| `fosindicatos_estabilidade_afastamentos_obter` | obter | fosindicatos_estabilidade_afastamentos | codigo_do_sindicato, codigo_da_regra, sequencial_da_regra | ✔ |
| `fosindicatos_estabilidade_afastamentos_totais` | totais | fosindicatos_estabilidade_afastamentos | — | ✔ |
| `fosindicatos_garantia_comissionados_consultar` | consultar | fosindicatos_garantia_comissionados | — | ✔ |
| `fosindicatos_garantia_comissionados_obter` | obter | fosindicatos_garantia_comissionados | codigo_do_sindicato, sequencial_da_regra | ✔ |
| `fosindicatos_garantia_comissionados_totais` | totais | fosindicatos_garantia_comissionados | — | ✔ |
| `fosindicatos_garantia_semestral_consultar` | consultar | fosindicatos_garantia_semestral | — | ✔ |
| `fosindicatos_garantia_semestral_obter` | obter | fosindicatos_garantia_semestral | codigo_do_sindicato, codigo_da_regra, sequencial_da_regra | ✔ |
| `fosindicatos_garantia_semestral_totais` | totais | fosindicatos_garantia_semestral | — | ✔ |
| `fosindicatos_indenizacao_especial_consultar` | consultar | fosindicatos_indenizacao_especial | — | ✔ |
| `fosindicatos_indenizacao_especial_obter` | obter | fosindicatos_indenizacao_especial | codigo_do_sindicato, codigo_da_regra, sequencial_da_regra | ✔ |
| `fosindicatos_indenizacao_especial_totais` | totais | fosindicatos_indenizacao_especial | — | ✔ |
| `fosindicatos_medias_consultar` | consultar | fosindicatos_medias | — | ✔ |
| `fosindicatos_medias_obter` | obter | fosindicatos_medias | codigo, tipo_de_media_1_ferias_2_13o_salario_3_a, codigo_da_configuracao, configuracao_de_media_para_comissoes_0_n | ✔ |
| `fosindicatos_medias_totais` | totais | fosindicatos_medias | — | ✔ |
| `fosindicatos_plr_consultar` | consultar | fosindicatos_plr | — | ✔ |
| `fosindicatos_plr_obter` | obter | fosindicatos_plr | codigo_do_sindicato, codigo_da_regra, codigo_sequencial_da_regra, tipo_de_configuracao_1_pagamento_2_desco | ✔ |
| `fosindicatos_plr_totais` | totais | fosindicatos_plr | — | ✔ |
