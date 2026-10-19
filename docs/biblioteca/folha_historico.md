# Módulo `folha_historico`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `situacao_mensal_empregado_consultar` | consultar | foafastamentos_competencia | empresa | ✔ |
| `situacao_mensal_empregado_totais` | totais | foafastamentos_competencia | empresa | ✔ |
| `alteracao_salarial_consultar` | consultar | foaltesal | empresa | ✔ |
| `alteracao_salarial_totais` | totais | foaltesal | empresa | ✔ |
| `alteracao_contratual_consultar` | consultar | foempregados_alteracao_contratual | empresa | ✔ |
| `alteracao_contratual_obter` | obter | foempregados_alteracao_contratual | empresa, empregado_codigo, data_alteracao | ✔ |
| `alteracao_contratual_totais` | totais | foempregados_alteracao_contratual | empresa | ✔ |
| `lancamento_evento_folha_consultar` | consultar | folancamentos_eventos | empresa | ✔ |
| `lancamento_evento_folha_totais` | totais | folancamentos_eventos | empresa | ✔ |

## `situacao_mensal_empregado_consultar`

Situação mensal do empregado (trabalhando, férias, afastado...) — tabela foafastamentos_competencia (módulo folha_historico, ~429.060 linhas).
O QUE É: Registra, para cada empregado e competência, em que situação ele estava (código de afastamento) e o período correspondente. ATENÇÃO: o código 1 é "Trabalhando": 400.581 de 429.093 linhas (93%) são o empregado trabalhando; os afastamentos (férias, doença, maternidade, demitido...) são a minoria. 429.093 linhas, 969 empresas.
COMENTÁRIO DO BANCO SOBRE A TABELA: AFASTAMENTOS SEPARADOS POR COMPETENCIA
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): empregado_codigo, periodo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna COMPETENCIA. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: empregado_codigo, competencia, situacao_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: empregado_codigo, competencia, situacao_codigo, data_real, data_inicio, data_fim, numero_dias, origem_registro. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): situacao_descricao.
EXEMPLO COM DADOS: a empresa 1196 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Situação 1 'Trabalhando' em 400.581 linhas; 9 'Férias' 13.319; 8 'Demitido' 10.418; 6 'Doença período superior a 15 dias' 1.130; 18 'Doença até 15 dias' 1.092; 5 'Licença maternidade' 741. Para listar só afastamentos filtre situacao_codigo diferente de 1. | O número de dias é igual a (data fim − data início + 1) em 427.267 de 429.093 linhas. | Dados suspeitos: competências de 1968-01 até 2028-11 (futuras) aparecem; use filtro de período.
PRIVACIDADE: A situação de afastamento pode revelar condição de saúde do empregado.
PRIVACIDADE (folha): as linhas são de empregados identificáveis; evite listar pessoas sem necessidade.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `empregado_codigo`: Filtra I_EMPREGADOS (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CODIGO)
- `competencia`: Filtra COMPETENCIA (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competência) Datas no formato AAAA-MM-DD.
- `situacao_codigo`: Filtra I_AFASTAMENTOS (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do afastamento referente ao tipo de afastamento da FOAFASTAMENTOS_TIPO)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `situacao_mensal_empregado_totais`

