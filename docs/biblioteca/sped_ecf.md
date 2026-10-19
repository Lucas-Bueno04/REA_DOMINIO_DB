# Módulo `sped_ecf`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `ecf_outros_dados_consultar` | consultar | ctsped_ecf_od | empresa | ✔ |
| `ecf_outros_dados_obter` | obter | ctsped_ecf_od | empresa, codigo | ✔ |
| `valor_mes_registro_ecf_consultar` | consultar | ctsped_ecf_od_mes | empresa | ✔ |
| `valor_mes_registro_ecf_obter` | obter | ctsped_ecf_od_mes | empresa, outros_dados, registro, mes | ✔ |
| `valor_mes_registro_ecf_totais` | totais | ctsped_ecf_od_mes | empresa | ✔ |
| `valor_registro_ecf_consultar` | consultar | ctsped_ecf_od_registro | empresa | ✔ |
| `valor_registro_ecf_totais` | totais | ctsped_ecf_od_registro | empresa | ✔ |
| `conta_registro_ecf_consultar` | consultar | ctsped_ecf_od_registro_conta | empresa | ✔ |
| `valor_lalur_ecf_consultar` | consultar | ctsped_ecf_od_registro_lalur | empresa | ✔ |
| `valor_lalur_ecf_totais` | totais | ctsped_ecf_od_registro_lalur | empresa | ✔ |
| `base_negativa_parte_b_ecf_consultar` | consultar | ctsped_ecf_od_registro_lalur_base_negativa_parte_b | empresa | ✔ |
| `base_negativa_parte_b_ecf_totais` | totais | ctsped_ecf_od_registro_lalur_base_negativa_parte_b | empresa | ✔ |
| `conta_lalur_ecf_consultar` | consultar | ctsped_ecf_od_registro_lalur_conta | empresa | ✔ |
| `conta_lalur_ecf_totais` | totais | ctsped_ecf_od_registro_lalur_conta | empresa | ✔ |
| `lancamento_lalur_ecf_consultar` | consultar | ctsped_ecf_od_registro_lalur_lancamento | empresa | ✔ |
| `lancamento_lalur_ecf_totais` | totais | ctsped_ecf_od_registro_lalur_lancamento | empresa | ✔ |
| `signatario_ecf_consultar` | consultar | ctsped_ecf_signatario | empresa | ✔ |
| `signatario_ecf_obter` | obter | ctsped_ecf_signatario | empresa, codigo | ✔ |
| `qualificacao_signatario_consultar` | consultar | ctsped_signatario_qualificacao | — | ✔ |
| `qualificacao_signatario_obter` | obter | ctsped_signatario_qualificacao | codigo | ✔ |
| `layout_registro_ecf_consultar` | consultar | cttabela_sped_ecf_od_registro | — | ✔ |
| `layout_registro_ecf_obter` | obter | cttabela_sped_ecf_od_registro | registro, codigo, vigencia | ✔ |

## `ecf_outros_dados_consultar`

