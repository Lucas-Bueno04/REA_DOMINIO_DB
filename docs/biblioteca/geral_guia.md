# Módulo `geral_guia`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `geguia_contribuicao_previdenciaria_consultar` | consultar | geguia_contribuicao_previdenciaria | empresa | ✔ |
| `geguia_contribuicao_previdenciaria_obter` | obter | geguia_contribuicao_previdenciaria | empresa, competencia, tipo_de_guia_1_mensal_2_13o_salario_3_tr, sequencial | ✔ |
| `geguia_contribuicao_previdenciaria_totais` | totais | geguia_contribuicao_previdenciaria | empresa | ✔ |
| `geguia_contribuicao_previdenciaria_compensacoes_dcomp_consultar` | consultar | geguia_contribuicao_previdenciaria_compensacoes_dcomp | empresa | ✔ |
| `geguia_contribuicao_previdenciaria_compensacoes_dcomp_obter` | obter | geguia_contribuicao_previdenciaria_compensacoes_dcomp | empresa, competencia, tipo_de_guia_1_mensal_2_13o_salario_3_tr, tipo_de_credito_1_pagamento_indevido_ou, sequencial_unico | ✔ |
| `geguia_contribuicao_previdenciaria_compensacoes_dcomp_totais` | totais | geguia_contribuicao_previdenciaria_compensacoes_dcomp | empresa | ✔ |
| `geguia_contribuicao_previdenciaria_saldos_compensar_consultar` | consultar | geguia_contribuicao_previdenciaria_saldos_compensar | empresa | ✔ |
| `geguia_contribuicao_previdenciaria_saldos_compensar_obter` | obter | geguia_contribuicao_previdenciaria_saldos_compensar | empresa, competencia, tipo_de_guia_1_mensal_2_13o_salario_3_tr, tipo_de_saldo_a_compensar_1_compensacao, sequencial | ✔ |
| `geguia_contribuicao_previdenciaria_saldos_compensar_totais` | totais | geguia_contribuicao_previdenciaria_saldos_compensar | empresa | ✔ |
| `geguia_contribuicao_previdenciaria_saldos_recolher_consultar` | consultar | geguia_contribuicao_previdenciaria_saldos_recolher | empresa | ✔ |
| `geguia_contribuicao_previdenciaria_saldos_recolher_obter` | obter | geguia_contribuicao_previdenciaria_saldos_recolher | empresa, competencia, tipo_de_guia_1_mensal_2_13o_salario_3_tr, tipo_saldo_recolher, sequencial | ✔ |
| `geguia_contribuicao_previdenciaria_saldos_recolher_totais` | totais | geguia_contribuicao_previdenciaria_saldos_recolher | empresa | ✔ |
| `geguia_contribuicao_previdenciaria_saldos_recolhe_8beb_consultar` | consultar | geguia_contribuicao_previdenciaria_saldos_recolher_valores_compensados | empresa | ✔ |
| `geguia_contribuicao_previdenciaria_saldos_recolher_va_8beb_obter` | obter | geguia_contribuicao_previdenciaria_saldos_recolher_valores_compensados | empresa, competencia, tipo_de_guia_1_mensal_2_13o_salario_3_tr, tipo_de_saldo_a_recolher, tipo_de_saldo_a_compensar, sequencial | ✔ |
| `geguia_contribuicao_previdenciaria_saldos_recolher_v_8beb_totais` | totais | geguia_contribuicao_previdenciaria_saldos_recolher_valores_compensados | empresa | ✔ |
