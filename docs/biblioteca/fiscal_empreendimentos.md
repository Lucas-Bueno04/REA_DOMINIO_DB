# Módulo `fiscal_empreendimentos`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `efempreendimentos_imobiliarios_consultar` | consultar | efempreendimentos_imobiliarios | empresa | ✔ |
| `efempreendimentos_imobiliarios_obter` | obter | efempreendimentos_imobiliarios | empresa, codigo_do_empreendimento | ✔ |
| `efempreendimentos_imobiliarios_totais` | totais | efempreendimentos_imobiliarios | empresa | ✔ |
| `efempreendimentos_imobiliarios_contratos_venda_consultar` | consultar | efempreendimentos_imobiliarios_contratos_venda | empresa | ✔ |
| `efempreendimentos_imobiliarios_contratos_venda_obter` | obter | efempreendimentos_imobiliarios_contratos_venda | empresa, codigo_do_contrato | ✔ |
| `efempreendimentos_imobiliarios_contratos_venda_totais` | totais | efempreendimentos_imobiliarios_contratos_venda | empresa | ✔ |
| `efempreendimentos_imobiliarios_contratos_venda_cliente_consultar` | consultar | efempreendimentos_imobiliarios_contratos_venda_cliente | empresa | ✔ |
| `efempreendimentos_imobiliarios_contratos_venda_cliente_obter` | obter | efempreendimentos_imobiliarios_contratos_venda_cliente | empresa, codigo_do_contrato, sequencial | ✔ |
| `efempreendimentos_imobiliarios_contratos_venda_cl_25eb_consultar` | consultar | efempreendimentos_imobiliarios_contratos_venda_cliente_alteracao | empresa | ✔ |
| `efempreendimentos_imobiliarios_contratos_venda_client_25eb_obter` | obter | efempreendimentos_imobiliarios_contratos_venda_cliente_alteracao | empresa, codigo_do_contrato_imobiliario, sequencial_da_alteracao, data_de_alteracao | ✔ |
| `efempreendimentos_imobiliarios_contratos_venda_lancto_consultar` | consultar | efempreendimentos_imobiliarios_contratos_venda_lancto | empresa | ✔ |
| `efempreendimentos_imobiliarios_contratos_venda_lancto_obter` | obter | efempreendimentos_imobiliarios_contratos_venda_lancto | empresa, numero_do_lancamento, empresa_do_contrato, codigo_do_contrato | ✔ |
| `efempreendimentos_imobiliarios_contratos_venda_pa_7397_consultar` | consultar | efempreendimentos_imobiliarios_contratos_venda_pagamentos | empresa | ✔ |
| `efempreendimentos_imobiliarios_contratos_venda_pagamentos_obter` | obter | efempreendimentos_imobiliarios_contratos_venda_pagamentos | empresa, codigo_do_contrato, codigo_da_parcela, codigo_do_pagamento | ✔ |
| `efempreendimentos_imobiliarios_contratos_venda_pagamentos_totais` | totais | efempreendimentos_imobiliarios_contratos_venda_pagamentos | empresa | ✔ |
| `efempreendimentos_imobiliarios_contratos_venda_pa_d1cc_consultar` | consultar | efempreendimentos_imobiliarios_contratos_venda_parcelas | empresa | ✔ |
| `efempreendimentos_imobiliarios_contratos_venda_parcelas_obter` | obter | efempreendimentos_imobiliarios_contratos_venda_parcelas | empresa, codigo_do_contrato, codigo_da_parcela | ✔ |
| `efempreendimentos_imobiliarios_contratos_venda_parcelas_totais` | totais | efempreendimentos_imobiliarios_contratos_venda_parcelas | empresa | ✔ |
| `efempreendimentos_imobiliarios_contratos_venda_un_4406_consultar` | consultar | efempreendimentos_imobiliarios_contratos_venda_unidades | empresa | ✔ |
| `efempreendimentos_imobiliarios_contratos_venda_unidades_obter` | obter | efempreendimentos_imobiliarios_contratos_venda_unidades | empresa, codigo_do_contrato, codigo_da_unidade | ✔ |
| `efempreendimentos_imobiliarios_contratos_venda_unidades_totais` | totais | efempreendimentos_imobiliarios_contratos_venda_unidades | empresa | ✔ |
| `efempreendimentos_imobiliarios_impostos_debito_consultar` | consultar | efempreendimentos_imobiliarios_impostos_debito | empresa | ✔ |
| `efempreendimentos_imobiliarios_impostos_debito_obter` | obter | efempreendimentos_imobiliarios_impostos_debito | empresa, codigo_do_empreendimento, codigo_do_imposto | ✔ |
| `efempreendimentos_imobiliarios_unidades_consultar` | consultar | efempreendimentos_imobiliarios_unidades | empresa | ✔ |
| `efempreendimentos_imobiliarios_unidades_obter` | obter | efempreendimentos_imobiliarios_unidades | empresa, codigo_do_empreendimento, codigo_da_unidade | ✔ |
| `efempreendimentos_imobiliarios_vigencia_consultar` | consultar | efempreendimentos_imobiliarios_vigencia | empresa | ✔ |
| `efempreendimentos_imobiliarios_vigencia_obter` | obter | efempreendimentos_imobiliarios_vigencia | empresa, codigo_do_empreendimento, vigencia | ✔ |
| `efempreendimentos_imobiliarios_vigencia_totais` | totais | efempreendimentos_imobiliarios_vigencia | empresa | ✔ |
| `efempreendimentos_imobiliarios_vigencia_impostos__d80b_consultar` | consultar | efempreendimentos_imobiliarios_vigencia_impostos_debito | empresa | ✔ |
| `efempreendimentos_imobiliarios_vigencia_impostos_debito_obter` | obter | efempreendimentos_imobiliarios_vigencia_impostos_debito | empresa, codigo_do_empreendimento, vigencia, codigo_do_imposto | ✔ |