ECF - Parâmetros da escrituração (Outros Dados) — tabela ctsped_ecf_od (módulo sped_ecf, ~2.533 linhas).
O QUE É: Um registro por empresa, ano-calendário e SCP, com os parâmetros que a Domínio usa para gerar a ECF: forma de tributação, período de apuração, retificação, situação especial e as respostas S/N das fichas de operações. 2.533 registros, 613 empresas, anos-calendário 2017 a 2025. Usa 56 dos 110 campos do cadastro (as respostas S/N de regimes especiais mais raros ficaram fora).
COMENTÁRIO DO BANCO SOBRE A TABELA: SPED ECF - Outros Dados
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna ano_calendario. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: codigo, ano_calendario, scp_codigo, forma_tributacao, periodo_apuracao, retificadora, tipo_escrituracao. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, ano_calendario, scp_codigo, empresa_scp, situacao_especial, situacao_especial_evento, situacao_especial_data, patrimonio_remanescente_cisao, retificadora, numero_recibo_retificadora, indicador_inicio_periodo, forma_tributacao, forma_tributacao_trimestre_1, forma_tributacao_trimestre_2, forma_tributacao_trimestre_3, forma_tributacao_trimestre_4, periodo_apuracao, qualificacao_pj, tipo_entidade_isenta_imune, tipo_escrituracao, criterio_reconhecimento_receita, atividade_tributada_irpj_csll, aliquota_csll_2019, optante_refis, optante_paes, optante_extincao_rtt_2014, gerar_contas_por_centro_custo, gerar_somente_contas_com_movimento, gerar_somente_tabelas_com_movimento, gerar_bloco_q_livro_caixa, gerar_registros_u100_u150, operacao_exterior, operacao_pessoa_vinculada, participacao_exterior, participacao_coligada_controlada, participacao_consorcio, vendas_exportacao, recebimento_exterior, pagamento_exterior, ativo_exterior, atividade_rural, lucro_exploracao, doacao_campanha_eleitoral, comercio_eletronico_ti, inovacao_tecnologica, pj_comercial_exportadora, royalties_recebidos, royalties_pagos, zona_franca_manaus, area_livre_comercio, zona_processamento_exportacao, regime_repes_recap_padis, pais_a_pais, preco_transferencia_2023, possui_cebas, cebas. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): empresa_nome, empresa_cnpj_cpf.
EXEMPLO COM DADOS: a empresa 965 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Chave de negócio: há exatamente um registro por (empresa, ano-calendário, SCP): os 2.533 grupos têm 1 linha. 65 registros são de SCP (`scp_codigo` preenchido). | Forma de tributação x período: lucro presumido (5) é trimestral em 2.112 registros; lucro real (1) é anual em 229 e trimestral em 9; isento (9) 170 e imune (8) 13. | Retificação: 2.454 originais (N), 78 retificadoras (S) e 1 original com mudança de forma de tributação (F). 67 registros têm situação especial. | Critério de reconhecimento da receita: 1.556 por competência (2) e 977 por caixa (1).
POSSÍVEIS DADOS PESSOAIS/FINANCEIROS (os dados saem em claro; devolva só o que a pergunta exigir): empresa_cnpj_cpf.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo`: Filtra i_outros_dados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Sequencial)
- `ano_calendario`: Filtra ano_calendario (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Ano da emissão do SPED) Datas no formato AAAA-MM-DD.
- `scp_codigo`: Filtra i_scp (integer). Aceita: valor simples (igualdade), igual, lista de valores. (SCP)
- `forma_tributacao`: Filtra forma_tributacao (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Lucro real, 2=Lucro real/arbitrado, 3=Lucro presumido/real, 5=Lucro presumido, 6=Lucro arbitrado, 7=Lucro presumido/arbitrado, 8=Imune de IRPJ, 9=Isento do IRPJ (FORMA DE TRIBUTAÇÃO DO LUCRO (1 - LUCRO REAL / 2 - LUCRO REAL/ARBITRADO / 3 - LUCRO PRESUMIDO/REAL / 5 - LUCRO PRESUMIDO / 6 - LUCRO ARBITRADO / 7 - LUCRO PRESUMIDO/ARBITRADO / 8 - IMUNE DE IRPJ / 9 - ISENTO DO IRPJ))
- `periodo_apuracao`: Filtra periodo_apuracao_irpj_csll (char). Aceita: valor simples (igualdade), igual. Códigos: T=Trimestral, A=Anual (Período de apuração do IRPJ e CSLL (T - Trimestral / A - Anual))
- `retificadora`: Filtra retificadora (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: N=ECF original, S=ECF retificadora, F=ECF original com mudança de forma de tributação (IN 166/1999) (TIPO DA ESCRITURAÇÃO RETIFICADORA (N - ECF ORIGINAL / S - ECF RETIFICADORA / F - ECF ORIGINAL COM MUDANÇA DE FORMA DE TRIBUTAÇÃO (IN Nº 166/1999)))
- `tipo_escrituracao`: Filtra tipo_escrituracao (char). Aceita: valor simples (igualdade), igual. Códigos: L=Livro caixa (lucro presumido) ou sem escrituração, C=Contábil (lucro presumido, imunes ou isentas)=None (Tipo de escrituração (L - Livro Caixa (Lucro Presumido) ou Sem Escrituração / C - Contábil (Lucro Presumido, Imunes ou Isentas)))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `ecf_outros_dados_obter`

ECF - Parâmetros da escrituração (Outros Dados) — obtém UM registro pela chave (codi_emp, i_outros_dados) da tabela ctsped_ecf_od. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use ecf_outros_dados_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra i_outros_dados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Sequencial)

## `valor_mes_registro_ecf_consultar`

ECF - Valores mensais de registros — tabela ctsped_ecf_od_mes (módulo sped_ecf, ~32.556 linhas).
O QUE É: Valor por mês (1 a 12) de registros que têm colunas mensais. 32.556 linhas, só dos registros Y690 (30.372) e Y682 (2.184).
COMENTÁRIO DO BANCO SOBRE A TABELA: SPED ECF - Outros Dados - Registros de colunas meses
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): outros_dados, registro.
FILTROS: outros_dados, registro, mes. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: outros_dados, registro, mes, valor. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 1009 tem registros nesta tabela (use para testar).
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `outros_dados`: Filtra i_outros_dados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Sequencial Outros Dados)
- `registro`: Filtra registro (varchar). Aceita: valor simples (igualdade), igual, lista de valores. (Registro)
- `mes`: Filtra i_mes (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Mês)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `valor_mes_registro_ecf_obter`

ECF - Valores mensais de registros — obtém UM registro pela chave (codi_emp, i_outros_dados, registro, i_mes) da tabela ctsped_ecf_od_mes. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use valor_mes_registro_ecf_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `outros_dados` (obrigatório): Filtra i_outros_dados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Sequencial Outros Dados)
- `registro` (obrigatório): Filtra registro (varchar). Aceita: valor simples (igualdade), igual, lista de valores. (Registro)
- `mes` (obrigatório): Filtra i_mes (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Mês)

## `valor_mes_registro_ecf_totais`

ECF - Valores mensais de registros — TOTAIS por grupo da tabela ctsped_ecf_od_mes (módulo sped_ecf). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): outros_dados, registro. CAMPOS SOMÁVEIS: valor. CAMPOS PARA AGRUPAR: outros_dados, registro, mes. Os filtros são os mesmos de valor_mes_registro_ecf_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `outros_dados`: Filtra i_outros_dados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Sequencial Outros Dados)
- `registro`: Filtra registro (varchar). Aceita: valor simples (igualdade), igual, lista de valores. (Registro)
- `mes`: Filtra i_mes (integer). Aceita: valor simples (igualdade), igual, lista de valores, {"entre":[a,b]}. (Mês)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["outros_dados"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `valor_registro_ecf_consultar`

ECF - Valores dos registros por competência — tabela ctsped_ecf_od_registro (módulo sped_ecf, ~8.584.047 linhas).
O QUE É: Cada linha é o valor de uma linha do layout (registro + código + vigência) numa competência do Outros Dados. 8,58 milhões de linhas, 2017 a 2025. 99% valem 0 (8.496.748), pois o sistema grava todas as linhas do layout. Registros mais frequentes: L210 (1,69 mi), N610, X480, N600, Y681, U182, P130.
COMENTÁRIO DO BANCO SOBRE A TABELA: SPED ECF - Outros Dados - Registros de colunas valor
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): outros_dados, periodo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna competencia. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: outros_dados, competencia, registro, codigo, valor. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: outros_dados, competencia, registro, codigo, vigencia, valor, saldo_anterior, contas, determinar_forma_importacao, forma_importacao. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): layout_descricao, layout_tipo, ano_calendario, forma_tributacao.
EXEMPLO COM DADOS: a empresa 1507 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Volume: 99% das linhas têm valor 0 (8.496.748 de 8.584.047). Para ver só o que foi declarado, filtre `valor` diferente de zero (use `gte`/`lte`). | Origem do valor: 8.581.577 linhas têm forma de importação 1 com indicador 'determinar forma' = N (padrão); só 2.470 têm forma definida (4: 1.165, 1: 556, 3: 416, 2: 333) e 3.223 trazem a lista de contas. | Sem órfãos: 0 valores sem cabeçalho (`ecf_outros_dados`) e 0 sem layout, em 149.616 valores das 3 empresas mais recentes.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `outros_dados`: Filtra i_outros_dados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Sequencial)
- `competencia`: Filtra competencia (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competência) Datas no formato AAAA-MM-DD.
- `registro`: Filtra registro (varchar). Aceita: valor simples (igualdade), igual, lista de valores. (Registro)
- `codigo`: Filtra codigo (numeric). Aceita: valor simples (igualdade), igual, lista de valores. (Código do registro)
- `valor`: Filtra valor (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Valor)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `valor_registro_ecf_totais`

ECF - Valores dos registros por competência — TOTAIS por grupo da tabela ctsped_ecf_od_registro (módulo sped_ecf). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): outros_dados, periodo. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna competencia. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor, saldo_anterior. CAMPOS PARA AGRUPAR: outros_dados, competencia:mes, registro, codigo, vigencia:mes, contas, determinar_forma_importacao, forma_importacao. Os filtros são os mesmos de valor_registro_ecf_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (determinar_forma_importacao, forma_importacao) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Volume: 99% das linhas têm valor 0 (8.496.748 de 8.584.047). Para ver só o que foi declarado, filtre `valor` diferente de zero (use `gte`/`lte`). | Origem do valor: 8.581.577 linhas têm forma de importação 1 com indicador 'determinar forma' = N (padrão); só 2.470 têm forma definida (4: 1.165, 1: 556, 3: 416, 2: 333) e 3.223 trazem a lista de contas. | Sem órfãos: 0 valores sem cabeçalho (`ecf_outros_dados`) e 0 sem layout, em 149.616 valores das 3 empresas mais recentes.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `outros_dados`: Filtra i_outros_dados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Sequencial)
- `competencia`: Filtra competencia (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competência) Datas no formato AAAA-MM-DD.
- `registro`: Filtra registro (varchar). Aceita: valor simples (igualdade), igual, lista de valores. (Registro)
- `codigo`: Filtra codigo (numeric). Aceita: valor simples (igualdade), igual, lista de valores. (Código do registro)
- `valor`: Filtra valor (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Valor)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["competencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `conta_registro_ecf_consultar`

ECF - Contas contábeis que compõem um valor de registro — tabela ctsped_ecf_od_registro_conta (módulo sped_ecf, ~4.866 linhas).
O QUE É: Detalha de quais contas contábeis da empresa vem o valor de uma linha do registro (forma de importação e operação de somar ou subtrair). 4.866 linhas. `plano_empresa` é a empresa dona do plano de contas, que pode ser outra.
COMENTÁRIO DO BANCO SOBRE A TABELA: SPED ECF - Outros Dados - Registros de conta contábil
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): outros_dados.
FILTROS: outros_dados, registro, conta_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: sequencial, outros_dados, competencia, registro, codigo, vigencia, conta_codigo, plano_empresa, forma_importacao, operacao. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): conta_classificacao, conta_nome.
EXEMPLO COM DADOS: a empresa 1027 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Forma de importação x operação: 5 (saldo anterior) com somar: 2.808; 1 (total débito) sem operação 858, somar 832, subtrair 26; 4 (saldo do exercício) somar 221; 2 (total crédito) sem operação 69, somar 26; 3 (saldo do período) sem operação 13, somar 13. A operação só é nula nas formas 1, 2 e 3.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `outros_dados`: Filtra i_outros_dados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Sequencial dos outros dados)
- `registro`: Filtra registro (varchar). Aceita: valor simples (igualdade), igual, lista de valores. (Registro)
- `conta_codigo`: Filtra codi_cta (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta contábil)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `valor_lalur_ecf_consultar`

ECF - Registros do Lalur (Parte A/B) — tabela ctsped_ecf_od_registro_lalur (módulo sped_ecf, ~4.078.361 linhas).
O QUE É: Valores e históricos das linhas de Lalur da ECF. 4,08 milhões de linhas, só dos registros M30G (2.144.041) e M35G (1.934.320); só 3.359 e 3.090 têm histórico preenchido.
COMENTÁRIO DO BANCO SOBRE A TABELA: SPED ECF - Outros Dados - Registros de colunas valor LALUR
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): outros_dados, periodo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna competencia. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: outros_dados, competencia, registro, codigo, valor. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: outros_dados, competencia, registro, codigo, vigencia, valor, historico. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 1420 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): O `codigo` do Lalur NÃO é o código do layout `layout_registro_ecf`: na empresa 1420 só 2.067 de 53.508 linhas casam por (registro, código, vigência) e é coincidência numérica (726 códigos distintos em M30G contra ~330 no layout), por isso o vínculo foi removido. Os programas da Domínio ligam este código às tabelas LRTABELA_GRUPO_* (IRPJ/CSLL, […] | Só 192 das 53.508 linhas da empresa 1420 têm valor diferente de 0.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `outros_dados`: Filtra i_outros_dados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Sequencial)
- `competencia`: Filtra competencia (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competência) Datas no formato AAAA-MM-DD.
- `registro`: Filtra registro (varchar). Aceita: valor simples (igualdade), igual, lista de valores. (Registro)
- `codigo`: Filtra codigo (numeric). Aceita: valor simples (igualdade), igual, lista de valores. (Código do registro)
- `valor`: Filtra valor (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Valor)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `valor_lalur_ecf_totais`

ECF - Registros do Lalur (Parte A/B) — TOTAIS por grupo da tabela ctsped_ecf_od_registro_lalur (módulo sped_ecf). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): outros_dados, periodo. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna competencia. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: valor. CAMPOS PARA AGRUPAR: outros_dados, competencia:mes, registro, codigo, vigencia:mes, historico. Os filtros são os mesmos de valor_lalur_ecf_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: O `codigo` do Lalur NÃO é o código do layout `layout_registro_ecf`: na empresa 1420 só 2.067 de 53.508 linhas casam por (registro, código, vigência) e é coincidência numérica (726 códigos distintos em M30G contra ~330 no layout), por isso o vínculo foi removido. Os programas da Domínio ligam este código às tabelas LRTABELA_GRUPO_* (IRPJ/CSLL, adição/exclusão, geral/rural/seguradora/sistema financeiro), […] | Só 192 das 53.508 linhas da empresa 1420 têm valor diferente de 0.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `outros_dados`: Filtra i_outros_dados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Sequencial)
- `competencia`: Filtra competencia (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competência) Datas no formato AAAA-MM-DD.
- `registro`: Filtra registro (varchar). Aceita: valor simples (igualdade), igual, lista de valores. (Registro)
- `codigo`: Filtra codigo (numeric). Aceita: valor simples (igualdade), igual, lista de valores. (Código do registro)
- `valor`: Filtra valor (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Valor)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["competencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `base_negativa_parte_b_ecf_consultar`

ECF - Base negativa da Parte B do Lalur — tabela ctsped_ecf_od_registro_lalur_base_negativa_parte_b (módulo sped_ecf, ~194 linhas).
O QUE É: Saldos de base de cálculo negativa da CSLL na Parte B do Lalur (194 linhas, indicador sempre C).
COMENTÁRIO DO BANCO SOBRE A TABELA: SPED ECF - Outros Dados - Registros de conta parte b LALUR
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de pequena (até alguns milhares de linhas)): outros_dados.
FILTROS: outros_dados, registro. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: outros_dados, competencia, registro, codigo, vigencia, sequencial, valor, descricao, indicador_lancamento, identificador_sped_ecf. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 1556 tem registros nesta tabela (use para testar).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `outros_dados`: Filtra i_outros_dados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Sequencial)
- `registro`: Filtra registro (varchar). Aceita: valor simples (igualdade), igual, lista de valores. (Registro)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `base_negativa_parte_b_ecf_totais`

ECF - Base negativa da Parte B do Lalur — TOTAIS por grupo da tabela ctsped_ecf_od_registro_lalur_base_negativa_parte_b (módulo sped_ecf). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de pequena (até alguns milhares de linhas)): outros_dados. CAMPOS SOMÁVEIS: valor. CAMPOS PARA AGRUPAR: outros_dados, competencia:mes, registro, codigo, vigencia:mes, sequencial, descricao, indicador_lancamento, identificador_sped_ecf. Os filtros são os mesmos de base_negativa_parte_b_ecf_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `outros_dados`: Filtra i_outros_dados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Sequencial)
- `registro`: Filtra registro (varchar). Aceita: valor simples (igualdade), igual, lista de valores. (Registro)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["competencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `conta_lalur_ecf_consultar`

ECF - Contas do Lalur — tabela ctsped_ecf_od_registro_lalur_conta (módulo sped_ecf, ~1.825 linhas).
O QUE É: Contas contábeis (da Parte B) ligadas a uma linha do Lalur, com valor e tipo de saldo. 1.825 linhas.
COMENTÁRIO DO BANCO SOBRE A TABELA: SPED ECF - Outros Dados - Registros de conta contábil LALUR
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): outros_dados.
FILTROS: outros_dados, registro, conta_codigo, tipo_saldo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: outros_dados, competencia, registro, codigo, vigencia, sequencial, conta_codigo, plano_empresa, valor, tipo_saldo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): conta_classificacao, conta_nome.
EXEMPLO COM DADOS: a empresa 1010 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Tipo de saldo: devedor (D) em 974 contas, credor (C) em 234 e vazio em 617. O vazio não consta no comentário do banco.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `outros_dados`: Filtra i_outros_dados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Sequencial)
- `registro`: Filtra registro (varchar). Aceita: valor simples (igualdade), igual, lista de valores. (Registro)
- `conta_codigo`: Filtra codi_cta (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta contábil)
- `tipo_saldo`: Filtra tipo_saldo (char). Aceita: valor simples (igualdade), igual. Códigos: D=Devedor, C=Credor, =Não informado [parcialmente confirmado] (Tipo Saldo: D-Devedor ou C-Credor.)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `conta_lalur_ecf_totais`

ECF - Contas do Lalur — TOTAIS por grupo da tabela ctsped_ecf_od_registro_lalur_conta (módulo sped_ecf). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): outros_dados. CAMPOS SOMÁVEIS: valor. CAMPOS PARA AGRUPAR: outros_dados, competencia:mes, registro, codigo, vigencia:mes, sequencial, conta_codigo, plano_empresa, tipo_saldo. Os filtros são os mesmos de conta_lalur_ecf_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (tipo_saldo) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Tipo de saldo: devedor (D) em 974 contas, credor (C) em 234 e vazio em 617. O vazio não consta no comentário do banco.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `outros_dados`: Filtra i_outros_dados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Sequencial)
- `registro`: Filtra registro (varchar). Aceita: valor simples (igualdade), igual, lista de valores. (Registro)
- `conta_codigo`: Filtra codi_cta (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Conta contábil)
- `tipo_saldo`: Filtra tipo_saldo (char). Aceita: valor simples (igualdade), igual. Códigos: D=Devedor, C=Credor, =Não informado [parcialmente confirmado] (Tipo Saldo: D-Devedor ou C-Credor.)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["competencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `lancamento_lalur_ecf_consultar`

ECF - Lançamentos contábeis do Lalur — tabela ctsped_ecf_od_registro_lalur_lancamento (módulo sped_ecf, ~14.978 linhas).
O QUE É: Lançamentos (data, lote, histórico, valor) que compõem a conta do Lalur. 14.978 linhas, de 2019-01 a 2025-12.
COMENTÁRIO DO BANCO SOBRE A TABELA: SPED ECF - Outros Dados - Registros de lançamento contábil LALUR
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): outros_dados.
FILTROS: outros_dados, registro, data, valor. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: outros_dados, competencia, registro, codigo, vigencia, sequencial_conta, sequencial, lote_numero, data, valor, historico_codigo, historico, tipo_saldo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 1012 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Tipo de saldo: devedor (D) 9.022, credor (C) 1.572 e vazio 4.384. Os lançamentos com saldo D vão de 2024-01 a 2025-12 e com C de 2024-07 a 2025-12; os vazios cobrem 2019-01 a 2024-12 (a explicação provável, tipo gravado só nas versões recentes, não foi confirmada).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `outros_dados`: Filtra i_outros_dados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Sequencial)
- `registro`: Filtra registro (varchar). Aceita: valor simples (igualdade), igual, lista de valores. (Registro)
- `data`: Filtra data_lancamento (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data do lançamento) Datas no formato AAAA-MM-DD.
- `valor`: Filtra valor (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Valor do lançamento)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `lancamento_lalur_ecf_totais`

ECF - Lançamentos contábeis do Lalur — TOTAIS por grupo da tabela ctsped_ecf_od_registro_lalur_lancamento (módulo sped_ecf). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): outros_dados. CAMPOS SOMÁVEIS: valor. CAMPOS PARA AGRUPAR: outros_dados, competencia:mes, registro, codigo, vigencia:mes, sequencial_conta, sequencial, lote_numero, data:mes, historico_codigo, historico, tipo_saldo. Os filtros são os mesmos de lancamento_lalur_ecf_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (tipo_saldo) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Tipo de saldo: devedor (D) 9.022, credor (C) 1.572 e vazio 4.384. Os lançamentos com saldo D vão de 2024-01 a 2025-12 e com C de 2024-07 a 2025-12; os vazios cobrem 2019-01 a 2024-12 (a explicação provável, tipo gravado só nas versões recentes, não foi confirmada).. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `outros_dados`: Filtra i_outros_dados (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Sequencial)
- `registro`: Filtra registro (varchar). Aceita: valor simples (igualdade), igual, lista de valores. (Registro)
- `data`: Filtra data_lancamento (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data do lançamento) Datas no formato AAAA-MM-DD.
- `valor`: Filtra valor (numeric). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"gte":v}, {"lte":v}, {"entre":[a,b]}. (Valor do lançamento)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["competencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["valor"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `signatario_ecf_consultar`

ECF - Signatários — tabela ctsped_ecf_signatario (módulo sped_ecf, ~1.051 linhas).
O QUE É: Pessoas e empresas que assinam a ECF por empresa, com a qualificação (contador, diretor etc.). 1.051 linhas. Só identificação e qualificação: e-mail e telefone ficaram de fora.
COMENTÁRIO DO BANCO SOBRE A TABELA: Tabela de Origem da Importação Registros Signatários.
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, tipo_inscricao, qualificacao_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, tipo_inscricao, inscricao, nome, qualificacao_codigo, crc. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): qualificacao_codigo_sped, qualificacao_descricao, qualificacao_registro_sped.
EXEMPLO COM DADOS: a empresa 1611 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Qualificação mais comum: 16 (Contador), com 587 dos 1.051 signatários (583 por CPF e 4 por CNPJ); 18 (Outros) 308; 1 (Diretor) 131.
PRIVACIDADE: Contém nome, CPF/CNPJ e CRC de pessoas físicas (contadores e administradores).
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): inscricao, nome, crc
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra i_signatario (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código Signatário.)
- `tipo_inscricao`: Filtra tipo_inscricao (tinyint). Aceita: valor simples (igualdade), igual. Códigos: 1=CNPJ, 2=CPF (1 - CNPJ/2 - CPF)
- `qualificacao_codigo`: Filtra i_qualificacao (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Qualificação da Entidade.)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `signatario_ecf_obter`

ECF - Signatários — obtém UM registro pela chave (i_signatario, codi_emp) da tabela ctsped_ecf_signatario. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use signatario_ecf_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra i_signatario (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código Signatário.)

## `qualificacao_signatario_consultar`

Qualificações de signatário (SPED Contábil e ECF) — tabela ctsped_signatario_qualificacao (módulo sped_ecf, ~21 linhas).
O QUE É: Catálogo global das 21 qualificações de signatário. `registro_sped` diz em qual SPED a qualificação vale (A ambos, E ECF, C Contábil).
COMENTÁRIO DO BANCO SOBRE A TABELA: Catálogo de qualificações de signatários para SPED Contábil e ECF
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
Tabela global (não depende de empresa): NÃO informe 'empresa'.
FILTROS: codigo, registro_sped. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, codigo_sped, descricao, registro_sped. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
REGRAS DE NEGÓCIO (conferidas nos dados): O código SPED não é único: 900 aparece para Contador (E), Contabilista (E) e Contador/Contabilista (C). Identifique a qualificação pelo código sequencial.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `codigo`: Filtra i_qualificacao (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Identificador de qualificação)
- `registro_sped`: Filtra registro_sped (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: A=Ambos, E=SPED ECF, C=SPED Contábil (A - AMBOS / E - SPED ECF / C - SPED CONTABIL)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `qualificacao_signatario_obter`

Qualificações de signatário (SPED Contábil e ECF) — obtém UM registro pela chave (i_qualificacao) da tabela ctsped_signatario_qualificacao. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use qualificacao_signatario_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `codigo` (obrigatório): Filtra i_qualificacao (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Identificador de qualificação)

## `layout_registro_ecf_consultar`

Layout dos registros do SPED ECF (tabela de colunas) — tabela cttabela_sped_ecf_od_registro (módulo sped_ecf, ~10.776 linhas).
O QUE É: Catálogo global das linhas de cada registro da ECF, por vigência do layout: descrição, tipo da linha, fórmula e, para o Lalur, o tipo de lançamento. 10.776 linhas, 52 registros, 14 vigências. É a "legenda" de `valor_registro_ecf`; as linhas do Lalur (`valor_lalur_ecf`) NÃO usam este layout (ver regras).
COMENTÁRIO DO BANCO SOBRE A TABELA: SPED ECF - Outros Dados - Tabela com colunas dos registros de valor
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
Tabela global (não depende de empresa): NÃO informe 'empresa'.
FILTROS: registro, codigo, vigencia, descricao, tipo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: registro, codigo, vigencia, descricao, tipo, formula, tipo_lancamento_lalur, mascara. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
REGRAS DE NEGÓCIO (conferidas nos dados): Todo valor de registro (`valor_registro_ecf`) tem a linha correspondente neste layout pela chave (registro, código, vigência): 0 sem layout em 149.616 valores conferidos (3 empresas mais recentes).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `registro`: Filtra registro (varchar). Aceita: valor simples (igualdade), igual, lista de valores. (Registro)
- `codigo`: Filtra codigo (numeric). Aceita: valor simples (igualdade), igual, lista de valores. (Código do registro)
- `vigencia`: Filtra vigencia (date). Aceita: valor simples (igualdade), igual, {"gte":v}, {"lte":v}. (Vigência do registro) Datas no formato AAAA-MM-DD.
- `descricao`: Filtra descricao (varchar). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}. (Descrição)
- `tipo`: Filtra tipo (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Título, 2=Valor, 3=Calculado, 4=Valor de outro registro, 5=Fórmula condicional com valor de outro registro, 6=Valor conta desabilitada, 7=Fórmula condicional com valor de outro registro habilitado (TIPO (1=TÍTULO / 2=VALOR / 3=CALCULADO / 4=VALOR DE OUTRO REGISTRO / 5=FÓRMULA CONDICIONAL COM VALOR DE OUTRO REGISTRO / 6=VALOR CONTA DESABILITADA / 7=FÓRMULA CONDICIONAL COM VALOR DE OUTRO REGISTRO HABILIT […]
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `layout_registro_ecf_obter`

Layout dos registros do SPED ECF (tabela de colunas) — obtém UM registro pela chave (registro, codigo, vigencia) da tabela cttabela_sped_ecf_od_registro. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use layout_registro_ecf_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `registro` (obrigatório): Filtra registro (varchar). Aceita: valor simples (igualdade), igual, lista de valores. (Registro)
- `codigo` (obrigatório): Filtra codigo (numeric). Aceita: valor simples (igualdade), igual, lista de valores. (Código do registro)
- `vigencia` (obrigatório): Filtra vigencia (date). Aceita: valor simples (igualdade), igual, {"gte":v}, {"lte":v}. (Vigência do registro) Datas no formato AAAA-MM-DD.
