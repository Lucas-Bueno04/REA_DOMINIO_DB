# Modelo — Geral - banking (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/geral_banking.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

4 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [gebanking_dados_fintech](#gebanking_dados_fintech) | `GEBANKING_DADOS_FINTECH` | 1.969 | pequeno | empresa |
| [gebanking_acoes_empregados](#gebanking_acoes_empregados) | `GEBANKING_ACOES_EMPREGADOS` | 1.420 | pequeno | empresa |
| [gebanking_log_temporario](#gebanking_log_temporario) | `GEBANKING_LOG_TEMPORARIO` | 6 | pequeno | empresa |
| [gebanking_feature_flag](#gebanking_feature_flag) | `GEBANKING_FEATURE_FLAG` | 2 | pequeno | — |

## gebanking_dados_fintech

**Configuracao de feature flags para integracao com a Fintech por empresa** — tabela `GEBANKING_DADOS_FINTECH` (1.969 linhas)

Configuracao de feature flags para integracao com a Fintech por empresa. 1.969 linhas no catálogo; chave: COMPANY_ID, CODI_EMP.

- **Chave:** `COMPANY_ID, CODI_EMP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `COMPANY_ID asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.969 linhas, 1.969 empresa(s).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 123).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| guid_do_escritorio | `company_id` | uniqueidentifier(16) |  |  | Guid do escritorio |
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Codigo da empresa |
| flag_para_ativar_nova_integracao_de_bene | `feature_flag_beneficios` | bit(1) |  |  | Flag para ativar nova integracao de beneficios (0=Desativado, 1=Ativado) |
| flag_para_controle_de_execucao_da_carga | `carga_inicial_employees_executada` | bit(1) |  |  | Flag para controle de execucao da carga inicial de empregados (0=Nao Executada, 1=Executada) |
| flag_para_controle_de_uso_do_portal_do_e | `usa_portal_empregado` | bit(1) |  |  | Flag para controle de uso do portal do empregado (0=Nao, 1=Sim) |
| flag_indicando_se_carga_inicial_de_empre | `envio_carga_inicial_portal_empregado` | bit(1) |  |  | Flag indicando se carga inicial de empregados por motivo portal foi enviada para esta empresa (0=Nao, 1=Sim) |
| flag_indicando_se_carga_inicial_de_benef | `envio_carga_inicial_portal_beneficio` | bit(1) |  |  | Flag indicando se carga inicial de beneficios foi enviada para esta empresa (0=Nao, 1=Sim) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `guid_do_escritorio` (eq/in)

## gebanking_acoes_empregados

**Controle de acoes de empregados para integracao com FinTech** — tabela `GEBANKING_ACOES_EMPREGADOS` (1.420 linhas)

Controle de acoes de empregados para integracao com FinTech. 1.420 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.400 linhas, 156 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_sequencial_do_registro | `codigo` | integer(4) |  |  | Codigo sequencial do registro |
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Codigo da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Codigo do empregado |
| cpf_do_empregado 🔒 | `cpf` | char(11) |  |  | CPF do empregado |
| tipo_de_evento_create_update_delete | `event_type` | varchar(20) |  |  | Tipo de evento (CREATE, UPDATE, DELETE) |
| indica_se_o_registro_foi_processado_0_na | `processado` | bit(1) |  |  | Indica se o registro foi processado 0- Não Processado/1-Processado |
| numero_de_tentativas_de_processamento_qu | `numero_tentativas` | integer(4) |  |  | Numero de tentativas de processamento que falharam |

**Filtros:** `codigo_sequencial_do_registro` (eq/in), `codigo_do_empregado` (eq/in), `cpf_do_empregado` (eq/in), `tipo_de_evento_create_update_delete` (eq/in)

## gebanking_log_temporario

**Tabela de logs para monitoramento temporário de processos** — tabela `GEBANKING_LOG_TEMPORARIO` (6 linhas)

Tabela de logs para monitoramento temporário de processos. 6 linhas no catálogo; chave: I_LOG.

- **Chave:** `I_LOG`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_LOG asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 6 linhas, 1 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| sequencial_auto_incremental | `i_log` | integer(4) |  |  | Sequencial auto incremental |
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| tipo_de_log_processando_aviso_advertenci | `tipo_log` | varchar(100) |  |  | Tipo de log (Processando, Aviso, Advertência ou Erro) |
| titulo_do_processo | `processo` | varchar(2048) |  |  | Título do processo |
| descricao_da_etapa_do_processo | `descricao` | varchar(2048) |  |  | Descrição da etapa do processo |

**Filtros:** `sequencial_auto_incremental` (eq/in), `tipo_de_log_processando_aviso_advertenci` (contem/prefixo), `titulo_do_processo` (contem/prefixo), `descricao_da_etapa_do_processo` (contem/prefixo)

## gebanking_feature_flag

**Controle de Feature Flags da Fintech** — tabela `GEBANKING_FEATURE_FLAG` (2 linhas)

Controle de Feature Flags da Fintech. 2 linhas no catálogo; chave: DESCRICAO_FEATURE.

- **Chave:** `DESCRICAO_FEATURE`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `DESCRICAO_FEATURE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas.
- status_da_feature_flag_0_inativa_1_ativa: todos os valores reais estão no comentário do banco (1=2).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| nome_da_feature_flag | `descricao_feature` | varchar(120) |  |  | Nome da Feature Flag |
| status_da_feature_flag_0_inativa_1_ativa | `ativo` | smallint(2) |  | gebanking_feature_flag_status_da_fea | Status da Feature Flag (0=Inativa / 1=Ativa) |

**Filtros:** `nome_da_feature_flag` (eq/in)

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

### gebanking_feature_flag_status_da_fea

Confirmado: sim

> Todos os valores observados em GEBANKING_FEATURE_FLAG.ATIVO estão no comentário do banco (2026-10-18). Distribuição: 1=2.

| Código | Significado |
|---|---|
| 0 | Inativa |
| 1 | Ativa |

