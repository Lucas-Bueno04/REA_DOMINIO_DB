# Modelo — Contábil - bem (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/contabil_bem.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

4 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [pmbem_taxa_alternativa](#pmbem_taxa_alternativa) | `PMBEM_TAXA_ALTERNATIVA` | 3.927 | pequeno | empresa |
| [pmbem_documentos_fiscais](#pmbem_documentos_fiscais) | `PMBEM_DOCUMENTOS_FISCAIS` | 372 | pequeno | empresa |
| [pmbem_lancto](#pmbem_lancto) | `PMBEM_LANCTO` | 116 | pequeno | empresa |
| [pmbem_historico](#pmbem_historico) | `PMBEM_HISTORICO` | 1 | pequeno | empresa |

## pmbem_taxa_alternativa

**Bens - Taxa Alternativa** — tabela `PMBEM_TAXA_ALTERNATIVA` (3.927 linhas)

Bens - Taxa Alternativa. 3.927 linhas no catálogo; chave: CODI_EMP, I_BEM, SEQUENCIAL.

- **Chave:** `CODI_EMP, I_BEM, SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA`
- **Ordem padrão:** `VIGENCIA desc`, `I_BEM asc`, `SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3.928 linhas, 260 empresa(s), VIGENCIA de 2006-01-01 a 2026-10-01.
- Vínculo pmbem (PMBEM): 0 de 4 linhas sem registro relacionado (empresa 750).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| bem | `i_bem` | numeric(16) |  |  | Bem |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| a_partir_de | `vigencia` | date(4) |  |  | A partir de |
| taxa_alternativa | `taxa_alternativa` | numeric(7) |  |  | Taxa alternativa |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `pmbem` → `PMBEM` por `codi_emp` = `codi_emp` e `i_bem` = `i_bem`; colunas: `pmbem_nome`

**Filtros:** `bem` (eq/in), `sequencial` (eq/in), `a_partir_de` (entre/gte/lte)

## pmbem_documentos_fiscais

**Tabela de cadastro referente a documento Notas Fiscais / Conhecimento** — tabela `PMBEM_DOCUMENTOS_FISCAIS` (372 linhas)

Tabela de cadastro referente a documento Notas Fiscais / Conhecimento. 372 linhas no catálogo; chave: CODI_EMP, I_BEM, SEQUENCIAL.

- **Chave:** `CODI_EMP, I_BEM, SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_EMISSAO`
- **Ordem padrão:** `DATA_EMISSAO desc`, `I_BEM asc`, `SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 372 linhas, 71 empresa(s), DATA_EMISSAO de 2010-01-18 a 2024-11-18.
- Vínculo pmbem (PMBEM): 0 de 2 linhas sem registro relacionado (empresa 1111).
- Vínculo effornece (effornece): 0 de 2 linhas sem registro relacionado (empresa 1111).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_bem | `i_bem` | numeric(16) |  |  | Código do bem |
| numero_sequencial | `sequencial` | integer(4) |  |  | Número sequencial |
| numero | `numero` | numeric(15) |  |  | Número |
| serie | `serie` | char(7) |  |  | Série |
| data_de_emissao | `data_emissao` | date(4) |  |  | Data de emissão |
| especie | `modelo` | integer(4) |  |  | Espécie |
| chave_nfe | `chave_nfe` | char(44) |  |  | Chave NFe |
| fornecedor | `codi_for` | integer(4) |  |  | Fornecedor |
| emitente_t_terceiros_p_propio | `emitente` | char(1) |  |  | Emitente T - Terceiros / P - Própio |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do Produto |
| sequencial_do_item | `sequencial_item` | integer(4) |  |  | Sequencial do Item |
| documento_c_conhecimento_de_transporte_n | `tipo` | char(1) |  |  | Documento C - Conhecimento de Transporte / N - Notas Fiscais |
| numero_do_documento_de_arrecadacao | `num_doc_arrecadacao` | varchar(50) |  |  | Número do documento de arrecadação |
| quantidade | `quantidade` | numeric(13) |  |  | Quantidade |
| valor_do_icms | `valor_icms` | numeric(13) |  |  | Valor do ICMS |
| valor_do_icms_substituicao_tributaria | `valor_icms_st` | numeric(13) |  |  | Valor do ICMS - Substituição Tributária |
| valor_do_icms_frete | `valor_icms_frete` | numeric(13) |  |  | Valor do ICMS - Frete |
| valor_do_icms_diferencial_de_aliquota | `valor_icms_difali` | numeric(13) |  |  | Valor do ICMS - Diferencial de Alíquota |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `pmbem` → `PMBEM` por `codi_emp` = `codi_emp` e `i_bem` = `i_bem`; colunas: `pmbem_nome`
- `effornece` → `effornece` por `codi_emp` = `codi_emp` e `codi_for` = `codi_for`; colunas: `effornece_nome`

**Filtros:** `codigo_do_bem` (eq/in), `numero_sequencial` (eq/in), `data_de_emissao` (entre/gte/lte), `serie` (eq/in), `chave_nfe` (contem/prefixo), `fornecedor` (eq/in), `emitente_t_terceiros_p_propio` (eq/in), `codigo_do_produto` (eq/in), `documento_c_conhecimento_de_transporte_n` (eq/in), `numero_do_documento_de_arrecadacao` (contem/prefixo)

## pmbem_lancto

**Bens - Lançamentos Contábeis** — tabela `PMBEM_LANCTO` (116 linhas)

Bens - Lançamentos Contábeis. 116 linhas no catálogo; chave: CODI_EMP, I_BEM, EMPRESA_LAN, NUME_LAN.

- **Chave:** `CODI_EMP, I_BEM, EMPRESA_LAN, NUME_LAN`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_BEM asc`, `EMPRESA_LAN asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 114 linhas, 30 empresa(s).
- Vínculo pmbem (PMBEM): 0 de 2 linhas sem registro relacionado (empresa 881).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| bem | `i_bem` | numeric(16) |  |  | Bem |
| empresa_do_lancamento_contabil | `empresa_lan` | integer(4) |  |  | Empresa do lançamento contábil |
| numero_do_lancamento_contabil | `nume_lan` | integer(4) |  |  | Número do lançamento contábil |
| empresa_que_originou_o_lancamento_contab | `fili_lan` | integer(4) |  |  | Empresa que originou o lançamento contábil |
| codigo_do_lote | `codi_lote` | integer(4) |  |  | Código do lote |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `pmbem` → `PMBEM` por `codi_emp` = `codi_emp` e `i_bem` = `i_bem`; colunas: `pmbem_nome`

**Filtros:** `bem` (eq/in), `empresa_do_lancamento_contabil` (eq/in), `numero_do_lancamento_contabil` (eq/in), `codigo_do_lote` (eq/in)

## pmbem_historico

**Bens - Históricos** — tabela `PMBEM_HISTORICO` (1 linhas)

Bens - Históricos. 1 linhas no catálogo; chave: CODI_EMP, I_BEM, SEQUENCIAL.

- **Chave:** `CODI_EMP, I_BEM, SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_HISTORICO`
- **Ordem padrão:** `DATA_HISTORICO desc`, `I_BEM asc`, `SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s), DATA_HISTORICO de 2026-04-30 a 2026-04-30.
- Vínculo pmbem (PMBEM): 0 de 1 linhas sem registro relacionado (empresa 591).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| bem | `i_bem` | numeric(16) |  |  | Bem |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| data | `data_historico` | date(4) |  |  | Data |
| descricao | `descricao` | varchar(100) |  |  | Descrição |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `pmbem` → `PMBEM` por `codi_emp` = `codi_emp` e `i_bem` = `i_bem`; colunas: `pmbem_nome`

**Filtros:** `bem` (eq/in), `sequencial` (eq/in), `data` (entre/gte/lte), `descricao` (contem/prefixo)

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

