# Módulo `fiscal_simulacao`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `efsimulacao_reforma_tributaria_consultar` | consultar | efsimulacao_reforma_tributaria | empresa | ✔ |
| `efsimulacao_reforma_tributaria_obter` | obter | efsimulacao_reforma_tributaria | empresa, periodo_competencia | ✔ |
| `efsimulacao_reforma_tributaria_ano_consultar` | consultar | efsimulacao_reforma_tributaria_ano | empresa | ✔ |
| `efsimulacao_reforma_tributaria_ano_obter` | obter | efsimulacao_reforma_tributaria_ano | empresa, periodo_competencia, reforma_tributaria_conforme_ano | ✔ |
| `efsimulacao_reforma_tributaria_ano_totais` | totais | efsimulacao_reforma_tributaria_ano | empresa | ✔ |
| `efsimulacao_reforma_tributaria_ano_impostos_consultar` | consultar | efsimulacao_reforma_tributaria_ano_impostos | empresa | ✔ |
| `efsimulacao_reforma_tributaria_ano_impostos_obter` | obter | efsimulacao_reforma_tributaria_ano_impostos | empresa, periodo_competencia, reforma_tributaria_conforme_ano, codigo_imposto | ✔ |
| `efsimulacao_reforma_tributaria_ano_impostos_totais` | totais | efsimulacao_reforma_tributaria_ano_impostos | empresa | ✔ |
| `efsimulacao_reforma_tributaria_ano_iva_consultar` | consultar | efsimulacao_reforma_tributaria_ano_iva | empresa | ✔ |
| `efsimulacao_reforma_tributaria_ano_iva_obter` | obter | efsimulacao_reforma_tributaria_ano_iva | empresa, periodo_competencia, reforma_tributaria_conforme_ano, codigo_imposto_iva, reducao_aliquota, agrupador_de_reducao_de_aliquota | ✔ |
| `efsimulacao_reforma_tributaria_ano_iva_totais` | totais | efsimulacao_reforma_tributaria_ano_iva | empresa | ✔ |
| `efsimulacao_reforma_tributaria_ano_iva_simples_consultar` | consultar | efsimulacao_reforma_tributaria_ano_iva_simples | empresa | ✔ |
| `efsimulacao_reforma_tributaria_ano_iva_simples_obter` | obter | efsimulacao_reforma_tributaria_ano_iva_simples | empresa, periodo_competencia, reforma_tributaria_conforme_ano, codigo_imposto_iva | ✔ |
| `efsimulacao_reforma_tributaria_ano_iva_simples_totais` | totais | efsimulacao_reforma_tributaria_ano_iva_simples | empresa | ✔ |
| `efsimulacao_reforma_tributaria_base_por_acumulador_consultar` | consultar | efsimulacao_reforma_tributaria_base_por_acumulador | empresa | ✔ |
| `efsimulacao_reforma_tributaria_base_por_acumulador_obter` | obter | efsimulacao_reforma_tributaria_base_por_acumulador | empresa, periodo_competencia, filial, codigo_acumulador, tipo_movimento_ce_credito_entrada_de_deb | ✔ |
| `efsimulacao_reforma_tributaria_base_por_acumulador_totais` | totais | efsimulacao_reforma_tributaria_base_por_acumulador | empresa | ✔ |
| `efsimulacao_reforma_tributaria_base_por_regime_fo_81d3_consultar` | consultar | efsimulacao_reforma_tributaria_base_por_regime_fornecedor | empresa | ✔ |
| `efsimulacao_reforma_tributaria_base_por_regime_fornecedor_obter` | obter | efsimulacao_reforma_tributaria_base_por_regime_fornecedor | empresa, periodo_competencia, filial, cliente_ou_fornecedor, regime_fornecedor, tipo_movimento_ce_credito_entrada_ds_deb | ✔ |
| `efsimulacao_reforma_tributaria_base_por_regime_fornecedor_totais` | totais | efsimulacao_reforma_tributaria_base_por_regime_fornecedor | empresa | ✔ |
| `efsimulacao_reforma_tributaria_cfop_sem_credito_consultar` | consultar | efsimulacao_reforma_tributaria_cfop_sem_credito | empresa | ✔ |
| `efsimulacao_reforma_tributaria_cfop_sem_credito_obter` | obter | efsimulacao_reforma_tributaria_cfop_sem_credito | empresa, sequencial_configuracao_cfop | ✔ |
| `efsimulacao_reforma_tributaria_impostos_consultar` | consultar | efsimulacao_reforma_tributaria_impostos | empresa | ✔ |
| `efsimulacao_reforma_tributaria_impostos_obter` | obter | efsimulacao_reforma_tributaria_impostos | empresa, periodo_competencia, codigo_imposto | ✔ |
| `efsimulacao_reforma_tributaria_impostos_totais` | totais | efsimulacao_reforma_tributaria_impostos | empresa | ✔ |
| `efsimulacao_reforma_tributaria_impostos_simples_n_f42b_consultar` | consultar | efsimulacao_reforma_tributaria_impostos_simples_nacional | empresa | ✔ |
| `efsimulacao_reforma_tributaria_impostos_simples_nacional_obter` | obter | efsimulacao_reforma_tributaria_impostos_simples_nacional | empresa, periodo_competencia, codigo_imposto | ✔ |
| `efsimulacao_reforma_tributaria_impostos_simples_nacional_totais` | totais | efsimulacao_reforma_tributaria_impostos_simples_nacional | empresa | ✔ |
