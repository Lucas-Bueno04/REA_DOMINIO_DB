# Módulo `pessoal_atendimento`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `foatendimento_acoes_consultar` | consultar | foatendimento_acoes | empresa | ✔ |
| `foatendimento_acoes_obter` | obter | foatendimento_acoes | empresa, codigo_sequencial_da_acao, codigo_do_empregado, codigo_da_empresa_do_atendimento, tipo_da_acao_1_inserir_2_excluir_3_desab | ✔ |
| `foatendimento_eventos_consultar` | consultar | foatendimento_eventos | empresa | ✔ |
| `foatendimento_eventos_obter` | obter | foatendimento_eventos | empresa, codigo_do_atendimento | ✔ |
| `foatendimento_eventos_backup_consultar` | consultar | foatendimento_eventos_backup | empresa | ✔ |
| `foatendimento_eventos_backup_obter` | obter | foatendimento_eventos_backup | empresa, codigo_do_atendimento | ✔ |
| `foatendimento_eventos_itens_consultar` | consultar | foatendimento_eventos_itens | empresa | ✔ |
| `foatendimento_eventos_itens_obter` | obter | foatendimento_eventos_itens | empresa, codigo_do_atendimento_referente_a_foaten, codigo_do_evento_referente_a_foeventos | ✔ |
| `foatendimento_eventos_itens_backup_consultar` | consultar | foatendimento_eventos_itens_backup | empresa | ✔ |
| `foatendimento_eventos_itens_backup_obter` | obter | foatendimento_eventos_itens_backup | empresa, i_atendimento_evento, i_eventos | ✔ |
| `foatendimento_eventos_itens_filiais_consultar` | consultar | foatendimento_eventos_itens_filiais | empresa | ✔ |
| `foatendimento_eventos_itens_filiais_obter` | obter | foatendimento_eventos_itens_filiais | empresa, codigo_do_atendimento_referente_a_foaten, codigo_do_evento_referente_a_foatendimen, codigo_filial | ✔ |
| `foatendimento_eventos_itens_filiais_backup_consultar` | consultar | foatendimento_eventos_itens_filiais_backup | empresa | ✔ |
| `foatendimento_eventos_itens_filiais_backup_obter` | obter | foatendimento_eventos_itens_filiais_backup | empresa, i_atendimento_evento, i_eventos, i_filiais | ✔ |
| `foatendimento_servicos_empresa_onvio_consultar` | consultar | foatendimento_servicos_empresa_onvio | empresa | ✔ |
| `foatendimento_servicos_empresa_onvio_obter` | obter | foatendimento_servicos_empresa_onvio | empresa, sequencial | ✔ |
| `foatendimento_sindicato_empresa_onvio_consultar` | consultar | foatendimento_sindicato_empresa_onvio | — | ✔ |
| `foatendimento_sindicato_empresa_onvio_obter` | obter | foatendimento_sindicato_empresa_onvio | sequencial | ✔ |
| `foatendimento_solicitacoes_abertas_rubrica_consultar` | consultar | foatendimento_solicitacoes_abertas_rubrica | empresa | ✔ |
| `foatendimento_solicitacoes_abertas_rubrica_obter` | obter | foatendimento_solicitacoes_abertas_rubrica | empresa, rubrica | ✔ |
