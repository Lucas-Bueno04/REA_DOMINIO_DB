# Modelo — Processos - vinculo (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/processos_vinculo.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

4 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [pcvinculo_processo](#pcvinculo_processo) | `PCVINCULO_PROCESSO` | 3 | pequeno | empresa |
| [pcvinculo_processo_responsavel](#pcvinculo_processo_responsavel) | `PCVINCULO_PROCESSO_RESPONSAVEL` | 3 | pequeno | — |
| [pcvinculo_processo_atividade](#pcvinculo_processo_atividade) | `PCVINCULO_PROCESSO_ATIVIDADE` | 3 | pequeno | — |
| [pcvinculo_processo_atividade_responsavel](#pcvinculo_processo_atividade_responsavel) | `PCVINCULO_PROCESSO_ATIVIDADE_RESPONSAVEL` | 3 | pequeno | — |

## pcvinculo_processo

**Vínculo entre processos e empresas** — tabela `PCVINCULO_PROCESSO` (3 linhas)

Vínculo entre processos e empresas. 3 linhas no catálogo; chave: I_VINCULO.

- **Chave:** `I_VINCULO`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA_INICIO`
- **Ordem padrão:** `COMPETENCIA_INICIO desc`, `I_VINCULO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3 linhas, 1 empresa(s), COMPETENCIA_INICIO de 2018-02-01 a 2018-02-01.
- Colunas expostas nulas em 100% das linhas (2): competencia_de_encerramento, usuario_que_encerrou.
- Vínculo geempre (geempre): 0 de 3 linhas sem registro relacionado (empresa 1).
- Vínculo pcprocesso (PCPROCESSO): 0 de 3 linhas sem registro relacionado (empresa 1).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `i_vinculo` | integer(4) |  |  | Código |
| ordem | `ordem` | integer(4) |  |  | Ordem |
| codigo_do_processo | `codi_emp` | integer(4) |  |  | Código do processo |
| codigo_da_empresa | `i_processo` | integer(4) |  |  | Código da empresa |
| a_partir_de | `competencia_inicio` | date(4) |  |  | A partir de |
| encerrar_s_n | `encerrar` | char(1) |  |  | Encerrar (S/N) |
| competencia_de_encerramento | `competencia_encerramento` | date(4) |  |  | Competência de encerramento |
| usuario_que_encerrou | `usuario_encerramento` | varchar(30) |  |  | Usuário que encerrou |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`
- `pcprocesso` → `PCPROCESSO` por `i_processo` = `i_processo`; colunas: `pcprocesso_nome`

**Filtros:** `codigo` (eq/in), `a_partir_de` (entre/gte/lte), `competencia_de_encerramento` (entre/gte/lte), `codigo_da_empresa` (eq/in), `encerrar_s_n` (eq/in), `usuario_que_encerrou` (contem/prefixo)

## pcvinculo_processo_responsavel

**Vínculo entre processos e empresas - Responsáveis** — tabela `PCVINCULO_PROCESSO_RESPONSAVEL` (3 linhas)

Vínculo entre processos e empresas - Responsáveis. 3 linhas no catálogo; chave: I_VINCULO, I_SEQUENCIAL_RESPONSAVEL.

- **Chave:** `I_VINCULO, I_SEQUENCIAL_RESPONSAVEL`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_VINCULO asc`, `I_SEQUENCIAL_RESPONSAVEL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3 linhas, COMPETENCIA de 2017-12-01 a 2018-02-01.
- Vínculo usconfusuario (usConfUsuario): 0 de 3 linhas sem registro relacionado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_vinculo | `i_vinculo` | integer(4) |  |  | Código do vínculo |
| sequencial | `i_sequencial_responsavel` | integer(4) |  |  | Sequencial |
| competencia | `competencia` | date(4) |  |  | Competência |
| codigo_do_responsavel | `i_responsavel` | integer(4) |  |  | Código do responsável |
| responsavel_tipo | `responsavel_tipo` | smallint(2) |  |  | Tipo do responsável (Fixo 1) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `usconfusuario` → `usConfUsuario` por `responsavel_tipo` = `tipo` e `i_responsavel` = `i_confusuario`; colunas: `usconfusuario_nome`

**Filtros:** `codigo_do_vinculo` (eq/in), `sequencial` (eq/in), `competencia` (entre/gte/lte), `codigo_do_responsavel` (eq/in), `responsavel_tipo` (eq/in)

## pcvinculo_processo_atividade

**Vínculo entre processos e empresas - Atividades** — tabela `PCVINCULO_PROCESSO_ATIVIDADE` (3 linhas)

Vínculo entre processos e empresas - Atividades. 3 linhas no catálogo; chave: I_VINCULO, I_SEQUENCIAL_ATIVIDADE.

- **Chave:** `I_VINCULO, I_SEQUENCIAL_ATIVIDADE`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `COMPETENCIA_INICIO`
- **Ordem padrão:** `COMPETENCIA_INICIO desc`, `I_VINCULO asc`, `I_SEQUENCIAL_ATIVIDADE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3 linhas, COMPETENCIA_INICIO de 2018-02-01 a 2018-02-01.
- Colunas expostas nulas em 100% das linhas (2): competencia_de_encerramento, usuario_que_encerrou.
- vencimento_tipo: todos os valores reais estão no comentário do banco (2=3).
- inicio_mes_1_anterior_ao_vencimento_2_in: todos os valores reais estão no comentário do banco (1=2, 3=1).
- competencia_de_referencia_mes_1_anterior: todos os valores reais estão no comentário do banco (1=2, 3=1).
- Vínculo pcatividade (PCATIVIDADE): 0 de 3 linhas sem registro relacionado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_vinculo | `i_vinculo` | integer(4) |  |  | Código do vínculo |
| sequencial | `i_sequencial_atividade` | integer(4) |  |  | Sequencial |
| ordem | `ordem` | integer(4) |  |  | Ordem |
| codigo_da_atividade | `i_atividade` | integer(4) |  |  | Código da atividade |
| a_partir_de | `competencia_inicio` | date(4) |  |  | A partir de |
| vencimento_dias | `vencimento_dia` | tinyint(1) |  |  | Vencimento - Dias |
| vencimento_tipo | `vencimento_tipo` | tinyint(1) |  | pcvinculo_processo_atividade_vencimento_ | Vencimento - Tipo (1=Dias corridos direto/ 2=Dias corridos antecipados/ 3=Dias corridos adiado/ 4=Dias úteis) |
| vencimento_mes_1o_bimestre | `vencimento_bimestre1` | tinyint(1) |  |  | Vencimento - Mês 1o Bimestre |
| vencimento_mes_2o_bimestre | `vencimento_bimestre2` | tinyint(1) |  |  | Vencimento - Mês 2o Bimestre |
| vencimento_mes_3o_bimestre | `vencimento_bimestre3` | tinyint(1) |  |  | Vencimento - Mês 3o Bimestre |
| vencimento_mes_4o_bimestre | `vencimento_bimestre4` | tinyint(1) |  |  | Vencimento - Mês 4o Bimestre |
| vencimento_mes_5o_bimestre | `vencimento_bimestre5` | tinyint(1) |  |  | Vencimento - Mês 5o Bimestre |
| vencimento_mes_6o_bimestre | `vencimento_bimestre6` | tinyint(1) |  |  | Vencimento - Mês 6o Bimestre |
| vencimento_mes_1o_trimestre | `vencimento_trimestre1` | tinyint(1) |  |  | Vencimento - Mês 1o Trimestre |
| vencimento_mes_2o_trimestre | `vencimento_trimestre2` | tinyint(1) |  |  | Vencimento - Mês 2o Trimestre |
| vencimento_mes_3o_trimestre | `vencimento_trimestre3` | tinyint(1) |  |  | Vencimento - Mês 3o Trimestre |
| vencimento_mes_4o_trimestre | `vencimento_trimestre4` | tinyint(1) |  |  | Vencimento - Mês 4o Trimestre |
| vencimento_mes_1o_quadrimestre | `vencimento_quadrimestre1` | tinyint(1) |  |  | Vencimento - Mês 1o Quadrimestre |
| vencimento_mes_2o_quadrimestre | `vencimento_quadrimestre2` | tinyint(1) |  |  | Vencimento - Mês 2o Quadrimestre |
| vencimento_mes_3o_quadrimestre | `vencimento_quadrimestre3` | tinyint(1) |  |  | Vencimento - Mês 3o Quadrimestre |
| vencimento_mes_1o_semestre | `vencimento_semestre1` | tinyint(1) |  |  | Vencimento - Mês 1o Semestre |
| vencimento_mes_2o_semestre | `vencimento_semestre2` | tinyint(1) |  |  | Vencimento - Mês 2o Semestre |
| vencimento_mes_ano | `vencimento_anual` | tinyint(1) |  |  | Vencimento - Mês Ano |
| inicio_dias | `inicio_dia` | tinyint(1) |  |  | Início - Dias |
| inicio_mes_1_anterior_ao_vencimento_2_in | `inicio_mes` | tinyint(1) |  | pcvinculo_processo_atividade_inicio_mes_ | Início - Mês (1=Anterior ao vencimento/ 2=Informar quantidade de meses anteriores ao vencimento/ 3=No mesmo do vencimento) |
| inicio_meses_anteriores | `inicio_mes_anterior` | tinyint(1) |  |  | Início - Meses anteriores |
| competencia_de_referencia_mes_1_anterior | `competencia_mes` | tinyint(1) |  | pcvinculo_processo_atividade_competencia | Competência de referencia - Mês (1=Anterior ao vencimento/ 2=Informar quantidade de meses anteriores ao vencimento/ 3=No mesmo do vencimento) |
| competencia_de_referencia_meses_anterior | `competencia_mes_anterior` | tinyint(1) |  |  | Competência de referencia - Meses anteriores |
| atividade_dependente_s_n | `dependente` | char(1) |  |  | Atividade dependente (S/N) |
| encerrar_s_n | `encerrar` | char(1) |  |  | Encerrar (S/N) |
| competencia_de_encerramento | `competencia_encerramento` | date(4) |  |  | Competência de encerramento |
| usuario_que_encerrou | `usuario_encerramento` | varchar(30) |  |  | Usuário que encerrou |
| vencimento_mes | `vencimento_mes` | integer(4) |  |  | Vencimento - Mês |
| vencimento_ano | `vencimento_ano` | integer(4) |  |  | Vencimento - Ano |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `pcatividade` → `PCATIVIDADE` por `i_atividade` = `i_atividade`; colunas: `pcatividade_nome`

**Filtros:** `codigo_do_vinculo` (eq/in), `sequencial` (eq/in), `a_partir_de` (entre/gte/lte), `competencia_de_encerramento` (entre/gte/lte), `codigo_da_atividade` (eq/in), `vencimento_tipo` (eq/in), `atividade_dependente_s_n` (eq/in), `encerrar_s_n` (eq/in), `usuario_que_encerrou` (contem/prefixo)

## pcvinculo_processo_atividade_responsavel

**Vínculo entre processos e empresas - Atividades - Responsáveis** — tabela `PCVINCULO_PROCESSO_ATIVIDADE_RESPONSAVEL` (3 linhas)

Vínculo entre processos e empresas - Atividades - Responsáveis. 3 linhas no catálogo; chave: I_VINCULO, I_SEQUENCIAL_ATIVIDADE, I_SEQUENCIAL_RESPONSAVEL.

- **Chave:** `I_VINCULO, I_SEQUENCIAL_ATIVIDADE, I_SEQUENCIAL_RESPONSAVEL`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `A_PARTIR_DE`
- **Ordem padrão:** `A_PARTIR_DE desc`, `I_VINCULO asc`, `I_SEQUENCIAL_ATIVIDADE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3 linhas, A_PARTIR_DE de 2017-12-01 a 2018-02-01.
- Colunas expostas nulas em 100% das linhas (1): encerrado_em.
- Vínculo usconfusuario (usConfUsuario): 0 de 3 linhas sem registro relacionado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_vinculo | `i_vinculo` | integer(4) |  |  | Código do vínculo |
| sequencial_da_atividade | `i_sequencial_atividade` | integer(4) |  |  | Sequencial da atividade |
| sequencial | `i_sequencial_responsavel` | integer(4) |  |  | Sequencial |
| codigo_do_responsavel | `i_responsavel` | integer(4) |  |  | Código do responsável |
| responsavel_tipo | `responsavel_tipo` | smallint(2) |  |  | Tipo do responsável (Fixo 1) |
| a_partir_de | `a_partir_de` | date(4) |  |  | A partir de |
| encerrado_em | `encerrado_em` | date(4) |  |  | Encerrado em |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `usconfusuario` → `usConfUsuario` por `responsavel_tipo` = `tipo` e `i_responsavel` = `i_confusuario`; colunas: `usconfusuario_nome`

**Filtros:** `codigo_do_vinculo` (eq/in), `sequencial_da_atividade` (eq/in), `sequencial` (eq/in), `a_partir_de` (entre/gte/lte), `encerrado_em` (entre/gte/lte), `codigo_do_responsavel` (eq/in), `responsavel_tipo` (eq/in)

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

### pcvinculo_processo_atividade_vencimento_

Confirmado: sim

> Todos os valores observados em PCVINCULO_PROCESSO_ATIVIDADE.VENCIMENTO_TIPO estão no comentário do banco (2026-10-18). Distribuição: 2=3.

| Código | Significado |
|---|---|
| 1 | Dias corridos direto |
| 2 | Dias corridos antecipados |
| 3 | Dias corridos adiado |
| 4 | Dias úteis |

### pcvinculo_processo_atividade_inicio_mes_

Confirmado: sim

> Todos os valores observados em PCVINCULO_PROCESSO_ATIVIDADE.INICIO_MES estão no comentário do banco (2026-10-18). Distribuição: 1=2, 3=1.

| Código | Significado |
|---|---|
| 1 | Anterior ao vencimento |
| 2 | Informar quantidade de meses anteriores ao vencimento |
| 3 | No mesmo do vencimento |

### pcvinculo_processo_atividade_competencia

Confirmado: sim

> Todos os valores observados em PCVINCULO_PROCESSO_ATIVIDADE.COMPETENCIA_MES estão no comentário do banco (2026-10-18). Distribuição: 1=2, 3=1.

| Código | Significado |
|---|---|
| 1 | Anterior ao vencimento |
| 2 | Informar quantidade de meses anteriores ao vencimento |
| 3 | No mesmo do vencimento |

