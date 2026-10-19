# Módulo `parametros_empresa`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `parametro_contabil_consultar` | consultar | ctparmto | empresa | ✔ |
| `parametro_folha_consultar` | consultar | foparmto | empresa | ✔ |
| `parametro_folha_totais` | totais | foparmto | empresa | ✔ |

## `parametro_contabil_consultar`

Parâmetros da contabilidade por empresa — tabela ctparmto (módulo parametros_empresa, ~1.441 linhas).
O QUE É: Configuração contábil da empresa: máscara e origem do plano de contas, regime (fiscal/caixa/gerencial), período de trabalho, centro de custo, contas de lucro e prejuízo e transferência do resultado. 1.441 linhas, uma por empresa. Usa 39 das 249 colunas.
COMENTÁRIO DO BANCO SOBRE A TABELA: Parametros
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: plano_origem_empresa, regime_contabil, compartilha_plano. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: regime_contabil, mascara_plano_contas, mascara_gerencial, mascara_relatorios, informar_conta_por, inicio_lancamentos, periodo_trabalho_inicio, periodo_trabalho_fim, acao_fora_do_periodo, relatorios_inicio, relatorios_fim, plano_origem_empresa, compartilha_plano, historico_origem_empresa, compartilha_historicos, centraliza_matriz_filiais, informa_filial_no_lancamento, contabilidade_por_centro_custo, rateio_centro_custo_por_filial, usa_dre, usa_dlpa, usa_doar, historico_obrigatorio, permite_lancamento_valor_zero, permite_cadastrar_contas, conta_inicial, conta_final, permite_cadastrar_historicos, historico_inicial, historico_final, conta_caixa, informa_conta_caixa, conta_patrimonio_liquido, conta_destino_resultado, conta_lucro_periodo, conta_prejuizo_periodo, transfere_resultado_automaticamente, altera_lancamentos_outros_sistemas, utiliza_dominio_cliente. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): empresa_nome.
EXEMPLO COM DADOS: a empresa 896 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Uma linha por empresa (1.441 empresas, 1.441 linhas). Regime contábil 1 (fiscal) em 1.440 e 3 (gerencial) em 1; conta informada por código (C) em 1.440 e por máscara (M) em 1. | Plano de contas: `plano_origem_empresa` é nulo em 1.354 empresas (plano próprio) e aponta para OUTRA empresa em 87; nenhuma aponta para si mesma. 57 empresas marcam compartilha_plano = S. Para resolver as contas de uma empresa use a empresa do plano (é o `plano_empresa` do lançamento). | Máscara do plano de contas: 9.9.9.99.999999 em 1.378 empresas; 9.9.9.99.9999 em 30; 9.9.99.999.999 em 17; 9.9.99.99.999 em 7; 9.9.9.99.99.999 em 6; 9.99.99.999999 em 2. | Período de trabalho: 1.273 empresas têm data final (de 2020-04-30 a 2030-12-31; datas muito futuras provavelmente significam 'sem limite'); fora do período o sistema bloqueia (N) em 971 empresas e libera (L) em 470; nenhuma usa avisar (A). | Demonstrações e fechamento: usa DRE (S) em 1.403 empresas, DLPA em 1.336, histórico obrigatório em 1.418 e transferência automática do resultado para o patrimônio líquido em 1.401; 14 empresas têm tudo isso desligado. (+1 regras: veja descrever_entidade)
POSSÍVEIS DADOS PESSOAIS/FINANCEIROS (os dados saem em claro; devolva só o que a pergunta exigir): conta_patrimonio_liquido.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `plano_origem_empresa`: Filtra codi_pad (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Origem do Plano de Contas)
- `regime_contabil`: Filtra ctcx_par (tinyint). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Fiscal, 2=Caixa, 3=Gerencial (Usar como (1=Fiscal, 2=Caixa, 3=Gerencial))
- `compartilha_plano`: Filtra comp_pad (char). Aceita: valor simples (igualdade), igual. Códigos: S=Sim, N=Não (Compartilha plano de contas (S/N))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `parametro_folha_consultar`

