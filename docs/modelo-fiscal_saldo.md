# Modelo — Fiscal - saldo (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/fiscal_saldo.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

4 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [efsaldo_imposto_descricao_vigencia_ordem](#efsaldo_imposto_descricao_vigencia_ordem) | `EFSALDO_IMPOSTO_DESCRICAO_VIGENCIA_ORDEM` | 9.636 | pequeno | — |
| [efsaldo_imposto_descricao_vigencia_recolher](#efsaldo_imposto_descricao_vigencia_recolher) | `EFSALDO_IMPOSTO_DESCRICAO_VIGENCIA_RECOLHER` | 769 | pequeno | — |
| [efsaldo_imposto_descricao_vigencia](#efsaldo_imposto_descricao_vigencia) | `EFSALDO_IMPOSTO_DESCRICAO_VIGENCIA` | 394 | pequeno | — |
| [efsaldo_imposto_ordem](#efsaldo_imposto_ordem) | `EFSALDO_IMPOSTO_ORDEM` | 155 | pequeno | — |

## efsaldo_imposto_descricao_vigencia_ordem

**Tela de Apuração de Impostos - Layouts - Ordem das colunas** — tabela `EFSALDO_IMPOSTO_DESCRICAO_VIGENCIA_ORDEM` (9.636 linhas)

Tela de Apuração de Impostos - Layouts - Ordem das colunas. 9.636 linhas no catálogo; chave: CODI_IMP, UF, VIGENCIA, MODELO, ORDEM.

- **Chave:** `CODI_IMP, UF, VIGENCIA, MODELO, ORDEM`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `VIGENCIA`
- **Ordem padrão:** `VIGENCIA desc`, `CODI_IMP asc`, `UF asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 9.636 linhas, VIGENCIA de 1900-01-01 a 2026-01-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_imposto | `codi_imp` | integer(4) |  |  | Código do imposto |
| uf | `uf` | char(2) |  |  | UF |
| vigencia | `vigencia` | date(4) |  |  | Vigência |
| modelo | `modelo` | integer(4) |  |  | Modelo |
| ordem | `ordem` | char(7) |  |  | Ordem |
| coluna | `coluna` | varchar(255) |  |  | Coluna |
| descricao_apuracao | `descricao` | varchar(255) |  |  | Descrição apuração |
| descricao_relatorio | `descricao_relatorio` | varchar(255) |  |  | Descrição relatório |
| operacao | `operacao` | integer(4) |  |  | Operacao |
| nivel | `nivel` | integer(4) |  |  | Nível |
| tipo | `tipo` | char(1) |  |  | Tipo |
| visualizacao | `visualizacao` | integer(4) |  |  | Visualização |
| detalhamento | `detalhamento` | integer(4) |  |  | Detalhamento |
| forma_exibicao | `forma_exibicao` | integer(4) |  |  | Forma Exibição |
| demonstra_relatorio_resumo | `demonstra_relatorio_resumo` | char(1) |  |  | Demonstra relatório resumo |
| coluna_relatorio_de_resumo_modelo_lancad | `coluna_relatorio_resumo_lancado` | varchar(255) |  |  | Coluna relatório de resumo - modelo lançado |
| coluna_relatorio_de_resumo_modelo_calcul | `coluna_relatorio_resumo_calculado` | varchar(255) |  |  | Coluna relatório de resumo - modelo calculado |
| para_colunas_que_possuem_valor_indicador | `soma_no_pai` | char(1) |  |  | Para colunas que possuem valor, indicador se vai somar no pai. |

**Filtros:** `codigo_do_imposto` (eq/in), `uf` (eq/in), `vigencia` (eq/in), `modelo` (eq/in), `ordem` (eq/in), `coluna` (contem/prefixo), `descricao_apuracao` (contem/prefixo), `descricao_relatorio` (contem/prefixo), `tipo` (eq/in), `demonstra_relatorio_resumo` (eq/in), `coluna_relatorio_de_resumo_modelo_lancad` (contem/prefixo), `coluna_relatorio_de_resumo_modelo_calcul` (contem/prefixo), `para_colunas_que_possuem_valor_indicador` (eq/in)

## efsaldo_imposto_descricao_vigencia_recolher

**Tela de Apuração de Impostos - Recolher** — tabela `EFSALDO_IMPOSTO_DESCRICAO_VIGENCIA_RECOLHER` (769 linhas)

Tela de Apuração de Impostos - Recolher. 769 linhas no catálogo; chave: CODI_IMP, UF, VIGENCIA, MODELO, ORDEM.

- **Chave:** `CODI_IMP, UF, VIGENCIA, MODELO, ORDEM`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `VIGENCIA`
- **Ordem padrão:** `VIGENCIA desc`, `CODI_IMP asc`, `UF asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 769 linhas, VIGENCIA de 1900-01-01 a 2025-10-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_imposto | `codi_imp` | integer(4) |  |  | Código do imposto |
| uf | `uf` | char(2) |  |  | UF |
| vigencia | `vigencia` | date(4) |  |  | Vigência |
| modelo | `modelo` | integer(4) |  |  | Modelo |
| ordem | `ordem` | integer(4) |  |  | Ordem |
| coluna | `coluna` | varchar(255) |  |  | Coluna |
| descricao_apuracao | `descricao` | varchar(255) |  |  | Descrição apuração |
| descricao_relatorio | `descricao_relatorio` | varchar(255) |  |  | Descrição relatório |
| visualizacao | `visualizacao` | integer(4) |  |  | Visualização |
| tipo | `tipo` | integer(4) |  |  | Tipo |
| botao_memoria_de_calculo | `memoria_calculo` | char(1) |  |  | Botão memória de cálculo |
| nivel | `nivel` | integer(4) |  |  | Nível |

**Filtros:** `codigo_do_imposto` (eq/in), `uf` (eq/in), `vigencia` (eq/in), `modelo` (eq/in), `ordem` (eq/in), `coluna` (contem/prefixo), `descricao_apuracao` (contem/prefixo), `descricao_relatorio` (contem/prefixo), `tipo` (eq/in), `botao_memoria_de_calculo` (eq/in)

## efsaldo_imposto_descricao_vigencia

**Tela de Apuração de Impostos - Layouts de Apresentação** — tabela `EFSALDO_IMPOSTO_DESCRICAO_VIGENCIA` (394 linhas)

Tela de Apuração de Impostos - Layouts de Apresentação. 394 linhas no catálogo; chave: CODI_IMP, UF, VIGENCIA, MODELO.

- **Chave:** `CODI_IMP, UF, VIGENCIA, MODELO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `VIGENCIA`
- **Ordem padrão:** `VIGENCIA desc`, `CODI_IMP asc`, `UF asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 394 linhas, VIGENCIA de 1900-01-01 a 2026-01-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_imposto | `codi_imp` | integer(4) |  |  | Código do imposto |
| uf | `uf` | char(2) |  |  | UF |
| vigencia | `vigencia` | date(4) |  |  | Vigência |
| modelo | `modelo` | integer(4) |  |  | Modelo |
| layout | `layout` | integer(4) |  |  | Layout |

**Filtros:** `codigo_do_imposto` (eq/in), `uf` (eq/in), `vigencia` (eq/in), `modelo` (eq/in)

## efsaldo_imposto_ordem

**Tela de Apuração de Impostos - Ordem dos Impostos** — tabela `EFSALDO_IMPOSTO_ORDEM` (155 linhas)

Tela de Apuração de Impostos - Ordem dos Impostos. 155 linhas no catálogo; chave: CODI_IMP.

- **Chave:** `CODI_IMP`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODI_IMP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 155 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_imposto | `codi_imp` | integer(4) |  |  | Código do imposto |
| ordem | `ordem` | integer(4) |  |  | Ordem |

**Filtros:** `codigo_do_imposto` (eq/in)

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

