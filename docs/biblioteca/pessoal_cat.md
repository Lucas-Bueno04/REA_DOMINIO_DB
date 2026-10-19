# Módulo `pessoal_cat`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `focat_agente_causador_consultar` | consultar | focat_agente_causador | — | ✔ |
| `focat_agente_causador_obter` | obter | focat_agente_causador | codigo_do_agente_causador | ✔ |
| `focat_agente_causador_lista_consultar` | consultar | focat_agente_causador_lista | empresa | ✔ |
| `focat_agente_causador_lista_obter` | obter | focat_agente_causador_lista | empresa, codigo_do_empregado, codigo_da_cat, sequencial_da_lista | ✔ |
| `focat_envios_esocial_consultar` | consultar | focat_envios_esocial | empresa | ✔ |
| `focat_envios_esocial_obter` | obter | focat_envios_esocial | empresa, codigo_do_empregado, codigo_do_cat_referente_a_focat, codigo_da_empresa_referente_a_foesocial, codigo_do_evento_referente_a_foesocial_d | ✔ |
| `focat_natureza_lesao_consultar` | consultar | focat_natureza_lesao | — | ✔ |
| `focat_natureza_lesao_obter` | obter | focat_natureza_lesao | codigo_da_natureza_da_lesao | ✔ |
| `focat_parte_corpo_atingida_consultar` | consultar | focat_parte_corpo_atingida | — | ✔ |
| `focat_parte_corpo_atingida_obter` | obter | focat_parte_corpo_atingida | codigo_da_parte_do_corpo_atingida | ✔ |
| `focat_parte_corpo_atingida_lista_consultar` | consultar | focat_parte_corpo_atingida_lista | empresa | ✔ |
| `focat_parte_corpo_atingida_lista_obter` | obter | focat_parte_corpo_atingida_lista | empresa, codigo_do_empregado, codigo_da_cat, sequencial_da_lista | ✔ |
| `focat_situacao_geradora_consultar` | consultar | focat_situacao_geradora | — | ✔ |
| `focat_situacao_geradora_obter` | obter | focat_situacao_geradora | codigo_da_situacao_geradora | ✔ |
| `focat_tipo_acidente_consultar` | consultar | focat_tipo_acidente | — | ✔ |
| `focat_tipo_acidente_obter` | obter | focat_tipo_acidente | codigo_do_tipo_de_acidente | ✔ |
