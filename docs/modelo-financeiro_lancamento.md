# Modelo — Financeiro do escritório - lancamento (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/financeiro_lancamento.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

6 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [hrlancamento_pagar_parcela](#hrlancamento_pagar_parcela) | `HRLANCAMENTO_PAGAR_PARCELA` | 8.259 | pequeno | empresa |
| [hrlancamento_pagar](#hrlancamento_pagar) | `HRLANCAMENTO_PAGAR` | 6.681 | pequeno | empresa |
| [hrlancamento_receber](#hrlancamento_receber) | `HRLANCAMENTO_RECEBER` | 6.371 | pequeno | empresa |
| [hrlancamento_pagar_lancto](#hrlancamento_pagar_lancto) | `HRLANCAMENTO_PAGAR_LANCTO` | 3.550 | pequeno | empresa |
| [hrlancamento_desconto](#hrlancamento_desconto) | `HRLANCAMENTO_DESCONTO` | 291 | pequeno | empresa |
| [hrlancamento_receber_competencia](#hrlancamento_receber_competencia) | `HRLANCAMENTO_RECEBER_COMPETENCIA` | 42 | pequeno | empresa |

## hrlancamento_pagar_parcela

**Lancamentos de contas a pagar - Parcelas** — tabela `HRLANCAMENTO_PAGAR_PARCELA` (8.259 linhas)

Lancamentos de contas a pagar - Parcelas. 8.259 linhas no catálogo; chave: CODI_EMP, I_PAGAR, I_PARCELA.

- **Chave:** `CODI_EMP, I_PAGAR, I_PARCELA`
- **Empresa:** `CODI_EMP`
- **Período:** `VENCIMENTO`
- **Ordem padrão:** `VENCIMENTO desc`, `I_PAGAR asc`, `I_PARCELA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 8.259 linhas, 2 empresa(s), VENCIMENTO de 2018-01-03 a 2026-01-20.
- Vínculo hrconta_financeira (HRCONTA_FINANCEIRA): 2 de 8.204 linhas sem registro relacionado (empresa 1).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| escritorio | `codi_emp` | integer(4) |  |  | Escritorio |
| lancamento_a_pagar | `i_pagar` | integer(4) |  |  | Lancamento a pagar |
| codigo | `i_parcela` | integer(4) |  |  | Codigo |
| data_de_vencimento | `vencimento` | date(4) |  |  | Data de vencimento |
| valor_da_parcela | `valor` | numeric(13) |  |  | Valor da parcela |
| possivel_conta_para_pagamento | `i_conta_financeira` | integer(4) |  |  | Possivel conta para pagamento |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| valor_irrf_aproveitado | `valor_irrf` | numeric(13) |  |  | Valor IRRF aproveitado |
| valor_de_iss_retido | `valor_iss_retido` | numeric(13) |  |  | Valor de ISS Retido |
| valor_de_inss_retido | `valor_inss_retido` | numeric(13) |  |  | Valor de INSS Retido |
| valor_de_crf_aproveitado | `valor_crf` | numeric(13) |  |  | Valor de CRF aproveitado |
| valor_original_sem_retencoes | `valor_original` | numeric(13) |  |  | Valor original sem retenções |
| documento_da_parcela | `documento` | integer(4) |  |  | Documento da Parcela |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `hrconta_financeira` → `HRCONTA_FINANCEIRA` por `codi_emp` = `codi_emp` e `i_conta_financeira` = `i_conta_financeira`; colunas: `hrconta_financeira_nome`

**Filtros:** `lancamento_a_pagar` (eq/in), `codigo` (eq/in), `data_de_vencimento` (entre/gte/lte), `possivel_conta_para_pagamento` (eq/in)

## hrlancamento_pagar

**Lancamentos de contas a pagar** — tabela `HRLANCAMENTO_PAGAR` (6.681 linhas)

Lancamentos de contas a pagar. 6.681 linhas no catálogo; chave: CODI_EMP, I_PAGAR.

- **Chave:** `CODI_EMP, I_PAGAR`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_PAGAMENTO`
- **Ordem padrão:** `DATA_PAGAMENTO desc`, `I_PAGAR asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 6.681 linhas, 2 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): data_de_pagamento.
- Vínculo effornece (effornece): 0 de 6.626 linhas sem registro relacionado (empresa 1).
- Vínculo hrcategoria_pagar (HRCATEGORIA_PAGAR): 0 de 6.626 linhas sem registro relacionado (empresa 1).
- Vínculo hrconta_financeira (HRCONTA_FINANCEIRA): 2 de 6.626 linhas sem registro relacionado (empresa 1).
- Vínculo hrhistorico (HRHISTORICO): 6.625 de 6.626 linhas sem registro relacionado (empresa 1).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| escritorio | `codi_emp` | integer(4) |  |  | Escritorio |
| codigo | `i_pagar` | integer(4) |  |  | Codigo |
| tipo_do_lancamento_v_a_vista_p_a_prazo | `tipo` | char(1) |  |  | Tipo do lancamento V A vista P A prazo |
| categoria | `i_categoria_pagar` | integer(4) |  |  | Categoria |
| fornecedor | `i_fornecedor` | integer(4) |  |  | Fornecedor |
| conta_financeira_ou_possivel_conta_para | `i_conta_financeira` | integer(4) |  |  | Conta financeira ou possivel conta para pagamento |
| documento | `documento` | integer(4) |  |  | Documento |
| serie | `serie` | varchar(7) |  |  | Serie |
| data_de_emissao | `emissao` | date(4) |  |  | Data de emissao |
| lancar_p_valor_da_parcela_t_valor_total | `lancar` | char(1) |  |  | Lancar P Valor da parcela T Valor total |
| valor_total | `valor` | numeric(13) |  |  | Valor total |
| valor_de_desconto | `valor_desconto` | numeric(13) |  |  | Valor de desconto |
| valor_sem_original_sem_desconto | `valor_original` | numeric(13) |  |  | Valor sem original sem desconto |
| data_de_pagamento | `data_pagamento` | date(4) |  |  | Data de pagamento |
| codigo_do_historico | `i_historico` | integer(4) |  |  | Codigo do historico |
| historico | `historico` | varchar(512) |  |  | Historico |
| quantidade_de_parcelas | `quantidade` | integer(4) |  |  | Quantidade de parcelas |
| data_de_vencimento_inicial | `vencimento_inicial` | date(4) |  |  | Data de vencimento inicial |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| valor_irrf | `valor_irrf` | numeric(13) |  |  | Valor IRRF |
| valor_de_iss_retido | `valor_iss_retido` | numeric(13) |  |  | Valor de ISS Retido |
| valor_de_inss_retido | `valor_inss_retido` | numeric(13) |  |  | Valor de INSS Retido |
| valor_de_crf | `valor_crf` | numeric(13) |  |  | Valor de CRF |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `effornece` → `effornece` por `codi_emp` = `codi_emp` e `i_fornecedor` = `codi_for`; colunas: `effornece_nome`
- `hrcategoria_pagar` → `HRCATEGORIA_PAGAR` por `codi_emp` = `codi_emp` e `i_categoria_pagar` = `i_categoria_pagar`; colunas: `hrcategoria_pagar_nome`
- `hrconta_financeira` → `HRCONTA_FINANCEIRA` por `codi_emp` = `codi_emp` e `i_conta_financeira` = `i_conta_financeira`; colunas: `hrconta_financeira_nome`
- `hrhistorico` → `HRHISTORICO` por `codi_emp` = `codi_emp` e `i_historico` = `i_historico`; colunas: `hrhistorico_nome`

**Filtros:** `codigo` (eq/in), `data_de_emissao` (entre/gte/lte), `data_de_pagamento` (entre/gte/lte), `data_de_vencimento_inicial` (entre/gte/lte), `tipo_do_lancamento_v_a_vista_p_a_prazo` (eq/in), `categoria` (eq/in), `fornecedor` (eq/in), `conta_financeira_ou_possivel_conta_para` (eq/in), `serie` (eq/in), `lancar_p_valor_da_parcela_t_valor_total` (eq/in), `codigo_do_historico` (eq/in), `historico` (contem/prefixo)

## hrlancamento_receber

**Lancamentos de contas a receber - Mensais e Fixos** — tabela `HRLANCAMENTO_RECEBER` (6.371 linhas)

Lancamentos de contas a receber - Mensais e Fixos. 6.371 linhas no catálogo; chave: CODI_EMP, I_CLIENTE, I_RECEBER.

- **Chave:** `CODI_EMP, I_CLIENTE, I_RECEBER`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_LANCAMENTO`
- **Ordem padrão:** `DATA_LANCAMENTO desc`, `I_CLIENTE asc`, `I_RECEBER asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 6.371 linhas, 2 empresa(s), DATA_LANCAMENTO de 2015-04-30 a 2210-11-25.
- Colunas expostas nulas em 100% das linhas (3): conta_corrente_escritorio, conta_corrente_cliente, conta_corrente_cliente_sequencial.
- Vínculo hrcliente (HRCLIENTE): 0 de 4.408 linhas sem registro relacionado (empresa 1).
- Vínculo hrcontrato (HRCONTRATO): 4.266 de 4.408 linhas sem registro relacionado (empresa 1).
- Vínculo hrevento (HREVENTO): 0 de 4.408 linhas sem registro relacionado (empresa 1).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| escritorio | `codi_emp` | integer(4) |  |  | Escritorio |
| cliente | `i_cliente` | integer(4) |  |  | Cliente |
| codigo | `i_receber` | integer(4) |  |  | Codigo |
| competencia_para_lancamento_mensal_ou_in | `competencia` | date(4) |  |  | Competencia para lancamento mensal ou Inicia em para lancamento fixo |
| conta_corrente_escritorio | `i_movimento_escritorio` | integer(4) |  |  | Conta corrente escritorio |
| conta_corrente_cliente | `i_movimento_cliente` | integer(4) |  |  | Conta corrente cliente |
| conta_corrente_cliente_sequencial | `i_movimento_cliente_seq` | integer(4) |  |  | Conta corrente cliente sequencial |
| competencia_do_primeiro_faturamento_do_l | `primeiro_faturamento` | date(4) |  |  | Competencia do primeiro faturamento do lancamento |
| lancamento_fixo_s_n | `fixo` | char(1) |  |  | Lancamento fixo S N |
| evento | `i_evento` | integer(4) |  |  | Evento |
| data_do_lancamento | `data_lancamento` | date(4) |  |  | Data do lancamento |
| fatura_com_o_contrato_s_n | `fatura_contrato` | char(1) |  |  | Fatura com o contrato S N |
| contrato | `i_contrato` | integer(4) |  |  | Contrato |
| data_de_vencimento_para_o_lancamento_men | `data_vencimento` | date(4) |  |  | Data de vencimento para o lancamento mensal |
| dia_de_vencimento_para_o_lancamento_fixo | `dia_vencimento` | tinyint(1) |  |  | Dia de vencimento para o lancamento fixo |
| mes_de_vecimento_para_o_lancamento_fixo | `mes_vencimento` | char(1) |  |  | Mes de vecimento para o lancamento fixo N No mes de faturamento A Apos o mes de faturamento S No segundo mes de faturmento |
| meses_para_faturamento_para_o_lancamento | `mes_faturamento` | char(1) |  |  | Meses para faturamento para o lancamento fixo T Todos os meses S Selecionar meses |
| meses_selecionados_para_o_lancamento_fix | `mes_selecionado` | varchar(40) |  |  | Meses selecionados para o lancamento fixo |
| definir_encerramento_do_lancamento_fixo | `encerrar` | char(1) |  |  | Definir encerramento do lancamento fixo S N |
| data_de_encerramento_do_lancamento_fixo | `data_encerramento` | date(4) |  |  | Data de encerramento do lancamento fixo |
| quantidade | `quantidade` | integer(4) |  |  | Quantidade |
| valor | `valor` | numeric(13) |  |  | Valor |
| pago_pelo_escritorio_s_n | `pago_escritorio` | char(1) |  |  | Pago pelo escritorio S N |
| complemento | `complemento` | varchar(512) |  |  | Complemento |
| origem_do_lancamento_l_lancamento_c_cont | `origem` | char(1) |  |  | Origem do lancamento L Lancamento C Contrato |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| modulo_que_originou_o_lancamento_hr_hono | `modulo_origem` | char(2) |  |  | Modulo que originou o lancamento (HR=Honorarios, EF=Escrita Fiscal, FO=Folha) |
| considerar_adicionar_anual | `considerar_adicional_anual` | char(1) |  |  | Considerar adicionar anual |
| observacao_do_lancamento | `observacao` | varchar(1000) |  |  | OBSERVACAO DO LANCAMENTO |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `hrcliente` → `HRCLIENTE` por `codi_emp` = `codi_emp` e `i_cliente` = `i_cliente`; colunas: `hrcliente_nome`
- `hrcontrato` → `HRCONTRATO` por `codi_emp` = `codi_emp` e `i_contrato` = `i_contrato`; colunas: `hrcontrato_nome`
- `hrevento` → `HREVENTO` por `codi_emp` = `codi_emp` e `i_evento` = `i_evento`; colunas: `hrevento_nome`

**Filtros:** `cliente` (eq/in), `codigo` (eq/in), `competencia_para_lancamento_mensal_ou_in` (entre/gte/lte), `competencia_do_primeiro_faturamento_do_l` (entre/gte/lte), `data_do_lancamento` (entre/gte/lte), `data_de_vencimento_para_o_lancamento_men` (entre/gte/lte), `data_de_encerramento_do_lancamento_fixo` (entre/gte/lte), `conta_corrente_escritorio` (eq/in), `conta_corrente_cliente` (eq/in), `conta_corrente_cliente_sequencial` (eq/in), `lancamento_fixo_s_n` (eq/in), `evento` (eq/in), `fatura_com_o_contrato_s_n` (eq/in), `contrato` (eq/in)

## hrlancamento_pagar_lancto

**Lancamentos de contas a pagar X Lancamentos Contabeis** — tabela `HRLANCAMENTO_PAGAR_LANCTO` (3.550 linhas)

Lancamentos de contas a pagar X Lancamentos Contabeis. 3.550 linhas no catálogo; chave: CODI_EMP, I_PAGAR, EMPRESA_LAN, NUME_LAN.

- **Chave:** `CODI_EMP, I_PAGAR, EMPRESA_LAN, NUME_LAN`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_PAGAR asc`, `EMPRESA_LAN asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3.550 linhas, 2 empresa(s).
- Vínculo geempre (geempre): 0 de 3.525 linhas sem registro relacionado (empresa 1).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| escritorio | `codi_emp` | integer(4) |  |  | Escritorio |
| lancamento_a_pagar | `i_pagar` | integer(4) |  |  | Lancamento a pagar |
| empresa_do_lancamento_contabil | `empresa_lan` | integer(4) |  |  | Empresa do lancamento contabil |
| numero_do_lancamento_contabil | `nume_lan` | integer(4) |  |  | Numero do lancamento contabil |
| empresa_que_originou_o_lancamento_contab | `fili_lan` | integer(4) |  |  | Empresa que originou o lancamento contabil |
| codigo_do_lote | `codi_lote` | integer(4) |  |  | Codigo do lote |
| tipo_do_lancamento_contabil_s_sistema_u | `tipo_lancamento` | char(1) |  |  | Tipo do lancamento contabil S Sistema U Usuario |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `fili_lan` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `lancamento_a_pagar` (eq/in), `empresa_do_lancamento_contabil` (eq/in), `numero_do_lancamento_contabil` (eq/in), `codigo_do_lote` (eq/in), `tipo_do_lancamento_contabil_s_sistema_u` (eq/in)

## hrlancamento_desconto

**Lancamentos de descontos** — tabela `HRLANCAMENTO_DESCONTO` (291 linhas)

Lancamentos de descontos. 291 linhas no catálogo; chave: CODI_EMP, I_CLIENTE, I_DESCONTO.

- **Chave:** `CODI_EMP, I_CLIENTE, I_DESCONTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_ENCERRAMENTO`
- **Ordem padrão:** `DATA_ENCERRAMENTO desc`, `I_CLIENTE asc`, `I_DESCONTO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 291 linhas, 1 empresa(s), DATA_ENCERRAMENTO de 2017-11-01 a 2026-02-01.
- origem_do_desconto_c_competencia_p_perio: todos os valores reais estão no comentário do banco (C=200, P=91).
- Vínculo hrcontrato (HRCONTRATO): 6 de 291 linhas sem registro relacionado (empresa 1).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| escritorio | `codi_emp` | integer(4) |  |  | Escritorio |
| cliente | `i_cliente` | integer(4) |  |  | Cliente |
| codigo | `i_desconto` | integer(4) |  |  | Codigo |
| competencia | `competencia` | date(4) |  |  | Competencia |
| lancamento_receber | `i_receber` | integer(4) |  |  | Lancamento receber |
| contrato | `i_contrato` | integer(4) |  |  | Contrato |
| o_desconto_e_para_o_adicional_anual_s_n | `adicional_anual` | char(1) |  |  | O desconto e para o adicional anual S N |
| tipo_de_lancamento_v_valor_p_percentual | `tipo_lancamento` | char(1) |  |  | Tipo de lancamento V Valor P Percentual |
| valor_ou_percentual | `valor_percentual` | numeric(13) |  |  | Valor ou percentual |
| historico | `historico` | varchar(100) |  |  | Historico |
| definir_encerramento_do_desconto_s_n | `encerrar` | char(1) |  |  | Definir encerramento do desconto (S/N) |
| data_de_encerramento_do_desconto | `data_encerramento` | date(4) |  |  | Data de encerramento do desconto |
| origem_do_desconto_c_competencia_p_perio | `origem` | char(1) |  | hrlancamento_desconto_origem_do_desconto_c_comp | Origem do desconto (C=Competência/ P=Período) |
| data_de_lancamento | `data_lancamento` | date(4) |  |  | Data de lançamento |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `hrcontrato` → `HRCONTRATO` por `codi_emp` = `codi_emp` e `i_contrato` = `i_contrato`; colunas: `hrcontrato_nome`

**Filtros:** `cliente` (eq/in), `codigo` (eq/in), `competencia` (entre/gte/lte), `data_de_encerramento_do_desconto` (entre/gte/lte), `data_de_lancamento` (entre/gte/lte), `lancamento_receber` (eq/in), `contrato` (eq/in), `o_desconto_e_para_o_adicional_anual_s_n` (eq/in), `tipo_de_lancamento_v_valor_p_percentual` (eq/in), `historico` (contem/prefixo), `definir_encerramento_do_desconto_s_n` (eq/in), `origem_do_desconto_c_competencia_p_perio` (eq/in)

## hrlancamento_receber_competencia

**Lancamentos de contas a receber - Mensais e Fixos - Competencias para faturamento futuro** — tabela `HRLANCAMENTO_RECEBER_COMPETENCIA` (42 linhas)

Lancamentos de contas a receber - Mensais e Fixos - Competencias para faturamento futuro. 42 linhas no catálogo; chave: CODI_EMP, I_CLIENTE, I_RECEBER, MES.

- **Chave:** `CODI_EMP, I_CLIENTE, I_RECEBER, MES`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CLIENTE asc`, `I_RECEBER asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 42 linhas, 2 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| escritorio | `codi_emp` | integer(4) |  |  | Escritorio |
| cliente | `i_cliente` | integer(4) |  |  | Cliente |
| lancamento_receber | `i_receber` | integer(4) |  |  | Lancamento receber |
| mes_de_faturamento | `mes` | tinyint(1) |  |  | Mes de faturamento |

**Filtros:** `cliente` (eq/in), `lancamento_receber` (eq/in), `mes_de_faturamento` (eq/in)

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

### hrlancamento_desconto_origem_do_desconto_c_comp

Confirmado: sim

> Todos os valores observados em HRLANCAMENTO_DESCONTO.ORIGEM estão no comentário do banco (2026-10-18). Distribuição: C=200, P=91.

| Código | Significado |
|---|---|
| C | Competência |
| P | Período |

