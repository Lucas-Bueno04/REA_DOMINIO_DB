# Módulo `honorarios`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `classificacao_cliente_consultar` | consultar | hrclassificacao | — | ✔ |
| `classificacao_cliente_obter` | obter | hrclassificacao | codigo | ✔ |
| `cliente_honorarios_consultar` | consultar | hrcliente | empresa | ✔ |
| `cliente_honorarios_obter` | obter | hrcliente | empresa, codigo | ✔ |
| `conta_corrente_cliente_consultar` | consultar | hrconta_corrente_cliente | empresa | ✔ |
| `conta_corrente_cliente_totais` | totais | hrconta_corrente_cliente | empresa | ✔ |
| `conta_corrente_escritorio_consultar` | consultar | hrconta_corrente_escritorio | empresa | ✔ |
| `conta_corrente_escritorio_totais` | totais | hrconta_corrente_escritorio | empresa | ✔ |
| `conta_financeira_consultar` | consultar | hrconta_financeira | empresa | ✔ |
| `conta_financeira_obter` | obter | hrconta_financeira | empresa, codigo | ✔ |
| `contrato_consultar` | consultar | hrcontrato | empresa | ✔ |
| `contrato_obter` | obter | hrcontrato | empresa, codigo | ✔ |
| `contrato_totais` | totais | hrcontrato | empresa | ✔ |
| `evento_honorario_consultar` | consultar | hrevento | empresa | ✔ |
| `evento_honorario_obter` | obter | hrevento | empresa, codigo | ✔ |
| `faturamento_consultar` | consultar | hrfaturamento | empresa | ✔ |
| `faturamento_obter` | obter | hrfaturamento | empresa, codigo | ✔ |
| `faturamento_totais` | totais | hrfaturamento | empresa | ✔ |
| `parcela_faturamento_consultar` | consultar | hrfaturamento_parcela | empresa | ✔ |
| `item_parcela_consultar` | consultar | hrfaturamento_parcela_item | empresa | ✔ |
| `item_parcela_totais` | totais | hrfaturamento_parcela_item | empresa | ✔ |
| `nfse_consultar` | consultar | hrnota_nfse | empresa | ✔ |
| `recebimento_consultar` | consultar | hrrecebimento | empresa | ✔ |
| `recebimento_totais` | totais | hrrecebimento | empresa | ✔ |
| `item_recebimento_consultar` | consultar | hrrecebimento_item | empresa | ✔ |
| `item_recebimento_totais` | totais | hrrecebimento_item | empresa | ✔ |

## `classificacao_cliente_consultar`

Classificações de cliente — tabela hrclassificacao (módulo honorarios, ~3 linhas).
O QUE É: Tabela global (3 linhas).
COMENTÁRIO DO BANCO SOBRE A TABELA: Classificacoes
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
Tabela global (não depende de empresa): NÃO informe 'empresa'.
FILTROS: codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, descricao. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
UTILIDADE LIMITADA: a tabela expõe só 2 campo(s) (tabela de apoio/ligação); ela NÃO traz o conteúdo que o nome pode sugerir (XML, arquivo, etc.).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `codigo`: Filtra I_CLASSIFICACAO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `classificacao_cliente_obter`

Classificações de cliente — obtém UM registro pela chave (I_CLASSIFICACAO) da tabela hrclassificacao. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use classificacao_cliente_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `codigo` (obrigatório): Filtra I_CLASSIFICACAO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `cliente_honorarios_consultar`

