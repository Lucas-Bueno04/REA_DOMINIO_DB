# Modelo — ICMS - substituição tributária por UF e ajustes da apuração

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/icms.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

2 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [apuracao_icms_st_uf](#apuracao_icms_st_uf) | `efsdoimp_subtri_por_uf` | 706.131 | grande | empresa; um de: periodo, uf |
| [ajuste_apuracao](#ajuste_apuracao) | `efajustes` | 50.027 | medio | empresa |

## apuracao_icms_st_uf

**Apuração do ICMS-ST por UF** — tabela `efsdoimp_subtri_por_uf` (706.131 linhas)

Desdobra a apuração da substituição tributária por UF favorecida (27 UFs) em cada empresa, competência e recolhimento: débitos e créditos, estornos, deduções, saldo devedor ou credor, valor pago e vencimento. A tabela guarda uma linha para TODAS as UFs de cada apuração: de 706.590 linhas só 1.076 têm saldo. 633 empresas, de 2007-04 a 2026-09.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM` · exige um de: `periodo, uf`
- **Ordem padrão:** `DATA_SIM desc`, `SIGLA_UF asc`

**Regras de negócio validadas:**

- Identidade da apuração: saldo devedor − saldo credor = (imposto das saídas + outros débitos + estorno de créditos + acréscimos) − (imposto das entradas + outros créditos + estorno de débitos + saldo credor anterior + deduções) em 706.590 de 706.590 linhas (tolerância 0,02); as colunas calculadas `debitos`, `creditos` e `saldo_liquido` reproduzem isso. Os ressarcimentos (CFOP 1603/2603/5603/6603 e de ST) não alteram a identidade: a fórmula fecha com e sem eles nas 706.590 linhas, ou seja, somam zero.
- Esparsidade: das 706.590 linhas, só 1.022 têm saldo devedor e 54 têm saldo credor; as outras 705.514 são zero. Para ver o que importa filtre `saldo_devedor` maior que zero (ou o saldo credor).
- Cobre as 27 UFs, 633 empresas e competências de 2007-04 a 2026-09.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| imposto_codigo | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| periodicidade | `pdic_sim` | integer(4) |  | periodicidade_apuracao | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| uf | `sigla_uf` | char(2) |  |  | Sigla da UF |
| recolhimento_sequencial | `i_recolhimento` | integer(4) |  |  | Recolhimento |
| valor_contabil_entradas | `valor_contabil_entradas` | numeric(13) |  |  | Valor contábil entradas |
| base_calculo_entradas | `base_calculo_entradas` | numeric(13) |  |  | Base cálculo entradas |
| imposto_entradas | `valor_imposto_entradas` | numeric(13) |  |  | Valor imposto entradas |
| valor_contabil_saidas | `valor_contabil_saidas` | numeric(13) |  |  | Valor contábil saídas |
| base_calculo_saidas | `base_calculo_saidas` | numeric(13) |  |  | Base cálculo saídas |
| imposto_saidas | `valor_imposto_saidas` | numeric(13) |  |  | Valor imposto saídas |
| outros_debitos | `outros_debitos` | numeric(13) |  |  | Outros Débitos |
| estorno_creditos | `estorno_creditos` | numeric(13) |  |  | Estorno de Créditos |
| outros_creditos | `outros_creditos` | numeric(13) |  |  | Outros Créditos |
| estorno_debitos | `estorno_debitos` | numeric(13) |  |  | Estorno de Debitos |
| acrescimos | `acrescimos` | numeric(13) |  |  | Acréscimos |
| deducoes | `deducoes` | numeric(13) |  |  | Deduções |
| saldo_credor_anterior | `saldo_credor_anterior` | numeric(13) |  |  | Saldo Credor Anterior |
| saldo_diferido_anterior | `saldo_diferido_anterior` | numeric(13) |  |  | Saldo Diferido Anterior |
| saldo_diferido | `saldo_diferido` | numeric(13) |  |  | Saldo Diferido |
| ressarcimento_cfop_1603_2603 | `ressarcimento_cfop_1603_2603` | numeric(13) |  |  | Ressarcimento CFOP 1603 2603 |
| ressarcimento_cfop_5603_6603 | `ressarcimento_cfop_5603_6603` | numeric(13) |  |  | Ressarcimento CFOP 5603 6603 |
| icms_ressarcimento_st | `valor_icms_ressarcimento_st` | numeric(13) |  |  | Valor Icms ressarcimento ST |
| saldo_devedor | `saldo_devedor` | numeric(13) |  |  | Saldo devedor |
| saldo_credor | `saldo_credor` | numeric(13) |  |  | Saldo credor |
| saldo_devedor_complementacao | `saldo_devedor_complementacao` | numeric(13) |  |  | Saldo devedor Complementação |
| outros_recolhimentos | `outros_recolhimentos` | numeric(13) |  |  | Outros Recolhimentos |
| valor_pago | `valor_pago` | numeric(13) |  |  | Valor Pago |
| vencimento | `data_vencimento` | date(4) |  |  | Data de vencimento |
| estorno_fcp_interestadual | `estorno_fcp_interestadual` | numeric(13) |  |  | Estorno do Fundo de Comabte a Pobreza Interestadual |
| estorno_devolucoes_fcp_interestadual | `estorno_devolucoes_fcp_interestadual` | numeric(13) |  |  | Estorno devolucoes FCP interestadual |
| deducao_fcp_interestadual | `deducao_ref_fcp_interestadual` | numeric(13) |  |  | Dedução ref. ao Fundo de Combate a Pobreza Interestadual |
| saldo_liquido (calculada) | `SALDO_DEVEDOR - SALDO_CREDOR` | — | — | | Calculada pelo modelo: SALDO_DEVEDOR - SALDO_CREDOR |
| debitos (calculada) | `VALOR_IMPOSTO_SAIDAS + OUTROS_DEBITOS + ESTORNO_CREDITOS + ACRESCIMOS` | — | — | | Calculada pelo modelo: VALOR_IMPOSTO_SAIDAS + OUTROS_DEBITOS + ESTORNO_CREDITOS + ACRESCIMOS |
| creditos (calculada) | `VALOR_IMPOSTO_ENTRADAS + OUTROS_CREDITOS + ESTORNO_DEBITOS + SALDO_CREDOR_ANTERIOR + DEDUCOES` | — | — | | Calculada pelo modelo: VALOR_IMPOSTO_ENTRADAS + OUTROS_CREDITOS + ESTORNO_DEBITOS + SALDO_CREDOR_ANTERIOR + DEDUCOES |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `imposto` → `geimposto` por `CODI_EMP` = `codi_emp` e `CODI_IMP` = `codi_imp`; colunas: `imposto_nome`, `imposto_sigla`

**Filtros:** `competencia` (eq/entre/gte/lte), `uf` (eq/in), `imposto_codigo` (eq/in), `saldo_devedor` (gte/lte/entre)

## ajuste_apuracao

**Códigos de ajuste da apuração** — tabela `efajustes` (50.027 linhas)

Cadastro de códigos de ajuste da apuração por empresa (nome, imposto, tipo de operação e as contas e o histórico usados na contabilização). Cada empresa tem 35 códigos padrão (1.418 empresas), mais os que cria. 50.027 linhas.

- **Chave:** `codi_emp, codi_aju`
- **Empresa:** `codi_emp`
- **Período:** `—`
- **Ordem padrão:** `oper_aju asc`, `codi_aju asc`

**Regras de negócio validadas:**

- Por operação: 1 (outros créditos) 18.585 · 3 (outros débitos) 14.290 · 5 (outras deduções) 4.288 · 2 (estorno de débitos) 2.860 · 4 (estorno de créditos) 2.858 · 6 (outros acréscimos) 2.858 · 7 (outros recolhimentos) 2.858 · 43 (créditos do ativo permanente) 1.429 · 18 (1). 1.429 empresas têm os códigos padrão.
- Contas de débito e crédito estão preenchidas em 50.015 dos 50.027 ajustes.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| ajuste_codigo | `codi_aju` | integer(4) |  |  | Codigo |
| nome | `nome_aju` | char(30) |  |  | Nome |
| imposto_codigo | `codi_imp` | integer(4) |  |  | Imposto |
| operacao | `oper_aju` | integer(4) |  | operacao_ajuste | Operacao |
| conta_debito | `cdeb_aju` | integer(4) |  |  | Conta debito |
| conta_credito | `ccre_aju` | integer(4) |  |  | Conta credito |
| historico_padrao | `chis_aju` | integer(4) |  |  | Historico padrao |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `imposto` → `geimposto` por `codi_emp` = `codi_emp` e `codi_imp` = `codi_imp`; colunas: `imposto_nome`, `imposto_sigla`

**Filtros:** `ajuste_codigo` (eq/in), `nome` (contem/prefixo), `operacao` (eq/in), `imposto_codigo` (eq/in)

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

### periodicidade_apuracao

Periodicidade da apuração (pdic_sim)

Confirmado: sim

| Código | Significado |
|---|---|
| 1 | 1º decêndio |
| 2 | 2º decêndio |
| 3 | 3º decêndio |
| 4 | 1ª quinzena |
| 5 | 2ª quinzena |
| 6 | Mensal |
| 7 | Trimestral |
| 11 | 1ª semana |
| 12 | 2ª semana |
| 13 | 3ª semana |
| 14 | 4ª semana |
| 15 | 5ª semana |
| 51 | Complementar |
| 52 | 13º salário |

### operacao_ajuste

Tipo de ajuste da apuração (efajustes.oper_aju)

Confirmado: parcial

> O comentário diz só "Operacao". A legenda vem dos nomes padrão dos ajustes (idênticos em 1.429 empresas) e das colunas da apuração a que correspondem: 1 = outros créditos (créditos por importação, compensação, benefícios fiscais, ajustes CAE 806, crédito de ICMS), 2 = estorno de débitos, 3 = outros débitos (por importação, compensação, de responsabilidade, ajustes CAE 803), 4 = estorno de créditos, 5 = outras deduções (de ICMS, IPI e ISS), 6 = outros acréscimos (ICMS e IPI), 7 = outros recolhimentos, 43 = créditos do ativo permanente e 18 = pagamento antecipado do mês anterior (1 registro). Por evidência dos nomes, não documentada pelo banco.

| Código | Significado |
|---|---|
| 1 | Outros créditos |
| 2 | Estorno de débitos |
| 3 | Outros débitos |
| 4 | Estorno de créditos |
| 5 | Outras deduções |
| 6 | Outros acréscimos |
| 7 | Outros recolhimentos |
| 18 | Pagamento antecipado do mês anterior |
| 43 | Créditos do ativo permanente |

