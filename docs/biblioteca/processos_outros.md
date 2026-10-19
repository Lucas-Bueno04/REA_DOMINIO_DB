# Módulo `processos_outros`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `pccampos_localizar_comprovante_consultar` | consultar | pccampos_localizar_comprovante | — | ✔ |
| `pccampos_localizar_comprovante_obter` | obter | pccampos_localizar_comprovante | sequencial | ✔ |
| `pcmovimento_atividade_consultar` | consultar | pcmovimento_atividade | — | ✔ |
| `pcmovimento_atividade_obter` | obter | pcmovimento_atividade | codigo_do_vinculo, sequencial_da_atividade, sequencial | ✔ |
| `pcmovimento_atividade_responsavel_consultar` | consultar | pcmovimento_atividade_responsavel | — | ✔ |
| `pcmovimento_atividade_responsavel_obter` | obter | pcmovimento_atividade_responsavel | codigo_do_vinculo, sequencial_da_atividade, sequencial_do_movimento, sequencial_do_responsavel | ✔ |
| `pcprocesso_atividade_consultar` | consultar | pcprocesso_atividade | — | ✔ |
| `pcprocesso_atividade_obter` | obter | pcprocesso_atividade | codigo_do_processo, sequencial | ✔ |
| `pcprocesso_responsavel_consultar` | consultar | pcprocesso_responsavel | — | ✔ |
| `pcprocesso_responsavel_obter` | obter | pcprocesso_responsavel | codigo_do_processo, codigo_do_responsavel, responsavel_tipo | ✔ |
| `pcresponsavel_empresa_consultar` | consultar | pcresponsavel_empresa | empresa | ✔ |
| `pcresponsavel_empresa_obter` | obter | pcresponsavel_empresa | empresa, codigo_do_responsavel, responsavel_tipo | ✔ |
