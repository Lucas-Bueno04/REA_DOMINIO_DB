# Modelo — Financeiro do escritório - tabela (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/financeiro_tabela.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

5 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [hrtabela_natureza_operacao](#hrtabela_natureza_operacao) | `HRTABELA_NATUREZA_OPERACAO` | 1.435 | pequeno | — |
| [hrtabela_mensagem_inconsistencia_importacao_remessa](#hrtabela_mensagem_inconsistencia_importacao_remessa) | `HRTABELA_MENSAGEM_INCONSISTENCIA_IMPORTACAO_REMESSA` | 551 | pequeno | — |
| [hrtabela_especie_titulo](#hrtabela_especie_titulo) | `HRTABELA_ESPECIE_TITULO` | 378 | pequeno | — |
| [hrtabela_nfse_aliquota_ibpt](#hrtabela_nfse_aliquota_ibpt) | `HRTABELA_NFSE_ALIQUOTA_IBPT` | 204 | pequeno | — |
| [hrtabela_cfps_nfse](#hrtabela_cfps_nfse) | `HRTABELA_CFPS_NFSE` | 57 | pequeno | — |

## hrtabela_natureza_operacao

**Natureza de operação para NFS-e** — tabela `HRTABELA_NATUREZA_OPERACAO` (1.435 linhas)

Natureza de operação para NFS-e. 1.435 linhas no catálogo; chave: I_SEQUENCIAL.

- **Chave:** `I_SEQUENCIAL`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `DATA_VIGENCIA`
- **Ordem padrão:** `DATA_VIGENCIA desc`, `I_SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.428 linhas, DATA_VIGENCIA de 1900-01-01 a 2023-08-28.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_sequencial | `i_sequencial` | integer(4) |  |  | Código sequencial |
| data_da_vigencia | `data_vigencia` | date(4) |  |  | Data da vigência |
| municipio_federal | `municipio_srf` | integer(4) |  |  | Município federal |
| item | `item` | integer(4) |  |  | Item |
| descricao | `descricao` | varchar(100) |  |  | Descrição |
| descricao_da_coluna | `descricao_coluna` | varchar(80) |  |  | Descrição da coluna |

**Filtros:** `codigo_sequencial` (eq/in), `data_da_vigencia` (entre/gte/lte), `descricao` (contem/prefixo), `descricao_da_coluna` (contem/prefixo)

## hrtabela_mensagem_inconsistencia_importacao_remessa

**Mensagens de inconsistências de arquivos de retorno de boleto bancário** — tabela `HRTABELA_MENSAGEM_INCONSISTENCIA_IMPORTACAO_REMESSA` (551 linhas)

Mensagens de inconsistências de arquivos de retorno de boleto bancário. 551 linhas no catálogo; chave: CODIGO, BANCO, TIPO_REMESSA.

- **Chave:** `CODIGO, BANCO, TIPO_REMESSA`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`, `BANCO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 551 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_mensagem | `codigo` | integer(4) |  |  | Código da mensagem |
| codigo_do_banco | `banco` | integer(4) |  |  | Código do banco |
| tipo_da_remessa_0_ambos_1_cnab_240_2_cna | `tipo_remessa` | integer(4) |  |  | Tipo da Remessa: 0 = Ambos/ 1 = CNAB 240/ 2 = CNAB 400 |
| descricao_da_mensagem | `descricao` | varchar(512) |  |  | Descrição da mensagem |

**Filtros:** `codigo_da_mensagem` (eq/in), `codigo_do_banco` (eq/in), `tipo_da_remessa_0_ambos_1_cnab_240_2_cna` (eq/in), `descricao_da_mensagem` (contem/prefixo)

## hrtabela_especie_titulo

**Tabela de especie de titulos - cobrança registrada - conta financeira** — tabela `HRTABELA_ESPECIE_TITULO` (378 linhas)

Tabela de especie de titulos - cobrança registrada - conta financeira. 378 linhas no catálogo; chave: CODIGO, SOMENTE_BANCO, COOPERATIVA_CREDITO, TIPO_REMESSA, CARTEIRA, COOPERATIVA_CREDITO_BANCO, VERSAO_ARQUIVO.

- **Chave:** `CODIGO, SOMENTE_BANCO, COOPERATIVA_CREDITO, TIPO_REMESSA, CARTEIRA, COOPERATIVA_CREDITO_BANCO, VERSAO_ARQUIVO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`, `SOMENTE_BANCO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 378 linhas.
- banco_da_cooperativa_u_unicred_s_sicoob: todos os valores reais estão no comentário do banco (U=320, N=30, S=28).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo` | integer(4) |  |  | Codigo |
| somente_para_o_banco_0_banco_padrao | `somente_banco` | integer(4) |  |  | Somente para o banco (0 = Banco padrão) |
| cooperativa_de_credito_s_n | `cooperativa_credito` | char(1) |  |  | Cooperativa de crédito (S/N) |
| tipo_remessa | `tipo_remessa` | integer(4) |  |  | Tipo de remessa (0 = Ambos / 1 = 240 posições / 2 = 400 posições |
| carteira | `carteira` | integer(4) |  |  | Carteira |
| banco_da_cooperativa_u_unicred_s_sicoob | `cooperativa_credito_banco` | char(1) |  | hrtabela_especie_titulo_banco_da_coo | Banco da cooperativa (U=Unicred/S=Sicoob/N=Uniprime) |
| versao | `versao_arquivo` | integer(4) |  |  | Versão |
| descricao | `descricao` | varchar(128) |  |  | Descricao |

**Filtros:** `codigo` (eq/in), `somente_para_o_banco_0_banco_padrao` (eq/in), `cooperativa_de_credito_s_n` (eq/in), `tipo_remessa` (eq/in), `carteira` (eq/in), `banco_da_cooperativa_u_unicred_s_sicoob` (eq/in), `versao` (eq/in), `descricao` (contem/prefixo)

## hrtabela_nfse_aliquota_ibpt

**Tabela Alíquota de impostos conforme IBPT** — tabela `HRTABELA_NFSE_ALIQUOTA_IBPT` (204 linhas)

Tabela Alíquota de impostos conforme IBPT. 204 linhas no catálogo; chave: I_ALIQUOTA.

- **Chave:** `I_ALIQUOTA`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `I_ALIQUOTA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 204 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `i_aliquota` | integer(4) |  |  | Código |
| descricao | `descricao` | varchar(500) |  |  | Descrição |
| aliquota | `aliquota` | numeric(5) |  |  | Alíquota |

**Filtros:** `codigo` (eq/in), `descricao` (contem/prefixo)

## hrtabela_cfps_nfse

**Tabela Codigo Fiscal de Prestacoes de Servicos - NFSE** — tabela `HRTABELA_CFPS_NFSE` (57 linhas)

Tabela Codigo Fiscal de Prestacoes de Servicos - NFSE. 57 linhas no catálogo; chave: I_CFPS.

- **Chave:** `I_CFPS`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `I_CFPS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 57 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_cfps | `i_cfps` | integer(4) |  |  | Código do CFPS |
| descricao_do_cfps | `descricao` | varchar(512) |  |  | Descrição do CFPS |

**Filtros:** `codigo_do_cfps` (eq/in), `descricao_do_cfps` (contem/prefixo)

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

### hrtabela_especie_titulo_banco_da_coo

Confirmado: sim

> Todos os valores observados em HRTABELA_ESPECIE_TITULO.COOPERATIVA_CREDITO_BANCO estão no comentário do banco (2026-10-18). Distribuição: U=320, N=30, S=28.

| Código | Significado |
|---|---|
| U | Unicred |
| S | Sicoob |
| N | Uniprime |

