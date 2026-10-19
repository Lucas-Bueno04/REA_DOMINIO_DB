# Módulo `produto_fiscal`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `produto_vigencia_consultar` | consultar | efprodutos_vigencia | empresa | ✔ |
| `produto_vigencia_obter` | obter | efprodutos_vigencia | empresa, produto_codigo, vigencia | ✔ |
| `produto_vigencia_totais` | totais | efprodutos_vigencia | empresa | ✔ |

## `produto_vigencia_consultar`

Classificação fiscal do produto por vigência — tabela efprodutos_vigencia (módulo produto_fiscal, ~261.123 linhas).
O QUE É: Como o produto é tributado a partir de uma data: CST e alíquotas de PIS/COFINS na entrada e na saída, tipo de contribuição, natureza da receita, CST e alíquota de ICMS e IPI, substituição tributária e monofásico. A vigência em uso numa data é a de maior `vigencia` até essa data. 261.175 linhas, 475 empresas; 190.836 produtos têm uma só vigência.
COMENTÁRIO DO BANCO SOBRE A TABELA: Produtos - Vigência
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
FILTROS: produto_codigo, vigencia, descricao, tipo_contribuicao, pis_cofins_cst_saida, icms_cst_saida, monofasico_pis_cofins. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: produto_codigo, vigencia, descricao, pis_cofins_cst_entrada, pis_cofins_cst_saida, tipo_contribuicao, natureza_receita, pis_cumulativo_art_6, cofins_cumulativo_art_10, monofasico_pis_cofins, codigo_recolhimento_pis, codigo_recolhimento_cofins, credito_vinculo, credito_base, credito_proporcional, credito_aliquota_diferenciada, credito_aliquota_pis, credito_aliquota_cofins, debito_aliquota_diferenciada, debito_aliquota_pis, debito_aliquota_cofins, dados_piscofins_ok, icms_cst_entrada, icms_cst_saida, icms_aliquota, ipi_cst_entrada, ipi_cst_saida, ipi_aliquota, ipi_periodicidade, ipi_classe_enquadramento, st_base_calculo, st_percentual_reducao_base, st_margem_valor_agregado, st_valor_unitario, st_produto_incluido, st_data_inicio, sped_tabela. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): produto_descricao_cadastro, produto_ncm.
EXEMPLO COM DADOS: a empresa 749 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Vigências: 190.836 produtos têm 1, 21.829 têm 2, 7.710 têm 3, 646 têm 4 e 167 têm 5 (até 14). A data mais antiga é 1964-06-01 (valor padrão). A vigência em uso numa data é a mais recente até essa data (mesma regra dos acumuladores). | Tipo de contribuição: sem incidência (S) 104.403 · cumulativo (C) 82.137 · não cumulativo (N) 74.635; substituição tributária (T) não ocorre. Monofásico em apenas 46 vigências e alíquota diferenciada de saída em 984. | CST de ICMS de saída mais frequentes: 0 (77.829), 102 (42.554), 60 (25.140), 500 (18.156), 400 (13.774), 101 (10.981), 100 (10.449) e 20 (9.768); as legendas desses CST/CSOSN vêm do layout oficial (ex.: 102 Simples sem permissão de crédito, 60 ICMS-ST cobrado anteriormente), não do banco. […] | Dados de PIS/COFINS conferidos (S) em 71.071 vigências e não conferidos (N) em 190.104: a apuração do PIS/COFINS usa esse indicador (com o do item) para sinalizar produtos com dados incompletos, não para excluí-los. | Integridade (5 maiores empresas, 71.973 vigências): todas têm o produto no cadastro (efprodutos), 0 sem cadastro.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `produto_codigo`: Filtra CODI_PDI (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Produto)
- `vigencia`: Filtra VIGENCIA_PDI (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.
- `descricao`: Filtra DESCRICAO (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Descricao)
- `tipo_contribuicao`: Filtra TIPO_CONTRIBUICAO (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: N=Não cumulativo, C=Cumulativo, T=Substituição tributária, S=Sem incidência (Tipo de contribuicao (N=Nao cumulativo/ C=Cumulativo/ T=Substituicao tributaria/ S=Sem incidencia))
- `pis_cofins_cst_saida`: Filtra CODIGO_CST_SAIDA (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Tributável com alíquota básica, 4=Monofásica com alíquota zero, 6=Alíquota zero, 7=Isenta, 8=Sem incidência, 49=Outras operações de saída, 99=Outras operações [parcialmente confirmado] (CST - Saidas)
- `icms_cst_saida`: Filtra CST_ICMS_SAIDA (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CST ICMS - Saída)
- `monofasico_pis_cofins`: Filtra PRODUTO_SUJEITO_TRIBUTACAO_MONOFASICA_PISCOFINS (char). Aceita: valor simples (igualdade), igual. Códigos: S=Sim, N=Não (Produto sujeito a tributação monofásica de PIS e COFINS)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `produto_vigencia_obter`

Classificação fiscal do produto por vigência — obtém UM registro pela chave (CODI_EMP, CODI_PDI, VIGENCIA_PDI) da tabela efprodutos_vigencia. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use produto_vigencia_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP).
- `produto_codigo` (obrigatório): Filtra CODI_PDI (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Produto)
- `vigencia` (obrigatório): Filtra VIGENCIA_PDI (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.

## `produto_vigencia_totais`

Classificação fiscal do produto por vigência — TOTAIS por grupo da tabela efprodutos_vigencia (módulo produto_fiscal). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP). CAMPOS SOMÁVEIS: natureza_receita, credito_base, st_margem_valor_agregado, st_valor_unitario. CAMPOS PARA AGRUPAR: produto_codigo, vigencia:mes, descricao, pis_cofins_cst_entrada, pis_cofins_cst_saida, tipo_contribuicao, pis_cumulativo_art_6, cofins_cumulativo_art_10, monofasico_pis_cofins, codigo_recolhimento_pis, codigo_recolhimento_cofins, credito_vinculo, credito_proporcional, credito_aliquota_diferenciada, credito_aliquota_pis, credito_aliquota_cofins, debito_aliquota_diferenciada, debito_aliquota_pis, debito_aliquota_cofins, dados_piscofins_ok, icms_cst_entrada, icms_cst_saida, icms_aliquota, ipi_cst_entrada, ipi_cst_saida, ipi_aliquota, ipi_periodicidade, ipi_classe_enquadramento, st_base_calculo, st_percentual_reducao_base, st_produto_incluido, st_data_inicio:mes, sped_tabela. Os filtros são os mesmos de produto_vigencia_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (pis_cofins_cst_entrada, pis_cofins_cst_saida, tipo_contribuicao, pis_cumulativo_art_6) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Vigências: 190.836 produtos têm 1, 21.829 têm 2, 7.710 têm 3, 646 têm 4 e 167 têm 5 (até 14). A data mais antiga é 1964-06-01 (valor padrão). A vigência em uso numa data é a mais recente até essa data (mesma regra dos acumuladores). | Tipo de contribuição: sem incidência (S) 104.403 · cumulativo (C) 82.137 · não cumulativo (N) 74.635; substituição tributária (T) não ocorre. Monofásico em apenas 46 vigências e alíquota diferenciada de saída em 984. | CST de ICMS de saída mais frequentes: 0 (77.829), 102 (42.554), 60 (25.140), 500 (18.156), 400 (13.774), 101 (10.981), 100 (10.449) e 20 (9.768); as legendas desses CST/CSOSN vêm do layout oficial (ex.: 102 Simples sem permissão de crédito, 60 ICMS-ST cobrado anteriormente), não do banco. Nenhum produto está marcado como incluído em ST (produto_incluido_st = N em 261.175). | Dados de PIS/COFINS conferidos (S) em 71.071 vigências e não conferidos (N) em 190.104: a apuração do PIS/COFINS usa esse indicador (com o do item) para sinalizar produtos com dados incompletos, não para excluí-los.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `produto_codigo`: Filtra CODI_PDI (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Produto)
- `vigencia`: Filtra VIGENCIA_PDI (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Vigencia) Datas no formato AAAA-MM-DD.
- `descricao`: Filtra DESCRICAO (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Descricao)
- `tipo_contribuicao`: Filtra TIPO_CONTRIBUICAO (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: N=Não cumulativo, C=Cumulativo, T=Substituição tributária, S=Sem incidência (Tipo de contribuicao (N=Nao cumulativo/ C=Cumulativo/ T=Substituicao tributaria/ S=Sem incidencia))
- `pis_cofins_cst_saida`: Filtra CODIGO_CST_SAIDA (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Tributável com alíquota básica, 4=Monofásica com alíquota zero, 6=Alíquota zero, 7=Isenta, 8=Sem incidência, 49=Outras operações de saída, 99=Outras operações [parcialmente confirmado] (CST - Saidas)
- `icms_cst_saida`: Filtra CST_ICMS_SAIDA (integer). Aceita: valor simples (igualdade), igual, lista de valores. (CST ICMS - Saída)
- `monofasico_pis_cofins`: Filtra PRODUTO_SUJEITO_TRIBUTACAO_MONOFASICA_PISCOFINS (char). Aceita: valor simples (igualdade), igual. Códigos: S=Sim, N=Não (Produto sujeito a tributação monofásica de PIS e COFINS)
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["vigencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["natureza_receita"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).
