# Módulo `referencial`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `plano_referencial_ecf_consultar` | consultar | ctcontas_sped_ecf_geral | — | ✔ |
| `plano_referencial_ecf_obter` | obter | ctcontas_sped_ecf_geral | codigo | ✔ |
| `conta_referencial_ecf_consultar` | consultar | ctcontas_sped_ecf_geral_ref | empresa | ✔ |
| `conta_referencial_ecf_obter` | obter | ctcontas_sped_ecf_geral_ref | empresa, conta_codigo, conta_referencial_codigo | ✔ |
| `plano_referencial_ecf_imune_isenta_consultar` | consultar | ctcontas_sped_ecf_imune_isenta | — | ✔ |
| `plano_referencial_ecf_imune_isenta_obter` | obter | ctcontas_sped_ecf_imune_isenta | codigo | ✔ |
| `conta_referencial_ecf_imune_isenta_consultar` | consultar | ctcontas_sped_ecf_imune_isenta_ref | empresa | ✔ |
| `conta_referencial_ecf_imune_isenta_obter` | obter | ctcontas_sped_ecf_imune_isenta_ref | empresa, conta_codigo, conta_referencial_codigo | ✔ |
| `plano_referencial_srf_consultar` | consultar | ctcontas_srf | — | ✔ |
| `plano_referencial_srf_obter` | obter | ctcontas_srf | codigo | ✔ |
| `conta_referencial_srf_consultar` | consultar | ctcontas_srf_ref | empresa | ✔ |
| `conta_referencial_srf_obter` | obter | ctcontas_srf_ref | empresa, conta_codigo, conta_referencial_codigo | ✔ |
| `lancamento_referencial_srf_consultar` | consultar | ctlancto_referencial_srf | empresa | ✔ |
| `lancamento_referencial_srf_totais` | totais | ctlancto_referencial_srf | empresa | ✔ |
| `lancamento_scp_consultar` | consultar | ctlancto_scp | empresa | ✔ |
| `lancamento_scp_obter` | obter | ctlancto_scp | empresa, lancamento_numero, tipo | ✔ |
| `lancamento_referencial_ecf_consultar` | consultar | ctlancto_sped_ecf_geral | empresa | ✔ |
| `lancamento_referencial_ecf_totais` | totais | ctlancto_sped_ecf_geral | empresa | ✔ |
| `lancamento_referencial_ecf_imune_isenta_consultar` | consultar | ctlancto_sped_ecf_imune_isenta | empresa | ✔ |
| `lancamento_referencial_ecf_imune_isenta_totais` | totais | ctlancto_sped_ecf_imune_isenta | empresa | ✔ |

## `plano_referencial_ecf_consultar`

