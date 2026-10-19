# Módulo `das_api`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `bilhetagem_das_api_consultar` | consultar | efdas_api_bilhetagem | empresa | ✔ |
| `envio_das_api_consultar` | consultar | efdas_api_envio_arquivos | empresa | ✔ |
| `envio_das_api_obter` | obter | efdas_api_envio_arquivos | empresa, envio | ✔ |
| `mensagem_envio_das_api_consultar` | consultar | efdas_api_envio_arquivos_mensagem | empresa | ✔ |

## `bilhetagem_das_api_consultar`

Bilhetagem (custo) das chamadas à API do DAS — tabela efdas_api_bilhetagem (módulo das_api, ~13.225 linhas).
O QUE É: Registra cada chamada com o contador que a fez, a hora e se a operação gerou custo. 13.320 linhas, uma por envio.
COMENTÁRIO DO BANCO SOBRE A TABELA: DAS Api - Envio dos Arquivos - Bilhetagem de custos
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna DATA_HORA_REQUISICAO. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: envio, requisicao_em, tipo_envio, gerou_custo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: envio, contador_codigo, sequencial, requisicao_em, tipo_envio, gerou_custo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 1464 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Gerou custo (S) em 11.281 chamadas e não (N) em 2.039. Por tipo: 1 (transmissão) S 5.494 / N 1.870; 2 (emissão da guia) S 5.499 / N 137; 3 S 288 / N 32. A hipótese de que as chamadas sem custo são as recusadas pela API não foi testada.
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `envio`: Filtra I_ENVIO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código sequencial de envio dos arquivos)
- `requisicao_em`: Filtra DATA_HORA_REQUISICAO (timestamp). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data/Hora da requisição) Datas no formato AAAA-MM-DD.
- `tipo_envio`: Filtra TIPO_ENVIO (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Transmissão da declaração PGDAS-D (por evidência), 2=Emissão da guia DAS (por evidência), 3=Outro serviço, provavelmente consulta (hipótese)=None [parcialmente confirmado] (Tipo de serviço realizado)
- `gerou_custo`: Filtra GEROU_CUSTO (char). Aceita: valor simples (igualdade), igual. Códigos: S=Sim, N=Não (Operação gerou custo)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `envio_das_api_consultar`

Envios à API do DAS/PGDAS-D — tabela efdas_api_envio_arquivos (módulo das_api, ~13.225 linhas).
O QUE É: Um registro por chamada à API: transmissão da declaração, emissão da guia DAS ou outro serviço, com situação e número da guia. 13.320 envios, 257 empresas, competências de 2024-04 a 2026-09 (envios de 2024-05 a 2026-10). O JSON trocado não é exposto.
COMENTÁRIO DO BANCO SOBRE A TABELA: DAS Api - Envio dos Arquivos
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
Parâmetro 'periodo' = {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} filtra pela coluna COMPETENCIA. Linhas com essa coluna VAZIA nunca aparecem num filtro de período; se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.
FILTROS: envio, competencia, tipo_envio, situacao, data_envio, numero_das. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: envio, competencia, tipo_envio, situacao, tipo_declaracao, data_envio, horario_envio, numero_das, valor_diferente_do_sistema, nome_arquivo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): empresa_nome.
EXEMPLO COM DADOS: a empresa 1464 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Situação x mensagem (por envio): situação 0 só tem mensagem de código 0 (950); 1 só 200 (11.155); 2 só 400 (967) ou 403 (126); 3 só 500 (121); 4 só 401 (1). Todo envio tem mensagem (0 sem). | Número da guia DAS: só em envios de tipo 2 com sucesso (3.505 de 5.490) e sempre com 17 posições; os outros 1.985 envios de emissão bem-sucedidos não trazem número. Os envios de transmissão (tipo 1) nunca trazem. | Retificação: 3.312 empresa/competências tiveram 1 transmissão com sucesso, 500 tiveram 2, 109 tiveram 3, 37 tiveram 4 e 59 tiveram 7 (o máximo é 9). A partir da segunda, todas são retificadoras (tipo 2): 1.334 de 1.334. | Valor diferente do que o sistema calculou: S em 273 envios, N em 2.478 e vazio em 10.569 (só preenchido nas emissões). | Integridade: 0 mensagens e 0 bilhetagens sem o envio correspondente; há 1 bilhetagem por envio (13.320 de 13.320).
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `periodo`: Período por data de referência: {"de":"AAAA-MM-DD","ate":"AAAA-MM-DD"} (um dos dois basta).
- `envio`: Filtra I_ENVIO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código sequencial de envio dos arquivos)
- `competencia`: Filtra COMPETENCIA (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Competência) Datas no formato AAAA-MM-DD.
- `tipo_envio`: Filtra TIPO_ENVIO (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=Transmissão da declaração PGDAS-D (por evidência), 2=Emissão da guia DAS (por evidência), 3=Outro serviço, provavelmente consulta (hipótese)=None [parcialmente confirmado] (Tipo de envio)
- `situacao`: Filtra SITUACAO (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 0=Aguardando retorno, 1=Sucesso, 2=Recusado pela API (400/403), 3=Erro no servidor (500), 4=Não autorizado (401) [parcialmente confirmado] (Situação processo)
- `data_envio`: Filtra DATA_ENVIO (date). Aceita: valor simples (igualdade), igual, {"entre":[a,b]}, {"gte":v}, {"lte":v}. (Data de envio) Datas no formato AAAA-MM-DD.
- `numero_das`: Filtra NUMERO_DAS (char). Aceita: valor simples (igualdade), igual. (Numero da guia DAS)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `envio_das_api_obter`

Envios à API do DAS/PGDAS-D — obtém UM registro pela chave (CODI_EMP, I_ENVIO) da tabela efdas_api_envio_arquivos. Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use envio_das_api_consultar. Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP).
- `envio` (obrigatório): Filtra I_ENVIO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código sequencial de envio dos arquivos)

## `mensagem_envio_das_api_consultar`

Mensagens de retorno da API do DAS — tabela efdas_api_envio_arquivos_mensagem (módulo das_api, ~18.635 linhas).
O QUE É: Mensagens devolvidas pela API em cada envio (código, título e descrição). 18.777 linhas; 16.612 são "Sucesso-PGDASD" (200).
COMENTÁRIO DO BANCO SOBRE A TABELA: DAS Api - Envio dos Arquivos - Retorno
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna CODI_EMP).
OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de média): envio.
FILTROS: envio, codigo. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: envio, sequencial, codigo, titulo, descricao. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
EXEMPLO COM DADOS: a empresa 1464 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Códigos: 200 Sucesso-PGDASD 16.612 · 400 Bad Request 967 · 0 (sem título) 950 · 403 Acesso negado (ICGERENCIADOR-032) 126 · 500 Erro no servidor 121 · 401 Unauthorized 1.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna CODI_EMP). Número ou lista de números.
- `envio`: Filtra I_ENVIO (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código sequencial de envio dos arquivos)
- `codigo`: Filtra CODIGO_MENSAGEM (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Código da mensagem de retorno)
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.
