# Módulo `pessoal_afastamentos`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `foafastamentos_dados_eventos_esocial_consultar` | consultar | foafastamentos_dados_eventos_esocial | empresa | ✔ |
| `foafastamentos_dados_eventos_esocial_obter` | obter | foafastamentos_dados_eventos_esocial | empresa, codigo_do_empregado, data_do_afastamento, codigo_sequencial | ✔ |
| `foafastamentos_envios_esocial_consultar` | consultar | foafastamentos_envios_esocial | empresa | ✔ |
| `foafastamentos_envios_esocial_obter` | obter | foafastamentos_envios_esocial | empresa, codigo_do_empregado, data_numerica_do_afastamento, codigo_da_empresa_referente_a_foesocial, codigo_referente_a_foesocial_dados_event | ✔ |
| `foafastamentos_estabilidade_consultar` | consultar | foafastamentos_estabilidade | empresa | ✔ |
| `foafastamentos_estabilidade_obter` | obter | foafastamentos_estabilidade | empresa, codigo_do_empregado, data_real_do_afastamento, codigo_do_tipo_de_estabilidade, codigo_sequencial_da_estabilidade | ✔ |
| `foafastamentos_periodo_aquisitivo_consultar` | consultar | foafastamentos_periodo_aquisitivo | empresa | ✔ |
| `foafastamentos_periodo_aquisitivo_obter` | obter | foafastamentos_periodo_aquisitivo | empresa, codigo, sequencia_de_periodos_aquisitivos, data_de_inicio_do_afastamento | ✔ |
| `foafastamentos_periodo_aquisitivo_totais` | totais | foafastamentos_periodo_aquisitivo | empresa | ✔ |
| `foafastamentos_somar_dias_consultar` | consultar | foafastamentos_somar_dias | empresa | ✔ |
| `foafastamentos_somar_dias_obter` | obter | foafastamentos_somar_dias | empresa, codigo_do_empregado, data_numerica_do_afastamento, data_real_dn_afastamento | ✔ |