Plano de contas referencial SPED ECF (Geral) — tabela ctcontas_sped_ecf_geral (módulo referencial, ~1.133 linhas).
O QUE É: Plano referencial da Receita para a ECF (1.133 contas), com vigência e regime de utilização. Tabela global.
COMENTÁRIO DO BANCO SOBRE A TABELA: Plano de contas SPED ECF Geral
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
Tabela global (não depende de empresa): NÃO informe 'empresa'.
FILTROS: codigo, classificacao, descricao, tipo, natureza, utilizacao. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, classificacao, descricao, tipo, nivel, conta_superior, natureza, utilizacao, validade_inicio, validade_fim, layout_inicio, layout_fim. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
REGRAS DE NEGÓCIO (conferidas nos dados): Estrutura (1.133 contas): 985 analíticas (níveis 5 e 6) e 148 sintéticas (níveis 1 a 5). A natureza 4 (Resultado) tem 399 contas, a 1 (Ativo) 474, a 2 (Passivo) 200 e a 3 (PL) 60.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `codigo`: Filtra codigo_cta_sped_ecf_geral (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código)
- `classificacao`: Filtra classificacao_sped_ecf_geral (varchar). Aceita: valor simples (igualdade), igual, {"prefixo":"x"}. (Classificação)
- `descricao`: Filtra descricao (varchar). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}. (Descrição)
- `tipo`: Filtra tipo (char). Aceita: valor simples (igualdade), igual. Códigos: A=Analítica, S=Sintética (Tipo (A = Analítica / S = Sintética))
- `natureza`: Filtra natureza (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Ativo, 2=Passivo, 3=Patrimônio Líquido, 4=Resultado (Natureza (1 - Ativo / 2 - Passivo / 3 - Patrimônio Líquido / 4 - Resultado))
- `utilizacao`: Filtra utilizacao (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Real e Presumido, 2=Somente Real, 3=Somente Presumido [parcialmente confirmado] (UTILIZAÇÃO (1 - REAL/PRESUMIDO / 2 - REAL / 3 - PRESUMIDO))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `plano_referencial_ecf_obter`

Plano de contas referencial SPED ECF (Geral) — obtém UM registro pela chave (codigo_cta_sped_ecf_geral) da tabela ctcontas_sped_ecf_geral. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use plano_referencial_ecf_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `codigo` (obrigatório): Filtra codigo_cta_sped_ecf_geral (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código)

## `conta_referencial_ecf_consultar`

Mapeamento das contas da empresa para o plano ECF Geral — tabela ctcontas_sped_ecf_geral_ref (módulo referencial, ~922.444 linhas).
O QUE É: Liga cada conta contábil da empresa (ctcontas) à conta do plano referencial ECF. Chave completa (empresa, conta, conta ECF): uma conta do livro pode apontar para mais de uma conta ECF (922 pares para 920 contas na empresa 1017).
COMENTÁRIO DO BANCO SOBRE A TABELA: Plano de contas SPED ECF Geral Referencial
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: conta_codigo, conta_referencial_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: conta_codigo, conta_referencial_codigo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): conta_classificacao, conta_nome, conta_referencial_classificacao, conta_referencial_descricao.
EXEMPLO COM DADOS: a empresa 1585 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Empresa 1017: 4.500 contas no plano, 920 com mapeamento ECF (922 pares). Só as contas mapeadas geram partida no lançamento referencial.
UTILIDADE LIMITADA: a tabela expõe só 2 campo(s) (tabela de apoio/ligação); ela NÃO traz o conteúdo que o nome pode sugerir (XML, arquivo, etc.).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `conta_codigo`: Filtra codi_cta (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta contábil)
- `conta_referencial_codigo`: Filtra codigo_cta_sped_ecf_geral (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta SPED ECF)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `conta_referencial_ecf_obter`

Mapeamento das contas da empresa para o plano ECF Geral — obtém UM registro pela chave (codi_emp, codi_cta, codigo_cta_sped_ecf_geral) da tabela ctcontas_sped_ecf_geral_ref. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use conta_referencial_ecf_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `conta_codigo` (obrigatório): Filtra codi_cta (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta contábil)
- `conta_referencial_codigo` (obrigatório): Filtra codigo_cta_sped_ecf_geral (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta SPED ECF)

## `plano_referencial_ecf_imune_isenta_consultar`

Plano de contas referencial SPED ECF - Imunes e Isentas — tabela ctcontas_sped_ecf_imune_isenta (módulo referencial, ~515 linhas).
O QUE É: Plano referencial da ECF para entidades imunes e isentas (515 contas). Tabela global.
COMENTÁRIO DO BANCO SOBRE A TABELA: Plano de contas SPED ECF Imunes e Isentas
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
Tabela global (não depende de empresa): NÃO informe 'empresa'.
FILTROS: codigo, classificacao, descricao, tipo, natureza. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, classificacao, descricao, tipo, nivel, conta_superior, natureza, ordem, validade_inicio, validade_fim. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `codigo`: Filtra codigo_cta_sped_ecf_imune_isenta (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código)
- `classificacao`: Filtra classificacao_sped_ecf_imune_isenta (varchar). Aceita: valor simples (igualdade), igual, {"prefixo":"x"}. (Classificação)
- `descricao`: Filtra descricao (varchar). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}. (Descrição)
- `tipo`: Filtra tipo (char). Aceita: valor simples (igualdade), igual. Códigos: A=Analítica, S=Sintética (Tipo (A = Analítica / S = Sintética))
- `natureza`: Filtra natureza (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Ativo, 2=Passivo, 3=Patrimônio Líquido, 4=Resultado (Natureza (1 - Ativo / 2 - Passivo / 3 - Patrimônio Líquido / 4 - Resultado))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `plano_referencial_ecf_imune_isenta_obter`

Plano de contas referencial SPED ECF - Imunes e Isentas — obtém UM registro pela chave (codigo_cta_sped_ecf_imune_isenta) da tabela ctcontas_sped_ecf_imune_isenta. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use plano_referencial_ecf_imune_isenta_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `codigo` (obrigatório): Filtra codigo_cta_sped_ecf_imune_isenta (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código)

## `conta_referencial_ecf_imune_isenta_consultar`

Mapeamento das contas da empresa para o plano ECF Imunes e Isentas — tabela ctcontas_sped_ecf_imune_isenta_ref (módulo referencial, ~17.511 linhas).
O QUE É: Liga cada conta contábil da empresa ao plano referencial ECF de imunes e isentas (17.511 pares).
COMENTÁRIO DO BANCO SOBRE A TABELA: Plano de contas SPED ECF Imunes e Isentas Referencial
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: conta_codigo, conta_referencial_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: conta_codigo, conta_referencial_codigo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): conta_classificacao, conta_nome, conta_referencial_classificacao, conta_referencial_descricao.
EXEMPLO COM DADOS: a empresa 1530 tem registros nesta tabela (use para testar).
UTILIDADE LIMITADA: a tabela expõe só 2 campo(s) (tabela de apoio/ligação); ela NÃO traz o conteúdo que o nome pode sugerir (XML, arquivo, etc.).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `conta_codigo`: Filtra codi_cta (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta contábil)
- `conta_referencial_codigo`: Filtra codigo_cta_sped_ecf_imune_isenta (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta SPED ECF)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `conta_referencial_ecf_imune_isenta_obter`

