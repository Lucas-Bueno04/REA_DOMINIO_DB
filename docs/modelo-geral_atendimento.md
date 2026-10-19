# Modelo — Geral - atendimento (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/geral_atendimento.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

20 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [geatendimento_sgd_notificacoes_usuarios](#geatendimento_sgd_notificacoes_usuarios) | `GEATENDIMENTO_SGD_NOTIFICACOES_USUARIOS` | 37.928 | medio | — |
| [geatendimento_plano_contas_contabilidade](#geatendimento_plano_contas_contabilidade) | `GEATENDIMENTO_PLANO_CONTAS_CONTABILIDADE` | 3.948 | pequeno | empresa |
| [geatendimento_digitalbank_catalogo](#geatendimento_digitalbank_catalogo) | `GEATENDIMENTO_DIGITALBANK_CATALOGO` | 2.155 | pequeno | empresa |
| [geatendimento_sgd_notificacoes](#geatendimento_sgd_notificacoes) | `GEATENDIMENTO_SGD_NOTIFICACOES` | 2.053 | pequeno | — |
| [geatendimento_codigo_empresa](#geatendimento_codigo_empresa) | `GEATENDIMENTO_CODIGO_EMPRESA` | 2.005 | pequeno | — |
| [geatendimento_mimetype](#geatendimento_mimetype) | `GEATENDIMENTO_MIMETYPE` | 818 | pequeno | — |
| [geatendimento_telemetria](#geatendimento_telemetria) | `GEATENDIMENTO_TELEMETRIA` | 407 | pequeno | — |
| [geatendimento_onvio_empresas_ignoradas](#geatendimento_onvio_empresas_ignoradas) | `GEATENDIMENTO_ONVIO_EMPRESAS_IGNORADAS` | 345 | pequeno | empresa |
| [geatendimento_sincronizar_dados](#geatendimento_sincronizar_dados) | `GEATENDIMENTO_SINCRONIZAR_DADOS` | 68 | pequeno | empresa |
| [geatendimento_dados_escritorio_historico](#geatendimento_dados_escritorio_historico) | `GEATENDIMENTO_DADOS_ESCRITORIO_HISTORICO` | 17 | pequeno | — |
| [geatendimento_bancos_iceberg](#geatendimento_bancos_iceberg) | `GEATENDIMENTO_BANCOS_ICEBERG` | 15 | pequeno | — |
| [geatendimento_log_catalogo](#geatendimento_log_catalogo) | `GEATENDIMENTO_LOG_CATALOGO` | 9 | pequeno | — |
| [geatendimento_escritorio](#geatendimento_escritorio) | `GEATENDIMENTO_ESCRITORIO` | 2 | pequeno | — |
| [geatendimento_bloco_informacoes](#geatendimento_bloco_informacoes) | `GEATENDIMENTO_BLOCO_INFORMACOES` | 2 | pequeno | — |
| [geatendimento_controle_requisicoes](#geatendimento_controle_requisicoes) | `GEATENDIMENTO_CONTROLE_REQUISICOES` | 1 | pequeno | — |
| [geatendimento_parar_servico](#geatendimento_parar_servico) | `GEATENDIMENTO_PARAR_SERVICO` | 1 | pequeno | — |
| [geatendimento_status_servico](#geatendimento_status_servico) | `GEATENDIMENTO_STATUS_SERVICO` | 1 | pequeno | — |
| [geatendimento_dados_escritorio](#geatendimento_dados_escritorio) | `GEATENDIMENTO_DADOS_ESCRITORIO` | 1 | pequeno | — |
| [geatendimento_sincronizar_empresas_da](#geatendimento_sincronizar_empresas_da) | `GEATENDIMENTO_SINCRONIZAR_EMPRESAS_DA` | 1 | pequeno | — |
| [geatendimento_status_opcoes_barra_dominio](#geatendimento_status_opcoes_barra_dominio) | `GEATENDIMENTO_STATUS_OPCOES_BARRA_DOMINIO` | 1 | pequeno | — |

## geatendimento_sgd_notificacoes_usuarios

**Notificações de suporte e notícias por usuário** — tabela `GEATENDIMENTO_SGD_NOTIFICACOES_USUARIOS` (37.928 linhas)

Notificações de suporte e notícias por usuário. 37.928 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 38.380 linhas, 0 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): codigo_da_empresa.
- A coluna de empresa (codi_emp) é nula em 100% das linhas: tabela global, sem filtro de empresa (medido em 2026-10-18).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_auto_numeracao | `codigo` | integer(4) |  |  | Codigo auto numeração |
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Codigo da empresa |
| fk_de_notificacoes | `codigo_notificacao` | integer(4) |  |  | fk de notificações |
| id_do_usuario_no_sgd | `id` | integer(4) |  |  | Id do usuario no SGD |
| status_da_notificacao_1_notificado_2_nao | `status_notificacao` | integer(4) |  |  | Status da notificação 1 - Notificado, 2 - Não Lida, 3 - Lida, 4 - Removida |

**Filtros:** `codigo_auto_numeracao` (eq/in), `fk_de_notificacoes` (eq/in)

## geatendimento_plano_contas_contabilidade

**Envio do plano de contas para a Conta Azul** — tabela `GEATENDIMENTO_PLANO_CONTAS_CONTABILIDADE` (3.948 linhas)

Envio do plano de contas para a Conta Azul. 3.948 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_CADASTRO`
- **Ordem padrão:** `DATA_CADASTRO desc`, `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3.948 linhas, 13 empresa(s), DATA_CADASTRO de 2000-01-01 a 2026-09-21.
- Colunas expostas nulas em 100% das linhas (2): data_inativacao, codi_emp_filial.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo` | integer(4) |  |  |  |
| codi_emp | `codi_emp` | integer(4) |  |  |  |
| permite_inserir_unica_acao_onvio | `permite_inserir_unica_acao_onvio` | smallint(2) |  |  |  |
| integration_key | `integration_key` | varchar(200) |  |  |  |
| c_1_nao_e_para_fazer_o_envio_0_nao_envia | `situacao_envio` | smallint(2) |  |  | -1 - Não é para fazer o envio/ 0 - Não Enviado; 1 - Enviado; 2 - Envio Pendente; 3 - Excluído; 4 - Exclusão Pendente; |
| cnpj 🔒 | `cnpj` | varchar(14) |  |  |  |
| cpf 🔒 | `cpf` | varchar(11) |  |  |  |
| razao_social 🔒 | `razao_social` | varchar(200) |  |  |  |
| c_envia_cadastro_de_conta_e_envia_altera | `tipo_alteracao` | char(1) |  |  | C - Envia Cadastro de Conta / E - Envia Alteração de Conta / D - Envia a Exclusão da conta / I - Insere Plano de Contas Completo |
| codigo_conta | `codigo_conta` | integer(4) |  |  |  |
| classificacao_conta | `classificacao_conta` | varchar(100) |  |  |  |
| tipo_conta | `tipo_conta` | char(1) |  |  |  |
| descricao_conta | `descricao_conta` | varchar(100) |  |  |  |
| data_cadastro | `data_cadastro` | date(4) |  |  |  |
| situacao_conta | `situacao_conta` | char(1) |  |  |  |
| data_inativacao | `data_inativacao` | date(4) |  |  |  |
| codi_emp_plano | `codi_emp_plano` | integer(4) |  |  |  |
| codi_emp_filial | `codi_emp_filial` | integer(4) |  |  |  |
| c_0_nao_replicou_1_replicou | `replicou_filial` | integer(4) |  |  | 0 - Não Replicou / 1 - Replicou |

**Filtros:** `codigo` (eq/in), `data_cadastro` (entre/gte/lte), `data_inativacao` (entre/gte/lte), `integration_key` (contem/prefixo), `c_1_nao_e_para_fazer_o_envio_0_nao_envia` (eq/in), `cnpj` (eq/in), `cpf` (eq/in), `razao_social` (contem/prefixo), `c_envia_cadastro_de_conta_e_envia_altera` (eq/in), `codigo_conta` (eq/in), `classificacao_conta` (contem/prefixo), `tipo_conta` (eq/in), `descricao_conta` (contem/prefixo), `situacao_conta` (eq/in)

## geatendimento_digitalbank_catalogo

**GEATENDIMENTO_DIGITALBANK_CATALOGO** — tabela `GEATENDIMENTO_DIGITALBANK_CATALOGO` (2.155 linhas)

GEATENDIMENTO_DIGITALBANK_CATALOGO. 2.155 linhas no catálogo; chave: CODI.

- **Chave:** `CODI`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_VENCIMENTO`
- **Ordem padrão:** `DATA_VENCIMENTO desc`, `CODI asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2.155 linhas, 1 empresa(s), DATA_VENCIMENTO de 2024-01-02 a 2025-08-20.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codi | `codi` | integer(4) |  |  |  |
| codi_emp | `codi_emp` | integer(4) |  |  |  |
| valor | `valor` | numeric(13) |  |  |  |
| id_transacao | `id_transacao` | char(50) |  |  |  |
| data_vencimento | `data_vencimento` | date(4) |  |  |  |
| data_pagamento | `data_pagamento` | date(4) |  |  |  |
| acao_processada | `acao_processada` | bit(1) |  |  |  |
| cpf 🔒 | `cpf` | char(11) |  |  |  |
| origem | `origem` | varchar(100) |  |  |  |
| modulo | `modulo` | smallint(2) |  |  |  |
| codigo_de_identificacao_do_banco | `codigo_banco` | integer(4) |  |  | Codigo de identificacão do banco |

**Filtros:** `codi` (eq/in), `data_vencimento` (entre/gte/lte), `data_pagamento` (entre/gte/lte), `id_transacao` (contem/prefixo), `cpf` (eq/in), `origem` (contem/prefixo), `codigo_de_identificacao_do_banco` (eq/in)

## geatendimento_sgd_notificacoes

**Notificações de suporte e notícias** — tabela `GEATENDIMENTO_SGD_NOTIFICACOES` (2.053 linhas)

Notificações de suporte e notícias. 2.053 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2.070 linhas, 0 empresa(s).
- Colunas expostas nulas em 100% das linhas (2): codigo_da_empresa, status_da_notificacao_1_notificado_2_nao.
- A coluna de empresa (codi_emp) é nula em 100% das linhas: tabela global, sem filtro de empresa (medido em 2026-10-18).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_auto_numeracao | `codigo` | integer(4) |  |  | Codigo auto numeração |
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Codigo da empresa |
| classificacao | `classificacao` | integer(4) |  |  | Classificação da notificação 2 - Suporte, 3 - Noticias |
| cliente_no_sgd | `cliente` | integer(4) |  |  | Cliente no SGD |
| status_da_notificacao_1_notificado_2_nao | `status` | integer(4) |  |  | Status da notificação 1 - Notificado, 2 - Não Lida, 3 - Lida, 4 - Removida |
| id_da_notificacao_no_sgd | `id` | integer(4) |  |  | Id da notificação no SGD |

**Filtros:** `codigo_auto_numeracao` (eq/in)

## geatendimento_codigo_empresa

**Relação de empresas no Contábil e Domínio Atendimento** — tabela `GEATENDIMENTO_CODIGO_EMPRESA` (2.005 linhas)

Relação de empresas no Contábil e Domínio Atendimento. 2.005 linhas no catálogo; chave: CODI_EMP_CONTABIL, CODI_SEQ_ATENDIMENTO, STATUS.

- **Chave:** `CODI_EMP_CONTABIL, CODI_SEQ_ATENDIMENTO, STATUS`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODI_EMP_CONTABIL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2.005 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codi_emp_contabil | `codi_emp_contabil` | integer(4) |  |  |  |
| codi_seq_atendimento | `codi_seq_atendimento` | integer(4) |  |  |  |
| c_1_usando_codigo_empresa_ativa_0_empres | `status` | integer(4) |  |  | 1-Usando código (empresa ativa) 0-Empresa Excluída |

**Filtros:** `codi_emp_contabil` (eq/in), `codi_seq_atendimento` (eq/in)

## geatendimento_mimetype

**Tipos de arquivos que são enviados para ASIS** — tabela `GEATENDIMENTO_MIMETYPE` (818 linhas)

Tipos de arquivos que são enviados para ASIS. 818 linhas no catálogo; chave: SEQUENCIAL.

- **Chave:** `SEQUENCIAL`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 818 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| chave_primaria | `sequencial` | integer(4) |  |  | Chave Primaria |
| extensao_do_arquivo | `extensao` | varchar(50) |  |  | Extensao do arquivo |
| mime_type_equivalente_a_extensao_do_arqu | `mime` | varchar(100) |  |  | Mime type equivalente a extensao do arquivo |

**Filtros:** `chave_primaria` (eq/in), `extensao_do_arquivo` (contem/prefixo), `mime_type_equivalente_a_extensao_do_arqu` (contem/prefixo)

## geatendimento_telemetria

**Dados de integração para telemetria** — tabela `GEATENDIMENTO_TELEMETRIA` (407 linhas)

Dados de integração para telemetria. 407 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 373 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_unico_na_tabela | `codigo` | integer(4) |  |  | Código único na tabela |
| situacao_n_nao_enviado_e_enviado_r_erro | `status` | char(1) |  |  | Situação N - Não enviado / E - Enviado / R - Erro |
| nome_do_servico_para_telemetria | `servico` | varchar(100) |  |  | Nome do serviço para telemetria |
| statuscode_de_retorno_da_requisicao | `codigo_status` | varchar(10) |  |  | Statuscode de retorno da requisição |
| mensagem_de_retorno_da_requisicao | `mensagem` | varchar(255) |  |  | Mensagem de retorno da requisição |
| nome_do_source_para_a_telemetria | `source` | varchar(100) |  |  | Nome do source para a telemetria |

**Filtros:** `codigo_unico_na_tabela` (eq/in), `situacao_n_nao_enviado_e_enviado_r_erro` (eq/in), `nome_do_servico_para_telemetria` (contem/prefixo), `statuscode_de_retorno_da_requisicao` (eq/in), `mensagem_de_retorno_da_requisicao` (contem/prefixo), `nome_do_source_para_a_telemetria` (contem/prefixo)

## geatendimento_onvio_empresas_ignoradas

**Erros de empresas enviadas ao Onvio ignorados.** — tabela `GEATENDIMENTO_ONVIO_EMPRESAS_IGNORADAS` (345 linhas)

Erros de empresas enviadas ao Onvio ignorados.. 345 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 345 linhas, 345 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): mensagem_do_erro.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| sequencial_autoincremento | `codigo` | integer(4) |  |  | Sequencial autoincremento |
| codigo_da_acao | `codigo_acao` | integer(4) |  |  | Código da ação |
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| mensagem_do_erro | `mensagem` | varchar(4096) |  |  | Mensagem do erro |
| versao_do_agente_em_que_foi_gerado_o_err | `versao_agente` | varchar(8) |  |  | Versão do Agente em que foi gerado o erro |

**Filtros:** `sequencial_autoincremento` (eq/in), `codigo_da_acao` (eq/in), `mensagem_do_erro` (contem/prefixo), `versao_do_agente_em_que_foi_gerado_o_err` (eq/in)

## geatendimento_sincronizar_dados

**Tabela para sincronizar dados com o atendimento** — tabela `GEATENDIMENTO_SINCRONIZAR_DADOS` (68 linhas)

Tabela para sincronizar dados com o atendimento. 68 linhas no catálogo; chave: I_ACOES.

- **Chave:** `I_ACOES`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ACOES asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 68 linhas, 27 empresa(s).
- Vínculo geempre (geempre): 0 de 3 linhas sem registro relacionado (empresa 10052).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| i_acoes | `i_acoes` | integer(4) |  |  |  |
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_da_empresa_no_dominio_atendimento | `codi_emp_atendimento` | integer(4) |  |  | Código da empresa no Domínio atendimento |
| tipo_da_informacao_que_sera_enviada | `tipo` | integer(4) |  |  | Tipo da informação que será enviada |
| codigo_sequencial_da_tabela_que_armazena | `codigo` | integer(4) |  |  | Código sequencial da tabela que armazena os dados que serão enviados. |
| acao_1_novo_atualizar_2_excluir | `acao` | smallint(2) |  |  | Acao 1=Novo/Atualizar - 2=Excluir |
| concluido | `concluido` | smallint(2) |  |  |  |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `i_acoes` (eq/in), `codigo_da_empresa_no_dominio_atendimento` (eq/in), `tipo_da_informacao_que_sera_enviada` (eq/in), `codigo_sequencial_da_tabela_que_armazena` (eq/in)

## geatendimento_dados_escritorio_historico

**Tabela de histórico de mudança da tabela GEATENDIMENTO_DADOS_ESCRITORIO** — tabela `GEATENDIMENTO_DADOS_ESCRITORIO_HISTORICO` (17 linhas)

Tabela de histórico de mudança da tabela GEATENDIMENTO_DADOS_ESCRITORIO. 17 linhas no catálogo; chave: SEQUENCIAL.

- **Chave:** `SEQUENCIAL`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 17 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| sequencial | `sequencial` | integer(4) |  |  |  |
| codigo_cliente | `codigo_cliente` | integer(4) |  |  |  |
| situacao_antiga | `situacao_antiga` | smallint(2) |  |  |  |
| situacao_nova | `situacao_nova` | smallint(2) |  |  |  |
| mensagem_detalhe | `mensagem_detalhe` | varchar(512) |  |  |  |
| estagio_migracao_com_dados | `estagio_migracao_com_dados` | integer(4) |  |  |  |
| estagio_migracao_com_dados_temp | `estagio_migracao_com_dados_temp` | integer(4) |  |  |  |
| indica_que_o_cliente_possui_boxe_ativo_o | `boxe_ativo` | integer(4) |  |  | Indica que o cliente possui boxe ativo ou empresas manifesto |

**Filtros:** `sequencial` (eq/in), `codigo_cliente` (eq/in), `situacao_antiga` (eq/in), `situacao_nova` (eq/in), `mensagem_detalhe` (contem/prefixo)

## geatendimento_bancos_iceberg

**Cadastro de Instituições Financeiras para o Iceberg** — tabela `GEATENDIMENTO_BANCOS_ICEBERG` (15 linhas)

Cadastro de Instituições Financeiras para o Iceberg. 15 linhas no catálogo; chave: CODIGO_BANCO.

- **Chave:** `CODIGO_BANCO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODIGO_BANCO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 15 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_instituicao_financeira | `codigo_banco` | integer(4) |  |  | Código da Instituição Financeira |
| nome_da_instituicao_financeira | `descricao_banco` | varchar(100) |  |  | Nome da Instituição Financeira |
| identificador_da_instituicao_financeira | `nome_banco` | varchar(100) |  |  | Identificador da Instituição Financeira |
| identificador_do_banco_central_para_part | `numero_codigo_bc` | char(3) |  |  | Identificador do Banco Central para participantes do Sistema de Transferências de Reservas. |
| informa_se_a_instituicao_usa_conexao_dir | `conexao_direta` | integer(4) |  |  | Informa se a instituição usa conexão direta |

**Filtros:** `codigo_da_instituicao_financeira` (eq/in), `nome_da_instituicao_financeira` (contem/prefixo), `identificador_da_instituicao_financeira` (contem/prefixo), `identificador_do_banco_central_para_part` (eq/in)

## geatendimento_log_catalogo

**Log dos Catalogos de NF-e retornados do servidor.** — tabela `GEATENDIMENTO_LOG_CATALOGO` (9 linhas)

Log dos Catalogos de NF-e retornados do servidor.. 9 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 9 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| campo_auto_numeraaao_identificaaao_do_re | `codigo` | integer(4) |  |  | Campo auto numeraÃ§Ã£o identificaÃ§Ã£o do registro |
| xml_do_catalogo_retornado_do_servidor | `catalogo` | xml(32767) |  |  | XML do Catalogo retornado do servidor |

**Filtros:** `campo_auto_numeraaao_identificaaao_do_re` (eq/in)

## geatendimento_escritorio

**DADOS DO ESCRITORIO NO ATENDIMENTO** — tabela `GEATENDIMENTO_ESCRITORIO` (2 linhas)

DADOS DO ESCRITORIO NO ATENDIMENTO. 2 linhas no catálogo; chave: CODIGO_CLIENTE.

- **Chave:** `CODIGO_CLIENTE`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODIGO_CLIENTE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| coluna_depreciada_nao_representa_o_codig | `codigo_cliente` | integer(4) |  |  | Coluna depreciada. Não representa o código do cliente. |
| usa_servico_nfe | `usa_servico_nfe` | smallint(2) |  |  |  |

**Filtros:** `coluna_depreciada_nao_representa_o_codig` (eq/in)

## geatendimento_bloco_informacoes

**Informações para o Onbalance** — tabela `GEATENDIMENTO_BLOCO_INFORMACOES` (2 linhas)

Informações para o Onbalance. 2 linhas no catálogo; chave: ID_BLOCO_INFORMACOES.

- **Chave:** `ID_BLOCO_INFORMACOES`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `ID_BLOCO_INFORMACOES asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| id_bloco_informacoes | `id_bloco_informacoes` | integer(4) |  |  |  |
| nome_tag | `nome_tag` | varchar(128) |  |  |  |

**Filtros:** `id_bloco_informacoes` (eq/in), `nome_tag` (contem/prefixo)

## geatendimento_controle_requisicoes

**Controle de requisições para download de notas** — tabela `GEATENDIMENTO_CONTROLE_REQUISICOES` (1 linhas)

Controle de requisições para download de notas. 1 linhas no catálogo; chave: I_SEQUENCIAL.

- **Chave:** `I_SEQUENCIAL`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `I_SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| sequencial_unico | `i_sequencial` | integer(4) |  |  | SEQUENCIAL UNICO |
| nome_maquina | `nome_maquina` | varchar(512) |  |  |  |
| id_da_conexao_responsavel_pelo_processo | `conection_id` | integer(4) |  |  | ID da conexÃ£o responsavel pelo processo |

**Filtros:** `sequencial_unico` (eq/in), `nome_maquina` (contem/prefixo)

## geatendimento_parar_servico

**Controle de parada de serviço do Agente de Comunicação** — tabela `GEATENDIMENTO_PARAR_SERVICO` (1 linhas)

Controle de parada de serviço do Agente de Comunicação. 1 linhas no catálogo; chave: PARAR_SERVICO.

- **Chave:** `PARAR_SERVICO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `PARAR_SERVICO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| c_1_parar_serviao_2_iniciar_serviao_3_pa | `parar_servico` | integer(4) |  |  | 1 - PARAR SERVIÃ‡O; 2 - INICIAR SERVIÃ‡O; 3 - PARAR TOTALMENTE; 4 - REINICIAR SERVIÃ‡O; 5 - AGUARDAR RECONEXÃƒO |

**Filtros:** `c_1_parar_serviao_2_iniciar_serviao_3_pa` (eq/in)

## geatendimento_status_servico

**Controle de conexão do Agente de Comunicação** — tabela `GEATENDIMENTO_STATUS_SERVICO` (1 linhas)

Controle de conexão do Agente de Comunicação. 1 linhas no catálogo; chave: I_SEQUENCIAL.

- **Chave:** `I_SEQUENCIAL`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `I_SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| pk_sempre_1_para_realizar_o_controle_de | `i_sequencial` | integer(4) |  |  | PK (SEMPRE 1) PARA REALIZAR O CONTROLE DE CONCORRENCIA |
| status_da_coneccao_com_o_dominio_atendim | `status_conectado` | integer(4) |  |  | STATUS DA CONECÇÃO COM O DOMINIO ATENDIMENTO 0-INATIVO 1-ATIVO |
| ping_no_website_0_website_offline_1_webs | `status_internet_atendimento` | integer(4) |  |  | PING NO WEBSITE 0-WEBSITE OFFLINE 1-WEBSITE ONLINE |
| ping_no_website_integra_0_website_offlin | `status_internet_integra` | integer(4) |  |  | PING NO WEBSITE INTEGRA 0-WEBSITE OFFLINE 1-WEBSITE ONLINE |
| c_1_login_com_sucesso_1_problema_no_logi | `status_login_atendimento` | integer(4) |  |  | 1-LOGIN COM SUCESSO -1 -PROBLEMA NO LOGIN |
| status_login_integra | `status_login_integra` | integer(4) |  |  | 1-LOGIN COM SUCESSO -1 -PROBLEMA NO LOGIN |
| nome_da_maquina_em_execucao_do_servico | `nome_maquina` | varchar(200) |  |  | NOME DA MAQUINA EM EXECUCAO DO SERVICO |
| coluna_para_realizar_o_controle_de_conco | `pendente_atendimento` | integer(4) |  |  | COLUNA PARA REALIZAR O CONTROLE DE CONCORRENCIA |
| status_login_atendimento_da_legado | `status_login_atendimento_da_legado` | integer(4) |  |  | 1-LOGIN COM SUCESSO -1 -PROBLEMA NO LOGIN. Coluna exclusa para o Dominio Atendimento Legado |

**Filtros:** `pk_sempre_1_para_realizar_o_controle_de` (eq/in), `nome_da_maquina_em_execucao_do_servico` (contem/prefixo)

## geatendimento_dados_escritorio

**Dados obtidos do SGD à respeito do escritório** — tabela `GEATENDIMENTO_DADOS_ESCRITORIO` (1 linhas)

Dados obtidos do SGD à respeito do escritório. 1 linhas no catálogo; chave: CODIGO_CLIENTE.

- **Chave:** `CODIGO_CLIENTE`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODIGO_CLIENTE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_cliente_do_sgd | `codigo_cliente` | integer(4) |  |  | Código do cliente do SGD |
| situacao_do_ambiente_utilizado_do_atendi | `situacao` | smallint(2) |  |  | Situação do ambiente utilizado do Atendimento: 1 - Ambiente DA, 5 - Ambiente Onvio nativo, 6 - Convertido SGD x Onvio, 7 - Em Processo de migração sem dados, 8 - Migrado Onvio sem dados, 9 - Ambiente Onvio Migrado com Dados, 10 - Cliente reativou contrato com Portal do Cliente |
| indica_que_os_usuarios_do_sgd_estao_em_c | `usuarios_em_conversao_sgd` | bit(1) |  |  | Indica que os usuários do SGD estão em conversão para o Onvio |
| c_0_sem_migracao_cadastrada_1_iniciar_mi | `estagio_migracao_com_dados` | integer(4) |  |  | 0 - Sem migração cadastrada, 1 - Iniciar migração DA Onvio, 2 - Sincronização DA iniciada, 3 - Sincronização DA finalizada, 5 - Sincronização DA com erro, 10 - Migração Swift iniciada, 11 - Migração Swift finalizada, 15 - Migração Swift com erro, 20 - Sincronização de códigos Swift iniciada, 21 - Sincronização de códigos Swift finalizada, 25 - Sincronização de códigos Swift com erro, 30 - Swift enviar e-mail iniciado, 31 - Swift enviar e-mail finalizado, 35 - Swift enviar e-mail erro, 40 - Swift interromper migração iniciado, 41 - Swift interromper migração finalizado, 45 - Swift interromper migração erro, 50 - Swift Rollback iniciado, 51 - Swift Rollback finalizado, 55 - Swift Rollback erro, 60 - Agente Rollback iniciado, 61 - Agente Rollback finalizado, 65 - Agente Rollback erro |
| estagio_migracao_com_dados_temp | `estagio_migracao_com_dados_temp` | integer(4) |  |  | 0 - Sem migração cadastrada, 1 - Iniciar migração DA Onvio, 2 - Sincronização DA iniciada, 3 - Sincronização DA finalizada, 5 - Sincronização DA com erro, 10 - Migração Swift iniciada, 11 - Migração Swift finalizada, 15 - Migração Swift com erro, 20 - Sincronização de códigos Swift iniciada, 21 - Sincronização de códigos Swift finalizada, 25 - Sincronização de códigos Swift com erro, 30 - Swift enviar e-mail iniciado, 31 - Swift enviar e-mail finalizado, 35 - Swift enviar e-mail erro, 40 - Swift interromper migração iniciado, 41 - Swift interromper migração finalizado, 45 - Swift interromper migração erro, 50 - Swift Rollback iniciado, 51 - Swift Rollback finalizado, 55 - Swift Rollback erro, 60 - Agente Rollback iniciado, 61 - Agente Rollback finalizado, 65 - Agente Rollback erro |
| ultimo_sequencial_nfe_disponivel_legado | `ultimo_sequencial_nfe_disponivel_legado` | bigint(8) |  |  |  |
| ultimo_sequencial_nfe_baixado_legado | `ultimo_sequencial_nfe_baixado_legado` | bigint(8) |  |  |  |
| informacao_de_se_o_cliente_usa_manifesto | `boxe_ativo` | integer(4) |  |  | Informação de se o cliente usa manifesto ou BOX-e, campo criado pois informação da tabela GEATENDIMENTO_ESCRITORIO não considera manifesto |

**Filtros:** `codigo_do_cliente_do_sgd` (eq/in), `situacao_do_ambiente_utilizado_do_atendi` (eq/in)

## geatendimento_sincronizar_empresas_da

**Tabela para controla de sincronia das empresas do DA para remarcação do módulo Atendimento** — tabela `GEATENDIMENTO_SINCRONIZAR_EMPRESAS_DA` (1 linhas)

Tabela para controla de sincronia das empresas do DA para remarcação do módulo Atendimento. 1 linhas no catálogo; chave: SINCRONIZADO, ATIVACAO_USUARIOS_CONCLUIDA.

- **Chave:** `SINCRONIZADO, ATIVACAO_USUARIOS_CONCLUIDA`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `SINCRONIZADO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| sincronizado | `sincronizado` | integer(4) |  |  |  |
| ativacao_usuarios_concluida | `ativacao_usuarios_concluida` | bit(1) |  |  |  |

**Filtros:** `sincronizado` (eq/in)

## geatendimento_status_opcoes_barra_dominio

**No Contábil a thread responsável por habilitar/desabilitar os botões da barra da Domino, verifica os valores nesta tabela.** — tabela `GEATENDIMENTO_STATUS_OPCOES_BARRA_DOMINIO` (1 linhas)

No Contábil a thread responsável por habilitar/desabilitar os botões da barra da Domino, verifica os valores nesta tabela.. 1 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_sempre_existira_apenas_uma_linha | `codigo` | integer(4) |  |  | Código, sempre existirá apenas uma linha |
| c_1_habilitar_2_desabilitar_status_do_fa | `habilitar_importacao_documentos_modulo_escrita_fiscal` | bit(1) |  |  | 1 - Habilitar, 2 - Desabilitar. Status do farol referente ao painel de importação de documentos no módulo Escrita Fiscal. |
| habilitar_importacao_documentos_modulo_f | `habilitar_importacao_documentos_modulo_folha` | bit(1) |  |  | 1 - Habilitar, 2 - Desabilitar. Status do farol referente ao painel de importação de documentos no módulo Folha. |

**Filtros:** `codigo_sempre_existira_apenas_uma_linha` (eq/in)

## Domínios (significado dos códigos)

`confirmado`: **sim** = vem do comentário do banco e/ou foi conferido nos dados; **parcial** = parte dos valores; **não** = hipótese, não use como regra.

### status_empresa

Situação da empresa no cadastro (geempre.stat_emp)

Confirmado: sim

| Código | Significado |
|---|---|
| A | Ativa |
| I | Inativa |
| C | Em constituição |
| M | Ativo sem movimento |
| B | Em processo de baixa |
| E | Excluindo |

### motivo_inatividade

Motivo da inatividade (geempre.tipoi_emp). Só aparece em empresas inativas.

Confirmado: sim

| Código | Significado |
|---|---|
| 1 | Outros |
| 2 | Baixada |
| 3 | Transferida |
| 4 | Inadimplente |

### tipo_inscricao

Tipo da inscrição (CNPJ/CPF/CEI/CAEPF)

Confirmado: sim

| Código | Significado |
|---|---|
| 1 | CNPJ |
| 2 | CPF |
| 3 | CEI |
| 6 | CAEPF |

### regime_federal_empresa

Regime federal da folha (geempre.rfed_emp)

Confirmado: parcial

| Código | Significado |
|---|---|
| 1 | Normal |
| 2 | Microempresa |
| 3 | Empresa de pequeno porte |

### tipo_honorario_empresa

Como a empresa usa o módulo Honorários (geempre.honorario_tipo)

Confirmado: sim

| Código | Significado |
|---|---|
| E | Escritório (quem fatura) |
| C | Cliente |

### sim_nao_texto

Confirmado: sim

| Código | Significado |
|---|---|
| S | Sim |
| N | Não |

### sim_nao_numerico

Confirmado: sim

| Código | Significado |
|---|---|
| 1 | Sim |
| 0 | Não |

