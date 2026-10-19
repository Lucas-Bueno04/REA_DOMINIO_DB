# Modelo — Processos - outros (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/processos_outros.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

6 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [pcresponsavel_empresa](#pcresponsavel_empresa) | `PCRESPONSAVEL_EMPRESA` | 469 | pequeno | empresa |
| [pcmovimento_atividade](#pcmovimento_atividade) | `PCMOVIMENTO_ATIVIDADE` | 61 | pequeno | — |
| [pcmovimento_atividade_responsavel](#pcmovimento_atividade_responsavel) | `PCMOVIMENTO_ATIVIDADE_RESPONSAVEL` | 61 | pequeno | — |
| [pcprocesso_responsavel](#pcprocesso_responsavel) | `PCPROCESSO_RESPONSAVEL` | 24 | pequeno | — |
| [pcprocesso_atividade](#pcprocesso_atividade) | `PCPROCESSO_ATIVIDADE` | 20 | pequeno | — |
| [pccampos_localizar_comprovante](#pccampos_localizar_comprovante) | `PCCAMPOS_LOCALIZAR_COMPROVANTE` | 4 | pequeno | — |

## pcresponsavel_empresa

**Responsáveis empresas** — tabela `PCRESPONSAVEL_EMPRESA` (469 linhas)

Responsáveis empresas. 469 linhas no catálogo; chave: I_RESPONSAVEL, RESPONSAVEL_TIPO, CODI_EMP.

- **Chave:** `I_RESPONSAVEL, RESPONSAVEL_TIPO, CODI_EMP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_RESPONSAVEL asc`, `RESPONSAVEL_TIPO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 469 linhas, 468 empresa(s).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 378).
- Vínculo usconfusuario (usConfUsuario): 0 de 1 linhas sem registro relacionado (empresa 378).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_responsavel | `i_responsavel` | integer(4) |  |  | Código do responsável |
| responsavel_tipo | `responsavel_tipo` | smallint(2) |  |  | Tipo do responsável (Fixo 1) |
| empresa | `codi_emp` | integer(4) |  |  | Empresa |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`
- `usconfusuario` → `usConfUsuario` por `responsavel_tipo` = `tipo` e `i_responsavel` = `i_confusuario`; colunas: `usconfusuario_nome`

**Filtros:** `codigo_do_responsavel` (eq/in), `responsavel_tipo` (eq/in)

## pcmovimento_atividade

**Movimentos atividades** — tabela `PCMOVIMENTO_ATIVIDADE` (61 linhas)

Movimentos atividades. 61 linhas no catálogo; chave: I_VINCULO, I_SEQUENCIAL_ATIVIDADE, I_SEQUENCIAL_MOVIMENTO.

- **Chave:** `I_VINCULO, I_SEQUENCIAL_ATIVIDADE, I_SEQUENCIAL_MOVIMENTO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `DATA_INICIO`
- **Ordem padrão:** `DATA_INICIO desc`, `I_VINCULO asc`, `I_SEQUENCIAL_ATIVIDADE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 61 linhas, DATA_INICIO de 2018-01-26 a 2020-06-10.
- Colunas expostas nulas em 100% das linhas (1): anotacao.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_vinculo | `i_vinculo` | integer(4) |  |  | Código do vínculo |
| sequencial_da_atividade | `i_sequencial_atividade` | integer(4) |  |  | Sequencial da atividade |
| sequencial | `i_sequencial_movimento` | integer(4) |  |  | Sequencial |
| data_de_inicio | `data_inicio` | date(4) |  |  | Data de início |
| competencia_de_referencia | `competencia_referencia` | date(4) |  |  | Competência de referência |
| data_de_vencimento_original | `data_vencimento_original` | date(4) |  |  | Data de vencimento original |
| data_de_vencimento | `data_vencimento` | date(4) |  |  | Data de vencimento |
| data_de_vencimento_legal_original | `data_vencimento_legal_original` | date(4) |  |  | Data de vencimento legal original |
| data_de_vencimento_legal | `data_vencimento_legal` | date(4) |  |  | Data de vencimento legal |
| concluida_s_n | `concluida` | char(1) |  |  | Concluída (S/N) |
| usuario_que_concluiu | `usuario_conclusao` | varchar(30) |  |  | Usuário que concluiu |
| anotacao | `anotacao` | varchar(1000) |  |  | Anotação |
| data_do_vencimento_do_aviso | `data_vencimento_aviso` | date(4) |  |  | Data do vencimento do aviso |
| data_que_inicia_o_aviso | `data_inicio_aviso` | date(4) |  |  | Data que inicia o aviso |
| informar_neste_campo_se_o_movimento_foi | `alterado_inicio_vencimento_utilitario` | tinyint(1) |  |  | Informar neste campo se o movimento foi alterado pelo utilitario "Alterar Unício e Vencimento das Atividades" |

**Filtros:** `codigo_do_vinculo` (eq/in), `sequencial_da_atividade` (eq/in), `sequencial` (eq/in), `data_de_inicio` (entre/gte/lte), `competencia_de_referencia` (entre/gte/lte), `data_de_vencimento_original` (entre/gte/lte), `data_de_vencimento` (entre/gte/lte), `data_de_vencimento_legal_original` (entre/gte/lte), `data_de_vencimento_legal` (entre/gte/lte), `data_do_vencimento_do_aviso` (entre/gte/lte), `data_que_inicia_o_aviso` (entre/gte/lte), `concluida_s_n` (eq/in), `usuario_que_concluiu` (contem/prefixo), `anotacao` (contem/prefixo)

## pcmovimento_atividade_responsavel

**Movimentos atividades - Responsáveis** — tabela `PCMOVIMENTO_ATIVIDADE_RESPONSAVEL` (61 linhas)

Movimentos atividades - Responsáveis. 61 linhas no catálogo; chave: I_VINCULO, I_SEQUENCIAL_ATIVIDADE, I_SEQUENCIAL_MOVIMENTO, I_SEQUENCIAL_RESPONSAVEL.

- **Chave:** `I_VINCULO, I_SEQUENCIAL_ATIVIDADE, I_SEQUENCIAL_MOVIMENTO, I_SEQUENCIAL_RESPONSAVEL`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `I_VINCULO asc`, `I_SEQUENCIAL_ATIVIDADE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 61 linhas.
- Vínculo usconfusuario (usConfUsuario): 0 de 61 linhas sem registro relacionado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_vinculo | `i_vinculo` | integer(4) |  |  | Código do vínculo |
| sequencial_da_atividade | `i_sequencial_atividade` | integer(4) |  |  | Sequencial da atividade |
| sequencial_do_movimento | `i_sequencial_movimento` | integer(4) |  |  | Sequencial do movimento |
| sequencial_do_responsavel | `i_sequencial_responsavel` | integer(4) |  |  | Sequencial do responsável |
| codigo_do_responsavel | `i_responsavel` | integer(4) |  |  | Código do responsável |
| responsavel_tipo | `responsavel_tipo` | smallint(2) |  |  | Tipo do responsável (Fixo 1) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `usconfusuario` → `usConfUsuario` por `responsavel_tipo` = `tipo` e `i_responsavel` = `i_confusuario`; colunas: `usconfusuario_nome`

**Filtros:** `codigo_do_vinculo` (eq/in), `sequencial_da_atividade` (eq/in), `sequencial_do_movimento` (eq/in), `sequencial_do_responsavel` (eq/in), `codigo_do_responsavel` (eq/in), `responsavel_tipo` (eq/in)

## pcprocesso_responsavel

**Processos - Responsáveis** — tabela `PCPROCESSO_RESPONSAVEL` (24 linhas)

Processos - Responsáveis. 24 linhas no catálogo; chave: I_PROCESSO, I_RESPONSAVEL, RESPONSAVEL_TIPO.

- **Chave:** `I_PROCESSO, I_RESPONSAVEL, RESPONSAVEL_TIPO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `I_PROCESSO asc`, `I_RESPONSAVEL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 24 linhas.
- Vínculo pcprocesso (PCPROCESSO): 0 de 24 linhas sem registro relacionado.
- Vínculo usconfusuario (usConfUsuario): 0 de 24 linhas sem registro relacionado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_processo | `i_processo` | integer(4) |  |  | Código do processo |
| codigo_do_responsavel | `i_responsavel` | integer(4) |  |  | Código do responsável |
| responsavel_tipo | `responsavel_tipo` | smallint(2) |  |  | Tipo do responsável (Fixo 1) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `pcprocesso` → `PCPROCESSO` por `i_processo` = `i_processo`; colunas: `pcprocesso_nome`
- `usconfusuario` → `usConfUsuario` por `responsavel_tipo` = `tipo` e `i_responsavel` = `i_confusuario`; colunas: `usconfusuario_nome`

**Filtros:** `codigo_do_processo` (eq/in), `codigo_do_responsavel` (eq/in), `responsavel_tipo` (eq/in)

## pcprocesso_atividade

**Processos - Atividades** — tabela `PCPROCESSO_ATIVIDADE` (20 linhas)

Processos - Atividades. 20 linhas no catálogo; chave: I_PROCESSO, I_SEQUENCIAL_ATIVIDADE.

- **Chave:** `I_PROCESSO, I_SEQUENCIAL_ATIVIDADE`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `I_PROCESSO asc`, `I_SEQUENCIAL_ATIVIDADE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 20 linhas.
- Vínculo pcatividade (PCATIVIDADE): 0 de 20 linhas sem registro relacionado.
- Vínculo pcprocesso (PCPROCESSO): 0 de 20 linhas sem registro relacionado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_processo | `i_processo` | integer(4) |  |  | Código do processo |
| sequencial | `i_sequencial_atividade` | integer(4) |  |  | Sequencial |
| ordem | `ordem` | integer(4) |  |  | Ordem |
| codigo_da_atividade | `i_atividade` | integer(4) |  |  | Código da atividade |
| atividade_dependente_s_n | `dependente` | char(1) |  |  | Atividade dependente (S/N) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `pcatividade` → `PCATIVIDADE` por `i_atividade` = `i_atividade`; colunas: `pcatividade_nome`
- `pcprocesso` → `PCPROCESSO` por `i_processo` = `i_processo`; colunas: `pcprocesso_nome`

**Filtros:** `codigo_do_processo` (eq/in), `sequencial` (eq/in), `codigo_da_atividade` (eq/in), `atividade_dependente_s_n` (eq/in)

## pccampos_localizar_comprovante

**Campos utilizados para localizador comprovantes** — tabela `PCCAMPOS_LOCALIZAR_COMPROVANTE` (4 linhas)

Campos utilizados para localizador comprovantes. 4 linhas no catálogo; chave: I_CAMPO_LOCALIZAR.

- **Chave:** `I_CAMPO_LOCALIZAR`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `I_CAMPO_LOCALIZAR asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| sequencial | `i_campo_localizar` | integer(4) |  |  | Sequencial |
| descricao_do_campo | `descricao` | varchar(100) |  |  | Descrição do campo |
| habilitar_definir_formato | `habilita_definir_formato` | char(1) |  |  | Habilitar definir formato |
| formato_padrao | `formato_padrao` | varchar(100) |  |  |  |

**Filtros:** `sequencial` (eq/in), `descricao_do_campo` (contem/prefixo), `habilitar_definir_formato` (eq/in), `formato_padrao` (contem/prefixo)

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

