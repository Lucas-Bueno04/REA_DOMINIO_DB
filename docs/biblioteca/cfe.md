# Módulo `cfe`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `cupom_fiscal_eletronico_consultar` | consultar | efcupom_fiscal_eletronico | empresa | ✔ |
| `cupom_fiscal_eletronico_obter` | obter | efcupom_fiscal_eletronico | empresa, codigo | ✔ |
| `cupom_fiscal_eletronico_totais` | totais | efcupom_fiscal_eletronico | empresa | ✔ |
| `item_cupom_fiscal_eletronico_consultar` | consultar | efcupom_fiscal_eletronico_estoque | empresa | ✔ |
| `item_cupom_fiscal_eletronico_totais` | totais | efcupom_fiscal_eletronico_estoque | empresa | ✔ |
| `imposto_cupom_fiscal_eletronico_consultar` | consultar | efcupom_fiscal_eletronico_impostos | empresa | ✔ |
| `imposto_cupom_fiscal_eletronico_totais` | totais | efcupom_fiscal_eletronico_impostos | empresa | ✔ |
| `detalhe_imposto_cupom_fiscal_eletronico_consultar` | consultar | efcupom_fiscal_eletronico_impostos_detalhamento | empresa | ✔ |
| `detalhe_imposto_cupom_fiscal_eletronico_totais` | totais | efcupom_fiscal_eletronico_impostos_detalhamento | empresa | ✔ |
| `lancamento_cupom_fiscal_eletronico_consultar` | consultar | efcupom_fiscal_eletronico_lancto | empresa | ✔ |
| `pis_cofins_cupom_fiscal_eletronico_consultar` | consultar | efcupom_fiscal_eletronico_pis_cofins | empresa | ✔ |
| `pis_cofins_cupom_fiscal_eletronico_totais` | totais | efcupom_fiscal_eletronico_pis_cofins | empresa | ✔ |

## `cupom_fiscal_eletronico_consultar`

