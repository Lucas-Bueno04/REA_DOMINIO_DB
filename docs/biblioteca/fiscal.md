# Módulo `fiscal`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `acumulador_consultar` | consultar | efacumulador | empresa | ✔ |
| `acumulador_obter` | obter | efacumulador | empresa, codigo | ✔ |
| `cliente_consultar` | consultar | efclientes | empresa | ✔ |
| `cliente_obter` | obter | efclientes | empresa, codigo | ✔ |
| `nota_entrada_consultar` | consultar | efentradas | empresa | ✔ |
| `nota_entrada_obter` | obter | efentradas | empresa, codigo | ✔ |
| `nota_entrada_totais` | totais | efentradas | empresa | ✔ |
| `pagamento_nota_entrada_consultar` | consultar | efentradaspag | empresa | ✔ |
| `pagamento_nota_entrada_totais` | totais | efentradaspag | empresa | ✔ |
| `parcela_nota_entrada_consultar` | consultar | efentradaspar | empresa | ✔ |
| `parcela_nota_entrada_totais` | totais | efentradaspar | empresa | ✔ |
| `especie_documento_consultar` | consultar | efespecies | — | ✔ |
| `especie_documento_obter` | obter | efespecies | codigo | ✔ |
| `fornecedor_consultar` | consultar | effornece | empresa | ✔ |
| `fornecedor_obter` | obter | effornece | empresa, codigo | ✔ |
| `imposto_nota_entrada_consultar` | consultar | efimpent | empresa | ✔ |
| `imposto_nota_entrada_totais` | totais | efimpent | empresa | ✔ |
| `imposto_nota_saida_consultar` | consultar | efimpsai | empresa | ✔ |
| `imposto_nota_saida_totais` | totais | efimpsai | empresa | ✔ |
| `imposto_nota_servico_consultar` | consultar | efimpser | empresa | ✔ |
| `imposto_nota_servico_totais` | totais | efimpser | empresa | ✔ |
| `item_nota_entrada_consultar` | consultar | efmvepro | empresa | ✔ |
| `item_nota_entrada_totais` | totais | efmvepro | empresa | ✔ |
| `item_nota_saida_consultar` | consultar | efmvspro | empresa | ✔ |
| `item_nota_saida_totais` | totais | efmvspro | empresa | ✔ |
| `natureza_operacao_consultar` | consultar | efnatureza | — | ✔ |
| `produto_consultar` | consultar | efprodutos | empresa | ✔ |
| `produto_obter` | obter | efprodutos | empresa, codigo | ✔ |
| `produto_totais` | totais | efprodutos | empresa | ✔ |
| `nota_saida_consultar` | consultar | efsaidas | empresa | ✔ |
| `nota_saida_obter` | obter | efsaidas | empresa, codigo | ✔ |
| `nota_saida_totais` | totais | efsaidas | empresa | ✔ |
| `pagamento_nota_saida_consultar` | consultar | efsaidaspag | empresa | ✔ |
| `pagamento_nota_saida_totais` | totais | efsaidaspag | empresa | ✔ |
| `parcela_nota_saida_consultar` | consultar | efsaidaspar | empresa | ✔ |
| `parcela_nota_saida_totais` | totais | efsaidaspar | empresa | ✔ |
| `apuracao_imposto_consultar` | consultar | efsdoimp | empresa | ✔ |
| `apuracao_imposto_obter` | obter | efsdoimp | empresa, imposto_codigo, competencia, periodicidade | ✔ |
| `apuracao_imposto_totais` | totais | efsdoimp | empresa | ✔ |
| `nota_servico_consultar` | consultar | efservicos | empresa | ✔ |
| `nota_servico_obter` | obter | efservicos | empresa, codigo | ✔ |
| `nota_servico_totais` | totais | efservicos | empresa | ✔ |
| `pagamento_nota_servico_consultar` | consultar | efservicospag | empresa | ✔ |
| `pagamento_nota_servico_totais` | totais | efservicospag | empresa | ✔ |
| `parcela_nota_servico_consultar` | consultar | efservicospar | empresa | ✔ |
| `parcela_nota_servico_totais` | totais | efservicospar | empresa | ✔ |
| `imposto_consultar` | consultar | geimposto | empresa | ✔ |
| `imposto_obter` | obter | geimposto | empresa, codigo | ✔ |

## `acumulador_consultar`

