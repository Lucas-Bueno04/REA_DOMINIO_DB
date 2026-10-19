# Módulo `guias`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `pagamento_imposto_consultar` | consultar | efpagimp | empresa | ✔ |
| `pagamento_imposto_totais` | totais | efpagimp | empresa | ✔ |
| `guia_imposto_consultar` | consultar | efsdoimp_por_recolhimento | empresa | ✔ |
| `guia_imposto_totais` | totais | efsdoimp_por_recolhimento | empresa | ✔ |
| `codigo_receita_imposto_consultar` | consultar | geimposto_vigencia_codrec | empresa | ✔ |
| `codigo_receita_imposto_obter` | obter | geimposto_vigencia_codrec | empresa, imposto_codigo, vigencia, codigo_receita | ✔ |
| `regra_recolhimento_consultar` | consultar | geimposto_vigencia_recolhimento | empresa | ✔ |
| `regra_recolhimento_totais` | totais | geimposto_vigencia_recolhimento | empresa | ✔ |

## `pagamento_imposto_consultar`

Pagamentos de impostos — tabela efpagimp (módulo guias, ~35.248 linhas).
O QUE É: Baixas de pagamento de cada imposto: data, valor, juros, multa, banco, DARE e a ligação com Honorários e parcelamentos. 35.248 linhas, 521 empresas, de 2013-01 a 2025-04 (o registro termina em 2025-04). O órgão arrecadador, o número do DARE e a descrição complementar estão vazios em todas as linhas.
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna data_pim. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: competencia, imposto_codigo, data_pagamento, banco. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: imposto_codigo, competencia, periodicidade, parcela, baixa, data_pagamento, valor, juros, multa, valor_pago_a_maior, banco, codigo_receita_irrf, recolhimento_sequencial, pagamento_operacoes, nota_saida_codigo, escritorio_honorarios, historico_honorarios, periodo, imposto_parcelado, origem_registro, total_pago_com_encargos. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): imposto_nome, imposto_sigla.
EXEMPLO COM DADOS: a empresa 881 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Todos os 35.248 pagamentos têm valor (vpag > 0); origem 0 (sistema) em 35.244 e 5 em 4. Nenhum tem DARE, órgão arrecadador ou imposto parcelado = S. | O registro vai de 2013-01 a 2025-04: não há pagamentos mais recentes; para saber se uma guia recente foi paga consulte o banco/Honorários, não esta tabela. | Impostos com mais pagamentos: 25 (contribuição retida na fonte) 6.571 · 16 (IRRF) 5.531 · 5 (COFINS) 4.879 · 4 (PIS) 4.776 · 6 (CSLL) 3.445.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `competencia`: Filtra data_pim (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia) Datas no formato AAAA-MM-DD.
- `imposto_codigo`: Filtra codi_imp (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Imposto)
- `data_pagamento`: Filtra dpag_pim (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data do pagamento) Datas no formato AAAA-MM-DD.
- `banco`: Filtra banco_pim (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo do Banco)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `pagamento_imposto_totais`

