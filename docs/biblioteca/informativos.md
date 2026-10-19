# Módulo `informativos`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `informativo_consultar` | consultar | efinformativos | — | ✔ |
| `informativo_obter` | obter | efinformativos | codigo | ✔ |
| `informativo_empresa_consultar` | consultar | efoutrosdados | empresa | ✔ |
| `informativo_empresa_obter` | obter | efoutrosdados | empresa, competencia, informativo_codigo | ✔ |
| `dado_informativo_consultar` | consultar | efoutrosdados_dados | empresa | ✔ |
| `dado_informativo_obter` | obter | efoutrosdados_dados | empresa, competencia, informativo_codigo, campo | ✔ |

## `informativo_consultar`

Catálogo de informativos (obrigações acessórias) — tabela efinformativos (módulo informativos, ~82 linhas).
O QUE É: Os 82 informativos que a Domínio trata, de DIPJ/DASN/DEFIS (um por ano) a guias estaduais (GIA, DIEF, GIM...), DCTF, DIRF, DMED, SPED, EFD-Reinf, MIT, DIRBI e DeRE. Tabela global.
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
Tabela global (não depende de empresa): NÃO informe 'empresa'.
FILTROS: codigo, descricao. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, descricao. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
REGRAS DE NEGÓCIO (conferidas nos dados): 82 informativos. Códigos de uso mais frequente: 35 (SPED PIS e COFINS), 36 (DCTF), 62 e 65 (EFD-Reinf e Reinf eventos), 32 (DIRF após 2009), 77 (MIT), 78 e 80 (DEFIS 2025 e 2026).
UTILIDADE LIMITADA: a tabela expõe só 2 campo(s) (tabela de apoio/ligação); ela NÃO traz o conteúdo que o nome pode sugerir (XML, arquivo, etc.).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `codigo`: Filtra i_informativos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `descricao`: Filtra descricao (varchar). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Descricao)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `informativo_obter`

Catálogo de informativos (obrigações acessórias) — obtém UM registro pela chave (i_informativos) da tabela efinformativos. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use informativo_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `codigo` (obrigatório): Filtra i_informativos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `informativo_empresa_consultar`

Informativos preparados por empresa e competência — tabela efoutrosdados (módulo informativos, ~83.235 linhas).
O QUE É: Marca que existe "outros dados" para um informativo numa competência de uma empresa: ou seja, a obrigação foi preparada ali. Para informativos anuais (DEFIS, DIRF, DMED) a competência é 1º de janeiro do ano de referência. 83.391 linhas, 1.911 empresas. Os campos informados ficam em dado_informativo.
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna competencia. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: competencia, informativo_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: competencia, informativo_codigo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): informativo_descricao.
EXEMPLO COM DADOS: a empresa 1723 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Por informativo (cabeçalhos): 35 SPED PIS/COFINS 29.100 (868 empresas) · 36 DCTF 17.730 (709) · 62 EFD-Reinf 16.004 (883) · 65 Reinf eventos 7.219 (667) · 77 MIT 5.266 (679, de 2020-09 a 2026-09) · 32 DIRF 5.180 (1.740) · 78 DEFIS 2025 582 (196) · 80 DEFIS 2026 432 (235). | Dado suspeito: 9 cabeçalhos têm ano impossível na competência (digitação): informativo 35 com anos 20 a 2240 (7 empresas) e informativo 62 com anos 3202 e 5025 (2 empresas). Filtre a competência entre 2000 e a data atual. | Integridade: todo campo (dado_informativo) tem o cabeçalho correspondente (0 sem cabeçalho em 3.842.053) e só 1 cabeçalho não tem campos.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
UTILIDADE LIMITADA: a tabela expõe só 2 campo(s) (tabela de apoio/ligação); ela NÃO traz o conteúdo que o nome pode sugerir (XML, arquivo, etc.).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `competencia`: Filtra competencia (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia) Datas no formato AAAA-MM-DD.
- `informativo_codigo`: Filtra i_informativos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Informativo)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `informativo_empresa_obter`

Informativos preparados por empresa e competência — obtém UM registro pela chave (codi_emp, competencia, i_informativos) da tabela efoutrosdados. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use informativo_empresa_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `competencia` (obrigatório): Filtra competencia (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia) Datas no formato AAAA-MM-DD.
- `informativo_codigo` (obrigatório): Filtra i_informativos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Informativo)

## `dado_informativo_consultar`

Campos informados em cada informativo (campo/valor) — tabela efoutrosdados_dados (módulo informativos, ~3.842.053 linhas).
O QUE É: Os parâmetros e respostas que o escritório informa para gerar cada obrigação, como pares campo/valor por empresa, competência e informativo (retificadora, número do recibo, regime, qualificação, opções...). 3,84 milhões de linhas; o informativo 35 (SPED PIS/COFINS) tem 2,9 milhões. O valor é sempre texto: o `tipo` diz como interpretá-lo (ver domínio). Alguns campos têm dado pessoal (CPF e nome do inventariante da DIRF, CNPJ do responsável).
COMENTÁRIO DO BANCO SOBRE A TABELA: Outros dados - Dados
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): informativo_codigo, periodo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna competencia. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: competencia, informativo_codigo, campo, tipo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: competencia, informativo_codigo, campo, tipo, valor. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): informativo_descricao.
EXEMPLO COM DADOS: a empresa 458 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Volume por informativo: 35 SPED PIS/COFINS 2.909.913 linhas (100 campos distintos) · 36 DCTF 383.650 (22) · 62 EFD-Reinf 201.167 (13) · 32 DIRF 138.911 (27) · 65 Reinf eventos 122.234 (18) · 77 MIT 47.061 (24). | Tipo: 1 em 2.965.178 campos (481.742 com valor vazio), 3 em 658.888, 4 em 169.850 e 2 em 49.921 (47.429 vazios); tipos 3 e 4 nunca têm valor vazio. | Campos de controle comuns: `retificadora`, `numero_recibo`, `situacao_especial`, `regime`, `evento`, `qualificacao`. Na DCTF (36) campos como retificadora, numero_recibo, regime, evento e qualificacao aparecem em todos os 17.730 cabeçalhos; no MIT (77) aparecem data_evento e situacao_especial em 5.266 e evento, qualificacao_pj, […]
PRIVACIDADE: Alguns valores contêm CPF, nome ou CNPJ (inventariante da DIRF, responsáveis).
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): valor
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `competencia`: Filtra competencia (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia) Datas no formato AAAA-MM-DD.
- `informativo_codigo`: Filtra i_informativos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Informativo)
- `campo`: Filtra campo (varchar). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Campo)
- `tipo`: Filtra tipo (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Indicador ou texto curto (por observação), 2=Data (por observação), 3=Opção ou código (por observação), 4=Valor ou texto longo (por observação) [parcialmente confirmado] (Tipo)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `dado_informativo_obter`

Campos informados em cada informativo (campo/valor) — obtém UM registro pela chave (codi_emp, competencia, i_informativos, campo) da tabela efoutrosdados_dados. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use dado_informativo_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `competencia` (obrigatório): Filtra competencia (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia) Datas no formato AAAA-MM-DD.
- `informativo_codigo` (obrigatório): Filtra i_informativos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Informativo)
- `campo` (obrigatório): Filtra campo (varchar). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Campo)
