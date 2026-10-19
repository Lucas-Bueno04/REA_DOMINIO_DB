# Módulo `esocial`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `evento_esocial_consultar` | consultar | foesocial_dados_eventos | empresa | ✔ |
| `evento_esocial_obter` | obter | foesocial_dados_eventos | empresa, codigo | ✔ |
| `ocorrencia_evento_esocial_consultar` | consultar | foesocial_dados_eventos_ocorrencias | empresa | ✔ |
| `catalogo_evento_esocial_consultar` | consultar | foesocial_eventos | — | ✔ |
| `catalogo_evento_esocial_obter` | obter | foesocial_eventos | evento_codigo | ✔ |
| `lote_esocial_consultar` | consultar | foesocial_lotes | empresa | ✔ |
| `lote_esocial_obter` | obter | foesocial_lotes | empresa, lote | ✔ |

## `evento_esocial_consultar`

Eventos do eSocial (fila de envio e retorno) — tabela foesocial_dados_eventos (módulo esocial, ~912.947 linhas).
O QUE É: Um registro por evento gerado para envio ao eSocial: qual evento (S-xxxx), o item a que se refere, tipo de envio, ID, recibo e resposta do ambiente nacional, validação e ajustes. 913 mil linhas, 888 empresas, de 2018-08 a hoje. O XML do evento não é exposto. Atenção: `descricao_resposta` e `nis_empregado` podem conter dados pessoais.
COMENTÁRIO DO BANCO SOBRE A TABELA: Dados dos eventos para envio ao eSocial.
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DATA_CRIACAO_REGISTRO. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: codigo, lote, evento_codigo, tipo_envio, resposta_codigo, validado, aguardando_ajuste, numero_recibo, competencia_calculo, criado_em. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, lote, evento_codigo, item_codigo_esocial, tipo_envio, tabela_origem, chave_origem, id_envio, numero_recibo, resposta_codigo, descricao_resposta, validado, aguardando_ajuste, tipo_validacao, advertencia_ajustada, reenviar, xml_alterado, inclusao_duplicada, competencia_calculo, data_alteracao, concluido_em, criado_em, alterado_em, versao_leiaute, versao_sistema, nis_empregado, evento_excluido, recibo_excluido. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): evento_descricao, evento_grupo, lote_status.
EXEMPLO COM DADOS: a empresa 1187 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Recibo x validação: 912.966 de 913.041 registros (99,99%) têm número de recibo, validado = 1, aguardando_ajuste = 0 e código de resposta. Os 75 restantes não têm recibo nem validação; 73 estão aguardando ajuste e 2 não. | Resposta: 201 em 879.954 registros e 202 em 32.635 (ambos 'Sucesso.'); 401 (conteúdo do evento inválido) em 420 e 411 (assinante inválido) em 17. Nos 40 maiores clientes, 202 sempre tem ocorrência registrada e 201 nunca tem: 202 = sucesso com advertência (por evidência). | Eventos por grupo do catálogo: iniciais e tabelas 584.307 · periódicos 242.657 · não periódicos 86.077. Mais frequentes: S-1299 (fechamento) 26.643, S-1200 (remuneração) e S-1210 (pagamentos); S-1298 (reabertura) 4.712. | `item_codigo_esocial` é o código do objeto dentro da empresa a que o evento se refere (nas amostras: 1, 2, 3... para S-1200/S-1210, vazio para S-1298/S-1299). A leitura é uma inferência dos padrões, não vem documentada. | Integridade (3 maiores empresas, 78.357 registros): todo registro tem o lote correspondente (0 sem lote) e o evento do lote é o mesmo do registro em 100%. O catálogo cobre todos os registros (0 sem evento no catálogo) e o ID de envio é único (913.041 IDs distintos). (+1 regras: veja descrever_entidade)
PRIVACIDADE: A descrição da resposta pode citar CPF de trabalhadores; o NIS do empregado é dado pessoal.
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): descricao_resposta, nis_empregado
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `codigo`: Filtra i_dados_eventos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do registro de envio.)
- `lote`: Filtra I_LOTE (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do lote.)
- `evento_codigo`: Filtra I_EVENTO_ESOCIAL (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do evento do eSocial.)
- `tipo_envio`: Filtra TIPO_ENVIO (smallint). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Inclusão, 2=Alteração, 3=Exclusão, 4=Retificação (Tipo de envio. (1=Inclusão/2=Alteração/3=Exclusão/4=Retificação))
- `resposta_codigo`: Filtra I_RESPOSTA (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 201=Sucesso, 202=Sucesso com advertência (por evidência), 401=Conteúdo do evento inválido, 411=Assinante inválido [parcialmente confirmado] (Código da resposta para o evento.)
- `validado`: Filtra VALIDADO (smallint). Aceita: valor simples (igualdade), igual. Códigos: 1=Sim, 0=Não (Evento validado. (0=Não/1=Sim))
- `aguardando_ajuste`: Filtra AGUARDANDO_AJUSTE (smallint). Aceita: valor simples (igualdade), igual. Códigos: 1=Sim, 0=Não (Quando invalidado, indica se o evento necessita de ajuste antes de ser reenviado. (0=Não/1=Sim))
- `numero_recibo`: Filtra NUMERO_RECIBO (varchar). Aceita: valor simples (igualdade), igual. (Número do recibo.)
- `competencia_calculo`: Filtra COMPETENCIA_CALCULO (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competência para gerar os dados do cálculo.) Datas no formato AAAA-MM-DD.
- `criado_em`: Filtra DATA_CRIACAO_REGISTRO (timestamp). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data de inserção do registro no banco de dados.) Datas no formato AAAA-MM-DD.
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `evento_esocial_obter`

