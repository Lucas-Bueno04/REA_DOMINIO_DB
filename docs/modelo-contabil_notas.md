# Modelo — Contábil - notas (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/contabil_notas.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

4 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [ctnotas_explicativas](#ctnotas_explicativas) | `ctnotas_explicativas` | 19 | pequeno | empresa |
| [ctnotas_explicativas_relacionamento_conta](#ctnotas_explicativas_relacionamento_conta) | `CTNOTAS_EXPLICATIVAS_RELACIONAMENTO_CONTA` | 19 | pequeno | empresa |
| [ctnotas_explicativas_relacionamento](#ctnotas_explicativas_relacionamento) | `CTNOTAS_EXPLICATIVAS_RELACIONAMENTO` | 6 | pequeno | empresa |
| [ctnotas_explicativas_relacionamento_conta_sped_contabil](#ctnotas_explicativas_relacionamento_conta_sped_contabil) | `CTNOTAS_EXPLICATIVAS_RELACIONAMENTO_CONTA_SPED_CONTABIL` | 1 | pequeno | empresa |

## ctnotas_explicativas

**Notas explicativas - Cadastro** — tabela `ctnotas_explicativas` (19 linhas)

Notas explicativas - Cadastro. 19 linhas no catálogo; chave: i_nota, codi_emp.

- **Chave:** `i_nota, codi_emp`
- **Empresa:** `codi_emp`
- **Período:** `balanco`
- **Ordem padrão:** `balanco desc`, `i_nota asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 19 linhas, 11 empresa(s), balanco de 2018-12-31 a 2025-12-31.
- Colunas expostas nulas em 100% das linhas (2): periodo_inicial, periodo_final.
- Vínculo geempre (geempre): 0 de 2 linhas sem registro relacionado (empresa 1558).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `i_nota` | integer(4) |  |  | Codigo |
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| ole | `i_ole` | integer(4) |  |  | OLE |
| descricao | `descricao` | char(100) |  |  | Descricao |
| data_de_encerramento_do_balanco | `balanco` | date(4) |  |  | Data de encerramento do balanco |
| periodo_inicial | `periodo_inicial` | date(4) |  |  | Período inicial |
| periodo_final | `periodo_final` | date(4) |  |  | Período final |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `codigo` (eq/in), `data_de_encerramento_do_balanco` (entre/gte/lte), `periodo_inicial` (entre/gte/lte), `periodo_final` (entre/gte/lte), `ole` (eq/in), `descricao` (contem/prefixo)

## ctnotas_explicativas_relacionamento_conta

**Notas explicativas - Relacionamento entre contas - Contas** — tabela `CTNOTAS_EXPLICATIVAS_RELACIONAMENTO_CONTA` (19 linhas)

Notas explicativas - Relacionamento entre contas - Contas. 19 linhas no catálogo; chave: CODI_EMP, I_RELACIONAMENTO, I_CONTA.

- **Chave:** `CODI_EMP, I_RELACIONAMENTO, I_CONTA`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_RELACIONAMENTO asc`, `I_CONTA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 19 linhas, 6 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `i_relacionamento` | integer(4) |  |  | Código |
| sequencial | `i_conta` | integer(4) |  |  | Sequencial |
| conta_contabil | `codi_cta` | integer(4) |  |  | Conta contábil |
| nota_explicativa | `nota_explicativa` | varchar(15) |  |  | Nota explicativa |

**Filtros:** `codigo` (eq/in), `sequencial` (eq/in), `conta_contabil` (eq/in), `nota_explicativa` (eq/in)

## ctnotas_explicativas_relacionamento

**Notas explicativas - Relacionamento entre contas** — tabela `CTNOTAS_EXPLICATIVAS_RELACIONAMENTO` (6 linhas)

Notas explicativas - Relacionamento entre contas. 6 linhas no catálogo; chave: CODI_EMP, I_RELACIONAMENTO.

- **Chave:** `CODI_EMP, I_RELACIONAMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `PERIODO_ENCERRADO`
- **Ordem padrão:** `PERIODO_ENCERRADO desc`, `I_RELACIONAMENTO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 6 linhas, 6 empresa(s), PERIODO_ENCERRADO de 2018-12-31 a 2024-12-31.
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 910).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `i_relacionamento` | integer(4) |  |  | Código |
| periodo_encerrado_em | `periodo_encerrado` | date(4) |  |  | Período encerrado em |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `codigo` (eq/in), `periodo_encerrado_em` (entre/gte/lte)

## ctnotas_explicativas_relacionamento_conta_sped_contabil

**Relacionamento de notas explicativas com o SPED contabil** — tabela `CTNOTAS_EXPLICATIVAS_RELACIONAMENTO_CONTA_SPED_CONTABIL` (1 linhas)

Relacionamento de notas explicativas com o SPED contabil. 1 linhas no catálogo; chave: CODI_EMP, I_RELACIONAMENTO, I_CONTA, SEQUENCIAL.

- **Chave:** `CODI_EMP, I_RELACIONAMENTO, I_CONTA, SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_RELACIONAMENTO asc`, `I_CONTA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Codigo da empresa |
| codigo_do_relacionamento | `i_relacionamento` | integer(4) |  |  | Codigo do relacionamento |
| codigo_da_conta_contabil | `i_conta` | integer(4) |  |  | Codigo da conta contabil |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| codigo_do_scp | `i_scp` | integer(4) |  |  | Código do SCP |
| observacao_da_nota_explicativa_relativa | `nota_exp_obs_scp` | varchar(255) |  |  | Observação da nota explicativa relativa ao bloco J do SPED Contabil |

**Filtros:** `codigo_do_relacionamento` (eq/in), `codigo_da_conta_contabil` (eq/in), `sequencial` (eq/in), `codigo_do_scp` (eq/in), `observacao_da_nota_explicativa_relativa` (contem/prefixo)

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

