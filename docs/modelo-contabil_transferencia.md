# Modelo — Contábil - transferencia (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/contabil_transferencia.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

4 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [pmtransferencia_conta_patrimonial](#pmtransferencia_conta_patrimonial) | `PMTRANSFERENCIA_CONTA_PATRIMONIAL` | 4.353 | pequeno | empresa |
| [pmtransferencia_centro_custo](#pmtransferencia_centro_custo) | `PMTRANSFERENCIA_CENTRO_CUSTO` | 4.353 | pequeno | empresa |
| [pmtransferencia_matriz_filial_lancto](#pmtransferencia_matriz_filial_lancto) | `PMTRANSFERENCIA_MATRIZ_FILIAL_LANCTO` | 28 | pequeno | empresa |
| [pmtransferencia_matriz_filial](#pmtransferencia_matriz_filial) | `PMTRANSFERENCIA_MATRIZ_FILIAL` | 8 | pequeno | empresa |

## pmtransferencia_conta_patrimonial

**Transferência de Contas Patrimoniais** — tabela `PMTRANSFERENCIA_CONTA_PATRIMONIAL` (4.353 linhas)

Transferência de Contas Patrimoniais. 4.353 linhas no catálogo; chave: CODI_EMP, I_TRANSFERENCIA.

- **Chave:** `CODI_EMP, I_TRANSFERENCIA`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_TRANSFERENCIA`
- **Ordem padrão:** `DATA_TRANSFERENCIA desc`, `I_TRANSFERENCIA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4.354 linhas, 261 empresa(s), DATA_TRANSFERENCIA de 2001-09-12 a 2026-09-23.
- Colunas expostas nulas em 100% das linhas (2): codigo_do_historico, codigo_da_transferencia_do_bem_principal.
- origem_da_transferencia_b_bem_t_transfer: todos os valores reais estão no comentário do banco (B=4.354).
- Vínculo pmbem (PMBEM): 0 de 4 linhas sem registro relacionado (empresa 1012).
- Vínculo pmconta_patrimonial (PMCONTA_PATRIMONIAL): 0 de 4 linhas sem registro relacionado (empresa 1012).
- Vínculo pmhistorico (PMHISTORICO): 4 de 4 linhas sem registro relacionado (empresa 1012).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `i_transferencia` | integer(4) |  |  | Código |
| bem | `i_bem` | numeric(16) |  |  | Bem |
| data_da_transferencia | `data_transferencia` | date(4) |  |  | Data da transferência |
| conta_patrimonial_destino | `i_conta_patrimonial` | integer(4) |  |  | Conta patrimonial destino |
| codigo_do_historico | `i_historico` | integer(4) |  |  | Código do histórico |
| historico | `historico` | varchar(512) |  |  | Histórico |
| origem_da_transferencia_b_bem_t_transfer | `origem_transferencia` | char(1) |  | pmtransferencia_conta_patrimonial_origem_da_tra | Origem da transferência (B=Bem/ T=Transferência) |
| depreciacao_fiscal_acumulada | `valor_depreciacao_fiscal_acumulada_bem` | numeric(13) |  |  | Depreciação fiscal acumulada |
| depreciacao_societaria_acumulada | `valor_depreciacao_societaria_acumulada_bem` | numeric(13) |  |  | Depreciação societária acumulada |
| quantidade_de_parcelas_para_calculo_de_d | `quantidade_parcelas_depreciacao_fiscal` | integer(4) |  |  | Quantidade de parcelas para cálculo de depreciação fiscal |
| codigo_da_transferencia_do_bem_principal | `i_transferencia_vinculo` | integer(4) |  |  | Código da transferência do bem Principal quando é realizada uma transferencia por vinculo. |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `pmbem` → `PMBEM` por `codi_emp` = `codi_emp` e `i_bem` = `i_bem`; colunas: `pmbem_nome`
- `pmconta_patrimonial` → `PMCONTA_PATRIMONIAL` por `codi_emp` = `codi_emp` e `i_conta_patrimonial` = `i_conta_patrimonial`; colunas: `pmconta_patrimonial_nome`
- `pmhistorico` → `PMHISTORICO` por `codi_emp` = `codi_emp` e `i_historico` = `i_historico`; colunas: `pmhistorico_nome`

**Filtros:** `codigo` (eq/in), `data_da_transferencia` (entre/gte/lte), `conta_patrimonial_destino` (eq/in), `codigo_do_historico` (eq/in), `historico` (contem/prefixo), `origem_da_transferencia_b_bem_t_transfer` (eq/in), `codigo_da_transferencia_do_bem_principal` (eq/in)

## pmtransferencia_centro_custo

**Transferência de Centros de Custos** — tabela `PMTRANSFERENCIA_CENTRO_CUSTO` (4.353 linhas)

Transferência de Centros de Custos. 4.353 linhas no catálogo; chave: CODI_EMP, I_TRANSFERENCIA.

- **Chave:** `CODI_EMP, I_TRANSFERENCIA`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_TRANSFERENCIA`
- **Ordem padrão:** `DATA_TRANSFERENCIA desc`, `I_TRANSFERENCIA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4.354 linhas, 261 empresa(s), DATA_TRANSFERENCIA de 2001-09-12 a 2026-09-23.
- Colunas expostas nulas em 100% das linhas (2): codigo_do_historico, codigo_da_transferencia_do_bem_principal.
- origem_da_transferencia_b_bem_t_transfer: todos os valores reais estão no comentário do banco (B=4.354).
- Vínculo ctccusto (ctccusto): 0 de 4 linhas sem registro relacionado (empresa 1012).
- Vínculo pmbem (PMBEM): 0 de 4 linhas sem registro relacionado (empresa 1012).
- Vínculo pmhistorico (PMHISTORICO): 4 de 4 linhas sem registro relacionado (empresa 1012).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `i_transferencia` | integer(4) |  |  | Código |
| bem | `i_bem` | numeric(16) |  |  | Bem |
| data_da_transferencia | `data_transferencia` | date(4) |  |  | Data da transferência |
| centro_de_custo | `i_centro_custo` | integer(4) |  |  | Centro de custo |
| codigo_do_historico | `i_historico` | integer(4) |  |  | Código do histórico |
| historico | `historico` | varchar(512) |  |  | Histórico |
| origem_da_transferencia_b_bem_t_transfer | `origem_transferencia` | char(1) |  | pmtransferencia_centro_custo_origem_da_trans | Origem da transferência (B=Bem/ T=Transferência) |
| depreciacao_fiscal_acumulada | `valor_depreciacao_fiscal_acumulada_bem` | numeric(13) |  |  | Depreciação fiscal acumulada |
| depreciacao_societaria_acumulada | `valor_depreciacao_societaria_acumulada_bem` | numeric(13) |  |  | Depreciação societária acumulada |
| codigo_da_transferencia_do_bem_principal | `i_transferencia_vinculo` | integer(4) |  |  | Código da transferência do bem Principal quando é realizada uma transferencia por vinculo. |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `ctccusto` → `ctccusto` por `codi_emp` = `codi_emp` e `i_centro_custo` = `codi_ccu`; colunas: `ctccusto_nome`
- `pmbem` → `PMBEM` por `codi_emp` = `codi_emp` e `i_bem` = `i_bem`; colunas: `pmbem_nome`
- `pmhistorico` → `PMHISTORICO` por `codi_emp` = `codi_emp` e `i_historico` = `i_historico`; colunas: `pmhistorico_nome`

**Filtros:** `codigo` (eq/in), `data_da_transferencia` (entre/gte/lte), `centro_de_custo` (eq/in), `codigo_do_historico` (eq/in), `historico` (contem/prefixo), `origem_da_transferencia_b_bem_t_transfer` (eq/in), `codigo_da_transferencia_do_bem_principal` (eq/in)

## pmtransferencia_matriz_filial_lancto

**Transferência de bens entre matriz/filiais - Lançamentos Contábeis** — tabela `PMTRANSFERENCIA_MATRIZ_FILIAL_LANCTO` (28 linhas)

Transferência de bens entre matriz/filiais - Lançamentos Contábeis. 28 linhas no catálogo; chave: CODI_EMP, I_TRANSFERENCIA, EMPRESA_LAN, NUME_LAN.

- **Chave:** `CODI_EMP, I_TRANSFERENCIA, EMPRESA_LAN, NUME_LAN`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_TRANSFERENCIA asc`, `EMPRESA_LAN asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 28 linhas, 2 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| transferencia_de_bens_entre_matriz_filia | `i_transferencia` | integer(4) |  |  | Transferência de bens entre matriz/filiais |
| empresa_do_lancamento_contabil | `empresa_lan` | integer(4) |  |  | Empresa do lançamento contábil |
| numero_do_lancamento_contabil | `nume_lan` | integer(4) |  |  | Número do lançamento contábil |
| empresa_que_originou_o_lancamento_contab | `fili_lan` | integer(4) |  |  | Empresa que originou o lançamento contábil |
| codigo_do_lote | `codi_lote` | integer(4) |  |  | Código do lote |

**Filtros:** `transferencia_de_bens_entre_matriz_filia` (eq/in), `empresa_do_lancamento_contabil` (eq/in), `numero_do_lancamento_contabil` (eq/in), `codigo_do_lote` (eq/in)

## pmtransferencia_matriz_filial

**Plano de contas SPED ECF Entidades Fechadas da Previdência Comp Referencial - Saldo anterior por Centro de Custo** — tabela `PMTRANSFERENCIA_MATRIZ_FILIAL` (8 linhas)

Plano de contas SPED ECF Entidades Fechadas da Previdência Comp Referencial - Saldo anterior por Centro de Custo. 8 linhas no catálogo; chave: CODI_EMP, I_TRANSFERENCIA.

- **Chave:** `CODI_EMP, I_TRANSFERENCIA`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_TRANSFERENCIA`
- **Ordem padrão:** `DATA_TRANSFERENCIA desc`, `I_TRANSFERENCIA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 8 linhas, 2 empresa(s), DATA_TRANSFERENCIA de 2025-01-14 a 2025-05-07.
- Colunas expostas nulas em 100% das linhas (11): codigo_historico, documento_fiscal_numero, documento_fiscal_serie, documento_fiscal_data_de_emissao, documento_fiscal_modelo, documento_fiscal_chave_nfe, documento_fiscal_cliente, documento_fiscal_emitente_t_terceiros_p, documento_fiscal_produto, documento_fiscal_sequencial_do_item, ultima_parcela_calculada_credito_icms.
- documento_fiscal_emitente_t_terceiros_p: coluna sem nenhum valor preenchido; o domínio do comentário do banco não pôde ser verificado.
- Vínculo pmbem (PMBEM): 0 de 6 linhas sem registro relacionado (empresa 1446).
- Vínculo ctccusto (ctccusto): 0 de 6 linhas sem registro relacionado (empresa 1446).
- Vínculo pmconta_patrimonial (PMCONTA_PATRIMONIAL): 0 de 6 linhas sem registro relacionado (empresa 1446).
- Vínculo pmhistorico (PMHISTORICO): 6 de 6 linhas sem registro relacionado (empresa 1446).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial_transferencia | `i_transferencia` | integer(4) |  |  | Sequencial transferência |
| bem | `i_bem` | numeric(16) |  |  | Bem |
| data_da_transferencia | `data_transferencia` | date(4) |  |  | Data da transferência |
| valor_da_depreciacao_fiscal_acumulada | `valor_depreciacao_fiscal_acumulada` | numeric(13) |  |  | Valor da depreciação fiscal acumulada |
| valor_da_depreciacao_societaria_acumulad | `valor_depreciacao_societaria_acumulada` | numeric(13) |  |  | Valor da depreciação societária acumulada |
| valor_do_saldo_do_bem_na_data_de_transfe | `valor_saldo_atual` | numeric(13) |  |  | Valor do saldo do bem na data de transferência |
| empresa_destino_transferencia | `codi_emp_destino` | integer(4) |  |  | Empresa destino transferência |
| conta_patrimonial_destino_transferencia | `i_conta_patrimonial_destino` | integer(4) |  |  | Conta patrimonial destino transferência |
| centro_de_custo_destino_transferencia | `i_centro_custo_destino` | integer(4) |  |  | Centro de custo destino transferência |
| bem_destino | `i_bem_destino` | numeric(16) |  |  | Bem destino |
| codigo_historico | `i_historico` | integer(4) |  |  | Código histórico |
| historico | `historico` | varchar(512) |  |  | Historico |
| nao_transferir_credito_remanescente_icms | `nao_transferir_credito_remanescente_icms` | char(1) |  |  | Não transferir crédito remanescente icms |
| nao_transferir_debito_remanescente_icms | `nao_transferir_debito_remanescente_icms` | char(1) |  |  | Não transferir débito remanescente icms importacao |
| documento_fiscal_numero | `fiscal_numero` | numeric(15) |  |  | Documento fiscal - Número |
| documento_fiscal_serie | `fiscal_serie` | char(7) |  |  | Documento fiscal - Série |
| documento_fiscal_data_de_emissao | `fiscal_data_emissao` | date(4) |  |  | Documento fiscal - Data de emissão |
| documento_fiscal_modelo | `fiscal_modelo` | integer(4) |  |  | Documento fiscal - Modelo |
| documento_fiscal_chave_nfe | `fiscal_chave_nfe` | char(44) |  |  | Documento fiscal - Chave NFe |
| documento_fiscal_cliente | `fiscal_codi_cli` | integer(4) |  |  | Documento fiscal - Cliente |
| documento_fiscal_emitente_t_terceiros_p | `fiscal_emitente` | char(1) |  | pmtransferencia_matriz_filial_documento_f | Documento fiscal - Emitente (T=Terceiros/P=Próprio) |
| documento_fiscal_produto | `fiscal_codi_pdi` | char(14) |  |  | Documento fiscal - Produto |
| documento_fiscal_sequencial_do_item | `fiscal_sequencial_item` | integer(4) |  |  | Documento fiscal - Sequencial do item |
| nao_transferir_debito_remanescente_icms_c | `nao_transferir_debito_remanescente_icms_dif_ali` | char(1) |  |  | Não transferir débito remanescente icms diferencial aliquota |
| ultima_parcela_calculada_credito_icms | `ultima_parcela_credito_icms` | integer(4) |  |  | Última parcela calculada credito ICMS |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `pmbem` → `PMBEM` por `codi_emp` = `codi_emp` e `i_bem` = `i_bem`; colunas: `pmbem_nome`
- `ctccusto` → `ctccusto` por `codi_emp_destino` = `codi_emp` e `i_centro_custo_destino` = `codi_ccu`; colunas: `ctccusto_nome`
- `pmconta_patrimonial` → `PMCONTA_PATRIMONIAL` por `codi_emp_destino` = `codi_emp` e `i_conta_patrimonial_destino` = `i_conta_patrimonial`; colunas: `pmconta_patrimonial_nome`
- `pmhistorico` → `PMHISTORICO` por `codi_emp` = `codi_emp` e `i_historico` = `i_historico`; colunas: `pmhistorico_nome`

**Filtros:** `sequencial_transferencia` (eq/in), `data_da_transferencia` (entre/gte/lte), `documento_fiscal_data_de_emissao` (entre/gte/lte), `empresa_destino_transferencia` (eq/in), `conta_patrimonial_destino_transferencia` (eq/in), `centro_de_custo_destino_transferencia` (eq/in), `codigo_historico` (eq/in), `historico` (contem/prefixo), `nao_transferir_credito_remanescente_icms` (eq/in), `nao_transferir_debito_remanescente_icms` (eq/in), `documento_fiscal_serie` (eq/in), `documento_fiscal_chave_nfe` (contem/prefixo), `documento_fiscal_cliente` (eq/in), `documento_fiscal_emitente_t_terceiros_p` (eq/in)

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

### pmtransferencia_conta_patrimonial_origem_da_tra

Confirmado: sim

> Todos os valores observados em PMTRANSFERENCIA_CONTA_PATRIMONIAL.ORIGEM_TRANSFERENCIA estão no comentário do banco (2026-10-18). Distribuição: B=4.354.

| Código | Significado |
|---|---|
| B | Bem |
| T | Transferência |

### pmtransferencia_centro_custo_origem_da_trans

Confirmado: sim

> Todos os valores observados em PMTRANSFERENCIA_CENTRO_CUSTO.ORIGEM_TRANSFERENCIA estão no comentário do banco (2026-10-18). Distribuição: B=4.354.

| Código | Significado |
|---|---|
| B | Bem |
| T | Transferência |

### pmtransferencia_matriz_filial_documento_f

Confirmado: parcial

> Coluna PMTRANSFERENCIA_MATRIZ_FILIAL.FISCAL_EMITENTE só tem valores nulos na data da medição (2026-10-18): sem evidência para confirmar o comentário do banco.

| Código | Significado |
|---|---|
| T | Terceiros |
| P | Próprio |

