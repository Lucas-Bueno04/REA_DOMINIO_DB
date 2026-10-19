# Módulo `folha_calculo`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `cadastro_base_calculo_folha_consultar` | consultar | focadbases | — | ✔ |
| `cadastro_base_calculo_folha_obter` | obter | focadbases | base_codigo | ✔ |
| `calculo_base_folha_consultar` | consultar | focalculosbases | — | ✔ |
| `calculo_base_folha_totais` | totais | focalculosbases | — | ✔ |
| `incidencia_evento_folha_consultar` | consultar | foeventosbases | empresa | ✔ |
| `incidencia_evento_folha_obter` | obter | foeventosbases | empresa, evento_codigo, base_codigo | ✔ |

## `cadastro_base_calculo_folha_consultar`

Cadastro de bases de cálculo da folha — tabela focadbases (módulo folha_calculo, ~270 linhas).
O QUE É: Os 270 tipos de base que o cálculo da folha usa (INSS Mensal, FGTS Mensal, INSS Férias, INSS empresa, terço de férias por rubrica, empréstimos...). 164 têm código negativo (bases internas do sistema) e 106 positivo. As fórmulas não são expostas. Tabela global.
COMENTÁRIO DO BANCO SOBRE A TABELA: Cadastro - Bases de calculo
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
Tabela global (não depende de empresa): NÃO informe 'empresa'.
FILTROS: base_codigo, descricao. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: base_codigo, descricao, tipo_base, ordem. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
REGRAS DE NEGÓCIO (conferidas nos dados): 270 bases: 164 internas (código negativo) e 106 de código positivo; as mais usadas nos cálculos de 2026 são 9 (INSS Mensal), -86 (INSS Empresa sem desoneração), 15 (FGTS Mensal), -6/-8/-7 (partes do INSS da empresa) e 10/16 (INSS e FGTS de férias).
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `base_codigo`: Filtra i_cadbases (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"gte":v}, {"lte":v}. (Codigo do cadastro da base)
- `descricao`: Filtra descricao (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Descricao)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `cadastro_base_calculo_folha_obter`

Cadastro de bases de cálculo da folha — obtém UM registro pela chave (i_cadbases) da tabela focadbases. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use cadastro_base_calculo_folha_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `base_codigo` (obrigatório): Filtra i_cadbases (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"gte":v}, {"lte":v}. (Codigo do cadastro da base)

## `calculo_base_folha_consultar`

Bases e valores de um cálculo da folha — tabela focalculosbases (módulo folha_calculo, ~8.459.388 linhas).
O QUE É: Para cada cálculo de um empregado (identificado por `calculo`), uma linha por base: valor da base, taxa aplicada e valor resultante, com a descrição de como foi calculado. Mais de 8,4 milhões de linhas; é obrigatório informar o cálculo (o identificador vem de movimento_folha ou base_folha). A tabela não tem coluna de empresa.
COMENTÁRIO DO BANCO SOBRE A TABELA: Calculos - Bases de calculos
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
Tabela global (não depende de empresa): NÃO informe 'empresa'.
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): calculo.
FILTROS: calculo, base_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: calculo_base, calculo, base_codigo, base, taxa, valor, como_foi_calculado. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): base_descricao.
REGRAS DE NEGÓCIO (conferidas nos dados): Integridade: toda base de cálculo tem o tipo no cadastro (0 sem cadastro em 3,66 milhões de linhas de cálculos recentes; 124 tipos distintos em uso). | Valor = base × taxa / 100 em 86,6% das bases com taxa (2.954 de 3.412 na empresa 354); as demais são progressivas (INSS, IRRF) ou com dedução, e toda base sem taxa tem valor 0. | Base do INSS mensal (base 9): em 688 cálculos de 40 empresas na competência 2026-08 (folha mensal), a base gravada é IGUAL à soma dos proventos (tipo P) cujos eventos incidem na base 9 (foeventosbases) em 582 (84,6%); em 36 é MENOR porque está limitada ao teto do INSS (8.475,55, o valor mais frequente quando a base é menor); […]
PRIVACIDADE: Bases e valores de INSS, FGTS e IRRF por empregado identificável (financeiro).
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): base, valor
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `calculo`: Filtra I_CALCULOS (uniqueidentifier). Aceita: valor simples (igualdade), igual, lista de valores. (Código do cálculo)
- `base_codigo`: Filtra i_cadbases (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Base de Calculo)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `calculo_base_folha_totais`

