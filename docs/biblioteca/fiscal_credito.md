# Módulo `fiscal_credito`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `efcredito_presumido_piscofins_consultar` | consultar | efcredito_presumido_piscofins | — | ✔ |
| `efcredito_presumido_piscofins_obter` | obter | efcredito_presumido_piscofins | sequencial_do_credito_presumido | ✔ |
| `efcredito_presumido_piscofins_receitas_consultar` | consultar | efcredito_presumido_piscofins_receitas | empresa | ✔ |
| `efcredito_presumido_piscofins_receitas_obter` | obter | efcredito_presumido_piscofins_receitas | empresa, sequencial | ✔ |
| `efcredito_presumido_piscofins_receitas_vigencia_consultar` | consultar | efcredito_presumido_piscofins_receitas_vigencia | empresa | ✔ |
| `efcredito_presumido_piscofins_receitas_vigencia_obter` | obter | efcredito_presumido_piscofins_receitas_vigencia | empresa, sequencial, vigencia | ✔ |
| `efcredito_presumido_piscofins_receitas_vigencia_d_4964_consultar` | consultar | efcredito_presumido_piscofins_receitas_vigencia_detalhamento | empresa | ✔ |
| `efcredito_presumido_piscofins_receitas_vigencia_detal_4964_obter` | obter | efcredito_presumido_piscofins_receitas_vigencia_detalhamento | empresa, sequencial, vigencia, sequencial_detalhamento | ✔ |
| `efcredito_presumido_piscofins_vigencia_consultar` | consultar | efcredito_presumido_piscofins_vigencia | — | ✔ |
| `efcredito_presumido_piscofins_vigencia_obter` | obter | efcredito_presumido_piscofins_vigencia | sequencial_do_credito_presumido, vigencia | ✔ |
| `efcredito_presumido_piscofins_vigencia_detalhamento_consultar` | consultar | efcredito_presumido_piscofins_vigencia_detalhamento | — | ✔ |
| `efcredito_presumido_piscofins_vigencia_detalhamento_obter` | obter | efcredito_presumido_piscofins_vigencia_detalhamento | sequencial_do_credito_presumido, vigencia, sequencial_do_detalhamento | ✔ |
| `efcredito_presumido_piscofins_vigencia_detalhamento_totais` | totais | efcredito_presumido_piscofins_vigencia_detalhamento | — | ✔ |
