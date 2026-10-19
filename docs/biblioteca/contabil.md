# Módulo `contabil`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `centro_custo_consultar` | consultar | ctccusto | empresa | ✔ |
| `centro_custo_obter` | obter | ctccusto | empresa, codigo | ✔ |
| `lancamento_centro_custo_consultar` | consultar | ctclancto | empresa | ✔ |
| `lancamento_centro_custo_totais` | totais | ctclancto | empresa | ✔ |
| `conta_contabil_consultar` | consultar | ctcontas | empresa | ✔ |
| `conta_contabil_obter` | obter | ctcontas | empresa, codigo | ✔ |
| `departamento_consultar` | consultar | ctdepto | empresa | ✔ |
| `departamento_obter` | obter | ctdepto | empresa, codigo | ✔ |
| `historico_padrao_consultar` | consultar | cthispad | empresa | ✔ |
| `historico_padrao_obter` | obter | cthispad | empresa, codigo | ✔ |
| `lancamento_consultar` | consultar | ctlancto | empresa | ✔ |
| `lancamento_obter` | obter | ctlancto | empresa, numero | ✔ |
| `lancamento_totais` | totais | ctlancto | empresa | ✔ |
| `lote_lancamento_consultar` | consultar | ctlanctolote | empresa | ✔ |
| `lote_lancamento_obter` | obter | ctlanctolote | empresa, codigo | ✔ |
| `lancamento_padrao_consultar` | consultar | ctlanctopadrao | empresa | ✔ |
| `lancamento_padrao_obter` | obter | ctlanctopadrao | empresa, codigo | ✔ |
| `contabilizacao_nota_entrada_consultar` | consultar | efentradas_lancto | empresa | ✔ |
| `contabilizacao_nota_saida_consultar` | consultar | efsaidas_lancto | empresa | ✔ |
| `contabilizacao_nota_servico_consultar` | consultar | efservicos_lancto | empresa | ✔ |

## `centro_custo_consultar`

