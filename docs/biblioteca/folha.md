# Módulo `folha`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `afastamento_consultar` | consultar | foafastamentos | empresa | ✔ |
| `afastamento_totais` | totais | foafastamentos | empresa | ✔ |
| `base_folha_consultar` | consultar | fobasesserv | empresa | ✔ |
| `base_folha_totais` | totais | fobasesserv | empresa | ✔ |
| `cargo_consultar` | consultar | focargos | empresa | ✔ |
| `cargo_obter` | obter | focargos | empresa, codigo | ✔ |
| `centro_custo_folha_consultar` | consultar | foccustos | empresa | ✔ |
| `centro_custo_folha_obter` | obter | foccustos | empresa, codigo | ✔ |
| `departamento_folha_consultar` | consultar | fodepto | empresa | ✔ |
| `departamento_folha_obter` | obter | fodepto | empresa, codigo | ✔ |
| `empregado_consultar` | consultar | foempregados | empresa | ✔ |
| `empregado_obter` | obter | foempregados | empresa, codigo | ✔ |
| `empregado_totais` | totais | foempregados | empresa | ✔ |
| `evento_consultar` | consultar | foeventos | empresa | ✔ |
| `evento_obter` | obter | foeventos | empresa, codigo | ✔ |
| `evento_padrao_consultar` | consultar | foeventosdef | — | ✔ |
| `evento_padrao_obter` | obter | foeventosdef | codigo | ✔ |
| `falta_consultar` | consultar | fofaltas | empresa | ✔ |
| `falta_totais` | totais | fofaltas | empresa | ✔ |
| `ferias_periodo_aquisitivo_consultar` | consultar | foferias_aquisitivos | empresa | ✔ |
| `ferias_periodo_aquisitivo_totais` | totais | foferias_aquisitivos | empresa | ✔ |
| `ferias_gozo_consultar` | consultar | foferias_gozo | empresa | ✔ |
| `ferias_gozo_totais` | totais | foferias_gozo | empresa | ✔ |
| `filial_folha_consultar` | consultar | fofiliais | empresa | ✔ |
| `filial_folha_obter` | obter | fofiliais | empresa, codigo | ✔ |
| `liquido_folha_consultar` | consultar | foliquidosfilepr | empresa | ✔ |
| `liquido_folha_totais` | totais | foliquidosfilepr | empresa | ✔ |
| `movimento_folha_consultar` | consultar | fomovtoserv | empresa | ✔ |
| `movimento_folha_totais` | totais | fomovtoserv | empresa | ✔ |
| `rescisao_consultar` | consultar | forescisoes | empresa | ✔ |
| `rescisao_totais` | totais | forescisoes | empresa | ✔ |
| `servico_folha_consultar` | consultar | foservicos | empresa | ✔ |
| `servico_folha_obter` | obter | foservicos | empresa, codigo | ✔ |
| `sindicato_consultar` | consultar | fosindicatos | — | ✔ |
| `sindicato_obter` | obter | fosindicatos | codigo | ✔ |
| `sindicato_totais` | totais | fosindicatos | — | ✔ |

## `afastamento_consultar`

Afastamentos — tabela FOAFASTAMENTOS (módulo folha, ~38.146 linhas).
O QUE É: Afastamentos do empregado (licenças, auxílio-doença, maternidade...). Colunas de saúde (CID, CAT, acidente) foram deixadas de fora de propósito.
COMENTÁRIO DO BANCO SOBRE A TABELA: AFASTAMENTOS DOS EMPREGADOS
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DATA_REAL. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: empregado_codigo, data_inicio, tipo_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: empregado_codigo, data_inicio, data_inicio_folha, data_fim, numero_dias, tipo_codigo, transferencia, origem. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): tipo_descricao, empregado_nome.
EXEMPLO COM DADOS: a empresa 992 tem registros nesta tabela (use para testar).
PRIVACIDADE: O tipo de afastamento pode revelar condição de saúde do empregado (ex.: auxílio-doença). Tratar como dado sensível.
PRIVACIDADE (folha): as linhas são de empregados identificáveis; evite listar pessoas sem necessidade.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `empregado_codigo`: Filtra I_EMPREGADOS (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CODIGO)
- `data_inicio`: Filtra DATA_REAL (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data Real) Datas no formato AAAA-MM-DD.
- `tipo_codigo`: Filtra I_AFASTAMENTOS (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do afastamento referente ao tipo de afastamento da FOAFASTAMENTOS_TIPO)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `afastamento_totais`

