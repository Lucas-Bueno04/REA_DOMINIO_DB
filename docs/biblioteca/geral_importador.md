# Módulo `geral_importador`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `geimportador_argumentos_consultar` | consultar | geimportador_argumentos | — | ✔ |
| `geimportador_argumentos_obter` | obter | geimportador_argumentos | codigo_do_argumento | ✔ |
| `geimportador_campos_calculados_consultar` | consultar | geimportador_campos_calculados | — | ✔ |
| `geimportador_campos_calculados_obter` | obter | geimportador_campos_calculados | codigo_da_definicao, codigo_da_tabela, codigo_da_coluna, codigo_do_campo_calculado | ✔ |
| `geimportador_campos_calculados_totais` | totais | geimportador_campos_calculados | — | ✔ |
| `geimportador_colunas_resumo_consultar` | consultar | geimportador_colunas_resumo | — | ✔ |
| `geimportador_colunas_resumo_obter` | obter | geimportador_colunas_resumo | nome_da_tabela, ordem_da_coluna | ✔ |
| `geimportador_colunas_valor_inicial_consultar` | consultar | geimportador_colunas_valor_inicial | — | ✔ |
| `geimportador_colunas_valor_inicial_obter` | obter | geimportador_colunas_valor_inicial | nome_da_tabela, nome_da_coluna | ✔ |
| `geimportador_conjunto_dados_consultar` | consultar | geimportador_conjunto_dados | — | ✔ |
| `geimportador_conjunto_dados_obter` | obter | geimportador_conjunto_dados | codigo_do_conjunto | ✔ |
| `geimportador_conjunto_dados_definicoes_dados_consultar` | consultar | geimportador_conjunto_dados_definicoes_dados | — | ✔ |
| `geimportador_conjunto_dados_definicoes_dados_obter` | obter | geimportador_conjunto_dados_definicoes_dados | codigo_do_conjunto, codigo_da_definicao | ✔ |
| `geimportador_definicao_dados_consultar` | consultar | geimportador_definicao_dados | — | ✔ |
| `geimportador_definicao_dados_obter` | obter | geimportador_definicao_dados | codigo_da_definicao | ✔ |
| `geimportador_definicao_dados_identificacao_consultar` | consultar | geimportador_definicao_dados_identificacao | — | ✔ |
| `geimportador_definicao_dados_identificacao_obter` | obter | geimportador_definicao_dados_identificacao | codigo_da_definicao, codigo_da_identificacao | ✔ |
| `geimportador_definicao_dados_tabelas_consultar` | consultar | geimportador_definicao_dados_tabelas | — | ✔ |
| `geimportador_definicao_dados_tabelas_obter` | obter | geimportador_definicao_dados_tabelas | codigo_da_definicao, codigo_da_tabela | ✔ |
| `geimportador_definicao_dados_tabelas_colunas_consultar` | consultar | geimportador_definicao_dados_tabelas_colunas | — | ✔ |
| `geimportador_definicao_dados_tabelas_colunas_obter` | obter | geimportador_definicao_dados_tabelas_colunas | codigo_da_definicao, codigo_da_tabela, codigo_da_coluna | ✔ |
| `geimportador_equivalencias_consultar` | consultar | geimportador_equivalencias | — | ✔ |
| `geimportador_equivalencias_obter` | obter | geimportador_equivalencias | codigo_do_leiaute, codigo_da_tabela_equivalente | ✔ |
| `geimportador_equivalencias_valores_consultar` | consultar | geimportador_equivalencias_valores | — | ✔ |
| `geimportador_equivalencias_valores_obter` | obter | geimportador_equivalencias_valores | codigo_do_leiaute, codigo_da_tabela_equivalente, codigo_do_valor_da_tabela_equivalente | ✔ |
| `geimportador_leiautes_consultar` | consultar | geimportador_leiautes | — | ✔ |
| `geimportador_leiautes_obter` | obter | geimportador_leiautes | codigo_do_leiaute | ✔ |
| `geimportador_leiautes_registros_consultar` | consultar | geimportador_leiautes_registros | — | ✔ |
| `geimportador_leiautes_registros_obter` | obter | geimportador_leiautes_registros | codigo_do_leiaute, codigo_do_registro | ✔ |
| `geimportador_leiautes_registros_campos_consultar` | consultar | geimportador_leiautes_registros_campos | — | ✔ |
| `geimportador_leiautes_registros_campos_obter` | obter | geimportador_leiautes_registros_campos | codigo_do_leiaute, codigo_do_registro, codigo_do_campo | ✔ |
| `geimportador_manipulacao_caracteres_consultar` | consultar | geimportador_manipulacao_caracteres | — | ✔ |
| `geimportador_manipulacao_caracteres_obter` | obter | geimportador_manipulacao_caracteres | codigo_do_leiaute, codigo_do_registro, codigo_da_manipulacao_de_caracteres | ✔ |
| `geimportador_manipulacao_caracteres_colunas_consultar` | consultar | geimportador_manipulacao_caracteres_colunas | — | ✔ |
| `geimportador_manipulacao_caracteres_colunas_obter` | obter | geimportador_manipulacao_caracteres_colunas | codigo_do_leiaute, codigo_do_registro_do_leiaute, codigo_da_manipulacao_de_caracteres, codigo_da_coluna_da_manipulacao | ✔ |
| `geimportador_manipulacao_caracteres_colunas_totais` | totais | geimportador_manipulacao_caracteres_colunas | — | ✔ |
| `geimportador_regras_consultar` | consultar | geimportador_regras | — | ✔ |
| `geimportador_regras_obter` | obter | geimportador_regras | codigo_do_leiaute, codigo_do_registro, codigo_da_regra | ✔ |
| `geimportador_regras_clausulas_consultar` | consultar | geimportador_regras_clausulas | — | ✔ |
| `geimportador_regras_clausulas_obter` | obter | geimportador_regras_clausulas | codigo_do_leiaute, codigo_do_registro, codigo_da_regra, codigo_da_clausula | ✔ |
| `geimportador_regras_clausulas_condicoes_consultar` | consultar | geimportador_regras_clausulas_condicoes | — | ✔ |
| `geimportador_regras_clausulas_condicoes_obter` | obter | geimportador_regras_clausulas_condicoes | codigo_do_leiaute, codigo_do_registro_do_leiaute, codigo_da_regra, codigo_da_clausula, codigo_da_condicao | ✔ |
| `geimportador_tabelas_disponiveis_consultar` | consultar | geimportador_tabelas_disponiveis | — | ✔ |
| `geimportador_tabelas_disponiveis_obter` | obter | geimportador_tabelas_disponiveis | nome_da_tabela | ✔ |
| `geimportador_tabelas_estrangeiras_consultar` | consultar | geimportador_tabelas_estrangeiras | — | ✔ |
| `geimportador_tabelas_estrangeiras_obter` | obter | geimportador_tabelas_estrangeiras | codigo_do_leiaute, codigo_do_registro_do_leiaute, codigo_da_tabela_estrangeira | ✔ |
| `geimportador_tabelas_estrangeiras_colunas_consultar` | consultar | geimportador_tabelas_estrangeiras_colunas | — | ✔ |
| `geimportador_tabelas_estrangeiras_colunas_obter` | obter | geimportador_tabelas_estrangeiras_colunas | codigo_do_leiaute, codigo_do_registro_do_leiaute, codigo_da_tabela_estrangeira, codigo_da_identificacao, codigo_da_coluna_da_tabela_estrangeira | ✔ |
| `geimportador_tabelas_estrangeiras_identificacoes_consultar` | consultar | geimportador_tabelas_estrangeiras_identificacoes | — | ✔ |
| `geimportador_tabelas_estrangeiras_identificacoes_obter` | obter | geimportador_tabelas_estrangeiras_identificacoes | codigo_do_leiaute, codigo_do_registro_do_leiaute, codigo_da_tabela_estrangeira, codigo_da_identificacao | ✔ |
