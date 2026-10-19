# Modelo — Geral - controle (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/geral_controle.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

5 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [gecontrole_acessos_nao_permitidos](#gecontrole_acessos_nao_permitidos) | `GECONTROLE_ACESSOS_NAO_PERMITIDOS` | 272 | pequeno | — |
| [gecontrole_execucao_threads](#gecontrole_execucao_threads) | `GECONTROLE_EXECUCAO_THREADS` | 2 | pequeno | — |
| [gecontrole_imposto_retido](#gecontrole_imposto_retido) | `GECONTROLE_IMPOSTO_RETIDO` | 1 | pequeno | — |
| [gecontrole_gestta_processos](#gecontrole_gestta_processos) | `GECONTROLE_GESTTA_PROCESSOS` | 1 | pequeno | — |
| [gecontrole_dominio_processos](#gecontrole_dominio_processos) | `GECONTROLE_DOMINIO_PROCESSOS` | 1 | pequeno | — |

## gecontrole_acessos_nao_permitidos

**Controle de acessos excedentes ao contrato** — tabela `GECONTROLE_ACESSOS_NAO_PERMITIDOS` (272 linhas)

Controle de acessos excedentes ao contrato. 272 linhas no catálogo; chave: I_ACESSO.

- **Chave:** `I_ACESSO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `I_ACESSO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 272 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| i_acesso | `i_acesso` | integer(4) |  |  |  |

**Filtros:** `i_acesso` (eq/in)

## gecontrole_execucao_threads

**Controle de execução de threads ao abrir o sistema** — tabela `GECONTROLE_EXECUCAO_THREADS` (2 linhas)

Controle de execução de threads ao abrir o sistema. 2 linhas no catálogo; chave: ID_THREAD.

- **Chave:** `ID_THREAD`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `DATA_ULTIMA_EXECUCAO`
- **Ordem padrão:** `DATA_ULTIMA_EXECUCAO desc`, `ID_THREAD asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, DATA_ULTIMA_EXECUCAO de 2026-10-16 a 2026-10-16.
- executou_com_sucesso_1_sim_0_nao: todos os valores reais estão no comentário do banco (1=2).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_identificador_da_thread | `id_thread` | integer(4) |  |  | Código identificador da thread |
| executou_com_sucesso_1_sim_0_nao | `executada_com_sucesso` | integer(4) |  | gecontrole_execucao_threads_executou_co | Executou com sucesso (1=Sim/0=Não) |
| data_da_ultima_execucao | `data_ultima_execucao` | date(4) |  |  | Data da última execução |

**Filtros:** `codigo_identificador_da_thread` (eq/in), `data_da_ultima_execucao` (entre/gte/lte)

## gecontrole_imposto_retido

**Controle do recolhimento do imposto retido - IRRF** — tabela `GECONTROLE_IMPOSTO_RETIDO` (1 linhas)

Controle do recolhimento do imposto retido - IRRF. 1 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo` | integer(4) |  |  |  |
| c_0_nao_deve_mostrar_mensagem_na_abertur | `mensagem_imposto_retido` | varchar(2) |  |  | 0 = NÃ£o deve mostrar mensagem na abertura 1 = Deve mostrar mensagem na abertura -1 = Erro na requisiÃ§Ã£o |

**Filtros:** `codigo` (eq/in), `c_0_nao_deve_mostrar_mensagem_na_abertur` (eq/in)

## gecontrole_gestta_processos

**Controla Ativação do gestta processos** — tabela `GECONTROLE_GESTTA_PROCESSOS` (1 linhas)

Controla Ativação do gestta processos. 1 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `DATAHORA_INCLUSAO`
- **Ordem padrão:** `DATAHORA_INCLUSAO desc`, `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, DATAHORA_INCLUSAO de 2021-09-09 a 2021-09-09.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| campo_criado_para_utilizar_o_update_no_c | `codigo` | integer(4) |  |  | Campo criado para utilizar o update no C# caso necess?rio |
| data_e_hora_que_o_registro_foi_criado | `datahora_inclusao` | date(4) |  |  | Data e hora que o registro foi criado |
| ja_utilizou_gestta | `ja_utilizou_gestta` | integer(4) |  |  |  |

**Filtros:** `campo_criado_para_utilizar_o_update_no_c` (eq/in), `data_e_hora_que_o_registro_foi_criado` (entre/gte/lte)

## gecontrole_dominio_processos

**Controla se o escritorio possui ou não permissão para utilizar o Domínio Processos** — tabela `GECONTROLE_DOMINIO_PROCESSOS` (1 linhas)

Controla se o escritorio possui ou não permissão para utilizar o Domínio Processos. 1 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo` | tinyint(1) |  |  |  |
| c_1_erro_na_requisiaao_0_nao_possui_aces | `tem_permissao` | integer(4) |  |  | -1 = Erro na requisiÃ§Ã£o 0 = NÃ£o possui acesso ao domÃ­nio processos 1 = Possui acesso ao domÃ­nio processos |

**Filtros:** `codigo` (eq/in)

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

### gecontrole_execucao_threads_executou_co

Confirmado: sim

> Todos os valores observados em GECONTROLE_EXECUCAO_THREADS.EXECUTADA_COM_SUCESSO estão no comentário do banco (2026-10-18). Distribuição: 1=2.

| Código | Significado |
|---|---|
| 1 | Sim |
| 0 | Não |