Centros de custo — tabela ctccusto (módulo contabil, ~1.383 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: Cadastro - Cadastro de centro de custos da contabilidade
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, descricao. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, descricao, departamento_codigo, data_cadastro. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): departamento_nome.
EXEMPLO COM DADOS: a empresa 691 tem registros nesta tabela (use para testar).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra codi_ccu (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `descricao`: Filtra desc_ccu (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Descricao)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `centro_custo_obter`

Centros de custo — obtém UM registro pela chave (codi_emp, codi_ccu) da tabela ctccusto. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use centro_custo_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra codi_ccu (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `lancamento_centro_custo_consultar`

Rateio de lançamentos por centro de custo — tabela ctclancto (módulo contabil, ~46.687 linhas).
O QUE É: Distribuição de um lançamento entre centros de custo (apenas empresas que usam centro de custo).
COMENTÁRIO DO BANCO SOBRE A TABELA: Lancamento do centro de custo
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna data_ccu. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: numero_lancamento, data, conta_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: numero_lancamento, conta_debito_centro, conta_credito_centro, conta_codigo, data, valor, filial, lancamento_contabil. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 641 tem registros nesta tabela (use para testar).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `numero_lancamento`: Filtra nume_ccu (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Numero do lancamento)
- `data`: Filtra data_ccu (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data do lancamento) Datas no formato AAAA-MM-DD.
- `conta_codigo`: Filtra codi_cta (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta contabil)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `lancamento_centro_custo_totais`

Rateio de lançamentos por centro de custo — TOTAIS por grupo da tabela ctclancto (módulo contabil). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna data_ccu. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor, lancamento_contabil. CAMPOS PARA AGRUPAR: numero_lancamento, conta_debito_centro, conta_credito_centro, conta_codigo, data:mes, filial. Os filtros são os mesmos de lancamento_centro_custo_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `numero_lancamento`: Filtra nume_ccu (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Numero do lancamento)
- `data`: Filtra data_ccu (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data do lancamento) Datas no formato AAAA-MM-DD.
- `conta_codigo`: Filtra codi_cta (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta contabil)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["data:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `conta_contabil_consultar`

Plano de contas — tabela ctcontas (módulo contabil, ~1.574.175 linhas).
O QUE É: Contas contábeis. ATENÇÃO: `empresa` aqui é a empresa DONA DO PLANO. Se a empresa consultada usa o plano de outra, informe a empresa do plano (ctlancto.codi_emp_plano). Só contas analíticas (tipo A) recebem lançamentos.
COMENTÁRIO DO BANCO SOBRE A TABELA: Contas Contabeis - Cadastro
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, classificacao, nome, tipo, situacao. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, classificacao, nome, tipo, situacao, data_cadastro, data_inativacao, grupo_dre, grupo_dlpa, grupo_doar, grupo_dmpl, grupo_dra, grupo_dsp, grupo_ebitda, grupo_lcdpr. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 1593 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): clas_cta é a classificação hierárquica (ex.: 1.1.01...): contas sintéticas totalizam as analíticas cujo clas_cta começa pelo mesmo prefixo. | Só contas analíticas (A) recebem lançamentos (13.267.083 lançamentos em contas A contra 33 em contas S — exceções de dado).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra codi_cta (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `classificacao`: Filtra clas_cta (char). Aceita: valor simples (igualdade), igual, {"prefixo":"x"}. (Classificacao)
- `nome`: Filtra nome_cta (varchar). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Descricao)
- `tipo`: Filtra tipo_cta (char). Aceita: valor simples (igualdade), igual. Códigos: A=Analítica (recebe lançamentos), S=Sintética (apenas totaliza) (Tipo (A=Analitico/S=Sintetico))
- `situacao`: Filtra SITUACAO_CTA (char). Aceita: valor simples (igualdade), igual. Códigos: A=Ativa, I=Inativa (Situacao (A-Ativa/I-Inativa))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `conta_contabil_obter`

Plano de contas — obtém UM registro pela chave (codi_emp, codi_cta) da tabela ctcontas. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use conta_contabil_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra codi_cta (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `departamento_consultar`

Departamentos (contabilidade) — tabela ctdepto (módulo contabil, ~1.372 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: Departamentos - Cadastro
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, descricao. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, descricao. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 691 tem registros nesta tabela (use para testar).
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
UTILIDADE LIMITADA: a tabela expõe só 2 campo(s) (tabela de apoio/ligação); ela NÃO traz o conteúdo que o nome pode sugerir (XML, arquivo, etc.).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra codi_dep (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `descricao`: Filtra desc_dep (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Descricao)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `departamento_obter`

Departamentos (contabilidade) — obtém UM registro pela chave (codi_emp, codi_dep) da tabela ctdepto. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use departamento_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra codi_dep (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `historico_padrao_consultar`

Históricos padrão — tabela cthispad (módulo contabil, ~266.424 linhas).
O QUE É: Textos-modelo de histórico, pertencentes ao plano (use a empresa do plano). 64% dos lançamentos não usam código de histórico e trazem o texto livre em chis_lan.
COMENTÁRIO DO BANCO SOBRE A TABELA: Historicos Padroes - Cadastro
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, descricao. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, descricao. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 1071 tem registros nesta tabela (use para testar).
UTILIDADE LIMITADA: a tabela expõe só 2 campo(s) (tabela de apoio/ligação); ela NÃO traz o conteúdo que o nome pode sugerir (XML, arquivo, etc.).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra codi_his (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `descricao`: Filtra desc_his (varchar). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Descricao)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `historico_padrao_obter`

Históricos padrão — obtém UM registro pela chave (codi_emp, codi_his) da tabela cthispad. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use historico_padrao_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra codi_his (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `lancamento_consultar`

Lançamentos contábeis — tabela ctlancto (módulo contabil, ~13.712.713 linhas).
O QUE É: Livro diário: uma linha por lançamento. Cada lançamento tem valor, conta a débito (cdeb_lan) e conta a crédito (ccre_lan); o valor 0 em um dos lados significa linha de lote com vários débitos ou créditos. Contas e histórico são do PLANO (codi_emp_plano), que pode ser de outra empresa.
COMENTÁRIO DO BANCO SOBRE A TABELA: Lancamentos Contabeis
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): periodo, numero, lote_codigo, documento.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna data_lan. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: numero, data, conta, conta_debito, conta_credito, valor, lote_codigo, origem, documento, filial, historico_codigo, usuario. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: numero, data, valor, conta_debito, conta_credito, plano_empresa, historico_codigo, historico, lote_codigo, lancamento_padrao_codigo, origem, documento, filial, data_original, data_ocorrencia, conciliado_debito, conciliado_credito, usuario, origem_registro, cpf_titular_pagamento, cpf_beneficiario_servico. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): conta_debito_classificacao, conta_debito_nome, conta_credito_classificacao, conta_credito_nome, historico_padrao_descricao, lote_tipo.
EXEMPLO COM DADOS: a empresa 1125 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Equilíbrio: em cada lote, soma dos valores com débito = soma dos valores com crédito. Conferido nos 40.317 lotes da empresa 1430 (tipos X, V, C e D: 100% equilibrados; total de débitos = créditos = 248.988.467,04). | vlor_lan nunca é negativo (0 negativos em 13,7 mi); 91 lançamentos têm valor 0. | Conta e histórico: ligar pelo PLANO (plano_empresa = CODI_EMP_PLANO), não por codi_emp. A ligação com o histórico não aparece nos JOINs dos programas da Domínio (por isso o validador avisa 'sem relação no grafo'); ela se sustenta nos dados: 0 órfãos por plano, contra 781 de 781 por codi_emp nos lançamentos de plano alheio. | Elo com a escrita fiscal: orig 5/6/7 ligam a efsaidas_lancto/efentradas_lancto/efservicos_lancto. REGRA ROBUSTA: o MAIOR lançamento ligado a uma nota é igual ao valor contábil dela (98,8% a 100% em 6 amostras de empresas e tipos de nota). […] | Datas: há lançamentos com data absurda (143 acima de 2100, ex.: 9282-06-06) — erro de digitação nos dados; filtre por período. (+1 regras: veja descrever_entidade)
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): cpf_titular_pagamento, cpf_beneficiario_servico
POSSÍVEIS DADOS PESSOAIS/FINANCEIROS (os dados saem em claro; devolva só o que a pergunta exigir): usuario.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `numero`: Filtra nume_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Numero)
- `data`: Filtra data_lan (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data) Datas no formato AAAA-MM-DD.
- `conta`: Filtra cdeb_lan (integer) OU ccre_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Debito)
- `conta_debito`: Filtra cdeb_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Debito)
- `conta_credito`: Filtra ccre_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Credito)
- `valor`: Filtra vlor_lan (numeric). Aceita: valor simples (igualdade), igual, {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Valor)
- `lote_codigo`: Filtra codi_lote (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Lancamento em lote)
- `origem`: Filtra orig_lan (tinyint). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Normal (digitado/importado), 2=Zeramento (comentário; não confirmado), 3=Patrimônio (comentário; não confirmado), 5=Escrita fiscal - saídas (confirmado), 6=Escrita fiscal - entradas (confirmado), 7=Escrita fiscal - serviços (confirmado), 10=Apuração de impostos (confirmado), 11=Pagamento de guia (confirmado), 13=Folha (comentário; não confirmado), […]
- `documento`: Filtra ndoc_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Relacao com Escrita Fiscal)
- `filial`: Filtra fili_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Filial)
- `historico_codigo`: Filtra codi_his (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo Historico)
- `usuario`: Filtra codi_usu (char). Aceita: valor simples (igualdade), igual. (Usuario)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `lancamento_obter`

