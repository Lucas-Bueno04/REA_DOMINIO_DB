# Módulo `comum`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `empresa_consultar` | consultar | geempre | empresa | ✔ |
| `empresa_totais` | totais | geempre | empresa | ✔ |

## `empresa_consultar`

Empresa (cadastro) — tabela geempre (módulo comum, ~1.969 linhas).
O QUE É: Empresas atendidas pelo escritório. 62% (1.227 de 1.969) estão INATIVAS mas continuam marcadas como usuárias dos módulos (ex.: 729 inativas ainda com 'usa escrita fiscal'); para uma lista de clientes atuais filtre `status = 'A'`.
QUANDO USAR: para listar, filtrar e paginar registros desta tabela e entender seus códigos. Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).
OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp).
FILTROS: codigo, status, nome, cnpj_cpf, uf, tipo_inscricao, usa_folha, usa_escrita_fiscal, usa_contabilidade. Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).
CAMPOS: codigo, nome, razao_social, nome_fantasia, apelido, cnpj_cpf, tipo_inscricao, inscricao_estadual, inscricao_municipal, inscricao_junta_comercial, data_inicio_atividades, data_cadastro, status, motivo_inatividade, data_inativacao, natureza_juridica_codigo, cnae, municipio_codigo, cidade, uf, regime_federal, enquadramento_simples, tipo_honorario, numero_empregados, faturamento_medio, valor_honorarios, responsavel_legal, usa_escrita_fiscal, usa_contabilidade, usa_folha, usa_ponto, usa_honorarios, usa_patrimonio, usa_lalur, usa_registro, usa_livro_caixa, usa_protocolo. Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.
CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): municipio_nome, municipio_ibge, natureza_juridica_descricao, cnae_descricao.
EXEMPLO COM DADOS: a empresa 123 tem registros nesta tabela (use para testar).
REGRAS DE NEGÓCIO (conferidas nos dados): Situação: 742 ativas (A) e 1.227 inativas (I). Nas inativas, motivo_inatividade explica: 636 'outros', 307 transferida, 282 baixada, 2 inadimplente. | As flags usa_* NÃO indicam uso atual: 729 empresas inativas ainda têm usa_escrita_fiscal = 1 e usa_contabilidade = 1. Combine com status = 'A'. | Das 742 empresas ativas: 680 com CNPJ de 14 dígitos, 61 com CPF (11) e 1 sem documento. | geempre_vigencia repete o cadastro por data de vigência, mas na prática tem 1 vigência por empresa (1.967 de 1.968) e é igual a geempre em status; não foi modelada como entidade própria. | Escritório: tipo_honorario = 'E' marca quem fatura no módulo Honorários (3 empresas); as demais (1.966) são 'C' (cliente).
CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): cnpj_cpf, faturamento_medio, valor_honorarios, responsavel_legal
DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais.
TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.
CONFIANÇA: modelo CURADO à mão e conciliado com os dados.
Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra codi_emp (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `status`: Filtra stat_emp (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: A=Ativa, I=Inativa, C=Em constituição, M=Ativo sem movimento, B=Em processo de baixa, E=Excluindo (A - Ativa / I - Inativa / C - Em Constituicao / M - Ativo sem movimento / B - Em processo de baixa / E - Excluindo)
- `nome`: Filtra nome_emp (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Nome)
- `cnpj_cpf`: Filtra cgce_emp (char). Aceita: valor simples (igualdade), igual. (CNPJ)
- `uf`: Filtra esta_emp (char). Aceita: valor simples (igualdade), igual, lista de valores. (Estado)
- `tipo_inscricao`: Filtra tins_emp (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=CNPJ, 2=CPF, 3=CEI, 6=CAEPF (Tipo da inscrição(1 - CNPJ/2 - CPF/3 - CEI/6 - CAEPF))
- `usa_folha`: Filtra ufol_emp (tinyint). Aceita: valor simples (igualdade), igual. Códigos: 1=Sim, 0=Não (Usa folha (1 - Sim/0 - Nao))
- `usa_escrita_fiscal`: Filtra uefi_emp (tinyint). Aceita: valor simples (igualdade), igual. Códigos: 1=Sim, 0=Não (Usa escrita fiscal (1 - Sim/0 - Nao))
- `usa_contabilidade`: Filtra ucta_emp (tinyint). Aceita: valor simples (igualdade), igual. Códigos: 1=Sim, 0=Não (Usa contabilidade (1 - Sim/0 - Nao))
- `colunas`: Campos desejados (padrão: todos). Veja CAMPOS na descrição.
- `ordem`: Ordenação, ex.: ["data desc", "numero"] (campos da entidade).
- `limite`: Linhas por página (1 a 500).
- `offset`: Quantas linhas pular (use proximo_offset da resposta anterior).
- `contar`: true devolve também o total de linhas do filtro (mais lento em tabelas grandes).
- `decodificar`: true acrescenta <campo>_descricao com o significado dos códigos conhecidos.

## `empresa_totais`

Empresa (cadastro) — TOTAIS por grupo da tabela geempre (módulo comum). QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. OBRIGATÓRIO: 'empresa' (código da empresa na coluna codi_emp). CAMPOS SOMÁVEIS: faturamento_medio, valor_honorarios. CAMPOS PARA AGRUPAR: codigo, nome, razao_social, nome_fantasia, apelido, cnpj_cpf, tipo_inscricao, inscricao_estadual, inscricao_municipal, inscricao_junta_comercial, data_inicio_atividades:mes, data_cadastro:mes, status, motivo_inatividade, data_inativacao:mes, natureza_juridica_codigo, cnae, municipio_codigo, cidade, uf, regime_federal, enquadramento_simples, tipo_honorario, numero_empregados, responsavel_legal, usa_escrita_fiscal, usa_contabilidade, usa_folha, usa_ponto, usa_honorarios, usa_patrimonio, usa_lalur, usa_registro, usa_livro_caixa, usa_protocolo. Os filtros são os mesmos de empresa_consultar. Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo (tipo_inscricao, status, motivo_inatividade, regime_federal) agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. REGRAS DA TABELA QUE AFETAM OS TOTAIS: Situação: 742 ativas (A) e 1.227 inativas (I). Nas inativas, motivo_inatividade explica: 636 'outros', 307 transferida, 282 baixada, 2 inadimplente. | As flags usa_* NÃO indicam uso atual: 729 empresas inativas ainda têm usa_escrita_fiscal = 1 e usa_contabilidade = 1. Combine com status = 'A'. | Das 742 empresas ativas: 680 com CNPJ de 14 dígitos, 61 com CPF (11) e 1 sem documento. | geempre_vigencia repete o cadastro por data de vigência, mas na prática tem 1 vigência por empresa (1.967 de 1.968) e é igual a geempre em status; não foi modelada como entidade própria.. Somente leitura.

Parâmetros:

- `empresa` (obrigatório): Código da empresa (coluna codi_emp). Número ou lista de números.
- `codigo`: Filtra codi_emp (integer). Aceita: valor simples (igualdade), igual, lista de valores. (Codigo)
- `status`: Filtra stat_emp (char). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: A=Ativa, I=Inativa, C=Em constituição, M=Ativo sem movimento, B=Em processo de baixa, E=Excluindo (A - Ativa / I - Inativa / C - Em Constituicao / M - Ativo sem movimento / B - Em processo de baixa / E - Excluindo)
- `nome`: Filtra nome_emp (char). Aceita: SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): {"contem":"x"}, {"prefixo":"x"}. (Nome)
- `cnpj_cpf`: Filtra cgce_emp (char). Aceita: valor simples (igualdade), igual. (CNPJ)
- `uf`: Filtra esta_emp (char). Aceita: valor simples (igualdade), igual, lista de valores. (Estado)
- `tipo_inscricao`: Filtra tins_emp (integer). Aceita: valor simples (igualdade), igual, lista de valores. Códigos: 1=CNPJ, 2=CPF, 3=CEI, 6=CAEPF (Tipo da inscrição(1 - CNPJ/2 - CPF/3 - CEI/6 - CAEPF))
- `usa_folha`: Filtra ufol_emp (tinyint). Aceita: valor simples (igualdade), igual. Códigos: 1=Sim, 0=Não (Usa folha (1 - Sim/0 - Nao))
- `usa_escrita_fiscal`: Filtra uefi_emp (tinyint). Aceita: valor simples (igualdade), igual. Códigos: 1=Sim, 0=Não (Usa escrita fiscal (1 - Sim/0 - Nao))
- `usa_contabilidade`: Filtra ucta_emp (tinyint). Aceita: valor simples (igualdade), igual. Códigos: 1=Sim, 0=Não (Usa contabilidade (1 - Sim/0 - Nao))
- `agrupar_por`: Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. Vazio = um total geral. Exemplo desta tabela: ["data_inicio_atividades:mes"].
- `metricas`: Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas. Exemplo: ["faturamento_medio"].
- `funcao`: soma | media | minimo | maximo (aplicada a todas as métricas).
- `limite`: Máximo de grupos (1 a 500).
- `decrescente`: true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).
