# Módulo `geral`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `atividade_secundaria_consultar` | consultar | geatvsecundaria | empresa | ✔ |
| `atividade_secundaria_obter` | obter | geatvsecundaria | empresa, cnae | ✔ |
| `cnae_consultar` | consultar | gecnae20 | — | ✔ |
| `cnae_obter` | obter | gecnae20 | codigo | ✔ |
| `estado_consultar` | consultar | geestado | — | ✔ |
| `feriado_consultar` | consultar | geferiados | — | ✔ |
| `imposto_vigencia_consultar` | consultar | geimposto_vigencia | empresa | ✔ |
| `imposto_vigencia_totais` | totais | geimposto_vigencia | empresa | ✔ |
| `municipio_consultar` | consultar | gemunicipio | — | ✔ |
| `municipio_obter` | obter | gemunicipio | codigo | ✔ |
| `natureza_juridica_consultar` | consultar | genatjuridica | — | ✔ |
| `natureza_juridica_obter` | obter | genatjuridica | codigo | ✔ |
| `pais_consultar` | consultar | gepais | — | ✔ |
| `quadro_societario_consultar` | consultar | gequadrosocietario | empresa | ✔ |
| `quadro_societario_obter` | obter | gequadrosocietario | empresa, data | ✔ |
| `participante_societario_consultar` | consultar | gequadrosocietario_socios | empresa | ✔ |
| `participante_societario_obter` | obter | gequadrosocietario_socios | empresa, data, socio_codigo, tipo | ✔ |
| `socio_consultar` | consultar | gesocios | — | ✔ |
| `socio_obter` | obter | gesocios | codigo | ✔ |

## `atividade_secundaria_consultar`

Atividades secundárias (CNAE) da empresa — tabela geatvsecundaria (módulo geral, ~3.952 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: Empresa - Cadastro - Atividades secundarias
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: cnae. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: cnae, ordem, usa_cnae20. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): cnae_descricao.
EXEMPLO COM DADOS: a empresa 867 tem registros nesta tabela (use para testar).
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `cnae`: Filtra codigo_cnae (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Codigo CNAE)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `atividade_secundaria_obter`

Atividades secundárias (CNAE) da empresa — obtém UM registro pela chave (codigo_cnae, codi_emp) da tabela geatvsecundaria. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use atividade_secundaria_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `cnae` (obrigatório): Filtra codigo_cnae (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Codigo CNAE)

## `cnae_consultar`

CNAE 2.0 — tabela gecnae20 (módulo geral, ~1.350 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: Tabela do CNAE 20
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
Tabela global (não depende de empresa): NÃO informe 'empresa'.
FILTROS: codigo, descricao. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, descricao. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
UTILIDADE LIMITADA: a tabela expõe só 2 campo(s) (tabela de apoio/ligação); ela NÃO traz o conteúdo que o nome pode sugerir (XML, arquivo, etc.).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `codigo`: Filtra i_cnae20 (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Codigo CNAE 20)
- `descricao`: Filtra descricao (varchar). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}. (Descricao)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `cnae_obter`

CNAE 2.0 — obtém UM registro pela chave (i_cnae20) da tabela gecnae20. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use cnae_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `codigo` (obrigatório): Filtra i_cnae20 (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Codigo CNAE 20)

## `estado_consultar`