Situação mensal do empregado (trabalhando, férias, afastado...) — TOTAIS por grupo da tabela foafastamentos_competencia (módulo folha_historico). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): empregado_codigo, periodo. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna COMPETENCIA. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: numero_dias. CAMPOS PARA AGRUPAR: empregado_codigo, competencia:mes, situacao_codigo, data_real:mes, data_inicio:mes, data_fim:mes, origem_registro. Os filtros são os mesmos de situacao_mensal_empregado_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Situação 1 'Trabalhando' em 400.581 linhas; 9 'Férias' 13.319; 8 'Demitido' 10.418; 6 'Doença período superior a 15 dias' 1.130; 18 'Doença até 15 dias' 1.092; 5 'Licença maternidade' 741. Para listar só afastamentos filtre situacao_codigo diferente de 1. | O número de dias é igual a (data fim − data início + 1) em 427.267 de 429.093 linhas. | Dados suspeitos: competências de 1968-01 até 2028-11 (futuras) aparecem; use filtro de período.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `empregado_codigo`: Filtra I_EMPREGADOS (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CODIGO)
- `competencia`: Filtra COMPETENCIA (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competência) Datas no formato AAAA-MM-DD.
- `situacao_codigo`: Filtra I_AFASTAMENTOS (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do afastamento referente ao tipo de afastamento da FOAFASTAMENTOS_TIPO)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["competencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["numero_dias"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `alteracao_salarial_consultar`

Alterações salariais do empregado — tabela foaltesal (módulo folha_historico, ~27.782 linhas).
O QUE É: Cada reajuste ou alteração de salário de um empregado: salário anterior e novo, forma da alteração, motivo, retroatividade e período. 27.825 linhas, 974 empresas, 10.976 empregados. Datas anteriores a 2000 (707 linhas) são provavelmente o valor padrão 1900-01-01.
COMENTÁRIO DO BANCO SOBRE A TABELA: Salarios - Processos
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): empregado_codigo, periodo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna competencia. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: empregado_codigo, competencia, forma_alteracao, retroativo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: empregado_codigo, competencia, tipo, forma_alteracao, salario_anterior, novo_salario, valor_adicionado, percentual_aumento, motivo, retroativo, retroativo_a_partir_de, forma_ajuste_retroativo, periodo_inicio, periodo_fim, origem_registro, novo_pelo_percentual, novo_pela_soma. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 1219 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Percentual: em 3.727 de 3.731 alterações de forma 3 (percentual), novo salário = salário anterior × (1 + %) com tolerância de 5 centavos. Adicionar valor: novo = anterior + valor adicionado em 107 de 107 (forma 2). | Continuidade: nas 40 empresas com mais alterações, o salário anterior de uma alteração é igual ao novo salário da alteração anterior do mesmo empregado em 8.915 de 8.955 pares (99,6%). | Formas de alteração: 1 (novo salário) 23.651 · 3 (percentual) 3.731 · 7 (sem legenda) 335 · 2 (adicionar valor) 107 · 6 (sem legenda) 1. Só existe o tipo 1 (normal). | Dados suspeitos: 707 alterações têm data anterior a 2000 (valor padrão 1900-01-01), 6 têm data futura (até 2026-10-20) e 2.225 têm novo salário zero. 4.430 são retroativas.
PRIVACIDADE: Salário por empregado identificável (financeiro).
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): salario_anterior, novo_salario, valor_adicionado
PRIVACIDADE (folha): as linhas são de empregados identificáveis; evite listar pessoas sem necessidade.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `empregado_codigo`: Filtra i_empregados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Empregado)
- `competencia`: Filtra competencia (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data) Datas no formato AAAA-MM-DD.
- `forma_alteracao`: Filtra forma_alteracao (tinyint). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Novo salário, 2=Adicionar valor, 3=Percentual de aumento, 6=Sem legenda (1 linha), 7=Sem legenda (335 linhas) [parcialmente confirmado] (Forma de alteração: (1=Novo salário/2=Adicionar valor/3=Percentual de aumento/4=Nível/5=Percentual CCT/6=Valor antecipação/7=Percentual CCT/8=Percentual variável/9=Conforme índice))
- `retroativo`: Filtra retroativo (tinyint). Aceita: valor simples (igualdade), igual. Códigos: 1=Sim, 0=Não (Aumento retroativo)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `alteracao_salarial_totais`