Bases e valores de um cálculo da folha — TOTAIS por grupo da tabela focalculosbases (módulo folha_calculo). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. Tabela global (não depende de empresa): NÃO informe 'empresa'. OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): calculo. CAMPOS SOMÁVEIS: base, valor. CAMPOS PARA AGRUPAR: calculo_base, calculo, base_codigo, taxa, como_foi_calculado. Os filtros são os mesmos de calculo_base_folha_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Integridade: toda base de cálculo tem o tipo no cadastro (0 sem cadastro em 3,66 milhões de linhas de cálculos recentes; 124 tipos distintos em uso). | Valor = base × taxa / 100 em 86,6% das bases com taxa (2.954 de 3.412 na empresa 354); as demais são progressivas (INSS, IRRF) ou com dedução, e toda base sem taxa tem valor 0. | Base do INSS mensal (base 9): em 688 cálculos de 40 empresas na competência 2026-08 (folha mensal), a base gravada é IGUAL à soma dos proventos (tipo P) cujos eventos incidem na base 9 (foeventosbases) em 582 (84,6%); em 36 é MENOR porque está limitada ao teto do INSS (8.475,55, o valor mais frequente quando a base é menor); em 56 é menor por outro motivo e em 14 é maior que a soma (causas não apuradas, 10% do total).. Somente leitura.

Parâmetros:

- `calculo`: Filtra I_CALCULOS (uniqueidentifier). Aceita: valor simples (igualdade), igual, lista de valores. (Código do cálculo)
- `base_codigo`: Filtra i_cadbases (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Base de Calculo)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["calculo_base"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["base"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `incidencia_evento_folha_consultar`

Bases em que cada evento da folha incide — tabela foeventosbases (módulo folha_calculo, ~6.082.422 linhas).
O QUE É: Liga cada evento (rubrica) às bases de cálculo em que ele incide (INSS, FGTS, IRRF, férias...): é o que decide o que entra em cada base. 1 linha por empresa, evento e base. Inclui indicadores de envio ao eSocial.
COMENTÁRIO DO BANCO SOBRE A TABELA: Cadastro - Eventos bases
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: evento_codigo, base_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: evento_codigo, base_codigo, enviar_esocial, gerar_retificacao_esocial. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): evento_nome, base_descricao.
EXEMPLO COM DADOS: a empresa 349 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): 6,08 milhões de linhas. Bases com mais eventos: 59 (594.625), 21 (403.823), 15 FGTS Mensal (381.352), 62 (338.979), 9 INSS Mensal (301.557) e 35 (269.016). Integridade (20 maiores empresas, 185.668 linhas): todo evento da incidência existe no cadastro de eventos (0 sem evento). | É a regra que reconcilia a base do INSS: a soma dos proventos dos eventos com incidência na base 9 é a base gravada em calculo_base_folha (ver regras daquela entidade).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `evento_codigo`: Filtra i_eventos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do evento)
- `base_codigo`: Filtra i_cadbases (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo da base)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `incidencia_evento_folha_obter`

Bases em que cada evento da folha incide — obtém UM registro pela chave (codi_emp, i_eventos, i_cadbases) da tabela foeventosbases. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use incidencia_evento_folha_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `evento_codigo` (obrigatório): Filtra i_eventos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do evento)
- `base_codigo` (obrigatório): Filtra i_cadbases (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo da base)