Lançamentos contábeis — obtém UM registro pela chave (codi_emp, nume_lan) da tabela ctlancto. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use lancamento_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `numero` (obrigatório): Filtra nume_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Numero)

## `lancamento_totais`

Lançamentos contábeis — TOTAIS por grupo da tabela ctlancto (módulo contabil). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): periodo, numero, lote_codigo, documento. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna data_lan. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor. CAMPOS PARA AGRUPAR: numero, data:mes, conta_debito, conta_credito, plano_empresa, historico_codigo, historico, lote_codigo, lancamento_padrao_codigo, origem, documento, filial, data_original:mes, data_ocorrencia:mes, conciliado_debito, conciliado_credito, usuario, origem_registro, cpf_titular_pagamento, cpf_beneficiario_servico. Os filtros são os mesmos de lancamento_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (origem, conciliado_debito, conciliado_credito) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Equilíbrio: em cada lote, soma dos valores com débito = soma dos valores com crédito. Conferido nos 40.317 lotes da empresa 1430 (tipos X, V, C e D: 100% equilibrados; total de débitos = créditos = 248.988.467,04). | vlor_lan nunca é negativo (0 negativos em 13,7 mi); 91 lançamentos têm valor 0. | Conta e histórico: ligar pelo PLANO (plano_empresa = CODI_EMP_PLANO), não por codi_emp. A ligação com o histórico não aparece nos JOINs dos programas da Domínio (por isso o validador avisa 'sem relação no grafo'); ela se sustenta nos dados: 0 órfãos por plano, contra 781 de 781 por codi_emp nos lançamentos de plano alheio. | Elo com a escrita fiscal: orig 5/6/7 ligam a efsaidas_lancto/efentradas_lancto/efservicos_lancto. REGRA ROBUSTA: o MAIOR lançamento ligado a uma nota é igual ao valor contábil dela (98,8% a 100% em 6 amostras de empresas e tipos de nota). A SOMA dos lançamentos ligados só fecha com o valor da nota quando a empresa contabiliza apenas o total (100% em saídas da empresa 1430; 65%, 33% e 64% em outras empresas), […]. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `numero`: Filtra nume_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Numero)
- `data`: Filtra data_lan (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data) Datas no formato AAAA-MM-DD.
- `conta`: Filtra cdeb_lan (integer) OU ccre_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Debito)
- `conta_debito`: Filtra cdeb_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Debito)
- `conta_credito`: Filtra ccre_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Credito)
- `valor`: Filtra vlor_lan (numeric). Aceita: valor simples (igualdade), igual, {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Valor)
- `lote_codigo`: Filtra codi_lote (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Lancamento em lote)
- `origem`: Filtra orig_lan (tinyint). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Normal (digitado/importado), 2=Zeramento (comentário; não confirmado), 3=Patrimônio (comentário; não confirmado), 5=Escrita fiscal - saídas (confirmado), 6=Escrita fiscal - entradas (confirmado), 7=Escrita fiscal - serviços (confirmado), 10=Apuração de impostos (confirmado), 11=Pagamento de guia (confirmado), 13=Folha (comentário; não confirmado), […]
- `documento`: Filtra ndoc_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Relacao com Escrita Fiscal)
- `filial`: Filtra fili_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Filial)
- `historico_codigo`: Filtra codi_his (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo Historico)
- `usuario`: Filtra codi_usu (char). Aceita: valor simples (igualdade), igual. (Usuario)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["data:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `lote_lancamento_consultar`

Lotes de lançamento — tabela ctlanctolote (módulo contabil, ~12.642.297 linhas).
O QUE É: Todo lançamento pertence a um lote (nenhum lançamento sem lote). O equilíbrio contábil (débitos = créditos) vale POR LOTE: no tipo X há 1 débito e 1 crédito na mesma linha; nos tipos D, C e V as linhas têm um dos lados zerado.
COMENTÁRIO DO BANCO SOBRE A TABELA: Lancamento em lote
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, tipo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, tipo, lancamento_padrao_codigo, localizador. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 1690 tem registros nesta tabela (use para testar).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra codi_lote (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Codigo)
- `tipo`: Filtra tipo (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: X=Um débito para um crédito, D=Um débito para vários créditos, C=Um crédito para vários débitos, V=Vários débitos para vários créditos (Tipo (D=Um debito para varios creditos/C=Um credito para varios debitos/X=Um debito para um credito/V=Varios debitos para varios creditos))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `lote_lancamento_obter`

Lotes de lançamento — obtém UM registro pela chave (codi_emp, codi_lote) da tabela ctlanctolote. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use lote_lancamento_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra codi_lote (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Codigo)

## `lancamento_padrao_consultar`

Lançamentos padrão — tabela ctlanctopadrao (módulo contabil, ~522 linhas).
O QUE É: Modelos de lançamento (contas e histórico pré-definidos).
COMENTÁRIO DO BANCO SOBRE A TABELA: Lancamentos Padroes em Lote - Cadastro
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, descricao. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, descricao, conta_debito, conta_credito, historico_codigo, tipo, filial. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 10052 tem registros nesta tabela (use para testar).
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra codi_pad (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `descricao`: Filtra desc_pad (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Descricao)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `lancamento_padrao_obter`

Lançamentos padrão — obtém UM registro pela chave (codi_emp, codi_pad) da tabela ctlanctopadrao. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use lancamento_padrao_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra codi_pad (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `contabilizacao_nota_entrada_consultar`

Contabilização das notas de entrada — tabela efentradas_lancto (módulo contabil, ~552.148 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: Notas de entradas X Lancamentos contabeis
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): codigo_nota, numero_lancamento.
FILTROS: codigo_nota, numero_lancamento. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo_nota, numero_lancamento, empresa_lancamento. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): lancamento_data, lancamento_valor, lancamento_conta_debito, lancamento_conta_credito.
EXEMPLO COM DADOS: a empresa 1004 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): O maior lancamento_valor ligado a uma nota de entrada é igual a vcon_ent em 99,9% (empresa 1430) e 100% (empresa 1047). A soma fecha em 95% (empresa 1430) mas só em 33% (empresa 1047).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo_nota`: Filtra codi_ent (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo da nota)
- `numero_lancamento`: Filtra nume_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Numero do lancamento)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `contabilizacao_nota_saida_consultar`

Contabilização das notas de saída — tabela efsaidas_lancto (módulo contabil, ~418.808 linhas).
O QUE É: Liga cada nota de saída (efsaidas) aos lançamentos que a contabilizaram. `empresa` = empresa da NOTA; `empresa_lancamento` (fili_lan) = empresa em cujo livro o lançamento foi feito — difere em 17% das linhas (notas de filiais contabilizadas na matriz).
COMENTÁRIO DO BANCO SOBRE A TABELA: Notas de saidas X Lancamentos contabeis
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): codigo_nota, numero_lancamento.
FILTROS: codigo_nota, numero_lancamento. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo_nota, numero_lancamento, empresa_lancamento, tipo, origem_lancamento. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): lancamento_data, lancamento_valor, lancamento_conta_debito, lancamento_conta_credito.
EXEMPLO COM DADOS: a empresa 229 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): O MAIOR lancamento_valor entre as linhas ligadas a uma nota de saída (cancelada='N') é igual a vcon_sai em 100% (empresa 1430) e 99,9% (empresa 879). NÃO assuma que a soma é igual: ela fecha em 100% na empresa 1430, mas em 65% na 879 (lançamentos adicionais de imposto/retenção).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo_nota`: Filtra codi_sai (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo da nota)
- `numero_lancamento`: Filtra nume_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Numero do lancamento)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `contabilizacao_nota_servico_consultar`

Contabilização das notas de serviço — tabela efservicos_lancto (módulo contabil, ~1.381.415 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: Notas de servicos X Lancamentos contabeis
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): codigo_nota, numero_lancamento.
FILTROS: codigo_nota, numero_lancamento. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo_nota, numero_lancamento, empresa_lancamento. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): lancamento_data, lancamento_valor, lancamento_conta_debito, lancamento_conta_credito.
EXEMPLO COM DADOS: a empresa 750 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): O maior lancamento_valor ligado a uma nota de serviço é igual a vcon_ser em 99,9% (empresa 138) e 98,8% (empresa 603). A soma NÃO fecha (0% na empresa 138, 64% na 603): serviços costumam gerar vários lançamentos (receita, retenções).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo_nota`: Filtra codi_ser (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo da nota)
- `numero_lancamento`: Filtra nume_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Numero do lancamento)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.