Afastamentos — TOTAIS por grupo da tabela FOAFASTAMENTOS (módulo folha). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DATA_REAL. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: numero_dias. CAMPOS PARA AGRUPAR: empregado_codigo, data_inicio:mes, data_inicio_folha:mes, data_fim:mes, tipo_codigo, transferencia, origem. Os filtros são os mesmos de afastamento_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `empregado_codigo`: Filtra I_EMPREGADOS (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CODIGO)
- `data_inicio`: Filtra DATA_REAL (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data Real) Datas no formato AAAA-MM-DD.
- `tipo_codigo`: Filtra I_AFASTAMENTOS (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do afastamento referente ao tipo de afastamento da FOAFASTAMENTOS_TIPO)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["data_inicio:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["numero_dias"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `base_folha_consultar`

Bases e totais da folha — tabela fobasesserv (módulo folha, ~415.218 linhas).
O QUE É: Uma linha por empregado, competência, tipo de folha, serviço e cálculo, com os totais já calculados pela Domínio: proventos, descontos e o líquido (calculado pelo modelo = proventos − descontos). Das ~35 colunas, o banco marca ~25 como "SEM USO" (IRRF, INSS, FGTS ficam em outras tabelas); só as vivas são expostas.
COMENTÁRIO DO BANCO SOBRE A TABELA: Bases - Calculo
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): periodo, empregado_codigo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna competencia. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: empregado_codigo, competencia, tipo_folha, departamento_codigo, centro_custo_codigo, cargo_codigo, rateio. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: empregado_codigo, competencia, tipo_folha, situacao_mes, departamento_codigo, centro_custo_codigo, cargo_codigo, numero_filhos, numero_dependentes, proventos, descontos, salario_mes, salario_maternidade, salario_familia, numero_cheque, servico_codigo, rateio, calculo, liquido. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): empregado_nome, departamento_nome, cargo_nome.
EXEMPLO COM DADOS: a empresa 9029 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): ATENÇÃO AO SOMAR: cada cálculo aparece em DUAS linhas com os mesmos proventos e descontos quando a empresa tem rateio por serviço: rateio = 0 é a linha principal (a que tem o líquido em foliquidosfilepr) e rateio = 1 repete o total por serviço; somar tudo DOBRA os valores (empresa 354, 2026-08, […] | proventos = Σ valor_calculado dos eventos P que aparecem no recibo; descontos = Σ dos eventos D que aparecem no recibo (validado: 99,99% e 99,4% de 56.026 linhas, 5 empresas). | liquido = proventos − descontos coincide com o líquido registrado pela Domínio em foliquidosfilepr em 99,8% dos pares empregado×cálculo. | situacao_mes (valores 1, 9, 8, 6, 5, 59, 3, 16...) não tem descrição no banco: significado não confirmado. | INSS, IRRF e FGTS NÃO estão aqui (colunas marcadas SEM USO); estão em tabelas próprias (fobasesirrf, fofgtsfilial, foguiainss...), ainda não modeladas.
PRIVACIDADE: Totais de remuneração por empregado identificável (financeiro). Os dados saem em claro nesta versão do servidor: devolva só o que a pergunta exigir.
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): proventos, descontos, salario_mes, salario_maternidade, salario_familia
PRIVACIDADE (folha): as linhas são de empregados identificáveis; evite listar pessoas sem necessidade.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `empregado_codigo`: Filtra i_empregados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Empregado)
- `competencia`: Filtra competencia (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia) Datas no formato AAAA-MM-DD.
- `tipo_folha`: Filtra tipo_process (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 11=Mensal, 31=1ª semana, 32=2ª semana, 33=3ª semana, 34=4ª semana, 35=Última semana, 36=Todas as semanas, 41=Adiantamento, 42=Complementar, 51=Adiantamento de 13º salário, … (+3) [parcialmente confirmado] (TIPO DE CALCULO)
- `departamento_codigo`: Filtra i_depto (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Departamento)
- `centro_custo_codigo`: Filtra i_ccustos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Centro de Custos)
- `cargo_codigo`: Filtra i_cargos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Cargo)
- `rateio`: Filtra rateio (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Rateio)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `base_folha_totais`

