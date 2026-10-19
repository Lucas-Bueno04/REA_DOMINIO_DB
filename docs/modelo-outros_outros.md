# Modelo — Outros - outros (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/outros_outros.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

3 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [relatorios_atualizacao](#relatorios_atualizacao) | `RELATORIOS_ATUALIZACAO` | 910 | pequeno | — |
| [tria_controle](#tria_controle) | `TRIA_CONTROLE` | 9 | pequeno | — |
| [confatualizacao](#confatualizacao) | `confatualizacao` | 1 | pequeno | — |

## relatorios_atualizacao

**CONTROLE DE ATUALIZACO DE RELATORIOS DO GERADOR** — tabela `RELATORIOS_ATUALIZACAO` (910 linhas)

CONTROLE DE ATUALIZACO DE RELATORIOS DO GERADOR. 910 linhas no catálogo; chave: I_RELATORIOS_ATUALIZACAO.

- **Chave:** `I_RELATORIOS_ATUALIZACAO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `I_RELATORIOS_ATUALIZACAO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 910 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| sequencial | `i_relatorios_atualizacao` | integer(4) |  |  | SEQUENCIAL |
| identificador_do_relatorio | `padrao` | char(50) |  |  | IDENTIFICADOR DO RELATORIO |
| revisao_do_relatorio_no_banco_de_dados | `revisao_db` | char(50) |  |  | REVISAO DO RELATORIO NO BANCO DE DADOS |
| revisao_do_relatorio_no_ponto_ver | `revisao_ver` | char(50) |  |  | REVISAO DO RELATORIO NO PONTO VER |
| usado_pelos_comandos_de_insert_na_atuali | `i_relatorio` | integer(4) |  |  | USADO PELOS COMANDOS DE INSERT NA ATUALIZACAO |
| c_1_classificacao_0_relatorio | `eh_classificacao` | integer(4) |  |  | 1.CLASSIFICACAO  0.RELATORIO |

**Filtros:** `sequencial` (eq/in), `identificador_do_relatorio` (contem/prefixo), `revisao_do_relatorio_no_banco_de_dados` (contem/prefixo), `revisao_do_relatorio_no_ponto_ver` (contem/prefixo), `usado_pelos_comandos_de_insert_na_atuali` (eq/in)

## tria_controle

**Controle de funcionalidades que utilizam TRIA** — tabela `TRIA_CONTROLE` (9 linhas)

Controle de funcionalidades que utilizam TRIA. 9 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 9 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_identificador | `codigo` | integer(4) |  |  | Código identificador |
| descricao | `descricao` | varchar(200) |  |  | Descrição |
| c_0_desativado_1_ativado | `status` | smallint(2) |  |  | 0:Desativado, 1:Ativado |

**Filtros:** `codigo_identificador` (eq/in), `descricao` (contem/prefixo)

## confatualizacao

**Configuracao do gerenciador de atualizacoes** — tabela `confatualizacao` (1 linhas)

Configuracao do gerenciador de atualizacoes. 1 linhas no catálogo; chave: i_confatualizacao.

- **Chave:** `i_confatualizacao`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `i_confatualizacao asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| i_confatualizacao | `i_confatualizacao` | integer(4) |  |  | i_confatualizacao |
| se_eh_para_testar_se_tem_uma_versao_disp | `verificar_versao` | tinyint(1) |  |  | Se eh para testar se tem uma versao disponivel no diretorio configurado. |
| caminho_para_verificar_se_tem_novas_vers | `caminho` | varchar(512) |  |  | Caminho para verificar se tem novas versões disponiveis |

**Filtros:** `i_confatualizacao` (eq/in), `caminho_para_verificar_se_tem_novas_vers` (contem/prefixo)

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