Cupons fiscais eletrônicos (CF-e SAT) — tabela efcupom_fiscal_eletronico (módulo cfe, ~7.235.124 linhas).
O QUE É: Cabeçalho de cada CF-e lançado na escrita fiscal: chave, data, extrato, equipamento SAT, situação e valor total. Cobre 40 empresas, de 2017-07 a 2026-01. Cancelamentos vêm como outro registro com extrato e chave de cancelamento preenchidos.
COMENTÁRIO DO BANCO SOBRE A TABELA: Cupom Fiscal Eletrônico - CF-e
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): periodo, codigo, chave_cfe, extrato.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna data_cfe. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: codigo, chave_cfe, data, extrato, sat, cliente_codigo, situacao, valor_total. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, chave_cfe, data, extrato, sat, cliente_codigo, tipo_titulo, identificacao, situacao, valor_total, origem_registro, extrato_cancelamento, chave_cancelamento, usuario, conferido. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): cliente_nome, cliente_cnpj_cpf, total_produtos, total_desconto, total_acrescimo.
EXEMPLO COM DADOS: a empresa 571 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Cancelamento: situação 2 tem extrato e chave de cancelamento em 12.083 de 12.090 CF-e, com valor total 0 e sem cliente; situação 0 nunca tem extrato de cancelamento (7.223.034 de 7.223.034). Para o que vale na apuração, filtre `situacao = 0`. | Chave: os 7.235.124 CF-e têm chave de 44 posições e não há chave repetida por empresa (empresa 1017: 0 repetidas em 554.404). | Fechamento (empresa 1017, 554.404 CF-e): valor_total do cabeçalho = valor_total do estoque_total em 100%; estoque_total = soma dos itens em 552.621 de 552.621; soma de impostos.valor_total = valor_total do cabeçalho em 552.621 de 552.621. Os 1.783 restantes são cancelados (valor 0, sem itens). | origem_registro vale 7 em 99,99% dos CF-e e esse código não é documentado no comentário do banco; tipo_titulo é sempre 99 e conferido é sempre N: não servem para filtrar.
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): identificacao
POSSÍVEIS DADOS PESSOAIS/FINANCEIROS (os dados saem em claro; devolva só o que a pergunta exigir): usuario, cliente_cnpj_cpf.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo`: Filtra i_cfe (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do CF-e)
- `chave_cfe`: Filtra chave_cfe (varchar). Aceita: valor simples (igualdade), igual. (Chave CF-e)
- `data`: Filtra data_cfe (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data do CF-e) Datas no formato AAAA-MM-DD.
- `extrato`: Filtra extrato (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Extrato)
- `sat`: Filtra sat (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do SAT CF-e)
- `cliente_codigo`: Filtra codi_cli (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do cliente)
- `situacao`: Filtra situacao (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 0=Normal, 1=Desconhecido (não ocorre), 2=Cancelado, 4=Desconhecido (não ocorre) [parcialmente confirmado] (Situação (0/1/2/4))
- `valor_total`: Filtra valor_total_cfe (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Valor Total do CF-e)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `cupom_fiscal_eletronico_obter`

Cupons fiscais eletrônicos (CF-e SAT) — obtém UM registro pela chave (codi_emp, i_cfe) da tabela efcupom_fiscal_eletronico. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use cupom_fiscal_eletronico_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra i_cfe (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do CF-e)

## `cupom_fiscal_eletronico_totais`

Cupons fiscais eletrônicos (CF-e SAT) — TOTAIS por grupo da tabela efcupom_fiscal_eletronico (módulo cfe). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): periodo, codigo, chave_cfe, extrato. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna data_cfe. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor_total. CAMPOS PARA AGRUPAR: codigo, chave_cfe, data:mes, extrato, sat, cliente_codigo, tipo_titulo, identificacao, situacao, origem_registro, extrato_cancelamento, chave_cancelamento, usuario, conferido. Os filtros são os mesmos de cupom_fiscal_eletronico_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (tipo_titulo, situacao, origem_registro, conferido) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Cancelamento: situação 2 tem extrato e chave de cancelamento em 12.083 de 12.090 CF-e, com valor total 0 e sem cliente; situação 0 nunca tem extrato de cancelamento (7.223.034 de 7.223.034). Para o que vale na apuração, filtre `situacao = 0`. | Chave: os 7.235.124 CF-e têm chave de 44 posições e não há chave repetida por empresa (empresa 1017: 0 repetidas em 554.404). | Fechamento (empresa 1017, 554.404 CF-e): valor_total do cabeçalho = valor_total do estoque_total em 100%; estoque_total = soma dos itens em 552.621 de 552.621; soma de impostos.valor_total = valor_total do cabeçalho em 552.621 de 552.621. Os 1.783 restantes são cancelados (valor 0, sem itens). | origem_registro vale 7 em 99,99% dos CF-e e esse código não é documentado no comentário do banco; tipo_titulo é sempre 99 e conferido é sempre N: não servem para filtrar.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo`: Filtra i_cfe (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do CF-e)
- `chave_cfe`: Filtra chave_cfe (varchar). Aceita: valor simples (igualdade), igual. (Chave CF-e)
- `data`: Filtra data_cfe (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data do CF-e) Datas no formato AAAA-MM-DD.
- `extrato`: Filtra extrato (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Extrato)
- `sat`: Filtra sat (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do SAT CF-e)
- `cliente_codigo`: Filtra codi_cli (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do cliente)
- `situacao`: Filtra situacao (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 0=Normal, 1=Desconhecido (não ocorre), 2=Cancelado, 4=Desconhecido (não ocorre) [parcialmente confirmado] (Situação (0/1/2/4))
- `valor_total`: Filtra valor_total_cfe (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Valor Total do CF-e)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["data:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor_total"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `item_cupom_fiscal_eletronico_consultar`

Itens dos CF-e (estoque) — tabela efcupom_fiscal_eletronico_estoque (módulo cfe, ~12.416.469 linhas).
O QUE É: Um item vendido por linha, com quantidade, valores e tributação de ICMS, PIS e COFINS. Colunas de combustível (bico, tanque, operação, modal), FECOEP/FECOP e quantidade tributável por unidade de medida só estão em usos específicos e foram omitidas.
COMENTÁRIO DO BANCO SOBRE A TABELA: Cupom Fiscal Eletrônico - CF-e - Estoque
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): codigo_cfe, periodo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna cupom.data_cfe. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: codigo_cfe, produto_codigo, cfop, cst_icms, cst_pis, cst_cofins, acumulador_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo_cfe, sequencial, produto_codigo, unidade, quantidade, valor_unitario, valor_produto, desconto, acrescimo, valor_total, cfop, cfop_versao, acumulador_codigo, cst_icms, base_icms, aliquota_icms, valor_icms, cst_pis, natureza_receita_pis, base_pis, aliquota_pis, valor_pis, cst_cofins, natureza_receita_cofins, base_cofins, aliquota_cofins, valor_cofins, dados_pis_cofins_ok, codigo_cest. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): cupom_data, cupom_chave, cupom_situacao, produto_descricao, produto_ncm, acumulador_nome.
EXEMPLO COM DADOS: a empresa 596 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Sem órfãos: os 702.017 itens da empresa 1017 têm o CF-e correspondente (0 sem cabeçalho); a soma de valor_total dos itens por CF-e é igual ao estoque_total em 552.621 de 552.621. | Na empresa 1017 o ICMS é quase sempre CST 60 (701.433 de 702.017) e os dados de PIS/COFINS estão todos conferidos (dados_pis_cofins_ok = S).
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_cfe`: Filtra i_cfe (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do CF-e)
- `produto_codigo`: Filtra codi_pdi (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Produto)
- `cfop`: Filtra codi_nat (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CFOP)
- `cst_icms`: Filtra cst_icms (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo da Situação Tributaria(ICMS))
- `cst_pis`: Filtra cst_pis (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CST do PIS)
- `cst_cofins`: Filtra cst_cofins (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CST da COFINS)
- `acumulador_codigo`: Filtra codi_acu (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do acumulador)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `item_cupom_fiscal_eletronico_totais`

Itens dos CF-e (estoque) — TOTAIS por grupo da tabela efcupom_fiscal_eletronico_estoque (módulo cfe). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): codigo_cfe, periodo. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna cupom.data_cfe. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: quantidade, valor_unitario, valor_produto, desconto, acrescimo, valor_total, base_icms, valor_icms, natureza_receita_pis, base_pis, valor_pis, natureza_receita_cofins, base_cofins, valor_cofins. CAMPOS PARA AGRUPAR: codigo_cfe, sequencial, produto_codigo, unidade, cfop, cfop_versao, acumulador_codigo, cst_icms, aliquota_icms, cst_pis, aliquota_pis, cst_cofins, aliquota_cofins, dados_pis_cofins_ok, codigo_cest. Os filtros são os mesmos de item_cupom_fiscal_eletronico_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (dados_pis_cofins_ok) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Sem órfãos: os 702.017 itens da empresa 1017 têm o CF-e correspondente (0 sem cabeçalho); a soma de valor_total dos itens por CF-e é igual ao estoque_total em 552.621 de 552.621. | Na empresa 1017 o ICMS é quase sempre CST 60 (701.433 de 702.017) e os dados de PIS/COFINS estão todos conferidos (dados_pis_cofins_ok = S).. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_cfe`: Filtra i_cfe (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do CF-e)
- `produto_codigo`: Filtra codi_pdi (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Produto)
- `cfop`: Filtra codi_nat (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CFOP)
- `cst_icms`: Filtra cst_icms (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo da Situação Tributaria(ICMS))
- `cst_pis`: Filtra cst_pis (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CST do PIS)
- `cst_cofins`: Filtra cst_cofins (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CST da COFINS)
- `acumulador_codigo`: Filtra codi_acu (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do acumulador)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["dados_pis_cofins_ok"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["quantidade"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `imposto_cupom_fiscal_eletronico_consultar`

Impostos dos CF-e por acumulador — tabela efcupom_fiscal_eletronico_impostos (módulo cfe, ~7.623.014 linhas).
O QUE É: Resumo por acumulador de cada CF-e (valor do produto, desconto, acréscimo e total). Alimenta a apuração: a soma do valor_total por CF-e é igual ao valor do cabeçalho.
COMENTÁRIO DO BANCO SOBRE A TABELA: Cupom Fiscal Eletrônico - CF-e - Impostos
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): codigo_cfe, periodo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna cupom.data_cfe. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: codigo_cfe, acumulador_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo_cfe, sequencial, acumulador_codigo, valor_produto, desconto, acrescimo, valor_total. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): cupom_data, cupom_chave, cupom_situacao, acumulador_nome.
EXEMPLO COM DADOS: a empresa 679 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Soma de valor_total por CF-e = valor_total do cabeçalho em 552.621 de 552.621 CF-e vigentes da empresa 1017.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_cfe`: Filtra i_cfe (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do CF-e)
- `acumulador_codigo`: Filtra codi_acu (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do acumulador)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `imposto_cupom_fiscal_eletronico_totais`

Impostos dos CF-e por acumulador — TOTAIS por grupo da tabela efcupom_fiscal_eletronico_impostos (módulo cfe). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): codigo_cfe, periodo. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna cupom.data_cfe. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor_produto, desconto, acrescimo, valor_total. CAMPOS PARA AGRUPAR: codigo_cfe, sequencial, acumulador_codigo. Os filtros são os mesmos de imposto_cupom_fiscal_eletronico_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Soma de valor_total por CF-e = valor_total do cabeçalho em 552.621 de 552.621 CF-e vigentes da empresa 1017.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_cfe`: Filtra i_cfe (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do CF-e)
- `acumulador_codigo`: Filtra codi_acu (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do acumulador)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["codigo_cfe"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor_produto"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `detalhe_imposto_cupom_fiscal_eletronico_consultar`

Detalhamento dos impostos do CF-e — tabela efcupom_fiscal_eletronico_impostos_detalhamento (módulo cfe, ~7.744.304 linhas).
O QUE É: Base, alíquota e valor por imposto (ICMS etc.), CST e CFOP de cada linha de imposto do CF-e.
COMENTÁRIO DO BANCO SOBRE A TABELA: Cupom Fiscal Eletrônico - CF-e - Impostos - Detalhamento
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): codigo_cfe, periodo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna cupom.data_cfe. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: codigo_cfe, imposto_codigo, cst, cfop. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo_cfe, imposto_sequencial, sequencial, imposto_codigo, valor_contabil, base_calculo, aliquota, valor_imposto, valor_isentas, valor_outros, cst, cfop, cfop_versao, observacao_codigo, observacao. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): cupom_data, cupom_situacao, imposto_nome, imposto_sigla.
EXEMPLO COM DADOS: a empresa 894 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Na empresa 1017 todo o detalhamento é de ICMS (codi_imp = 1; 554.530 linhas).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_cfe`: Filtra i_cfe (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do CF-e)
- `imposto_codigo`: Filtra codi_imp (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=ICMS, 2=IPI, 3=ISS, 4=PIS, 5=COFINS, 8=DIFALI, 9=Substituição Tributária, 16=IRRF, 18=ISS Retido, 22=PIS (Retido), … (+3) (Código do imposto)
- `cst`: Filtra cst (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CST)
- `cfop`: Filtra codi_nat (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CFOP)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `detalhe_imposto_cupom_fiscal_eletronico_totais`

Detalhamento dos impostos do CF-e — TOTAIS por grupo da tabela efcupom_fiscal_eletronico_impostos_detalhamento (módulo cfe). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): codigo_cfe, periodo. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna cupom.data_cfe. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor_contabil, base_calculo, valor_imposto, valor_isentas, valor_outros. CAMPOS PARA AGRUPAR: codigo_cfe, imposto_sequencial, sequencial, imposto_codigo, aliquota, cst, cfop, cfop_versao, observacao_codigo, observacao. Os filtros são os mesmos de detalhe_imposto_cupom_fiscal_eletronico_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (imposto_codigo) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Na empresa 1017 todo o detalhamento é de ICMS (codi_imp = 1; 554.530 linhas).. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_cfe`: Filtra i_cfe (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do CF-e)
- `imposto_codigo`: Filtra codi_imp (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=ICMS, 2=IPI, 3=ISS, 4=PIS, 5=COFINS, 8=DIFALI, 9=Substituição Tributária, 16=IRRF, 18=ISS Retido, 22=PIS (Retido), … (+3) (Código do imposto)
- `cst`: Filtra cst (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CST)
- `cfop`: Filtra codi_nat (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CFOP)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["imposto_codigo"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor_contabil"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `lancamento_cupom_fiscal_eletronico_consultar`

Lançamentos contábeis dos CF-e — tabela efcupom_fiscal_eletronico_lancto (módulo cfe, ~7.399.590 linhas).
O QUE É: Liga cada CF-e ao lançamento contábil gerado (ctlancto). `empresa_cfe` é a empresa dona do CF-e; `codi_emp` é a empresa do lançamento.
COMENTÁRIO DO BANCO SOBRE A TABELA: Cupom Fiscal Eletrônico - CF-e - Lançamentos Contábeis
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): codigo_cfe, periodo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna cupom.data_cfe. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: codigo_cfe, lancamento_numero. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo_cfe, lancamento_numero, empresa_cfe, tipo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): cupom_data, cupom_situacao.
EXEMPLO COM DADOS: a empresa 364 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Na empresa 1017 os 554.516 lançamentos têm fili_lan igual a codi_emp e tipo 1.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_cfe`: Filtra i_cfe (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do CF-e)
- `lancamento_numero`: Filtra nume_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Número do lançamento)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `pis_cofins_cupom_fiscal_eletronico_consultar`

PIS/COFINS dos CF-e (resumo por CST) — tabela efcupom_fiscal_eletronico_pis_cofins (módulo cfe, ~1.363.671 linhas).
O QUE É: Resumo de PIS e COFINS por CST/natureza da receita/CFOP, usado pela apuração (a apuração lê esta tabela e a de itens). Cobre 1,36 milhão de linhas, bem menos que os itens (nem todo CF-e tem resumo).
COMENTÁRIO DO BANCO SOBRE A TABELA: Cupom Fiscal Eletrônico - CF-e - PIS/COFINS
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): codigo_cfe, periodo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna cupom.data_cfe. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: codigo_cfe, cst, cfop. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo_cfe, sequencial, cst, natureza_receita, cfop, cfop_versao, valor_contabil, exclusoes, base_calculo, aliquota_pis, aliquota_cofins, quantidade_tributada, valor_pis, valor_cofins, exclusao_cooperativa, percentual_reducao_bc, codigo_recolhimento_pis, codigo_recolhimento_cofins. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): cupom_data, cupom_situacao.
EXEMPLO COM DADOS: a empresa 1018 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Na empresa 1017, 148.571 linhas: CST 4 em 147.105 e CST 1 em 1.466.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_cfe`: Filtra i_cfe (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do CF-e)
- `cst`: Filtra cst (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CST)
- `cfop`: Filtra codi_nat (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CFOP)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `pis_cofins_cupom_fiscal_eletronico_totais`

PIS/COFINS dos CF-e (resumo por CST) — TOTAIS por grupo da tabela efcupom_fiscal_eletronico_pis_cofins (módulo cfe). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): codigo_cfe, periodo. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna cupom.data_cfe. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: natureza_receita, valor_contabil, base_calculo, quantidade_tributada, valor_pis, valor_cofins. CAMPOS PARA AGRUPAR: codigo_cfe, sequencial, cst, cfop, cfop_versao, exclusoes, aliquota_pis, aliquota_cofins, exclusao_cooperativa, percentual_reducao_bc, codigo_recolhimento_pis, codigo_recolhimento_cofins. Os filtros são os mesmos de pis_cofins_cupom_fiscal_eletronico_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Na empresa 1017, 148.571 linhas: CST 4 em 147.105 e CST 1 em 1.466.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_cfe`: Filtra i_cfe (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do CF-e)
- `cst`: Filtra cst (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CST)
- `cfop`: Filtra codi_nat (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CFOP)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["codigo_cfe"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["natureza_receita"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).
