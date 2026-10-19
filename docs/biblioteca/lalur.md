# Módulo `lalur`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `calculo_lalur_consultar` | consultar | lrcalculo | empresa | ✔ |
| `calculo_lalur_obter` | obter | lrcalculo | empresa, calculo | ✔ |
| `apuracao_csll_real_consultar` | consultar | lrcalculo_csll_real | empresa | ✔ |
| `apuracao_csll_real_obter` | obter | lrcalculo_csll_real | empresa, calculo, ajuste_anual | ✔ |
| `apuracao_csll_real_totais` | totais | lrcalculo_csll_real | empresa | ✔ |
| `apuracao_irpj_real_consultar` | consultar | lrcalculo_irpj_real | empresa | ✔ |
| `apuracao_irpj_real_obter` | obter | lrcalculo_irpj_real | empresa, calculo, ajuste_anual | ✔ |
| `apuracao_irpj_real_totais` | totais | lrcalculo_irpj_real | empresa | ✔ |
| `lucro_antes_irpj_csll_consultar` | consultar | lrlucro_antes_csll_irpj | empresa | ✔ |
| `lucro_antes_irpj_csll_totais` | totais | lrlucro_antes_csll_irpj | empresa | ✔ |

## `calculo_lalur_consultar`

Cálculos do Lalur (cabeçalho) — tabela lrcalculo (módulo lalur, ~2.884 linhas).
O QUE É: Cada vez que o Lalur é calculado para uma empresa e competência fica um registro com o usuário e a hora. 2.884 cálculos, 76 empresas, de 2015-01 a 2026-09, feitos por 22 usuários. As apurações de IRPJ e CSLL ficam em apuracao_irpj_real e apuracao_csll_real, ligadas por (empresa, cálculo).
COMENTÁRIO DO BANCO SOBRE A TABELA: Cálculo do Lalur
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna COMPETENCIA. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: calculo, competencia. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: calculo, competencia, usuario, calculado_em, scp_codigo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): empresa_nome.
EXEMPLO COM DADOS: a empresa 1366 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Cada cálculo de IRPJ real tem o cabeçalho (0 sem cabeçalho em 3.108) e cada um tem também o cálculo de CSLL (3.108 de 3.108). As competências cobrem todos os meses (~240 por mês); dezembro tem 464 por incluir as 224 linhas de ajuste anual.
POSSÍVEIS DADOS PESSOAIS/FINANCEIROS (os dados saem em claro; devolva só o que a pergunta exigir): usuario.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `calculo`: Filtra I_CALCULO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código)
- `competencia`: Filtra COMPETENCIA (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competência) Datas no formato AAAA-MM-DD.
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `calculo_lalur_obter`

Cálculos do Lalur (cabeçalho) — obtém UM registro pela chave (CODI_EMP, I_CALCULO) da tabela lrcalculo. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use calculo_lalur_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP).
- `calculo` (obrigatório): Filtra I_CALCULO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código)

## `apuracao_csll_real_consultar`