Clientes de honorários — tabela hrcliente (módulo honorarios, ~2.918 linhas).
O QUE É: Clientes que o escritório fatura. `empresa` = ESCRITÓRIO. Fixos (tipo F) ligam à empresa cadastrada por `empresa_cliente_codigo` (= geempre.codi_emp). Contatos e observações livres não são expostos.
COMENTÁRIO DO BANCO SOBRE A TABELA: Clientes Fixos e Eventuais
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, nome, tipo, inscricao, empresa_cliente_codigo, uf. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, apelido, nome, tipo, empresa_cliente_codigo, data_cadastro, tipo_inscricao, inscricao, municipio_codigo, uf, regime_federal, classificacao_codigo, conta_contabil, gera_contabilizacao. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): classificacao_nome, empresa_cliente_nome.
EXEMPLO COM DADOS: a empresa 1 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Cliente fixo (F): empresa_cliente_codigo existe em geempre em 100% dos casos (1.644 de 1.644). Cliente eventual (E): sem empresa cadastrada. | Dois escritórios no banco (códigos 1 e 930): sempre filtre `empresa` pelo escritório desejado.
PRIVACIDADE: 1.141 clientes são pessoas físicas (CPF). Nome e inscrição mascarados por padrão.
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): nome, inscricao
POSSÍVEIS DADOS PESSOAIS/FINANCEIROS (os dados saem em claro; devolva só o que a pergunta exigir): classificacao_nome, empresa_cliente_nome.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra I_CLIENTE (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `nome`: Filtra NOME (varchar). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Nome)
- `tipo`: Filtra TIPO (char). Aceita: valor simples (igualdade), igual. Códigos: F=Fixo (empresa cadastrada), E=Eventual (Tipo F Fixo E Eventual)
- `inscricao`: Filtra INSCRICAO (varchar). Aceita: valor simples (igualdade), igual. (Inscricao)
- `empresa_cliente_codigo`: Filtra I_CLIENTE_FIXO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo do cliente fixo)
- `uf`: Filtra UF (char). Aceita: valor simples (igualdade), igual, lista de valores. (UF)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `cliente_honorarios_obter`

