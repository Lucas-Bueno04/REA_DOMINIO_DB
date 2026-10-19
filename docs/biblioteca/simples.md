# Módulo `simples`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `apuracao_simples_nacional_consultar` | consultar | efsdoimp_simples_nacional | empresa | ✔ |
| `apuracao_simples_nacional_totais` | totais | efsdoimp_simples_nacional | empresa | ✔ |
| `aliquota_simples_nacional_consultar` | consultar | efsdoimp_simples_nacional_aliquotas | empresa | ✔ |
| `aliquota_simples_nacional_totais` | totais | efsdoimp_simples_nacional_aliquotas | empresa | ✔ |
| `receita_bruta_anterior_simples_consultar` | consultar | efsimples_nacional_receita_bruta_anterior | empresa | ✔ |
| `receita_bruta_anterior_simples_obter` | obter | efsimples_nacional_receita_bruta_anterior | empresa, periodo | ✔ |
| `receita_bruta_anterior_simples_totais` | totais | efsimples_nacional_receita_bruta_anterior | empresa | ✔ |

## `apuracao_simples_nacional_consultar`

Apuração mensal do Simples Nacional — tabela efsdoimp_simples_nacional (módulo simples, ~31.723 linhas).
O QUE É: Resultado da apuração do Simples de cada empresa e competência: base de cálculo (receita bruta) e imposto por anexo, seção e tabela, com a repartição por tributo (IRPJ, CSLL, COFINS, PIS, INSS, IPI, ICMS, ISS), as alíquotas efetivas, o excedente do sublimite e as devoluções de venda. 31.758 linhas, 503 empresas, 2015-01 a 2026-09. Para cada filial e tipo de receita há uma LINHA DE TOTAL (anexo, seção e tabela = 0) além das linhas de detalhe: nunca some todas as linhas juntas (dobra o valor).
COMENTÁRIO DO BANCO SOBRE A TABELA: Saldo dos Impostos - Detalhamento do Simples Nacional
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna data_sim. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: competencia, filial, anexo, secao, tipo_receita. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: imposto_codigo, competencia, periodicidade, filial, anexo, secao, tabela_aliquota, tipo_receita, anexo_origem, secao_origem, tabela_origem, situacoes, sequencial, municipio, reducao_icms_aliquota, reducao_iss_aliquota, reducao_pis_aliquota, reducao_cofins_aliquota, aplica_reducao_icms, aplica_reducao_iss, incidencia, faixa, base_calculo, base_excedente_sublimite, base_excedente, valor_imposto, valor_imposto_excedente_sublimite, valor_imposto_excedente, aliquota, aliquota_excedente_sublimite, aliquota_excedente, aliquota_efetiva_calculada, base_irpj, valor_irpj, aliquota_irpj, base_csll, valor_csll, aliquota_csll, base_pis, valor_pis, aliquota_pis, base_cofins, valor_cofins, aliquota_cofins, base_inss, valor_inss, aliquota_inss, base_ipi, valor_ipi, aliquota_ipi, base_icms, valor_icms, aliquota_icms, base_iss, valor_iss, aliquota_iss, valor_iss_retido, isentas_icms, isentas_iss, icms_fixo, iss_fixo, valor_devolucao_venda, receita_excedente_estadual, fator_federal, fator_estadual, base_negativa, base_negativa_secundaria, valor_estoque, estoque_disponivel, deducao_emissoras_radio_tv, soma_tributos. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): empresa_nome.
EXEMPLO COM DADOS: a empresa 575 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Linha de total x detalhes: para cada (empresa, competência, filial, tipo de receita) existe uma linha de TOTAL (anexo = seção = tabela = 0) cuja base e cujo imposto são iguais à soma das linhas de detalhe (anexo > 0) em 18.355 de 18.355 grupos. Some só os detalhes OU só o total; somar tudo dobra. | Imposto: valor_imposto é a soma dos tributos (IRPJ + CSLL + COFINS + PIS + INSS + IPI + ICMS + ISS) em 13.403 de 13.403 linhas de detalhe (tolerância 0,02); `soma_tributos` recalcula. | Receita bruta (base_calculo) = saídas não canceladas de acumuladores que incidem sobre receita bruta (IREC_ACU = S) + serviços (idem) + cupons fiscais (CF-e vigentes, acumulador idem) - devoluções de venda lançadas em entradas com acumulador que incide sobre devolução (IDEV_ACU = S); a vigência do acumulador é a mais recente até a data da nota. […] | valor_devolucao_venda é a soma das devoluções de venda do mês: empresa 644, 2026-09: 10.355,94 = devoluções lançadas em entradas com CFOP de devolução de venda; vendas 48.850,63 - 10.355,94 = base 38.494,69. | Competência sem movimento: dos 17.613 pares empresa/competência com apuração, 6.654 têm SÓ a linha de total (anexo = 0) e, destes, 6.654 com base zero (declaração sem receita). Ao testar 'existe apuração', não exija linhas de detalhe (anexo > 0). (+1 regras: veja descrever_entidade)
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `competencia`: Filtra data_sim (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia) Datas no formato AAAA-MM-DD.
- `filial`: Filtra filial (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo da filial)
- `anexo`: Filtra anexo (tinyint). Aceita: valor simples (igualdade), igual, lista de valores. (Anexo)
- `secao`: Filtra secao (tinyint). Aceita: valor simples (igualdade), igual, lista de valores. (Secao)
- `tipo_receita`: Filtra TIPO_RECEITA (integer). Aceita: valor simples (igualdade), igual. Códigos: 1=Mercado interno, 2=Exportação (Tipo Receita (1- Mercado Interno / 2- Exportação))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `apuracao_simples_nacional_totais`