Mapeamento das contas da empresa para o plano ECF Imunes e Isentas — obtém UM registro pela chave (codi_emp, codi_cta, codigo_cta_sped_ecf_imune_isenta) da tabela ctcontas_sped_ecf_imune_isenta_ref. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use conta_referencial_ecf_imune_isenta_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `conta_codigo` (obrigatório): Filtra codi_cta (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta contábil)
- `conta_referencial_codigo` (obrigatório): Filtra codigo_cta_sped_ecf_imune_isenta (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta SPED ECF)

## `plano_referencial_srf_consultar`

Plano de contas referencial SRF — tabela ctcontas_srf (módulo referencial, ~809 linhas).
O QUE É: Plano referencial da Receita Federal (809 contas) usado no lançamento referencial SRF. Tabela global.
COMENTÁRIO DO BANCO SOBRE A TABELA: Plano de contas SRF
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
Tabela global (não depende de empresa): NÃO informe 'empresa'.
FILTROS: codigo, classificacao, descricao, utilizacao, tipo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, classificacao, descricao, utilizacao, tipo, validade_inicio, validade_fim. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
REGRAS DE NEGÓCIO (conferidas nos dados): Utilização x tipo: A/A 589, A/S 109, F/A 44, F/S 12, S/A 45, S/S 10 (total 809). A coluna `natureza_srf` indica analítica/sintética, não ativo/passivo.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `codigo`: Filtra codigo_cta_srf (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `classificacao`: Filtra classificacao_srf (varchar). Aceita: valor simples (igualdade), igual, {"prefixo":"x"}. (Classificacao)
- `descricao`: Filtra descricao_srf (varchar). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}. (Descricao)
- `utilizacao`: Filtra utilizacao_srf (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: F=Fiscal, S=Societária, A=Ambas (Utilização (F=Fiscal / S=Societária / A=Ambas))
- `tipo`: Filtra natureza_srf (char). Aceita: valor simples (igualdade), igual. Códigos: S=Sintética, A=Analítica (Natureza (S=Sintética / A=Analítica))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `plano_referencial_srf_obter`

Plano de contas referencial SRF — obtém UM registro pela chave (codigo_cta_srf) da tabela ctcontas_srf. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use plano_referencial_srf_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `codigo` (obrigatório): Filtra codigo_cta_srf (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `conta_referencial_srf_consultar`

Mapeamento das contas da empresa para o plano SRF — tabela ctcontas_srf_ref (módulo referencial, ~635.418 linhas).
O QUE É: Liga cada conta contábil da empresa ao plano referencial SRF (635.418 pares).
COMENTÁRIO DO BANCO SOBRE A TABELA: Plano de contas SRF Referencial
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: conta_codigo, conta_referencial_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: conta_codigo, conta_referencial_codigo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): conta_classificacao, conta_nome, conta_referencial_classificacao, conta_referencial_descricao.
EXEMPLO COM DADOS: a empresa 654 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Empresa 596: 5.260 contas no plano, 515 com mapeamento SRF (539 pares).
UTILIDADE LIMITADA: a tabela expõe só 2 campo(s) (tabela de apoio/ligação); ela NÃO traz o conteúdo que o nome pode sugerir (XML, arquivo, etc.).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `conta_codigo`: Filtra codi_cta (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta contabil)
- `conta_referencial_codigo`: Filtra codigo_cta_srf (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta SRF)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `conta_referencial_srf_obter`

Mapeamento das contas da empresa para o plano SRF — obtém UM registro pela chave (codi_emp, codi_cta, codigo_cta_srf) da tabela ctcontas_srf_ref. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use conta_referencial_srf_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `conta_codigo` (obrigatório): Filtra codi_cta (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta contabil)
- `conta_referencial_codigo` (obrigatório): Filtra codigo_cta_srf (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta SRF)

## `lancamento_referencial_srf_consultar`

Lançamentos referenciais SRF — tabela ctlancto_referencial_srf (módulo referencial, ~1.152.027 linhas).
O QUE É: Partidas do livro diário no plano referencial SRF (1,15 milhão de linhas, 573 empresas). Mesma estrutura do ECF, porém só existe partida para contas que têm mapeamento SRF, então muitos lançamentos têm uma só perna.
COMENTÁRIO DO BANCO SOBRE A TABELA: Lancamento Referencial SRF
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): lancamento_numero, lote_codigo, periodo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna lancamento.data_lan. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: lancamento_numero, lote_codigo, conta_debito, conta_credito, valor. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: lancamento_numero, sequencial, lote_codigo, valor, conta_debito, conta_credito, origem_registro. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): lancamento_data, lancamento_valor, lancamento_conta_debito, lancamento_conta_credito, conta_debito_classificacao, conta_debito_descricao, conta_credito_classificacao, conta_credito_descricao.
EXEMPLO COM DADOS: a empresa 560 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Cada linha é uma perna (débito OU crédito). Empresa 596 (55.423 linhas, 52.961 lançamentos): 52.275 pernas de débito e 3.148 de crédito; 50.499 lançamentos têm 1 linha e 2.462 têm 2. A perna só existe se a conta do livro tem mapeamento SRF (52.961 de 54.974 lançamentos do livro têm linha referencial). | Conciliação (empresa 596): a soma das pernas de débito é igual a ctlancto.vlor_lan em 52.238 de 52.961 lançamentos e a das pernas de crédito em 3.111. | Integridade: 0 contas fora do plano SRF, 0 lançamentos órfãos e 0 lotes órfãos; origem_registro é sempre 0.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `lancamento_numero`: Filtra nume_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Número do lançamento)
- `lote_codigo`: Filtra codi_lote (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Lançamento em lote)
- `conta_debito`: Filtra conta_debito (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta Débito)
- `conta_credito`: Filtra conta_credito (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta Crédito)
- `valor`: Filtra valor (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Valor)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `lancamento_referencial_srf_totais`

