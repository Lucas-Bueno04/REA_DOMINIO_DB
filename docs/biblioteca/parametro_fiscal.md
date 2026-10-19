# Módulo `parametro_fiscal`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `acumulador_vigencia_consultar` | consultar | efacumulador_vigencia | empresa | ✔ |
| `acumulador_vigencia_obter` | obter | efacumulador_vigencia | empresa, acumulador_codigo, vigencia | ✔ |
| `acumulador_vigencia_cfop_consultar` | consultar | efacumulador_vigencia_cfop | empresa | ✔ |
| `acumulador_vigencia_cfop_obter` | obter | efacumulador_vigencia_cfop | empresa, acumulador_codigo, vigencia, cfop | ✔ |
| `acumulador_vigencia_imposto_consultar` | consultar | efacumulador_vigencia_impostos | empresa | ✔ |
| `acumulador_vigencia_imposto_obter` | obter | efacumulador_vigencia_impostos | empresa, acumulador_codigo, vigencia, imposto_codigo | ✔ |
| `acumulador_vigencia_aliquota_consultar` | consultar | efacumulador_vigencia_impostos_aliquotas | empresa | ✔ |
| `acumulador_vigencia_conta_consultar` | consultar | efacumulador_vigencia_impostos_contas | empresa | ✔ |
| `acumulador_vigencia_conta_obter` | obter | efacumulador_vigencia_impostos_contas | empresa, acumulador_codigo, vigencia, imposto_codigo | ✔ |
| `acumulador_vigencia_conta_totais` | totais | efacumulador_vigencia_impostos_contas | empresa | ✔ |
| `parametro_fiscal_geral_consultar` | consultar | efparametro | empresa | ✔ |
| `parametro_fiscal_consultar` | consultar | efparametro_vigencia | empresa | ✔ |
| `parametro_fiscal_obter` | obter | efparametro_vigencia | empresa, vigencia | ✔ |
| `parametro_fiscal_totais` | totais | efparametro_vigencia | empresa | ✔ |
| `parametro_fiscal_imposto_consultar` | consultar | efparametro_vigencia_impostos | empresa | ✔ |
| `parametro_fiscal_imposto_obter` | obter | efparametro_vigencia_impostos | empresa, vigencia, imposto_codigo | ✔ |

## `acumulador_vigencia_consultar`

