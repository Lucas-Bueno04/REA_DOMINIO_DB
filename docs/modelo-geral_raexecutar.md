# Modelo — Geral - raexecutar (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/geral_raexecutar.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

6 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [geraexecutar_empregados](#geraexecutar_empregados) | `GERAEXECUTAR_EMPREGADOS` | 52.256 | medio | empresa |
| [geraexecutar_empresas](#geraexecutar_empresas) | `GERAEXECUTAR_EMPRESAS` | 32.994 | medio | empresa |
| [geraexecutar_rotinas](#geraexecutar_rotinas) | `GERAEXECUTAR_ROTINAS` | 508 | pequeno | — |
| [geraexecutar_empresas_opcoes_honorarios](#geraexecutar_empresas_opcoes_honorarios) | `GERAEXECUTAR_EMPRESAS_OPCOES_HONORARIOS` | 40 | pequeno | empresa |
| [geraexecutar_empresas_opcoes_contabilidade](#geraexecutar_empresas_opcoes_contabilidade) | `GERAEXECUTAR_EMPRESAS_OPCOES_CONTABILIDADE` | 6 | pequeno | empresa |
| [geraexecutar_semanas](#geraexecutar_semanas) | `GERAEXECUTAR_SEMANAS` | 1 | pequeno | — |

## geraexecutar_empregados

**Rotinas automáticas - Empregados executar** — tabela `GERAEXECUTAR_EMPREGADOS` (52.256 linhas)

Rotinas automáticas - Empregados executar. 52.256 linhas no catálogo; chave: I_EXECUTARRA, I_SISTEMA, CODI_EMP, I_EMPREGADOS.

- **Chave:** `I_EXECUTARRA, I_SISTEMA, CODI_EMP, I_EMPREGADOS`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_EXECUTARRA asc`, `I_SISTEMA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 52.308 linhas, 924 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_execucao | `i_executarra` | integer(4) |  |  | Código da execução. |
| codigo_do_sistema | `i_sistema` | smallint(2) |  |  | Código do sistema. |
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado. |

**Filtros:** `codigo_da_execucao` (eq/in), `codigo_do_sistema` (eq/in), `codigo_do_empregado` (eq/in)

## geraexecutar_empresas

**SELEÇÃO DE EMPRESAS DA EXECUÇÃO DE ROTINAS AUTOMÁTICAS** — tabela `GERAEXECUTAR_EMPRESAS` (32.994 linhas)

SELEÇÃO DE EMPRESAS DA EXECUÇÃO DE ROTINAS AUTOMÁTICAS. 32.994 linhas no catálogo; chave: I_EXECUTARRA, I_SISTEMA, CODI_EMP.

- **Chave:** `I_EXECUTARRA, I_SISTEMA, CODI_EMP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_EXECUTARRA asc`, `I_SISTEMA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 33.003 linhas, 1.504 empresa(s).
- Vínculo geraexecutar (GERAEXECUTAR): 0 de 19 linhas sem registro relacionado (empresa 1731).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_execucao | `i_executarra` | integer(4) |  |  | CÓDIGO DA EXECUÇÃO |
| codigo_do_sistema | `i_sistema` | smallint(2) |  |  | CÓDIGO DO SISTEMA |
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | CÓDIGO DA EMPRESA |
| pasta_de_destino_arquivos | `pasta_destino` | char(200) |  |  | Pasta de destino arquivos. |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geraexecutar` → `GERAEXECUTAR` por `i_executarra` = `i_executarra` e `i_sistema` = `i_sistema`; colunas: `geraexecutar_nome`

**Filtros:** `codigo_da_execucao` (eq/in), `codigo_do_sistema` (eq/in), `pasta_de_destino_arquivos` (contem/prefixo)

## geraexecutar_rotinas

**ROTINAS DA EXECUÇÃO DAS ROTINAS AUTOMÁTICAS** — tabela `GERAEXECUTAR_ROTINAS` (508 linhas)

ROTINAS DA EXECUÇÃO DAS ROTINAS AUTOMÁTICAS. 508 linhas no catálogo; chave: I_EXECUTARRA, I_SISTEMA, I_ROTINAS.

- **Chave:** `I_EXECUTARRA, I_SISTEMA, I_ROTINAS`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `I_EXECUTARRA asc`, `I_SISTEMA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 508 linhas.
- Vínculo geraexecutar (GERAEXECUTAR): 0 de 508 linhas sem registro relacionado.
- Vínculo gerarotinas (GERAROTINAS): 0 de 508 linhas sem registro relacionado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_execucao | `i_executarra` | integer(4) |  |  | CÓDIGO DA EXECUÇÃO |
| codigo_do_sistema | `i_sistema` | smallint(2) |  |  | CÓDIGO DO SISTEMA |
| codigo_da_rotina | `i_rotinas` | integer(4) |  |  | CÓDIGO DA ROTINA |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geraexecutar` → `GERAEXECUTAR` por `i_executarra` = `i_executarra` e `i_sistema` = `i_sistema`; colunas: `geraexecutar_nome`
- `gerarotinas` → `GERAROTINAS` por `i_rotinas` = `i_rotinas` e `i_sistema` = `i_sistema`; colunas: `gerarotinas_nome`

**Filtros:** `codigo_da_execucao` (eq/in), `codigo_do_sistema` (eq/in), `codigo_da_rotina` (eq/in)

## geraexecutar_empresas_opcoes_honorarios

**Informações do honorarios por empresa utilizados na rotina automatica** — tabela `GERAEXECUTAR_EMPRESAS_OPCOES_HONORARIOS` (40 linhas)

Informações do honorarios por empresa utilizados na rotina automatica. 40 linhas no catálogo; chave: I_EXECUTARRA, I_SISTEMA, CODI_EMP, OPCAO_ID.

- **Chave:** `I_EXECUTARRA, I_SISTEMA, CODI_EMP, OPCAO_ID`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_EXECUTARRA asc`, `I_SISTEMA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 40 linhas, 1 empresa(s).
- Vínculo geraexecutar (GERAEXECUTAR): 0 de 40 linhas sem registro relacionado (empresa 1).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_execucao | `i_executarra` | integer(4) |  |  | Código da execução |
| codigo_do_sistema | `i_sistema` | smallint(2) |  |  | Código do sistema |
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| id_da_opcao_do_honorarios | `opcao_id` | varchar(128) |  |  | ID da opção do honorarios |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geraexecutar` → `GERAEXECUTAR` por `i_executarra` = `i_executarra` e `i_sistema` = `i_sistema`; colunas: `geraexecutar_nome`

**Filtros:** `codigo_da_execucao` (eq/in), `codigo_do_sistema` (eq/in), `id_da_opcao_do_honorarios` (eq/in)

## geraexecutar_empresas_opcoes_contabilidade

**Informações da contabilidade por empresa utilizados na rotina automatica** — tabela `GERAEXECUTAR_EMPRESAS_OPCOES_CONTABILIDADE` (6 linhas)

Informações da contabilidade por empresa utilizados na rotina automatica. 6 linhas no catálogo; chave: I_EXECUTARRA, I_SISTEMA, CODI_EMP, PROCESSO, OPCAO_CAMPO.

- **Chave:** `I_EXECUTARRA, I_SISTEMA, CODI_EMP, PROCESSO, OPCAO_CAMPO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_EXECUTARRA asc`, `I_SISTEMA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 6 linhas, 1 empresa(s).
- processo_da_contabilidade_1_importacao_e: todos os valores reais estão no comentário do banco (1=6).
- Vínculo geraexecutar (GERAEXECUTAR): 0 de 6 linhas sem registro relacionado (empresa 275).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_execucao | `i_executarra` | integer(4) |  |  | Código da execução |
| codigo_do_sistema | `i_sistema` | smallint(2) |  |  | Código do sistema |
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| processo_da_contabilidade_1_importacao_e | `processo` | integer(4) |  | geraexecutar_empresas_opcoes_contabilidade_processo_da | Processo da contabilidade (1-Importação Extrato/2-Conciliação Bancaria) |
| campo_da_opcao_da_contabilidade | `opcao_campo` | varchar(128) |  |  | Campo da opção da contabilidade |
| valor_da_opcao_da_contabilidade | `opcao_valor` | varchar(512) |  |  | Valor da opção da contabilidade |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geraexecutar` → `GERAEXECUTAR` por `i_executarra` = `i_executarra` e `i_sistema` = `i_sistema`; colunas: `geraexecutar_nome`

**Filtros:** `codigo_da_execucao` (eq/in), `codigo_do_sistema` (eq/in), `processo_da_contabilidade_1_importacao_e` (eq/in), `campo_da_opcao_da_contabilidade` (eq/in), `valor_da_opcao_da_contabilidade` (contem/prefixo)

## geraexecutar_semanas

**Configuração de agendamento semanal das rotinas automáticas (SAI 101818)** — tabela `GERAEXECUTAR_SEMANAS` (1 linhas)

Configuração de agendamento semanal das rotinas automáticas (SAI 101818). 1 linhas no catálogo; chave: I_EXECUTARRA, I_SISTEMA.

- **Chave:** `I_EXECUTARRA, I_SISTEMA`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `DATA_ULTIMA_NOTIFICACAO_SEMANAL`
- **Ordem padrão:** `DATA_ULTIMA_NOTIFICACAO_SEMANAL desc`, `I_EXECUTARRA asc`, `I_SISTEMA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas.
- Colunas expostas nulas em 100% das linhas (1): data_da_ultima_ocorrencia_semanal_notifi.
- Vínculo geraexecutar (GERAEXECUTAR): 0 de 1 linhas sem registro relacionado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_rotina_automatica_fk_geraexecu | `i_executarra` | integer(4) |  |  | Código da rotina automática (FK GERAEXECUTAR) |
| codigo_do_sistema_fk_geraexecutar | `i_sistema` | smallint(2) |  |  | Código do sistema (FK GERAEXECUTAR) |
| dia_da_semana_1_segunda_7_domingo | `dia_semana` | smallint(2) |  |  | Dia da semana (1=Segunda..7=Domingo) |
| c_1a_semana_do_mes_0_nao_1_sim | `semana_1` | smallint(2) |  |  | 1ª semana do mês (0=Não, 1=Sim) |
| c_2a_semana_do_mes_0_nao_1_sim | `semana_2` | smallint(2) |  |  | 2ª semana do mês (0=Não, 1=Sim) |
| c_3a_semana_do_mes_0_nao_1_sim | `semana_3` | smallint(2) |  |  | 3ª semana do mês (0=Não, 1=Sim) |
| c_4a_semana_do_mes_0_nao_1_sim | `semana_4` | smallint(2) |  |  | 4ª semana do mês (0=Não, 1=Sim) |
| ultima_semana_do_mes_0_nao_1_sim | `semana_ultima` | smallint(2) |  |  | Última semana do mês (0=Não, 1=Sim) |
| data_da_ultima_ocorrencia_semanal_notifi | `data_ultima_notificacao_semanal` | date(4) |  |  | Data da última ocorrência semanal notificada ao usuário (SAI 101818) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geraexecutar` → `GERAEXECUTAR` por `i_executarra` = `i_executarra` e `i_sistema` = `i_sistema`; colunas: `geraexecutar_nome`

**Filtros:** `codigo_da_rotina_automatica_fk_geraexecu` (eq/in), `codigo_do_sistema_fk_geraexecutar` (eq/in), `data_da_ultima_ocorrencia_semanal_notifi` (entre/gte/lte)

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

### geraexecutar_empresas_opcoes_contabilidade_processo_da

Confirmado: sim

> Todos os valores observados em GERAEXECUTAR_EMPRESAS_OPCOES_CONTABILIDADE.PROCESSO estão no comentário do banco (2026-10-18). Distribuição: 1=6.

| Código | Significado |
|---|---|
| 1 | Importação Extrato |
| 2 | Conciliação Bancaria |