Bases e totais da folha — TOTAIS por grupo da tabela fobasesserv (módulo folha). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): periodo, empregado_codigo. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna competencia. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: proventos, descontos, salario_maternidade, salario_familia. CAMPOS PARA AGRUPAR: empregado_codigo, competencia:mes, tipo_folha, situacao_mes, departamento_codigo, centro_custo_codigo, cargo_codigo, numero_filhos, numero_dependentes, salario_mes, numero_cheque, servico_codigo, rateio, calculo. Os filtros são os mesmos de base_folha_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (tipo_folha) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: ATENÇÃO AO SOMAR: cada cálculo aparece em DUAS linhas com os mesmos proventos e descontos quando a empresa tem rateio por serviço: rateio = 0 é a linha principal (a que tem o líquido em foliquidosfilepr) e rateio = 1 repete o total por serviço; somar tudo DOBRA os valores (empresa 354, 2026-08, folha mensal: proventos 89.783,78 com rateio = 0 e 179.567,56 somando as duas). […] | proventos = Σ valor_calculado dos eventos P que aparecem no recibo; descontos = Σ dos eventos D que aparecem no recibo (validado: 99,99% e 99,4% de 56.026 linhas, 5 empresas). | liquido = proventos − descontos coincide com o líquido registrado pela Domínio em foliquidosfilepr em 99,8% dos pares empregado×cálculo. | situacao_mes (valores 1, 9, 8, 6, 5, 59, 3, 16...) não tem descrição no banco: significado não confirmado.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `empregado_codigo`: Filtra i_empregados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Empregado)
- `competencia`: Filtra competencia (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia) Datas no formato AAAA-MM-DD.
- `tipo_folha`: Filtra tipo_process (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 11=Mensal, 31=1ª semana, 32=2ª semana, 33=3ª semana, 34=4ª semana, 35=Última semana, 36=Todas as semanas, 41=Adiantamento, 42=Complementar, 51=Adiantamento de 13º salário, … (+3) [parcialmente confirmado] (TIPO DE CALCULO)
- `departamento_codigo`: Filtra i_depto (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Departamento)
- `centro_custo_codigo`: Filtra i_ccustos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Centro de Custos)
- `cargo_codigo`: Filtra i_cargos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Cargo)
- `rateio`: Filtra rateio (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Rateio)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["competencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["proventos"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `cargo_consultar`

Cargos — tabela focargos (módulo folha, ~6.043 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: Cargo - Cadastro
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, nome, cbo_2002, situacao. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, nome, cbo_1994, cbo_2002, atividade, situacao, data_inicio, data_inativacao, codigo_esocial. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 719 tem registros nesta tabela (use para testar).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra i_cargos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `nome`: Filtra nome (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Nome)
- `cbo_2002`: Filtra cbo_2002 (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CBO 2002)
- `situacao`: Filtra SITUACAO (smallint). Aceita: valor simples (igualdade), igual. Códigos: 0=Inativo, 1=Ativo (Situação do cargo. (0=Inativo/1=Ativo))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `cargo_obter`

Cargos — obtém UM registro pela chave (codi_emp, i_cargos) da tabela focargos. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use cargo_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra i_cargos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `centro_custo_folha_consultar`

Centros de custo (folha) — tabela foccustos (módulo folha, ~1.629 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: Centro de Custos - Cadastro
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, nome. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, nome, tipo, sintetico_codigo, mascara. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 646 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): tipo: 1 = sintético, 2 = analítico (comentário do banco).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra i_ccustos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `nome`: Filtra nome (varchar). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Nome)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `centro_custo_folha_obter`

Centros de custo (folha) — obtém UM registro pela chave (codi_emp, i_ccustos) da tabela foccustos. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use centro_custo_folha_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra i_ccustos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `departamento_folha_consultar`

Departamentos (folha) — tabela fodepto (módulo folha, ~1.403 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: Departamento - Cadastro
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, nome, situacao. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, nome, situacao, data_inicio, data_inativacao. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 903 tem registros nesta tabela (use para testar).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra i_depto (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `nome`: Filtra nome (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Nome)
- `situacao`: Filtra SITUACAO (smallint). Aceita: valor simples (igualdade), igual. Códigos: 0=Inativo, 1=Ativo (Situação do departamento. (0=Inativo/1=Ativo))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `departamento_folha_obter`

Departamentos (folha) — obtém UM registro pela chave (codi_emp, i_depto) da tabela fodepto. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use departamento_folha_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra i_depto (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `empregado_consultar`

Empregados (cadastro funcional) — tabela foempregados (módulo folha, ~10.974 linhas).
O QUE É: Dados funcionais do empregado. Apenas colunas necessárias ao uso de DP; veja o bloco de privacidade no topo do arquivo. A tabela tem 416 colunas (27 marcadas pelo próprio banco como "SEM USO"); só um subconjunto é exposto.
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, matricula, nome, cpf, admissao, filial_codigo, departamento_codigo, cargo_codigo, centro_custo_codigo, categoria, vinculo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, matricula, nome, cpf, pis, identidade, data_nascimento, sexo, estado_civil, grau_instrucao, admissao, categoria, vinculo, salario, forma_pagamento, horas_mes, horas_semana, horas_dia, vencimento_ferias, optante_fgts, data_opcao_fgts, tipo_contribuinte, filial_codigo, departamento_codigo, cargo_codigo, centro_custo_codigo, servico_codigo, sindicato_codigo, data_transferencia, origem_registro. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): filial_nome, departamento_nome, cargo_nome, cargo_cbo, centro_custo_nome, sindicato_nome.
EXEMPLO COM DADOS: a empresa 640 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): O cadastro de empregados NÃO traz situação atual (ativo/demitido). A demissão está em `rescisao`; afastamentos em `afastamento`. | categoria (1=10.741, 5=217, 7=14, 4=2) e vinculo (1, 11, 50, 0, 13, 52...) são códigos sem tabela de descrição no banco: significado não confirmado. | Dados dos 'SEM USO' do próprio banco foram ignorados.
PRIVACIDADE: Contém dado pessoal (nome, CPF, PIS, identidade, nascimento) e salário. Os dados saem em claro nesta versão do servidor: devolva só o que a pergunta exigir.
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): nome, cpf, pis, identidade, data_nascimento, salario
POSSÍVEIS DADOS PESSOAIS/FINANCEIROS (os dados saem em claro; devolva só o que a pergunta exigir): filial_nome, departamento_nome, cargo_nome, centro_custo_nome, sindicato_nome.
PRIVACIDADE (folha): as linhas são de empregados identificáveis; evite listar pessoas sem necessidade.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra i_empregados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `matricula`: Filtra matricula (char). Aceita: valor simples (igualdade), igual. (Matricula)
- `nome`: Filtra nome (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Nome)
- `cpf`: Filtra cpf (char). Aceita: valor simples (igualdade), igual. (CPF)
- `admissao`: Filtra admissao (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Admissao) Datas no formato AAAA-MM-DD.
- `filial_codigo`: Filtra i_filiais (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo Filial)
- `departamento_codigo`: Filtra i_depto (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Departamento)
- `cargo_codigo`: Filtra i_cargos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Cargo)
- `centro_custo_codigo`: Filtra i_ccustos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Centro de Custos)
- `categoria`: Filtra categoria (smallint). Aceita: valor simples (igualdade), igual, lista de valores. (Categoria)
- `vinculo`: Filtra vinculo (smallint). Aceita: valor simples (igualdade), igual, lista de valores. (Vinculo empregaticio)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `empregado_obter`