Apuração da CSLL pelo lucro real — tabela lrcalculo_csll_real (módulo lalur, ~3.108 linhas).
O QUE É: Cadeia da CSLL de um cálculo do Lalur: lucro antes, adições, exclusões, base de cálculo antes e depois da compensação da base negativa, CSLL devida (9%), deduções e valor a recolher; geral e rural. 3.108 linhas, 76 empresas. Usa 26 das 60 colunas.
COMENTÁRIO DO BANCO SOBRE A TABELA: Cálculo do Lalur - Imposto CSLL Real
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): calculo.
FILTROS: calculo, ajuste_anual, a_recolher. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: calculo, ajuste_anual, lucro_liquido_antes_csll_irpj, adicoes, exclusoes, base_calculo_antes_compensacao, compensacao_base_negativa, base_calculo, base_calculo_geral, base_calculo_rural, csll_devida, deducoes, deducao_orgao_publico_federal, deducao_pago_em_meses_anteriores, deducao_outras_pessoas_juridicas, deducao_estado_municipio, deducao_administracao_publica, deducao_outras, isencao_prouni, isencao_perse_pgsc, bonus_adimplencia, diferido_periodo_anterior, diferido_periodo, a_recolher, compensar_periodo_seguinte, deduzir_periodo_seguinte, base_recalculada. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): competencia, calculado_em.
EXEMPLO COM DADOS: a empresa 1366 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Base antes da compensação = lucro antes + adições − exclusões e base = antes − compensação, ambas em 3.108 de 3.108 linhas (tolerância 0,02). | CSLL devida = 9% da base positiva em 277 das 278 linhas com base positiva (a outra é 9,03%, arredondamento); nas 2.830 linhas com base zero ou negativa a CSLL devida é 0 em todas. | Deduções (total) = soma das 6 parcelas em 3.103 de 3.108 linhas; as 5 restantes não fecham nem somando o Perse/PGSC (causa não apurada). | Valor a recolher = max(0, CSLL devida − deduções − isenção Prouni − bônus de adimplência + diferido do período anterior − diferido do período) em 278 de 278 linhas com CSLL devida.
PRIVACIDADE: Resultado tributário da empresa (financeiro).
POSSÍVEIS DADOS PESSOAIS/FINANCEIROS (os dados saem em claro; devolva só o que a pergunta exigir): lucro_liquido_antes_csll_irpj.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `calculo`: Filtra I_CALCULO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do cálculo)
- `ajuste_anual`: Filtra AJUSTE_ANUAL (integer). Aceita: valor simples (igualdade), igual. Códigos: 0=Cálculo do período, 1=Ajuste anual [parcialmente confirmado] (Ajuste Anual)
- `a_recolher`: Filtra VALOR_A_RECOLHER (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (CSLL a recolher)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `apuracao_csll_real_obter`

Apuração da CSLL pelo lucro real — obtém UM registro pela chave (CODI_EMP, I_CALCULO, AJUSTE_ANUAL) da tabela lrcalculo_csll_real. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use apuracao_csll_real_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP).
- `calculo` (obrigatório): Filtra I_CALCULO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do cálculo)
- `ajuste_anual` (obrigatório): Filtra AJUSTE_ANUAL (integer). Aceita: valor simples (igualdade), igual. Códigos: 0=Cálculo do período, 1=Ajuste anual [parcialmente confirmado] (Ajuste Anual)

## `apuracao_csll_real_totais`