Clientes de honorários — obtém UM registro pela chave (codi_emp, i_cliente) da tabela hrcliente. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use cliente_honorarios_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra I_CLIENTE (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `conta_corrente_cliente_consultar`

Conta corrente do cliente — tabela hrconta_corrente_cliente (módulo honorarios, ~88.987 linhas).
O QUE É: Razão do cliente: faturamento entra (E, origem F), pagamento/adiantamento sai (S). Cada movimento principal (P) pode ter desdobramentos (juros e multa, desconto, retenções) pelo sequencial.
COMENTÁRIO DO BANCO SOBRE A TABELA: Conta corente do cliente
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DATA_MOVIMENTO. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: cliente_codigo, data, tipo, origem, detalhe. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: movimento, sequencial, detalhe, cliente_codigo, data, tipo, origem, valor, historico. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): cliente_nome.
EXEMPLO COM DADOS: a empresa 1 tem registros nesta tabela (use para testar).
PRIVACIDADE: Movimentação financeira por cliente. Os dados saem em claro nesta versão do servidor: devolva só o que a pergunta exigir.
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): valor
POSSÍVEIS DADOS PESSOAIS/FINANCEIROS (os dados saem em claro; devolva só o que a pergunta exigir): cliente_nome.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `cliente_codigo`: Filtra I_CLIENTE (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Cliente)
- `data`: Filtra DATA_MOVIMENTO (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data) Datas no formato AAAA-MM-DD.
- `tipo`: Filtra TIPO (char). Aceita: valor simples (igualdade), igual. Códigos: E=Entrada, S=Saída, T=Transferência (Tipo E Entrada S Saida)
- `origem`: Filtra ORIGEM (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: F=Faturamento, P=Pagamento, A=Adiantamento, C=Cancelamento de nota fiscal, E=Pago pelo escritório, R=Renegociação (ORIGEM (F=FATURAMENTO/ P=PAGAMENTO/ A=ADIANTAMENTO/ C=CANCELAMENTO DE NOTA FISCAL/ E=PAGO PELO ESCRITORIO/ R=RENEGOCIAÇÃO))
- `detalhe`: Filtra DETALHE (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: P=Principal, J=Juros e multa, D=Desconto, R=Retenções, U=Juros, M=Multa (DETALHE DO MOVIMENTO (P=PRINCIPAL/ J=JUROS E MULTA/ D=DESCONTO/ R=RETENCOES/ U=JUROS/ M=MULTA))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `conta_corrente_cliente_totais`

Conta corrente do cliente — TOTAIS por grupo da tabela hrconta_corrente_cliente (módulo honorarios). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DATA_MOVIMENTO. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor. CAMPOS PARA AGRUPAR: movimento, sequencial, detalhe, cliente_codigo, data:mes, tipo, origem, historico. Os filtros são os mesmos de conta_corrente_cliente_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (detalhe, tipo, origem) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `cliente_codigo`: Filtra I_CLIENTE (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Cliente)
- `data`: Filtra DATA_MOVIMENTO (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data) Datas no formato AAAA-MM-DD.
- `tipo`: Filtra TIPO (char). Aceita: valor simples (igualdade), igual. Códigos: E=Entrada, S=Saída, T=Transferência (Tipo E Entrada S Saida)
- `origem`: Filtra ORIGEM (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: F=Faturamento, P=Pagamento, A=Adiantamento, C=Cancelamento de nota fiscal, E=Pago pelo escritório, R=Renegociação (ORIGEM (F=FATURAMENTO/ P=PAGAMENTO/ A=ADIANTAMENTO/ C=CANCELAMENTO DE NOTA FISCAL/ E=PAGO PELO ESCRITORIO/ R=RENEGOCIAÇÃO))
- `detalhe`: Filtra DETALHE (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: P=Principal, J=Juros e multa, D=Desconto, R=Retenções, U=Juros, M=Multa (DETALHE DO MOVIMENTO (P=PRINCIPAL/ J=JUROS E MULTA/ D=DESCONTO/ R=RETENCOES/ U=JUROS/ M=MULTA))
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["data:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `conta_corrente_escritorio_consultar`

Conta corrente do escritório — tabela hrconta_corrente_escritorio (módulo honorarios, ~65.980 linhas).
O QUE É: Razão financeiro do próprio escritório (recebimentos, pagamentos a fornecedores, impostos, funcionários, transferências).
COMENTÁRIO DO BANCO SOBRE A TABELA: Conta corrente do escritorio
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DATA_MOVIMENTO. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: data, tipo, origem. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: movimento, data, tipo, origem, valor, conta_origem_codigo, conta_destino_codigo, categoria_receber_codigo, categoria_pagar_codigo, historico. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 1 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Movimento de recebimento (origem R) registra o valor BRUTO recebido (igual a hrrecebimento.valor_recebido em 98,3%).
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): valor
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `data`: Filtra DATA_MOVIMENTO (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data) Datas no formato AAAA-MM-DD.
- `tipo`: Filtra TIPO (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: E=Entrada, S=Saída, T=Transferência (Tipo E Entrada S Saida T Transferencia)
- `origem`: Filtra ORIGEM (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: M=Manual, F=Pagamento a fornecedor, I=Pagamento de imposto, P=Pagamento de funcionário, C=Pagamento de item para cliente, R=Recebimento, A=Adiantamento, H=Cheque, X=Extrato bancário (Origem - M-Manual/F-Pagamento fornecedor/I-Pagamento imposto/P-Pagamento funcionario/C-Pagamento de item para cliente/R-Recebimento/A-Adiantamento/H-Cheque/X-Extrato Bancário)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `conta_corrente_escritorio_totais`

Conta corrente do escritório — TOTAIS por grupo da tabela hrconta_corrente_escritorio (módulo honorarios). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DATA_MOVIMENTO. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor. CAMPOS PARA AGRUPAR: movimento, data:mes, tipo, origem, conta_origem_codigo, conta_destino_codigo, categoria_receber_codigo, categoria_pagar_codigo, historico. Os filtros são os mesmos de conta_corrente_escritorio_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (tipo, origem) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Movimento de recebimento (origem R) registra o valor BRUTO recebido (igual a hrrecebimento.valor_recebido em 98,3%).. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `data`: Filtra DATA_MOVIMENTO (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data) Datas no formato AAAA-MM-DD.
- `tipo`: Filtra TIPO (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: E=Entrada, S=Saída, T=Transferência (Tipo E Entrada S Saida T Transferencia)
- `origem`: Filtra ORIGEM (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: M=Manual, F=Pagamento a fornecedor, I=Pagamento de imposto, P=Pagamento de funcionário, C=Pagamento de item para cliente, R=Recebimento, A=Adiantamento, H=Cheque, X=Extrato bancário (Origem - M-Manual/F-Pagamento fornecedor/I-Pagamento imposto/P-Pagamento funcionario/C-Pagamento de item para cliente/R-Recebimento/A-Adiantamento/H-Cheque/X-Extrato Bancário)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["data:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `conta_financeira_consultar`

Contas financeiras do escritório — tabela hrconta_financeira (módulo honorarios, ~24 linhas).
O QUE É: Bancos e caixas do escritório (24 linhas). Número da conta, agência e convênio não são expostos.
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, tipo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, descricao, tipo, banco_codigo, conta_contabil, envia_cobranca_registrada. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 930 tem registros nesta tabela (use para testar).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra I_CONTA_FINANCEIRA (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `tipo`: Filtra TIPO (char). Aceita: valor simples (igualdade), igual. Códigos: B=Bancária, C=Caixa, H=Cheque (TIPO (B=BANCARIA/C=CAIXA/H=CHEQUE))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `conta_financeira_obter`

Contas financeiras do escritório — obtém UM registro pela chave (codi_emp, I_CONTA_FINANCEIRA) da tabela hrconta_financeira. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use conta_financeira_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra I_CONTA_FINANCEIRA (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `contrato_consultar`

Contratos de honorários — tabela hrcontrato (módulo honorarios, ~1.064 linhas).
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, cliente_codigo, evento_codigo, data_inicio, data_termino. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, descricao, cliente_codigo, tipo_contrato_codigo, evento_codigo, data_emissao, data_inicio, data_inicio_faturamento, dia_vencimento, mes_vencimento, define_termino, data_termino, valor_contrato, valor_original. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): cliente_nome, evento_descricao.
EXEMPLO COM DADOS: a empresa 1 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): 583 contratos não têm término definido e 481 têm; destes, nenhum está vigente (todos encerrados).
PRIVACIDADE: Valor contratado por cliente (financeiro).
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): valor_contrato, valor_original
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra I_CONTRATO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `cliente_codigo`: Filtra I_CLIENTE (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Cliente)
- `evento_codigo`: Filtra I_EVENTO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Evento honorarios)
- `data_inicio`: Filtra DATA_INICIO (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Inicio do contrato) Datas no formato AAAA-MM-DD.
- `data_termino`: Filtra DATA_TERMINO (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data de termino) Datas no formato AAAA-MM-DD.
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `contrato_obter`

Contratos de honorários — obtém UM registro pela chave (codi_emp, I_CONTRATO) da tabela hrcontrato. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use contrato_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra I_CONTRATO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `contrato_totais`

Contratos de honorários — TOTAIS por grupo da tabela hrcontrato (módulo honorarios). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). CAMPOS SOMÁVEIS: valor_contrato, valor_original. CAMPOS PARA AGRUPAR: codigo, descricao, cliente_codigo, tipo_contrato_codigo, evento_codigo, data_emissao:mes, data_inicio:mes, data_inicio_faturamento:mes, dia_vencimento, mes_vencimento, define_termino, data_termino:mes. Os filtros são os mesmos de contrato_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (mes_vencimento, define_termino) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: 583 contratos não têm término definido e 481 têm; destes, nenhum está vigente (todos encerrados).. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra I_CONTRATO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `cliente_codigo`: Filtra I_CLIENTE (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Cliente)
- `evento_codigo`: Filtra I_EVENTO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Evento honorarios)
- `data_inicio`: Filtra DATA_INICIO (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Inicio do contrato) Datas no formato AAAA-MM-DD.
- `data_termino`: Filtra DATA_TERMINO (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data de termino) Datas no formato AAAA-MM-DD.
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["data_emissao:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor_contrato"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `evento_honorario_consultar`

Eventos de honorário (tipos de cobrança) — tabela hrevento (módulo honorarios, ~89 linhas).
O QUE É: Catálogo de serviços/cobranças do escritório (89 linhas) com as marcações de impostos retidos.
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, descricao. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, descricao, data_cadastro, unidade, referencia, categoria_codigo, imposto_codigo, soma_irrf, aliquota_irrf, soma_iss, aliquota_iss, dia_vencimento, mes_vencimento, fatura_contrato. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 1 tem registros nesta tabela (use para testar).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra I_EVENTO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `descricao`: Filtra DESCRICAO (varchar). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Descricao)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `evento_honorario_obter`

Eventos de honorário (tipos de cobrança) — obtém UM registro pela chave (codi_emp, I_EVENTO) da tabela hrevento. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use evento_honorario_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra I_EVENTO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `faturamento_consultar`

Faturamentos — tabela hrfaturamento (módulo honorarios, ~43.194 linhas).
O QUE É: Cabeçalho de cada faturamento de honorários (um por cliente e competência).
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DATA_FATURAMENTO. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: codigo, cliente_codigo, competencia, data_faturamento, tipo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, cliente_codigo, competencia, data_faturamento, tipo, somente_vencimento, gerar_parcelado, quantidade_parcelas, intervalo_dias, nota_fiscal_codigo, nfse_codigo, usuario, data_hora. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): cliente_nome.
EXEMPLO COM DADOS: a empresa 1 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Faturamentos de 2015-09 a 2025-12; não há nada em 2026.
POSSÍVEIS DADOS PESSOAIS/FINANCEIROS (os dados saem em claro; devolva só o que a pergunta exigir): usuario.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo`: Filtra I_FATURAMENTO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `cliente_codigo`: Filtra I_CLIENTE (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Cliente)
- `competencia`: Filtra COMPETENCIA (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Compentecia) Datas no formato AAAA-MM-DD.
- `data_faturamento`: Filtra DATA_FATURAMENTO (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data do faturamento) Datas no formato AAAA-MM-DD.
- `tipo`: Filtra TIPO_FATURAMENTO (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: T=Todos, C=Contratos e eventos com contrato, E=Eventos sem contrato (Tipo de faturamento T Todos C Contratos e eventos com contrato E Eventos sem contrato)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `faturamento_obter`

Faturamentos — obtém UM registro pela chave (codi_emp, I_FATURAMENTO) da tabela hrfaturamento. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use faturamento_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra I_FATURAMENTO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)

## `faturamento_totais`

Faturamentos — TOTAIS por grupo da tabela hrfaturamento (módulo honorarios). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DATA_FATURAMENTO. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: quantidade_parcelas, intervalo_dias. CAMPOS PARA AGRUPAR: codigo, cliente_codigo, competencia:mes, data_faturamento:mes, tipo, somente_vencimento, gerar_parcelado, nota_fiscal_codigo, nfse_codigo, usuario, data_hora:mes. Os filtros são os mesmos de faturamento_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (tipo, somente_vencimento, gerar_parcelado) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Faturamentos de 2015-09 a 2025-12; não há nada em 2026.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo`: Filtra I_FATURAMENTO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `cliente_codigo`: Filtra I_CLIENTE (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Cliente)
- `competencia`: Filtra COMPETENCIA (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Compentecia) Datas no formato AAAA-MM-DD.
- `data_faturamento`: Filtra DATA_FATURAMENTO (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data do faturamento) Datas no formato AAAA-MM-DD.
- `tipo`: Filtra TIPO_FATURAMENTO (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: T=Todos, C=Contratos e eventos com contrato, E=Eventos sem contrato (Tipo de faturamento T Todos C Contratos e eventos com contrato E Eventos sem contrato)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["competencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["quantidade_parcelas"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `parcela_faturamento_consultar`

Parcelas de faturamento — tabela hrfaturamento_parcela (módulo honorarios, ~43.224 linhas).
O QUE É: Vencimentos de cada faturamento, com o estado de emissão de boleto e de documento de cobrança. O valor da parcela é a soma dos itens (item_parcela); o recebido é a soma de recebimento.valor. Para o saldo pronto use a consulta `contas_a_receber`.
COMENTÁRIO DO BANCO SOBRE A TABELA: Faturamento - Parcelas
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna VENCIMENTO. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: faturamento_codigo, vencimento, imprimiu_boleto. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: faturamento_codigo, parcela, vencimento, vencimento_original, imprimiu_boleto, emissao_boleto, nosso_numero_boleto, conta_financeira_boleto, tipo_boleto, imprimiu_cobranca, numero_cobranca, emissao_cobranca. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): cliente_codigo, faturamento_competencia, faturamento_data.
EXEMPLO COM DADOS: a empresa 1 tem registros nesta tabela (use para testar).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `faturamento_codigo`: Filtra I_FATURAMENTO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Faturamento)
- `vencimento`: Filtra VENCIMENTO (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data de vencimento) Datas no formato AAAA-MM-DD.
- `imprimiu_boleto`: Filtra IMPRIMIU_BOLETO (char). Aceita: valor simples (igualdade), igual. Códigos: S=Sim, N=Não (Imprimiu boleto S N)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `item_parcela_consultar`

Itens das parcelas — tabela hrfaturamento_parcela_item (módulo honorarios, ~43.766 linhas).
O QUE É: Cada evento (honorário) cobrado em uma parcela, com valores, descontos e retenções (IRRF, ISS, INSS, CRF).
COMENTÁRIO DO BANCO SOBRE A TABELA: Faturamento - Parcelas - Itens
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): faturamento_codigo.
FILTROS: faturamento_codigo, evento_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: faturamento_codigo, parcela, evento_codigo, pago_pelo_escritorio, valor, valor_original, valor_desconto, valor_irrf, aliquota_irrf, valor_iss, aliquota_iss, valor_iss_retido, valor_inss_retido, valor_crf, movimento_cliente_codigo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): evento_descricao, parcela_vencimento.
EXEMPLO COM DADOS: a empresa 1 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Valor do movimento da conta corrente do cliente = valor do item em 99,6% dos itens (43.594 de 43.766; 172 itens sem movimento). | valor é o valor cobrado do item; a soma dos itens de uma parcela é o valor faturado dela.
PRIVACIDADE: Valores cobrados por cliente (financeiro).
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): valor, valor_original, valor_desconto, valor_irrf, valor_iss, valor_iss_retido, valor_inss_retido, valor_crf
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `faturamento_codigo`: Filtra I_FATURAMENTO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Faturamento)
- `evento_codigo`: Filtra I_EVENTO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Evento)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `item_parcela_totais`