Apuração mensal do Simples Nacional — TOTAIS por grupo da tabela efsdoimp_simples_nacional (módulo simples). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna data_sim. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: base_calculo, base_excedente_sublimite, base_excedente, valor_imposto, valor_imposto_excedente_sublimite, valor_imposto_excedente, base_irpj, valor_irpj, base_csll, valor_csll, base_pis, valor_pis, base_cofins, valor_cofins, base_inss, valor_inss, base_ipi, valor_ipi, base_icms, valor_icms, base_iss, valor_iss, valor_iss_retido, valor_devolucao_venda, receita_excedente_estadual, base_negativa, base_negativa_secundaria, valor_estoque, estoque_disponivel. CAMPOS PARA AGRUPAR: imposto_codigo, competencia:mes, periodicidade, filial, anexo, secao, tabela_aliquota, tipo_receita, anexo_origem, secao_origem, tabela_origem, situacoes, sequencial, municipio, reducao_icms_aliquota, reducao_iss_aliquota, reducao_pis_aliquota, reducao_cofins_aliquota, aplica_reducao_icms, aplica_reducao_iss, incidencia, faixa, aliquota, aliquota_excedente_sublimite, aliquota_excedente, aliquota_efetiva_calculada, aliquota_irpj, aliquota_csll, aliquota_pis, aliquota_cofins, aliquota_inss, aliquota_ipi, aliquota_icms, aliquota_iss, isentas_icms, isentas_iss, icms_fixo. Os filtros são os mesmos de apuracao_simples_nacional_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (imposto_codigo, periodicidade, tipo_receita, aplica_reducao_icms) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Linha de total x detalhes: para cada (empresa, competência, filial, tipo de receita) existe uma linha de TOTAL (anexo = seção = tabela = 0) cuja base e cujo imposto são iguais à soma das linhas de detalhe (anexo > 0) em 18.355 de 18.355 grupos. Some só os detalhes OU só o total; somar tudo dobra. | Imposto: valor_imposto é a soma dos tributos (IRPJ + CSLL + COFINS + PIS + INSS + IPI + ICMS + ISS) em 13.403 de 13.403 linhas de detalhe (tolerância 0,02); `soma_tributos` recalcula. | Receita bruta (base_calculo) = saídas não canceladas de acumuladores que incidem sobre receita bruta (IREC_ACU = S) + serviços (idem) + cupons fiscais (CF-e vigentes, acumulador idem) - devoluções de venda lançadas em entradas com acumulador que incide sobre devolução (IDEV_ACU = S); a vigência do acumulador é a mais recente até a data da nota. Conferido numa amostra aleatória de 40 empresa/competências (mensal, […] | valor_devolucao_venda é a soma das devoluções de venda do mês: empresa 644, 2026-09: 10.355,94 = devoluções lançadas em entradas com CFOP de devolução de venda; vendas 48.850,63 - 10.355,94 = base 38.494,69.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `competencia`: Filtra data_sim (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia) Datas no formato AAAA-MM-DD.
- `filial`: Filtra filial (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo da filial)
- `anexo`: Filtra anexo (tinyint). Aceita: valor simples (igualdade), igual, lista de valores. (Anexo)
- `secao`: Filtra secao (tinyint). Aceita: valor simples (igualdade), igual, lista de valores. (Secao)
- `tipo_receita`: Filtra TIPO_RECEITA (integer). Aceita: valor simples (igualdade), igual. Códigos: 1=Mercado interno, 2=Exportação (Tipo Receita (1- Mercado Interno / 2- Exportação))
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["competencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["base_calculo"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `aliquota_simples_nacional_consultar`

Alíquotas efetivas do Simples Nacional por anexo — tabela EFSDOIMP_SIMPLES_NACIONAL_ALIQUOTAS (módulo simples, ~34.074 linhas).
O QUE É: Alíquota efetiva de cada tributo na competência, por anexo, seção e tabela (34.090 linhas, 493 empresas, 2018-01 a 2026-09). Complementa a apuração. Só existem os anexos 1 e 2.
COMENTÁRIO DO BANCO SOBRE A TABELA: Saldo dos Impostos - Alíquotas Simples Nacional
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DATA_SIM. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: competencia, anexo, secao. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: imposto_codigo, competencia, periodicidade, anexo, secao, tabela_aliquota, aliquota_irpj, aliquota_csll, aliquota_cofins, aliquota_pis, aliquota_inss, aliquota_icms, aliquota_iss, aliquota_total, soma_aliquotas. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 1197 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Chave (empresa, imposto, competência, periodicidade, anexo, seção, tabela) é a PK; as colunas GUID de integração (Contábil e Onvio) ficam fora da entidade. | Soma das partes: aliquota_total é igual à soma das alíquotas de IRPJ, CSLL, COFINS, PIS, INSS, ICMS e ISS em 17.045 de 17.045 linhas do anexo 1 e em 0 de 17.045 do anexo 2 (no anexo 2 o total é maior que a soma das partes; a causa não foi apurada — a tabela não tem coluna de IPI). Use aliquota_total, não `soma_aliquotas`, como alíquota efetiva. | Conferência com a apuração: nas empresas 644, 679, 718 e 762, a alíquota efetiva da apuração (apuracao_simples_nacional.aliquota) é igual a aliquota_total em 397 de 397 linhas de detalhe cruzadas.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `competencia`: Filtra DATA_SIM (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competência) Datas no formato AAAA-MM-DD.
- `anexo`: Filtra ANEXO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Anexo)
- `secao`: Filtra SECAO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Seção)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `aliquota_simples_nacional_totais`

