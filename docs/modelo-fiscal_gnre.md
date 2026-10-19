# Modelo — Fiscal - gnre (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/fiscal_gnre.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

5 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [efgnre_avulsa_receita_produtos](#efgnre_avulsa_receita_produtos) | `EFGNRE_AVULSA_RECEITA_PRODUTOS` | 2.037 | pequeno | — |
| [efgnre_avulsa_receita](#efgnre_avulsa_receita) | `EFGNRE_AVULSA_RECEITA` | 251 | pequeno | — |
| [efgnre_avulsa_receita_documentos_origem](#efgnre_avulsa_receita_documentos_origem) | `EFGNRE_AVULSA_RECEITA_DOCUMENTOS_ORIGEM` | 251 | pequeno | — |
| [efgnre_receita_produtos](#efgnre_receita_produtos) | `EFGNRE_RECEITA_PRODUTOS` | 144 | pequeno | — |
| [efgnre_avulsa_receita_detalhamento](#efgnre_avulsa_receita_detalhamento) | `EFGNRE_AVULSA_RECEITA_DETALHAMENTO` | 122 | pequeno | — |

## efgnre_avulsa_receita_produtos

**Produtos - GNRE Avulsa** — tabela `EFGNRE_AVULSA_RECEITA_PRODUTOS` (2.037 linhas)

Produtos - GNRE Avulsa. 2.037 linhas no catálogo; chave: UF_FAVORECIDA, CODIGO_RECEITA_GNRE, CODIGO_PRODUTO_GNRE.

- **Chave:** `UF_FAVORECIDA, CODIGO_RECEITA_GNRE, CODIGO_PRODUTO_GNRE`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `UF_FAVORECIDA asc`, `CODIGO_RECEITA_GNRE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2.037 linhas.
- Vínculo eftabela_gnre_avulsa_pro (EFTABELA_GNRE_AVULSA_PRODUTOS): 0 de 2.037 linhas sem registro relacionado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| uf_favorecida | `uf_favorecida` | char(2) |  |  | UF Favorecida |
| codigo_da_receita | `codigo_receita_gnre` | integer(4) |  |  | Código da receita |
| codigo_do_produto_da_receitar | `codigo_produto_gnre` | integer(4) |  |  | Código do produto da receitar |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `eftabela_gnre_avulsa_pro` → `EFTABELA_GNRE_AVULSA_PRODUTOS` por `codigo_produto_gnre` = `codigo_produto_gnre`; colunas: `eftabela_gnre_avulsa_pro_nome`

**Filtros:** `uf_favorecida` (eq/in), `codigo_da_receita` (eq/in), `codigo_do_produto_da_receitar` (eq/in)

## efgnre_avulsa_receita

**Tabela de receita - GNRE Avulsa** — tabela `EFGNRE_AVULSA_RECEITA` (251 linhas)

Tabela de receita - GNRE Avulsa. 251 linhas no catálogo; chave: UF_FAVORECIDA, CODIGO_RECEITA_GNRE.

- **Chave:** `UF_FAVORECIDA, CODIGO_RECEITA_GNRE`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `UF_FAVORECIDA asc`, `CODIGO_RECEITA_GNRE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 251 linhas.
- Vínculo eftabela_gnre_avulsa_rec (EFTABELA_GNRE_AVULSA_RECEITA): 0 de 251 linhas sem registro relacionado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| uf_favorecida | `uf_favorecida` | char(2) |  |  | UF Favorecida |
| codigo_da_receita | `codigo_receita_gnre` | integer(4) |  |  | Código da receita |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `eftabela_gnre_avulsa_rec` → `EFTABELA_GNRE_AVULSA_RECEITA` por `codigo_receita_gnre` = `codigo_receita_gnre`; colunas: `eftabela_gnre_avulsa_rec_nome`

**Filtros:** `uf_favorecida` (eq/in), `codigo_da_receita` (eq/in)

## efgnre_avulsa_receita_documentos_origem

**Documentos de origem - GNRE Avulsa** — tabela `EFGNRE_AVULSA_RECEITA_DOCUMENTOS_ORIGEM` (251 linhas)

Documentos de origem - GNRE Avulsa. 251 linhas no catálogo; chave: UF_FAVORECIDA, CODIGO_RECEITA_GNRE, CODIGO_DOCUMENTO_ORIGEM_GNRE.

- **Chave:** `UF_FAVORECIDA, CODIGO_RECEITA_GNRE, CODIGO_DOCUMENTO_ORIGEM_GNRE`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `UF_FAVORECIDA asc`, `CODIGO_RECEITA_GNRE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 251 linhas.
- Vínculo eftabela_gnre_avulsa_doc (EFTABELA_GNRE_AVULSA_DOCUMENTOS_ORIGEM): 0 de 251 linhas sem registro relacionado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| uf_favorecida | `uf_favorecida` | char(2) |  |  | UF Favorecida |
| codigo_da_receita | `codigo_receita_gnre` | integer(4) |  |  | Código da receita |
| codigo_do_documento_de_origem_da_receita | `codigo_documento_origem_gnre` | integer(4) |  |  | Código do documento de origem da receita |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `eftabela_gnre_avulsa_doc` → `EFTABELA_GNRE_AVULSA_DOCUMENTOS_ORIGEM` por `codigo_documento_origem_gnre` = `codigo_documento_origem_gnre`; colunas: `eftabela_gnre_avulsa_doc_nome`

**Filtros:** `uf_favorecida` (eq/in), `codigo_da_receita` (eq/in), `codigo_do_documento_de_origem_da_receita` (eq/in)

## efgnre_receita_produtos

**GNRE - Receita** — tabela `EFGNRE_RECEITA_PRODUTOS` (144 linhas)

GNRE - Receita. 144 linhas no catálogo; chave: UF_FAVORECIDA, CODIGO_RECEITA_GNRE, CODIGO_PRODUTO_GNRE.

- **Chave:** `UF_FAVORECIDA, CODIGO_RECEITA_GNRE, CODIGO_PRODUTO_GNRE`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `UF_FAVORECIDA asc`, `CODIGO_RECEITA_GNRE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 144 linhas.
- Vínculo eftabela_gnre_avulsa_pro (EFTABELA_GNRE_AVULSA_PRODUTOS): 0 de 144 linhas sem registro relacionado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| uf_favorecida | `uf_favorecida` | char(2) |  |  | UF favorecida |
| codigo_receita | `codigo_receita_gnre` | integer(4) |  |  | Código Receita |
| codigo_produto | `codigo_produto_gnre` | integer(4) |  |  | Código Produto |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `eftabela_gnre_avulsa_pro` → `EFTABELA_GNRE_AVULSA_PRODUTOS` por `codigo_produto_gnre` = `codigo_produto_gnre`; colunas: `eftabela_gnre_avulsa_pro_nome`

**Filtros:** `uf_favorecida` (eq/in), `codigo_receita` (eq/in), `codigo_produto` (eq/in)

## efgnre_avulsa_receita_detalhamento

**Detalhamento - GNRE Avulsa** — tabela `EFGNRE_AVULSA_RECEITA_DETALHAMENTO` (122 linhas)

Detalhamento - GNRE Avulsa. 122 linhas no catálogo; chave: UF_FAVORECIDA, CODIGO_RECEITA_GNRE, CODIGO_DETALHAMENTO_RECEITA_GNRE.

- **Chave:** `UF_FAVORECIDA, CODIGO_RECEITA_GNRE, CODIGO_DETALHAMENTO_RECEITA_GNRE`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `UF_FAVORECIDA asc`, `CODIGO_RECEITA_GNRE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 122 linhas.
- Vínculo eftabela_gnre_avulsa_det (EFTABELA_GNRE_AVULSA_DETALHAMENTO): 0 de 122 linhas sem registro relacionado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| uf_favorecida | `uf_favorecida` | char(2) |  |  | UF Favorecida |
| codigo_da_receita | `codigo_receita_gnre` | integer(4) |  |  | Código da receita |
| codigo_do_detalhamento_da_receita | `codigo_detalhamento_receita_gnre` | integer(4) |  |  | Código do detalhamento da receita |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `eftabela_gnre_avulsa_det` → `EFTABELA_GNRE_AVULSA_DETALHAMENTO` por `codigo_detalhamento_receita_gnre` = `codigo_detalhamento_receita_gnre`; colunas: `eftabela_gnre_avulsa_det_nome`

**Filtros:** `uf_favorecida` (eq/in), `codigo_da_receita` (eq/in), `codigo_do_detalhamento_da_receita` (eq/in)

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