Empregados (cadastro funcional) — obtém UM registro pela chave (codi_emp, i_empregados) da tabela foempregados. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use empregado_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra i_empregados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `empregado_totais`

Empregados (cadastro funcional) — TOTAIS por grupo da tabela foempregados (módulo folha). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). CAMPOS SOMÁVEIS: salario, horas_mes, horas_semana, horas_dia. CAMPOS PARA AGRUPAR: codigo, matricula, nome, cpf, pis, identidade, data_nascimento:mes, sexo, estado_civil, grau_instrucao, admissao:mes, categoria, vinculo, forma_pagamento, vencimento_ferias:mes, optante_fgts, data_opcao_fgts:mes, tipo_contribuinte, filial_codigo, departamento_codigo, cargo_codigo, centro_custo_codigo, servico_codigo, sindicato_codigo, data_transferencia:mes, origem_registro. Os filtros são os mesmos de empregado_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (estado_civil, optante_fgts) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: O cadastro de empregados NÃO traz situação atual (ativo/demitido). A demissão está em `rescisao`; afastamentos em `afastamento`. | categoria (1=10.741, 5=217, 7=14, 4=2) e vinculo (1, 11, 50, 0, 13, 52...) são códigos sem tabela de descrição no banco: significado não confirmado. | Dados dos 'SEM USO' do próprio banco foram ignorados.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra i_empregados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `matricula`: Filtra matricula (char). Aceita: valor simples (igualdade), igual. (Matricula)
- `nome`: Filtra nome (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Nome)
- `cpf`: Filtra cpf (char). Aceita: valor simples (igualdade), igual. (CPF)
- `admissao`: Filtra admissao (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Admissao) Datas no formato AAAA-MM-DD.
- `filial_codigo`: Filtra i_filiais (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo Filial)
- `departamento_codigo`: Filtra i_depto (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Departamento)
- `cargo_codigo`: Filtra i_cargos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Cargo)
- `centro_custo_codigo`: Filtra i_ccustos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Centro de Custos)
- `categoria`: Filtra categoria (smallint). Aceita: valor simples (igualdade), igual, lista de valores. (Categoria)
- `vinculo`: Filtra vinculo (smallint). Aceita: valor simples (igualdade), igual, lista de valores. (Vinculo empregaticio)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["data_nascimento:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["salario"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `evento_consultar`

Eventos / rubricas — tabela foeventos (módulo folha, ~1.306.923 linhas).
O QUE É: Rubricas da folha (proventos, descontos e informativos) com as marcações que definem sobre quais bases incidem e se aparecem no recibo. IMPORTANTE: só entram nos totais (proventos/descontos) os eventos com aparece_recibo = 'S'.
COMENTÁRIO DO BANCO SOBRE A TABELA: Eventos - Cadastro
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, nome, tipo, aparece_recibo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, nome, tipo, unidade, taxa, ordem_calculo, classificacao, aparece_recibo, soma_ficha_financeira, base_inss, base_irrf, base_fgts, base_sindicato, base_hora_extra, base_periculosidade, compoe_horas_mes, media_13, media_ferias, sai_na_rais, paga_proporcional, rendimento_tributavel, rendimento_isento. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 638 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Totais da folha: fobasesserv.proventos = Σ valor calculado dos eventos P que entram no recibo; fobasesserv.descontos = Σ dos eventos D idem (entra = aparece_recibo 'S' no cadastro próprio ou, na falta, no padrão; evento sem cadastro nenhum entra). Validado em 65.877 linhas de base, 9 empresas (proventos 100,0%, descontos 99,5%). […] | Uma empresa pode não ter nenhuma linha aqui e ainda assim ter movimento de folha: ela usa os eventos padrão (entidade evento_padrao). | As marcações base_* têm formatos diferentes (S/N em umas, 0/1 em outras): não as use como booleano sem conferir o valor real.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra i_eventos (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Codigo)
- `nome`: Filtra nome (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Nome)
- `tipo`: Filtra prov_desc (varchar). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: P=Provento, D=Desconto, I=Informativo (não soma), ID=Informativo de desconto (inferido) [parcialmente confirmado] (Tipo)
- `aparece_recibo`: Filtra aparece_recibo (char). Aceita: valor simples (igualdade), igual. Códigos: S=Sim, N=Não (Aparece no Recibo)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `evento_obter`

Eventos / rubricas — obtém UM registro pela chave (codi_emp, i_eventos) da tabela foeventos. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use evento_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra i_eventos (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Codigo)

## `evento_padrao_consultar`

Eventos padrão (rubricas-modelo) — tabela foeventosdef (módulo folha, ~1.695 linhas).
O QUE É: Cadastro global de rubricas-modelo da Domínio. Empresas sem eventos próprios (309 delas têm movimento de folha) usam estes. Tem as mesmas marcações de `evento`, sem filtro de empresa.
COMENTÁRIO DO BANCO SOBRE A TABELA: Eventos Padrao
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
Tabela global (não depende de empresa): NÃO informe 'empresa'.
FILTROS: codigo, nome, tipo, aparece_recibo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, nome, tipo, unidade, aparece_recibo, soma_ficha_financeira, base_inss, base_irrf, base_fgts. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `codigo`: Filtra i_eventos (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Codigo)
- `nome`: Filtra nome (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Nome)
- `tipo`: Filtra prov_desc (varchar). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: P=Provento, D=Desconto, I=Informativo (não soma), ID=Informativo de desconto (inferido) [parcialmente confirmado] (Tipo)
- `aparece_recibo`: Filtra aparece_recibo (char). Aceita: valor simples (igualdade), igual. Códigos: S=Sim, N=Não (Aparece no Recibo)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `evento_padrao_obter`

Eventos padrão (rubricas-modelo) — obtém UM registro pela chave (i_eventos) da tabela foeventosdef. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use evento_padrao_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `codigo` (obrigatório): Filtra i_eventos (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Codigo)

## `falta_consultar`

Faltas — tabela FOFALTAS (módulo folha, ~15.865 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: CADASTRO DE FALTAS DOS EMPREGADOS
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DIA. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: empregado_codigo, dia, tipo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: empregado_codigo, sequencial, dia, tipo, origem, horas. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): empregado_nome.
EXEMPLO COM DADOS: a empresa 1557 tem registros nesta tabela (use para testar).
PRIVACIDADE (folha): as linhas são de empregados identificáveis; evite listar pessoas sem necessidade.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `empregado_codigo`: Filtra I_EMPREGADOS (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CODIGO)
- `dia`: Filtra DIA (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (DIA QUE OCORREU A FALTA) Datas no formato AAAA-MM-DD.
- `tipo`: Filtra TIPO (smallint). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Normal, 2=DSR, 3=Reembolso, 4=Parcial, 5=Noturna, 6=DSR noturna, 7=Suspensão, 8=DSR suspensão (Tipo de falta. (1=Normal/2=DSR/3=Reembolso/4=Parcial/5=Noturna/6=DSR Noturna/7=Suspensão/8=DSR suspensão))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `falta_totais`

Faltas — TOTAIS por grupo da tabela FOFALTAS (módulo folha). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DIA. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: horas. CAMPOS PARA AGRUPAR: empregado_codigo, sequencial, dia:mes, tipo, origem. Os filtros são os mesmos de falta_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (tipo, origem) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `empregado_codigo`: Filtra I_EMPREGADOS (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CODIGO)
- `dia`: Filtra DIA (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (DIA QUE OCORREU A FALTA) Datas no formato AAAA-MM-DD.
- `tipo`: Filtra TIPO (smallint). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Normal, 2=DSR, 3=Reembolso, 4=Parcial, 5=Noturna, 6=DSR noturna, 7=Suspensão, 8=DSR suspensão (Tipo de falta. (1=Normal/2=DSR/3=Reembolso/4=Parcial/5=Noturna/6=DSR Noturna/7=Suspensão/8=DSR suspensão))
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["dia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["horas"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `ferias_periodo_aquisitivo_consultar`

Férias — períodos aquisitivos — tabela FOFERIAS_AQUISITIVOS (módulo folha, ~23.266 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: CADASTRO DE PERIODOS ARQUISITIVOS
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DATA_INICIO. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: empregado_codigo, data_inicio, limite_para_gozo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: empregado_codigo, sequencia, data_inicio, data_fim, situacao, dias_direito, dias_gozados, dias_abono, dias_faltas, avos_adquiridos, limite_para_gozo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): empregado_nome.
EXEMPLO COM DADOS: a empresa 864 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): situacao (GOZADO, PERDIDA etc., segundo o comentário) é um código sem tabela de descrição: significado não confirmado.
PRIVACIDADE (folha): as linhas são de empregados identificáveis; evite listar pessoas sem necessidade.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `empregado_codigo`: Filtra I_EMPREGADOS (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CODIGO)
- `data_inicio`: Filtra DATA_INICIO (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (DATA DO INICIO DO PERIODO AQUISITIVO) Datas no formato AAAA-MM-DD.
- `limite_para_gozo`: Filtra LIMITE_PARA_GOZO (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (DIA MAXIMO PARA INICIO O GOZO SEM MULTA) Datas no formato AAAA-MM-DD.
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `ferias_periodo_aquisitivo_totais`

Férias — períodos aquisitivos — TOTAIS por grupo da tabela FOFERIAS_AQUISITIVOS (módulo folha). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DATA_INICIO. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: dias_direito, dias_gozados, dias_abono, dias_faltas. CAMPOS PARA AGRUPAR: empregado_codigo, sequencia, data_inicio:mes, data_fim:mes, situacao, avos_adquiridos, limite_para_gozo:mes. Os filtros são os mesmos de ferias_periodo_aquisitivo_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: situacao (GOZADO, PERDIDA etc., segundo o comentário) é um código sem tabela de descrição: significado não confirmado.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `empregado_codigo`: Filtra I_EMPREGADOS (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CODIGO)
- `data_inicio`: Filtra DATA_INICIO (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (DATA DO INICIO DO PERIODO AQUISITIVO) Datas no formato AAAA-MM-DD.
- `limite_para_gozo`: Filtra LIMITE_PARA_GOZO (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (DIA MAXIMO PARA INICIO O GOZO SEM MULTA) Datas no formato AAAA-MM-DD.
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["data_inicio:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["dias_direito"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `ferias_gozo_consultar`

Férias — gozo — tabela FOFERIAS_GOZO (módulo folha, ~19.023 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: CONTROLE DE GOZO DE FERIAS
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna GOZO_INICIO. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: empregado_codigo, gozo_inicio, tipo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: empregado_codigo, sequencia, periodo_aquisitivo, gozo_inicio, gozo_fim, paga_abono, abono_inicio, abono_fim, data_pagamento, paga_adiantamento_13, dias_faltas, tipo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): empregado_nome.
EXEMPLO COM DADOS: a empresa 421 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): tipo 5 (provisão), 7 e 8 (simulação) NÃO são férias efetivamente gozadas; filtre tipo in (1,2,3,4,6) para férias reais.
PRIVACIDADE (folha): as linhas são de empregados identificáveis; evite listar pessoas sem necessidade.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `empregado_codigo`: Filtra I_EMPREGADOS (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CODIGO)
- `gozo_inicio`: Filtra GOZO_INICIO (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (INICIO DO GOZO) Datas no formato AAAA-MM-DD.
- `tipo`: Filtra TIPO (smallint). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Individual, 2=Coletiva, 3=Rescisão, 4=Manual, 5=Provisão, 6=Acerto, 7=Simulação de férias, 8=Simulação de rescisão (Tipo de cálculo das férias. (1=Individual/2=Coletiva/3=Rescisão/4=Manual/5=Provisão/6=Acerto/7=Simulação férias/8=Simulação rescisão))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `ferias_gozo_totais`

Férias — gozo — TOTAIS por grupo da tabela FOFERIAS_GOZO (módulo folha). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna GOZO_INICIO. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: dias_faltas. CAMPOS PARA AGRUPAR: empregado_codigo, sequencia, periodo_aquisitivo, gozo_inicio:mes, gozo_fim:mes, paga_abono, abono_inicio:mes, abono_fim:mes, data_pagamento:mes, paga_adiantamento_13, tipo. Os filtros são os mesmos de ferias_gozo_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (paga_abono, paga_adiantamento_13, tipo) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: tipo 5 (provisão), 7 e 8 (simulação) NÃO são férias efetivamente gozadas; filtre tipo in (1,2,3,4,6) para férias reais.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `empregado_codigo`: Filtra I_EMPREGADOS (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CODIGO)
- `gozo_inicio`: Filtra GOZO_INICIO (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (INICIO DO GOZO) Datas no formato AAAA-MM-DD.
- `tipo`: Filtra TIPO (smallint). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Individual, 2=Coletiva, 3=Rescisão, 4=Manual, 5=Provisão, 6=Acerto, 7=Simulação de férias, 8=Simulação de rescisão (Tipo de cálculo das férias. (1=Individual/2=Coletiva/3=Rescisão/4=Manual/5=Provisão/6=Acerto/7=Simulação férias/8=Simulação rescisão))
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["gozo_inicio:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["dias_faltas"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `filial_folha_consultar`

Filiais (folha) — tabela fofiliais (módulo folha, ~1.672 linhas).
O QUE É: Estabelecimentos da empresa na folha (CNPJ da filial). Dados de pessoa jurídica.
COMENTÁRIO DO BANCO SOBRE A TABELA: Filiais - Cadastro
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, nome. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, nome, razao_social, tipo_inscricao, inscricao, inscricao_estadual, cnae, cidade, uf, municipio_codigo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 1403 tem registros nesta tabela (use para testar).
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra i_filiais (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `nome`: Filtra nome (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Nome)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `filial_folha_obter`

Filiais (folha) — obtém UM registro pela chave (codi_emp, i_filiais) da tabela fofiliais. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use filial_folha_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra i_filiais (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `liquido_folha_consultar`

Líquido a pagar — tabela foliquidosfilepr (módulo folha, ~216.930 linhas).
O QUE É: Líquido registrado pela Domínio para pagamento, por empregado e cálculo.
COMENTÁRIO DO BANCO SOBRE A TABELA: Liquidos por filial - Empregados
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): empregado_codigo.
FILTROS: empregado_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: empregado_codigo, liquido, sequencial, numero_rpa, calculo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): empregado_nome.
EXEMPLO COM DADOS: a empresa 715 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Não há data nesta tabela; a competência vem do cálculo (calculo = base_folha.calculo).
PRIVACIDADE: Valor líquido por empregado identificável (financeiro). Os dados saem em claro nesta versão do servidor: devolva só o que a pergunta exigir.
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): liquido
PRIVACIDADE (folha): as linhas são de empregados identificáveis; evite listar pessoas sem necessidade.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `empregado_codigo`: Filtra i_empregados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo do empregado)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `liquido_folha_totais`

Líquido a pagar — TOTAIS por grupo da tabela foliquidosfilepr (módulo folha). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): empregado_codigo. CAMPOS SOMÁVEIS: liquido. CAMPOS PARA AGRUPAR: empregado_codigo, sequencial, numero_rpa, calculo. Os filtros são os mesmos de liquido_folha_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Não há data nesta tabela; a competência vem do cálculo (calculo = base_folha.calculo).. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `empregado_codigo`: Filtra i_empregados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo do empregado)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["empregado_codigo"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["liquido"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `movimento_folha_consultar`

Movimento da folha (valores por evento) — tabela fomovtoserv (módulo folha, ~2.927.129 linhas).
O QUE É: Uma linha por evento (rubrica) calculado de cada empregado, competência e tipo de folha — o "recibo" aberto. O identificador do cálculo (calculo) é um GUID e faz parte da chave.
COMENTÁRIO DO BANCO SOBRE A TABELA: Movimentacao - Calculo
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): periodo, empregado_codigo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna data. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: empregado_codigo, competencia, tipo_folha, evento_codigo, tipo_evento, simulacao. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: empregado_codigo, competencia, tipo_folha, evento_codigo, tipo_evento, valor_calculado, valor_informado, valor_calculado_integral, origem, rateio, servico_codigo, simulacao, calculo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): evento_proprio_nome, evento_proprio_aparece_recibo, evento_padrao_nome, evento_padrao_aparece_recibo, empregado_nome.
EXEMPLO COM DADOS: a empresa 1476 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): REGRA DOS EVENTOS (validada): o evento de um movimento é buscado primeiro no cadastro da própria empresa (foeventos) e, se não existir, nos eventos padrão (foeventosdef). 208.504 movimentos (7,1%) de 310 empresas não têm evento próprio; 309 dessas empresas não têm NENHUM evento próprio e usam só os padrões (92% dos casos resolvem pelos padrões; […] | Para somar proventos/descontos como a Domínio: some valor_calculado dos eventos tipo P ou D com evento_aparece_recibo = 'S'. Evento sem cadastro nenhum (nem próprio nem padrão) CONTA (default 'S'). Com essa regra: proventos batem em 65.869 de 65.877 linhas de base (100,0%) e descontos em 65.560 (99,5%), […] | competencia é sempre o dia 1º do mês (data = primeiro dia da competência). | Há competências futuras já calculadas (até 2026-12): filtre por período. | origem 'F' (172 mil linhas) são cálculos de férias; 'C' são da folha mensal e demais.
PRIVACIDADE: Valores pagos por empregado identificável (financeiro). Os dados saem em claro nesta versão do servidor: devolva só o que a pergunta exigir.
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): valor_calculado, valor_informado, valor_calculado_integral
PRIVACIDADE (folha): as linhas são de empregados identificáveis; evite listar pessoas sem necessidade.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `empregado_codigo`: Filtra i_empregados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Empregado)
- `competencia`: Filtra data (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia) Datas no formato AAAA-MM-DD.
- `tipo_folha`: Filtra tipo_proces (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 11=Mensal, 31=1ª semana, 32=2ª semana, 33=3ª semana, 34=4ª semana, 35=Última semana, 36=Todas as semanas, 41=Adiantamento, 42=Complementar, 51=Adiantamento de 13º salário, … (+3) [parcialmente confirmado] (Tipo folha)
- `evento_codigo`: Filtra i_eventos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Evento)
- `tipo_evento`: Filtra prov_desc (varchar). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: P=Provento, D=Desconto, I=Informativo (não soma), ID=Informativo de desconto (inferido) [parcialmente confirmado] (Provento/Desconto)
- `simulacao`: Filtra SIMULACAO (smallint). Aceita: valor simples (igualdade), igual. (Simulação de cálculo. (0=Não/1=Sim))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `movimento_folha_totais`

Movimento da folha (valores por evento) — TOTAIS por grupo da tabela fomovtoserv (módulo folha). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): periodo, empregado_codigo. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna data. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor_calculado, valor_informado, valor_calculado_integral. CAMPOS PARA AGRUPAR: empregado_codigo, competencia:mes, tipo_folha, evento_codigo, tipo_evento, origem, rateio, servico_codigo, simulacao, calculo. Os filtros são os mesmos de movimento_folha_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (tipo_folha, tipo_evento, origem) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: REGRA DOS EVENTOS (validada): o evento de um movimento é buscado primeiro no cadastro da própria empresa (foeventos) e, se não existir, nos eventos padrão (foeventosdef). 208.504 movimentos (7,1%) de 310 empresas não têm evento próprio; 309 dessas empresas não têm NENHUM evento próprio e usam só os padrões (92% dos casos resolvem pelos padrões; o resto existe só em outra empresa). […] | Para somar proventos/descontos como a Domínio: some valor_calculado dos eventos tipo P ou D com evento_aparece_recibo = 'S'. Evento sem cadastro nenhum (nem próprio nem padrão) CONTA (default 'S'). Com essa regra: proventos batem em 65.869 de 65.877 linhas de base (100,0%) e descontos em 65.560 (99,5%), em 9 empresas incluindo as que só usam eventos padrão. Sem o default 'S' a regra falha nessas empresas (ex.: 19% na empresa 37). | competencia é sempre o dia 1º do mês (data = primeiro dia da competência). | Há competências futuras já calculadas (até 2026-12): filtre por período.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `empregado_codigo`: Filtra i_empregados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Empregado)
- `competencia`: Filtra data (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia) Datas no formato AAAA-MM-DD.
- `tipo_folha`: Filtra tipo_proces (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 11=Mensal, 31=1ª semana, 32=2ª semana, 33=3ª semana, 34=4ª semana, 35=Última semana, 36=Todas as semanas, 41=Adiantamento, 42=Complementar, 51=Adiantamento de 13º salário, … (+3) [parcialmente confirmado] (Tipo folha)
- `evento_codigo`: Filtra i_eventos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Evento)
- `tipo_evento`: Filtra prov_desc (varchar). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: P=Provento, D=Desconto, I=Informativo (não soma), ID=Informativo de desconto (inferido) [parcialmente confirmado] (Provento/Desconto)
- `simulacao`: Filtra SIMULACAO (smallint). Aceita: valor simples (igualdade), igual. (Simulação de cálculo. (0=Não/1=Sim))
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["competencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor_calculado"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `rescisao_consultar`

Rescisões — tabela forescisoes (módulo folha, ~7.192 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: Rescisao - Calculo
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna demissao. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: empregado_codigo, demissao, motivo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: empregado_codigo, tipo, calculo, demissao, motivo, data_aviso, aviso_indenizado, avos_13, ferias_vencidas, meses_ferias_proporcionais, codigo_saque_fgts, salario, proventos, descontos, saldo_fgts, fgts_rescisao, liquido. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): empregado_nome, empregado_admissao.
EXEMPLO COM DADOS: a empresa 9060 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): A chave é (empresa, cálculo, empregado, tipo): um empregado pode ter mais de uma linha (rescisão normal e complementar). Hoje há 6.904 normais (tipo 1) e 288 complementares (tipo 2); simulações (tipo 4) não aparecem. | Para contar demissões, filtre tipo = 1; somar normal + complementar duplica o evento de desligamento. | motivo é um código sem tabela de descrição no banco (mais frequentes: 2, 4, 43, 99, 10, 27, 11, 12): significado não confirmado.
PRIVACIDADE: Verbas rescisórias por empregado identificável (financeiro). Os dados saem em claro nesta versão do servidor: devolva só o que a pergunta exigir.
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): salario, proventos, descontos, saldo_fgts, fgts_rescisao
PRIVACIDADE (folha): as linhas são de empregados identificáveis; evite listar pessoas sem necessidade.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `empregado_codigo`: Filtra i_empregados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Empregado)
- `demissao`: Filtra demissao (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data Demissao) Datas no formato AAAA-MM-DD.
- `motivo`: Filtra motivo (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Motivo)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `rescisao_totais`

