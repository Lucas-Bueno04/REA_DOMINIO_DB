# Módulo `processos_vinculo`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `pcvinculo_processo_consultar` | consultar | pcvinculo_processo | empresa | ✔ |
| `pcvinculo_processo_obter` | obter | pcvinculo_processo | empresa, codigo | ✔ |
| `pcvinculo_processo_atividade_consultar` | consultar | pcvinculo_processo_atividade | — | ✔ |
| `pcvinculo_processo_atividade_obter` | obter | pcvinculo_processo_atividade | codigo_do_vinculo, sequencial | ✔ |
| `pcvinculo_processo_atividade_responsavel_consultar` | consultar | pcvinculo_processo_atividade_responsavel | — | ✔ |
| `pcvinculo_processo_atividade_responsavel_obter` | obter | pcvinculo_processo_atividade_responsavel | codigo_do_vinculo, sequencial_da_atividade, sequencial | ✔ |
| `pcvinculo_processo_responsavel_consultar` | consultar | pcvinculo_processo_responsavel | — | ✔ |
| `pcvinculo_processo_responsavel_obter` | obter | pcvinculo_processo_responsavel | codigo_do_vinculo, sequencial | ✔ |
