# Módulo `pessoal_memoria`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `fomemoria_calculo_diferenca_consultar` | consultar | fomemoria_calculo_diferenca | — | ✔ |
| `fomemoria_calculo_diferenca_obter` | obter | fomemoria_calculo_diferenca | codigo_do_calculo_ajustado, codigo_do_calculo_da_diferenca | ✔ |
| `fomemoria_calculo_diferenca_salarial_cct_esocial_consultar` | consultar | fomemoria_calculo_diferenca_salarial_cct_esocial | empresa | ✔ |
| `fomemoria_calculo_diferenca_salarial_cct_esocial_obter` | obter | fomemoria_calculo_diferenca_salarial_cct_esocial | empresa, codigo_do_evento, servico, rateio, codigo_do_calculo_ajustado, codigo_do_calculo_da_diferenca | ✔ |
| `fomemoria_calculo_diferenca_salarial_cct_esocial_totais` | totais | fomemoria_calculo_diferenca_salarial_cct_esocial | empresa | ✔ |
| `fomemoria_calculo_diferenca_salario_consultar` | consultar | fomemoria_calculo_diferenca_salario | empresa | ✔ |
| `fomemoria_calculo_diferenca_salario_obter` | obter | fomemoria_calculo_diferenca_salario | empresa, codigo_do_evento, servico, rateio, codigo_do_calculo_ajustado, codigo_do_calculo_da_diferenca | ✔ |
| `fomemoria_calculo_diferenca_salario_totais` | totais | fomemoria_calculo_diferenca_salario | empresa | ✔ |
| `fomemoria_calculo_diferenca_salario_bases_consultar` | consultar | fomemoria_calculo_diferenca_salario_bases | — | ✔ |
| `fomemoria_calculo_diferenca_salario_bases_obter` | obter | fomemoria_calculo_diferenca_salario_bases | codigo_da_base_de_calculo, servico, rateio, codigo_do_calculo_ajustado, codigo_do_calculo_da_diferenca | ✔ |
| `fomemoria_calculo_diferenca_salario_bases_totais` | totais | fomemoria_calculo_diferenca_salario_bases | — | ✔ |
| `fomemoria_calculo_inss_consultar` | consultar | fomemoria_calculo_inss | empresa | ✔ |
| `fomemoria_calculo_inss_obter` | obter | fomemoria_calculo_inss | empresa, codigo_do_empregado, competencia, tipo_de_processo, codigo_da_rubrica, rateio, codigo_do_servico, sequencial, codigo_do_calculo | ✔ |
| `fomemoria_calculo_inss_totais` | totais | fomemoria_calculo_inss | empresa | ✔ |
| `fomemoria_calculo_salario_indenizacao_mp_936_consultar` | consultar | fomemoria_calculo_salario_indenizacao_mp_936 | empresa | ✔ |
| `fomemoria_calculo_salario_indenizacao_mp_936_obter` | obter | fomemoria_calculo_salario_indenizacao_mp_936 | empresa, codigo_do_empregado, competencia, tipo_da_folha, codigo_do_servico, rateio_do_servico, codigo_sequencial, codigo_do_calculo | ✔ |
| `fomemoria_calculo_salario_indenizacao_mp_936_totais` | totais | fomemoria_calculo_salario_indenizacao_mp_936 | empresa | ✔ |
| `fomemoria_calculo_salario_proporcional_consultar` | consultar | fomemoria_calculo_salario_proporcional | empresa | ✔ |
| `fomemoria_calculo_salario_proporcional_obter` | obter | fomemoria_calculo_salario_proporcional | empresa, codigo_do_empregado, competencia, tipo_da_folha, codigo_do_servico, rateio_do_servico, codigo_sequencial, codigo_do_calculo | ✔ |
| `fomemoria_calculo_salario_proporcional_totais` | totais | fomemoria_calculo_salario_proporcional | empresa | ✔ |
