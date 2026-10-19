# Modelo — Fiscal - configuracao (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/fiscal_configuracao.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

5 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [efconfiguracao_produto_por_ncm](#efconfiguracao_produto_por_ncm) | `EFCONFIGURACAO_PRODUTO_POR_NCM` | 1 | pequeno | empresa |
| [efconfiguracao_produto_por_ncm_vigencia](#efconfiguracao_produto_por_ncm_vigencia) | `EFCONFIGURACAO_PRODUTO_POR_NCM_VIGENCIA` | 1 | pequeno | empresa |
| [efconfiguracao_produto_por_ncm_vigencia_itens](#efconfiguracao_produto_por_ncm_vigencia_itens) | `EFCONFIGURACAO_PRODUTO_POR_NCM_VIGENCIA_ITENS` | 1 | pequeno | empresa |
| [efconfiguracao_produto_por_ncm_vigencia_itens_pro](#efconfiguracao_produto_por_ncm_vigencia_itens_pro) | `EFCONFIGURACAO_PRODUTO_POR_NCM_VIGENCIA_ITENS_PRO` | 1 | pequeno | empresa |
| [efconfiguracao_produto_por_ncm_vigencia_itens_ncm](#efconfiguracao_produto_por_ncm_vigencia_itens_ncm) | `EFCONFIGURACAO_PRODUTO_POR_NCM_VIGENCIA_ITENS_NCM` | 1 | pequeno | empresa |

## efconfiguracao_produto_por_ncm

**Configurar Dados de Impostos por NCM** — tabela `EFCONFIGURACAO_PRODUTO_POR_NCM` (1 linhas)

Configurar Dados de Impostos por NCM. 1 linhas no catálogo; chave: CODI_EMP, I_CONFIGURACAO_NCM.

- **Chave:** `CODI_EMP, I_CONFIGURACAO_NCM`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CONFIGURACAO_NCM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 234).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da Empresa |
| codigo_da_configuracao_de_produto_por_nc | `i_configuracao_ncm` | integer(4) |  |  | Código da Configuração de Produto por NCM |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `codigo_da_configuracao_de_produto_por_nc` (eq/in)

## efconfiguracao_produto_por_ncm_vigencia

**Configuração de Impostos para Produtos - Vigência** — tabela `EFCONFIGURACAO_PRODUTO_POR_NCM_VIGENCIA` (1 linhas)

Configuração de Impostos para Produtos - Vigência. 1 linhas no catálogo; chave: CODI_EMP, I_CONFIGURACAO_NCM, DATA_VIGENCIA.

- **Chave:** `CODI_EMP, I_CONFIGURACAO_NCM, DATA_VIGENCIA`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_VIGENCIA`
- **Ordem padrão:** `DATA_VIGENCIA desc`, `I_CONFIGURACAO_NCM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s), DATA_VIGENCIA de 2017-07-01 a 2017-07-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da Empresa |
| codigo_da_configuracao_de_produto_por_nc | `i_configuracao_ncm` | integer(4) |  |  | Código da Configuração de Produto por NCM |
| vigencia | `data_vigencia` | date(4) |  |  | Vigência |
| descricao | `descricao` | varchar(1024) |  |  | Descrição |

**Filtros:** `codigo_da_configuracao_de_produto_por_nc` (eq/in), `vigencia` (eq/in), `descricao` (contem/prefixo)

## efconfiguracao_produto_por_ncm_vigencia_itens

**Configuração de Impostos para Produtos - Registros** — tabela `EFCONFIGURACAO_PRODUTO_POR_NCM_VIGENCIA_ITENS` (1 linhas)

Configuração de Impostos para Produtos - Registros. 1 linhas no catálogo; chave: CODI_EMP, I_CONFIGURACAO_NCM, DATA_VIGENCIA, I_SEQUENCIAL.

- **Chave:** `CODI_EMP, I_CONFIGURACAO_NCM, DATA_VIGENCIA, I_SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_VIGENCIA`
- **Ordem padrão:** `DATA_VIGENCIA desc`, `I_CONFIGURACAO_NCM asc`, `I_SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s), DATA_VIGENCIA de 2017-07-01 a 2017-07-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da Empresa |
| codigo_da_configuracao_de_produto_por_nc | `i_configuracao_ncm` | integer(4) |  |  | Código da Configuração de Produto por NCM |
| vigencia | `data_vigencia` | date(4) |  |  | Vigência |
| sequencial | `i_sequencial` | integer(4) |  |  | Sequencial |
| codigo | `codigo_item` | integer(4) |  |  | Código |
| descricao | `descricao_item` | varchar(855) |  |  | Descrição |

**Filtros:** `codigo_da_configuracao_de_produto_por_nc` (eq/in), `vigencia` (eq/in), `sequencial` (eq/in), `codigo` (eq/in), `descricao` (contem/prefixo)

## efconfiguracao_produto_por_ncm_vigencia_itens_pro

**Configuração de Impostos para Produtos - Definição de Impostos** — tabela `EFCONFIGURACAO_PRODUTO_POR_NCM_VIGENCIA_ITENS_PRO` (1 linhas)

Configuração de Impostos para Produtos - Definição de Impostos. 1 linhas no catálogo; chave: CODI_EMP, I_CONFIGURACAO_NCM, DATA_VIGENCIA, I_SEQUENCIAL.

- **Chave:** `CODI_EMP, I_CONFIGURACAO_NCM, DATA_VIGENCIA, I_SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_VIGENCIA`
- **Ordem padrão:** `DATA_VIGENCIA desc`, `I_CONFIGURACAO_NCM asc`, `I_SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s), DATA_VIGENCIA de 2017-07-01 a 2017-07-01.
- Colunas expostas nulas em 100% das linhas (15): vinculo_do_credito, base_do_credito, unidade_tributavel_entradas, codigo_da_unidade_tributavel_entradas, codigo_de_recolhimento_pis, codigo_de_recolhimento_cofins, unidade_tributavel_saidas, codigo_da_unidade_tributavel_saidas, tabela_sped, marca_grupo_sped, sequencial_da_tabela_aliquota_do_icms, unidade_tributavel_ipi ....
- tipo_de_contribuicao_n_nao_cumulativo_c: todos os valores reais estão no comentário do banco (C=1).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da Empresa |
| codigo_da_configuracao_de_produto_por_nc | `i_configuracao_ncm` | integer(4) |  |  | Código da Configuração de Produto por NCM |
| vigencia | `data_vigencia` | date(4) |  |  | Vigência |
| sequencial | `i_sequencial` | integer(4) |  |  | Sequencial |
| tipo_de_contribuicao_n_nao_cumulativo_c | `tipo_contribuicao` | char(1) |  | efconfiguracao_produto_por_ncm_vigencia_itens_pro_tipo_de_con | Tipo de contribuição (N-Não cumulativo/C-Cumulativo/T-Subt. Tributária/S-Sem incidência) |
| pis_com_incidencia_cumulativa_conforme_l | `pis_incidencia_cumulativa_art_6` | char(1) |  |  | PIS com incidência cumulativa, conforme lei 12.693/12, Art. 6 (S/N) |
| cofins_com_incidencia_cumulativa_conform | `cofins_incidencia_cumulativa_art_10` | char(1) |  |  | COFINS com incidência cumulativa, conforme lei 10.833/03, Art. 10 (S/N) |
| cst_entradas | `codigo_cst_entrada` | integer(4) |  |  | CST - Entradas |
| vinculo_do_credito | `vinculo_credito` | integer(4) |  |  | Vínculo do crédito |
| base_do_credito | `base_credito` | integer(4) |  |  | Base do crédito |
| aproveitar_credito_proporcional_apenas_r | `aproveitar_credito_proporcional` | char(1) |  |  | Aproveitar crédito proporcional apenas referente a receita não cumulativa (S/N) |
| excluir_da_bc_os_valores_frete_seguros_e | `excluir_base_frete_seguro_oper_importacao` | char(1) |  |  | Excluir da BC os valores frete, seguros e desp. acessórias na importação (S/N) |
| credito_por_unidade_de_medida_s_n_entrad | `credito_unidade_medida` | char(1) |  |  | Crédito por unidade de medida (S/N) - Entradas |
| unidade_tributada_diferente_da_inventari | `unidade_diferente_credito` | char(1) |  |  | Unidade tributada diferente da inventariada (S/N) - Entradas |
| unidade_tributavel_entradas | `unidade_tributavel_credito` | char(6) |  |  | Unidade Tributável - Entradas |
| codigo_da_unidade_tributavel_entradas | `codigo_unidade_credito` | integer(4) |  |  | Código da unidade Tributável - Entradas |
| fator_de_conversao_entradas | `fator_conversao_credito` | numeric(15) |  |  | Fator de conversao - Entradas |
| valor_de_pis_entradas | `valor_pis_credito` | numeric(13) |  |  | Valor de PIS - Entradas |
| valor_de_cofins_entradas | `valor_cofins_credito` | numeric(13) |  |  | Valor de COFINS - Entradas |
| credito_por_aliquota_diferenciada_s_n_en | `credito_aliquota_diferenciada` | char(1) |  |  | Crédito por alíquota diferenciada (S/N) - Entradas |
| aliquota_do_pis_entradas | `aliquota_pis_credito` | numeric(7) |  |  | Alíquota do PIS - Entradas |
| aliquota_do_cofins_entradas | `aliquota_cofins_credito` | numeric(7) |  |  | Alíquota do COFINS - Entradas |
| cst_saidas | `codigo_cst_saida` | integer(4) |  |  | CST - Saídas |
| natureza_da_receita | `natureza_receita` | integer(4) |  |  | Natureza da receita |
| codigo_de_recolhimento_pis | `codigo_recolhimento_pis` | char(6) |  |  | Código de recolhimento PIS |
| codigo_de_recolhimento_cofins | `codigo_recolhimento_cofins` | char(6) |  |  | Código de recolhimento COFINS |
| debito_por_unidade_de_medida_s_n_saidas | `debito_unidade_medida` | char(1) |  |  | Débito por unidade de medida (S/N) - Saídas |
| unidade_diferente_debito | `unidade_diferente_debito` | char(1) |  |  | Unidade tributada diferente da inventariada (S/N) - Saídas |
| unidade_tributavel_saidas | `unidade_tributavel_debito` | char(6) |  |  | Unidade Tributável - Saídas |
| codigo_da_unidade_tributavel_saidas | `codigo_unidade_debito` | integer(4) |  |  | Código da unidade Tributável - Saídas |
| fator_de_conversao_saidas | `fator_conversao_debito` | numeric(15) |  |  | Fator de conversao - Saídas |
| valor_de_pis_saidas | `valor_pis_debito` | numeric(13) |  |  | Valor de PIS - Saídas |
| valor_de_cofins_saidas | `valor_cofins_debito` | numeric(13) |  |  | Valor de COFINS - Saídas |
| debito_por_aliquota_diferenciada_s_n_sai | `debito_aliquota_diferenciada` | char(1) |  |  | Débito por alíquota diferenciada (S/N) - Saídas |
| aliquota_do_pis_saidas | `aliquota_pis_debito` | numeric(7) |  |  | Alíquota do PIS - Saídas |
| aliquota_do_cofins_saidas | `aliquota_cofins_debito` | numeric(7) |  |  | Alíquota do COFINS - Saídas |
| produto_com_marca_comercial_refri_bebida | `produto_com_marca_comercial` | char(1) |  |  | Produto com marca comercial - REFRI (Bebidas Frias)(S/N) |
| tabela_sped | `tabela_sped` | integer(4) |  |  | Tabela SPED |
| marca_grupo_sped | `marca_grupo_sped` | integer(4) |  |  | Marca grupo SPED |
| cst_icms_entrada | `cst_icms_entrada` | integer(4) |  |  | CST ICMS - Entrada |
| cst_icms_saida | `cst_icms_saida` | integer(4) |  |  | CST ICMS - Saída |
| sequencial_da_tabela_aliquota_do_icms | `i_tabela_icms` | integer(4) |  |  | Sequencial da Tabela Alíquota do ICMS |
| aliquota_do_icms | `aliquota_icms` | numeric(5) |  |  | Alíquota do ICMS |
| cst_ipi_entrada | `cst_ipi_entrada` | integer(4) |  |  | CST IPI - Entrada |
| cst_ipi_saida | `cst_ipi_saida` | integer(4) |  |  | CST IPI - Saída |
| periodicidade_do_ipi_m_q_d_t_s_e_n_r_v | `periodicidade_ipi` | char(1) |  |  | Periodicidade do IPI (M/Q/D/T/S/E/N/R/V) |
| aliquota_do_ipi | `aliquota_ipi` | numeric(5) |  |  | Alíquota do IPI |
| calcula_ipi_por_unidade_de_medida_s_n | `calcula_ipi_unidade_medida` | char(1) |  |  | Calcula IPI por Unidade de Medida (S/N) |
| unidade_tributada_diferente_inventariada | `unidade_tributada_diferente_inventariada_ipi` | char(1) |  |  | Unidade Tributada Diferente da Inventariada do IPI (S/N) |
| unidade_tributavel_ipi | `unidade_tributavel_ipi` | char(6) |  |  | Unidade Tributável - Saídas |
| codigo_unidade_tributavel_ipi | `codigo_unidade_tributavel_ipi` | integer(4) |  |  | Código da Unidade Tributável - Saídas |
| fator_conversao_ipi | `fator_conversao_ipi` | numeric(15) |  |  | Fator de Conversão - Saídas |
| classe_do_enquadramento_do_ipi | `classe_enquadramento_ipi` | integer(4) |  |  | Classe do Enquadramento do IPI |
| valor_por_unidade_do_ipi | `valor_por_unidade_ipi` | numeric(13) |  |  | Valor por Unidade do IPI |
| produto_sujeito_a_tributacao_de_pis_e_co | `produto_sujeito_tributacao_monofasica_piscofins` | char(1) |  |  | Produto sujeito a tributação de PIS e COFINS  (S/N) |
| produto_sujeito_tributacao_monofasica_pi | `produto_sujeito_tributacao_monofasica_piscofins_tipo` | integer(4) |  |  | Produto sujeito a tributação de PIS e COFINS - Tipo (1/2) |
| produto_possui_percentual_de_reducao_na | `produto_possui_perc_red_bc_pis_cofins_saida` | char(1) |  |  | Produto possui percentual de redução na base de cálculo (S/N) |
| percentual_do_produto_possui_percentual | `percentual_reducao_base_calculo_pis_cofins_saida` | numeric(5) |  |  | Percentual do produto possui percentual de redução na base de cálculo |
| codigo_de_recolhimento_de_ipi | `i_recolhimento_ipi` | integer(4) |  |  | Código de recolhimento de IPI |
| codigo_da_cst_para_relacionamento_da_nat | `codigo_cst_natureza_receita` | integer(4) |  |  | Código da CST para relacionamento da natureza da receita |

**Filtros:** `codigo_da_configuracao_de_produto_por_nc` (eq/in), `vigencia` (eq/in), `sequencial` (eq/in), `tipo_de_contribuicao_n_nao_cumulativo_c` (eq/in), `pis_com_incidencia_cumulativa_conforme_l` (eq/in), `cofins_com_incidencia_cumulativa_conform` (eq/in), `cst_entradas` (eq/in), `aproveitar_credito_proporcional_apenas_r` (eq/in), `excluir_da_bc_os_valores_frete_seguros_e` (eq/in), `credito_por_unidade_de_medida_s_n_entrad` (eq/in), `unidade_tributada_diferente_da_inventari` (eq/in), `unidade_tributavel_entradas` (eq/in), `codigo_da_unidade_tributavel_entradas` (eq/in), `credito_por_aliquota_diferenciada_s_n_en` (eq/in)

## efconfiguracao_produto_por_ncm_vigencia_itens_ncm

**Configuração de Impostos para Produtos - Definição de NCMs** — tabela `EFCONFIGURACAO_PRODUTO_POR_NCM_VIGENCIA_ITENS_NCM` (1 linhas)

Configuração de Impostos para Produtos - Definição de NCMs. 1 linhas no catálogo; chave: CODI_EMP, I_CONFIGURACAO_NCM, DATA_VIGENCIA, I_SEQUENCIAL, I_SEQUENCIAL_NCM.

- **Chave:** `CODI_EMP, I_CONFIGURACAO_NCM, DATA_VIGENCIA, I_SEQUENCIAL, I_SEQUENCIAL_NCM`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_VIGENCIA`
- **Ordem padrão:** `DATA_VIGENCIA desc`, `I_CONFIGURACAO_NCM asc`, `I_SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s), DATA_VIGENCIA de 2017-07-01 a 2017-07-01.
- Colunas expostas nulas em 100% das linhas (1): codigo_cest.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da Empresa |
| codigo_da_configuracao_de_produto_por_nc | `i_configuracao_ncm` | integer(4) |  |  | Código da Configuração de Produto por NCM |
| vigencia | `data_vigencia` | date(4) |  |  | Vigência |
| sequencial | `i_sequencial` | integer(4) |  |  | Sequencial |
| sequencial_ncm | `i_sequencial_ncm` | integer(4) |  |  | Sequencial NCM |
| codigo_ncm | `ncm` | char(8) |  |  | Código NCM |
| codigo_cest | `codigo_cest` | char(7) |  |  | Codigo CEST |

**Filtros:** `codigo_da_configuracao_de_produto_por_nc` (eq/in), `vigencia` (eq/in), `sequencial` (eq/in), `sequencial_ncm` (eq/in), `codigo_ncm` (eq/in), `codigo_cest` (eq/in)

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

### efconfiguracao_produto_por_ncm_vigencia_itens_pro_tipo_de_con

Confirmado: sim

> Todos os valores observados em EFCONFIGURACAO_PRODUTO_POR_NCM_VIGENCIA_ITENS_PRO.TIPO_CONTRIBUICAO estão no comentário do banco (2026-10-18). Distribuição: C=1.

| Código | Significado |
|---|---|
| N | Não cumulativo |
| C | Cumulativo |
| T | Subt. Tributária |
| S | Sem incidência |

