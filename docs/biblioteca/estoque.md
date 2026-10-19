# Módulo `estoque`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `saldo_produto_consultar` | consultar | efsdopro | empresa | ✔ |
| `saldo_produto_obter` | obter | efsdopro | empresa, produto_codigo, competencia | ✔ |
| `saldo_produto_totais` | totais | efsdopro | empresa | ✔ |
| `saldo_produto_diario_consultar` | consultar | efsdopro_diario | empresa | ✔ |
| `saldo_produto_diario_obter` | obter | efsdopro_diario | empresa, competencia, produto_codigo, dia | ✔ |
| `saldo_produto_diario_totais` | totais | efsdopro_diario | empresa | ✔ |

## `saldo_produto_consultar`

Saldo mensal dos produtos (estoque fiscal) — tabela efsdopro (módulo estoque, ~8.451.202 linhas).
O QUE É: Uma linha por empresa, produto e competência (primeiro dia do mês): saldo físico e em valor no início, entradas e saídas do mês e saldo no fim. Traz também o estoque final da Portaria CAT 17/99 (SP) e o saldo de ICMS-ST. 8,45 milhões de linhas, 473 empresas, 2014-01 a 2026-09. Origem do movimento: notas de entrada (`efmvepro`), notas de saída (`efmvspro`) e CF-e.
COMENTÁRIO DO BANCO SOBRE A TABELA: Saldo dos Produtos
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): produto_codigo, periodo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna data_pro. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: produto_codigo, competencia, saldo_valido. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: produto_codigo, competencia, saldo_fisico_anterior, saldo_valor_anterior, entradas_fisicas, entradas_valor, saidas_fisicas, saidas_valor, saldo_fisico, saldo_valor, estoque_final_cat17, valor_unitario_cat17, saldo_final_cat17, quantidade_final_icms_st, valor_unitario_medio_icms_st, valor_final_icms_st, saldo_valido, origem_registro, saldo_fisico_recalculado, saldo_valor_recalculado. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): produto_descricao, produto_ncm.
EXEMPLO COM DADOS: a empresa 349 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Identidade do saldo (empresa 680, 63.777 saldos): saldo_valor = saldo_valor_anterior + entradas_valor - saidas_valor em 100% (tolerância 0,01); saldo_fisico = anterior + entradas - saídas em 100% a menos de 0,001 (463 saldos diferem só por arredondamento, desvio máximo 0,0005). Use `saldo_fisico` e `saldo_valor`; […] | Continuidade: o saldo anterior de um mês é igual ao saldo do mês anterior do mesmo produto em 62.130 de 62.130 pares (físico e valor). 76 saldos têm anterior diferente de zero sem registro do mês anterior (produto sem movimento no mês não gera linha). | Entradas: entradas_fisicas é igual à soma de efmvepro.qtde_mep (notas de entrada) por produto e mês em 63.775 de 63.777 (empresa 680). | Saídas: saidas_fisicas é igual à soma de efmvspro.qtde_msp (notas de saída) MAIS a quantidade dos itens de CF-e vigentes (situação 0) em 63.777 de 63.777 saldos a menos de 0,001 (63.258 exatos a 0,0001; os outros 519 diferem no máximo 0,0005, arredondamento). Só com as notas de saída seriam 57.529 (90,2%): o CF-e entra no saldo. Empresa 680. | Portaria CAT 17/99: estoque_final_cat17 x valor_unitario_cat17 = saldo_final_cat17 (tolerância 0,05) em 63.777 de 63.777; todos os saldos da empresa 680 têm saldo_valido = S. (+1 regras: veja descrever_entidade)
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `produto_codigo`: Filtra codi_pdi (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Produto)
- `competencia`: Filtra data_pro (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia) Datas no formato AAAA-MM-DD.
- `saldo_valido`: Filtra SALDO_VALIDO (char). Aceita: valor simples (igualdade), igual. Códigos: S=Sim, N=Não
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `saldo_produto_obter`

Saldo mensal dos produtos (estoque fiscal) — obtém UM registro pela chave (codi_emp, codi_pdi, data_pro) da tabela efsdopro. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use saldo_produto_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `produto_codigo` (obrigatório): Filtra codi_pdi (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Produto)
- `competencia` (obrigatório): Filtra data_pro (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia) Datas no formato AAAA-MM-DD.

## `saldo_produto_totais`

