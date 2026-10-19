# Modelo — Geral - imposto (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/geral_imposto.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

6 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [geimposto_vigencia_pagamentos_ctb](#geimposto_vigencia_pagamentos_ctb) | `GEIMPOSTO_VIGENCIA_PAGAMENTOS_CTB` | 81.815 | medio | empresa |
| [geimposto_vigencia_parcelamento_ctb](#geimposto_vigencia_parcelamento_ctb) | `GEIMPOSTO_VIGENCIA_PARCELAMENTO_CTB` | 35.396 | medio | empresa |
| [geimposto_vigencia_recolhimento_ctb](#geimposto_vigencia_recolhimento_ctb) | `GEIMPOSTO_VIGENCIA_RECOLHIMENTO_CTB` | 3.213 | pequeno | empresa |
| [geimposto_vigencia_recolhimento_natureza_rendimento](#geimposto_vigencia_recolhimento_natureza_rendimento) | `GEIMPOSTO_VIGENCIA_RECOLHIMENTO_NATUREZA_RENDIMENTO` | 1.399 | pequeno | empresa |
| [geimposto_vigencia_codrec_natureza_rendimento](#geimposto_vigencia_codrec_natureza_rendimento) | `GEIMPOSTO_VIGENCIA_CODREC_NATUREZA_RENDIMENTO` | 48 | pequeno | empresa |
| [geimposto_vigencia_sub_apuracao](#geimposto_vigencia_sub_apuracao) | `GEIMPOSTO_VIGENCIA_SUB_APURACAO` | 3 | pequeno | empresa |

## geimposto_vigencia_pagamentos_ctb

**Impostos - Cadastro - Contas para Pagamento** — tabela `GEIMPOSTO_VIGENCIA_PAGAMENTOS_CTB` (81.815 linhas)

Impostos - Cadastro - Contas para Pagamento. 81.815 linhas no catálogo; chave: CODI_EMP, CODI_IMP, VIGENCIA_IMP.

- **Chave:** `CODI_EMP, CODI_IMP, VIGENCIA_IMP`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA_IMP`
- **Ordem padrão:** `VIGENCIA_IMP desc`, `CODI_IMP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 81.815 linhas, 1.504 empresa(s), VIGENCIA_IMP de 1964-06-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| vigencia | `vigencia_imp` | date(4) |  |  | Vigencia |
| conta_debito | `ctdb_ctp` | integer(4) |  |  | Conta debito |
| conta_credito | `ctcr_ctp` | integer(4) |  |  | Conta credito |
| historico_padrao | `chis_ctp` | integer(4) |  |  | Historico padrao |
| conta_debito_dos_juros | `jrdb_ctp` | integer(4) |  |  | Conta debito dos juros |
| conta_credito_dos_juros | `jrcr_ctp` | integer(4) |  |  | Conta credito dos juros |
| historico_padrao_dos_juros | `jrch_ctp` | integer(4) |  |  | Historico padrao dos juros |
| conta_debito_da_multa | `mtdb_ctp` | integer(4) |  |  | Conta debito da multa |
| conta_credito_da_multa | `mtcr_ctp` | integer(4) |  |  | Conta credito da multa |
| historico_padrao_da_multa | `mtch_ctp` | integer(4) |  |  | Historico padrao da multa |
| conta_credito_do_parcelamento | `ctparcelamentocredito` | integer(4) |  |  | Conta credito do parcelamento |
| historico_padrao_do_parcelamento | `htparcelamento` | integer(4) |  |  | Historico padrao do parcelamento |
| debito_valor_pago_a_maior_conta | `ctdebito_valor_pago_a_maior` | integer(4) |  |  | Débito Valor Pago a Maior - Conta |
| credito_valor_pago_a_maior_conta | `ctcredito_valor_pago_a_maior` | integer(4) |  |  | Crédito Valor Pago a Maior  - Conta |
| valor_pago_a_maior_historico | `ht_valor_pago_a_maior` | integer(4) |  |  | Valor Pago a Maior - Histórico |
| correcao_conta_debito | `ctcorrecao_debito` | integer(4) |  |  | Correção - Conta Débito |
| correcao_conta_credito | `ctcorrecao_credito` | integer(4) |  |  | Correção - Conta Crédito |
| correcao_historico | `htcorrecao` | integer(4) |  |  | Correção - Histórico |
| acrescimo_conta_debito | `ctacrescimo_debito` | integer(4) |  |  | Acrescimo - Conta Débito |
| acrescimo_conta_credito | `ctacrescimo_credito` | integer(4) |  |  | Acrescimo - Conta Crédito |
| acrescimo_historico | `htacrescimo` | integer(4) |  |  | Acrescimo - Histórico |
| desconto_debito | `ctdesconto_debito` | integer(4) |  |  | Desconto - Débito |
| desconto_credito | `ctdesconto_credito` | integer(4) |  |  | Desconto - Crédito |
| desconto_historico | `htdesconto` | integer(4) |  |  | Desconto - Histórico |

**Filtros:** `imposto` (eq/in), `vigencia` (eq/in)

## geimposto_vigencia_parcelamento_ctb

**Impostos - Cadastro - Contas para Parcelamento** — tabela `GEIMPOSTO_VIGENCIA_PARCELAMENTO_CTB` (35.396 linhas)

Impostos - Cadastro - Contas para Parcelamento. 35.396 linhas no catálogo; chave: CODI_EMP, CODI_IMP, VIGENCIA_IMP.

- **Chave:** `CODI_EMP, CODI_IMP, VIGENCIA_IMP`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA_IMP`
- **Ordem padrão:** `VIGENCIA_IMP desc`, `CODI_IMP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 35.398 linhas, 1.504 empresa(s), VIGENCIA_IMP de 1966-07-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| vigencia | `vigencia_imp` | date(4) |  |  | Vigência |
| gerar_lancamentos_de_partida_simples_s_n | `gerar_lancamento_partida_simples` | char(1) |  |  | Gerar lançamentos de partida simples (S/N) |
| conta_da_provisao | `ctprovisao` | integer(4) |  |  | Conta da provisão |
| historico_padrao_da_provisao | `htprovisao` | integer(4) |  |  | Histórico padrão da provisão |
| conta_provisao_dos_juros | `ctjurosprovisao` | integer(4) |  |  | Conta provisão dos juros |
| conta_despesa_dos_juros | `ctjurosdespesa` | integer(4) |  |  | Conta despesa dos juros |
| historico_padrao_dos_juros | `htjuros` | integer(4) |  |  | Histórico padrão dos juros |
| conta_provisao_da_multa | `ctmultaprovisao` | integer(4) |  |  | Conta provisão da multa |
| conta_despesa_da_multa | `ctmultadespesa` | integer(4) |  |  | Conta despesa da multa |
| historico_padrao_da_multa | `htmulta` | integer(4) |  |  | Histórico padrão da multa |
| conta_provisao_de_encargos | `ct_encargos_provisao` | integer(4) |  |  | Conta provisão de encargos |
| conta_despesa_de_encargos | `ct_encargos_despesa` | integer(4) |  |  | Conta despesa de encargos |
| historico_padrao_de_encargos | `ht_encargos` | integer(4) |  |  | Histórico padrão de encargos |

**Filtros:** `imposto` (eq/in), `vigencia` (eq/in), `gerar_lancamentos_de_partida_simples_s_n` (eq/in)

## geimposto_vigencia_recolhimento_ctb

**Impostos - Cadastro - Codigo de Recolhimento - Contabilidade** — tabela `GEIMPOSTO_VIGENCIA_RECOLHIMENTO_CTB` (3.213 linhas)

Impostos - Cadastro - Codigo de Recolhimento - Contabilidade. 3.213 linhas no catálogo; chave: CODI_EMP, CODI_IMP, VIGENCIA_IMP, I_RECOLHIMENTO.

- **Chave:** `CODI_EMP, CODI_IMP, VIGENCIA_IMP, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA_IMP`
- **Ordem padrão:** `VIGENCIA_IMP desc`, `CODI_IMP asc`, `I_RECOLHIMENTO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3.213 linhas, 1.429 empresa(s), VIGENCIA_IMP de 1964-06-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_imp` | integer(4) |  |  | Codigo |
| vigencia | `vigencia_imp` | date(4) |  |  | Vigencia |
| sequencial | `i_recolhimento` | integer(4) |  |  | Sequencial |
| imposto_a_recolher_conta | `ct_recolher` | integer(4) |  |  | Imposto a recolher - Conta |
| imposto_a_recolher_historico | `ht_recolher` | integer(4) |  |  | Imposto a recolher - Histórico |
| imposto_a_recolher_imposto_venda | `ct_vendas` | integer(4) |  |  | Imposto a recolher - Imposto Venda |
| pagamento_valor_principal_conta_debito | `ct_principal_debito` | integer(4) |  |  | Pagamento - Valor Principal - Conta débito |
| pagamento_valor_principal_conta_credito | `ct_principal_credito` | integer(4) |  |  | Pagamento - Valor Principal - Conta crédito |
| pagamento_valor_principal_historico | `ht_principal` | integer(4) |  |  | Pagamento - Valor Principal - Histórico |
| pagamento_valor_juros_conta_debito | `ct_juros_debito` | integer(4) |  |  | Pagamento - Valor Juros - Conta débito |
| pagamento_valor_juros_conta_credito | `ct_juros_credito` | integer(4) |  |  | Pagamento - Valor Juros - Conta crédito |
| pagamento_valor_juros_historico | `ht_juros` | integer(4) |  |  | Pagamento - Valor Juros - Histórico |
| pagamento_valor_multa_conta_debito | `ct_multa_debito` | integer(4) |  |  | Pagamento - Valor Multa - Conta débito |
| pagamento_valor_multa_conta_credito | `ct_multa_credito` | integer(4) |  |  | Pagamento - Valor Multa - Conta crédito |
| pagamento_valor_multa_historico | `ht_multa` | integer(4) |  |  | Pagamento - Valor Multa - Histórico |
| gera_lancamento_contabeis_por_nota | `gera_lancamento_contabeis_por_nota` | char(1) |  |  | Gera Lançamento Contábeis por Nota |
| devolucoes_imposto_a_recuperar_conta | `ct_recuperar` | integer(4) |  |  | Devoluções - Imposto a recuperar - Conta |
| devolucoes_devolucoes_vendas_conta | `ct_devolucao_vendas` | integer(4) |  |  | Devoluções - Devoluções vendas - Conta |
| devolucoes_historico | `ht_devolucao_vendas` | integer(4) |  |  | Devoluções - Histórico |
| zeramento_historico | `ht_zeramento` | integer(4) |  |  | Zeramento - Histórico |
| imposto_a_recuperar_historico | `ht_recuperar` | integer(4) |  |  | Imposto a recuperar - Histórico |
| imposto_a_recuperar_imposto_compras | `ct_compras` | integer(4) |  |  | Imposto a recuperar - Imposto Compras |
| estorno_de_debitos_subtri_debito | `ct_debito_estorno_debitos_subtri` | integer(4) |  |  | Estorno de débitos - Subtri - Débito |
| estorno_de_debitos_subtri_credito | `ct_credito_estorno_debitos_subtri` | integer(4) |  |  | Estorno de débitos - Subtri - Crédito |
| estorno_de_debitos_subtri_historico | `ht_estorno_debitos_subtri` | integer(4) |  |  | Estorno de débitos - Subtri - Histórico |
| debito_estorno_creditos_subtri_conta | `ct_debito_estorno_creditos_subtri` | integer(4) |  |  | Debito estorno creditos SUBTRI - Conta |
| credito_estorno_creditos_subtri_conta | `ct_credito_estorno_creditos_subtri` | integer(4) |  |  | Credito estorno creditos SUBTRI - Conta |
| estorno_creditos_subtri_historico | `ht_estorno_creditos_subtri` | integer(4) |  |  | Estorno creditos SUBTRI - Historico |

**Filtros:** `codigo` (eq/in), `vigencia` (eq/in), `sequencial` (eq/in), `gera_lancamento_contabeis_por_nota` (eq/in)

## geimposto_vigencia_recolhimento_natureza_rendimento

**Natureza de rendimentos do recolhimento** — tabela `GEIMPOSTO_VIGENCIA_RECOLHIMENTO_NATUREZA_RENDIMENTO` (1.399 linhas)

Natureza de rendimentos do recolhimento. 1.399 linhas no catálogo; chave: CODI_EMP, CODI_IMP, VIGENCIA_IMP, I_RECOLHIMENTO, I_SEQUENCIAL_NATUREZA.

- **Chave:** `CODI_EMP, CODI_IMP, VIGENCIA_IMP, I_RECOLHIMENTO, I_SEQUENCIAL_NATUREZA`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA_IMP`
- **Ordem padrão:** `VIGENCIA_IMP desc`, `CODI_IMP asc`, `I_RECOLHIMENTO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.399 linhas, 200 empresa(s), VIGENCIA_IMP de 2003-10-01 a 2026-06-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_imp` | integer(4) |  |  | Codigo |
| vigencia | `vigencia_imp` | date(4) |  |  | Vigencia |
| sequencial | `i_recolhimento` | integer(4) |  |  | Sequencial |
| sequencial_natureza | `i_sequencial_natureza` | integer(4) |  |  | Sequencial Natureza |
| codigo_do_recolhimento | `codigo_recolhimento` | char(6) |  |  | Codigo do recolhimento |
| codigo_da_natureza_de_rendimento | `codi_nat_rendimento` | integer(4) |  |  | Código da Natureza de Rendimento |

**Filtros:** `codigo` (eq/in), `vigencia` (eq/in), `sequencial` (eq/in), `sequencial_natureza` (eq/in), `codigo_do_recolhimento` (eq/in), `codigo_da_natureza_de_rendimento` (eq/in)

## geimposto_vigencia_codrec_natureza_rendimento

**Tabela com as naturezas de rendimento dos impostos** — tabela `GEIMPOSTO_VIGENCIA_CODREC_NATUREZA_RENDIMENTO` (48 linhas)

Tabela com as naturezas de rendimento dos impostos. 48 linhas no catálogo; chave: CODI_EMP, CODI_IMP, VIGENCIA_IMP, CODI_REC, I_SEQUENCIAL_NATUREZA.

- **Chave:** `CODI_EMP, CODI_IMP, VIGENCIA_IMP, CODI_REC, I_SEQUENCIAL_NATUREZA`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA_IMP`
- **Ordem padrão:** `VIGENCIA_IMP desc`, `CODI_IMP asc`, `CODI_REC asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 48 linhas, 25 empresa(s), VIGENCIA_IMP de 2022-01-01 a 2026-05-01.
- Colunas expostas nulas em 100% das linhas (2): tipo_de_isencao_para_rendimentos_isentos, descricao_de_isencao_para_rendimentos_is.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| vigencia | `vigencia_imp` | date(4) |  |  | Vigencia |
| codigo_do_recolhimento | `codi_rec` | char(6) |  |  | Codigo do recolhimento |
| sequencial_do_recolhimento_x_natureza_de | `i_sequencial_natureza` | integer(4) |  |  | Sequencial do recolhimento x natureza de rendimento |
| codigo_da_natureza_de_rendimento | `codi_nat_rendimento` | integer(4) |  |  | Código da Natureza de Rendimento |
| tipo_de_isencao_para_rendimentos_isentos | `tipo_isencao` | integer(4) |  |  | Tipo de isenção para rendimentos isentos |
| descricao_de_isencao_para_rendimentos_is | `descricao_isencao` | varchar(100) |  |  | Descrição de isenção para rendimentos isentos |

**Filtros:** `imposto` (eq/in), `vigencia` (eq/in), `codigo_do_recolhimento` (eq/in), `sequencial_do_recolhimento_x_natureza_de` (eq/in), `codigo_da_natureza_de_rendimento` (eq/in), `tipo_de_isencao_para_rendimentos_isentos` (eq/in), `descricao_de_isencao_para_rendimentos_is` (contem/prefixo)

## geimposto_vigencia_sub_apuracao

**Impostos - Cadastro - AM - Crédito Estímulo** — tabela `GEIMPOSTO_VIGENCIA_SUB_APURACAO` (3 linhas)

Impostos - Cadastro - AM - Crédito Estímulo. 3 linhas no catálogo; chave: CODI_EMP, CODI_IMP, VIGENCIA_IMP, I_SUB_APURACAO.

- **Chave:** `CODI_EMP, CODI_IMP, VIGENCIA_IMP, I_SUB_APURACAO`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA_IMP`
- **Ordem padrão:** `VIGENCIA_IMP desc`, `CODI_IMP asc`, `I_SUB_APURACAO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3 linhas, 1 empresa(s), VIGENCIA_IMP de 2025-05-01 a 2026-01-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| vigencia | `vigencia_imp` | date(4) |  |  | Vigência |
| sequencial | `i_sub_apuracao` | integer(4) |  |  | Sequencial |
| descricao | `descricao` | varchar(30) |  |  | Descrição |
| codigo_recolhimento | `codigo_recolhimento` | char(6) |  |  | Código recolhimento |
| data_do_vencimento | `dia_vencimento` | integer(4) |  |  | Data do vencimento |
| conta_a_recolher | `ct_recolher` | integer(4) |  |  | Conta a recolher |
| historico_a_recolher | `ht_recolher` | integer(4) |  |  | Histórico a recolher |
| conta_a_recuperar | `ct_recuperar` | integer(4) |  |  | Conta a recuperar |
| historico_a_recuperar | `ht_recuperar` | integer(4) |  |  | Histórico a recuperar |
| conta_do_incentivo_fiscal | `ct_incentivo_fiscal` | integer(4) |  |  | Conta do incentivo fiscal |
| historico_do_incentivo_fiscal | `ht_incentivo_fiscal` | integer(4) |  |  | Histórico do incentivo fiscal |

**Filtros:** `imposto` (eq/in), `vigencia` (eq/in), `sequencial` (eq/in), `descricao` (contem/prefixo), `codigo_recolhimento` (eq/in)

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

