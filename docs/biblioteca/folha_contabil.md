# Módulo `folha_contabil`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `configuracao_integracao_folha_consultar` | consultar | fointegcont | empresa | ✔ |
| `configuracao_integracao_folha_obter` | obter | fointegcont | empresa, separador, codigo, tipo | ✔ |
| `evento_integracao_folha_consultar` | consultar | fointegconteve | empresa | ✔ |
| `evento_integracao_folha_obter` | obter | fointegconteve | empresa, separador, codigo, evento_codigo, tipo | ✔ |
| `lancamento_integracao_folha_consultar` | consultar | fointegcontlanc | empresa | ✔ |
| `lancamento_integracao_folha_obter` | obter | fointegcontlanc | empresa, competencia, lancamento_numero, tipo | ✔ |
| `lancamento_integracao_folha_totais` | totais | fointegcontlanc | empresa | ✔ |

## `configuracao_integracao_folha_consultar`

Configuração da integração da folha com a contabilidade — tabela fointegcont (módulo folha_contabil, ~112.913 linhas).
O QUE É: Para cada empresa, separador (centro de custos, departamento...), código e tipo: descrição (ex.: salários, vale transporte, PIS sobre folha), conta de débito e de crédito, histórico padrão e, para guias, contas de juros e multa. 112.913 linhas, 706 empresas; todas de origem "sistema".
COMENTÁRIO DO BANCO SOBRE A TABELA: Integracao Contabilidade - Configuracao
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: separador, codigo, tipo, descricao. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: separador, codigo, tipo, descricao, conta_credito, conta_debito, historico_codigo, historico_complemento, conta_debito_juros, historico_juros_codigo, historico_juros_complemento, conta_debito_multa, historico_multa_codigo, historico_multa_complemento. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 395 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Cada configuração (empresa, separador, código, tipo) é a chave; as contas e o histórico são os usados quando a folha é contabilizada. Todas as 112.913 linhas têm origem 0 (sistema). | Descrições típicas do tipo 1: SALÁRIOS, DESCONTOS DE FOLHA, PRO-LABORE, DESCONTOS PRO-LABORE, CONTRIBUIÇÃO SINDICAL, VALE TRANSPORTE.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `separador`: Filtra i_separador (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Separador)
- `codigo`: Filtra i_codigo (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `tipo`: Filtra tipo (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Sem legenda, 2=Sem legenda, 3=Sem legenda, 4=Sem legenda, 5=Sem legenda, 6=Sem legenda, 7=Sem legenda, 8=Sem legenda, 10=Sem legenda [significado NÃO confirmado: hipótese] (Tipo de configuracao)
- `descricao`: Filtra descricao (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Descricao)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `configuracao_integracao_folha_obter`

Configuração da integração da folha com a contabilidade — obtém UM registro pela chave (codi_emp, i_separador, i_codigo, tipo) da tabela fointegcont. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use configuracao_integracao_folha_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `separador` (obrigatório): Filtra i_separador (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Separador)
- `codigo` (obrigatório): Filtra i_codigo (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `tipo` (obrigatório): Filtra tipo (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Sem legenda, 2=Sem legenda, 3=Sem legenda, 4=Sem legenda, 5=Sem legenda, 6=Sem legenda, 7=Sem legenda, 8=Sem legenda, 10=Sem legenda [significado NÃO confirmado: hipótese] (Tipo de configuracao)

## `evento_integracao_folha_consultar`

Eventos de cada configuração da integração — tabela fointegconteve (módulo folha_contabil, ~831.213 linhas).
O QUE É: Liga cada configuração da integração (separador, código e tipo) aos eventos (rubricas) da folha que a alimentam. 831.213 linhas, 706 empresas.
COMENTÁRIO DO BANCO SOBRE A TABELA: Integracao Contabilidade - Configuracao - Eventos
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: separador, codigo, evento_codigo, tipo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: separador, codigo, evento_codigo, tipo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): configuracao_descricao, evento_nome.
EXEMPLO COM DADOS: a empresa 927 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Toda linha tem a configuração correspondente (0 sem registro na amostra da empresa 927, 1.194 linhas).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `separador`: Filtra i_separador (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Separador)
- `codigo`: Filtra i_codigo (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `evento_codigo`: Filtra i_eventos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Evento)
- `tipo`: Filtra tipo (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Sem legenda, 2=Sem legenda, 3=Sem legenda, 4=Sem legenda, 5=Sem legenda, 6=Sem legenda, 7=Sem legenda, 8=Sem legenda, 10=Sem legenda [significado NÃO confirmado: hipótese] (Tipo de configuracao)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `evento_integracao_folha_obter`

Eventos de cada configuração da integração — obtém UM registro pela chave (codi_emp, i_separador, i_codigo, i_eventos, tipo) da tabela fointegconteve. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use evento_integracao_folha_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `separador` (obrigatório): Filtra i_separador (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Separador)
- `codigo` (obrigatório): Filtra i_codigo (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `evento_codigo` (obrigatório): Filtra i_eventos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Evento)
- `tipo` (obrigatório): Filtra tipo (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Sem legenda, 2=Sem legenda, 3=Sem legenda, 4=Sem legenda, 5=Sem legenda, 6=Sem legenda, 7=Sem legenda, 8=Sem legenda, 10=Sem legenda [significado NÃO confirmado: hipótese] (Tipo de configuracao)

## `lancamento_integracao_folha_consultar`

Lançamentos contábeis gerados pela integração da folha — tabela fointegcontlanc (módulo folha_contabil, ~213.590 linhas).
O QUE É: Registra, por empresa da folha, competência e tipo de integração, o número do lançamento contábil gerado (na empresa da contabilidade `codi_emp_cta`), com o separador usado. 213.590 linhas, 457 empresas, de 2013-01 a 2026-09. Os valores ficam em contabil.lancamento.
COMENTÁRIO DO BANCO SOBRE A TABELA: Numero do lancamentos
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna competencia. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: competencia, lancamento_numero, tipo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: competencia, lancamento_numero, tipo, empresa_contabilidade, tipo_separador, separador. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): lancamento_data, lancamento_valor.
EXEMPLO COM DADOS: a empresa 920 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Integridade: todo lançamento registrado existe em ctlancto (0 sem lançamento nos 38.065 de 2025). | Tipos em uso: 1 (102.127 linhas), 5 (30.117), 6 (25.574), 4 (21.715), 2 (16.688), 3 (16.268) e 10 (1.213). Quase tudo sem separador (211.854); 1.714 por centro de custos. | Empresa 1430, 2026-08: valor lançado por tipo 1 = 108.484,19 (9 lançamentos), 2 = 13.978,47, 3 = 9.473,61, 4 = 22.725,96, 5 = 10.687,46, 6 = 5.380,51; a folha do mês soma proventos 144.751,35, descontos 96.374,31 e líquido 48.377,04, sem correspondência exata com um tipo.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `competencia`: Filtra competencia (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia) Datas no formato AAAA-MM-DD.
- `lancamento_numero`: Filtra nume_lanc (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Numero lancamento)
- `tipo`: Filtra tipo (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Sem legenda, 2=Sem legenda, 3=Sem legenda, 4=Sem legenda, 5=Sem legenda, 6=Sem legenda, 7=Sem legenda, 8=Sem legenda, 10=Sem legenda [significado NÃO confirmado: hipótese] (Tipo da integracao)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `lancamento_integracao_folha_obter`

Lançamentos contábeis gerados pela integração da folha — obtém UM registro pela chave (codi_emp, competencia, nume_lanc, tipo) da tabela fointegcontlanc. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use lancamento_integracao_folha_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `competencia` (obrigatório): Filtra competencia (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia) Datas no formato AAAA-MM-DD.
- `lancamento_numero` (obrigatório): Filtra nume_lanc (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Numero lancamento)
- `tipo` (obrigatório): Filtra tipo (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Sem legenda, 2=Sem legenda, 3=Sem legenda, 4=Sem legenda, 5=Sem legenda, 6=Sem legenda, 7=Sem legenda, 8=Sem legenda, 10=Sem legenda [significado NÃO confirmado: hipótese] (Tipo da integracao)

## `lancamento_integracao_folha_totais`

Lançamentos contábeis gerados pela integração da folha — TOTAIS por grupo da tabela fointegcontlanc (módulo folha_contabil). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna competencia. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: empresa_contabilidade. CAMPOS PARA AGRUPAR: competencia:mes, lancamento_numero, tipo, tipo_separador, separador. Os filtros são os mesmos de lancamento_integracao_folha_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (tipo, tipo_separador) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Integridade: todo lançamento registrado existe em ctlancto (0 sem lançamento nos 38.065 de 2025). | Tipos em uso: 1 (102.127 linhas), 5 (30.117), 6 (25.574), 4 (21.715), 2 (16.688), 3 (16.268) e 10 (1.213). Quase tudo sem separador (211.854); 1.714 por centro de custos. | Empresa 1430, 2026-08: valor lançado por tipo 1 = 108.484,19 (9 lançamentos), 2 = 13.978,47, 3 = 9.473,61, 4 = 22.725,96, 5 = 10.687,46, 6 = 5.380,51; a folha do mês soma proventos 144.751,35, descontos 96.374,31 e líquido 48.377,04, sem correspondência exata com um tipo.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `competencia`: Filtra competencia (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia) Datas no formato AAAA-MM-DD.
- `lancamento_numero`: Filtra nume_lanc (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Numero lancamento)
- `tipo`: Filtra tipo (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Sem legenda, 2=Sem legenda, 3=Sem legenda, 4=Sem legenda, 5=Sem legenda, 6=Sem legenda, 7=Sem legenda, 8=Sem legenda, 10=Sem legenda [significado NÃO confirmado: hipótese] (Tipo da integracao)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["competencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["empresa_contabilidade"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).
