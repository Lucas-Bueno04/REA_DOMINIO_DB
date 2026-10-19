# Modelo — Fiscal - parametro (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/fiscal_parametro.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

2 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [efparametro_vigencia_aproveita_credito](#efparametro_vigencia_aproveita_credito) | `EFPARAMETRO_VIGENCIA_APROVEITA_CREDITO` | 103.824 | medio | empresa |
| [efparametro_vigencia_inscricoes_subtri](#efparametro_vigencia_inscricoes_subtri) | `EFPARAMETRO_VIGENCIA_INSCRICOES_SUBTRI` | 16 | pequeno | empresa |

## efparametro_vigencia_aproveita_credito

**Parametros - Cadastro - Escrita Fiscal - Aproveitamento Crédito** — tabela `EFPARAMETRO_VIGENCIA_APROVEITA_CREDITO` (103.824 linhas)

Parametros - Cadastro - Escrita Fiscal - Aproveitamento Crédito. 103.824 linhas no catálogo; chave: CODI_EMP, VIGENCIA_PAR, CODIGO_CREDITO.

- **Chave:** `CODI_EMP, VIGENCIA_PAR, CODIGO_CREDITO`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA_PAR`
- **Ordem padrão:** `VIGENCIA_PAR desc`, `CODIGO_CREDITO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 103.824 linhas, 896 empresa(s), VIGENCIA_PAR de 1964-06-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| vigencia | `vigencia_par` | date(4) |  |  | Vigência |
| codigo_do_credito | `codigo_credito` | integer(4) |  |  | Código do Crédito |
| ordem_de_aproveitamento | `ordem` | integer(4) |  |  | Ordem de Aproveitamento |

**Filtros:** `vigencia` (eq/in), `codigo_do_credito` (eq/in)

## efparametro_vigencia_inscricoes_subtri

**Paramentros - Inscricoes de Substituicao Tributaria** — tabela `EFPARAMETRO_VIGENCIA_INSCRICOES_SUBTRI` (16 linhas)

Paramentros - Inscricoes de Substituicao Tributaria. 16 linhas no catálogo; chave: CODI_EMP, SIGL_EST, VIGENCIA_PAR.

- **Chave:** `CODI_EMP, SIGL_EST, VIGENCIA_PAR`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA_PAR`
- **Ordem padrão:** `VIGENCIA_PAR desc`, `SIGL_EST asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 16 linhas, 4 empresa(s), VIGENCIA_PAR de 2026-01-01 a 2026-05-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sigla_do_estado_uf | `sigl_est` | char(2) |  |  | Sigla do estado (UF) |
| vigencia | `vigencia_par` | date(4) |  |  | Vigencia |
| inscricao_estadual 🔒 | `iest_inf` | char(22) |  |  | Inscricao Estadual |
| preco_medio_ponderado_fiscal | `pmpf_inf` | char(1) |  |  | Preco Medio Ponderado Fiscal |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | integer(4) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |

**Filtros:** `sigla_do_estado_uf` (eq/in), `vigencia` (eq/in), `inscricao_estadual` (contem/prefixo), `preco_medio_ponderado_fiscal` (eq/in)

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