Acumuladores fiscais por vigência (configuração) — tabela efacumulador_vigencia (módulo parametro_fiscal, ~460.804 linhas).
O QUE É: Cada acumulador classifica as notas (entrada, saída, serviço) e define como entram na receita, no faturamento, nos impostos e na contabilidade. A configuração vale por vigência: o acumulador em vigor numa nota é o de maior `vigencia` até a data da nota (as notas não guardam a vigência). 460.803 linhas, 1.419 empresas, 434 mil acumuladores (96% com uma só vigência).
COMENTÁRIO DO BANCO SOBRE A TABELA: Acumuladores - Cadastro
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: acumulador_codigo, vigencia, descricao, incide_receita_bruta, incide_devolucao. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: acumulador_codigo, vigencia, descricao, incide_receita_bruta, incide_faturamento, incide_devolucao, incide_acrescimo_financeiro, enquadramento_epp, faz_estoque_dipi, gera_bens_patrimonio, gera_parcelas, tipo_nota, nota_transferencia_credito, confere_natureza, nota_cancelada, servico_terceirizado, incide_simples_municipal, simples_nao_somar_servico_50, simples_aliquota_diferenciada, simples_credito_presumido, simples_entradas_mercadoria, produtos_sujeitos_st, credito_presumido, importacao_credito_icms, gera_entrada_outra_empresa, conta_debito, conta_credito, historico_padrao, conta_contrapartida_pagamento, conta_juros, conta_multa, conta_desconto, conta_devolucao, conta_icms_compras, cop. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 112 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Receita bruta do Simples: as notas de saída, serviços e CF-e contam na receita quando o acumulador em vigor na data tem `incide_receita_bruta` = S; as devoluções lançadas em entradas abatem quando `incide_devolucao` = S. Conferido em 38 de 40 empresa/competências sorteadas (ver simples.apuracao_simples_nacional). | Indicadores (460.803 vigências): receita = faturamento = S em 138.517 (inclui 23.216 que também incidem em devolução), ambos N em 322.111 (31.402 só devolução); receita S e faturamento N em 133 e o inverso em 42. Receita e faturamento quase sempre andam juntos. | 96% dos acumuladores (416.083 de 434.521) têm uma só vigência; 14.633 têm duas; o máximo é 15. | Tipo de nota: 458.456 vigências são O (outras), 1.236 V (à vista) e 1.111 P (a prazo): o tipo só é usado em poucos acumuladores.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `acumulador_codigo`: Filtra codi_acu (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `vigencia`: Filtra vigencia_acu (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.
- `descricao`: Filtra DESCRICAO_ACU (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Descricao)
- `incide_receita_bruta`: Filtra IREC_ACU (char). Aceita: valor simples (igualdade), igual. Códigos: S=Sim, N=Não (Incide sobre Receita Bruta (S/N))
- `incide_devolucao`: Filtra IDEV_ACU (char). Aceita: valor simples (igualdade), igual. Códigos: S=Sim, N=Não (Incide sobre Devolucao (S/N))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `acumulador_vigencia_obter`

Acumuladores fiscais por vigência (configuração) — obtém UM registro pela chave (codi_emp, codi_acu, vigencia_acu) da tabela efacumulador_vigencia. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use acumulador_vigencia_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `acumulador_codigo` (obrigatório): Filtra codi_acu (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `vigencia` (obrigatório): Filtra vigencia_acu (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.

## `acumulador_vigencia_cfop_consultar`

CFOPs permitidos em cada acumulador por vigência — tabela efacumulador_vigencia_cfop (módulo parametro_fiscal, ~767.782 linhas).
O QUE É: Lista de CFOPs (naturezas de operação) que o acumulador aceita numa vigência. Cada acumulador costuma ter 2 CFOPs (o estadual e o interestadual, ex.: 5xxx e 6xxx) ou 1. 767.782 linhas, 1.414 empresas, 512 CFOPs distintos.
COMENTÁRIO DO BANCO SOBRE A TABELA: Acumuladores - Cadastro - Naturezas
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): acumulador_codigo.
FILTROS: acumulador_codigo, vigencia, cfop. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: acumulador_codigo, vigencia, cfop, complemento_cfop_cat_17_99. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): acumulador_descricao.
EXEMPLO COM DADOS: a empresa 1703 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Número de CFOPs por acumulador/vigência: 2 em 349.322, 1 em 63.684, 3 em 1.653, 4 em 103; máximo 8. Todas as linhas têm o acumulador e a vigência correspondentes (0 órfãs em 767.782). | Conciliação com as notas: em 13.088 notas de saída de 2025 de 3 empresas médias, o CFOP da nota está na lista do acumulador vigente na data em 13.071 (99,9%); as outras 17 são de acumuladores sem lista de CFOPs.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `acumulador_codigo`: Filtra CODI_ACU (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Acumulador)
- `vigencia`: Filtra VIGENCIA_ACU (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.
- `cfop`: Filtra CODI_NAT (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Natureza)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `acumulador_vigencia_cfop_obter`

CFOPs permitidos em cada acumulador por vigência — obtém UM registro pela chave (CODI_EMP, CODI_ACU, VIGENCIA_ACU, CODI_NAT) da tabela efacumulador_vigencia_cfop. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use acumulador_vigencia_cfop_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP).
- `acumulador_codigo` (obrigatório): Filtra CODI_ACU (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Acumulador)
- `vigencia` (obrigatório): Filtra VIGENCIA_ACU (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.
- `cfop` (obrigatório): Filtra CODI_NAT (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Natureza)

## `acumulador_vigencia_imposto_consultar`

Impostos de cada acumulador por vigência — tabela efacumulador_vigencia_impostos (módulo parametro_fiscal, ~896.703 linhas).
O QUE É: Como cada acumulador trata cada imposto: alíquota da base de cálculo, onde lançar a diferença da base, redução, e o enquadramento no Simples Nacional (anexo, seção e tabela) usado na segregação da receita. 896.705 linhas, 40 impostos diferentes.
COMENTÁRIO DO BANCO SOBRE A TABELA: Acumuladores - Cadastro - Impostos
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): acumulador_codigo.
FILTROS: acumulador_codigo, vigencia, imposto_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: acumulador_codigo, vigencia, imposto_codigo, aliquota_base_calculo, diferenca_base_lancar_em, percentual_reducao, reduz_imposto, codigo_recolhimento_padrao, sequencial_recolhimento, simples_anexo, simples_secao, simples_tabela, simples_situacao_irpj, simples_situacao_csll, simples_situacao_cofins, simples_situacao_pis, simples_situacao_inss, simples_situacao_ipi, simples_situacao_icms, simples_situacao_iss, simples_reducao_base_icms, simples_reducao_base_iss, simples_utilizar_reducao_icms, simples_servicos_702_705, modalidade_operacao, debito_especial_sped, dacon_tipo_receita. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): acumulador_descricao, imposto_nome, imposto_sigla.
EXEMPLO COM DADOS: a empresa 419 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Toda linha tem o acumulador e a vigência correspondentes em acumulador_vigencia (0 sem acumulador em 896.705). | O enquadramento no Simples (anexo preenchido) está quase só no imposto 44 (Simples Nacional): 33.057 linhas; seguem IPI 528, PIS 204, Simples MEI 19 e outros com poucas linhas.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `acumulador_codigo`: Filtra CODI_ACU (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Acumulador)
- `vigencia`: Filtra VIGENCIA_ACU (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.
- `imposto_codigo`: Filtra CODI_IMP (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Imposto)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `acumulador_vigencia_imposto_obter`

Impostos de cada acumulador por vigência — obtém UM registro pela chave (CODI_EMP, CODI_ACU, VIGENCIA_ACU, CODI_IMP) da tabela efacumulador_vigencia_impostos. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use acumulador_vigencia_imposto_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP).
- `acumulador_codigo` (obrigatório): Filtra CODI_ACU (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Acumulador)
- `vigencia` (obrigatório): Filtra VIGENCIA_ACU (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.
- `imposto_codigo` (obrigatório): Filtra CODI_IMP (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Imposto)

## `acumulador_vigencia_aliquota_consultar`

Alíquotas pré-definidas dos impostos de cada acumulador — tabela efacumulador_vigencia_impostos_aliquotas (módulo parametro_fiscal, ~379.002 linhas).
O QUE É: Alíquotas e percentual de base de cálculo pré-definidos para cada imposto de um acumulador numa vigência (mais de uma por imposto, pelo sequencial), com o tipo de alíquota de ICMS (informada ou por tabela), adicional, carga tributária e coeficiente. 379.002 linhas.
COMENTÁRIO DO BANCO SOBRE A TABELA: Acumuladores - Cadastro - Aliquotas
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): acumulador_codigo.
FILTROS: acumulador_codigo, vigencia, imposto_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: acumulador_codigo, vigencia, imposto_codigo, sequencial, aliquota, percentual_base_calculo, tipo_aliquota_icms, tabela_icms, adicional_aliquota, carga_tributaria, coeficiente. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 655 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Tipo de alíquota do ICMS: informada (A) em 378.968 linhas, por tabela (T) em 5 e vazio em 28. Todas as linhas têm o acumulador e a vigência correspondentes (0 órfãs em 379.002).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `acumulador_codigo`: Filtra CODI_ACU (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Acumulador)
- `vigencia`: Filtra VIGENCIA_ACU (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.
- `imposto_codigo`: Filtra CODI_IMP (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Imposto)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `acumulador_vigencia_conta_consultar`

Contas contábeis dos impostos de cada acumulador — tabela efacumulador_vigencia_impostos_contas (módulo parametro_fiscal, ~453.490 linhas).
O QUE É: Contas e históricos padrão que a contabilização usa para cada imposto de um acumulador: imposto a recolher, a recuperar, sobre vendas, sobre compras, devoluções e estornos, e se gera lançamento contábil. 453.490 linhas, 1.417 empresas.
COMENTÁRIO DO BANCO SOBRE A TABELA: Acumuladores - Cadastro - Impostos - Contas
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): acumulador_codigo.
FILTROS: acumulador_codigo, vigencia, imposto_codigo, gera_lancamento_contabil. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: acumulador_codigo, vigencia, imposto_codigo, conta_imposto_a_recolher, historico_imposto_a_recolher, conta_imposto_a_recuperar, historico_imposto_a_recuperar, conta_imposto_sobre_vendas, conta_imposto_sobre_compras, conta_devolucao_vendas, conta_devolucao_compras, historico_devolucao_compras, gera_lancamento_contabil, historico_estorno_debito, historico_credito_venda_fora_estabelecimento. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): imposto_nome, imposto_sigla.
EXEMPLO COM DADOS: a empresa 1566 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Gera lançamento contábil (S) em 453.474 linhas e não (N) em 17. Todas as linhas têm o acumulador e a vigência correspondentes (0 órfãs em 453.490).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `acumulador_codigo`: Filtra CODI_ACU (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Acumulador)
- `vigencia`: Filtra VIGENCIA_ACU (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.
- `imposto_codigo`: Filtra CODI_IMP (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Imposto)
- `gera_lancamento_contabil`: Filtra GERA_LAN_CTB_IAC (char). Aceita: valor simples (igualdade), igual. Códigos: S=Sim, N=Não (Gera lancamentos contabeis(S/N))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `acumulador_vigencia_conta_obter`

Contas contábeis dos impostos de cada acumulador — obtém UM registro pela chave (CODI_EMP, CODI_ACU, VIGENCIA_ACU, CODI_IMP) da tabela efacumulador_vigencia_impostos_contas. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use acumulador_vigencia_conta_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP).
- `acumulador_codigo` (obrigatório): Filtra CODI_ACU (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Acumulador)
- `vigencia` (obrigatório): Filtra VIGENCIA_ACU (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.
- `imposto_codigo` (obrigatório): Filtra CODI_IMP (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Imposto)

## `acumulador_vigencia_conta_totais`

Contas contábeis dos impostos de cada acumulador — TOTAIS por grupo da tabela efacumulador_vigencia_impostos_contas (módulo parametro_fiscal). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): acumulador_codigo. CAMPOS SOMÁVEIS: historico_imposto_a_recolher, historico_imposto_a_recuperar, historico_estorno_debito, historico_credito_venda_fora_estabelecimento. CAMPOS PARA AGRUPAR: acumulador_codigo, vigencia:mes, imposto_codigo, conta_imposto_a_recolher, conta_imposto_a_recuperar, conta_imposto_sobre_vendas, conta_imposto_sobre_compras, conta_devolucao_vendas, conta_devolucao_compras, historico_devolucao_compras, gera_lancamento_contabil. Os filtros são os mesmos de acumulador_vigencia_conta_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (gera_lancamento_contabil) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Gera lançamento contábil (S) em 453.474 linhas e não (N) em 17. Todas as linhas têm o acumulador e a vigência correspondentes (0 órfãs em 453.490).. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `acumulador_codigo`: Filtra CODI_ACU (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Acumulador)
- `vigencia`: Filtra VIGENCIA_ACU (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.
- `imposto_codigo`: Filtra CODI_IMP (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Imposto)
- `gera_lancamento_contabil`: Filtra GERA_LAN_CTB_IAC (char). Aceita: valor simples (igualdade), igual. Códigos: S=Sim, N=Não (Gera lancamentos contabeis(S/N))
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["vigencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["historico_imposto_a_recolher"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `parametro_fiscal_geral_consultar`

Parâmetros gerais da escrita fiscal (sem vigência) — tabela efparametro (módulo parametro_fiscal, ~1.434 linhas).
O QUE É: Opções da escrita fiscal que não variam por vigência: período atual de trabalho, data de fechamento (não se lança depois dela), SPED, controle de estoque, forma de lançar clientes e fornecedores e integração contábil. Uma linha por empresa (1.434). Usa 38 das 135 colunas; as demais são opções de tela e de regras estaduais.
COMENTÁRIO DO BANCO SOBRE A TABELA: Paramentros - Cadastro - Escrita Fiscal
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
FILTROS: periodo_atual, fechamento_fiscal, gera_sped_fiscal. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: periodo_atual, periodo_inicial, fechamento_fiscal, inicio_efetivo_atividades, simples_inicio_no_sistema, controla_estoque, gera_movimento_produtos_sintegra, gera_sped, gera_sped_fiscal, perfil_sped, gera_lancamentos_contabeis, gera_perdcomp, gera_informacoes_sintegra, verifica_inscricao_estadual, lancamento_fornecedor_por, lancamento_cliente_por, opcao_lancamento_produtos, sequencia_automatica_saidas_servicos, controla_contas_a_pagar_receber, usa_tabelas_municipais, controla_aidf, informativo_nota_fiscal_paulista, importa_nfe_do_site_da_receita, informa_chave_nfe_terceiros, distribuidora_de_combustivel, limite_lancamento_reducao_z, utiliza_dominio_cliente, scanc_ctb, entrega_a_domicilio. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): empresa_nome.
EXEMPLO COM DADOS: a empresa 1409 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Uma linha por empresa (1.434 empresas; todas têm vigência em parametro_fiscal, 0 sem). Período atual de 2010-01 a 2026-09. | Fechamento fiscal (`fechamento_fiscal`, 'não é permitido lançamento após esta data'): preenchido nas 1.434 empresas, de 1966-06-30 a 2026-04-30; é anterior ao período atual em 1.433 e posterior em 1 — o fechamento costuma estar ATRASADO em relação ao período de trabalho. Datas como 1966 são provavelmente 'sem fechamento'. | SPED Fiscal: gera (S) em 921 empresas e não em 513; o controle genérico `gera_sped` é N em todas as 1.434. Controla estoque (1) em 1.429 empresas e não (2) em 5; gera lançamentos contábeis em 1.431 e não em 3. | Perfil do SPED é A em todas; lançamento de produtos Normal (N) em 1.430 e NCM (C) em 4. O início do cálculo do Simples no sistema está preenchido em 358 empresas (de 2015-01 a 2026-09).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo_atual`: Filtra PERI_PAR (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Periodo atual) Datas no formato AAAA-MM-DD.
- `fechamento_fiscal`: Filtra PFEC_PAR (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data do fechamento, nao e permitido lancto apos esta data) Datas no formato AAAA-MM-DD.
- `gera_sped_fiscal`: Filtra SPED_FISCAL_PAR (char). Aceita: valor simples (igualdade), igual. Códigos: S=Sim, N=Não (Gera SPED Fiscal (S/N))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `parametro_fiscal_consultar`

Parâmetros da escrita fiscal por vigência — tabela efparametro_vigencia (módulo parametro_fiscal, ~6.450 linhas).
O QUE É: Configuração fiscal de cada empresa a partir de uma data (vigência): regimes federal, estadual e municipal, geração de lançamentos contábeis, integração das notas, fatos geradores das retenções e opções do Simples. Cada alteração de regime cria uma nova vigência; a vigente em uma data é a mais recente com `vigencia` até essa data. 6.449 linhas, 1.434 empresas (308 com uma só vigência, até 24). Usa ~45 das 650+ colunas.
COMENTÁRIO DO BANCO SOBRE A TABELA: Paramentros - Cadastro - Escrita Fiscal
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna vigencia_par. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: vigencia, regime_federal, regime_estadual. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: vigencia, descricao, regime_federal, regime_estadual, regime_municipal, regime_recolhimento, gera_lancamentos_contabeis, lancamentos_em_outra_empresa, empresa_da_contabilidade, processa_filiais, agrupa_lancamentos_filiais, apuracao_consolidada, centralizacao_recolhimento, gera_honorarios, substituicao_tributaria, integracao_entradas, integracao_saidas, integracao_servicos, cada_fornecedor_gera_conta, cada_cliente_gera_conta, fato_gerador_crf, fato_gerador_irrf, fato_gerador_crf_pf, fato_gerador_irrf_pf, prestadora_servico_base_16, deduz_st_base_irpj_csll, transfere_creditos_acumulados, calcula_adicional_icms, simples_saldo_negativo_proximo_mes, simples_federal_com_iss, simples_50_prestadoras, simples_aliquota_diferenciada, regime_especial_st, margem_valor_agregado. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): empresa_nome, empresa_cnpj_cpf.
EXEMPLO COM DADOS: a empresa 1359 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Vigência em vigor numa data = a de maior `vigencia` menor ou igual a essa data, por empresa (a mesma regra vale para acumuladores; validada na receita do Simples: 38 de 40 competências fecham ao centavo). 308 empresas têm 1 vigência, 198 têm 2 e há empresas com até 24. | Regime federal (rfed_par), vigência mais recente por empresa: 5 = lucro presumido (733 empresas), 4 = Simples Nacional (466), 1 = provável lucro real (170), 2 = variante do Simples (29), 9 (32) incerto, 6 e 8 (2 cada) não determinados. A legenda NÃO consta no banco; ver a nota do domínio regime_federal_fiscal. […] | Regime estadual 13 não está no comentário do banco (que lista 1 a 4) e é o único além do 1: 1.736 das 1.764 vigências de regime federal 4 e 103 das 114 de regime federal 2 têm 13; todas as demais têm 1. | Regime de recolhimento: todas as 6.449 vigências têm R (real), inclusive as de lucro presumido: o campo não identifica o regime de tributação. 6.429 vigências geram lançamentos contábeis (lctb = S) e 20 não. | Há vigência datada de 1964-06-01 (a mais antiga); datas anteriores a 2000 provavelmente são digitação do ano.
POSSÍVEIS DADOS PESSOAIS/FINANCEIROS (os dados saem em claro; devolva só o que a pergunta exigir): empresa_cnpj_cpf.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `vigencia`: Filtra vigencia_par (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.
- `regime_federal`: Filtra RFED_PAR (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Lucro real (provável), 2=Simples - variante do Simples Nacional (por evidência), 4=Simples Nacional, 5=Lucro presumido, 6=Não determinado, 8=Não determinado, 9=Não determinado [parcialmente confirmado] (Regime federal (1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9))
- `regime_estadual`: Filtra REST_PAR (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Normal, 13=Simples Nacional (por evidência) [parcialmente confirmado] (Regime estadual (1 - Normal/2 - ME/3 - Estimativa/4 - EPP))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `parametro_fiscal_obter`

Parâmetros da escrita fiscal por vigência — obtém UM registro pela chave (codi_emp, vigencia_par) da tabela efparametro_vigencia. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use parametro_fiscal_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `vigencia` (obrigatório): Filtra vigencia_par (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.

## `parametro_fiscal_totais`

Parâmetros da escrita fiscal por vigência — TOTAIS por grupo da tabela efparametro_vigencia (módulo parametro_fiscal). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna vigencia_par. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: empresa_da_contabilidade, margem_valor_agregado. CAMPOS PARA AGRUPAR: vigencia:mes, descricao, regime_federal, regime_estadual, regime_municipal, regime_recolhimento, gera_lancamentos_contabeis, lancamentos_em_outra_empresa, processa_filiais, agrupa_lancamentos_filiais, apuracao_consolidada, centralizacao_recolhimento, gera_honorarios, substituicao_tributaria, integracao_entradas, integracao_saidas, integracao_servicos, cada_fornecedor_gera_conta, cada_cliente_gera_conta, fato_gerador_crf, fato_gerador_irrf, fato_gerador_crf_pf, fato_gerador_irrf_pf, prestadora_servico_base_16, deduz_st_base_irpj_csll, transfere_creditos_acumulados, calcula_adicional_icms, simples_saldo_negativo_proximo_mes, simples_federal_com_iss, simples_50_prestadoras, simples_aliquota_diferenciada, regime_especial_st. Os filtros são os mesmos de parametro_fiscal_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (regime_federal, regime_estadual, regime_municipal, regime_recolhimento) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Vigência em vigor numa data = a de maior `vigencia` menor ou igual a essa data, por empresa (a mesma regra vale para acumuladores; validada na receita do Simples: 38 de 40 competências fecham ao centavo). 308 empresas têm 1 vigência, 198 têm 2 e há empresas com até 24. | Regime federal (rfed_par), vigência mais recente por empresa: 5 = lucro presumido (733 empresas), 4 = Simples Nacional (466), 1 = provável lucro real (170), 2 = variante do Simples (29), 9 (32) incerto, 6 e 8 (2 cada) não determinados. A legenda NÃO consta no banco; ver a nota do domínio regime_federal_fiscal. Cruze com a apuração (efsdoimp_simples_nacional, IRPJ) antes de afirmar o regime de uma empresa. | Regime estadual 13 não está no comentário do banco (que lista 1 a 4) e é o único além do 1: 1.736 das 1.764 vigências de regime federal 4 e 103 das 114 de regime federal 2 têm 13; todas as demais têm 1. | Regime de recolhimento: todas as 6.449 vigências têm R (real), inclusive as de lucro presumido: o campo não identifica o regime de tributação. 6.429 vigências geram lançamentos contábeis (lctb = S) e 20 não.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `vigencia`: Filtra vigencia_par (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.
- `regime_federal`: Filtra RFED_PAR (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Lucro real (provável), 2=Simples - variante do Simples Nacional (por evidência), 4=Simples Nacional, 5=Lucro presumido, 6=Não determinado, 8=Não determinado, 9=Não determinado [parcialmente confirmado] (Regime federal (1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9))
- `regime_estadual`: Filtra REST_PAR (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Normal, 13=Simples Nacional (por evidência) [parcialmente confirmado] (Regime estadual (1 - Normal/2 - ME/3 - Estimativa/4 - EPP))
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["vigencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["empresa_da_contabilidade"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `parametro_fiscal_imposto_consultar`

Impostos ativos em cada vigência dos parâmetros fiscais — tabela efparametro_vigencia_impostos (módulo parametro_fiscal, ~89.621 linhas).
O QUE É: Quais impostos a empresa apura em cada vigência (89.618 linhas, 1.434 empresas, 54 impostos diferentes).
COMENTÁRIO DO BANCO SOBRE A TABELA: Paramentros - Cadastro - Escrita Fiscal - Impostos
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna vigencia_par. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: vigencia, imposto_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: vigencia, imposto_codigo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): imposto_nome, imposto_sigla.
EXEMPLO COM DADOS: a empresa 676 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Toda linha tem a vigência correspondente em parametro_fiscal (0 órfãs em 89.618).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
UTILIDADE LIMITADA: a tabela expõe só 2 campo(s) (tabela de apoio/ligação); ela NÃO traz o conteúdo que o nome pode sugerir (XML, arquivo, etc.).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `vigencia`: Filtra vigencia_par (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.
- `imposto_codigo`: Filtra codi_imp (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Imposto)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `parametro_fiscal_imposto_obter`

Impostos ativos em cada vigência dos parâmetros fiscais — obtém UM registro pela chave (codi_emp, vigencia_par, codi_imp) da tabela efparametro_vigencia_impostos. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use parametro_fiscal_imposto_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `vigencia` (obrigatório): Filtra vigencia_par (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.
- `imposto_codigo` (obrigatório): Filtra codi_imp (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Imposto)