Estados (UF) — tabela geestado (módulo geral, ~28 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: Cadastro de estados
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
Tabela global (não depende de empresa): NÃO informe 'empresa'.
FILTROS: sigla. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, nome, sigla, regiao, aliquota_icms. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `sigla`: Filtra sigla_uf (char). Aceita: valor simples (igualdade), igual, lista de valores. (Sigla do estado)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `feriado_consultar`

Feriados — tabela geferiados (módulo geral, ~106 linhas).
O QUE É: Feriados federais, estaduais, municipais e sindicais usados nos cálculos e vencimentos. Fixos têm dia/mês; móveis têm ano.
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
Tabela global (não depende de empresa): NÃO informe 'empresa'.
FILTROS: abrangencia, mes, uf_codigo, municipio_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, descricao, abrangencia, tipo, dia, mes, ano, municipio_codigo, uf_codigo, sindicato_codigo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `abrangencia`: Filtra abrangencia (tinyint). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Federal, 2=Estadual, 3=Municipal, 4=Sindical (Abrangência: (1=Federal/2=Estadual/3=Municipal/4=Sindical))
- `mes`: Filtra mes (tinyint). Aceita: valor simples (igualdade), igual, lista de valores. (mes)
- `uf_codigo`: Filtra codigo_uf (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo do estado para feriado estadal)
- `municipio_codigo`: Filtra codigo_municipio (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo sequencial do municipio para feriados municipais)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `imposto_vigencia_consultar`

Configuração de impostos por vigência — tabela GEIMPOSTO_VIGENCIA (módulo geral, ~316.644 linhas).
O QUE É: Como cada empresa apura cada imposto a partir de uma data (vigência): competência (federal/estadual/municipal), periodicidade, forma e dias de vencimento, códigos de recolhimento e contas/históricos contábeis. A configuração em vigor numa data é a de MAIOR `vigencia` menor ou igual a essa data. A tabela tem 367 colunas; só as ~30 de uso geral são expostas.
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): imposto_codigo, periodo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna VIGENCIA_IMP. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: imposto_codigo, vigencia. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: imposto_codigo, vigencia, descricao, competencia, periodicidade, forma_vencimento, dias_vencimento, a_partir_de_meses, aliquota, aliquota_base_calculo, tipo_calculo, codigo_recolhimento, codigo_recolhimento_juros, codigo_recolhimento_multa, codigo_recolhimento_atualizacao, conta_imposto_a_recolher, historico_imposto_a_recolher, conta_imposto_a_recuperar, historico_imposto_a_recuperar, conta_imposto_sobre_vendas, conta_imposto_sobre_compras, gera_lancamento_contabil_por_nota. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): imposto_nome, imposto_sigla.
EXEMPLO COM DADOS: a empresa 873 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): ATENÇÃO: periodicidade_imposto (1 mensal, 2 quinzenal, 3 decendial, 4 trimestral, 5 semanal, 6 semestral) usa codificação DIFERENTE da periodicidade da apuração em efsdoimp.pdic_sim (6 = mensal, 4/5 = quinzenas, 7 = trimestral...). Não misture. | As contas contábeis (conta_*) são códigos do plano de contas; resolva-os pelo plano da empresa (ver regra do plano em contabil.yaml).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `imposto_codigo`: Filtra CODI_IMP (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `vigencia`: Filtra VIGENCIA_IMP (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `imposto_vigencia_totais`

Configuração de impostos por vigência — TOTAIS por grupo da tabela GEIMPOSTO_VIGENCIA (módulo geral). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): imposto_codigo, periodo. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna VIGENCIA_IMP. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: dias_vencimento, historico_imposto_a_recolher, historico_imposto_a_recuperar. CAMPOS PARA AGRUPAR: imposto_codigo, vigencia:mes, descricao, competencia, periodicidade, forma_vencimento, a_partir_de_meses, aliquota, aliquota_base_calculo, tipo_calculo, codigo_recolhimento, codigo_recolhimento_juros, codigo_recolhimento_multa, codigo_recolhimento_atualizacao, conta_imposto_a_recolher, conta_imposto_a_recuperar, conta_imposto_sobre_vendas, conta_imposto_sobre_compras, gera_lancamento_contabil_por_nota. Os filtros são os mesmos de imposto_vigencia_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (competencia, periodicidade, forma_vencimento, tipo_calculo) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: ATENÇÃO: periodicidade_imposto (1 mensal, 2 quinzenal, 3 decendial, 4 trimestral, 5 semanal, 6 semestral) usa codificação DIFERENTE da periodicidade da apuração em efsdoimp.pdic_sim (6 = mensal, 4/5 = quinzenas, 7 = trimestral...). Não misture. | As contas contábeis (conta_*) são códigos do plano de contas; resolva-os pelo plano da empresa (ver regra do plano em contabil.yaml).. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `imposto_codigo`: Filtra CODI_IMP (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `vigencia`: Filtra VIGENCIA_IMP (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["vigencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["dias_vencimento"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `municipio_consultar`

Municípios — tabela gemunicipio (módulo geral, ~5.576 linhas).
O QUE É: Tabela global de municípios. `codigo` é um código INTERNO sequencial da Domínio (1 a 5.576), NÃO o código IBGE (que está em `ibge`). As demais colunas de código (SRF, ANP, NFS-e...) servem a integrações específicas.
COMENTÁRIO DO BANCO SOBRE A TABELA: Cadastro de municipios
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
Tabela global (não depende de empresa): NÃO informe 'empresa'.
FILTROS: codigo, nome, ibge, uf_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, nome, nome_acentuado, uf_codigo, ibge, srf, srf_2016, codigo_estadual. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): uf, uf_nome.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `codigo`: Filtra codigo_municipio (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo sequencial)
- `nome`: Filtra nome_municipio (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Nome do municipio)
- `ibge`: Filtra codigo_ibge (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo do IBGE/RAIS)
- `uf_codigo`: Filtra codigo_uf (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo do estado)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `municipio_obter`

Municípios — obtém UM registro pela chave (codigo_municipio) da tabela gemunicipio. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use municipio_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `codigo` (obrigatório): Filtra codigo_municipio (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo sequencial)

## `natureza_juridica_consultar`

Naturezas jurídicas — tabela genatjuridica (módulo geral, ~96 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: Natureza juridica
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
Tabela global (não depende de empresa): NÃO informe 'empresa'.
FILTROS: codigo, descricao. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, descricao, tipo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `codigo`: Filtra codigo (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `descricao`: Filtra descricao (varchar). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}. (Descricao)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `natureza_juridica_obter`

Naturezas jurídicas — obtém UM registro pela chave (codigo) da tabela genatjuridica. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use natureza_juridica_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `codigo` (obrigatório): Filtra codigo (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `pais_consultar`

Países — tabela gepais (módulo geral, ~273 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: Cadastro de paises
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
Tabela global (não depende de empresa): NÃO informe 'empresa'.
FILTROS: nome, sigla_iso. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, nome, codigo_bacen, codigo_siscomex, sigla_iso, codigo_iso, codigo_reinf. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `nome`: Filtra nome_pais (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Nome do pais)
- `sigla_iso`: Filtra SIGLA_ISO (char). Aceita: valor simples (igualdade), igual. (Sigla padrão ISO de 2 letras.)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `quadro_societario_consultar`

Quadros societários (histórico) — tabela gequadrosocietario (módulo geral, ~1.571 linhas).
O QUE É: Uma linha por empresa e data de alteração: capital social e quotas. O quadro vigente é o de maior `data`. 988 empresas têm 1 quadro; as demais têm histórico (até 6).
COMENTÁRIO DO BANCO SOBRE A TABELA: Empresa - Cadastro - Quadro Societario
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna data. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: data. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: data, quotas, capital_social, capital_a_integralizar, quotas_integralizadas, quotas_a_integralizar, capital_integralizado, quotas_em_tesouraria_percentual, liberado_registro. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 675 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Coerência com os participantes: a soma da participação dos sócios (tipo S) é 100% em 1.474 de 1.486 quadros (99,2%; 12 abaixo, 0 acima) e a soma das quotas dos sócios é igual às quotas do quadro em 1.472 (99,1%).
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): capital_social, capital_a_integralizar, capital_integralizado
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `data`: Filtra data (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data) Datas no formato AAAA-MM-DD.
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `quadro_societario_obter`

Quadros societários (histórico) — obtém UM registro pela chave (codi_emp, data) da tabela gequadrosocietario. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use quadro_societario_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `data` (obrigatório): Filtra data (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data) Datas no formato AAAA-MM-DD.

## `participante_societario_consultar`

Participantes do quadro societário — tabela gequadrosocietario_socios (módulo geral, ~4.980 linhas).
O QUE É: Sócios, administradores e demais participantes de cada quadro, com quotas e participação percentual.
COMENTÁRIO DO BANCO SOBRE A TABELA: Empresa - Cadastro - Quadro Societario - Socios
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna data. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: data, socio_codigo, tipo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: data, socio_codigo, tipo, quotas, quotas_a_integralizar, participacao_percentual, condicao, cargo, data_ingresso, data_saida, exerce_atividade. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): socio_nome.
EXEMPLO COM DADOS: a empresa 305 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Para o quadro de uma data some só tipo = 'S' ao conferir 100%. O tipo 'E' (64 linhas) é desconhecido; não o some como sócio. | Todos os participantes têm cadastro em gesocios (0 sem cadastro em 4.980).
PRIVACIDADE: Liga pessoa física a empresa e percentual de participação. Mascarar nome por padrão.
POSSÍVEIS DADOS PESSOAIS/FINANCEIROS (os dados saem em claro; devolva só o que a pergunta exigir): socio_nome.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `data`: Filtra data (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data) Datas no formato AAAA-MM-DD.
- `socio_codigo`: Filtra i_socio (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo sequencial)
- `tipo`: Filtra tipo (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: S=Sócio, A=Administrador, R=Representante legal, E=Desconhecido (64 linhas, não documentado) [parcialmente confirmado] (Tipo (S - Socio/A - Administrador/R - Representante Legal))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `participante_societario_obter`

Participantes do quadro societário — obtém UM registro pela chave (codi_emp, data, i_socio, tipo) da tabela gequadrosocietario_socios. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use participante_societario_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `data` (obrigatório): Filtra data (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data) Datas no formato AAAA-MM-DD.
- `socio_codigo` (obrigatório): Filtra i_socio (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo sequencial)
- `tipo` (obrigatório): Filtra tipo (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: S=Sócio, A=Administrador, R=Representante legal, E=Desconhecido (64 linhas, não documentado) [parcialmente confirmado] (Tipo (S - Socio/A - Administrador/R - Representante Legal))

## `socio_consultar`

Sócios (cadastro mínimo) — tabela gesocios (módulo geral, ~2.316 linhas).
O QUE É: Cadastro GLOBAL de pessoas sócias (não depende de empresa; 412 de 2.125 aparecem em mais de uma empresa). Somente identificação mínima.
COMENTÁRIO DO BANCO SOBRE A TABELA: Socios - Cadastro
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
Tabela global (não depende de empresa): NÃO informe 'empresa'.
FILTROS: codigo, nome, inscricao. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, nome, sexo, tipo_inscricao, inscricao, uf. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
PRIVACIDADE: Pessoa física identificada (nome e CPF). Os dados saem em claro nesta versão do servidor: devolva só o que a pergunta exigir.
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): nome, inscricao
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `codigo`: Filtra i_socio (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo socio)
- `nome`: Filtra nome (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Nome)
- `inscricao`: Filtra inscricao (char). Aceita: valor simples (igualdade), igual. (CPF ou CNPJ)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `socio_obter`

Sócios (cadastro mínimo) — obtém UM registro pela chave (i_socio) da tabela gesocios. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use socio_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `codigo` (obrigatório): Filtra i_socio (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo socio)
