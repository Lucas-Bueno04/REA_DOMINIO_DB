# Módulo `geral_raexecutar`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `geraexecutar_empregados_consultar` | consultar | geraexecutar_empregados | empresa | ✔ |
| `geraexecutar_empregados_obter` | obter | geraexecutar_empregados | empresa, codigo_da_execucao, codigo_do_sistema, codigo_do_empregado | ✔ |
| `geraexecutar_empresas_consultar` | consultar | geraexecutar_empresas | empresa | ✔ |
| `geraexecutar_empresas_obter` | obter | geraexecutar_empresas | empresa, codigo_da_execucao, codigo_do_sistema | ✔ |
| `geraexecutar_empresas_opcoes_contabilidade_consultar` | consultar | geraexecutar_empresas_opcoes_contabilidade | empresa | ✔ |
| `geraexecutar_empresas_opcoes_contabilidade_obter` | obter | geraexecutar_empresas_opcoes_contabilidade | empresa, codigo_da_execucao, codigo_do_sistema, processo_da_contabilidade_1_importacao_e, campo_da_opcao_da_contabilidade | ✔ |
| `geraexecutar_empresas_opcoes_honorarios_consultar` | consultar | geraexecutar_empresas_opcoes_honorarios | empresa | ✔ |
| `geraexecutar_empresas_opcoes_honorarios_obter` | obter | geraexecutar_empresas_opcoes_honorarios | empresa, codigo_da_execucao, codigo_do_sistema, id_da_opcao_do_honorarios | ✔ |
| `geraexecutar_rotinas_consultar` | consultar | geraexecutar_rotinas | — | ✔ |
| `geraexecutar_rotinas_obter` | obter | geraexecutar_rotinas | codigo_da_execucao, codigo_do_sistema, codigo_da_rotina | ✔ |
| `geraexecutar_semanas_consultar` | consultar | geraexecutar_semanas | — | ✔ |
| `geraexecutar_semanas_obter` | obter | geraexecutar_semanas | codigo_da_rotina_automatica_fk_geraexecu, codigo_do_sistema_fk_geraexecutar | ✔ |