Rescisões — TOTAIS por grupo da tabela forescisoes (módulo folha). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna demissao. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: salario, proventos, descontos, saldo_fgts. CAMPOS PARA AGRUPAR: empregado_codigo, tipo, calculo, demissao:mes, motivo, data_aviso:mes, aviso_indenizado, avos_13, ferias_vencidas, meses_ferias_proporcionais, codigo_saque_fgts, fgts_rescisao. Os filtros são os mesmos de rescisao_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (tipo, aviso_indenizado) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: A chave é (empresa, cálculo, empregado, tipo): um empregado pode ter mais de uma linha (rescisão normal e complementar). Hoje há 6.904 normais (tipo 1) e 288 complementares (tipo 2); simulações (tipo 4) não aparecem. | Para contar demissões, filtre tipo = 1; somar normal + complementar duplica o evento de desligamento. | motivo é um código sem tabela de descrição no banco (mais frequentes: 2, 4, 43, 99, 10, 27, 11, 12): significado não confirmado.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `empregado_codigo`: Filtra i_empregados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Empregado)
- `demissao`: Filtra demissao (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data Demissao) Datas no formato AAAA-MM-DD.
- `motivo`: Filtra motivo (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Motivo)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["demissao:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["salario"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `servico_folha_consultar`

Serviços / tomadores (folha) — tabela foservicos (módulo folha, ~1.770 linhas).
O QUE É: Código de serviço usado no rateio da folha (a maior parte das colunas do banco está marcada SEM USO).
COMENTÁRIO DO BANCO SOBRE A TABELA: Servico - Cadastro
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, nome. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, nome, situacao, data_inicio, data_inativacao. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 9084 tem registros nesta tabela (use para testar).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra i_servicos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `nome`: Filtra nome (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Nome)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `servico_folha_obter`

Serviços / tomadores (folha) — obtém UM registro pela chave (codi_emp, i_servicos) da tabela foservicos. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use servico_folha_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra i_servicos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `sindicato_consultar`

Sindicatos / convenções coletivas — tabela fosindicatos (módulo folha, ~155 linhas).
O QUE É: Cadastro global (não depende de empresa) de convenções coletivas e regras de cálculo.
COMENTÁRIO DO BANCO SOBRE A TABELA: Convenção Coletiva - Cadastro
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
Tabela global (não depende de empresa): NÃO informe 'empresa'.
FILTROS: codigo, nome. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, nome, piso_salarial, mes_base, mes_contribuicao, adicional_noturno_percentual, dias_multa_rescisao, percentual_multa_rescisao. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `codigo`: Filtra i_sindicatos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código da convenção coletiva)
- `nome`: Filtra nome (varchar). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Nome)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `sindicato_obter`

Sindicatos / convenções coletivas — obtém UM registro pela chave (i_sindicatos) da tabela fosindicatos. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use sindicato_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `codigo` (obrigatório): Filtra i_sindicatos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código da convenção coletiva)

## `sindicato_totais`

Sindicatos / convenções coletivas — TOTAIS por grupo da tabela fosindicatos (módulo folha). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. Tabela global (não depende de empresa): NÃO informe 'empresa'. CAMPOS SOMÁVEIS: dias_multa_rescisao. CAMPOS PARA AGRUPAR: codigo, nome, piso_salarial, mes_base, mes_contribuicao, adicional_noturno_percentual, percentual_multa_rescisao. Os filtros são os mesmos de sindicato_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. Somente leitura.

Parâmetros:

- `codigo`: Filtra i_sindicatos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código da convenção coletiva)
- `nome`: Filtra nome (varchar). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Nome)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["codigo"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["dias_multa_rescisao"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).
