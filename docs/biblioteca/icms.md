# Módulo `icms`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `ajuste_apuracao_consultar` | consultar | efajustes | empresa | ✔ |
| `ajuste_apuracao_obter` | obter | efajustes | empresa, ajuste_codigo | ✔ |
| `apuracao_icms_st_uf_consultar` | consultar | efsdoimp_subtri_por_uf | empresa | ✔ |
| `apuracao_icms_st_uf_totais` | totais | efsdoimp_subtri_por_uf | empresa | ✔ |

## `ajuste_apuracao_consultar`

Códigos de ajuste da apuração — tabela efajustes (módulo icms, ~50.027 linhas).
O QUE É: Cadastro de códigos de ajuste da apuração por empresa (nome, imposto, tipo de operação e as contas e o histórico usados na contabilização). Cada empresa tem 35 códigos padrão (1.418 empresas), mais os que cria. 50.027 linhas.
COMENTÁRIO DO BANCO SOBRE A TABELA: Ajustes - Cadastro
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: ajuste_codigo, nome, operacao, imposto_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: ajuste_codigo, nome, imposto_codigo, operacao, conta_debito, conta_credito, historico_padrao. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): imposto_nome, imposto_sigla.
EXEMPLO COM DADOS: a empresa 643 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Por operação: 1 (outros créditos) 18.585 · 3 (outros débitos) 14.290 · 5 (outras deduções) 4.288 · 2 (estorno de débitos) 2.860 · 4 (estorno de créditos) 2.858 · 6 (outros acréscimos) 2.858 · 7 (outros recolhimentos) 2.858 · 43 (créditos do ativo permanente) 1.429 · 18 (1). 1.429 empresas têm os códigos padrão. | Contas de débito e crédito estão preenchidas em 50.015 dos 50.027 ajustes.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `ajuste_codigo`: Filtra codi_aju (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `nome`: Filtra nome_aju (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Nome)
- `operacao`: Filtra oper_aju (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Outros créditos, 2=Estorno de débitos, 3=Outros débitos, 4=Estorno de créditos, 5=Outras deduções, 6=Outros acréscimos, 7=Outros recolhimentos, 18=Pagamento antecipado do mês anterior, 43=Créditos do ativo permanente [parcialmente confirmado] (Operacao)
- `imposto_codigo`: Filtra codi_imp (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Imposto)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `ajuste_apuracao_obter`

Códigos de ajuste da apuração — obtém UM registro pela chave (codi_emp, codi_aju) da tabela efajustes. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use ajuste_apuracao_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `ajuste_codigo` (obrigatório): Filtra codi_aju (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `apuracao_icms_st_uf_consultar`

Apuração do ICMS-ST por UF — tabela efsdoimp_subtri_por_uf (módulo icms, ~706.131 linhas).
O QUE É: Desdobra a apuração da substituição tributária por UF favorecida (27 UFs) em cada empresa, competência e recolhimento: débitos e créditos, estornos, deduções, saldo devedor ou credor, valor pago e vencimento. A tabela guarda uma linha para TODAS as UFs de cada apuração: de 706.590 linhas só 1.076 têm saldo. 633 empresas, de 2007-04 a 2026-09.
COMENTÁRIO DO BANCO SOBRE A TABELA: Saldo dos Impostos - Substituição Tributária Por UF
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): periodo, uf.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DATA_SIM. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: competencia, uf, imposto_codigo, saldo_devedor. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: imposto_codigo, competencia, periodicidade, uf, recolhimento_sequencial, valor_contabil_entradas, base_calculo_entradas, imposto_entradas, valor_contabil_saidas, base_calculo_saidas, imposto_saidas, outros_debitos, estorno_creditos, outros_creditos, estorno_debitos, acrescimos, deducoes, saldo_credor_anterior, saldo_diferido_anterior, saldo_diferido, ressarcimento_cfop_1603_2603, ressarcimento_cfop_5603_6603, icms_ressarcimento_st, saldo_devedor, saldo_credor, saldo_devedor_complementacao, outros_recolhimentos, valor_pago, vencimento, estorno_fcp_interestadual, estorno_devolucoes_fcp_interestadual, deducao_fcp_interestadual, saldo_liquido, debitos, creditos. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): imposto_nome, imposto_sigla.
EXEMPLO COM DADOS: a empresa 960 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Identidade da apuração: saldo devedor − saldo credor = (imposto das saídas + outros débitos + estorno de créditos + acréscimos) − (imposto das entradas + outros créditos + estorno de débitos + saldo credor anterior + deduções) em 706.590 de 706.590 linhas (tolerância 0,02); as colunas calculadas `debitos`, […] | Esparsidade: das 706.590 linhas, só 1.022 têm saldo devedor e 54 têm saldo credor; as outras 705.514 são zero. Para ver o que importa filtre `saldo_devedor` maior que zero (ou o saldo credor). | Cobre as 27 UFs, 633 empresas e competências de 2007-04 a 2026-09.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `competencia`: Filtra DATA_SIM (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia) Datas no formato AAAA-MM-DD.
- `uf`: Filtra SIGLA_UF (char). Aceita: valor simples (igualdade), igual, lista de valores. (Sigla da UF)
- `imposto_codigo`: Filtra CODI_IMP (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Imposto)
- `saldo_devedor`: Filtra SALDO_DEVEDOR (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Saldo devedor)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `apuracao_icms_st_uf_totais`

Apuração do ICMS-ST por UF — TOTAIS por grupo da tabela efsdoimp_subtri_por_uf (módulo icms). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): periodo, uf. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DATA_SIM. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor_contabil_entradas, base_calculo_entradas, imposto_entradas, valor_contabil_saidas, base_calculo_saidas, imposto_saidas, outros_debitos, estorno_creditos, outros_creditos, estorno_debitos, acrescimos, saldo_credor_anterior, saldo_diferido_anterior, saldo_diferido, icms_ressarcimento_st, saldo_devedor, saldo_credor, saldo_devedor_complementacao, valor_pago, deducao_fcp_interestadual. CAMPOS PARA AGRUPAR: imposto_codigo, competencia:mes, periodicidade, uf, recolhimento_sequencial, deducoes, ressarcimento_cfop_1603_2603, ressarcimento_cfop_5603_6603, outros_recolhimentos, vencimento:mes, estorno_fcp_interestadual, estorno_devolucoes_fcp_interestadual. Os filtros são os mesmos de apuracao_icms_st_uf_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (periodicidade) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Identidade da apuração: saldo devedor − saldo credor = (imposto das saídas + outros débitos + estorno de créditos + acréscimos) − (imposto das entradas + outros créditos + estorno de débitos + saldo credor anterior + deduções) em 706.590 de 706.590 linhas (tolerância 0,02); as colunas calculadas `debitos`, `creditos` e `saldo_liquido` reproduzem isso. […] | Esparsidade: das 706.590 linhas, só 1.022 têm saldo devedor e 54 têm saldo credor; as outras 705.514 são zero. Para ver o que importa filtre `saldo_devedor` maior que zero (ou o saldo credor). | Cobre as 27 UFs, 633 empresas e competências de 2007-04 a 2026-09.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `competencia`: Filtra DATA_SIM (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia) Datas no formato AAAA-MM-DD.
- `uf`: Filtra SIGLA_UF (char). Aceita: valor simples (igualdade), igual, lista de valores. (Sigla da UF)
- `imposto_codigo`: Filtra CODI_IMP (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Imposto)
- `saldo_devedor`: Filtra SALDO_DEVEDOR (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Saldo devedor)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["competencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor_contabil_entradas"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).
