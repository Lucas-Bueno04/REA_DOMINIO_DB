# Módulo `pessoal_eventos`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `foeventos_afast_consultar` | consultar | foeventos_afast | empresa | ✔ |
| `foeventos_afast_obter` | obter | foeventos_afast | empresa, codigo_do_evento, situacao | ✔ |
| `foeventos_afastdef_consultar` | consultar | foeventos_afastdef | — | ✔ |
| `foeventos_afastdef_obter` | obter | foeventos_afastdef | codigo_do_evento, situacao | ✔ |
| `foeventos_alteracao_consultar` | consultar | foeventos_alteracao | empresa | ✔ |
| `foeventos_alteracao_obter` | obter | foeventos_alteracao | empresa, codigo_da_rubrica, vigencia_da_alteracao | ✔ |
| `foeventos_alteracao_controle_envio_esocial_consultar` | consultar | foeventos_alteracao_controle_envio_esocial | empresa | ✔ |
| `foeventos_alteracao_controle_envio_esocial_obter` | obter | foeventos_alteracao_controle_envio_esocial | empresa, codigo_da_rubrica, vigencia_da_alteracao, codigo_da_empresa_de_envio_do_evento_ao | ✔ |
| `foeventos_alteracao_controle_envio_esocial_envios_db2f_consultar` | consultar | foeventos_alteracao_controle_envio_esocial_envios_esocial | empresa | ✔ |
| `foeventos_alteracao_controle_envio_esocial_envios_esocial_obter` | obter | foeventos_alteracao_controle_envio_esocial_envios_esocial | empresa, codigo_do_evento, vigencia, codigo_da_empresa_de_envio_do_evento_ao, codigo_da_empresa_referente_a_foesocial, codigo_do_evento_referente_a_foesocial_d | ✔ |
| `foeventos_alteracao_dados_cadastrais_consultar` | consultar | foeventos_alteracao_dados_cadastrais | empresa | ✔ |
| `foeventos_alteracao_dados_cadastrais_obter` | obter | foeventos_alteracao_dados_cadastrais | empresa, codigo_da_rubrica, vigencia_da_alteracao | ✔ |
| `foeventos_alteracao_dados_cadastrais_totais` | totais | foeventos_alteracao_dados_cadastrais | empresa | ✔ |
| `foeventos_ordem_calculo_consultar` | consultar | foeventos_ordem_calculo | empresa | ✔ |
| `foeventos_ordem_calculo_obter` | obter | foeventos_ordem_calculo | empresa, codigo_dos_eventos | ✔ |