Alterações salariais do empregado — TOTAIS por grupo da tabela foaltesal (módulo folha_historico). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): empregado_codigo, periodo. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna competencia. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: salario_anterior, novo_salario, valor_adicionado. CAMPOS PARA AGRUPAR: empregado_codigo, competencia:mes, tipo, forma_alteracao, percentual_aumento, motivo, retroativo, retroativo_a_partir_de:mes, forma_ajuste_retroativo, periodo_inicio:mes, periodo_fim:mes, origem_registro. Os filtros são os mesmos de alteracao_salarial_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (tipo, forma_alteracao, retroativo) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Percentual: em 3.727 de 3.731 alterações de forma 3 (percentual), novo salário = salário anterior × (1 + %) com tolerância de 5 centavos. Adicionar valor: novo = anterior + valor adicionado em 107 de 107 (forma 2). | Continuidade: nas 40 empresas com mais alterações, o salário anterior de uma alteração é igual ao novo salário da alteração anterior do mesmo empregado em 8.915 de 8.955 pares (99,6%). | Formas de alteração: 1 (novo salário) 23.651 · 3 (percentual) 3.731 · 7 (sem legenda) 335 · 2 (adicionar valor) 107 · 6 (sem legenda) 1. Só existe o tipo 1 (normal). | Dados suspeitos: 707 alterações têm data anterior a 2000 (valor padrão 1900-01-01), 6 têm data futura (até 2026-10-20) e 2.225 têm novo salário zero. 4.430 são retroativas.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `empregado_codigo`: Filtra i_empregados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Empregado)
- `competencia`: Filtra competencia (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data) Datas no formato AAAA-MM-DD.
- `forma_alteracao`: Filtra forma_alteracao (tinyint). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Novo salário, 2=Adicionar valor, 3=Percentual de aumento, 6=Sem legenda (1 linha), 7=Sem legenda (335 linhas) [parcialmente confirmado] (Forma de alteração: (1=Novo salário/2=Adicionar valor/3=Percentual de aumento/4=Nível/5=Percentual CCT/6=Valor antecipação/7=Percentual CCT/8=Percentual variável/9=Conforme índice))
- `retroativo`: Filtra retroativo (tinyint). Aceita: valor simples (igualdade), igual. Códigos: 1=Sim, 0=Não (Aumento retroativo)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["competencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["salario_anterior"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `alteracao_contratual_consultar`

Alterações contratuais do empregado — tabela foempregados_alteracao_contratual (módulo folha_historico, ~33.276 linhas).
O QUE É: Histórico das condições do contrato de cada empregado a partir de uma data: serviço, cargo, função, convenção coletiva, categoria, vínculo, salário, jornada e horas semanais. 33.339 linhas, 977 empresas, todas com salário. Usa 23 das 55 colunas (as demais são de estágio, contrato por prazo determinado e controle do eSocial).
COMENTÁRIO DO BANCO SOBRE A TABELA: Registros de alteração cadastral para envio ao eSocial.
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): empregado_codigo, periodo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DATA_ALTERACAO. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: empregado_codigo, data_alteracao, cargo_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: empregado_codigo, data_alteracao, servico_codigo, cargo_codigo, funcao_codigo, sindicato_codigo, categoria, vinculo, tipo_horario, salario, horas_semana, carga_horaria_variavel, jornada_codigo, local_trabalho_codigo, remuneracao_variavel_codigo, sindicalizado, categoria_esocial, tipo_contribuinte, fim_contrato_prazo_determinado, dias_contrato_prazo_determinado, alvara_judicial, modalidade_contratacao, numero_processo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 1219 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): 33.339 linhas e todas têm salário preenchido; a data mais antiga é 1900-01-01 (valor padrão) e a mais recente 2026-10-20.
PRIVACIDADE: Salário e cargo por empregado identificável (financeiro).
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): salario
POSSÍVEIS DADOS PESSOAIS/FINANCEIROS (os dados saem em claro; devolva só o que a pergunta exigir): remuneracao_variavel_codigo.
PRIVACIDADE (folha): as linhas são de empregados identificáveis; evite listar pessoas sem necessidade.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `empregado_codigo`: Filtra I_EMPREGADOS (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do empregado.)
- `data_alteracao`: Filtra DATA_ALTERACAO (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data da alteração.) Datas no formato AAAA-MM-DD.
- `cargo_codigo`: Filtra I_CARGOS (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do cargo.)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `alteracao_contratual_obter`

Alterações contratuais do empregado — obtém UM registro pela chave (CODI_EMP, I_EMPREGADOS, DATA_ALTERACAO) da tabela foempregados_alteracao_contratual. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use alteracao_contratual_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP).
- `empregado_codigo` (obrigatório): Filtra I_EMPREGADOS (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do empregado.)
- `data_alteracao` (obrigatório): Filtra DATA_ALTERACAO (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data da alteração.) Datas no formato AAAA-MM-DD.

## `alteracao_contratual_totais`

