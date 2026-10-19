# Modelo — Financeiro do escritório - faturamento (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/financeiro_faturamento.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

7 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [hrfaturamento_parcela_emissao](#hrfaturamento_parcela_emissao) | `HRFATURAMENTO_PARCELA_EMISSAO` | 38.631 | medio | empresa |
| [hrfaturamento_contrato](#hrfaturamento_contrato) | `HRFATURAMENTO_CONTRATO` | 35.038 | medio | empresa |
| [hrfaturamento_parcela_item_detalhamento](#hrfaturamento_parcela_item_detalhamento) | `HRFATURAMENTO_PARCELA_ITEM_DETALHAMENTO` | 27.868 | medio | empresa |
| [hrfaturamento_lancto](#hrfaturamento_lancto) | `HRFATURAMENTO_LANCTO` | 12.697 | medio | empresa |
| [hrfaturamento_evento](#hrfaturamento_evento) | `HRFATURAMENTO_EVENTO` | 6.008 | pequeno | empresa |
| [hrfaturamento_adicional](#hrfaturamento_adicional) | `HRFATURAMENTO_ADICIONAL` | 2.646 | pequeno | empresa |
| [hrfaturamento_evento_renegociacao](#hrfaturamento_evento_renegociacao) | `HRFATURAMENTO_EVENTO_RENEGOCIACAO` | 106 | pequeno | empresa |

## hrfaturamento_parcela_emissao

**Faturamento - Parcelas - Emissoes e exclusoes de boletos e documento de cobranca** — tabela `HRFATURAMENTO_PARCELA_EMISSAO` (38.631 linhas)

Faturamento - Parcelas - Emissoes e exclusoes de boletos e documento de cobranca. 38.631 linhas no catálogo; chave: CODI_EMP, I_FATURAMENTO, I_PARCELA, TIPO, DATA_HORA, ACAO.

- **Chave:** `CODI_EMP, I_FATURAMENTO, I_PARCELA, TIPO, DATA_HORA, ACAO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_FATURAMENTO asc`, `I_PARCELA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 38.631 linhas, 2 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| escritorio | `codi_emp` | integer(4) |  |  | Escritorio |
| faturamento | `i_faturamento` | integer(4) |  |  | Faturamento |
| parcela | `i_parcela` | integer(4) |  |  | Parcela |
| tipo_do_relatorio_b_boleto_d_documento_d | `tipo` | char(1) |  |  | Tipo do relatorio B Boleto D Documento de cobranca |
| data_e_hora_da_emissao_ou_da_exclusao | `data_hora` | timestamp(8) |  |  | Data e hora da emissao ou da exclusao |
| acao_e_emissao_x_exclusao | `acao` | char(1) |  |  | Acao E Emissao X Exclusao |
| usuario_que_emitiu_ou_excluiu | `usuario` | varchar(128) |  |  | Usuario que emitiu ou excluiu |

**Filtros:** `faturamento` (eq/in), `parcela` (eq/in), `tipo_do_relatorio_b_boleto_d_documento_d` (eq/in), `data_e_hora_da_emissao_ou_da_exclusao` (eq/in), `acao_e_emissao_x_exclusao` (eq/in), `usuario_que_emitiu_ou_excluiu` (contem/prefixo)

## hrfaturamento_contrato

**Faturamento - Contratos** — tabela `HRFATURAMENTO_CONTRATO` (35.038 linhas)

Faturamento - Contratos. 35.038 linhas no catálogo; chave: CODI_EMP, I_FATURAMENTO.

- **Chave:** `CODI_EMP, I_FATURAMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_FATURAMENTO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 35.038 linhas, 2 empresa(s).
- Vínculo hrcontrato (HRCONTRATO): 0 de 34.985 linhas sem registro relacionado (empresa 1).
- Vínculo hrevento (HREVENTO): 0 de 34.985 linhas sem registro relacionado (empresa 1).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| escritorio | `codi_emp` | integer(4) |  |  | Escritorio |
| faturamento | `i_faturamento` | integer(4) |  |  | Faturamento |
| contrato | `i_contrato` | integer(4) |  |  | Contrato |
| evento_do_contrato | `i_evento` | integer(4) |  |  | Evento do contrato |
| valor | `valor` | numeric(13) |  |  | Valor |
| valor_de_desconto | `valor_desconto` | numeric(13) |  |  | Valor de desconto |
| valor_de_desconto_concedido_por_adimplen | `valor_desconto_adimplente` | numeric(13) |  |  | Valor de desconto concedido por adimplente |
| valor_original | `valor_original` | numeric(13) |  |  | Valor original |
| limite_de_numero_de_lancamentos_contabei | `contabil_limite` | integer(4) |  |  | Limite de numero de lancamentos contabeis |
| numero_de_lancamentos_contabeis_faturado | `contabil_faturado` | integer(4) |  |  | Numero de lancamentos contabeis faturados |
| limite_de_numero_de_notas_ficais | `fiscal_limite` | integer(4) |  |  | Limite de numero de notas ficais |
| numero_de_notas_ficais_faturados | `fiscal_faturado` | integer(4) |  |  | Numero de notas ficais faturados |
| limite_de_numero_de_horas_trabalhadas | `hora_limite` | integer(4) |  |  | Limite de numero de horas trabalhadas |
| numero_de_horas_trabalhadas_faturadas | `hora_faturado` | integer(4) |  |  | Numero de horas trabalhadas faturadas |
| limite_de_numero_de_horas_trabalhadas_na | `hora_contabilidade_limite` | integer(4) |  |  | Limite de numero de horas trabalhadas na contabilidade |
| numero_de_horas_trabalhadas_na_contabili | `hora_contabilidade_faturado` | integer(4) |  |  | Numero de horas trabalhadas na contabilidade faturadas |
| hora_folha_limite | `hora_folha_limite` | integer(4) |  |  | Limite de numero de horas trabalhadas na folha |
| numero_de_horas_trabalhadas_na_folha_fat | `hora_folha_faturado` | integer(4) |  |  | Numero de horas trabalhadas na folha faturadas |
| hora_escrita_limite | `hora_escrita_limite` | integer(4) |  |  | Limite de numero de horas trabalhadas na escrita |
| numero_de_horas_trabalhadas_na_escrita_f | `hora_escrita_faturado` | integer(4) |  |  | Numero de horas trabalhadas na escrita faturadas |
| limite_de_numero_de_horas_trabalhadas_no | `hora_patrimonio_limite` | integer(4) |  |  | Limite de numero de horas trabalhadas no patrimonio |
| numero_de_horas_trabalhadas_no_patrimoni | `hora_patrimonio_faturado` | integer(4) |  |  | Numero de horas trabalhadas no patrimonio faturadas |
| hora_lalur_limite | `hora_lalur_limite` | integer(4) |  |  | Limite de numero de horas trabalhadas no lalur |
| numero_de_horas_trabalhadas_no_lalur_fat | `hora_lalur_faturado` | integer(4) |  |  | Numero de horas trabalhadas no lalur faturadas |
| hora_atualizar_limite | `hora_atualizar_limite` | integer(4) |  |  | Limite de numero de horas trabalhadas no atualizar |
| numero_de_horas_trabalhadas_no_atualizar | `hora_atualizar_faturado` | integer(4) |  |  | Numero de horas trabalhadas no atualizar faturadas |
| hora_registro_limite | `hora_registro_limite` | integer(4) |  |  | Limite de numero de horas trabalhadas no registro |
| numero_de_horas_trabalhadas_no_registro | `hora_registro_faturado` | integer(4) |  |  | Numero de horas trabalhadas no registro faturadas |
| limite_de_numero_de_empregados | `funcionario_limite` | integer(4) |  |  | Limite de numero de empregados |
| numero_de_empregados_faturados | `funcionario_faturado` | integer(4) |  |  | Numero de empregados faturados |
| limite_do_valor_do_faturamento | `faturamento_limite` | numeric(13) |  |  | Limite do valor do faturamento |
| valor_do_faturamento_fatudado | `faturamento_faturado` | numeric(13) |  |  | Valor do faturamento fatudado |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `hrcontrato` → `HRCONTRATO` por `codi_emp` = `codi_emp` e `i_contrato` = `i_contrato`; colunas: `hrcontrato_nome`
- `hrevento` → `HREVENTO` por `codi_emp` = `codi_emp` e `i_evento` = `i_evento`; colunas: `hrevento_nome`

**Filtros:** `faturamento` (eq/in), `contrato` (eq/in), `evento_do_contrato` (eq/in)

## hrfaturamento_parcela_item_detalhamento

**Faturamento - Parcelas - Itens - Detalhamento** — tabela `HRFATURAMENTO_PARCELA_ITEM_DETALHAMENTO` (27.868 linhas)

Faturamento - Parcelas - Itens - Detalhamento. 27.868 linhas no catálogo; chave: CODI_EMP, I_FATURAMENTO, I_PARCELA, I_EVENTO, SEQUENCIAL, PAGO_ESCRITORIO.

- **Chave:** `CODI_EMP, I_FATURAMENTO, I_PARCELA, I_EVENTO, SEQUENCIAL, PAGO_ESCRITORIO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_FATURAMENTO asc`, `I_PARCELA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 27.868 linhas, 2 empresa(s).
- Colunas expostas nulas em 100% das linhas (2): aliquota_efetiva_ibs, aliquota_efetiva_cbs.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| escritorio | `codi_emp` | integer(4) |  |  | Escritorio |
| faturamento | `i_faturamento` | integer(4) |  |  | Faturamento |
| parcela | `i_parcela` | integer(4) |  |  | Parcela |
| evento | `i_evento` | integer(4) |  |  | Evento |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| pago_pelo_escritorio_s_n | `pago_escritorio` | char(1) |  |  | Pago pelo escritorio S N |
| complemento | `complemento` | varchar(500) |  |  | Complemento |
| valor | `valor` | numeric(13) |  |  | Valor |
| valor_de_desconto | `valor_desconto` | numeric(13) |  |  | Valor de desconto |
| valor_de_desconto_concedido_por_adimplen | `valor_desconto_adimplente` | numeric(13) |  |  | Valor de desconto concedido por adimplente |
| valor_original | `valor_original` | numeric(13) |  |  | Valor original |
| valor_irrf_aproveitado | `valor_irrf` | numeric(13) |  |  | Valor IRRF aproveitado |
| valor_irrf_calculado | `valor_irrf_calculado` | numeric(13) |  |  | Valor IRRF calculado |
| aliquota_de_irrf | `aliquota_irrf` | numeric(5) |  |  | Aliquota de IRRF |
| valor_de_iss | `valor_iss` | numeric(13) |  |  | Valor de ISS |
| aliquota_de_iss | `aliquota_iss` | numeric(5) |  |  | Aliquota de ISS |
| valor_de_iss_retido | `valor_iss_retido` | numeric(13) |  |  | Valor de ISS Retido |
| valor_de_iss_retido_calculado | `valor_iss_retido_calculado` | numeric(13) |  |  | Valor de ISS Retido calculado |
| aliquota_iss_ret | `aliquota_iss_ret` | numeric(5) |  |  | Aliquota de ISS |
| valor_de_inss_retido | `valor_inss_retido` | numeric(13) |  |  | Valor de INSS Retido |
| valor_de_inss_retido_calculado | `valor_inss_retido_calculado` | numeric(13) |  |  | Valor de INSS Retido calculado |
| aliquota_de_inss | `aliquota_inss_ret` | numeric(5) |  |  | Aliquota de INSS |
| valor_de_crf_aproveitado | `valor_crf` | numeric(13) |  |  | Valor de CRF aproveitado |
| valor_de_crf_calculado | `valor_crf_calculado` | numeric(13) |  |  | Valor de CRF calculado |
| valor_de_crf_pis_calculado | `valor_crf_pis_calculado` | numeric(13) |  |  | Valor de CRF PIS calculado |
| valor_de_crf_cofins_calculado | `valor_crf_cofins_calculado` | numeric(13) |  |  | Valor de CRF COFINS calculado |
| valor_de_crf_csll_calculado | `valor_crf_csll_calculado` | numeric(13) |  |  | Valor de CRF CSLL calculado |
| valor_de_crf_pis_aproveitado | `valor_crf_pis` | numeric(13) |  |  | Valor de CRF PIS aproveitado |
| valor_de_crf_cofins_aproveitado | `valor_crf_cofins` | numeric(13) |  |  | Valor de CRF COFINS aproveitado |
| valor_de_crf_csll_aproveitado | `valor_crf_csll` | numeric(13) |  |  | Valor de CRF CSLL aproveitado |
| aliquota_de_retencao_na_fonte | `aliquota_retencao_fonte` | numeric(5) |  |  | Aliquota de Retencao na Fonte |
| valor_de_pis_usado_somente_para_df | `valor_pis` | numeric(13) |  |  | Valor de PIS (Usado somente para DF) |
| aliquota_de_pis_usado_somente_para_df | `aliquota_pis` | numeric(5) |  |  | Aliquota de PIS (Usado somente para DF) |
| valor_de_cofins_usado_somente_para_df | `valor_cofins` | numeric(13) |  |  | Valor de COFINS (Usado somente para DF) |
| aliquota_de_cofins_usado_somente_para_df | `aliquota_cofins` | numeric(5) |  |  | Aliquota de COFINS (Usado somente para DF) |
| valor_ibs | `valor_ibs` | numeric(13) |  |  | Valor IBS |
| base_de_calculo_ibs | `base_calculo_ibs` | numeric(13) |  |  | Base de cálculo IBS |
| aliquota_ibs | `aliquota_ibs` | numeric(5) |  |  | Alíquota IBS |
| valor_cbs | `valor_cbs` | numeric(13) |  |  | Valor CBS |
| base_de_calculo_cbs | `base_calculo_cbs` | numeric(13) |  |  | Base de cálculo CBS |
| aliquota_cbs | `aliquota_cbs` | numeric(5) |  |  | Alíquota CBS |
| aliquota_efetiva_ibs | `aliquota_efetiva_ibs` | numeric(5) |  |  | Aliquota efetiva IBS |
| aliquota_efetiva_cbs | `aliquota_efetiva_cbs` | numeric(5) |  |  | Aliquota efetiva CBS |

**Filtros:** `faturamento` (eq/in), `parcela` (eq/in), `evento` (eq/in), `sequencial` (eq/in), `pago_pelo_escritorio_s_n` (eq/in), `complemento` (contem/prefixo)

## hrfaturamento_lancto

**Faturamento X Lancamentos Contabeis** — tabela `HRFATURAMENTO_LANCTO` (12.697 linhas)

Faturamento X Lancamentos Contabeis. 12.697 linhas no catálogo; chave: CODI_EMP, I_FATURAMENTO, EMPRESA_LAN, NUME_LAN.

- **Chave:** `CODI_EMP, I_FATURAMENTO, EMPRESA_LAN, NUME_LAN`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_FATURAMENTO asc`, `EMPRESA_LAN asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 12.697 linhas, 2 empresa(s).
- Vínculo geempre (geempre): 0 de 12.157 linhas sem registro relacionado (empresa 1).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| escritorio | `codi_emp` | integer(4) |  |  | Escritorio |
| faturamento | `i_faturamento` | integer(4) |  |  | Faturamento |
| empresa_do_lancamento_contabil | `empresa_lan` | integer(4) |  |  | Empresa do lancamento contabil |
| numero_do_lancamento_contabil | `nume_lan` | integer(4) |  |  | Numero do lancamento contabil |
| empresa_que_originou_o_lancamento_contab | `fili_lan` | integer(4) |  |  | Empresa que originou o lancamento contabil |
| codigo_do_lote | `codi_lote` | integer(4) |  |  | Codigo do lote |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `fili_lan` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `faturamento` (eq/in), `empresa_do_lancamento_contabil` (eq/in), `numero_do_lancamento_contabil` (eq/in), `codigo_do_lote` (eq/in)

## hrfaturamento_evento

**Faturamento - Eventos** — tabela `HRFATURAMENTO_EVENTO` (6.008 linhas)

Faturamento - Eventos. 6.008 linhas no catálogo; chave: CODI_EMP, I_FATURAMENTO, I_CLIENTE, I_RECEBER.

- **Chave:** `CODI_EMP, I_FATURAMENTO, I_CLIENTE, I_RECEBER`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_FATURAMENTO asc`, `I_CLIENTE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 6.008 linhas, 2 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| escritorio | `codi_emp` | integer(4) |  |  | Escritorio |
| faturamento | `i_faturamento` | integer(4) |  |  | Faturamento |
| cliente | `i_cliente` | integer(4) |  |  | Cliente |
| lancamento_receber | `i_receber` | integer(4) |  |  | Lancamento receber |
| valor | `valor` | numeric(13) |  |  | Valor |
| valor_de_desconto | `valor_desconto` | numeric(13) |  |  | Valor de desconto |
| valor_original | `valor_original` | numeric(13) |  |  | Valor original |

**Filtros:** `faturamento` (eq/in), `cliente` (eq/in), `lancamento_receber` (eq/in)

## hrfaturamento_adicional

**Faturamento - Adicional** — tabela `HRFATURAMENTO_ADICIONAL` (2.646 linhas)

Faturamento - Adicional. 2.646 linhas no catálogo; chave: CODI_EMP, I_FATURAMENTO, I_CONTRATO.

- **Chave:** `CODI_EMP, I_FATURAMENTO, I_CONTRATO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_FATURAMENTO asc`, `I_CONTRATO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2.646 linhas, 1 empresa(s).
- Vínculo hrcontrato (HRCONTRATO): 0 de 2.646 linhas sem registro relacionado (empresa 1).
- Vínculo hrevento (HREVENTO): 0 de 2.646 linhas sem registro relacionado (empresa 1).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| escritorio | `codi_emp` | integer(4) |  |  | Escritorio |
| faturamento | `i_faturamento` | integer(4) |  |  | Faturamento |
| contrato | `i_contrato` | integer(4) |  |  | Contrato |
| evento_do_adicional_anual | `i_evento` | integer(4) |  |  | Evento do adicional anual |
| faturou_com_contrato_s_n | `faturar_contrato` | char(1) |  |  | Faturou com contrato S N |
| valor | `valor` | numeric(13) |  |  | Valor |
| valor_de_desconto | `valor_desconto` | numeric(13) |  |  | Valor de desconto |
| valor_original | `valor_original` | numeric(13) |  |  | Valor original |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `hrcontrato` → `HRCONTRATO` por `codi_emp` = `codi_emp` e `i_contrato` = `i_contrato`; colunas: `hrcontrato_nome`
- `hrevento` → `HREVENTO` por `codi_emp` = `codi_emp` e `i_evento` = `i_evento`; colunas: `hrevento_nome`

**Filtros:** `faturamento` (eq/in), `contrato` (eq/in), `evento_do_adicional_anual` (eq/in), `faturou_com_contrato_s_n` (eq/in)

## hrfaturamento_evento_renegociacao

**Faturamento - Eventos oriundos da renegociacao** — tabela `HRFATURAMENTO_EVENTO_RENEGOCIACAO` (106 linhas)

Faturamento - Eventos oriundos da renegociacao. 106 linhas no catálogo; chave: CODI_EMP, I_FATURAMENTO, I_EVENTO, PAGO_ESCRITORIO.

- **Chave:** `CODI_EMP, I_FATURAMENTO, I_EVENTO, PAGO_ESCRITORIO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_FATURAMENTO asc`, `I_EVENTO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 106 linhas, 1 empresa(s).
- Vínculo hrevento (HREVENTO): 0 de 106 linhas sem registro relacionado (empresa 1).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| escritorio | `codi_emp` | integer(4) |  |  | Escritorio |
| faturamento | `i_faturamento` | integer(4) |  |  | Faturamento |
| evento | `i_evento` | integer(4) |  |  | Evento |
| pago_pelo_escritorio_s_n | `pago_escritorio` | char(1) |  |  | Pago pelo escritorio S N |
| valor | `valor` | numeric(13) |  |  | Valor |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `hrevento` → `HREVENTO` por `codi_emp` = `codi_emp` e `i_evento` = `i_evento`; colunas: `hrevento_nome`

**Filtros:** `faturamento` (eq/in), `evento` (eq/in), `pago_pelo_escritorio_s_n` (eq/in)

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

