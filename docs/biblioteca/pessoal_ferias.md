# Módulo `pessoal_ferias`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `foferias_coletivas_consultar` | consultar | foferias_coletivas | empresa | ✔ |
| `foferias_coletivas_obter` | obter | foferias_coletivas | empresa, sequencial_de_ferias_coletivas | ✔ |
| `foferias_gozo_afastamentos_consultar` | consultar | foferias_gozo_afastamentos | empresa | ✔ |
| `foferias_gozo_afastamentos_obter` | obter | foferias_gozo_afastamentos | empresa, codigo_do_empregado, sequencial_do_calculo_de_ferias, sequencial | ✔ |
| `foferias_gozo_diasdesconsiderar_consultar` | consultar | foferias_gozo_diasdesconsiderar | empresa | ✔ |
| `foferias_gozo_diasdesconsiderar_obter` | obter | foferias_gozo_diasdesconsiderar | empresa, codigo, sequencial_de_periodos_de_gozo, dia_a_ser_desconsiderado | ✔ |
| `foferias_gozo_diasdesconsiderar_simulacao_consultar` | consultar | foferias_gozo_diasdesconsiderar_simulacao | empresa | ✔ |
| `foferias_gozo_diasdesconsiderar_simulacao_obter` | obter | foferias_gozo_diasdesconsiderar_simulacao | empresa, codigo, sequencial_de_periodos_de_gozo, dia_a_ser_desconsiderado | ✔ |
| `foferias_gozo_medias_consultar` | consultar | foferias_gozo_medias | empresa | ✔ |
| `foferias_gozo_medias_obter` | obter | foferias_gozo_medias | empresa, codigo, sequencial_de_periodos_de_gozo, horas_valor_vantagem_ou_hora_aula, ferias_vencidas_ou_13o_salario | ✔ |
| `foferias_gozo_medias_totais` | totais | foferias_gozo_medias | empresa | ✔ |
| `foferias_gozo_medias_simulacao_consultar` | consultar | foferias_gozo_medias_simulacao | empresa | ✔ |
| `foferias_gozo_medias_simulacao_obter` | obter | foferias_gozo_medias_simulacao | empresa, codigo, sequencial_de_periodos_de_gozo, horas_valor_vantagem_ou_hora_aula, ferias_vencidas_ou_13o_salario | ✔ |
| `foferias_gozo_medias_simulacao_totais` | totais | foferias_gozo_medias_simulacao | empresa | ✔ |
| `foferias_gozo_simulacao_consultar` | consultar | foferias_gozo_simulacao | empresa | ✔ |
| `foferias_gozo_simulacao_obter` | obter | foferias_gozo_simulacao | empresa, codigo, sequencial_de_periodos_de_gozo | ✔ |
| `foferias_gozo_simulacao_totais` | totais | foferias_gozo_simulacao | empresa | ✔ |
| `foferias_gozo_tipo_consultar` | consultar | foferias_gozo_tipo | empresa | ✔ |
| `foferias_gozo_tipo_obter` | obter | foferias_gozo_tipo | empresa, codigo, sequencial_de_periodos_de_gozo, tipo_de_gozo_gozo_abono_lic_remum, competencia, data_numerica_inicial | ✔ |
| `foferias_gozo_tipo_totais` | totais | foferias_gozo_tipo | empresa | ✔ |
| `foferias_gozo_tipo_simulacao_consultar` | consultar | foferias_gozo_tipo_simulacao | empresa | ✔ |
| `foferias_gozo_tipo_simulacao_obter` | obter | foferias_gozo_tipo_simulacao | empresa, codigo, sequencial_de_periodos_de_gozo, tipo_de_gozo_gozo_abono_lic_remum, competencia, data_numerica_inicial | ✔ |
| `foferias_gozo_tipo_simulacao_totais` | totais | foferias_gozo_tipo_simulacao | empresa | ✔ |
| `foferias_gozo_vantagens_consultar` | consultar | foferias_gozo_vantagens | empresa | ✔ |
| `foferias_gozo_vantagens_obter` | obter | foferias_gozo_vantagens | empresa, codigo, sequencial_de_periodos_de_gozo, codigo_do_evento | ✔ |
| `foferias_gozo_vantagens_totais` | totais | foferias_gozo_vantagens | empresa | ✔ |
| `foferias_gozo_vantagens_simulacao_consultar` | consultar | foferias_gozo_vantagens_simulacao | empresa | ✔ |
| `foferias_gozo_vantagens_simulacao_obter` | obter | foferias_gozo_vantagens_simulacao | empresa, codigo, sequencial_de_periodos_de_gozo, codigo_do_evento | ✔ |
| `foferias_gozo_vantagens_simulacao_totais` | totais | foferias_gozo_vantagens_simulacao | empresa | ✔ |
| `foferias_lancamentos_consultar` | consultar | foferias_lancamentos | empresa | ✔ |
| `foferias_lancamentos_obter` | obter | foferias_lancamentos | empresa, codigo_do_empregado, codigo_do_gozo, codigo_do_evento | ✔ |
| `foferias_lancamentos_totais` | totais | foferias_lancamentos | empresa | ✔ |
| `foferias_lancamentos_pensao_alimenticia_consultar` | consultar | foferias_lancamentos_pensao_alimenticia | empresa | ✔ |
| `foferias_lancamentos_pensao_alimenticia_obter` | obter | foferias_lancamentos_pensao_alimenticia | empresa, codigo_do_empregado, codigo_do_periodo_de_gozo, codigo_do_evento, codigo_do_dependente | ✔ |
| `foferias_lancamentos_pensao_alimenticia_totais` | totais | foferias_lancamentos_pensao_alimenticia | empresa | ✔ |
| `foferias_lancamentos_planosaude_consultar` | consultar | foferias_lancamentos_planosaude | empresa | ✔ |
| `foferias_lancamentos_planosaude_obter` | obter | foferias_lancamentos_planosaude | empresa, codigo_do_empregado, codigo_do_gozo, codigo_do_evento, sequencial_de_beneficiario | ✔ |
| `foferias_lancamentos_planosaude_totais` | totais | foferias_lancamentos_planosaude | empresa | ✔ |
| `foferias_programacao_consultar` | consultar | foferias_programacao | empresa | ✔ |
| `foferias_programacao_obter` | obter | foferias_programacao | empresa, codigo, codigo_da_programacao_de_ferias, c_1_programacao_2_aviso | ✔ |
| `foferias_programacao_totais` | totais | foferias_programacao | empresa | ✔ |