Alterações contratuais do empregado — TOTAIS por grupo da tabela foempregados_alteracao_contratual (módulo folha_historico). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): empregado_codigo, periodo. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DATA_ALTERACAO. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: salario, horas_semana, dias_contrato_prazo_determinado. CAMPOS PARA AGRUPAR: empregado_codigo, data_alteracao:mes, servico_codigo, cargo_codigo, funcao_codigo, sindicato_codigo, categoria, vinculo, tipo_horario, carga_horaria_variavel, jornada_codigo, local_trabalho_codigo, remuneracao_variavel_codigo, sindicalizado, categoria_esocial, tipo_contribuinte, fim_contrato_prazo_determinado:mes, alvara_judicial, modalidade_contratacao, numero_processo. Os filtros são os mesmos de alteracao_contratual_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (carga_horaria_variavel, sindicalizado, alvara_judicial) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: 33.339 linhas e todas têm salário preenchido; a data mais antiga é 1900-01-01 (valor padrão) e a mais recente 2026-10-20.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `empregado_codigo`: Filtra I_EMPREGADOS (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do empregado.)
- `data_alteracao`: Filtra DATA_ALTERACAO (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data da alteração.) Datas no formato AAAA-MM-DD.
- `cargo_codigo`: Filtra I_CARGOS (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do cargo.)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["data_alteracao:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["salario"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `lancamento_evento_folha_consultar`

Lançamentos de eventos da folha (variáveis e fixos) — tabela folancamentos_eventos (módulo folha_historico, ~226.043 linhas).
O QUE É: Eventos lançados para um empregado (horas extras, faltas, comissões, descontos fixos...) com a competência inicial e final, o tipo de folha, o valor informado e a origem do lançamento. 226.061 linhas, 805 empresas. 213.860 não têm competência final (valem sem prazo).
COMENTÁRIO DO BANCO SOBRE A TABELA: Lançamentos de eventos para o cálculo
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): empregado_codigo, periodo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna COMPETENCIA_INICIAL. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: empregado_codigo, evento_codigo, tipo_folha, competencia_inicial. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: empregado_codigo, evento_codigo, tipo_folha, tipo_lancamento, competencia_inicial, competencia_final, meses_aplicaveis, prioridade, valor_informado, valor_calculado, origem_lancamento, sequencial, competencia_alteracao, data_pagamento_alteracao_calculo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): evento_nome.
EXEMPLO COM DADOS: a empresa 1536 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Tipo de lançamento: mensal (1) em 203.673 e fixo (2) em 22.388. Origem: lançamento de eventos 169.827 · importação 25.772 · origem 4 (sem legenda) 17.300 · alterar cálculo 10.612 · origem 6 (sem legenda) 2.477 · origem 5 (sem legenda) 73. | 213.860 lançamentos não têm competência final (valem até serem encerrados) e 15.291 têm valor informado zero. Dado suspeito: há competência inicial no ano 2400. | Por tipo de folha: mensal (11) 216.286 · participação nos lucros (70) 4.323 · adiantamento (41) 3.197 · 13º (52) 1.027 · adiantamento de 13º (51) 648 · complementar (42) 580.
PRIVACIDADE: Valores lançados por empregado identificável (financeiro).
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): valor_informado, valor_calculado
PRIVACIDADE (folha): as linhas são de empregados identificáveis; evite listar pessoas sem necessidade.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `empregado_codigo`: Filtra I_EMPREGADOS (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do empregado)
- `evento_codigo`: Filtra I_EVENTOS (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do evento)
- `tipo_folha`: Filtra TIPO_PROCESSO (smallint). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 11=Mensal, 41=Adiantamento, 42=Complementar, 51=Adiantamento de 13º salário, 52=13º salário, 70=Participação nos lucros [parcialmente confirmado] (Tipo do processo: 11=Mensal/31=1ª semana/32=2ª semana/33=3ª semana/34=4ª semana/35=Última semana/36=Todas as semanas/41=Adiantamento/42=Complementar/51=Adiantamento 13º salário/52=13º salário)
- `competencia_inicial`: Filtra COMPETENCIA_INICIAL (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competência inicial) Datas no formato AAAA-MM-DD.
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `lancamento_evento_folha_totais`

Lançamentos de eventos da folha (variáveis e fixos) — TOTAIS por grupo da tabela folancamentos_eventos (módulo folha_historico). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): empregado_codigo, periodo. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna COMPETENCIA_INICIAL. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor_informado, valor_calculado. CAMPOS PARA AGRUPAR: empregado_codigo, evento_codigo, tipo_folha, tipo_lancamento, competencia_inicial:mes, competencia_final:mes, meses_aplicaveis, prioridade, origem_lancamento, sequencial, competencia_alteracao:mes, data_pagamento_alteracao_calculo:mes. Os filtros são os mesmos de lancamento_evento_folha_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (tipo_folha, tipo_lancamento, origem_lancamento) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Tipo de lançamento: mensal (1) em 203.673 e fixo (2) em 22.388. Origem: lançamento de eventos 169.827 · importação 25.772 · origem 4 (sem legenda) 17.300 · alterar cálculo 10.612 · origem 6 (sem legenda) 2.477 · origem 5 (sem legenda) 73. | 213.860 lançamentos não têm competência final (valem até serem encerrados) e 15.291 têm valor informado zero. Dado suspeito: há competência inicial no ano 2400. | Por tipo de folha: mensal (11) 216.286 · participação nos lucros (70) 4.323 · adiantamento (41) 3.197 · 13º (52) 1.027 · adiantamento de 13º (51) 648 · complementar (42) 580.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `empregado_codigo`: Filtra I_EMPREGADOS (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do empregado)
- `evento_codigo`: Filtra I_EVENTOS (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do evento)
- `tipo_folha`: Filtra TIPO_PROCESSO (smallint). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 11=Mensal, 41=Adiantamento, 42=Complementar, 51=Adiantamento de 13º salário, 52=13º salário, 70=Participação nos lucros [parcialmente confirmado] (Tipo do processo: 11=Mensal/31=1ª semana/32=2ª semana/33=3ª semana/34=4ª semana/35=Última semana/36=Todas as semanas/41=Adiantamento/42=Complementar/51=Adiantamento 13º salário/52=13º salário)
- `competencia_inicial`: Filtra COMPETENCIA_INICIAL (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competência inicial) Datas no formato AAAA-MM-DD.
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["competencia_inicial:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor_informado"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).
