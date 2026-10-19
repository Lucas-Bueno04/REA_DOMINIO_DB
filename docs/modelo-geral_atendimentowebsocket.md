# Modelo — Geral - atendimentowebsocket (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/geral_atendimentowebsocket.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

9 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [geatendimentowebsocket_onvio_rota_lancamentos_contabeis](#geatendimentowebsocket_onvio_rota_lancamentos_contabeis) | `GEATENDIMENTOWEBSOCKET_ONVIO_ROTA_LANCAMENTOS_CONTABEIS` | 128.090 | medio | um de: codigo_sequencial |
| [geatendimentowebsocket_onvio_rota_emp_ativas_boxe](#geatendimentowebsocket_onvio_rota_emp_ativas_boxe) | `GEATENDIMENTOWEBSOCKET_ONVIO_ROTA_EMP_ATIVAS_BOXE` | 9.084 | pequeno | — |
| [geatendimentowebsocket_onvio_rota_lancamento_iceberg](#geatendimentowebsocket_onvio_rota_lancamento_iceberg) | `GEATENDIMENTOWEBSOCKET_ONVIO_ROTA_LANCAMENTO_ICEBERG` | 6.948 | pequeno | — |
| [geatendimentowebsocket_sgd_notificacoes](#geatendimentowebsocket_sgd_notificacoes) | `GEATENDIMENTOWEBSOCKET_SGD_NOTIFICACOES` | 3.035 | pequeno | — |
| [geatendimentowebsocket_onvio_rota_conta_iceberg](#geatendimentowebsocket_onvio_rota_conta_iceberg) | `GEATENDIMENTOWEBSOCKET_ONVIO_ROTA_CONTA_ICEBERG` | 86 | pequeno | — |
| [geatendimentowebsocket_onvio_rota_brclient_conflitos_motivos](#geatendimentowebsocket_onvio_rota_brclient_conflitos_motivos) | `GEATENDIMENTOWEBSOCKET_ONVIO_ROTA_BRCLIENT_CONFLITOS_MOTIVOS` | 4 | pequeno | — |
| [geatendimentowebsocket_onvio_rota_lancamento_controle](#geatendimentowebsocket_onvio_rota_lancamento_controle) | `GEATENDIMENTOWEBSOCKET_ONVIO_ROTA_LANCAMENTO_CONTROLE` | 1 | pequeno | — |
| [geatendimentowebsocket_onvio_rota_conta_controle](#geatendimentowebsocket_onvio_rota_conta_controle) | `GEATENDIMENTOWEBSOCKET_ONVIO_ROTA_CONTA_CONTROLE` | 1 | pequeno | — |
| [geatendimentowebsocket_onvio_rota_openbanking_controle](#geatendimentowebsocket_onvio_rota_openbanking_controle) | `GEATENDIMENTOWEBSOCKET_ONVIO_ROTA_OPENBANKING_CONTROLE` | 1 | pequeno | — |

## geatendimentowebsocket_onvio_rota_lancamentos_contabeis

**Armazena mensagens recebidos pelo websocket referente a rota que informa as empresas que utilizam Lançamentos Contábeis.** — tabela `GEATENDIMENTOWEBSOCKET_ONVIO_ROTA_LANCAMENTOS_CONTABEIS` (128.090 linhas)

Armazena mensagens recebidos pelo websocket referente a rota que informa as empresas que utilizam Lançamentos Contábeis.. 128.090 linhas no catálogo; chave: CODI, FILE_GUID.

- **Chave:** `CODI, FILE_GUID`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—` · exige um de: `codigo_sequencial`
- **Ordem padrão:** `CODI asc`, `FILE_GUID asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 128.090 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_sequencial | `codi` | integer(4) |  |  | Código sequencial. |
| file_guid | `file_guid` | uniqueidentifier(16) |  |  |  |
| hasmore | `hasmore` | bit(1) |  |  |  |
| package | `package` | bit(1) |  |  |  |
| c_0_nao_1_sim_informa_se_a_mensagem_foi | `acao_processada` | bit(1) |  |  | 0-Não/1-Sim. Informa se a mensagem foi processada pela thread responsável. |

**Filtros:** `codigo_sequencial` (eq/in), `file_guid` (eq/in)

## geatendimentowebsocket_onvio_rota_emp_ativas_boxe

**Armazena mensagens recebidos pelo websocket referente a rota que informa as empresas que utilizam box-e/manifesto.** — tabela `GEATENDIMENTOWEBSOCKET_ONVIO_ROTA_EMP_ATIVAS_BOXE` (9.084 linhas)

Armazena mensagens recebidos pelo websocket referente a rota que informa as empresas que utilizam box-e/manifesto.. 9.084 linhas no catálogo; chave: CODI.

- **Chave:** `CODI`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODI asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 9.108 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_sequencial | `codi` | integer(4) |  |  | CÃ³digo sequencial. |
| c_0_nao_1_sim_informa_se_a_mensagem_foi | `acao_processada` | bit(1) |  |  | 0-NÃ£o/1-Sim. Informa se a mensagem foi processada pela thread responsÃ¡vel. |
| c_1_boxe_2_manifesto | `tipo_ativacao` | tinyint(1) |  |  | 1-Boxe/2-Manifesto |

**Filtros:** `codigo_sequencial` (eq/in), `c_1_boxe_2_manifesto` (eq/in)

## geatendimentowebsocket_onvio_rota_lancamento_iceberg

**Armazena mensagens recebidos pelo websocket referente a rota que busca as transações do Iceberg** — tabela `GEATENDIMENTOWEBSOCKET_ONVIO_ROTA_LANCAMENTO_ICEBERG` (6.948 linhas)

Armazena mensagens recebidos pelo websocket referente a rota que busca as transações do Iceberg. 6.948 linhas no catálogo; chave: CODI.

- **Chave:** `CODI`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODI asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 6.948 linhas.
- Colunas expostas nulas em 100% das linhas (3): parceiro_de_conexao_open_banking, versao_do_schema_do_payload_da_fintech, sequencial_do_json_que_atualizou_a_linha.
- situacao_da_transacao_apos_processamento: todos os valores reais estão no comentário do banco (1=6.948).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_sequencial | `codi` | integer(4) |  |  | Código sequencial. |
| c_2_transacoes_ignoradas_1_automacao_0_p | `acao_processada` | integer(4) |  |  | -2 - Transações ignoradas, -1 - Automação, 0 - Pendentes, 1 - Processadas, 2 - Não implementado, 4 - Pendente de Reprocessar |
| messageid_do_payload | `message_id` | varchar(50) |  |  | messageID do PayLoad |
| clientid_do_payload | `client_id` | varchar(50) |  |  | clientId do PayLoad |
| messageorigin_do_payload | `message_origin` | varchar(50) |  |  | messageOrigin do PayLoad |
| identificador_da_transacao | `id_transacao` | varchar(50) |  |  | Identificador da transação |
| identificador_da_transacao_por_client_id | `transaction_id` | varchar(50) |  |  | Identificador da transação por client_id |
| parceiro_de_conexao_open_banking | `partner` | varchar(100) |  |  | Parceiro de conexão Open Banking |
| versao_do_schema_do_payload_da_fintech | `schema_version` | varchar(10) |  |  | Versão do schema do payload da fintech |
| situacao_da_transacao_apos_processamento | `status_transacao` | integer(4) |  | geatendimentowebsocket_onvio_rota_lancamento_iceberg_situacao_da | Situação da transação após processamento (1=Transação Original/2=Atualizada/3=Atualizada Apos Fechamento/4=Excluida Apos Fechamento/5=Atualizada Com Vinculo/6=Excluida Com Vinculo) |
| sequencial_do_json_que_atualizou_a_linha | `codi_history` | integer(4) |  |  | Sequencial do JSON que atualizou a linha original |
| consent_id_da_transacao | `consent_id` | varchar(100) |  |  | Consent_id da transação |

**Filtros:** `codigo_sequencial` (eq/in), `messageid_do_payload` (contem/prefixo), `clientid_do_payload` (contem/prefixo), `messageorigin_do_payload` (contem/prefixo), `identificador_da_transacao` (contem/prefixo), `identificador_da_transacao_por_client_id` (contem/prefixo), `parceiro_de_conexao_open_banking` (contem/prefixo), `versao_do_schema_do_payload_da_fintech` (eq/in), `sequencial_do_json_que_atualizou_a_linha` (eq/in), `consent_id_da_transacao` (contem/prefixo)

## geatendimentowebsocket_sgd_notificacoes

**Notificações de suporte e notícias recebidas pelo websocket** — tabela `GEATENDIMENTOWEBSOCKET_SGD_NOTIFICACOES` (3.035 linhas)

Notificações de suporte e notícias recebidas pelo websocket. 3.035 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3.045 linhas, 0 empresa(s).
- Colunas expostas nulas em 100% das linhas (2): codigo_da_empresa, tipo_de_ativacao.
- A coluna de empresa (codi_emp) é nula em 100% das linhas: tabela global, sem filtro de empresa (medido em 2026-10-18).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_auto_numeracao | `codigo` | integer(4) |  |  | Codigo auto numeração |
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Codigo da empresa |
| marca_se_a_mensagem_foi_processada | `acao_processada` | bit(1) |  |  | Marca se a mensagem foi processada |
| tipo_de_ativacao | `tipo_ativacao` | tinyint(1) |  |  | Tipo de ativação |

**Filtros:** `codigo_auto_numeracao` (eq/in), `tipo_de_ativacao` (eq/in)

## geatendimentowebsocket_onvio_rota_conta_iceberg

**Armazena mensagens recebidos pelo websocket referente a rota que busca as contas financeiras do Iceberg** — tabela `GEATENDIMENTOWEBSOCKET_ONVIO_ROTA_CONTA_ICEBERG` (86 linhas)

Armazena mensagens recebidos pelo websocket referente a rota que busca as contas financeiras do Iceberg. 86 linhas no catálogo; chave: CODI.

- **Chave:** `CODI`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODI asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 86 linhas.
- Colunas expostas nulas em 100% das linhas (4): messageid_do_payload, identificador_do_consentimento_open_bank, parceiro_de_conexao_open_banking, versao_do_schema_do_payload_da_fintech.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_sequencial | `codi` | integer(4) |  |  | Código sequencial. |
| c_0_nao_1_sim_2_aguardando_informa_se_a | `acao_processada` | integer(4) |  |  | 0-Não/1-Sim/2-aguardando. Informa se a mensagem foi processada pela thread responsável. |
| messageid_do_payload | `message_id` | varchar(50) |  |  | messageId do Payload |
| identificador_do_consentimento_open_bank | `consent_id` | varchar(50) |  |  | Identificador do consentimento Open Banking |
| parceiro_de_conexao_open_banking | `partner` | varchar(100) |  |  | Parceiro de conexão Open Banking |
| versao_do_schema_do_payload_da_fintech | `schema_version` | varchar(10) |  |  | Versão do schema do payload da fintech |

**Filtros:** `codigo_sequencial` (eq/in), `messageid_do_payload` (contem/prefixo), `identificador_do_consentimento_open_bank` (contem/prefixo), `parceiro_de_conexao_open_banking` (contem/prefixo), `versao_do_schema_do_payload_da_fintech` (eq/in)

## geatendimentowebsocket_onvio_rota_brclient_conflitos_motivos

**Motivo do conflito no envio das informações para o BRClient** — tabela `GEATENDIMENTOWEBSOCKET_ONVIO_ROTA_BRCLIENT_CONFLITOS_MOTIVOS` (4 linhas)

Motivo do conflito no envio das informações para o BRClient. 4 linhas no catálogo; chave: GUID.

- **Chave:** `GUID`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `GUID asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| id_do_registro | `guid` | uniqueidentifier(16) |  |  | ID do registro |
| a_causa_do_conflito | `motivo` | varchar(150) |  |  | A causa do conflito |
| sugestao_para_resolucao_do_conflito | `sugestao` | varchar(300) |  |  | Sugestão para resolução do conflito |

**Filtros:** `id_do_registro` (eq/in), `a_causa_do_conflito` (contem/prefixo), `sugestao_para_resolucao_do_conflito` (contem/prefixo)

## geatendimentowebsocket_onvio_rota_lancamento_controle

**Tabela de controle de lançamentos pra o Domínio Inova** — tabela `GEATENDIMENTOWEBSOCKET_ONVIO_ROTA_LANCAMENTO_CONTROLE` (1 linhas)

Tabela de controle de lançamentos pra o Domínio Inova. 1 linhas no catálogo; chave: EVENT_DATE.

- **Chave:** `EVENT_DATE`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `EVENT_DATE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| event_date | `event_date` | timestamp(8) |  |  |  |

**Filtros:** `event_date` (eq/in)

## geatendimentowebsocket_onvio_rota_conta_controle

**Tabela de controle para o Domínio Inova** — tabela `GEATENDIMENTOWEBSOCKET_ONVIO_ROTA_CONTA_CONTROLE` (1 linhas)

Tabela de controle para o Domínio Inova. 1 linhas no catálogo; chave: EVENT_DATE.

- **Chave:** `EVENT_DATE`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `EVENT_DATE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| event_date | `event_date` | timestamp(8) |  |  |  |

**Filtros:** `event_date` (eq/in)

## geatendimentowebsocket_onvio_rota_openbanking_controle

**Tabela de controle de Offset de operações Open Banking** — tabela `GEATENDIMENTOWEBSOCKET_ONVIO_ROTA_OPENBANKING_CONTROLE` (1 linhas)

Tabela de controle de Offset de operações Open Banking. 1 linhas no catálogo; chave: EVENT_DATE.

- **Chave:** `EVENT_DATE`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `EVENT_DATE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas.
- Colunas expostas nulas em 100% das linhas (1): informa_lasteventdate_ao_realizar_subscr.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| informa_lasteventdate_ao_realizar_subscr | `event_date` | timestamp(8) |  |  | Informa lastEventDate ao realizar subscribe no WebSocket |

**Filtros:** `informa_lasteventdate_ao_realizar_subscr` (eq/in)

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

### geatendimentowebsocket_onvio_rota_lancamento_iceberg_situacao_da

Confirmado: sim

> Todos os valores observados em GEATENDIMENTOWEBSOCKET_ONVIO_ROTA_LANCAMENTO_ICEBERG.STATUS_TRANSACAO estão no comentário do banco (2026-10-18). Distribuição: 1=6.948.

| Código | Significado |
|---|---|
| 1 | Transação Original |
| 2 | Atualizada |
| 3 | Atualizada Apos Fechamento |
| 4 | Excluida Apos Fechamento |
| 5 | Atualizada Com Vinculo |
| 6 | Excluida Com Vinculo |

