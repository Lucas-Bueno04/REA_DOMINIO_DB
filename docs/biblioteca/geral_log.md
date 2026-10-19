# Módulo `geral_log`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `gelog_erro_atualizacao_banco_consultar` | consultar | gelog_erro_atualizacao_banco | — | ✔ |
| `gelog_erro_atualizacao_banco_obter` | obter | gelog_erro_atualizacao_banco | i_numero_erro | ✔ |
| `gelog_geral_consultar` | consultar | gelog_geral | — | ✔ |
| `gelog_geral_obter` | obter | gelog_geral | guid_do_registro | ✔ |
| `gelog_utilitarios_consultar` | consultar | gelog_utilitarios | empresa | ✔ |
| `gelog_utilitarios_obter` | obter | gelog_utilitarios | empresa, sequencial | ✔ |
| `gelog_utilitarios_nota_consultar` | consultar | gelog_utilitarios_nota | empresa | ✔ |
| `gelog_utilitarios_nota_obter` | obter | gelog_utilitarios_nota | empresa, sequencial, tipo_da_nota_1_entrada_2_saida_3_servico, codigo_da_nota | ✔ |