Lançamentos referenciais SRF — TOTAIS por grupo da tabela ctlancto_referencial_srf (módulo referencial). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): lancamento_numero, lote_codigo, periodo. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna lancamento.data_lan. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor. CAMPOS PARA AGRUPAR: lancamento_numero, sequencial, lote_codigo, conta_debito, conta_credito, origem_registro. Os filtros são os mesmos de lancamento_referencial_srf_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (origem_registro) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Cada linha é uma perna (débito OU crédito). Empresa 596 (55.423 linhas, 52.961 lançamentos): 52.275 pernas de débito e 3.148 de crédito; 50.499 lançamentos têm 1 linha e 2.462 têm 2. A perna só existe se a conta do livro tem mapeamento SRF (52.961 de 54.974 lançamentos do livro têm linha referencial). | Conciliação (empresa 596): a soma das pernas de débito é igual a ctlancto.vlor_lan em 52.238 de 52.961 lançamentos e a das pernas de crédito em 3.111. | Integridade: 0 contas fora do plano SRF, 0 lançamentos órfãos e 0 lotes órfãos; origem_registro é sempre 0.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `lancamento_numero`: Filtra nume_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Número do lançamento)
- `lote_codigo`: Filtra codi_lote (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Lançamento em lote)
- `conta_debito`: Filtra conta_debito (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta Débito)
- `conta_credito`: Filtra conta_credito (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta Crédito)
- `valor`: Filtra valor (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Valor)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["origem_registro"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `lancamento_scp_consultar`

Lançamentos de SCP (Sociedade em Conta de Participação) — tabela ctlancto_scp (módulo referencial, ~2.742 linhas).
O QUE É: Marca os lançamentos do livro que pertencem a uma SCP: um registro por lançamento e lado (débito ou crédito), com o código do SCP e a empresa do SCP. 2.742 linhas, 6 empresas, 11 SCPs.
COMENTÁRIO DO BANCO SOBRE A TABELA: Lancamento SCP
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna lancamento.data_lan. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: lancamento_numero, tipo, scp_codigo, lote_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: lancamento_numero, tipo, lote_codigo, empresa_scp, scp_codigo, origem_registro. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): lancamento_data, lancamento_valor, lancamento_conta_debito, lancamento_conta_credito.
EXEMPLO COM DADOS: a empresa 749 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Distribuição: 1.374 registros de débito e 1.298 de crédito de origem 0 (6 empresas, 11 SCPs) e 35 de cada lado de origem 2 (1 empresa, 1 SCP).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `lancamento_numero`: Filtra nume_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Número do lançamento)
- `tipo`: Filtra tipo (char). Aceita: valor simples (igualdade), igual. Códigos: D=Débito, C=Crédito (Tipo (D=Débito/ C=Crédito))
- `scp_codigo`: Filtra i_scp (integer). Aceita: valor simples (igualdade), igual, lista de valores. (SCP)
- `lote_codigo`: Filtra codi_lote (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Número do lote)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `lancamento_scp_obter`