Apuração da CSLL pelo lucro real — TOTAIS por grupo da tabela lrcalculo_csll_real (módulo lalur). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): calculo. CAMPOS SOMÁVEIS: lucro_liquido_antes_csll_irpj, base_calculo_antes_compensacao, compensacao_base_negativa, base_calculo, base_calculo_geral, base_calculo_rural, deducao_orgao_publico_federal, deducao_pago_em_meses_anteriores, deducao_outras_pessoas_juridicas, deducao_estado_municipio, deducao_administracao_publica, deducao_outras. CAMPOS PARA AGRUPAR: calculo, ajuste_anual, adicoes, exclusoes, csll_devida, deducoes, isencao_prouni, isencao_perse_pgsc, bonus_adimplencia, diferido_periodo_anterior, diferido_periodo, a_recolher, compensar_periodo_seguinte, deduzir_periodo_seguinte. Os filtros são os mesmos de apuracao_csll_real_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (ajuste_anual) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Base antes da compensação = lucro antes + adições − exclusões e base = antes − compensação, ambas em 3.108 de 3.108 linhas (tolerância 0,02). | CSLL devida = 9% da base positiva em 277 das 278 linhas com base positiva (a outra é 9,03%, arredondamento); nas 2.830 linhas com base zero ou negativa a CSLL devida é 0 em todas. | Deduções (total) = soma das 6 parcelas em 3.103 de 3.108 linhas; as 5 restantes não fecham nem somando o Perse/PGSC (causa não apurada). | Valor a recolher = max(0, CSLL devida − deduções − isenção Prouni − bônus de adimplência + diferido do período anterior − diferido do período) em 278 de 278 linhas com CSLL devida.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `calculo`: Filtra I_CALCULO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do cálculo)
- `ajuste_anual`: Filtra AJUSTE_ANUAL (integer). Aceita: valor simples (igualdade), igual. Códigos: 0=Cálculo do período, 1=Ajuste anual [parcialmente confirmado] (Ajuste Anual)
- `a_recolher`: Filtra VALOR_A_RECOLHER (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (CSLL a recolher)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["ajuste_anual"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["lucro_liquido_antes_csll_irpj"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `apuracao_irpj_real_consultar`

Apuração do IRPJ pelo lucro real — tabela lrcalculo_irpj_real (módulo lalur, ~3.108 linhas).
O QUE É: Cadeia completa do IRPJ de um cálculo do Lalur: lucro líquido antes do IRPJ, adições, exclusões, lucro real antes e depois da compensação de prejuízos, IRPJ devido (15%), adicional (10%), deduções, incentivos, diferimento e valor a recolher; há os mesmos blocos para a atividade geral e a rural. 3.108 linhas, 76 empresas. Usa 38 das 62 colunas.
COMENTÁRIO DO BANCO SOBRE A TABELA: Cálculo do Lalur - Imposto IRPJ Real
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): calculo.
FILTROS: calculo, ajuste_anual, lucro_real, a_recolher. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: calculo, ajuste_anual, lucro_liquido_antes_irpj, adicoes, exclusoes, lucro_real_antes_compensacao, compensacao_prejuizo, lucro_real, prejuizo_periodo, lucro_liquido_antes_irpj_geral, adicoes_geral, exclusoes_geral, lucro_real_geral, lucro_liquido_antes_irpj_rural, adicoes_rural, exclusoes_rural, lucro_real_rural, irpj_devido, adicional, deducoes, deducao_pago_em_meses_anteriores, deducao_irrf, deducao_irrf_orgao_publico_federal, deducao_irrf_administracao_publica, deducao_outras, deducao_pago_exterior, deducao_ganhos_renda_variavel, deducao_parcelamento_formalizado, deducao_compensacao_federal_periodo_anterior, deducao_saldo_periodo_anterior, incentivo_fiscal, reducao_lucro_exploracao, reducao_por_reinvestimento, diferido_periodo_anterior, diferido_periodo, a_recolher, compensar_periodo_seguinte, deduzir_periodo_seguinte, lucro_real_recalculado. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): competencia, calculado_em.
EXEMPLO COM DADOS: a empresa 1366 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Lucro real antes da compensação = lucro líquido antes do IRPJ + adições − exclusões em 3.108 de 3.108 linhas; lucro real = antes da compensação − compensação em 3.108 de 3.108 (tolerância 0,02). | IRPJ devido = 15% do lucro real em 278 de 278 linhas com lucro real positivo; nas 2.830 linhas com lucro real zero ou negativo o IRPJ devido é 0 em todas. | Adicional = 10% × (lucro real − 20.000 × m), com m inteiro entre 1 e 12 em 167 de 167 linhas com adicional (m = nº de meses do período; mais comuns 3 e 12). Não use um limite fixo. | Deduções (total) = soma das 10 parcelas em 3.108 de 3.108. | Valor a recolher = max(0, IRPJ devido + adicional − deduções − incentivos fiscais − redução do lucro da exploração − redução por reinvestimento + diferido do período anterior − diferido do período) em 278 de 278 linhas com imposto devido; em 96 delas as deduções cobrem o imposto e o valor a recolher é 0. Nas 2.830 linhas sem imposto devido, […] (+1 regras: veja descrever_entidade)
PRIVACIDADE: Resultado tributário da empresa (financeiro).
POSSÍVEIS DADOS PESSOAIS/FINANCEIROS (os dados saem em claro; devolva só o que a pergunta exigir): lucro_liquido_antes_irpj, lucro_liquido_antes_irpj_geral, lucro_liquido_antes_irpj_rural.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `calculo`: Filtra I_CALCULO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do cálculo)
- `ajuste_anual`: Filtra AJUSTE_ANUAL (integer). Aceita: valor simples (igualdade), igual. Códigos: 0=Cálculo do período, 1=Ajuste anual [parcialmente confirmado] (Ajuste Anual)
- `lucro_real`: Filtra VALOR_LUCRO_REAL (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Lucro Real da atividade)
- `a_recolher`: Filtra VALOR_A_RECOLHER (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (IRPJ a recolher)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `apuracao_irpj_real_obter`

Apuração do IRPJ pelo lucro real — obtém UM registro pela chave (CODI_EMP, I_CALCULO, AJUSTE_ANUAL) da tabela lrcalculo_irpj_real. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use apuracao_irpj_real_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP).
- `calculo` (obrigatório): Filtra I_CALCULO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do cálculo)
- `ajuste_anual` (obrigatório): Filtra AJUSTE_ANUAL (integer). Aceita: valor simples (igualdade), igual. Códigos: 0=Cálculo do período, 1=Ajuste anual [parcialmente confirmado] (Ajuste Anual)

## `apuracao_irpj_real_totais`

