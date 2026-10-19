# Módulo `contabil_contas`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `ctcontas_aneel_consultar` | consultar | ctcontas_aneel | — | ✔ |
| `ctcontas_aneel_obter` | obter | ctcontas_aneel | codigo_sequencial, vigencia | ✔ |
| `ctcontas_ans_consultar` | consultar | ctcontas_ans | empresa | ✔ |
| `ctcontas_ans_obter` | obter | ctcontas_ans | empresa, codigo | ✔ |
| `ctcontas_bc_adm_consorcios_consultar` | consultar | ctcontas_bc_adm_consorcios | — | ✔ |
| `ctcontas_bc_adm_consorcios_obter` | obter | ctcontas_bc_adm_consorcios | codigo | ✔ |
| `ctcontas_bc_bancos_cambio_consultar` | consultar | ctcontas_bc_bancos_cambio | — | ✔ |
| `ctcontas_bc_bancos_cambio_obter` | obter | ctcontas_bc_bancos_cambio | codigo | ✔ |
| `ctcontas_bc_geral_consultar` | consultar | ctcontas_bc_geral | — | ✔ |
| `ctcontas_bc_geral_obter` | obter | ctcontas_bc_geral | codigo | ✔ |
| `ctcontas_bc_instituicao_pagamento_consultar` | consultar | ctcontas_bc_instituicao_pagamento | — | ✔ |
| `ctcontas_bc_instituicao_pagamento_obter` | obter | ctcontas_bc_instituicao_pagamento | codigo | ✔ |
| `ctcontas_bc_sociedade_corretora_cambio_consultar` | consultar | ctcontas_bc_sociedade_corretora_cambio | — | ✔ |
| `ctcontas_bc_sociedade_corretora_cambio_obter` | obter | ctcontas_bc_sociedade_corretora_cambio | codigo | ✔ |
| `ctcontas_bc_sociedade_corretora_cambio_totais` | totais | ctcontas_bc_sociedade_corretora_cambio | — | ✔ |
| `ctcontas_bc_sociedade_corretora_titulos_consultar` | consultar | ctcontas_bc_sociedade_corretora_titulos | — | ✔ |
| `ctcontas_bc_sociedade_corretora_titulos_obter` | obter | ctcontas_bc_sociedade_corretora_titulos | codigo | ✔ |
| `ctcontas_bc_valores_mobiliarios_consultar` | consultar | ctcontas_bc_valores_mobiliarios | — | ✔ |
| `ctcontas_bc_valores_mobiliarios_obter` | obter | ctcontas_bc_valores_mobiliarios | codigo | ✔ |
| `ctcontas_cofi_consultar` | consultar | ctcontas_cofi | — | ✔ |
| `ctcontas_cofi_obter` | obter | ctcontas_cofi | codigo | ✔ |
| `ctcontas_cosif_consultar` | consultar | ctcontas_cosif | — | ✔ |
| `ctcontas_cosif_obter` | obter | ctcontas_cosif | codigo | ✔ |
| `ctcontas_equivalentes_consultar` | consultar | ctcontas_equivalentes | empresa | ✔ |
| `ctcontas_equivalentes_obter` | obter | ctcontas_equivalentes | empresa, conta_equivalente_caixa | ✔ |
| `ctcontas_grupos_dlpa_consultar` | consultar | ctcontas_grupos_dlpa | empresa | ✔ |
| `ctcontas_grupos_dlpa_obter` | obter | ctcontas_grupos_dlpa | empresa, codigo_da_conta, codigo_do_grupo_dlpa | ✔ |
| `ctcontas_idiomas_consultar` | consultar | ctcontas_idiomas | empresa | ✔ |
| `ctcontas_idiomas_obter` | obter | ctcontas_idiomas | empresa, codigo_da_conta, codigo_do_idioma | ✔ |
| `ctcontas_scp_consultar` | consultar | ctcontas_scp | empresa | ✔ |
| `ctcontas_scp_obter` | obter | ctcontas_scp | empresa, codigo_da_conta, empresa_corrente | ✔ |
| `ctcontas_sped_ecf_entidade_fechada_consultar` | consultar | ctcontas_sped_ecf_entidade_fechada | — | ✔ |
| `ctcontas_sped_ecf_entidade_fechada_obter` | obter | ctcontas_sped_ecf_entidade_fechada | codigo | ✔ |
| `ctcontas_sped_ecf_geral_ref_sa_scp_consultar` | consultar | ctcontas_sped_ecf_geral_ref_sa_scp | empresa | ✔ |
| `ctcontas_sped_ecf_geral_ref_sa_scp_obter` | obter | ctcontas_sped_ecf_geral_ref_sa_scp | empresa, conta_contabil, empresa_corrente, conta_sped_ecf, sequencial | ✔ |
| `ctcontas_sped_ecf_geral_ref_sa_scp_totais` | totais | ctcontas_sped_ecf_geral_ref_sa_scp | empresa | ✔ |
| `ctcontas_sped_ecf_imune_isenta_ref_sa_scp_consultar` | consultar | ctcontas_sped_ecf_imune_isenta_ref_sa_scp | empresa | ✔ |
| `ctcontas_sped_ecf_imune_isenta_ref_sa_scp_obter` | obter | ctcontas_sped_ecf_imune_isenta_ref_sa_scp | empresa, conta_contabil, empresa_corrente, conta_sped_ecf, sequencial | ✔ |
| `ctcontas_sped_ecf_imune_isenta_ref_sa_scp_totais` | totais | ctcontas_sped_ecf_imune_isenta_ref_sa_scp | empresa | ✔ |
| `ctcontas_sped_ecf_partido_politico_consultar` | consultar | ctcontas_sped_ecf_partido_politico | — | ✔ |
| `ctcontas_sped_ecf_partido_politico_obter` | obter | ctcontas_sped_ecf_partido_politico | codigo | ✔ |
| `ctcontas_sped_ecf_seguradora_consultar` | consultar | ctcontas_sped_ecf_seguradora | — | ✔ |
| `ctcontas_sped_ecf_seguradora_obter` | obter | ctcontas_sped_ecf_seguradora | codigo | ✔ |
| `ctcontas_sped_ecf_sistema_financeiro_consultar` | consultar | ctcontas_sped_ecf_sistema_financeiro | — | ✔ |
| `ctcontas_sped_ecf_sistema_financeiro_obter` | obter | ctcontas_sped_ecf_sistema_financeiro | codigo | ✔ |
| `ctcontas_sped_ecf_sistema_financeiro_presumido_consultar` | consultar | ctcontas_sped_ecf_sistema_financeiro_presumido | — | ✔ |
| `ctcontas_sped_ecf_sistema_financeiro_presumido_obter` | obter | ctcontas_sped_ecf_sistema_financeiro_presumido | codigo | ✔ |
| `ctcontas_sped_ecf_tef_consultar` | consultar | ctcontas_sped_ecf_tef | — | ✔ |
| `ctcontas_sped_ecf_tef_obter` | obter | ctcontas_sped_ecf_tef | codigo | ✔ |
| `ctcontas_susep_consultar` | consultar | ctcontas_susep | — | ✔ |
| `ctcontas_susep_obter` | obter | ctcontas_susep | codigo | ✔ |
