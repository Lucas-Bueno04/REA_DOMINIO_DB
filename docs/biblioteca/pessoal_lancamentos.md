# Módulo `pessoal_lancamentos`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `folancamentos_automaticos_complementos_consultar` | consultar | folancamentos_automaticos_complementos | empresa | ✔ |
| `folancamentos_automaticos_complementos_obter` | obter | folancamentos_automaticos_complementos | empresa, codigo_do_lancamento_automatico, codigo_do_complemento_de_calculo | ✔ |
| `folancamentos_eventos_complementos_consultar` | consultar | folancamentos_eventos_complementos | empresa | ✔ |
| `folancamentos_eventos_complementos_obter` | obter | folancamentos_eventos_complementos | empresa, codigo_do_empregado, codigo_do_evento, tipo_do_processo_42_complementar, tipo_do_lancamento_1_mensal_2_fixo, competencia_inicial_do_lancamento, sequencial_do_lancamento, codigo_do_complemento_de_calculo | ✔ |
| `folancamentos_eventos_pensao_alimenticia_consultar` | consultar | folancamentos_eventos_pensao_alimenticia | empresa | ✔ |
| `folancamentos_eventos_pensao_alimenticia_obter` | obter | folancamentos_eventos_pensao_alimenticia | empresa, codigo_do_empregado, codigo_do_evento, tipo_de_processo, tipo_de_lancamento_1_mensal_2_fixo, competencia_do_lancamento, sequencial, codigo_do_dependente | ✔ |
| `folancamentos_eventos_pensao_alimenticia_totais` | totais | folancamentos_eventos_pensao_alimenticia | empresa | ✔ |
| `folancamentos_eventos_servicos_consultar` | consultar | folancamentos_eventos_servicos | empresa | ✔ |
| `folancamentos_eventos_servicos_obter` | obter | folancamentos_eventos_servicos | empresa, codigo_do_empregado, codigo_do_evento, tipo_do_processo_11_mensal_31_1a_semana, tipo_de_lancamento_1_mensal_2_fixo, competencia_inicial, sequencial, codigo_do_servico | ✔ |
| `folancamentos_eventos_servicos_totais` | totais | folancamentos_eventos_servicos | empresa | ✔ |
| `folancamentos_eventos_vale_alimentacao_consultar` | consultar | folancamentos_eventos_vale_alimentacao | empresa | ✔ |
| `folancamentos_eventos_vale_alimentacao_obter` | obter | folancamentos_eventos_vale_alimentacao | empresa, codigo_do_vale_alimentacao, codigo_do_empregado, competencia_do_lancamento, tipo_de_processo_do_lancamento, tipo_do_lancamento, sequencial_do_lancamento | ✔ |
| `folancamentos_eventos_vale_alimentacao_totais` | totais | folancamentos_eventos_vale_alimentacao | empresa | ✔ |