Lançamentos de SCP (Sociedade em Conta de Participação) — obtém UM registro pela chave (codi_emp, nume_lan, tipo) da tabela ctlancto_scp. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use lancamento_scp_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `lancamento_numero` (obrigatório): Filtra nume_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Número do lançamento)
- `tipo` (obrigatório): Filtra tipo (char). Aceita: valor simples (igualdade), igual. Códigos: D=Débito, C=Crédito (Tipo (D=Débito/ C=Crédito))

## `lancamento_referencial_ecf_consultar`

Lançamentos referenciais SPED ECF (Geral) — tabela ctlancto_sped_ecf_geral (módulo referencial, ~21.735.224 linhas).
O QUE É: Partidas do livro diário traduzidas para o plano referencial ECF Geral: cada linha é UMA perna do lançamento (débito OU crédito; a outra conta vale 0), identificada por (lançamento, sequencial). 21,7 milhões de linhas em 754 empresas.
COMENTÁRIO DO BANCO SOBRE A TABELA: Lancamento Referencial SPED ECF Geral
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): lancamento_numero, lote_codigo, periodo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna lancamento.data_lan. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: lancamento_numero, lote_codigo, conta_debito, conta_credito, valor. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: lancamento_numero, sequencial, lote_codigo, valor, conta_debito, conta_credito, origem_registro. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): lancamento_data, lancamento_valor, lancamento_conta_debito, lancamento_conta_credito, conta_debito_classificacao, conta_debito_descricao, conta_credito_classificacao, conta_credito_descricao.
EXEMPLO COM DADOS: a empresa 266 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Cada linha é uma perna: na empresa 1017 todas as 1.158.926 linhas têm só o débito (579.198) ou só o crédito (579.728) preenchido; valor nunca é 0. Um lançamento tem 2 linhas (578.660) ou 1 (1.606). | Conciliação com o livro (empresa 1017, 580.266 lançamentos): a soma das pernas de débito é igual a ctlancto.vlor_lan em 579.198 e a das pernas de crédito em 579.728; todo lançamento do livro tem linha referencial. Não some `valor` direto como se fosse o valor do lançamento: soma as duas pernas, o dobro. | Conta referencial = conta do livro mapeada em conta_referencial_ecf: em 100% das pernas de débito (579.198) a conta do livro (cdeb_lan) tem o par (conta, conta_debito) no mapeamento. | Integridade: 0 contas fora do plano referencial, 0 lançamentos órfãos, 0 lotes órfãos, e codi_lote igual ao do lançamento em 100%.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `lancamento_numero`: Filtra nume_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Número do lançamento)
- `lote_codigo`: Filtra codi_lote (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Lançamento em lote)
- `conta_debito`: Filtra conta_debito (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta Débito)
- `conta_credito`: Filtra conta_credito (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta Crédito)
- `valor`: Filtra valor (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Valor)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `lancamento_referencial_ecf_totais`

