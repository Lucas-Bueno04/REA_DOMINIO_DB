# Módulo `pessoal_movtoserv`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `fomovtoserv_dados_formula_consultar` | consultar | fomovtoserv_dados_formula | empresa | ✔ |
| `fomovtoserv_dados_formula_obter` | obter | fomovtoserv_dados_formula | empresa, codigo_do_empregado, competencia_do_calculo, tipo_de_calculo, codigo_do_evento, rateio, codigo_do_servico, codigo_do_calculo | ✔ |
| `fomovtoserv_dados_formula_totais` | totais | fomovtoserv_dados_formula | empresa | ✔ |
| `fomovtoserv_dados_per_dcomp_consultar` | consultar | fomovtoserv_dados_per_dcomp | empresa | ✔ |
| `fomovtoserv_dados_per_dcomp_obter` | obter | fomovtoserv_dados_per_dcomp | empresa, codigo_do_empregado, competencia_do_calculo, tipo_de_calculo, codigo_do_evento, rateio, codigo_do_servico, sequencial, codigo_do_calculo | ✔ |
| `fomovtoserv_dados_per_dcomp_totais` | totais | fomovtoserv_dados_per_dcomp | empresa | ✔ |
| `fomovtoserv_pensao_alimenticia_consultar` | consultar | fomovtoserv_pensao_alimenticia | empresa | ✔ |
| `fomovtoserv_pensao_alimenticia_obter` | obter | fomovtoserv_pensao_alimenticia | empresa, codigo_do_empregado, competencia, tipo_de_processo, codigo_do_evento, rateio, codigo_do_servico, codigo_do_dependente, codigo_do_calculo | ✔ |
| `fomovtoserv_pensao_alimenticia_totais` | totais | fomovtoserv_pensao_alimenticia | empresa | ✔ |
| `fomovtoserv_planosaude_consultar` | consultar | fomovtoserv_planosaude | empresa | ✔ |
| `fomovtoserv_planosaude_obter` | obter | fomovtoserv_planosaude | empresa, codigo_do_empregado, competencia, tipo_de_calculo, codigo_do_evento, rateio, codigo_do_servico, sequencial_de_beneficiario, codigo_do_calculo | ✔ |
| `fomovtoserv_planosaude_totais` | totais | fomovtoserv_planosaude | empresa | ✔ |
| `fomovtoserv_salario_familia_consultar` | consultar | fomovtoserv_salario_familia | empresa | ✔ |
| `fomovtoserv_salario_familia_obter` | obter | fomovtoserv_salario_familia | empresa, codigo_do_empregado, competencia, tipo_de_folha, codigo_do_evento, rateio, codigo_do_servico, codigo_do_dependente, codigo_do_calculo | ✔ |
| `fomovtoserv_simulacao_consultar` | consultar | fomovtoserv_simulacao | empresa | ✔ |
| `fomovtoserv_simulacao_obter` | obter | fomovtoserv_simulacao | empresa, empregado, competencia, tipo_folha, evento, rateio, servico, codigo_do_calculo | ✔ |
| `fomovtoserv_simulacao_totais` | totais | fomovtoserv_simulacao | empresa | ✔ |
