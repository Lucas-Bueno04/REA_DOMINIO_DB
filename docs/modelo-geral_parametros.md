# Modelo — Geral - parametros (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/geral_parametros.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

5 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [geparametros_listagem_modelo_coluna_filtro](#geparametros_listagem_modelo_coluna_filtro) | `GEPARAMETROS_LISTAGEM_MODELO_COLUNA_FILTRO` | 5.314 | pequeno | — |
| [geparametros_impressao_relatorio](#geparametros_impressao_relatorio) | `GEPARAMETROS_IMPRESSAO_RELATORIO` | 2.794 | pequeno | — |
| [geparametros_impressora](#geparametros_impressora) | `GEPARAMETROS_IMPRESSORA` | 786 | pequeno | — |
| [geparametros_listagem_modelo_coluna](#geparametros_listagem_modelo_coluna) | `GEPARAMETROS_LISTAGEM_MODELO_COLUNA` | 95 | pequeno | — |
| [geparametros_listagem_modelo](#geparametros_listagem_modelo) | `GEPARAMETROS_LISTAGEM_MODELO` | 23 | pequeno | — |

## geparametros_listagem_modelo_coluna_filtro

**Configuração dos filtros dos relatórios gerados através do botão Listagem nos cadastros** — tabela `GEPARAMETROS_LISTAGEM_MODELO_COLUNA_FILTRO` (5.314 linhas)

Configuração dos filtros dos relatórios gerados através do botão Listagem nos cadastros. 5.314 linhas no catálogo; chave: ID_MODELO, ID_COLUNA, ID_FILTRO, USUARIO, TIPO_CONDICAO, VALOR_CONDICAO, OPERADOR, AVANCADO.

- **Chave:** `ID_MODELO, ID_COLUNA, ID_FILTRO, USUARIO, TIPO_CONDICAO, VALOR_CONDICAO, OPERADOR, AVANCADO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `ID_MODELO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 5.314 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| id_modelo | `id_modelo` | integer(4) |  |  |  |
| id_coluna | `id_coluna` | integer(4) |  |  |  |
| id_filtro | `id_filtro` | integer(4) |  |  |  |
| usuario | `usuario` | varchar(100) |  |  |  |
| tipo_condicao | `tipo_condicao` | integer(4) |  |  |  |
| valor_condicao | `valor_condicao` | varchar(500) |  |  |  |
| operador | `operador` | integer(4) |  |  |  |
| avancado | `avancado` | integer(4) |  |  |  |

**Filtros:** `id_modelo` (eq/in), `usuario` (contem/prefixo), `tipo_condicao` (eq/in), `valor_condicao` (contem/prefixo)

## geparametros_impressao_relatorio

**Parâmetros de impressao do relatório** — tabela `GEPARAMETROS_IMPRESSAO_RELATORIO` (2.794 linhas)

Parâmetros de impressao do relatório. 2.794 linhas no catálogo; chave: USUARIO, ID_RELATORIO, NOME_ESTACAO, MODULO.

- **Chave:** `USUARIO, ID_RELATORIO, NOME_ESTACAO, MODULO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `USUARIO asc`, `ID_RELATORIO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2.794 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| usuario | `usuario` | varchar(120) |  |  |  |
| id_relatorio | `id_relatorio` | varchar(120) |  |  |  |
| nome_estacao | `nome_estacao` | varchar(120) |  |  |  |
| modulo | `modulo` | smallint(2) |  |  |  |
| impressora_padrao | `impressora_padrao` | varchar(120) |  |  |  |
| percentual_zoom | `percentual_zoom` | integer(4) |  |  |  |
| largura_caracter | `largura_caracter` | integer(4) |  |  |  |
| percentual_aumentar | `percentual_aumentar` | numeric(13) |  |  |  |
| orientacao | `orientacao` | smallint(2) |  |  |  |
| espacamento_linhas | `espacamento_linhas` | smallint(2) |  |  |  |
| margem_direita | `margem_direita` | integer(4) |  |  |  |
| margem_esquerda | `margem_esquerda` | integer(4) |  |  |  |
| margem_superior | `margem_superior` | integer(4) |  |  |  |
| margem_inferior | `margem_inferior` | integer(4) |  |  |  |
| largura_papel | `largura_papel` | integer(4) |  |  |  |
| personalizadar_margem | `personalizadar_margem` | smallint(2) |  |  |  |
| personalizadar_impressao | `personalizadar_impressao` | smallint(2) |  |  |  |

**Filtros:** `usuario` (eq/in), `id_relatorio` (eq/in), `nome_estacao` (eq/in), `modulo` (eq/in), `impressora_padrao` (contem/prefixo)

## geparametros_impressora

**Parâmetros da impressora** — tabela `GEPARAMETROS_IMPRESSORA` (786 linhas)

Parâmetros da impressora. 786 linhas no catálogo; chave: USUARIO, NOME_IMPRESSORA, NOME_ESTACAO, NOME_EXECUTAVEL.

- **Chave:** `USUARIO, NOME_IMPRESSORA, NOME_ESTACAO, NOME_EXECUTAVEL`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `USUARIO asc`, `NOME_IMPRESSORA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 787 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| usuario | `usuario` | varchar(120) |  |  |  |
| nome_impressora | `nome_impressora` | varchar(120) |  |  |  |
| nome_estacao | `nome_estacao` | varchar(120) |  |  |  |
| nome_executavel | `nome_executavel` | varchar(40) |  |  |  |
| modelo | `modelo` | varchar(120) |  |  |  |
| codigo_compactacao10cpp | `codigo_compactacao10cpp` | varchar(40) |  |  |  |
| codigo_compactacao17cpp | `codigo_compactacao17cpp` | varchar(40) |  |  |  |
| codigo_compactacao20cpp | `codigo_compactacao20cpp` | varchar(40) |  |  |  |
| codigo_compactacaooitavos | `codigo_compactacaooitavos` | varchar(40) |  |  |  |
| codigo_compactacaosextos | `codigo_compactacaosextos` | varchar(40) |  |  |  |
| margem_direita | `margem_direita` | integer(4) |  |  |  |
| margem_esquerda | `margem_esquerda` | integer(4) |  |  |  |
| margem_superior | `margem_superior` | integer(4) |  |  |  |
| margem_inferior | `margem_inferior` | integer(4) |  |  |  |
| largura_papel | `largura_papel` | integer(4) |  |  |  |
| percentual_zoom | `percentual_zoom` | integer(4) |  |  |  |
| largura_caracter | `largura_caracter` | integer(4) |  |  |  |
| tipo | `tipo` | smallint(2) |  |  |  |
| percentual_aumentar | `percentual_aumentar` | numeric(13) |  |  |  |

**Filtros:** `usuario` (eq/in), `nome_impressora` (eq/in), `nome_estacao` (eq/in), `nome_executavel` (eq/in), `modelo` (contem/prefixo), `codigo_compactacao10cpp` (contem/prefixo), `codigo_compactacao17cpp` (contem/prefixo), `codigo_compactacao20cpp` (contem/prefixo), `codigo_compactacaooitavos` (contem/prefixo), `codigo_compactacaosextos` (contem/prefixo), `tipo` (eq/in)

## geparametros_listagem_modelo_coluna

**Configuração das colunas dos relatórios gerados através do botão Listagem nos cadastros** — tabela `GEPARAMETROS_LISTAGEM_MODELO_COLUNA` (95 linhas)

Configuração das colunas dos relatórios gerados através do botão Listagem nos cadastros. 95 linhas no catálogo; chave: ID_MODELO, ID_COLUNA, NOME_COLUNA, ORDENACAO, ORDEM_ORDENACAO, ORDEM_APRESENTACAO, SELECIONADA_EMISSAO, TAMANHO_COLUNA, TIPO_DADO, TIPO_FILTRO, NOME_COLUNA_DB.

- **Chave:** `ID_MODELO, ID_COLUNA, NOME_COLUNA, ORDENACAO, ORDEM_ORDENACAO, ORDEM_APRESENTACAO, SELECIONADA_EMISSAO, TAMANHO_COLUNA, TIPO_DADO, TIPO_FILTRO, NOME_COLUNA_DB`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `ID_MODELO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 95 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| id_modelo | `id_modelo` | integer(4) |  |  |  |
| id_coluna | `id_coluna` | integer(4) |  |  |  |
| nome_coluna | `nome_coluna` | varchar(100) |  |  |  |
| ordenacao | `ordenacao` | integer(4) |  |  |  |
| ordem_ordenacao | `ordem_ordenacao` | integer(4) |  |  |  |
| ordem_apresentacao | `ordem_apresentacao` | integer(4) |  |  |  |
| selecionada_emissao | `selecionada_emissao` | integer(4) |  |  |  |
| tamanho_coluna | `tamanho_coluna` | integer(4) |  |  |  |
| tipo_dado | `tipo_dado` | integer(4) |  |  |  |
| tipo_filtro | `tipo_filtro` | integer(4) |  |  |  |
| nome_coluna_db | `nome_coluna_db` | varchar(100) |  |  |  |

**Filtros:** `id_modelo` (eq/in), `nome_coluna` (contem/prefixo), `tipo_dado` (eq/in), `tipo_filtro` (eq/in), `nome_coluna_db` (contem/prefixo)

## geparametros_listagem_modelo

**Configuração dos relatórios gerados através do botão Listagem nos cadastros** — tabela `GEPARAMETROS_LISTAGEM_MODELO` (23 linhas)

Configuração dos relatórios gerados através do botão Listagem nos cadastros. 23 linhas no catálogo; chave: ID_MODELO, JANELA, NOME_MODELO, TIPO_PAGINA, DESTACAR_LINHA, NOME_TABELA_DB.

- **Chave:** `ID_MODELO, JANELA, NOME_MODELO, TIPO_PAGINA, DESTACAR_LINHA, NOME_TABELA_DB`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `ID_MODELO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 23 linhas.
- Colunas expostas nulas em 100% das linhas (1): nome_tabela_db.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| id_modelo | `id_modelo` | integer(4) |  |  |  |
| janela | `janela` | varchar(150) |  |  |  |
| nome_modelo | `nome_modelo` | varchar(50) |  |  |  |
| tipo_pagina | `tipo_pagina` | integer(4) |  |  |  |
| destacar_linha | `destacar_linha` | integer(4) |  |  |  |
| nome_tabela_db | `nome_tabela_db` | varchar(200) |  |  |  |

**Filtros:** `id_modelo` (eq/in), `janela` (contem/prefixo), `nome_modelo` (contem/prefixo), `tipo_pagina` (eq/in), `nome_tabela_db` (contem/prefixo)

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