Lançamentos referenciais SPED ECF (Geral) — TOTAIS por grupo da tabela ctlancto_sped_ecf_geral (módulo referencial). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): lancamento_numero, lote_codigo, periodo. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna lancamento.data_lan. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor. CAMPOS PARA AGRUPAR: lancamento_numero, sequencial, lote_codigo, conta_debito, conta_credito, origem_registro. Os filtros são os mesmos de lancamento_referencial_ecf_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (origem_registro) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Cada linha é uma perna: na empresa 1017 todas as 1.158.926 linhas têm só o débito (579.198) ou só o crédito (579.728) preenchido; valor nunca é 0. Um lançamento tem 2 linhas (578.660) ou 1 (1.606). | Conciliação com o livro (empresa 1017, 580.266 lançamentos): a soma das pernas de débito é igual a ctlancto.vlor_lan em 579.198 e a das pernas de crédito em 579.728; todo lançamento do livro tem linha referencial. Não some `valor` direto como se fosse o valor do lançamento: soma as duas pernas, o dobro. | Conta referencial = conta do livro mapeada em conta_referencial_ecf: em 100% das pernas de débito (579.198) a conta do livro (cdeb_lan) tem o par (conta, conta_debito) no mapeamento. | Integridade: 0 contas fora do plano referencial, 0 lançamentos órfãos, 0 lotes órfãos, e codi_lote igual ao do lançamento em 100%.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `lancamento_numero`: Filtra nume_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Número do lançamento)
- `lote_codigo`: Filtra codi_lote (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Lançamento em lote)
- `conta_debito`: Filtra conta_debito (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta Débito)
- `conta_credito`: Filtra conta_credito (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta Crédito)
- `valor`: Filtra valor (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Valor)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["origem_registro"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `lancamento_referencial_ecf_imune_isenta_consultar`

Lançamentos referenciais SPED ECF - Imunes e Isentas — tabela ctlancto_sped_ecf_imune_isenta (módulo referencial, ~469.590 linhas).
O QUE É: Partidas do livro diário no plano referencial ECF de imunes e isentas (469.590 linhas, 32 empresas). Mesma estrutura do ECF Geral.
COMENTÁRIO DO BANCO SOBRE A TABELA: Lançamento Referencial SPED ECF Imunes e Isentas
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): lancamento_numero, lote_codigo, periodo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna lancamento.data_lan. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: lancamento_numero, lote_codigo, conta_debito, conta_credito, valor. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: lancamento_numero, sequencial, lote_codigo, valor, conta_debito, conta_credito, origem_registro. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): lancamento_data, lancamento_valor, lancamento_conta_debito, lancamento_conta_credito, conta_debito_classificacao, conta_debito_descricao, conta_credito_classificacao, conta_credito_descricao.
EXEMPLO COM DADOS: a empresa 1432 tem registros nesta tabela (use para testar).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `lancamento_numero`: Filtra nume_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Número do lançamento)
- `lote_codigo`: Filtra codi_lote (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Lançamento em lote)
- `conta_debito`: Filtra conta_debito (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta Débito)
- `conta_credito`: Filtra conta_credito (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta Crédito)
- `valor`: Filtra valor (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Valor)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `lancamento_referencial_ecf_imune_isenta_totais`

Lançamentos referenciais SPED ECF - Imunes e Isentas — TOTAIS por grupo da tabela ctlancto_sped_ecf_imune_isenta (módulo referencial). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): lancamento_numero, lote_codigo, periodo. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna lancamento.data_lan. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor. CAMPOS PARA AGRUPAR: lancamento_numero, sequencial, lote_codigo, conta_debito, conta_credito, origem_registro. Os filtros são os mesmos de lancamento_referencial_ecf_imune_isenta_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (origem_registro) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `lancamento_numero`: Filtra nume_lan (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Número do lançamento)
- `lote_codigo`: Filtra codi_lote (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Lançamento em lote)
- `conta_debito`: Filtra conta_debito (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta Débito)
- `conta_credito`: Filtra conta_credito (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta Crédito)
- `valor`: Filtra valor (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Valor)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["origem_registro"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).