Saldo mensal dos produtos (estoque fiscal) — TOTAIS por grupo da tabela efsdopro (módulo estoque). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de GRANDE (milhões de linhas: use filtros e limite)): produto_codigo, periodo. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna data_pro. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: saldo_fisico_anterior, saldo_valor_anterior, entradas_valor, saidas_valor, saldo_fisico, saldo_valor, estoque_final_cat17, valor_unitario_cat17, saldo_final_cat17, quantidade_final_icms_st, valor_unitario_medio_icms_st, valor_final_icms_st. CAMPOS PARA AGRUPAR: produto_codigo, competencia:mes, entradas_fisicas, saidas_fisicas, saldo_valido, origem_registro. Os filtros são os mesmos de saldo_produto_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (saldo_valido, origem_registro) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Identidade do saldo (empresa 680, 63.777 saldos): saldo_valor = saldo_valor_anterior + entradas_valor - saidas_valor em 100% (tolerância 0,01); saldo_fisico = anterior + entradas - saídas em 100% a menos de 0,001 (463 saldos diferem só por arredondamento, desvio máximo 0,0005). Use `saldo_fisico` e `saldo_valor`; as colunas `*_recalculado` existem para conferir. | Continuidade: o saldo anterior de um mês é igual ao saldo do mês anterior do mesmo produto em 62.130 de 62.130 pares (físico e valor). 76 saldos têm anterior diferente de zero sem registro do mês anterior (produto sem movimento no mês não gera linha). | Entradas: entradas_fisicas é igual à soma de efmvepro.qtde_mep (notas de entrada) por produto e mês em 63.775 de 63.777 (empresa 680). | Saídas: saidas_fisicas é igual à soma de efmvspro.qtde_msp (notas de saída) MAIS a quantidade dos itens de CF-e vigentes (situação 0) em 63.777 de 63.777 saldos a menos de 0,001 (63.258 exatos a 0,0001; os outros 519 diferem no máximo 0,0005, arredondamento). Só com as notas de saída seriam 57.529 (90,2%): o CF-e entra no saldo. Empresa 680.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `produto_codigo`: Filtra codi_pdi (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Produto)
- `competencia`: Filtra data_pro (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competencia) Datas no formato AAAA-MM-DD.
- `saldo_valido`: Filtra SALDO_VALIDO (char). Aceita: valor simples (igualdade), igual. Códigos: S=Sim, N=Não
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["competencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["saldo_fisico_anterior"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).

## `saldo_produto_diario_consultar`

Saldo diário dos produtos (estoque fiscal) — tabela efsdopro_diario (módulo estoque, ~249.231 linhas).
O QUE É: Saldo físico e em valor, e de ICMS e ICMS-ST, de cada produto por dia com movimento dentro da competência. 249 mil linhas, 173 empresas, 2018-09 a 2026-09. É o detalhe do saldo mensal.
COMENTÁRIO DO BANCO SOBRE A TABELA: Saldo dos Produtos - Diário
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): produto_codigo, periodo.
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna dia_saldo. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: produto_codigo, competencia, dia. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: competencia, produto_codigo, dia, saldo_fisico_anterior, saldo_valor_anterior, icms_total_anterior, saldo_fisico_final, saldo_valor_final, icms_total_final, saldo_fisico_icms_st_anterior, icms_st_total_anterior, saldo_fisico_icms_st_final, icms_st_total_final, saldo_valido. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): produto_descricao.
EXEMPLO COM DADOS: a empresa 761 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Fechamento com o mensal (empresa 644, 82.962 meses de produto): o saldo físico e o saldo em valor do último dia da competência são iguais a saldo_produto.saldo_fisico e saldo_valor em 82.962 de 82.962. | A empresa 644 tem 86.485 linhas diárias, só do ano de 2024 (2024-01 a 2024-12); todas com saldo_valido = S.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `produto_codigo`: Filtra codi_pdi (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Código do produto)
- `competencia`: Filtra data_pro (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competência) Datas no formato AAAA-MM-DD.
- `dia`: Filtra dia_saldo (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Dia) Datas no formato AAAA-MM-DD.
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `saldo_produto_diario_obter`

Saldo diário dos produtos (estoque fiscal) — obtém UM registro pela chave (codi_emp, data_pro, codi_pdi, dia_saldo) da tabela efsdopro_diario. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use saldo_produto_diario_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `competencia` (obrigatório): Filtra data_pro (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competência) Datas no formato AAAA-MM-DD.
- `produto_codigo` (obrigatório): Filtra codi_pdi (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Código do produto)
- `dia` (obrigatório): Filtra dia_saldo (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Dia) Datas no formato AAAA-MM-DD.

## `saldo_produto_diario_totais`

Saldo diário dos produtos (estoque fiscal) — TOTAIS por grupo da tabela efsdopro_diario (módulo estoque). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): produto_codigo, periodo. Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna dia_saldo. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele. CAMPOS SOMÁVEIS: saldo_fisico_anterior, saldo_valor_anterior, icms_total_anterior, saldo_fisico_final, saldo_valor_final, icms_total_final, saldo_fisico_icms_st_anterior, icms_st_total_anterior, saldo_fisico_icms_st_final, icms_st_total_final. CAMPOS PARA AGRUPAR: competencia:mes, produto_codigo, dia:mes, saldo_valido. Os filtros são os mesmos de saldo_produto_diario_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (saldo_valido) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Fechamento com o mensal (empresa 644, 82.962 meses de produto): o saldo físico e o saldo em valor do último dia da competência são iguais a saldo_produto.saldo_fisico e saldo_valor em 82.962 de 82.962. | A empresa 644 tem 86.485 linhas diárias, só do ano de 2024 (2024-01 a 2024-12); todas com saldo_valido = S.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `produto_codigo`: Filtra codi_pdi (char). Aceita: valor simples (igualdade), igual, lista de valores, {"prefixo":"x"}. (Código do produto)
- `competencia`: Filtra data_pro (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competência) Datas no formato AAAA-MM-DD.
- `dia`: Filtra dia_saldo (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Dia) Datas no formato AAAA-MM-DD.
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["competencia:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["saldo_fisico_anterior"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).