Apuração do IRPJ pelo lucro real — TOTAIS por grupo da tabela lrcalculo_irpj_real (módulo lalur). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): calculo. CAMPOS SOMÁVEIS: lucro_liquido_antes_irpj, lucro_real_antes_compensacao, compensacao_prejuizo, lucro_real, prejuizo_periodo, lucro_liquido_antes_irpj_geral, lucro_real_geral, lucro_liquido_antes_irpj_rural, lucro_real_rural, irpj_devido, deducao_pago_em_meses_anteriores, deducao_irrf, deducao_irrf_orgao_publico_federal, deducao_irrf_administracao_publica, deducao_outras, deducao_pago_exterior, deducao_ganhos_renda_variavel, deducao_parcelamento_formalizado, deducao_compensacao_federal_periodo_anterior, deducao_saldo_periodo_anterior. CAMPOS PARA AGRUPAR: calculo, ajuste_anual, adicoes, exclusoes, adicoes_geral, exclusoes_geral, adicoes_rural, exclusoes_rural, adicional, deducoes, incentivo_fiscal, reducao_lucro_exploracao, reducao_por_reinvestimento, diferido_periodo_anterior, diferido_periodo, a_recolher, compensar_periodo_seguinte, deduzir_periodo_seguinte. Os filtros são os mesmos de apuracao_irpj_real_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (ajuste_anual) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Lucro real antes da compensação = lucro líquido antes do IRPJ + adições − exclusões em 3.108 de 3.108 linhas; lucro real = antes da compensação − compensação em 3.108 de 3.108 (tolerância 0,02). | IRPJ devido = 15% do lucro real em 278 de 278 linhas com lucro real positivo; nas 2.830 linhas com lucro real zero ou negativo o IRPJ devido é 0 em todas. | Adicional = 10% × (lucro real − 20.000 × m), com m inteiro entre 1 e 12 em 167 de 167 linhas com adicional (m = nº de meses do período; mais comuns 3 e 12). Não use um limite fixo. | Deduções (total) = soma das 10 parcelas em 3.108 de 3.108.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `calculo`: Filtra I_CALCULO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do cálculo)
- `ajuste_anual`: Filtra AJUSTE_ANUAL (integer). Aceita: valor simples (igualdade), igual. Códigos: 0=Cálculo do período, 1=Ajuste anual [parcialmente confirmado] (Ajuste Anual)
- `lucro_real`: Filtra VALOR_LUCRO_REAL (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Lucro Real da atividade)
- `a_recolher`: Filtra VALOR_A_RECOLHER (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (IRPJ a recolher)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["ajuste_anual"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["lucro_liquido_antes_irpj"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `lucro_antes_irpj_csll_consultar`

Lucro antes da CSLL e do IRPJ (apurado na contabilidade) — tabela lrlucro_antes_csll_irpj (módulo lalur, ~2.813 linhas).
O QUE É: Lucro ou prejuízo contábil, operacional e não operacional, geral e rural, que alimenta o cálculo do Lalur numa competência. 2.813 linhas, 78 empresas, de 2013-01 a 2026-10.
COMENTÁRIO DO BANCO SOBRE A TABELA: Lucro Antes da CSLL e IRPJ
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna COMPETENCIA. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: competencia. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: lucro_antes, competencia, lucro_operacional, prejuizo_operacional, lucro_nao_operacional, prejuizo_nao_operacional, lucro_operacional_geral, prejuizo_operacional_geral, lucro_nao_operacional_geral, prejuizo_nao_operacional_geral, lucro_operacional_rural, prejuizo_operacional_rural, scp_codigo, historico_geral, historico_rural. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 1446 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Nunca há lucro e prejuízo operacionais ao mesmo tempo na mesma linha (0 de 2.813); nenhuma linha é de SCP.
PRIVACIDADE: Resultado contábil da empresa (financeiro).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `competencia`: Filtra COMPETENCIA (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competência) Datas no formato AAAA-MM-DD.
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `lucro_antes_irpj_csll_totais`

Lucro antes da CSLL e do IRPJ (apurado na contabilidade) — TOTAIS por grupo da tabela lrlucro_antes_csll_irpj (módulo lalur). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna COMPETENCIA. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: lucro_operacional, prejuizo_operacional, lucro_nao_operacional, prejuizo_nao_operacional, lucro_operacional_geral, prejuizo_operacional_geral, lucro_nao_operacional_geral, prejuizo_nao_operacional_geral, lucro_operacional_rural, prejuizo_operacional_rural. CAMPOS PARA AGRUPAR: lucro_antes, competencia:mes, scp_codigo, historico_geral, historico_rural. Os filtros são os mesmos de lucro_antes_irpj_csll_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Nunca há lucro e prejuízo operacionais ao mesmo tempo na mesma linha (0 de 2.813); nenhuma linha é de SCP.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `competencia`: Filtra COMPETENCIA (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competência) Datas no formato AAAA-MM-DD.
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["competencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["lucro_operacional"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).
