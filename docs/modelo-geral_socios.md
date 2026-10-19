# Modelo — Geral - socios (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/geral_socios.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

6 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [gesocios_empresas](#gesocios_empresas) | `gesocios_empresas` | 2.022 | pequeno | — |
| [gesocios_dependentes](#gesocios_dependentes) | `gesocios_dependentes` | 3 | pequeno | — |
| [gesocios_bens](#gesocios_bens) | `gesocios_bens` | 2 | pequeno | — |
| [gesocios_comerciais](#gesocios_comerciais) | `gesocios_comerciais` | 2 | pequeno | — |
| [gesocios_pessoais](#gesocios_pessoais) | `gesocios_pessoais` | 2 | pequeno | — |
| [gesocios_seguros](#gesocios_seguros) | `gesocios_seguros` | 2 | pequeno | — |

## gesocios_empresas

**Socios - Cadastro - Empresas que Participa** — tabela `gesocios_empresas` (2.022 linhas)

Socios - Cadastro - Empresas que Participa. 2.022 linhas no catálogo; chave: i_socio, cnpj.

- **Chave:** `i_socio, cnpj`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `data_entrada`
- **Ordem padrão:** `data_entrada desc`, `i_socio asc`, `cnpj asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2.022 linhas, data_entrada de 1987-01-16 a 2026-05-04.
- Vínculo gesocios (gesocios): 0 de 2.022 linhas sem registro relacionado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_socio | `i_socio` | integer(4) |  |  | Codigo socio |
| cnpj 🔒 | `cnpj` | char(14) |  |  | CNPJ |
| razao_social 🔒 | `razao_social` | char(40) |  |  | Razao Social |
| data_de_entrada | `data_entrada` | date(4) |  |  | Data de entrada |
| data_de_saida | `data_saida` | date(4) |  |  | Data de saida |
| participacao_percentual | `participacao` | numeric(5) |  |  | Participacao percentual |
| dirigente_s_n | `dirigente` | char(1) |  |  | Dirigente (S/N) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `gesocios` → `gesocios` por `i_socio` = `i_socio`; colunas: `gesocios_nome`

**Filtros:** `codigo_socio` (eq/in), `cnpj` (eq/in), `data_de_entrada` (entre/gte/lte), `data_de_saida` (entre/gte/lte), `razao_social` (contem/prefixo), `dirigente_s_n` (eq/in)

## gesocios_dependentes

**Socios - Cadastro - Dependentes** — tabela `gesocios_dependentes` (3 linhas)

Socios - Cadastro - Dependentes. 3 linhas no catálogo; chave: i_socio, sequencial.

- **Chave:** `i_socio, sequencial`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `dtnascimento`
- **Ordem padrão:** `dtnascimento desc`, `i_socio asc`, `sequencial asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3 linhas, dtnascimento de 1998-01-01 a 2004-05-02.
- tipo_21_filho_24_descendente_31_dependen: todos os valores reais estão no comentário do banco (21=3).
- Vínculo gesocios (gesocios): 0 de 3 linhas sem registro relacionado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_socio | `i_socio` | integer(4) |  |  | Codigo socio |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| tipo_21_filho_24_descendente_31_dependen | `tipo` | tinyint(1) |  | gesocios_dependentes_tipo_21_filho_24_desce | Tipo (21 - Filho/24 - Descendente/31 - Dependente Ascendente/41 - Menor Probre/90 - Outros) |
| nome | `nome` | char(40) |  |  | Nome |
| data_de_nascimento | `dtnascimento` | date(4) |  |  | Data de nascimento |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `gesocios` → `gesocios` por `i_socio` = `i_socio`; colunas: `gesocios_nome`

**Filtros:** `codigo_socio` (eq/in), `sequencial` (eq/in), `data_de_nascimento` (entre/gte/lte), `tipo_21_filho_24_descendente_31_dependen` (eq/in), `nome` (contem/prefixo)

## gesocios_bens

**Socios - Cadastro - Bens** — tabela `gesocios_bens` (2 linhas)

Socios - Cadastro - Bens. 2 linhas no catálogo; chave: i_socio, sequencial.

- **Chave:** `i_socio, sequencial`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `data_matricula`
- **Ordem padrão:** `data_matricula desc`, `i_socio asc`, `sequencial asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, data_matricula de 1999-01-10 a 1999-01-10.
- Colunas expostas nulas em 100% das linhas (5): valor_do_onus, credor, vencimento_final, empresa_do_leasing, data_do_contrato_de_leasing.
- classificacao_m_movel_i_imovel_s_semoven: todos os valores reais estão no comentário do banco (M=1, I=1).
- tipo_u_urbano_r_rural: todos os valores reais estão no comentário do banco (U=2).
- tipo_de_onus_p_penhora_h_hipoteca: todos os valores reais estão no comentário do banco (H=2).
- Vínculo gesocios (gesocios): 0 de 2 linhas sem registro relacionado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_socio | `i_socio` | integer(4) |  |  | Codigo socio |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| classificacao_m_movel_i_imovel_s_semoven | `classificacao` | char(1) |  | gesocios_bens_classificacao_m_movel_i_imove | Classificacao(M - Movel/I - Imovel/S - Semovente) |
| tipo_u_urbano_r_rural | `tipo` | char(1) |  | gesocios_bens_tipo_u_urbano_r_rural | Tipo (U - Urbano/R - Rural) |
| descricao | `descricao` | char(100) |  |  | Descricao |
| localizacao | `localizacao` | char(100) |  |  | Localizacao |
| valor_do_bem | `valor` | numeric(13) |  |  | Valor do bem |
| area_em_m2_ou_ha | `area` | numeric(13) |  |  | Area (em m2 ou HA) |
| area_construida_em_m2 | `area_construida` | numeric(13) |  |  | Area construida em m2 |
| onus_s_n | `onus` | char(1) |  |  | Onus (S/N) |
| tipo_de_onus_p_penhora_h_hipoteca | `tipo_onus` | char(1) |  | gesocios_bens_tipo_de_onus_p_penhora_h_hipo | Tipo de Onus ( P - Penhora/H - Hipoteca) |
| valor_do_onus | `valor_onus` | numeric(13) |  |  | Valor do onus |
| credor | `credor` | char(40) |  |  | Credor |
| matricula | `matricula` | char(20) |  |  | Matricula |
| cartorio | `cartorio` | char(30) |  |  | Cartorio |
| data_da_matricula | `data_matricula` | date(4) |  |  | Data da matricula |
| numero_do_livro | `livro` | char(10) |  |  | Numero do livro |
| numero_da_folha | `folha` | char(10) |  |  | Numero da folha |
| cessao_s_n | `cessao` | char(1) |  |  | Cessao (S/N) |
| bem_impenhoravel_s_n | `impenhoravel` | char(1) |  |  | Bem impenhoravel (S/N) |
| imovel_rural_enquadrado_s_n | `rural_enquadrado` | char(1) |  |  | Imovel rural enquadrado(S/N) |
| marca | `marca` | char(30) |  |  | Marca |
| ano | `ano` | integer(4) |  |  | Ano |
| alienado_s_n | `alienado` | char(1) |  |  | Alienado(S/N) |
| vencimento_final | `vencimento` | date(4) |  |  | Vencimento final |
| leasing_s_n | `leasing` | char(1) |  |  | Leasing (S/N) |
| empresa_do_leasing | `empresa` | char(30) |  |  | Empresa do leasing |
| data_do_contrato_de_leasing | `data_contrato` | date(4) |  |  | Data do contrato de leasing |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `gesocios` → `gesocios` por `i_socio` = `i_socio`; colunas: `gesocios_nome`

**Filtros:** `codigo_socio` (eq/in), `sequencial` (eq/in), `data_da_matricula` (entre/gte/lte), `vencimento_final` (entre/gte/lte), `data_do_contrato_de_leasing` (entre/gte/lte), `classificacao_m_movel_i_imovel_s_semoven` (eq/in), `tipo_u_urbano_r_rural` (eq/in), `descricao` (contem/prefixo), `localizacao` (contem/prefixo), `onus_s_n` (eq/in), `tipo_de_onus_p_penhora_h_hipoteca` (eq/in), `credor` (contem/prefixo), `matricula` (eq/in), `cartorio` (contem/prefixo)

## gesocios_comerciais

**Socios - Cadastro - Referencias Comerciais** — tabela `gesocios_comerciais` (2 linhas)

Socios - Cadastro - Referencias Comerciais. 2 linhas no catálogo; chave: i_socio, sequencial.

- **Chave:** `i_socio, sequencial`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `i_socio asc`, `sequencial asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas.
- Colunas expostas nulas em 100% das linhas (1): complemento.
- Vínculo gesocios (gesocios): 0 de 2 linhas sem registro relacionado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_socio | `i_socio` | integer(4) |  |  | Codigo socio |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| nome_da_empresa | `empresa` | char(40) |  |  | Nome da empresa |
| endereco 🔒 | `endereco` | char(40) |  |  | Endereco |
| bairro 🔒 | `bairro` | char(40) |  |  | Bairro |
| cidade | `cidade` | char(40) |  |  | Cidade |
| uf | `uf` | char(2) |  |  | UF |
| numero | `numero` | integer(4) |  |  | Numero |
| cep 🔒 | `cep` | char(8) |  |  | CEP |
| complemento | `complemento` | char(30) |  |  | Complemento |
| ddd | `ddd` | integer(4) |  |  | DDD |
| fone 🔒 | `fone` | char(14) |  |  | Fone |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `gesocios` → `gesocios` por `i_socio` = `i_socio`; colunas: `gesocios_nome`

**Filtros:** `codigo_socio` (eq/in), `sequencial` (eq/in), `nome_da_empresa` (contem/prefixo), `endereco` (contem/prefixo), `bairro` (contem/prefixo), `cidade` (contem/prefixo), `uf` (eq/in), `cep` (eq/in), `complemento` (contem/prefixo), `fone` (eq/in)

## gesocios_pessoais

**Socios - Cadastro - Referencias Pessoais** — tabela `gesocios_pessoais` (2 linhas)

Socios - Cadastro - Referencias Pessoais. 2 linhas no catálogo; chave: i_socio, sequencial.

- **Chave:** `i_socio, sequencial`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `i_socio asc`, `sequencial asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas.
- Colunas expostas nulas em 100% das linhas (1): complemento.
- Vínculo gesocios (gesocios): 0 de 2 linhas sem registro relacionado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_socio | `i_socio` | integer(4) |  |  | Codigo socio |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| nome_da_empresa | `empresa` | char(40) |  |  | Nome da empresa |
| endereco 🔒 | `endereco` | char(40) |  |  | Endereco |
| bairro 🔒 | `bairro` | char(40) |  |  | Bairro |
| cidade | `cidade` | char(40) |  |  | Cidade |
| uf | `uf` | char(2) |  |  | UF |
| numero | `numero` | integer(4) |  |  | Numero |
| cep 🔒 | `cep` | char(8) |  |  | CEP |
| complemento | `complemento` | char(30) |  |  | Complemento |
| ddd | `ddd` | integer(4) |  |  | DDD |
| fone 🔒 | `fone` | char(14) |  |  | Fone |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `gesocios` → `gesocios` por `i_socio` = `i_socio`; colunas: `gesocios_nome`

**Filtros:** `codigo_socio` (eq/in), `sequencial` (eq/in), `nome_da_empresa` (contem/prefixo), `endereco` (contem/prefixo), `bairro` (contem/prefixo), `cidade` (contem/prefixo), `uf` (eq/in), `cep` (eq/in), `complemento` (contem/prefixo), `fone` (eq/in)

## gesocios_seguros

**Socios - Cadastro - Seguros** — tabela `gesocios_seguros` (2 linhas)

Socios - Cadastro - Seguros. 2 linhas no catálogo; chave: i_socio, sequencial.

- **Chave:** `i_socio, sequencial`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `vencimento`
- **Ordem padrão:** `vencimento desc`, `i_socio asc`, `sequencial asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, vencimento de 2005-07-10 a 2005-07-10.
- Vínculo gesocios (gesocios): 0 de 2 linhas sem registro relacionado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_socio | `i_socio` | integer(4) |  |  | Codigo socio |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| modalidade_do_seguro | `modalidade` | char(30) |  |  | Modalidade do seguro |
| bem_segurado | `bem` | char(40) |  |  | Bem segurado |
| nome_da_seguradora | `seguradora` | char(40) |  |  | Nome da seguradora |
| valor_do_seguro | `valor` | numeric(13) |  |  | Valor do seguro |
| data_de_vencimento | `vencimento` | date(4) |  |  | Data de vencimento |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `gesocios` → `gesocios` por `i_socio` = `i_socio`; colunas: `gesocios_nome`

**Filtros:** `codigo_socio` (eq/in), `sequencial` (eq/in), `data_de_vencimento` (entre/gte/lte), `modalidade_do_seguro` (contem/prefixo), `bem_segurado` (contem/prefixo), `nome_da_seguradora` (contem/prefixo)

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

### gesocios_dependentes_tipo_21_filho_24_desce

Confirmado: sim

> Todos os valores observados em gesocios_dependentes.tipo estão no comentário do banco (2026-10-18). Distribuição: 21=3.

| Código | Significado |
|---|---|
| 21 | Filho |
| 24 | Descendente |
| 31 | Dependente Ascendente |
| 41 | Menor Probre |
| 90 | Outros |

### gesocios_bens_classificacao_m_movel_i_imove

Confirmado: sim

> Todos os valores observados em gesocios_bens.classificacao estão no comentário do banco (2026-10-18). Distribuição: M=1, I=1.

| Código | Significado |
|---|---|
| M | Movel |
| I | Imovel |
| S | Semovente |

### gesocios_bens_tipo_u_urbano_r_rural

Confirmado: sim

> Todos os valores observados em gesocios_bens.tipo estão no comentário do banco (2026-10-18). Distribuição: U=2.

| Código | Significado |
|---|---|
| U | Urbano |
| R | Rural |

### gesocios_bens_tipo_de_onus_p_penhora_h_hipo

Confirmado: sim

> Todos os valores observados em gesocios_bens.tipo_onus estão no comentário do banco (2026-10-18). Distribuição: H=2.

| Código | Significado |
|---|---|
| P | Penhora |
| H | Hipoteca |

