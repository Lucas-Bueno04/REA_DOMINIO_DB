# Módulo `reinf`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `envio_reinf_consultar` | consultar | efd_reinf_envio_arquivos | empresa | ✔ |
| `erro_envio_reinf_consultar` | consultar | efd_reinf_envio_arquivos_erros | empresa | ✔ |
| `retorno_reinf_consultar` | consultar | efd_reinf_retorno_arquivos | empresa | ✔ |

## `envio_reinf_consultar`

Envios da EFD-Reinf (um evento por linha) — tabela efd_reinf_envio_arquivos (módulo reinf, ~74.952 linhas).
O QUE É: Controle de cada evento gerado/transmitido à Receita pela Domínio: competência, evento (R-xxxx), tipo de envio, situação, recibo, protocolo e data de envio. Chave (empresa, envio, filial); `i_filial` é diferente de 0 em todas as linhas. Cobre 875 empresas, competências de 2018-12 a 2026-09.
COMENTÁRIO DO BANCO SOBRE A TABELA: EFD-Reinf - Envio dos Arquivos
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna competencia. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: envio, competencia, evento, situacao, tipo_envio, data_envio, numero_recibo, evento_excluido. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: envio, filial, competencia, evento, situacao, tipo_envio, ambiente, id_evento, numero_recibo, numero_recibo_excluido_retificado, numero_protocolo_entrega, data_envio, horario_envio, data_inicio_processamento, inscricao, inscricao_cliente_fornecedor, nome_arquivo, evento_excluido, evento_excluido_por, data_hora_exclusao, validacao_envio, situacao_especial, gerado_em. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 754 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Recibo x situação: situação 1 tem número de recibo em 57.770 de 57.924 envios (99,7%); situações 0, 3, 4, 5 e 6 nunca têm recibo; a 2 tem em 2 de 4.485. Use `numero_recibo` preenchido para afirmar que a Receita recebeu o evento. | Rejeição x erro: 8.680 de 8.702 envios com situação 3 têm erro em efd_reinf_envio_arquivos_erros (99,8%); nas demais situações os erros são raros (situação 1: 31 de 57.924). | Tipo x evento: tipo E só no R-9000, F só em 2099/4099, B só em 2098/4099, A só no R-1000. | Eventos excluídos (`evento_excluido = S`, 17.939 linhas) continuam na tabela; filtre `evento_excluido = N` para ver o que está vigente. | Não há duplicidade na chave (empresa, envio, filial) e todo erro e todo retorno tem o envio correspondente (0 órfãos).
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): inscricao, inscricao_cliente_fornecedor
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `envio`: Filtra i_envio (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código sequencial de envio dos arquivos)
- `competencia`: Filtra competencia (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competência) Datas no formato AAAA-MM-DD.
- `evento`: Filtra i_evento (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1000=R-1000 Informações do contribuinte, 2010=R-2010 Retenção contribuição previdenciária - serviços tomados, 2020=R-2020 Retenção contribuição previdenciária - serviços prestados, 2050=R-2050 Comercialização da produção por produtor rural PJ/agroindústria, 2060=R-2060 Contribuição previdenciária sobre a receita bruta (CPRB), 2098=R-2098 Reabertura dos eventos da série R-2000, […]
- `situacao`: Filtra situacao (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 0=Enviado, aguardando retorno (hipótese), 1=Processado com recibo (hipótese forte), 2=Excluído/cancelado (hipótese), 3=Rejeitado com erro (hipótese forte), 4=Desconhecido, 5=Desconhecido, 6=Desconhecido [parcialmente confirmado] (Situação processo)
- `tipo_envio`: Filtra tipo_envio (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: I=Inclusão (envio original), R=Retificação, E=Exclusão (R-9000), F=Fechamento, B=Reabertura, A=Alteração (R-1000) [parcialmente confirmado] (Tipo de envio)
- `data_envio`: Filtra data_envio (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data de envio) Datas no formato AAAA-MM-DD.
- `numero_recibo`: Filtra numero_recibo (varchar). Aceita: valor simples (igualdade), igual. (Número do recibo)
- `evento_excluido`: Filtra evento_excluido (char). Aceita: valor simples (igualdade), igual. Códigos: S=Sim, N=Não (Evento Excluído(S/N))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `erro_envio_reinf_consultar`

Erros dos envios da EFD-Reinf — tabela efd_reinf_envio_arquivos_erros (módulo reinf, ~11.960 linhas).
O QUE É: Erros de validação ou do retorno da Receita, vinculados ao envio. Um envio pode ter vários erros. `codigo_erro` 0 aparece em todos os erros de origem D (validação local).
COMENTÁRIO DO BANCO SOBRE A TABELA: EFD-Reinf - Envio dos Arquivos - Erros
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): envio.
FILTROS: envio, codigo_erro, origem. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: envio, filial, sequencia, codigo_erro, mensagem, localizacao, identificador_retorno_lote, origem. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): competencia, evento, situacao_envio, data_envio.
EXEMPLO COM DADOS: a empresa 1186 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Códigos mais frequentes: 1005 (4.129), 0 (1.291, origem D), 1353 (1.092), 13 (947), 1556 (858), 15 (842). A tabela não traz descrição do código; use `mensagem`.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `envio`: Filtra i_envio (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código sequencial de envio dos arquivos)
- `codigo_erro`: Filtra codigo_erro (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do erro)
- `origem`: Filtra origem_erro (char). Aceita: valor simples (igualdade), igual. Códigos: D=Domínio (validação local, hipótese)=None, R=Receita/retorno do web service (hipótese) [parcialmente confirmado] (Origem do erro(D/R))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `retorno_reinf_consultar`

Retorno do web service da EFD-Reinf — tabela efd_reinf_retorno_arquivos (módulo reinf, ~25.114 linhas).
O QUE É: Dados da consulta de retorno de cada envio (hash, data da consulta e estabelecimento). Com o fechamento R-2099 traz também o indicador de movimento da competência.
COMENTÁRIO DO BANCO SOBRE A TABELA: EFD-Reinf - Retorno do Web Service
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): envio, data_consulta.
FILTROS: envio, data_consulta. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: envio, filial, hash, data_consulta, tipo_inscricao_estabelecimento, inscricao_estabelecimento. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): possui_movimento, competencia, evento, numero_recibo.
EXEMPLO COM DADOS: a empresa 1518 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Todo retorno tem o envio correspondente em efd_reinf_envio_arquivos (0 órfãos em 25.231); o hash vem preenchido em 100%. | possui_movimento (R-2099): N em 10.623 e S em 987 fechamentos; todos correspondem a envios com i_evento = 2099.
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): inscricao_estabelecimento
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `envio`: Filtra i_envio (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Sequencial)
- `data_consulta`: Filtra data_consulta (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data de consulta) Datas no formato AAAA-MM-DD.
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.