Alíquotas efetivas do Simples Nacional por anexo — TOTAIS por grupo da tabela EFSDOIMP_SIMPLES_NACIONAL_ALIQUOTAS (módulo simples). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DATA_SIM. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: aliquota_total. CAMPOS PARA AGRUPAR: imposto_codigo, competencia:mes, periodicidade, anexo, secao, tabela_aliquota, aliquota_irpj, aliquota_csll, aliquota_cofins, aliquota_pis, aliquota_inss, aliquota_icms, aliquota_iss. Os filtros são os mesmos de aliquota_simples_nacional_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (imposto_codigo, periodicidade) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Chave (empresa, imposto, competência, periodicidade, anexo, seção, tabela) é a PK; as colunas GUID de integração (Contábil e Onvio) ficam fora da entidade. | Soma das partes: aliquota_total é igual à soma das alíquotas de IRPJ, CSLL, COFINS, PIS, INSS, ICMS e ISS em 17.045 de 17.045 linhas do anexo 1 e em 0 de 17.045 do anexo 2 (no anexo 2 o total é maior que a soma das partes; a causa não foi apurada — a tabela não tem coluna de IPI). Use aliquota_total, não `soma_aliquotas`, como alíquota efetiva. | Conferência com a apuração: nas empresas 644, 679, 718 e 762, a alíquota efetiva da apuração (apuracao_simples_nacional.aliquota) é igual a aliquota_total em 397 de 397 linhas de detalhe cruzadas.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `competencia`: Filtra DATA_SIM (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competência) Datas no formato AAAA-MM-DD.
- `anexo`: Filtra ANEXO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Anexo)
- `secao`: Filtra SECAO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Seção)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["competencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["aliquota_total"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `receita_bruta_anterior_simples_consultar`

Receita bruta de períodos anteriores (Simples Nacional) — tabela efsimples_nacional_receita_bruta_anterior (módulo simples, ~5.334 linhas).
O QUE É: Receita bruta informada manualmente para períodos anteriores ao uso do sistema, que entra no RBT12 do Simples (mercado interno e exportação). 5.347 linhas, 342 empresas, por empresa e mês, de 2016-07 a 2026 (mais 12 linhas com período em 2170-2171).
COMENTÁRIO DO BANCO SOBRE A TABELA: Simples Nacional - Valores da Receita Bruta dos periodos anteriores
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna periodo. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: periodo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: periodo, receita_bruta, receita_mercado_interno, receita_exportacao, mercado_interno_mais_exportacao. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 1171 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): receita_bruta = receita_mercado_interno + receita_exportacao em 5.347 de 5.347 linhas (tolerância 0,01); 134 linhas têm exportação diferente de zero. | Dado suspeito: 12 linhas da empresa 715 têm período de 2170-10 a 2171-09 (valor 0), provável erro de digitação do ano; filtre `periodo` até a data atual para ignorá-las.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `receita_bruta_anterior_simples_obter`

Receita bruta de períodos anteriores (Simples Nacional) — obtém UM registro pela chave (codi_emp, periodo) da tabela efsimples_nacional_receita_bruta_anterior. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use receita_bruta_anterior_simples_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `periodo` (obrigatório): Filtra periodo (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (periodo) Datas no formato AAAA-MM-DD.

## `receita_bruta_anterior_simples_totais`

Receita bruta de períodos anteriores (Simples Nacional) — TOTAIS por grupo da tabela efsimples_nacional_receita_bruta_anterior (módulo simples). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna periodo. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: receita_bruta, receita_mercado_interno, receita_exportacao. CAMPOS PARA AGRUPAR: periodo:mes. Os filtros são os mesmos de receita_bruta_anterior_simples_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: receita_bruta = receita_mercado_interno + receita_exportacao em 5.347 de 5.347 linhas (tolerância 0,01); 134 linhas têm exportação diferente de zero. | Dado suspeito: 12 linhas da empresa 715 têm período de 2170-10 a 2171-09 (valor 0), provável erro de digitação do ano; filtre `periodo` até a data atual para ignorá-las.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["periodo:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["receita_bruta"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).