Itens das parcelas — TOTAIS por grupo da tabela hrfaturamento_parcela_item (módulo honorarios). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): faturamento_codigo. CAMPOS SOMÁVEIS: valor, valor_original, valor_desconto, valor_irrf, valor_iss, valor_iss_retido, valor_inss_retido, valor_crf. CAMPOS PARA AGRUPAR: faturamento_codigo, parcela, evento_codigo, pago_pelo_escritorio, aliquota_irrf, aliquota_iss, movimento_cliente_codigo. Os filtros são os mesmos de item_parcela_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (pago_pelo_escritorio) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Valor do movimento da conta corrente do cliente = valor do item em 99,6% dos itens (43.594 de 43.766; 172 itens sem movimento). | valor é o valor cobrado do item; a soma dos itens de uma parcela é o valor faturado dela.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `faturamento_codigo`: Filtra I_FATURAMENTO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Faturamento)
- `evento_codigo`: Filtra I_EVENTO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Evento)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["pago_pelo_escritorio"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `nfse_consultar`

Notas fiscais de serviço eletrônicas emitidas pelo escritório — tabela hrnota_nfse (módulo honorarios, ~36.496 linhas).
O QUE É: NFS-e do escritório aos clientes. Observação livre e CNAE não são expostos.
COMENTÁRIO DO BANCO SOBRE A TABELA: Notas fiscais de servico eletronica emitidas
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna EMISSAO_NFSE. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: numero_nfse, cliente_codigo, emissao, cancelada. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, cliente_codigo, numero_rps, lote_codigo, numero_nfse, codigo_verificacao, emissao, hora_emissao, cancelada, data_cancelamento, aliquota, serie, municipio_prestacao_codigo, usuario. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): cliente_nome.
EXEMPLO COM DADOS: a empresa 1 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Emissões de 2018-03-20 a 2025-04-16: 36.426 válidas e 70 canceladas. Não há NFS-e emitida por este módulo depois de 2025-04.
POSSÍVEIS DADOS PESSOAIS/FINANCEIROS (os dados saem em claro; devolva só o que a pergunta exigir): usuario.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `numero_nfse`: Filtra NUMERO_NFSE (numeric). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Numero da nota fiscal)
- `cliente_codigo`: Filtra I_CLIENTE (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Cliente)
- `emissao`: Filtra EMISSAO_NFSE (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data de emissao da nota fiscal) Datas no formato AAAA-MM-DD.
- `cancelada`: Filtra CANCELADA_NOTA_NFSE (char). Aceita: valor simples (igualdade), igual. Códigos: S=Sim, N=Não (Nota fiscal cancelada (S/N))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `recebimento_consultar`