Parâmetros da folha por empresa — tabela foparmto (módulo parametros_empresa, ~1.355 linhas).
O QUE É: Configuração da folha da empresa: competência e tipo de processamento atuais, tipos de folha usados, regras de adiantamento, 13º e férias, integração contábil, rateio por serviço e dia do pagamento. 1.356 linhas, uma por empresa. Usa 39 das 599 colunas.
COMENTÁRIO DO BANCO SOBRE A TABELA: Tabela de parâmetros
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: competencia_atual, tipo_folha_atual, gera_lancamentos_contabeis. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: competencia_atual, tipo_folha_atual, mes_encerrado, empresa_dos_eventos, folha_semanal, folha_quinzenal, folha_professor, adiantamento_base, adiantamento_percentual, adiantamento_afastados, adiantamento_contribuintes, adiantamento_dias_minimos, decimo_terceiro_percentual, decimo_terceiro_paga_medias, decimo_terceiro_paga_adicionais, decimo_terceiro_nao_calcula_diretores, decimo_terceiro_mais_de_um_adiantamento, decimo_terceiro_estagiario, decimo_terceiro_desconta_faltas, ajusta_13_em_dezembro, ferias_desconta_faltas, ferias_paga_adicionais, ferias_paga_medias, ferias_adianta_13, ferias_estagiario, gera_lancamentos_contabeis, lancamentos_na_empresa, contabil_separa_rescisao, contabil_separa_ferias, contabil_tipo_exportacao, contabil_por_centro_custo, usa_rateio_por_servico, rateio_inicio, discrimina_dsr, ordena_eventos, movimento_ferias_na_folha_mensal, data_pagamento_mensal, optante_simples_nacional, conta_debito_gps. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): empresa_nome.
EXEMPLO COM DADOS: a empresa 1148 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Uma linha por empresa (1.356). Nenhuma empresa trabalha com folha semanal, quinzenal ou de professores (todas N). | Competência atual (data_proces): de 2013-01 a 2026-10; 255 empresas estão em setembro/2026 ou depois, 25 entre janeiro e agosto de 2026 e 1.076 antes de 2026 (empresas sem folha ativa). | Tipo de folha atual: 11 (mensal) em 911 empresas, 70 em 375, 41 em 65, 51 e 52 em 2 cada e 42 em 1. | Encerramento: `mes_encerrado` tem valor em todas as 1.356 linhas, de 1900-01-01 (padrão 'não informado') a 2026-03: está desatualizado em relação à competência atual e não deve ser usado para saber se a folha está fechada (use o S-1299 do eSocial: função situacao_esocial). | Integração contábil: gera lançamentos (cta_gera = 1) em 1.257 empresas e não em 99; só 3 usam rateio por serviço. Eventos próprios em 711 empresas e eventos de outra empresa (codi_emp_eve) em 645. (+1 regras: veja descrever_entidade)
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `competencia_atual`: Filtra data_proces (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia atual) Datas no formato AAAA-MM-DD.
- `tipo_folha_atual`: Filtra tipo_proces (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 11=Mensal, 41=Adiantamento, 42=Complementar, 51=Adiantamento de 13º salário, 52=13º salário, 70=Participação nos lucros [parcialmente confirmado] (tipo folha atual)
- `gera_lancamentos_contabeis`: Filtra cta_gera (tinyint). Aceita: valor simples (igualdade), igual. Códigos: 1=Sim, 0=Não (Gera lancamentos contabeis)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `parametro_folha_totais`

Parâmetros da folha por empresa — TOTAIS por grupo da tabela foparmto (módulo parametros_empresa). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). CAMPOS SOMÁVEIS: adiantamento_dias_minimos. CAMPOS PARA AGRUPAR: competencia_atual:mes, tipo_folha_atual, mes_encerrado:mes, empresa_dos_eventos, folha_semanal, folha_quinzenal, folha_professor, adiantamento_base, adiantamento_percentual, adiantamento_afastados, adiantamento_contribuintes, decimo_terceiro_percentual, decimo_terceiro_paga_medias, decimo_terceiro_paga_adicionais, decimo_terceiro_nao_calcula_diretores, decimo_terceiro_mais_de_um_adiantamento, decimo_terceiro_estagiario, decimo_terceiro_desconta_faltas, ajusta_13_em_dezembro, ferias_desconta_faltas, ferias_paga_adicionais, ferias_paga_medias, ferias_adianta_13, ferias_estagiario, gera_lancamentos_contabeis, lancamentos_na_empresa, contabil_separa_rescisao, contabil_separa_ferias, contabil_tipo_exportacao, contabil_por_centro_custo, usa_rateio_por_servico, rateio_inicio:mes, discrimina_dsr, ordena_eventos, movimento_ferias_na_folha_mensal, data_pagamento_mensal, optante_simples_nacional, […]. Os filtros são os mesmos de parametro_folha_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (tipo_folha_atual, folha_semanal, folha_quinzenal, folha_professor) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Uma linha por empresa (1.356). Nenhuma empresa trabalha com folha semanal, quinzenal ou de professores (todas N). | Competência atual (data_proces): de 2013-01 a 2026-10; 255 empresas estão em setembro/2026 ou depois, 25 entre janeiro e agosto de 2026 e 1.076 antes de 2026 (empresas sem folha ativa). | Tipo de folha atual: 11 (mensal) em 911 empresas, 70 em 375, 41 em 65, 51 e 52 em 2 cada e 42 em 1. | Encerramento: `mes_encerrado` tem valor em todas as 1.356 linhas, de 1900-01-01 (padrão 'não informado') a 2026-03: está desatualizado em relação à competência atual e não deve ser usado para saber se a folha está fechada (use o S-1299 do eSocial: função situacao_esocial).. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `competencia_atual`: Filtra data_proces (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia atual) Datas no formato AAAA-MM-DD.
- `tipo_folha_atual`: Filtra tipo_proces (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 11=Mensal, 41=Adiantamento, 42=Complementar, 51=Adiantamento de 13º salário, 52=13º salário, 70=Participação nos lucros [parcialmente confirmado] (tipo folha atual)
- `gera_lancamentos_contabeis`: Filtra cta_gera (tinyint). Aceita: valor simples (igualdade), igual. Códigos: 1=Sim, 0=Não (Gera lancamentos contabeis)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["competencia_atual:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["adiantamento_dias_minimos"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).
