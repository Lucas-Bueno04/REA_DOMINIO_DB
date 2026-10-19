# Módulo `pessoal_basesserv`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `fobasesserv_calculos_rateio_servico_consultar` | consultar | fobasesserv_calculos_rateio_servico | empresa | ✔ |
| `fobasesserv_calculos_rateio_servico_obter` | obter | fobasesserv_calculos_rateio_servico | empresa, codigo_do_empregado_do_calculo_integral, competencia_do_calculo_integral, tipo_de_processo_do_calculo_integral, codigo_do_servico_do_calculo_integral, rateio_do_calculo_integral, codigo_da_empresa_do_calculo_relacionado, codigo_do_empregado_do_calculo_relaciona, competencia_do_calculo_relacionado, tipo_de_processo_do_calculo_relacionado, codigo_do_servico_do_calculo_relacionado, rateio_do_calculo_relacionado, codigo_do_calculo_do_calculo_integral, codigo_do_calculo_do_calculo_relacionado | ✔ |
| `fobasesserv_envios_esocial_consultar` | consultar | fobasesserv_envios_esocial | empresa | ✔ |
| `fobasesserv_envios_esocial_obter` | obter | fobasesserv_envios_esocial | empresa, codigo_do_empregado, competencia, tipo_da_folha, codigo_do_servico, rateio, codigo_da_empresa_referente_a_foesocial, codigo_do_evento_referente_a_foesocial_d, codigo_do_calculo | ✔ |
| `fobasesserv_fofilhos_consultar` | consultar | fobasesserv_fofilhos | empresa | ✔ |
| `fobasesserv_fofilhos_obter` | obter | fobasesserv_fofilhos | empresa, codigo_do_empregado, competencia, tipo_de_folha, codigo_do_servico, rateio, codigo_do_dependente, codigo_do_calculo | ✔ |
| `fobasesserv_simulacao_consultar` | consultar | fobasesserv_simulacao | empresa | ✔ |
| `fobasesserv_simulacao_obter` | obter | fobasesserv_simulacao | empresa, empregado, competencia, tipo_de_calculo, servico, rateio, codigo_sequencial_de_calculos | ✔ |
| `fobasesserv_simulacao_totais` | totais | fobasesserv_simulacao | empresa | ✔ |