Eventos do eSocial (fila de envio e retorno) — obtém UM registro pela chave (codi_emp, i_dados_eventos) da tabela foesocial_dados_eventos. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use evento_esocial_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `codigo` (obrigatório): Filtra i_dados_eventos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do registro de envio.)

## `ocorrencia_evento_esocial_consultar`

Ocorrências do retorno de um envio ao eSocial — tabela foesocial_dados_eventos_ocorrencias (módulo esocial, ~82.751 linhas).
O QUE É: Mensagens que o ambiente nacional devolve sobre um evento (erros e advertências), com localização. 82.751 linhas. A descrição costuma citar CPF e matrícula do trabalhador.
COMENTÁRIO DO BANCO SOBRE A TABELA: Ocorrências do envio do evento.
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): envio.
FILTROS: envio, ocorrencia_codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: envio, sequencial, ocorrencia_codigo, descricao, localizacao, mostrar_no_painel. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 681 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Códigos mais frequentes: 163 (40.636 — trabalhador sem vínculo consta na base do eSocial mas não foi informado), 1727 (20.101 — advertências ao confirmar o fechamento da folha para a DCTFWeb), 1895 (6.388), 424 (5.674), 162 (5.579) e 1090 (1.628).
PRIVACIDADE: A descrição pode citar CPF de trabalhadores.
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): descricao
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `envio`: Filtra i_dados_eventos (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do registro de envio.)
- `ocorrencia_codigo`: Filtra I_RESPOSTA (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código da resposta.)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `catalogo_evento_esocial_consultar`

Catálogo dos eventos do eSocial — tabela foesocial_eventos (módulo esocial, ~44 linhas).
O QUE É: Os 44 eventos tratados pela Domínio (S-1000 ... S-3500) com grupo, ordem de envio e se são gerados automaticamente. Tabela global.
COMENTÁRIO DO BANCO SOBRE A TABELA: Eventos do e-Social
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
Tabela global (não depende de empresa): NÃO informe 'empresa'.
FILTROS: evento_codigo, grupo, descricao. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: evento_codigo, descricao, grupo, ordem_envio, gerar_automatico, validar_sem_recibo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
REGRAS DE NEGÓCIO (conferidas nos dados): 44 eventos: 11 iniciais/tabelas (1000 a 1080 e 2100), 11 periódicos (1200 a 1300) e 22 não periódicos (2190 a 2501, 3000 e 3500). O código é o número do evento (1200 = S-1200 Remuneração; 1210 = S-1210 Pagamentos; 1299 = S-1299 Fechamento). | 26 dos 44 eventos têm validar_sem_recibo = 1 (o comentário do banco: validar sem recibo quando o retorno for o código 537, registro duplicado), entre eles S-1200, S-1210, S-1299, S-2200, S-2299 e S-3000.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `evento_codigo`: Filtra i_evento_esocial (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do evento do e-Social)
- `grupo`: Filtra GRUPO (smallint). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Iniciais e tabelas, 2=Não periódicos, 3=Periódicos (Grupo (1=Iniciais e Tabelas/2=Não periódicos/3=Periódicos))
- `descricao`: Filtra DESCRICAO (varchar). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}. (Descrição do evento do e-Social)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `catalogo_evento_esocial_obter`

Catálogo dos eventos do eSocial — obtém UM registro pela chave (i_evento_esocial) da tabela foesocial_eventos. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use catalogo_evento_esocial_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `evento_codigo` (obrigatório): Filtra i_evento_esocial (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do evento do e-Social)

## `lote_esocial_consultar`

Lotes de envio ao eSocial — tabela foesocial_lotes (módulo esocial, ~210.737 linhas).
O QUE É: Cada lote reúne eventos do mesmo tipo de uma empresa para transmissão. 210.827 lotes, 916 empresas, de 2018-08 a hoje.
COMENTÁRIO DO BANCO SOBRE A TABELA: Lotes para envio do e-Social
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DATA_CRIACAO_REGISTRO. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: lote, status, evento_codigo, criado_em. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: lote, status, evento_codigo, versao_xml, lote_exclusao, possui_eventos_invalidados, criado_em, alterado_em, processado_em, versao_sistema. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): evento_descricao.
EXEMPLO COM DADOS: a empresa 483 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Status dos 210.827 lotes: 4 (concluído) 210.800 · 6 (aguardando múltiplos vínculos) 24 · 9 (erro de preenchimento) 2 · 3 (aguardando ajuste) 1. Lotes concluídos com eventos invalidados: 152.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `lote`: Filtra i_lote (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do lote)
- `status`: Filtra STATUS (smallint). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Aguardando envio, 2=Enviado, 3=Aguardando ajuste, 4=Concluído, 5=Aguardando senha A3, 6=Aguardando envio de múltiplos vínculos, 7=Aguardando fim da thread contábil, 8=Erro no lote, 9=Erro de preenchimento (Status do lote.(1=Aguardando envio/2=Enviado/3=Aguardando ajuste/4=Concluído/5=Aguardando senha A3/6=Aguardando Envio Multiplos Vinculos/7=Aguardando fim thread contábil/8=Erro lote/9=Erro preench […]
- `evento_codigo`: Filtra I_EVENTO_ESOCIAL (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do evento do eSocial que será enviado no lote.)
- `criado_em`: Filtra DATA_CRIACAO_REGISTRO (timestamp). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data de inserção do registro no banco de dados.) Datas no formato AAAA-MM-DD.
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `lote_esocial_obter`

Lotes de envio ao eSocial — obtém UM registro pela chave (codi_emp, i_lote) da tabela foesocial_lotes. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use lote_esocial_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp).
- `lote` (obrigatório): Filtra i_lote (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código do lote)
