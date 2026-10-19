# Módulo `pessoal_provisoes`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `foprovisoes_periodos_consultar` | consultar | foprovisoes_periodos | empresa | ✔ |
| `foprovisoes_periodos_obter` | obter | foprovisoes_periodos | empresa, codigo_do_empregado, competencia, tipo_da_provisao, sequencia_de_periodos_aquisitivos | ✔ |
| `foprovisoes_periodos_totais` | totais | foprovisoes_periodos | empresa | ✔ |
| `foprovisoes_periodos_valores_consultar` | consultar | foprovisoes_periodos_valores | empresa | ✔ |
| `foprovisoes_periodos_valores_obter` | obter | foprovisoes_periodos_valores | empresa, codigo_do_empregado, competencia, tipo_de_provisao, sequencia_de_periodos_aquisitivos, tipo_de_valor_da_provisao | ✔ |
| `foprovisoes_periodos_valores_totais` | totais | foprovisoes_periodos_valores | empresa | ✔ |
| `foprovisoes_valores_consultar` | consultar | foprovisoes_valores | empresa | ✔ |
| `foprovisoes_valores_obter` | obter | foprovisoes_valores | empresa, codigo_do_empregado, competencia, tipo_de_provisao, tipo_de_valor | ✔ |
| `foprovisoes_valores_totais` | totais | foprovisoes_valores | empresa | ✔ |
| `foprovisoes_valores_tipos_consultar` | consultar | foprovisoes_valores_tipos | — | ✔ |
| `foprovisoes_valores_tipos_obter` | obter | foprovisoes_valores_tipos | tipo_de_valor | ✔ |