Acumuladores — tabela EFACUMULADOR (módulo fiscal, ~434.521 linhas).
O QUE É: Acumuladores fiscais (classificam notas de entrada, saída e serviço).
COMENTÁRIO DO BANCO SOBRE A TABELA: Acumuladores - Cadastro
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, nome, situacao. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, nome, situacao, data_cadastro, data_inativacao. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 1320 tem registros nesta tabela (use para testar).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra codi_acu (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `nome`: Filtra nome_acu (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Nome)
- `situacao`: Filtra situacao_acu (char). Aceita: valor simples (igualdade), igual. (Situação)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `acumulador_obter`

Acumuladores — obtém UM registro pela chave (codi_emp, codi_acu) da tabela EFACUMULADOR. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use acumulador_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra codi_acu (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `cliente_consultar`

Clientes — tabela efclientes (módulo fiscal, ~689.035 linhas).
O QUE É: Cadastro de clientes da escrita fiscal (por empresa). Inclui pessoas físicas — ver `sensivel`.
COMENTÁRIO DO BANCO SOBRE A TABELA: Clientes - Cadastro
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, nome, cnpj_cpf, uf, regime_apuracao. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, nome, nome_resumido, cnpj_cpf, tipo_inscricao, inscricao_estadual, inscricao_municipal, contribuinte_icms, regime_apuracao, produtor_rural_pf, endereco, numero, complemento, bairro, cidade, uf, cep, telefone, municipio_codigo, pais_codigo, conta_contabil, data_cadastro. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): municipio_nome, municipio_ibge.
EXEMPLO COM DADOS: a empresa 1128 tem registros nesta tabela (use para testar).
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): cnpj_cpf, endereco, telefone
POSSÍVEIS DADOS PESSOAIS/FINANCEIROS (os dados saem em claro; devolva só o que a pergunta exigir): nome, nome_resumido, municipio_nome.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra codi_cli (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `nome`: Filtra nome_cli (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Razao Social)
- `cnpj_cpf`: Filtra cgce_cli (char). Aceita: valor simples (igualdade), igual. (CNPJ)
- `uf`: Filtra sigl_est (char). Aceita: valor simples (igualdade), igual, lista de valores. (Estado)
- `regime_apuracao`: Filtra regime_cli (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: N=Normal, M=ME - Simples Nacional, E=EPP - Simples Nacional, O=Outros, U=Imune, I=Isenta, S=ME - Simples Nacional (fornecedor), P=EPP - Simples Nacional (fornecedor) [parcialmente confirmado] (REGIME DE APURACAO (N - NORMAL/M- ME - SIMPLES NACIONAL/E - EPP - SIMPLES NACIONAL/O - OUTROS/U - IMUNE/I - ISENTA))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `cliente_obter`

Clientes — obtém UM registro pela chave (codi_emp, codi_cli) da tabela efclientes. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use cliente_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra codi_cli (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `nota_entrada_consultar`

Notas fiscais de entrada — tabela efentradas (módulo fiscal, ~511.949 linhas).
O QUE É: Cabeçalho das notas fiscais de entrada (compras e outras entradas) lançadas na escrita fiscal.
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna dent_ent. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: codigo, numero, serie, data_entrada, data_emissao, competencia, fornecedor_codigo, acumulador_codigo, natureza_codigo, especie_codigo, emitente, situacao, chave_nfe, valor_contabil. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, numero, numero_final, serie, sub_serie, data_entrada, data_emissao, competencia, valor_contabil, valor_produtos, valor_frete, valor_seguro, despesas_acessorias, valor_pis, valor_cofins, valor_excluido, fornecedor_codigo, acumulador_codigo, natureza_codigo, natureza_versao, especie_codigo, municipio_codigo, situacao, emitente, tipo_frete, chave_nfe, cfop_documento, observacao, usuario, origem_registro. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): fornecedor_nome, fornecedor_cnpj_cpf, acumulador_nome, natureza_nome, especie_nome, especie_modelo, municipio_nome, municipio_ibge.
EXEMPLO COM DADOS: a empresa 1547 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Na apuração de um imposto só entram as notas que têm aquele imposto (imposto_nota_entrada); a soma do valor_contabil do cabeçalho das notas NÃO fecha com a apuração (ex.: 418.479,86 nas notas contra 372.995,98 apurados de ICMS). Validado centavo a centavo somando imposto_nota_entrada.valor_contabil. | O mês de apuração é o de data_entrada, não o de competencia (quase sempre 1900-01-01).
POSSÍVEIS DADOS PESSOAIS/FINANCEIROS (os dados saem em claro; devolva só o que a pergunta exigir): usuario, fornecedor_cnpj_cpf.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo`: Filtra codi_ent (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `numero`: Filtra nume_ent (numeric). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Documento)
- `serie`: Filtra seri_ent (char). Aceita: valor simples (igualdade), igual. (Serie)
- `data_entrada`: Filtra dent_ent (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data de entrada) Datas no formato AAAA-MM-DD.
- `data_emissao`: Filtra ddoc_ent (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data de emissao) Datas no formato AAAA-MM-DD.
- `competencia`: Filtra compte_ent (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}. (Competencia) Datas no formato AAAA-MM-DD.
- `fornecedor_codigo`: Filtra codi_for (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Fornecedor)
- `acumulador_codigo`: Filtra codi_acu (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Acumulador)
- `natureza_codigo`: Filtra codi_nat (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Natureza)
- `especie_codigo`: Filtra codi_esp (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Especie)
- `emitente`: Filtra emitente_ent (char). Aceita: valor simples (igualdade), igual. Códigos: P=Próprio, T=Terceiro (Emitente da Nota Fiscal ( P-Proprio / T-Terceiro ))
- `situacao`: Filtra situacao_ent (tinyint). Aceita: valor simples (igualdade), igual, lista de valores.  (Codigo do modelo do documento fiscal)
- `chave_nfe`: Filtra chave_nfe_ent (char). Aceita: valor simples (igualdade), igual. (Chave da nota fiscal eletrônica)
- `valor_contabil`: Filtra vcon_ent (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Valor contabil)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `nota_entrada_obter`

Notas fiscais de entrada — obtém UM registro pela chave (codi_emp, codi_ent) da tabela efentradas. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use nota_entrada_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra codi_ent (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `nota_entrada_totais`

Notas fiscais de entrada — TOTAIS por grupo da tabela efentradas (módulo fiscal). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna dent_ent. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor_contabil, valor_produtos, valor_frete, valor_seguro, despesas_acessorias, valor_pis, valor_cofins, valor_excluido. CAMPOS PARA AGRUPAR: codigo, numero, numero_final, serie, sub_serie, data_entrada:mes, data_emissao:mes, competencia:mes, fornecedor_codigo, acumulador_codigo, natureza_codigo, natureza_versao, especie_codigo, municipio_codigo, situacao, emitente, tipo_frete, chave_nfe, cfop_documento, observacao, usuario, origem_registro. Os filtros são os mesmos de nota_entrada_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (situacao, emitente, tipo_frete) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Na apuração de um imposto só entram as notas que têm aquele imposto (imposto_nota_entrada); a soma do valor_contabil do cabeçalho das notas NÃO fecha com a apuração (ex.: 418.479,86 nas notas contra 372.995,98 apurados de ICMS). Validado centavo a centavo somando imposto_nota_entrada.valor_contabil. | O mês de apuração é o de data_entrada, não o de competencia (quase sempre 1900-01-01).. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo`: Filtra codi_ent (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `numero`: Filtra nume_ent (numeric). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Documento)
- `serie`: Filtra seri_ent (char). Aceita: valor simples (igualdade), igual. (Serie)
- `data_entrada`: Filtra dent_ent (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data de entrada) Datas no formato AAAA-MM-DD.
- `data_emissao`: Filtra ddoc_ent (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data de emissao) Datas no formato AAAA-MM-DD.
- `competencia`: Filtra compte_ent (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}. (Competencia) Datas no formato AAAA-MM-DD.
- `fornecedor_codigo`: Filtra codi_for (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Fornecedor)
- `acumulador_codigo`: Filtra codi_acu (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Acumulador)
- `natureza_codigo`: Filtra codi_nat (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Natureza)
- `especie_codigo`: Filtra codi_esp (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Especie)
- `emitente`: Filtra emitente_ent (char). Aceita: valor simples (igualdade), igual. Códigos: P=Próprio, T=Terceiro (Emitente da Nota Fiscal ( P-Proprio / T-Terceiro ))
- `situacao`: Filtra situacao_ent (tinyint). Aceita: valor simples (igualdade), igual, lista de valores.  (Codigo do modelo do documento fiscal)
- `chave_nfe`: Filtra chave_nfe_ent (char). Aceita: valor simples (igualdade), igual. (Chave da nota fiscal eletrônica)
- `valor_contabil`: Filtra vcon_ent (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Valor contabil)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["data_entrada:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor_contabil"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `pagamento_nota_entrada_consultar`

Pagamentos das notas de entrada — tabela efentradaspag (módulo fiscal, ~104.582 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: Notas Fiscais de Entrada - Pagamento das Parcelas
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna pgto_entp. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: codigo_nota, data_pagamento, tipo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo_nota, parcela, data_pagamento, tipo, numero_pagamento, valor, lancamento_contabil, origem_pagamento, numero_titulo, historico. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 695 tem registros nesta tabela (use para testar).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_nota`: Filtra codi_ent (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Entrada)
- `data_pagamento`: Filtra pgto_entp (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data do pagamento) Datas no formato AAAA-MM-DD.
- `tipo`: Filtra tipo_entp (tinyint). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Normal, 2=Juros, 3=Multa, 4=Desconto, 5=Devolução, 6=PIS, 7=COFINS, 8=CSOC, 9=CRF, 10=IRRF, … (+4) (Tipo (1-Normal/ 2-Juros/ 3-Multa/ 4-Descto/ 5-Devolucao/ 6-PIS/ 7-COFINS/ 8-CSOC/ 9-CRF/ 10-IRRF/ 11-IRRFPF/ 12-Juros Valor Presente/ 13-ISS/ 14-Outras))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `pagamento_nota_entrada_totais`

Pagamentos das notas de entrada — TOTAIS por grupo da tabela efentradaspag (módulo fiscal). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna pgto_entp. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor, lancamento_contabil. CAMPOS PARA AGRUPAR: codigo_nota, parcela, data_pagamento:mes, tipo, numero_pagamento, origem_pagamento, numero_titulo, historico. Os filtros são os mesmos de pagamento_nota_entrada_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (tipo, origem_pagamento) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_nota`: Filtra codi_ent (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Entrada)
- `data_pagamento`: Filtra pgto_entp (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data do pagamento) Datas no formato AAAA-MM-DD.
- `tipo`: Filtra tipo_entp (tinyint). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Normal, 2=Juros, 3=Multa, 4=Desconto, 5=Devolução, 6=PIS, 7=COFINS, 8=CSOC, 9=CRF, 10=IRRF, … (+4) (Tipo (1-Normal/ 2-Juros/ 3-Multa/ 4-Descto/ 5-Devolucao/ 6-PIS/ 7-COFINS/ 8-CSOC/ 9-CRF/ 10-IRRF/ 11-IRRFPF/ 12-Juros Valor Presente/ 13-ISS/ 14-Outras))
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["data_pagamento:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `parcela_nota_entrada_consultar`

Parcelas das notas de entrada — tabela efentradaspar (módulo fiscal, ~157.539 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: Notas Fiscais de Entrada - Parcelas
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna vcto_entp. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: codigo_nota, vencimento. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo_nota, parcela, vencimento, valor, valor_bruto, tipo, valor_crf, valor_irrf, valor_iss_retido, valor_inss_retido, valor_pis_retido, valor_cofins_retido, valor_csll_retido, numero_titulo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 661 tem registros nesta tabela (use para testar).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_nota`: Filtra codi_ent (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Entrada)
- `vencimento`: Filtra vcto_entp (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data de vencimento da Parcela) Datas no formato AAAA-MM-DD.
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `parcela_nota_entrada_totais`

Parcelas das notas de entrada — TOTAIS por grupo da tabela efentradaspar (módulo fiscal). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna vcto_entp. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor, valor_bruto, valor_crf, valor_irrf, valor_iss_retido, valor_inss_retido, valor_pis_retido, valor_cofins_retido, valor_csll_retido. CAMPOS PARA AGRUPAR: codigo_nota, parcela, vencimento:mes, tipo, numero_titulo. Os filtros são os mesmos de parcela_nota_entrada_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (tipo) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_nota`: Filtra codi_ent (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Entrada)
- `vencimento`: Filtra vcto_entp (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data de vencimento da Parcela) Datas no formato AAAA-MM-DD.
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["vencimento:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `especie_documento_consultar`

Espécies de documento fiscal — tabela efespecies (módulo fiscal, ~55 linhas).
O QUE É: Tabela global de espécies (NF, NFe, NFCe, CTe...). Não depende de empresa.
COMENTÁRIO DO BANCO SOBRE A TABELA: Especies - Cadastro
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
Tabela global (não depende de empresa): NÃO informe 'empresa'.
FILTROS: codigo, nome. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, nome, modelo_documento, codigo_modelo, tipo, documento_nao_fiscal, nota_fiscal_conjugada. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `codigo`: Filtra codi_esp (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `nome`: Filtra nome_esp (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}. (Nome)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `especie_documento_obter`

Espécies de documento fiscal — obtém UM registro pela chave (codi_esp) da tabela efespecies. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use especie_documento_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `codigo` (obrigatório): Filtra codi_esp (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `fornecedor_consultar`

Fornecedores — tabela effornece (módulo fiscal, ~61.984 linhas).
O QUE É: Cadastro de fornecedores da escrita fiscal (por empresa).
COMENTÁRIO DO BANCO SOBRE A TABELA: Fornecedores - Cadastro
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, nome, cnpj_cpf, uf. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, nome, nome_resumido, cnpj_cpf, tipo_inscricao, inscricao_estadual, inscricao_municipal, contribuinte_icms, regime_apuracao, endereco, numero, complemento, bairro, cidade, uf, cep, telefone, email, municipio_codigo, pais_codigo, conta_contabil, data_cadastro. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): municipio_nome, municipio_ibge.
EXEMPLO COM DADOS: a empresa 66 tem registros nesta tabela (use para testar).
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): cnpj_cpf, endereco, telefone, email
POSSÍVEIS DADOS PESSOAIS/FINANCEIROS (os dados saem em claro; devolva só o que a pergunta exigir): nome, nome_resumido, municipio_nome.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra codi_for (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `nome`: Filtra nome_for (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Razao social)
- `cnpj_cpf`: Filtra cgce_for (char). Aceita: valor simples (igualdade), igual. (CNPJ)
- `uf`: Filtra sigl_est (char). Aceita: valor simples (igualdade), igual, lista de valores. (Estado)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `fornecedor_obter`

Fornecedores — obtém UM registro pela chave (codi_emp, codi_for) da tabela effornece. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use fornecedor_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra codi_for (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `imposto_nota_entrada_consultar`

Impostos das notas de entrada — tabela efimpent (módulo fiscal, ~806.969 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: Notas Fiscais de Entrada - Impostos
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): codigo_nota, periodo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna nota.dent_ent. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: codigo_nota, imposto_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo_nota, imposto_codigo, sequencia, percentual_base, base_calculo, aliquota, valor_imposto, valor_isentas, valor_outras, valor_contabil, nao_tributadas, parcela_reduzida, valor_ipi, valor_substituicao, codigo_recolhimento. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): nota_numero, nota_serie, nota_data_entrada, imposto_nome, imposto_sigla.
EXEMPLO COM DADOS: a empresa 1634 tem registros nesta tabela (use para testar).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_nota`: Filtra codi_ent (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Entrada)
- `imposto_codigo`: Filtra codi_imp (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=ICMS, 2=IPI, 3=ISS, 4=PIS, 5=COFINS, 8=DIFALI, 9=Substituição Tributária, 16=IRRF, 18=ISS Retido, 22=PIS (Retido), … (+3) (Imposto)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `imposto_nota_entrada_totais`

Impostos das notas de entrada — TOTAIS por grupo da tabela efimpent (módulo fiscal). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): codigo_nota, periodo. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna nota.dent_ent. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: base_calculo, valor_imposto, valor_isentas, valor_outras, valor_contabil, valor_ipi, valor_substituicao. CAMPOS PARA AGRUPAR: codigo_nota, imposto_codigo, sequencia, percentual_base, aliquota, nao_tributadas, parcela_reduzida, codigo_recolhimento. Os filtros são os mesmos de imposto_nota_entrada_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (imposto_codigo) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_nota`: Filtra codi_ent (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Entrada)
- `imposto_codigo`: Filtra codi_imp (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=ICMS, 2=IPI, 3=ISS, 4=PIS, 5=COFINS, 8=DIFALI, 9=Substituição Tributária, 16=IRRF, 18=ISS Retido, 22=PIS (Retido), … (+3) (Imposto)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["imposto_codigo"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["base_calculo"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `imposto_nota_saida_consultar`

Impostos das notas de saída — tabela efimpsai (módulo fiscal, ~636.496 linhas).
O QUE É: Uma linha por imposto de cada nota de saída (ICMS, IPI, ISS, PIS, COFINS, retenções...), com base, alíquota e valor.
COMENTÁRIO DO BANCO SOBRE A TABELA: Notas Fiscais de Saida - Impostos
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): codigo_nota, periodo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna nota.dsai_sai. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: codigo_nota, imposto_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo_nota, imposto_codigo, sequencia, percentual_base, base_calculo, aliquota, valor_imposto, valor_isentas, valor_outras, valor_contabil, nao_tributadas, parcela_reduzida, valor_ipi, codigo_recolhimento. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): nota_numero, nota_serie, nota_data_saida, imposto_nome, imposto_sigla.
EXEMPLO COM DADOS: a empresa 896 tem registros nesta tabela (use para testar).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_nota`: Filtra codi_sai (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Saida)
- `imposto_codigo`: Filtra codi_imp (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=ICMS, 2=IPI, 3=ISS, 4=PIS, 5=COFINS, 8=DIFALI, 9=Substituição Tributária, 16=IRRF, 18=ISS Retido, 22=PIS (Retido), … (+3) (Imposto)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `imposto_nota_saida_totais`

Impostos das notas de saída — TOTAIS por grupo da tabela efimpsai (módulo fiscal). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): codigo_nota, periodo. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna nota.dsai_sai. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: base_calculo, valor_imposto, valor_isentas, valor_outras, valor_contabil, valor_ipi. CAMPOS PARA AGRUPAR: codigo_nota, imposto_codigo, sequencia, percentual_base, aliquota, nao_tributadas, parcela_reduzida, codigo_recolhimento. Os filtros são os mesmos de imposto_nota_saida_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (imposto_codigo) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_nota`: Filtra codi_sai (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Saida)
- `imposto_codigo`: Filtra codi_imp (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=ICMS, 2=IPI, 3=ISS, 4=PIS, 5=COFINS, 8=DIFALI, 9=Substituição Tributária, 16=IRRF, 18=ISS Retido, 22=PIS (Retido), … (+3) (Imposto)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["imposto_codigo"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["base_calculo"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `imposto_nota_servico_consultar`

Impostos das notas de serviço — tabela efimpser (módulo fiscal, ~1.155.629 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: Notas Fiscais de Servico - Impostos
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): codigo_nota, periodo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna nota.dser_ser. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: codigo_nota, imposto_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo_nota, imposto_codigo, sequencia, percentual_base, base_calculo, aliquota, valor_imposto, valor_isentas, valor_outras, valor_contabil, codigo_recolhimento. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): nota_numero, nota_serie, nota_data_servico, imposto_nome, imposto_sigla.
EXEMPLO COM DADOS: a empresa 1606 tem registros nesta tabela (use para testar).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_nota`: Filtra codi_ser (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Servico)
- `imposto_codigo`: Filtra codi_imp (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=ICMS, 2=IPI, 3=ISS, 4=PIS, 5=COFINS, 8=DIFALI, 9=Substituição Tributária, 16=IRRF, 18=ISS Retido, 22=PIS (Retido), … (+3) (Imposto)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `imposto_nota_servico_totais`

Impostos das notas de serviço — TOTAIS por grupo da tabela efimpser (módulo fiscal). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): codigo_nota, periodo. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna nota.dser_ser. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: base_calculo, valor_imposto, valor_isentas, valor_outras, valor_contabil. CAMPOS PARA AGRUPAR: codigo_nota, imposto_codigo, sequencia, percentual_base, aliquota, codigo_recolhimento. Os filtros são os mesmos de imposto_nota_servico_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (imposto_codigo) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_nota`: Filtra codi_ser (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Servico)
- `imposto_codigo`: Filtra codi_imp (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=ICMS, 2=IPI, 3=ISS, 4=PIS, 5=COFINS, 8=DIFALI, 9=Substituição Tributária, 16=IRRF, 18=ISS Retido, 22=PIS (Retido), … (+3) (Imposto)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["imposto_codigo"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["base_calculo"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `item_nota_entrada_consultar`

Itens das notas de entrada — tabela efmvepro (módulo fiscal, ~620.302 linhas).
O QUE É: Produtos de cada nota de entrada, com bases e valores de ICMS, ST e IPI.
COMENTÁRIO DO BANCO SOBRE A TABELA: Notas Fiscais de Entrada - Produtos
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): codigo_nota, periodo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna nota.dent_ent. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: codigo_nota, produto_codigo, cst_icms, cfop, data. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo_nota, sequencial, produto_codigo, quantidade, valor_unitario, valor_produto, valor_desconto, valor_total, valor_frete, valor_seguro, despesas_acessorias, cst_icms, base_icms, aliquota_icms, valor_icms, base_icms_st, aliquota_st, valor_st, base_ipi, aliquota_ipi, valor_ipi, cfop, cst_pis, base_pis, aliquota_pis, valor_pis, cst_cofins, base_cofins, aliquota_cofins, valor_cofins, data. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): nota_numero, nota_serie, nota_data_entrada, produto_descricao, produto_ncm.
EXEMPLO COM DADOS: a empresa 9999 tem registros nesta tabela (use para testar).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_nota`: Filtra codi_ent (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Entrada)
- `produto_codigo`: Filtra codi_pdi (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Produto)
- `cst_icms`: Filtra cst_mep (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo da Situacao Tributaria)
- `cfop`: Filtra cfop_mep (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CFOP)
- `data`: Filtra data_mep (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data) Datas no formato AAAA-MM-DD.
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `item_nota_entrada_totais`

Itens das notas de entrada — TOTAIS por grupo da tabela efmvepro (módulo fiscal). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): codigo_nota, periodo. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna nota.dent_ent. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: quantidade, valor_unitario, valor_produto, valor_desconto, valor_total, valor_frete, valor_seguro, despesas_acessorias, base_icms, valor_icms, base_icms_st, valor_st, base_ipi, valor_ipi, base_pis, valor_pis, base_cofins, valor_cofins. CAMPOS PARA AGRUPAR: codigo_nota, sequencial, produto_codigo, cst_icms, aliquota_icms, aliquota_st, aliquota_ipi, cfop, cst_pis, aliquota_pis, cst_cofins, aliquota_cofins, data:mes. Os filtros são os mesmos de item_nota_entrada_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_nota`: Filtra codi_ent (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Entrada)
- `produto_codigo`: Filtra codi_pdi (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Produto)
- `cst_icms`: Filtra cst_mep (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo da Situacao Tributaria)
- `cfop`: Filtra cfop_mep (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CFOP)
- `data`: Filtra data_mep (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data) Datas no formato AAAA-MM-DD.
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["data:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["quantidade"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `item_nota_saida_consultar`

Itens das notas de saída — tabela efmvspro (módulo fiscal, ~1.338.693 linhas).
O QUE É: Produtos de cada nota de saída, com bases e valores de ICMS, ST, IPI, PIS e COFINS.
COMENTÁRIO DO BANCO SOBRE A TABELA: Notas Fiscais de Saida - Produtos
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): codigo_nota, periodo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna nota.dsai_sai. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: codigo_nota, produto_codigo, cfop, cst_icms, data. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo_nota, sequencial, produto_codigo, quantidade, unidade, valor_unitario, valor_produto, valor_desconto, valor_frete, valor_seguro, despesas_acessorias, cfop, cst_icms, base_icms, aliquota_icms, valor_icms, base_icms_st, aliquota_st, valor_st, base_ipi, aliquota_ipi, valor_ipi, cst_pis, base_pis, aliquota_pis, valor_pis, cst_cofins, base_cofins, aliquota_cofins, valor_cofins, quantidade_cancelada, valor_cancelado, data. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): nota_numero, nota_serie, nota_data_saida, nota_cancelada, produto_descricao, produto_ncm.
EXEMPLO COM DADOS: a empresa 1566 tem registros nesta tabela (use para testar).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_nota`: Filtra codi_sai (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Saida)
- `produto_codigo`: Filtra codi_pdi (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Produto)
- `cfop`: Filtra cfop_msp (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CFOP)
- `cst_icms`: Filtra cst_msp (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo da Stituacao Tributaria)
- `data`: Filtra data_msp (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data) Datas no formato AAAA-MM-DD.
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `item_nota_saida_totais`

Itens das notas de saída — TOTAIS por grupo da tabela efmvspro (módulo fiscal). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): codigo_nota, periodo. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna nota.dsai_sai. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: quantidade, valor_unitario, valor_produto, valor_desconto, valor_frete, valor_seguro, despesas_acessorias, base_icms, valor_icms, base_icms_st, valor_st, base_ipi, valor_ipi, base_pis, valor_pis, base_cofins, valor_cofins, quantidade_cancelada, valor_cancelado. CAMPOS PARA AGRUPAR: codigo_nota, sequencial, produto_codigo, unidade, cfop, cst_icms, aliquota_icms, aliquota_st, aliquota_ipi, cst_pis, aliquota_pis, cst_cofins, aliquota_cofins, data:mes. Os filtros são os mesmos de item_nota_saida_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_nota`: Filtra codi_sai (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Saida)
- `produto_codigo`: Filtra codi_pdi (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Produto)
- `cfop`: Filtra cfop_msp (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CFOP)
- `cst_icms`: Filtra cst_msp (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo da Stituacao Tributaria)
- `data`: Filtra data_msp (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data) Datas no formato AAAA-MM-DD.
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["data:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["quantidade"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `natureza_operacao_consultar`

Naturezas de operação (CFOP) — tabela efnatureza (módulo fiscal, ~1.548 linhas).
O QUE É: Tabela global de naturezas/CFOP (não depende de empresa). Existem versões (versao_nat 1 e 2).
COMENTÁRIO DO BANCO SOBRE A TABELA: Naturezas - Cadastro
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
Tabela global (não depende de empresa): NÃO informe 'empresa'.
FILTROS: codigo, nome. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, versao, nome, mascara. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `codigo`: Filtra codi_nat (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Codigo)
- `nome`: Filtra nome_nat (varchar). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}. (Nome)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `produto_consultar`

Produtos — tabela efprodutos (módulo fiscal, ~221.153 linhas).
O QUE É: Cadastro de produtos/mercadorias (por empresa) — base de itens de entrada e saída e do inventário.
COMENTÁRIO DO BANCO SOBRE A TABELA: Produtos - Cadastro
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, descricao, ncm, tipo, tipo_item. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, descricao, grupo_codigo, unidade, ncm, ean, tipo, tipo_item, cst, aliquota_icms, aliquota_ipi, valor_unitario, quantidade_inicial, valor_inicial, quantidade_final, valor_final. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 1242 tem registros nesta tabela (use para testar).
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra codi_pdi (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Codigo)
- `descricao`: Filtra desc_pdi (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Descricao)
- `ncm`: Filtra cncm_pdi (char). Aceita: valor simples (igualdade), igual, {"prefixo":"x"}. (Nomenclatura Comum do Mercosul)
- `tipo`: Filtra tipo_pdi (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: V=Veículos novos, M=Medicamentos, A=Armas de fogo, O=Outros, C=Combustíveis, U=Comunicação, E=Energia elétrica, S=Veículos usados (Tipo(V=Veíc. Novos/M=Medicamentos/A=Armas Fogo/O=Outros/C=Combustíveis/U=Comunicação/E=Energ. Elétr./S=Veíc. Usados))
- `tipo_item`: Filtra tipo_item_pdi (tinyint). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 0=Mercadoria para revenda, 1=Matéria-prima, 2=Produto intermediário, 3=Produto em fabricação, 4=Produto acabado, 5=Embalagem, 9=Serviços, 10=Outros insumos, 99=Outras (Tipo do item (0=Mercadoria/1=Materia Prima/2=Produto Intermediario/3=Produto em Fabricacao/4=Produto Acabado/5=Embalagem/9=Serviços/10=Outros insumos/99=Outros))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `produto_obter`

Produtos — obtém UM registro pela chave (codi_emp, codi_pdi) da tabela efprodutos. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use produto_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra codi_pdi (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Codigo)

## `produto_totais`

Produtos — TOTAIS por grupo da tabela efprodutos (módulo fiscal). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). CAMPOS SOMÁVEIS: valor_unitario, quantidade_inicial, valor_inicial, quantidade_final, valor_final. CAMPOS PARA AGRUPAR: codigo, descricao, grupo_codigo, unidade, ncm, ean, tipo, tipo_item, cst, aliquota_icms, aliquota_ipi. Os filtros são os mesmos de produto_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (tipo, tipo_item) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra codi_pdi (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Codigo)
- `descricao`: Filtra desc_pdi (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Descricao)
- `ncm`: Filtra cncm_pdi (char). Aceita: valor simples (igualdade), igual, {"prefixo":"x"}. (Nomenclatura Comum do Mercosul)
- `tipo`: Filtra tipo_pdi (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: V=Veículos novos, M=Medicamentos, A=Armas de fogo, O=Outros, C=Combustíveis, U=Comunicação, E=Energia elétrica, S=Veículos usados (Tipo(V=Veíc. Novos/M=Medicamentos/A=Armas Fogo/O=Outros/C=Combustíveis/U=Comunicação/E=Energ. Elétr./S=Veíc. Usados))
- `tipo_item`: Filtra tipo_item_pdi (tinyint). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 0=Mercadoria para revenda, 1=Matéria-prima, 2=Produto intermediário, 3=Produto em fabricação, 4=Produto acabado, 5=Embalagem, 9=Serviços, 10=Outros insumos, 99=Outras (Tipo do item (0=Mercadoria/1=Materia Prima/2=Produto Intermediario/3=Produto em Fabricacao/4=Produto Acabado/5=Embalagem/9=Serviços/10=Outros insumos/99=Outros))
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["tipo"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor_unitario"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `nota_saida_consultar`

Notas fiscais de saída — tabela efsaidas (módulo fiscal, ~513.113 linhas).
O QUE É: Cabeçalho das notas fiscais de saída (mercadorias e outras saídas) lançadas na escrita fiscal.
COMENTÁRIO DO BANCO SOBRE A TABELA: Notas Fiscais de Saida
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna dsai_sai. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: codigo, numero, serie, data_saida, data_emissao, competencia, cliente_codigo, acumulador_codigo, natureza_codigo, especie_codigo, uf, cancelada, situacao, chave_nfe, valor_contabil. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, numero, numero_final, serie, sub_serie, data_saida, data_emissao, competencia, valor_contabil, valor_produtos, valor_frete, valor_seguro, despesas_acessorias, valor_deducao, valor_excluido, cliente_codigo, acumulador_codigo, natureza_codigo, natureza_versao, especie_codigo, uf, municipio_codigo, situacao, cancelada, tipo_frete, chave_nfe, cfps, observacao, usuario, origem_registro. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): cliente_nome, cliente_cnpj_cpf, acumulador_nome, natureza_nome, especie_nome, especie_modelo, municipio_nome, municipio_ibge.
EXEMPLO COM DADOS: a empresa 1682 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): A apuração (apuracao_imposto) de cada imposto soma o valor contábil POR IMPOSTO (imposto_nota_saida.valor_contabil, com codigo_imposto = o do imposto), e não o valor_contabil do cabeçalho da nota: nota sem aquele imposto não entra na soma. Validado centavo a centavo (6 de 6 competências, empresa 1430, ICMS). | O mês de apuração é o de data_saida. A coluna competencia quase sempre vale 1900-01-01 (não informada) e não deve ser usada como período. | cancelada = 'S' marca a nota cancelada. situacao tem significado NÃO confirmado (ver domínio situacao_documento); não use situacao = 2 como sinônimo de cancelada.
POSSÍVEIS DADOS PESSOAIS/FINANCEIROS (os dados saem em claro; devolva só o que a pergunta exigir): usuario, cliente_cnpj_cpf.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo`: Filtra codi_sai (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `numero`: Filtra nume_sai (numeric). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Documento)
- `serie`: Filtra seri_sai (char). Aceita: valor simples (igualdade), igual. (Serie)
- `data_saida`: Filtra dsai_sai (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data de saida) Datas no formato AAAA-MM-DD.
- `data_emissao`: Filtra ddoc_sai (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data de emissao) Datas no formato AAAA-MM-DD.
- `competencia`: Filtra compte_sai (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}. (Competencia) Datas no formato AAAA-MM-DD.
- `cliente_codigo`: Filtra codi_cli (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Cliente)
- `acumulador_codigo`: Filtra codi_acu (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Acumulador)
- `natureza_codigo`: Filtra codi_nat (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Natureza)
- `especie_codigo`: Filtra codi_esp (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Especie)
- `uf`: Filtra sigl_est (char). Aceita: valor simples (igualdade), igual, lista de valores. (Estado)
- `cancelada`: Filtra cancelada_sai (char). Aceita: valor simples (igualdade), igual. Códigos: S=Sim, N=Não (Nota cancelada (S/N))
- `situacao`: Filtra situacao_sai (tinyint). Aceita: valor simples (igualdade), igual, lista de valores.  (Codigo do modelo do documento fiscal)
- `chave_nfe`: Filtra chave_nfe_sai (char). Aceita: valor simples (igualdade), igual. (Chave da nota fiscal eletrônica)
- `valor_contabil`: Filtra vcon_sai (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Valor contabil)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `nota_saida_obter`

Notas fiscais de saída — obtém UM registro pela chave (codi_emp, codi_sai) da tabela efsaidas. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use nota_saida_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra codi_sai (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `nota_saida_totais`

Notas fiscais de saída — TOTAIS por grupo da tabela efsaidas (módulo fiscal). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna dsai_sai. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor_contabil, valor_produtos, valor_frete, valor_seguro, despesas_acessorias, valor_deducao, valor_excluido. CAMPOS PARA AGRUPAR: codigo, numero, numero_final, serie, sub_serie, data_saida:mes, data_emissao:mes, competencia:mes, cliente_codigo, acumulador_codigo, natureza_codigo, natureza_versao, especie_codigo, uf, municipio_codigo, situacao, cancelada, tipo_frete, chave_nfe, cfps, observacao, usuario, origem_registro. Os filtros são os mesmos de nota_saida_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (situacao, cancelada, tipo_frete) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: A apuração (apuracao_imposto) de cada imposto soma o valor contábil POR IMPOSTO (imposto_nota_saida.valor_contabil, com codigo_imposto = o do imposto), e não o valor_contabil do cabeçalho da nota: nota sem aquele imposto não entra na soma. Validado centavo a centavo (6 de 6 competências, empresa 1430, ICMS). | O mês de apuração é o de data_saida. A coluna competencia quase sempre vale 1900-01-01 (não informada) e não deve ser usada como período. | cancelada = 'S' marca a nota cancelada. situacao tem significado NÃO confirmado (ver domínio situacao_documento); não use situacao = 2 como sinônimo de cancelada.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo`: Filtra codi_sai (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `numero`: Filtra nume_sai (numeric). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Documento)
- `serie`: Filtra seri_sai (char). Aceita: valor simples (igualdade), igual. (Serie)
- `data_saida`: Filtra dsai_sai (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data de saida) Datas no formato AAAA-MM-DD.
- `data_emissao`: Filtra ddoc_sai (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data de emissao) Datas no formato AAAA-MM-DD.
- `competencia`: Filtra compte_sai (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}. (Competencia) Datas no formato AAAA-MM-DD.
- `cliente_codigo`: Filtra codi_cli (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Cliente)
- `acumulador_codigo`: Filtra codi_acu (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Acumulador)
- `natureza_codigo`: Filtra codi_nat (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Natureza)
- `especie_codigo`: Filtra codi_esp (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Especie)
- `uf`: Filtra sigl_est (char). Aceita: valor simples (igualdade), igual, lista de valores. (Estado)
- `cancelada`: Filtra cancelada_sai (char). Aceita: valor simples (igualdade), igual. Códigos: S=Sim, N=Não (Nota cancelada (S/N))
- `situacao`: Filtra situacao_sai (tinyint). Aceita: valor simples (igualdade), igual, lista de valores.  (Codigo do modelo do documento fiscal)
- `chave_nfe`: Filtra chave_nfe_sai (char). Aceita: valor simples (igualdade), igual. (Chave da nota fiscal eletrônica)
- `valor_contabil`: Filtra vcon_sai (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Valor contabil)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["data_saida:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor_contabil"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `pagamento_nota_saida_consultar`

Recebimentos das notas de saída — tabela efsaidaspag (módulo fiscal, ~2.970 linhas).
O QUE É: Pagamentos/recebimentos (e juros, multas, descontos, retenções) lançados contra as parcelas.
COMENTÁRIO DO BANCO SOBRE A TABELA: Notas Fiscais de Saida - Pagamento das Parcelas
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna pgto_saip. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: codigo_nota, data_pagamento, tipo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo_nota, parcela, data_pagamento, tipo, numero_pagamento, valor, lancamento_contabil, origem_pagamento, numero_titulo, historico. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 1378 tem registros nesta tabela (use para testar).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_nota`: Filtra codi_sai (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Saida)
- `data_pagamento`: Filtra pgto_saip (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data do pagamento) Datas no formato AAAA-MM-DD.
- `tipo`: Filtra tipo_saip (tinyint). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Normal, 2=Juros, 3=Multa, 4=Desconto, 5=Devolução, 6=PIS, 7=COFINS, 8=CSLL, 9=IRRF, 11=PISOP, … (+9) (TIPO (1-NORMAL/ 2-JUROS/ 3-MULTA/ 4-DESCONTO/ 5-DEVOLUCAO/ 6-PIS/ 7-COFINS/ 8-CSLL/ 9-IRRF/ 11-PISOP/ 12-COFINSOP/ 13-CSLLOP/ 14-IRPJOP/ 15-IRRFP/ 16-JUROS VALOR PRESENTE/ 17-OUTRAS/ 18-PROFISSIONAL PARCEIRO/19 - ICMS ST/20-FETHAB))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `pagamento_nota_saida_totais`

Recebimentos das notas de saída — TOTAIS por grupo da tabela efsaidaspag (módulo fiscal). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna pgto_saip. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor, lancamento_contabil. CAMPOS PARA AGRUPAR: codigo_nota, parcela, data_pagamento:mes, tipo, numero_pagamento, origem_pagamento, numero_titulo, historico. Os filtros são os mesmos de pagamento_nota_saida_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (tipo, origem_pagamento) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_nota`: Filtra codi_sai (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Saida)
- `data_pagamento`: Filtra pgto_saip (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data do pagamento) Datas no formato AAAA-MM-DD.
- `tipo`: Filtra tipo_saip (tinyint). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Normal, 2=Juros, 3=Multa, 4=Desconto, 5=Devolução, 6=PIS, 7=COFINS, 8=CSLL, 9=IRRF, 11=PISOP, … (+9) (TIPO (1-NORMAL/ 2-JUROS/ 3-MULTA/ 4-DESCONTO/ 5-DEVOLUCAO/ 6-PIS/ 7-COFINS/ 8-CSLL/ 9-IRRF/ 11-PISOP/ 12-COFINSOP/ 13-CSLLOP/ 14-IRPJOP/ 15-IRRFP/ 16-JUROS VALOR PRESENTE/ 17-OUTRAS/ 18-PROFISSIONAL PARCEIRO/19 - ICMS ST/20-FETHAB))
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["data_pagamento:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `parcela_nota_saida_consultar`

Parcelas das notas de saída — tabela efsaidaspar (módulo fiscal, ~181.154 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: Notas Fiscais de Saida - Parcelas
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna vcto_saip. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: codigo_nota, vencimento. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo_nota, parcela, vencimento, valor, valor_bruto, tipo, valor_crf, valor_irrf, valor_iss_retido, valor_inss_retido, valor_pis_retido, valor_cofins_retido, valor_csll_retido, numero_titulo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 1507 tem registros nesta tabela (use para testar).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_nota`: Filtra codi_sai (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Saida)
- `vencimento`: Filtra vcto_saip (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data de vencimento da parcela) Datas no formato AAAA-MM-DD.
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `parcela_nota_saida_totais`

Parcelas das notas de saída — TOTAIS por grupo da tabela efsaidaspar (módulo fiscal). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna vcto_saip. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor, valor_bruto, valor_crf, valor_irrf, valor_iss_retido, valor_inss_retido, valor_pis_retido, valor_cofins_retido, valor_csll_retido. CAMPOS PARA AGRUPAR: codigo_nota, parcela, vencimento:mes, tipo, numero_titulo. Os filtros são os mesmos de parcela_nota_saida_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (tipo) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_nota`: Filtra codi_sai (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Saida)
- `vencimento`: Filtra vcto_saip (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data de vencimento da parcela) Datas no formato AAAA-MM-DD.
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["vencimento:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `apuracao_imposto_consultar`

Apuração de impostos (saldos) — tabela efsdoimp (módulo fiscal, ~791.318 linhas).
O QUE É: Saldo/apuração de cada imposto por competência e periodicidade: totais de entradas, saídas e serviços (valor contábil, base, imposto, isentas, outras), créditos, débitos, estornos e saldo a recolher/credor.
COMENTÁRIO DO BANCO SOBRE A TABELA: Saldo dos Impostos
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna data_sim. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: imposto_codigo, competencia, periodicidade. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: imposto_codigo, competencia, periodicidade, saldo_a_recolher, saldo_credor, entradas_valor_contabil, entradas_base_calculo, entradas_valor_imposto, entradas_isentas, entradas_outras, saidas_valor_contabil, saidas_base_calculo, saidas_valor_imposto, saidas_isentas, saidas_outras, servicos_valor_contabil, servicos_base_calculo, servicos_valor_imposto, servicos_isentas, servicos_outras, outros_creditos, estorno_debitos, outros_debitos, estorno_creditos, outras_deducoes, outros_acrescimos, base_acumulada_mes_anterior. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): imposto_nome, imposto_sigla.
EXEMPLO COM DADOS: a empresa 983 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Totais de entradas/saídas/serviços (…_valor_contabil) = soma de imposto_nota_*.valor_contabil do mesmo imposto no mês, pela data de movimento da nota. Conferido 6/6 competências nas três origens. | Os totais de 'entradas'/'saídas'/'serviços' são por imposto: o mesmo documento pode aparecer em vários impostos. Não some entre impostos diferentes.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `imposto_codigo`: Filtra codi_imp (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=ICMS, 2=IPI, 3=ISS, 4=PIS, 5=COFINS, 8=DIFALI, 9=Substituição Tributária, 16=IRRF, 18=ISS Retido, 22=PIS (Retido), … (+3) (Imposto)
- `competencia`: Filtra data_sim (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia) Datas no formato AAAA-MM-DD.
- `periodicidade`: Filtra pdic_sim (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=1º decêndio, 2=2º decêndio, 3=3º decêndio, 4=1ª quinzena, 5=2ª quinzena, 6=Mensal, 7=Trimestral, 11=1ª semana, 12=2ª semana, 13=3ª semana, … (+4) (Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `apuracao_imposto_obter`

Apuração de impostos (saldos) — obtém UM registro pela chave (codi_emp, codi_imp, data_sim, pdic_sim) da tabela efsdoimp. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use apuracao_imposto_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `imposto_codigo` (obrigatório): Filtra codi_imp (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=ICMS, 2=IPI, 3=ISS, 4=PIS, 5=COFINS, 8=DIFALI, 9=Substituição Tributária, 16=IRRF, 18=ISS Retido, 22=PIS (Retido), … (+3) (Imposto)
- `competencia` (obrigatório): Filtra data_sim (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia) Datas no formato AAAA-MM-DD.
- `periodicidade` (obrigatório): Filtra pdic_sim (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=1º decêndio, 2=2º decêndio, 3=3º decêndio, 4=1ª quinzena, 5=2ª quinzena, 6=Mensal, 7=Trimestral, 11=1ª semana, 12=2ª semana, 13=3ª semana, … (+4) (Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal))

## `apuracao_imposto_totais`

Apuração de impostos (saldos) — TOTAIS por grupo da tabela efsdoimp (módulo fiscal). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna data_sim. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: saldo_a_recolher, saldo_credor, entradas_valor_contabil, entradas_base_calculo, entradas_valor_imposto, saidas_valor_contabil, saidas_base_calculo, saidas_valor_imposto, servicos_valor_contabil, servicos_base_calculo, servicos_valor_imposto, outros_creditos, estorno_debitos, outros_debitos, estorno_creditos, outros_acrescimos. CAMPOS PARA AGRUPAR: imposto_codigo, competencia:mes, periodicidade, entradas_isentas, entradas_outras, saidas_isentas, saidas_outras, servicos_isentas, servicos_outras, outras_deducoes, base_acumulada_mes_anterior. Os filtros são os mesmos de apuracao_imposto_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (imposto_codigo, periodicidade) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Totais de entradas/saídas/serviços (…_valor_contabil) = soma de imposto_nota_*.valor_contabil do mesmo imposto no mês, pela data de movimento da nota. Conferido 6/6 competências nas três origens. | Os totais de 'entradas'/'saídas'/'serviços' são por imposto: o mesmo documento pode aparecer em vários impostos. Não some entre impostos diferentes.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `imposto_codigo`: Filtra codi_imp (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=ICMS, 2=IPI, 3=ISS, 4=PIS, 5=COFINS, 8=DIFALI, 9=Substituição Tributária, 16=IRRF, 18=ISS Retido, 22=PIS (Retido), … (+3) (Imposto)
- `competencia`: Filtra data_sim (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia) Datas no formato AAAA-MM-DD.
- `periodicidade`: Filtra pdic_sim (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=1º decêndio, 2=2º decêndio, 3=3º decêndio, 4=1ª quinzena, 5=2ª quinzena, 6=Mensal, 7=Trimestral, 11=1ª semana, 12=2ª semana, 13=3ª semana, … (+4) (Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal))
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["competencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["saldo_a_recolher"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `nota_servico_consultar`

Notas fiscais de serviço — tabela efservicos (módulo fiscal, ~585.771 linhas).
O QUE É: Notas fiscais de serviços prestados lançadas na escrita fiscal.
COMENTÁRIO DO BANCO SOBRE A TABELA: Notas Fiscais de Servico
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna dser_ser. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: codigo, numero, serie, data_servico, data_emissao, cliente_codigo, acumulador_codigo, especie_codigo, cancelada, situacao, chave_eletronica, valor_contabil. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, numero, numero_final, serie, sub_serie, data_servico, data_emissao, valor_contabil, valor_servicos, valor_desconto, valor_deducao, valor_ibs, valor_cbs, cliente_codigo, acumulador_codigo, especie_codigo, uf, municipio_codigo, situacao, cancelada, chave_eletronica, cfps, observacao, usuario, origem_registro. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): cliente_nome, cliente_cnpj_cpf, acumulador_nome, especie_nome, especie_modelo, municipio_nome, municipio_ibge.
EXEMPLO COM DADOS: a empresa 1484 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): A apuração do ISS soma imposto_nota_servico.valor_contabil (por imposto), validado centavo a centavo em 6 de 6 competências; somar o valor_contabil do cabeçalho divergiu em 1 de 6 (diferença de 5.299,00 por notas sem ISS). | O mês de apuração é o de data_servico (dser_ser).
POSSÍVEIS DADOS PESSOAIS/FINANCEIROS (os dados saem em claro; devolva só o que a pergunta exigir): usuario, cliente_cnpj_cpf.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo`: Filtra codi_ser (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `numero`: Filtra nume_ser (numeric). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Documento)
- `serie`: Filtra seri_ser (char). Aceita: valor simples (igualdade), igual. (Serie)
- `data_servico`: Filtra dser_ser (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data do servico) Datas no formato AAAA-MM-DD.
- `data_emissao`: Filtra ddoc_ser (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data de emissao) Datas no formato AAAA-MM-DD.
- `cliente_codigo`: Filtra codi_cli (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Cliente)
- `acumulador_codigo`: Filtra codi_acu (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Acumulador)
- `especie_codigo`: Filtra codi_esp (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Especie)
- `cancelada`: Filtra cancelada_ser (char). Aceita: valor simples (igualdade), igual. Códigos: S=Sim, N=Não (Nota cancelada(S/N))
- `situacao`: Filtra situacao_ser (tinyint). Aceita: valor simples (igualdade), igual, lista de valores.  (Codigo do modelo do documento fiscal)
- `chave_eletronica`: Filtra chave_eletronica (varchar). Aceita: valor simples (igualdade), igual. (Chave eletronica)
- `valor_contabil`: Filtra vcon_ser (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Valor contabil)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `nota_servico_obter`

Notas fiscais de serviço — obtém UM registro pela chave (codi_emp, codi_ser) da tabela efservicos. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use nota_servico_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra codi_ser (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `nota_servico_totais`

Notas fiscais de serviço — TOTAIS por grupo da tabela efservicos (módulo fiscal). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna dser_ser. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor_contabil, valor_servicos, valor_desconto, valor_deducao, valor_ibs, valor_cbs. CAMPOS PARA AGRUPAR: codigo, numero, numero_final, serie, sub_serie, data_servico:mes, data_emissao:mes, cliente_codigo, acumulador_codigo, especie_codigo, uf, municipio_codigo, situacao, cancelada, chave_eletronica, cfps, observacao, usuario, origem_registro. Os filtros são os mesmos de nota_servico_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (situacao, cancelada) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: A apuração do ISS soma imposto_nota_servico.valor_contabil (por imposto), validado centavo a centavo em 6 de 6 competências; somar o valor_contabil do cabeçalho divergiu em 1 de 6 (diferença de 5.299,00 por notas sem ISS). | O mês de apuração é o de data_servico (dser_ser).. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo`: Filtra codi_ser (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `numero`: Filtra nume_ser (numeric). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Documento)
- `serie`: Filtra seri_ser (char). Aceita: valor simples (igualdade), igual. (Serie)
- `data_servico`: Filtra dser_ser (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data do servico) Datas no formato AAAA-MM-DD.
- `data_emissao`: Filtra ddoc_ser (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data de emissao) Datas no formato AAAA-MM-DD.
- `cliente_codigo`: Filtra codi_cli (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Cliente)
- `acumulador_codigo`: Filtra codi_acu (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Acumulador)
- `especie_codigo`: Filtra codi_esp (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Especie)
- `cancelada`: Filtra cancelada_ser (char). Aceita: valor simples (igualdade), igual. Códigos: S=Sim, N=Não (Nota cancelada(S/N))
- `situacao`: Filtra situacao_ser (tinyint). Aceita: valor simples (igualdade), igual, lista de valores.  (Codigo do modelo do documento fiscal)
- `chave_eletronica`: Filtra chave_eletronica (varchar). Aceita: valor simples (igualdade), igual. (Chave eletronica)
- `valor_contabil`: Filtra vcon_ser (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Valor contabil)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["data_servico:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor_contabil"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `pagamento_nota_servico_consultar`

Recebimentos das notas de serviço — tabela efservicospag (módulo fiscal, ~215.111 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: Notas Fiscais de Servico - Pagamento das Parcelas
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna pgto_serp. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: codigo_nota, data_pagamento, tipo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo_nota, parcela, data_pagamento, tipo, numero_pagamento, valor, lancamento_contabil, origem_pagamento, numero_titulo, historico. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 623 tem registros nesta tabela (use para testar).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_nota`: Filtra codi_ser (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Servico)
- `data_pagamento`: Filtra pgto_serp (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data do pagamento) Datas no formato AAAA-MM-DD.
- `tipo`: Filtra tipo_serp (tinyint). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Normal, 2=Juros, 3=Multa, 4=Desconto, 5=Devolução, 6=PIS, 7=COFINS, 8=CSLL, 9=IRRF, 11=PISOP, … (+9) (TIPO (1-NORMAL/ 2-JUROS/ 3-MULTA/ 4-DESCONTO/ 5-DEVOLUCAO/ 6-PIS/ 7-COFINS/ 8-CSLL/ 9-IRRF/ 11-PISOP/ 12-COFINSOP/ 13-CSLLOP/ 14-IRPJOP/ 15-IRRFP/ 16-JUROS VALOR PRESENTE/ 17-OUTRAS/ 18-PROFISSIONAL PARCEIRO))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `pagamento_nota_servico_totais`

Recebimentos das notas de serviço — TOTAIS por grupo da tabela efservicospag (módulo fiscal). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna pgto_serp. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor, lancamento_contabil. CAMPOS PARA AGRUPAR: codigo_nota, parcela, data_pagamento:mes, tipo, numero_pagamento, origem_pagamento, numero_titulo, historico. Os filtros são os mesmos de pagamento_nota_servico_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (tipo, origem_pagamento) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_nota`: Filtra codi_ser (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Servico)
- `data_pagamento`: Filtra pgto_serp (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data do pagamento) Datas no formato AAAA-MM-DD.
- `tipo`: Filtra tipo_serp (tinyint). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Normal, 2=Juros, 3=Multa, 4=Desconto, 5=Devolução, 6=PIS, 7=COFINS, 8=CSLL, 9=IRRF, 11=PISOP, … (+9) (TIPO (1-NORMAL/ 2-JUROS/ 3-MULTA/ 4-DESCONTO/ 5-DEVOLUCAO/ 6-PIS/ 7-COFINS/ 8-CSLL/ 9-IRRF/ 11-PISOP/ 12-COFINSOP/ 13-CSLLOP/ 14-IRPJOP/ 15-IRRFP/ 16-JUROS VALOR PRESENTE/ 17-OUTRAS/ 18-PROFISSIONAL PARCEIRO))
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["data_pagamento:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `parcela_nota_servico_consultar`

Parcelas das notas de serviço — tabela efservicospar (módulo fiscal, ~115.341 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: Notas Fiscais de Servico - Parcelas
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna vcto_serp. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: codigo_nota, vencimento. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo_nota, parcela, vencimento, valor, valor_bruto, tipo, valor_crf, valor_irrf, valor_iss_retido, valor_inss_retido, valor_pis_retido, valor_cofins_retido, valor_csll_retido, numero_titulo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 985 tem registros nesta tabela (use para testar).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_nota`: Filtra codi_ser (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Servico)
- `vencimento`: Filtra vcto_serp (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vencimento da Parcela) Datas no formato AAAA-MM-DD.
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `parcela_nota_servico_totais`

Parcelas das notas de serviço — TOTAIS por grupo da tabela efservicospar (módulo fiscal). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna vcto_serp. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor, valor_bruto, valor_crf, valor_irrf, valor_iss_retido, valor_inss_retido, valor_pis_retido, valor_cofins_retido, valor_csll_retido. CAMPOS PARA AGRUPAR: codigo_nota, parcela, vencimento:mes, tipo, numero_titulo. Os filtros são os mesmos de parcela_nota_servico_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (tipo) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo_nota`: Filtra codi_ser (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Servico)
- `vencimento`: Filtra vcto_serp (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vencimento da Parcela) Datas no formato AAAA-MM-DD.
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["vencimento:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `imposto_consultar`

Impostos (cadastro por empresa) — tabela geimposto (módulo fiscal, ~272.150 linhas).
O QUE É: Cadastro de impostos por empresa. O código (codi_imp) tem o mesmo significado em todas as empresas.
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, nome. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, nome, sigla, nome_resumido. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 374 tem registros nesta tabela (use para testar).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra codi_imp (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=ICMS, 2=IPI, 3=ISS, 4=PIS, 5=COFINS, 8=DIFALI, 9=Substituição Tributária, 16=IRRF, 18=ISS Retido, 22=PIS (Retido), … (+3) (Codigo)
- `nome`: Filtra nome_imp (varchar). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}. (Nome)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `imposto_obter`

Impostos (cadastro por empresa) — obtém UM registro pela chave (codi_emp, codi_imp) da tabela geimposto. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use imposto_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra codi_imp (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=ICMS, 2=IPI, 3=ISS, 4=PIS, 5=COFINS, 8=DIFALI, 9=Substituição Tributária, 16=IRRF, 18=ISS Retido, 22=PIS (Retido), … (+3) (Codigo)
