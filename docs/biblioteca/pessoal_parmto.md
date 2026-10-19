# Módulo `pessoal_parmto`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `foparmto_alteracao_consultar` | consultar | foparmto_alteracao | empresa | ✔ |
| `foparmto_alteracao_obter` | obter | foparmto_alteracao | empresa, vigencia_da_alteracao | ✔ |
| `foparmto_alteracao_envios_esocial_consultar` | consultar | foparmto_alteracao_envios_esocial | empresa | ✔ |
| `foparmto_alteracao_envios_esocial_obter` | obter | foparmto_alteracao_envios_esocial | empresa, vigencia, codigo_da_empresa_referente_a_foesocial, codigo_do_evento_referente_a_foesocial_d | ✔ |
| `foparmto_configuracao_data_pagamento_consultar` | consultar | foparmto_configuracao_data_pagamento | empresa | ✔ |
| `foparmto_configuracao_data_pagamento_obter` | obter | foparmto_configuracao_data_pagamento | empresa, tipo_de_empregado_1_empregado_2_contribu, tipo_de_calculo, configuracao_para_o_13o_integral_pago_em | ✔ |
| `foparmto_configuracao_data_pagamento_totais` | totais | foparmto_configuracao_data_pagamento | empresa | ✔ |
| `foparmto_natureza_desconto_comp_consultar` | consultar | foparmto_natureza_desconto_comp | empresa | ✔ |
| `foparmto_natureza_desconto_comp_obter` | obter | foparmto_natureza_desconto_comp | empresa, natureza_da_rubrica | ✔ |