Pagamentos de impostos — TOTAIS por grupo da tabela efpagimp (módulo guias). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna data_pim. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor, juros, multa, valor_pago_a_maior. CAMPOS PARA AGRUPAR: imposto_codigo, competencia:mes, periodicidade, parcela, baixa, data_pagamento:mes, banco, codigo_receita_irrf, recolhimento_sequencial, pagamento_operacoes, nota_saida_codigo, escritorio_honorarios, historico_honorarios, periodo:mes, imposto_parcelado, origem_registro. Os filtros são os mesmos de pagamento_imposto_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (periodicidade, imposto_parcelado, origem_registro) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Todos os 35.248 pagamentos têm valor (vpag > 0); origem 0 (sistema) em 35.244 e 5 em 4. Nenhum tem DARE, órgão arrecadador ou imposto parcelado = S. | O registro vai de 2013-01 a 2025-04: não há pagamentos mais recentes; para saber se uma guia recente foi paga consulte o banco/Honorários, não esta tabela. | Impostos com mais pagamentos: 25 (contribuição retida na fonte) 6.571 · 16 (IRRF) 5.531 · 5 (COFINS) 4.879 · 4 (PIS) 4.776 · 6 (CSLL) 3.445.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `competencia`: Filtra data_pim (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia) Datas no formato AAAA-MM-DD.
- `imposto_codigo`: Filtra codi_imp (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Imposto)
- `data_pagamento`: Filtra dpag_pim (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data do pagamento) Datas no formato AAAA-MM-DD.
- `banco`: Filtra banco_pim (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo do Banco)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["competencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `guia_imposto_consultar`

Guias de impostos (apuração por código de recolhimento) — tabela efsdoimp_por_recolhimento (módulo guias, ~407.907 linhas).
O QUE É: Desdobra a apuração de cada imposto (empresa, imposto, competência e periodicidade) em um registro por código de recolhimento: saldo a recolher, vencimento, valor já pago, créditos, débitos, estornos e deduções. É a base das guias (DARF, DAS, DAE, GPS...). 408.276 linhas, 1.312 empresas, de 2007-04 a 2026-09; só 28.910 têm saldo a recolher (as demais têm saldo credor ou zero). Usa 39 das 137 colunas.
COMENTÁRIO DO BANCO SOBRE A TABELA: Saldo dos impostos - detalhamento dos impostos por código de recolhimento
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DATA_SIM. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: competencia, imposto_codigo, periodicidade, codigo_recolhimento, vencimento, saldo_a_recolher. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: imposto_codigo, competencia, periodicidade, recolhimento_sequencial, codigo_recolhimento, parcela, vencimento, classe_vencimento, saldo_a_recolher, valor_pago, saldo_devedor, saldo_credor, saldo_credor_anterior, valor_contabil_saida, base_calculo_saida, imposto_saida, valor_contabil_entrada, base_calculo_entrada, imposto_entrada, outros_creditos, outros_debitos, estorno_creditos, estorno_debitos, outras_deducoes, outros_acrescimos, isentas_saida, outras_saida, isentas_entrada, outras_entrada, credito_presumido, estorno_credito_presumido, regime_especial, estorno_regime_especial, compensacao_pagamento_indevido, outras_compensacoes, creditos_devolucao_entradas, creditos_devolucao_saidas, valor_diferido, valor_diferido_anterior, saldo_em_aberto. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): imposto_nome, imposto_sigla.
EXEMPLO COM DADOS: a empresa 1227 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Saldo a recolher: em 17.951 linhas de 2024 em diante com saldo a recolher, 17.926 (99,9%) têm saldo_a_recolher = saldo_devedor; só 2 têm saldo devedor zero. 28.910 de 408.276 linhas têm saldo a recolher. | O REGISTRO DE PAGAMENTOS PAROU: linhas com saldo a recolher e valor pago: 2018 733 de 877 · 2019 1.125 de 1.260 · 2020 1.313 de 1.460 · 2021 1.784 de 2.122 · 2022 1.874 de 2.442 · 2023 1.525 de 2.738 · 2024 17 de 6.347 · 2025 6 de 6.742 · 2026 0 de 4.862. Não conclua que uma guia de 2024 em diante está em aberto só porque não tem valor pago. | Pagamento: nas 60 empresas com mais pagamentos em 2023-2024, valor_pago desta tabela é igual à soma de pagamento_imposto (vpag) por imposto, competência e periodicidade em 2.044 de 2.082 guias com saldo (98,2%); em 37 a soma dos pagamentos é MAIOR que o valor_pago e em nenhuma é menor (1 guia não entrou na comparação). | Vencimento: a classe de vencimento é 0 em 407.652 linhas e 10049 em 624. Todas as linhas têm data de vencimento (0 nulas). | Chave: (empresa, imposto, competência, periodicidade, sequencial do recolhimento) é a PK. Um imposto pode ter vários códigos de recolhimento na mesma competência.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `competencia`: Filtra DATA_SIM (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competência) Datas no formato AAAA-MM-DD.
- `imposto_codigo`: Filtra CODI_IMP (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Imposto)
- `periodicidade`: Filtra PDIC_SIM (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=1º decêndio, 2=2º decêndio, 3=3º decêndio, 4=1ª quinzena, 5=2ª quinzena, 6=Mensal, 7=Trimestral, 11=1ª semana, 12=2ª semana, 13=3ª semana, … (+4) (Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=COMPLEMENTAR, 52=13SAL))
- `codigo_recolhimento`: Filtra CODIGO_RECOLHIMENTO (char). Aceita: valor simples (igualdade), igual, lista de valores. (Código de recolhimento)
- `vencimento`: Filtra DATA_VENCIMENTO (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data do vencimento) Datas no formato AAAA-MM-DD.
- `saldo_a_recolher`: Filtra SALDO_RECOLHER (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Saldo a recolher)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `guia_imposto_totais`

