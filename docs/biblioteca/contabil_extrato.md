# Módulo `contabil_extrato`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `ctextrato_bancario_configuracao_consultar` | consultar | ctextrato_bancario_configuracao | empresa | ✔ |
| `ctextrato_bancario_configuracao_obter` | obter | ctextrato_bancario_configuracao | empresa, codigo | ✔ |
| `ctextrato_bancario_configuracao_iceberg_consultar` | consultar | ctextrato_bancario_configuracao_iceberg | empresa | ✔ |
| `ctextrato_bancario_configuracao_iceberg_obter` | obter | ctextrato_bancario_configuracao_iceberg | empresa, codigo_da_transacao | ✔ |
| `ctextrato_bancario_configuracao_iceberg_detalhe_consultar` | consultar | ctextrato_bancario_configuracao_iceberg_detalhe | empresa | ✔ |
| `ctextrato_bancario_configuracao_iceberg_detalhe_obter` | obter | ctextrato_bancario_configuracao_iceberg_detalhe | empresa, codigo_da_transacao, sequencial_do_detalhe | ✔ |
| `ctextrato_bancario_configuracao_iceberg_outros_consultar` | consultar | ctextrato_bancario_configuracao_iceberg_outros | empresa | ✔ |
| `ctextrato_bancario_configuracao_iceberg_outros_obter` | obter | ctextrato_bancario_configuracao_iceberg_outros | empresa, tipo_de_transacao | ✔ |
| `ctextrato_bancario_lancamento_consultar` | consultar | ctextrato_bancario_lancamento | empresa | ✔ |
| `ctextrato_bancario_lancamento_obter` | obter | ctextrato_bancario_lancamento | empresa, codigo | ✔ |
| `ctextrato_bancario_lancamento_totais` | totais | ctextrato_bancario_lancamento | empresa | ✔ |
| `ctextrato_bancario_lancamento_iceberg_consultar` | consultar | ctextrato_bancario_lancamento_iceberg | empresa | ✔ |
| `ctextrato_bancario_lancamento_iceberg_obter` | obter | ctextrato_bancario_lancamento_iceberg | empresa, codigo_da_empresa_do_lancamento, sequencial_do_extrato, sequencial | ✔ |
| `ctextrato_bancario_lancamento_iceberg_totais` | totais | ctextrato_bancario_lancamento_iceberg | empresa | ✔ |
| `ctextrato_bancario_lancamento_iceberg_lancto_consultar` | consultar | ctextrato_bancario_lancamento_iceberg_lancto | empresa | ✔ |
| `ctextrato_bancario_lancamento_iceberg_lancto_obter` | obter | ctextrato_bancario_lancamento_iceberg_lancto | empresa, codigo_da_empresa_do_lancamento, codigo_extrato, sequencial_do_item, numero_do_lancamento_contabil, codigo_do_lote | ✔ |
| `ctextrato_bancario_lancamento_iceberg_lancto_totais` | totais | ctextrato_bancario_lancamento_iceberg_lancto | empresa | ✔ |
| `ctextrato_bancario_lancamento_item_consultar` | consultar | ctextrato_bancario_lancamento_item | empresa | ✔ |
| `ctextrato_bancario_lancamento_item_obter` | obter | ctextrato_bancario_lancamento_item | empresa, codigo_extrato, sequencial_do_item | ✔ |
| `ctextrato_bancario_lancamento_item_totais` | totais | ctextrato_bancario_lancamento_item | empresa | ✔ |
| `ctextrato_bancario_lancamento_item_lancto_consultar` | consultar | ctextrato_bancario_lancamento_item_lancto | empresa | ✔ |
| `ctextrato_bancario_lancamento_item_lancto_obter` | obter | ctextrato_bancario_lancamento_item_lancto | empresa, codigo_extrato, sequencial_do_item, numero_do_lancamento_contabil | ✔ |
| `ctextrato_bancario_transacoes_iceberg_consultar` | consultar | ctextrato_bancario_transacoes_iceberg | — | ✔ |
| `ctextrato_bancario_transacoes_iceberg_obter` | obter | ctextrato_bancario_transacoes_iceberg | codigo_da_transacao | ✔ |
| `ctextrato_bancario_transacoes_iceberg_tarifa_consultar` | consultar | ctextrato_bancario_transacoes_iceberg_tarifa | — | ✔ |
| `ctextrato_bancario_transacoes_iceberg_tarifa_obter` | obter | ctextrato_bancario_transacoes_iceberg_tarifa | codigo_da_tarifa | ✔ |
