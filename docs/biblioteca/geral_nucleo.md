# Módulo `geral_nucleo`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `geanalytics_consultar` | consultar | geanalytics | — | ✔ |
| `geanalytics_obter` | obter | geanalytics | codigo_sequencial_do_registro | ✔ |
| `geatendimentoacoes_consultar` | consultar | geatendimentoacoes | empresa | ✔ |
| `geatendimentoacoes_obter` | obter | geatendimentoacoes | empresa, codigo | ✔ |
| `geatendimentoacoes_totais` | totais | geatendimentoacoes | empresa | ✔ |
| `geatendimentocolunasbaixar_consultar` | consultar | geatendimentocolunasbaixar | — | ✔ |
| `geatendimentocolunasbaixar_obter` | obter | geatendimentocolunasbaixar | codigo | ✔ |
| `geatendimentocolunasbaixar_totais` | totais | geatendimentocolunasbaixar | — | ✔ |
| `geatendimentocolunastransferir_consultar` | consultar | geatendimentocolunastransferir | — | ✔ |
| `geatendimentocolunastransferir_obter` | obter | geatendimentocolunastransferir | codigo | ✔ |
| `geatendimentocolunastransferir_totais` | totais | geatendimentocolunastransferir | — | ✔ |
| `geatendimentogrupoexecucao_consultar` | consultar | geatendimentogrupoexecucao | — | ✔ |
| `geatendimentogrupoexecucao_obter` | obter | geatendimentogrupoexecucao | codigo | ✔ |
| `geatendimentolog_consultar` | consultar | geatendimentolog | — | ✔ |
| `geatendimentolog_obter` | obter | geatendimentolog | codigo | ✔ |
| `geatendimentologingestta_consultar` | consultar | geatendimentologingestta | — | ✔ |
| `geatendimentologingestta_obter` | obter | geatendimentologingestta | codigo | ✔ |
| `geatendimentosequencialgrupo_consultar` | consultar | geatendimentosequencialgrupo | — | ✔ |
| `geatendimentosequencialgrupo_obter` | obter | geatendimentosequencialgrupo | codigo | ✔ |
| `geatendimentotabelasbaixar_consultar` | consultar | geatendimentotabelasbaixar | — | ✔ |
| `geatendimentotabelasbaixar_obter` | obter | geatendimentotabelasbaixar | codigo | ✔ |
| `geatendimentotabelastransferir_consultar` | consultar | geatendimentotabelastransferir | — | ✔ |
| `geatendimentotabelastransferir_obter` | obter | geatendimentotabelastransferir | codigo | ✔ |
| `geatividades_consultar` | consultar | geatividades | empresa | ✔ |
| `geatividades_obter` | obter | geatividades | empresa, codigo_sequencial_das_atividades | ✔ |
| `gecae_consultar` | consultar | gecae | — | ✔ |
| `gecae_obter` | obter | gecae | codigo | ✔ |
| `geclassificacoes_consultar` | consultar | geclassificacoes | — | ✔ |
| `geclassificacoes_obter` | obter | geclassificacoes | codigo | ✔ |
| `gecmdexecutado_consultar` | consultar | gecmdexecutado | — | ✔ |
| `gecmdexecutado_obter` | obter | gecmdexecutado | sequencial | ✔ |
| `gecnae_consultar` | consultar | gecnae | — | ✔ |
| `gecnae_obter` | obter | gecnae | codigo_cnae | ✔ |
| `geconexoesativas_consultar` | consultar | geconexoesativas | — | ✔ |
| `geconexoesativas_obter` | obter | geconexoesativas | i_conexoesativas | ✔ |
| `gecontador_consultar` | consultar | gecontador | — | ✔ |
| `gecontador_obter` | obter | gecontador | codigo | ✔ |
| `geconversao_consultar` | consultar | geconversao | — | ✔ |
| `geconversao_obter` | obter | geconversao | convertido | ✔ |
| `gedicas_consultar` | consultar | gedicas | — | ✔ |
| `gedicas_obter` | obter | gedicas | codigo_do_sistema, numero_da_dica | ✔ |
| `gedicasconf_consultar` | consultar | gedicasconf | — | ✔ |
| `gedicasconf_obter` | obter | gedicasconf | usuario | ✔ |
| `gedicasusuarios_consultar` | consultar | gedicasusuarios | — | ✔ |
| `gedicasusuarios_obter` | obter | gedicasusuarios | i_usuario, numero_da_dica, codigo_do_sistema | ✔ |
| `geestacoes_consultar` | consultar | geestacoes | — | ✔ |
| `geestacoes_obter` | obter | geestacoes | endereco_mac_da_placa_de_rede | ✔ |
| `geestacoes_totais` | totais | geestacoes | — | ✔ |
| `geiaconfig_consultar` | consultar | geiaconfig | — | ✔ |
| `geiaconfig_obter` | obter | geiaconfig | codigo_agent | ✔ |
| `geindice_consultar` | consultar | geindice | — | ✔ |
| `geindice_obter` | obter | geindice | codigo | ✔ |
| `geinformacao_consultar` | consultar | geinformacao | empresa | ✔ |
| `geinformacao_obter` | obter | geinformacao | empresa, competencia | ✔ |
| `geintegra_consultar` | consultar | geintegra | — | ✔ |
| `geintegra_obter` | obter | geintegra | sequencial | ✔ |
| `gemenufavoritos_consultar` | consultar | gemenufavoritos | — | ✔ |
| `gemenufavoritos_obter` | obter | gemenufavoritos | i_modulo, i_confusuario, i_menufavorito, tipo_usuario | ✔ |
| `gemodulos_consultar` | consultar | gemodulos | — | ✔ |
| `gemodulos_obter` | obter | gemodulos | i_modulo | ✔ |
| `geprareas_consultar` | consultar | geprareas | — | ✔ |
| `geprareas_obter` | obter | geprareas | id | ✔ |
| `geprassuntos_consultar` | consultar | geprassuntos | — | ✔ |
| `geprassuntos_obter` | obter | geprassuntos | id | ✔ |
| `geprop_consultar` | consultar | geprop | — | ✔ |
| `geprop_obter` | obter | geprop | nome_pro | ✔ |
| `geraexecutar_consultar` | consultar | geraexecutar | — | ✔ |
| `geraexecutar_obter` | obter | geraexecutar | codigo_da_execucao, codigo_do_sistema | ✔ |
| `geraexecutar_totais` | totais | geraexecutar | — | ✔ |
| `gerarotinas_consultar` | consultar | gerarotinas | — | ✔ |
| `gerarotinas_obter` | obter | gerarotinas | codigo_da_rotina, codigo_do_sistema | ✔ |
| `gerepresentante_consultar` | consultar | gerepresentante | — | ✔ |
| `gerepresentante_obter` | obter | gerepresentante | codigo_do_cadastro_de_representante | ✔ |
| `geresponsavel_consultar` | consultar | geresponsavel | empresa | ✔ |
| `geresponsavel_obter` | obter | geresponsavel | empresa, codigo | ✔ |
| `gescp_consultar` | consultar | gescp | empresa | ✔ |
| `gescp_obter` | obter | gescp | empresa, sequencial_do_scp | ✔ |
| `geselecao_consultar` | consultar | geselecao | empresa | ✔ |
| `geselecao_obter` | obter | geselecao | empresa, sequencial_da_selecao, sequencial_do_tipo_de_selecao | ✔ |
| `geselemp_consultar` | consultar | geselemp | — | ✔ |
| `geselemp_obter` | obter | geselemp | nome_da_selecao | ✔ |
