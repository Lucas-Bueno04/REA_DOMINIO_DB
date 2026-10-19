# Módulo `pessoal_calculos`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `focalculos_alteracao_salarial_consultar` | consultar | focalculos_alteracao_salarial | empresa | ✔ |
| `focalculos_alteracao_salarial_obter` | obter | focalculos_alteracao_salarial | empresa, codigo_do_empregado, data_da_alteracao_salarial, tipo_da_alteracao_salarial_1_normal_2_va, tipo_da_utilizacao_da_alteracao_no_calcu, codigo_do_calculo | ✔ |
| `focalculos_bases_inss_terceiros_consultar` | consultar | focalculos_bases_inss_terceiros | — | ✔ |
| `focalculos_bases_inss_terceiros_obter` | obter | focalculos_bases_inss_terceiros | codigo_do_convenio_de_terceiros, codigo_da_base_de_calculo | ✔ |
| `focalculos_bases_inss_terceiros_totais` | totais | focalculos_bases_inss_terceiros | — | ✔ |
| `focalculos_complementos_consultar` | consultar | focalculos_complementos | empresa | ✔ |
| `focalculos_complementos_obter` | obter | focalculos_complementos | empresa, codigo | ✔ |
| `focalculos_diferenca_rais_consultar` | consultar | focalculos_diferenca_rais | empresa | ✔ |
| `focalculos_diferenca_rais_obter` | obter | focalculos_diferenca_rais | empresa, codigo_do_empregado, competencia_do_calculo, codigo_do_calculo | ✔ |
| `focalculos_eventos_bases_consultar` | consultar | focalculos_eventos_bases | empresa | ✔ |
| `focalculos_eventos_bases_obter` | obter | focalculos_eventos_bases | empresa, codigo_do_empregado, identificacao_do_calculo, codigo_do_evento, codigo_da_base, codigo_do_emprestimo | ✔ |
| `focalculos_eventos_bases_totais` | totais | focalculos_eventos_bases | empresa | ✔ |
