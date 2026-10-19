# Módulo `fiscal_piscofins`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `efpiscofins_apropriacao_direta_credito_consultar` | consultar | efpiscofins_apropriacao_direta_credito | empresa | ✔ |
| `efpiscofins_apropriacao_direta_credito_obter` | obter | efpiscofins_apropriacao_direta_credito | empresa, sequencial | ✔ |
| `efpiscofins_apropriacao_direta_credito_vigencia_consultar` | consultar | efpiscofins_apropriacao_direta_credito_vigencia | empresa | ✔ |
| `efpiscofins_apropriacao_direta_credito_vigencia_obter` | obter | efpiscofins_apropriacao_direta_credito_vigencia | empresa, sequencial, vigencia | ✔ |
| `efpiscofins_apropriacao_direta_credito_vigencia_totais` | totais | efpiscofins_apropriacao_direta_credito_vigencia | empresa | ✔ |
| `efpiscofins_outros_saldo_retencao_consultar` | consultar | efpiscofins_outros_saldo_retencao | empresa | ✔ |
| `efpiscofins_outros_saldo_retencao_obter` | obter | efpiscofins_outros_saldo_retencao | empresa, codigo_sequencial | ✔ |
| `efpiscofins_outros_saldo_retencao_totais` | totais | efpiscofins_outros_saldo_retencao | empresa | ✔ |
| `efpiscofins_outros_saldo_retencao_item_consultar` | consultar | efpiscofins_outros_saldo_retencao_item | empresa | ✔ |
| `efpiscofins_outros_saldo_retencao_item_obter` | obter | efpiscofins_outros_saldo_retencao_item | empresa, codigo_sequencial, periodo_da_retencao, natureza_da_retencao | ✔ |
| `efpiscofins_outros_saldo_retencao_item_totais` | totais | efpiscofins_outros_saldo_retencao_item | empresa | ✔ |