Recebimentos — tabela hrrecebimento (módulo honorarios, ~43.042 linhas).
O QUE É: Baixas de parcelas. `valor_recebido` é o BRUTO (inclui juros e multa); `valor` é o LÍQUIDO que abate o principal da parcela. Identidade validada em 100%: valor = valor_recebido − juros − multa + desconto.
COMENTÁRIO DO BANCO SOBRE A TABELA: Recebimento de contas a receber
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DATA_RECEBIMENTO. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: faturamento_codigo, data_recebimento, origem, conta_financeira_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: faturamento_codigo, parcela, recebimento, data_recebimento, origem, conta_financeira_codigo, movimento_escritorio_codigo, valor_liquido, valor_recebido, valor_juros, valor_multa, valor_desconto, valor_irrf, valor_crf, valor_refaturado, valor_reparcelado, valor_quitado, historico. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): conta_financeira_descricao, cliente_codigo, faturamento_competencia.
EXEMPLO COM DADOS: a empresa 1 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Identidade: valor_liquido = valor_recebido − valor_juros − valor_multa + valor_desconto, em 43.042 de 43.042 recebimentos (100%) e 43.581 de 43.603 itens (99,95%). | O valor_recebido do recebimento é igual à soma dos itens em 99,95% (43.019 de 43.042); o valor_liquido em 99,998%. | O movimento do escritório ligado tem valor igual a valor_recebido em 98,3% (42.295 de 43.042; 746 recebimentos sem movimento) — o movimento registra o BRUTO, não o líquido. | Para saber o que ainda está em aberto use a consulta `contas_a_receber`: saldo da parcela = Σ valor dos itens − Σ valor_liquido dos recebimentos. Validado: 42.824 parcelas quitadas, 399 em aberto e 1 inconsistente (99,998%). Somar também desconto/quitado/refaturado/reparcelado produz 588 'baixadas a mais' artificiais.
PRIVACIDADE: Valores recebidos por cliente (financeiro).
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): valor_liquido, valor_recebido, valor_juros, valor_multa, valor_desconto, valor_irrf, valor_crf, valor_refaturado, valor_reparcelado, valor_quitado
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `faturamento_codigo`: Filtra I_FATURAMENTO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Faturamento)
- `data_recebimento`: Filtra DATA_RECEBIMENTO (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data do recebimento) Datas no formato AAAA-MM-DD.
- `origem`: Filtra ORIGEM (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: D=Individual, G=Em grupo, R=Renegociação - recebimento, P=Renegociação - reparcelada, Q=Renegociação - quitada, N=Renegociação - novo faturamento, A=Adiantamento, F=Faturamento, I=Consulta de faturamento integral, E=Consulta de faturamento por evento, […]
- `conta_financeira_codigo`: Filtra I_CONTA_FINANCEIRA (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta financeira)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `recebimento_totais`

Recebimentos — TOTAIS por grupo da tabela hrrecebimento (módulo honorarios). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DATA_RECEBIMENTO. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor_liquido, valor_recebido, valor_juros, valor_multa, valor_desconto, valor_irrf, valor_crf, valor_refaturado, valor_reparcelado, valor_quitado. CAMPOS PARA AGRUPAR: faturamento_codigo, parcela, recebimento, data_recebimento:mes, origem, conta_financeira_codigo, movimento_escritorio_codigo, historico. Os filtros são os mesmos de recebimento_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (origem) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Identidade: valor_liquido = valor_recebido − valor_juros − valor_multa + valor_desconto, em 43.042 de 43.042 recebimentos (100%) e 43.581 de 43.603 itens (99,95%). | O valor_recebido do recebimento é igual à soma dos itens em 99,95% (43.019 de 43.042); o valor_liquido em 99,998%. | O movimento do escritório ligado tem valor igual a valor_recebido em 98,3% (42.295 de 43.042; 746 recebimentos sem movimento) — o movimento registra o BRUTO, não o líquido. | Para saber o que ainda está em aberto use a consulta `contas_a_receber`: saldo da parcela = Σ valor dos itens − Σ valor_liquido dos recebimentos. Validado: 42.824 parcelas quitadas, 399 em aberto e 1 inconsistente (99,998%). Somar também desconto/quitado/refaturado/reparcelado produz 588 'baixadas a mais' artificiais.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `faturamento_codigo`: Filtra I_FATURAMENTO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Faturamento)
- `data_recebimento`: Filtra DATA_RECEBIMENTO (date). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data do recebimento) Datas no formato AAAA-MM-DD.
- `origem`: Filtra ORIGEM (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: D=Individual, G=Em grupo, R=Renegociação - recebimento, P=Renegociação - reparcelada, Q=Renegociação - quitada, N=Renegociação - novo faturamento, A=Adiantamento, F=Faturamento, I=Consulta de faturamento integral, E=Consulta de faturamento por evento, […]
- `conta_financeira_codigo`: Filtra I_CONTA_FINANCEIRA (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta financeira)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["data_recebimento:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor_liquido"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `item_recebimento_consultar`

Itens dos recebimentos — tabela hrrecebimento_item (módulo honorarios, ~43.603 linhas).
O QUE É: Rateio de cada recebimento pelos eventos (itens) da parcela.
COMENTÁRIO DO BANCO SOBRE A TABELA: Recebimento de contas a receber - Itens
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): faturamento_codigo.
FILTROS: faturamento_codigo, evento_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: faturamento_codigo, parcela, recebimento, evento_codigo, pago_pelo_escritorio, valor_liquido, valor_recebido, valor_juros, valor_multa, valor_desconto. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): evento_descricao.
EXEMPLO COM DADOS: a empresa 1 tem registros nesta tabela (use para testar).
PRIVACIDADE: Valores recebidos por cliente (financeiro).
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): valor_liquido, valor_recebido, valor_juros, valor_multa, valor_desconto
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `faturamento_codigo`: Filtra I_FATURAMENTO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Faturamento)
- `evento_codigo`: Filtra I_EVENTO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Evento)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `item_recebimento_totais`

Itens dos recebimentos — TOTAIS por grupo da tabela hrrecebimento_item (módulo honorarios). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): faturamento_codigo. CAMPOS SOMÁVEIS: valor_liquido, valor_recebido, valor_juros, valor_multa, valor_desconto. CAMPOS PARA AGRUPAR: faturamento_codigo, parcela, recebimento, evento_codigo, pago_pelo_escritorio. Os filtros são os mesmos de item_recebimento_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (pago_pelo_escritorio) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `faturamento_codigo`: Filtra I_FATURAMENTO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Faturamento)
- `evento_codigo`: Filtra I_EVENTO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Evento)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["pago_pelo_escritorio"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor_liquido"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).