Guias de impostos (apuração por código de recolhimento) — TOTAIS por grupo da tabela efsdoimp_por_recolhimento (módulo guias). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DATA_SIM. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: saldo_a_recolher, valor_pago, saldo_devedor, saldo_credor, saldo_credor_anterior, valor_contabil_saida, base_calculo_saida, imposto_saida, valor_contabil_entrada, base_calculo_entrada, imposto_entrada, outros_creditos, outros_debitos, estorno_creditos, estorno_debitos, outros_acrescimos, credito_presumido, estorno_credito_presumido, compensacao_pagamento_indevido, creditos_devolucao_entradas, creditos_devolucao_saidas, valor_diferido, valor_diferido_anterior. CAMPOS PARA AGRUPAR: imposto_codigo, competencia:mes, periodicidade, recolhimento_sequencial, codigo_recolhimento, parcela, vencimento:mes, classe_vencimento, outras_deducoes, isentas_saida, outras_saida, isentas_entrada, outras_entrada, regime_especial, estorno_regime_especial, outras_compensacoes. Os filtros são os mesmos de guia_imposto_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (periodicidade) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Saldo a recolher: em 17.951 linhas de 2024 em diante com saldo a recolher, 17.926 (99,9%) têm saldo_a_recolher = saldo_devedor; só 2 têm saldo devedor zero. 28.910 de 408.276 linhas têm saldo a recolher. | O REGISTRO DE PAGAMENTOS PAROU: linhas com saldo a recolher e valor pago: 2018 733 de 877 · 2019 1.125 de 1.260 · 2020 1.313 de 1.460 · 2021 1.784 de 2.122 · 2022 1.874 de 2.442 · 2023 1.525 de 2.738 · 2024 17 de 6.347 · 2025 6 de 6.742 · 2026 0 de 4.862. Não conclua que uma guia de 2024 em diante está em aberto só porque não tem valor pago. | Pagamento: nas 60 empresas com mais pagamentos em 2023-2024, valor_pago desta tabela é igual à soma de pagamento_imposto (vpag) por imposto, competência e periodicidade em 2.044 de 2.082 guias com saldo (98,2%); em 37 a soma dos pagamentos é MAIOR que o valor_pago e em nenhuma é menor (1 guia não entrou na comparação). | Vencimento: a classe de vencimento é 0 em 407.652 linhas e 10049 em 624. Todas as linhas têm data de vencimento (0 nulas).. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `competencia`: Filtra DATA_SIM (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competência) Datas no formato AAAA-MM-DD.
- `imposto_codigo`: Filtra CODI_IMP (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Imposto)
- `periodicidade`: Filtra PDIC_SIM (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=1º decêndio, 2=2º decêndio, 3=3º decêndio, 4=1ª quinzena, 5=2ª quinzena, 6=Mensal, 7=Trimestral, 11=1ª semana, 12=2ª semana, 13=3ª semana, … (+4) (Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=COMPLEMENTAR, 52=13SAL))
- `codigo_recolhimento`: Filtra CODIGO_RECOLHIMENTO (char). Aceita: valor simples (igualdade), igual, lista de valores. (Código de recolhimento)
- `vencimento`: Filtra DATA_VENCIMENTO (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data do vencimento) Datas no formato AAAA-MM-DD.
- `saldo_a_recolher`: Filtra SALDO_RECOLHER (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Saldo a recolher)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["competencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["saldo_a_recolher"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `codigo_receita_imposto_consultar`

Códigos de receita permitidos por imposto e vigência — tabela geimposto_vigencia_codrec (módulo guias, ~38.319 linhas).
O QUE É: Códigos de receita selecionáveis para os impostos que restringem o código, por empresa e vigência, com descrição. 38.319 linhas, 1.504 empresas, mas só 19 códigos distintos.
COMENTÁRIO DO BANCO SOBRE A TABELA: Impostos - Cadastro - Codigos de Recolhimento
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): imposto_codigo.
FILTROS: imposto_codigo, vigencia, codigo_receita, descricao. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: imposto_codigo, vigencia, codigo_receita, descricao. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 10059 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Só 19 códigos de receita distintos em 38.319 linhas. A lista é usada por poucas regras: nas 40 empresas com mais regras, só 241 de 17.343 regras de recolhimento têm o código na lista (1,4%); para a maioria dos impostos o código é digitado direto na regra.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `imposto_codigo`: Filtra CODI_IMP (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Imposto)
- `vigencia`: Filtra VIGENCIA_IMP (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.
- `codigo_receita`: Filtra CODI_REC (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Codigo do recolhimento)
- `descricao`: Filtra DESCRICAO (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}. (Descricao)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `codigo_receita_imposto_obter`

Códigos de receita permitidos por imposto e vigência — obtém UM registro pela chave (CODI_EMP, CODI_IMP, VIGENCIA_IMP, CODI_REC) da tabela geimposto_vigencia_codrec. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use codigo_receita_imposto_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP).
- `imposto_codigo` (obrigatório): Filtra CODI_IMP (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Imposto)
- `vigencia` (obrigatório): Filtra VIGENCIA_IMP (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.
- `codigo_receita` (obrigatório): Filtra CODI_REC (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Codigo do recolhimento)

## `regra_recolhimento_consultar`

Regras de recolhimento por imposto e vigência — tabela geimposto_vigencia_recolhimento (módulo guias, ~315.670 linhas).
O QUE É: Para cada imposto de uma empresa e vigência: código de recolhimento (receita), periodicidade, dias de vencimento (até 5), classes de vencimento, alíquota, forma de recolhimento e se gera crédito de ICMS. É a regra que gera as guias de guia_imposto. 315.670 linhas, 1.503 empresas; 177.414 (56%) têm periodicidade "por nota". Usa 29 das 45 colunas.
COMENTÁRIO DO BANCO SOBRE A TABELA: Impostos - Cadastro - Codigo de Recolhimento
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): imposto_codigo.
FILTROS: imposto_codigo, vigencia, codigo_recolhimento, periodicidade. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: imposto_codigo, vigencia, recolhimento_sequencial, codigo_recolhimento, descricao, tipo_guia, periodicidade, periodo_subsequente, forma_vencimento, dia_vencimento_1, dia_vencimento_2, dia_vencimento_3, dia_vencimento_4, dia_vencimento_5, classe_vencimento_1, classe_vencimento_2, aliquota, tipo, forma_recolhimento, gera_credito_icms, utilizar_credito_na_apuracao_icms, apropriacao_credito, tipo_antecipacao, uf_favorecida, calcula_adicional_fcp, irrf_cooperativa, codigo_sped_fiscal, fundamentacao_legal, numero_ttd_1. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): imposto_nome, imposto_sigla.
EXEMPLO COM DADOS: a empresa 941 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Código de recolhimento: a guia (guia_imposto) herda o código da regra (mesma empresa, imposto e sequência, vigência mais recente até a competência): 7.426 de 7.427 guias de 2023 das 80 empresas com mais guias. | Vencimento (guias de 2022-2023 com saldo, 3.316): 2.072 (62,5%) vencem exatamente num dos dias configurados; 939 (28,3%) vencem ANTECIPADOS para o dia útil anterior quando o dia configurado cai no sábado ou domingo (ex.: dia 20 vira sexta 18 ou 19); 305 (9,2%) não foram explicados (provavelmente feriados, não modelados). […] | Periodicidades em uso: 7 (por nota) 177.417 · 1 (mensal) 133.662 · 2 (quinzenal) 3.177 · 3 (decendial) 1.397 · 5 (semanal) 12 · 10 (sem legenda) 5. Tipo de guia sempre 1. Combinações com a forma de vencimento mais comuns: 7 (por nota) com forma 6 · 177.414; 1 (mensal) com forma 4 · 92.010; 1 com forma 1 · 40.705; […] | Tipo da regra: normal (1) em 314.011 e TTD (2) em 1.659; forma de recolhimento sempre 1 (junto com o ICMS normal). A vigência mais antiga é 1964-06-01 (valor padrão).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `imposto_codigo`: Filtra CODI_IMP (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `vigencia`: Filtra VIGENCIA_IMP (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.
- `codigo_recolhimento`: Filtra CODIGO_RECOLHIMENTO (char). Aceita: valor simples (igualdade), igual, lista de valores. (Código do recolhimento)
- `periodicidade`: Filtra PERIODICIDADE (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Mensal, 2=Quinzenal, 3=Decendial, 4=Trimestral, 5=Semanal, 6=Semestral, 7=Por nota, 10=Sem legenda [parcialmente confirmado] (Periodicidade (1-Mensal/2-Quinzenal/3-Decendial/4-Trimestral/5-Semanal/6-Semestral/7-Por Nota/8-Trimestral/Mensal/9-Por Vencimento/10-Diária))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `regra_recolhimento_totais`

Regras de recolhimento por imposto e vigência — TOTAIS por grupo da tabela geimposto_vigencia_recolhimento (módulo guias). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): imposto_codigo. CAMPOS SOMÁVEIS: utilizar_credito_na_apuracao_icms, apropriacao_credito. CAMPOS PARA AGRUPAR: imposto_codigo, vigencia:mes, recolhimento_sequencial, codigo_recolhimento, descricao, tipo_guia, periodicidade, periodo_subsequente, forma_vencimento, dia_vencimento_1, dia_vencimento_2, dia_vencimento_3, dia_vencimento_4, dia_vencimento_5, classe_vencimento_1, classe_vencimento_2, aliquota, tipo, forma_recolhimento, gera_credito_icms, tipo_antecipacao, uf_favorecida, calcula_adicional_fcp, irrf_cooperativa, codigo_sped_fiscal, fundamentacao_legal, numero_ttd_1. Os filtros são os mesmos de regra_recolhimento_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (tipo_guia, periodicidade, tipo, forma_recolhimento) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Código de recolhimento: a guia (guia_imposto) herda o código da regra (mesma empresa, imposto e sequência, vigência mais recente até a competência): 7.426 de 7.427 guias de 2023 das 80 empresas com mais guias. | Vencimento (guias de 2022-2023 com saldo, 3.316): 2.072 (62,5%) vencem exatamente num dos dias configurados; 939 (28,3%) vencem ANTECIPADOS para o dia útil anterior quando o dia configurado cai no sábado ou domingo (ex.: dia 20 vira sexta 18 ou 19); 305 (9,2%) não foram explicados (provavelmente feriados, não modelados). Aparece nos impostos de maior volume (25 e 16); a regra de antecipação não está gravada no banco, é inferida. | Periodicidades em uso: 7 (por nota) 177.417 · 1 (mensal) 133.662 · 2 (quinzenal) 3.177 · 3 (decendial) 1.397 · 5 (semanal) 12 · 10 (sem legenda) 5. Tipo de guia sempre 1. Combinações com a forma de vencimento mais comuns: 7 (por nota) com forma 6 · 177.414; 1 (mensal) com forma 4 · 92.010; 1 com forma 1 · 40.705; 2 (quinzenal) com forma 5 · 3.177; 3 (decendial) com forma 3 · 1.397. O comentário da forma de vencimento não traz legenda. | Tipo da regra: normal (1) em 314.011 e TTD (2) em 1.659; forma de recolhimento sempre 1 (junto com o ICMS normal). A vigência mais antiga é 1964-06-01 (valor padrão).. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `imposto_codigo`: Filtra CODI_IMP (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `vigencia`: Filtra VIGENCIA_IMP (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.
- `codigo_recolhimento`: Filtra CODIGO_RECOLHIMENTO (char). Aceita: valor simples (igualdade), igual, lista de valores. (Código do recolhimento)
- `periodicidade`: Filtra PERIODICIDADE (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Mensal, 2=Quinzenal, 3=Decendial, 4=Trimestral, 5=Semanal, 6=Semestral, 7=Por nota, 10=Sem legenda [parcialmente confirmado] (Periodicidade (1-Mensal/2-Quinzenal/3-Decendial/4-Trimestral/5-Semanal/6-Semestral/7-Por Nota/8-Trimestral/Mensal/9-Por Vencimento/10-Diária))
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["vigencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["utilizar_credito_na_apuracao_icms"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).
