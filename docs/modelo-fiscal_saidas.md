# Modelo — Fiscal - saidas (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/fiscal_saidas.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

24 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [efsaidas_info_comp_contrib](#efsaidas_info_comp_contrib) | `EFSAIDAS_INFO_COMP_CONTRIB` | 426.402 | medio | empresa |
| [efsaidas_info_comp_fisco](#efsaidas_info_comp_fisco) | `EFSAIDAS_INFO_COMP_FISCO` | 101.415 | medio | empresa |
| [efsaidas_pis_cofins](#efsaidas_pis_cofins) | `EFSAIDAS_PIS_COFINS` | 70.092 | medio | empresa |
| [efsaidas_observacao_contrib](#efsaidas_observacao_contrib) | `EFSAIDAS_OBSERVACAO_CONTRIB` | 39.572 | medio | empresa |
| [efsaidas_difal_nc](#efsaidas_difal_nc) | `EFSAIDAS_DIFAL_NC` | 31.780 | medio | empresa |
| [efsaidas_detalhamento_mg](#efsaidas_detalhamento_mg) | `efsaidas_detalhamento_mg` | 27.581 | medio | empresa |
| [efsaidas_info_pag](#efsaidas_info_pag) | `EFSAIDAS_INFO_PAG` | 21.809 | medio | empresa |
| [efsaidas_estadual_sp](#efsaidas_estadual_sp) | `EFSAIDAS_ESTADUAL_SP` | 9.350 | pequeno | empresa |
| [efsaidas_estadual_rj](#efsaidas_estadual_rj) | `EFSAIDAS_ESTADUAL_RJ` | 8.745 | pequeno | empresa |
| [efsaidas_inss_rb](#efsaidas_inss_rb) | `EFSAIDAS_INSS_RB` | 2.296 | pequeno | empresa |
| [efsaidas_efd_reinf](#efsaidas_efd_reinf) | `EFSAIDAS_EFD_REINF` | 961 | pequeno | empresa |
| [efsaidas_documentos_fiscais_referenciados](#efsaidas_documentos_fiscais_referenciados) | `EFSAIDAS_DOCUMENTOS_FISCAIS_REFERENCIADOS` | 618 | pequeno | empresa |
| [efsaidas_estadual_pe](#efsaidas_estadual_pe) | `EFSAIDAS_ESTADUAL_PE` | 102 | pequeno | empresa |
| [efsaidas_icms_desonerado](#efsaidas_icms_desonerado) | `EFSAIDAS_ICMS_DESONERADO` | 72 | pequeno | empresa |
| [efsaidas_frete](#efsaidas_frete) | `efsaidas_frete` | 61 | pequeno | empresa |
| [efsaidas_exportacao](#efsaidas_exportacao) | `efsaidas_exportacao` | 53 | pequeno | empresa |
| [efsaidas_estadual_mg](#efsaidas_estadual_mg) | `EFSAIDAS_ESTADUAL_MG` | 35 | pequeno | empresa |
| [efsaidas_estadual_sc](#efsaidas_estadual_sc) | `EFSAIDAS_ESTADUAL_SC` | 34 | pequeno | empresa |
| [efsaidas_estadual_ba](#efsaidas_estadual_ba) | `EFSAIDAS_ESTADUAL_BA` | 13 | pequeno | empresa |
| [efsaidas_nota_devolvida](#efsaidas_nota_devolvida) | `EFSAIDAS_NOTA_DEVOLVIDA` | 8 | pequeno | empresa |
| [efsaidas_valor_presente_provisao](#efsaidas_valor_presente_provisao) | `EFSAIDAS_VALOR_PRESENTE_PROVISAO` | 5 | pequeno | empresa |
| [efsaidas_estadual_ro](#efsaidas_estadual_ro) | `EFSAIDAS_ESTADUAL_RO` | 2 | pequeno | empresa |
| [efsaidas_observacao_fisco](#efsaidas_observacao_fisco) | `EFSAIDAS_OBSERVACAO_FISCO` | 1 | pequeno | empresa |
| [efsaidas_estadual_ac](#efsaidas_estadual_ac) | `EFSAIDAS_ESTADUAL_AC` | 1 | pequeno | empresa |

## efsaidas_info_comp_contrib

**Notas Fiscais de Saídas - Informação complementar de interesse do contribuinte** — tabela `EFSAIDAS_INFO_COMP_CONTRIB` (426.402 linhas)

Notas Fiscais de Saídas - Informação complementar de interesse do contribuinte. 426.402 linhas no catálogo; chave: CODI_EMP, CODI_SAI, I_SEQUENCIAL_CONTRIB.

- **Chave:** `CODI_EMP, CODI_SAI, I_SEQUENCIAL_CONTRIB`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `I_SEQUENCIAL_CONTRIB asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 427.133 linhas, 130 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): codigo_da_informacao_complementar.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_sai` | integer(4) |  |  | Codigo |
| sequencial | `i_sequencial_contrib` | integer(4) |  |  | Sequencial |
| codigo_da_informacao_complementar | `i_info_comp_contrib` | integer(4) |  |  | Código da Informação Complementar |
| descricao_da_informacao_complementar | `descricao_contrib` | varchar(1000) |  |  | Descrição da Informação Complementar |

**Filtros:** `codigo` (eq/in), `sequencial` (eq/in), `codigo_da_informacao_complementar` (eq/in), `descricao_da_informacao_complementar` (contem/prefixo)

## efsaidas_info_comp_fisco

**Notas Fiscais de Saídas - Informação complementar de interesse do fisco** — tabela `EFSAIDAS_INFO_COMP_FISCO` (101.415 linhas)

Notas Fiscais de Saídas - Informação complementar de interesse do fisco. 101.415 linhas no catálogo; chave: CODI_EMP, CODI_SAI, I_SEQUENCIAL_FISCO.

- **Chave:** `CODI_EMP, CODI_SAI, I_SEQUENCIAL_FISCO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `I_SEQUENCIAL_FISCO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 101.425 linhas, 41 empresa(s).
- Colunas expostas nulas em 100% das linhas (2): codigo_da_informacao_complementar, identificador.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_sai` | integer(4) |  |  | Codigo |
| sequencial | `i_sequencial_fisco` | integer(4) |  |  | Sequencial |
| codigo_da_informacao_complementar | `i_info_comp_fisco` | integer(4) |  |  | Código da Informação Complementar |
| descricao_da_informacao_complementar | `descricao_fisco` | varchar(1000) |  |  | Descrição da Informação Complementar |
| identificador | `identificador_sped` | varchar(6) |  |  | Identificador |

**Filtros:** `codigo` (eq/in), `sequencial` (eq/in), `codigo_da_informacao_complementar` (eq/in), `descricao_da_informacao_complementar` (contem/prefixo), `identificador` (eq/in)

## efsaidas_pis_cofins

**Notas Fiscais de Saida - PIS/COFINS** — tabela `EFSAIDAS_PIS_COFINS` (70.092 linhas)

Notas Fiscais de Saida - PIS/COFINS. 70.092 linhas no catálogo; chave: CODI_EMP, CODI_SAI, I_PIS_COFINS.

- **Chave:** `CODI_EMP, CODI_SAI, I_PIS_COFINS`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `I_PIS_COFINS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 70.100 linhas, 69 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): codigo_do_beneficio_dirbi.
- Vínculo eftabela_natureza_receit (EFTABELA_NATUREZA_RECEITA): 0 de 20 linhas sem registro relacionado (empresa 662).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_da_saida | `codi_sai` | integer(4) |  |  | Código da saída |
| sequencial | `i_pis_cofins` | integer(4) |  |  | Sequencial |
| cst | `cst` | integer(4) |  |  | CST |
| natureza_da_receita | `natureza_receita` | integer(4) |  |  | Natureza da receita |
| valor_contabil | `valor_contabil` | numeric(13) |  |  | Valor contábil |
| exclusoes | `exclusoes` | numeric(13) |  |  | Exclusões |
| base_de_calculo | `base_calculo` | numeric(13) |  |  | Base de cálculo |
| aliquota_do_pis | `aliquota_pis` | numeric(7) |  |  | Alíquota do PIS |
| aliquota_da_cofins | `aliquota_cofins` | numeric(7) |  |  | Alíquota da COFINS |
| quantidade_tributada | `quantidade_tributada` | numeric(13) |  |  | Quantidade tributada |
| valor_por_unidade_do_pis_por_unidade_de | `valor_unidade_medida_pis` | numeric(13) |  |  | Valor por unidade do PIS por unidade de medida |
| valor_por_unidade_da_cofins_por_unidade | `valor_unidade_medida_cofins` | numeric(13) |  |  | Valor por unidade da COFINS por unidade de medida |
| valor_do_pis | `valor_pis` | numeric(13) |  |  | Valor do PIS |
| valor_da_cofins | `valor_cofins` | numeric(13) |  |  | Valor da COFINS |
| exclusao_cooperativa | `exclusao_cooperativa` | numeric(13) |  |  | Exclusão Cooperativa |
| percentual_reducao_base_calculo | `percentual_reducao_bc` | numeric(5) |  |  | Percentual Redução Base Cálculo |
| codigo_sequencial_do_recolhimento_do_pis | `i_recolhimento_pis` | integer(4) |  |  | Código Sequencial do Recolhimento do PIS |
| codigo_do_recolhimento_do_pis | `codigo_recolhimento_pis` | char(6) |  |  | Código do Recolhimento do PIS |
| codigo_sequencial_do_recolhimento_do_cof | `i_recolhimento_cofins` | integer(4) |  |  | Código Sequencial do Recolhimento do COFINS |
| codigo_do_recolhimento_do_cofins | `codigo_recolhimento_cofins` | char(6) |  |  | Código do Recolhimento do COFINS |
| codigo_do_beneficio_dirbi | `codigo_beneficio_dirbi` | integer(4) |  |  | Código do Benefício DIRBI |
| calcular_reducao_linear_lc224 | `calcular_reducao_linear_lc224` | char(1) |  |  | Calcular redução conf. LC 224/2025 |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `eftabela_natureza_receit` → `EFTABELA_NATUREZA_RECEITA` por `natureza_receita` = `codigo` e `cst` = `codigo_cst`; colunas: `eftabela_natureza_receit_nome`

**Filtros:** `codigo_da_saida` (eq/in), `sequencial` (eq/in), `codigo_sequencial_do_recolhimento_do_pis` (eq/in), `codigo_do_recolhimento_do_pis` (eq/in), `codigo_sequencial_do_recolhimento_do_cof` (eq/in), `codigo_do_recolhimento_do_cofins` (eq/in), `codigo_do_beneficio_dirbi` (eq/in), `calcular_reducao_linear_lc224` (eq/in)

## efsaidas_observacao_contrib

**Notas Fiscais de Saídas - Obseração de interesse do contribuinte** — tabela `EFSAIDAS_OBSERVACAO_CONTRIB` (39.572 linhas)

Notas Fiscais de Saídas - Obseração de interesse do contribuinte. 39.572 linhas no catálogo; chave: CODI_EMP, CODI_SAI, I_SEQUENCIAL_CONTRIB.

- **Chave:** `CODI_EMP, CODI_SAI, I_SEQUENCIAL_CONTRIB`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `I_SEQUENCIAL_CONTRIB asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 39.801 linhas, 13 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): codigo_da_observacao.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_sai` | integer(4) |  |  | Codigo |
| sequencial | `i_sequencial_contrib` | integer(4) |  |  | Sequencial |
| codigo_da_observacao | `i_observacao_contrib` | integer(4) |  |  | Código da Observação |
| descricao_da_observacao | `descricao_contrib` | varchar(300) |  |  | Descrição da Observação |

**Filtros:** `codigo` (eq/in), `sequencial` (eq/in), `codigo_da_observacao` (eq/in), `descricao_da_observacao` (contem/prefixo)

## efsaidas_difal_nc

**Notas Fiscais de Saida - DIFAL NC** — tabela `EFSAIDAS_DIFAL_NC` (31.780 linhas)

Notas Fiscais de Saida - DIFAL NC. 31.780 linhas no catálogo; chave: CODI_EMP, CODI_SAI.

- **Chave:** `CODI_EMP, CODI_SAI`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 32.016 linhas, 24 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_sai` | integer(4) |  |  | Código |
| base_calculo | `base_calculo` | numeric(15) |  |  | Base Cálculo |
| aliquota | `aliquota` | numeric(5) |  |  | Alíquota |
| valor_uf_origem | `valor_uf_origem` | numeric(15) |  |  | Valor UF Origem |
| valor_uf_destino | `valor_uf_destino` | numeric(15) |  |  | Valor UF Destino |
| valor_total | `valor_total` | numeric(15) |  |  | Valor Total |
| valor_fcp | `valor_fcp` | numeric(15) |  |  | Valor FCP |

**Filtros:** `codigo` (eq/in)

## efsaidas_detalhamento_mg

**Notas Fiscais de Saidas - Detalhamentos - MG** — tabela `efsaidas_detalhamento_mg` (27.581 linhas)

Notas Fiscais de Saidas - Detalhamentos - MG. 27.581 linhas no catálogo; chave: codi_emp, codi_sai.

- **Chave:** `codi_emp, codi_sai`
- **Empresa:** `codi_emp`
- **Período:** `—`
- **Ordem padrão:** `codi_sai asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 27.581 linhas, 4 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| nota | `codi_sai` | integer(4) |  |  | Nota |
| isentas | `isentas` | numeric(13) |  |  | Isentas |
| nao_tributadas | `nao_tributadas` | numeric(13) |  |  | Nao tributadas |
| parcela_de_base_de_calculo_reduzida | `base_reduzida` | numeric(13) |  |  | Parcela de base de calculo reduzida |
| diferidas | `diferidas` | numeric(13) |  |  | Diferidas |
| suspensas | `suspensas` | numeric(13) |  |  | Suspensas |
| substituicao_tributaria | `substituicao` | numeric(13) |  |  | Substituicao tributaria |
| outras | `outras` | numeric(13) |  |  | Outras |

**Filtros:** `nota` (eq/in)

## efsaidas_info_pag

**Notas Fiscais de Saidas - Informação Pagamento** — tabela `EFSAIDAS_INFO_PAG` (21.809 linhas)

Notas Fiscais de Saidas - Informação Pagamento. 21.809 linhas no catálogo; chave: CODI_EMP, CODI_SAI, I_SEQUENCIAL.

- **Chave:** `CODI_EMP, CODI_SAI, I_SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `I_SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 22.587 linhas, 37 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_sai` | integer(4) |  |  | Codigo |
| sequencial | `i_sequencial` | integer(4) |  |  | Sequencial |
| indicador_da_forma_de_pagamento | `indicador_forma_pagamento` | integer(4) |  |  | Indicador da forma de pagamento |
| meio_de_pagamento | `meio_pagamento` | integer(4) |  |  | Meio de pagamento |
| valor_do_pagamento | `valor_pagamento` | numeric(13) |  |  | Valor do pagamento |
| tipo_de_integracao_para_pagamento | `tipo_integracao_pagamento` | integer(4) |  |  | Tipo de integracao para pagamento |
| cnpj_da_instituicao_de_pagamento 🔒 | `cnpj_instituicao_pagamento` | char(14) |  |  | CNPJ da instituicao de pagamento |
| bandeira_da_operadora_de_cartao_de_credi | `bandeira_operadora_cartao_cred_deb` | integer(4) |  |  | Bandeira da operadora de cartao de credito e/ou debito |
| numero_de_autorizacao_da_operacao_cartao | `numero_autorizacao_operacao_cartao_cred_deb` | varchar(20) |  |  | Numero de autorizacao da operacao cartao de credito e/ou debito |
| valor_do_troco | `valor_troco` | numeric(13) |  |  | Valor do troco |

**Filtros:** `codigo` (eq/in), `sequencial` (eq/in), `tipo_de_integracao_para_pagamento` (eq/in), `cnpj_da_instituicao_de_pagamento` (eq/in), `numero_de_autorizacao_da_operacao_cartao` (eq/in)

## efsaidas_estadual_sp

**Notas Fiscais de Saídas - Dados Estaduais - SP** — tabela `EFSAIDAS_ESTADUAL_SP` (9.350 linhas)

Notas Fiscais de Saídas - Dados Estaduais - SP. 9.350 linhas no catálogo; chave: CODI_EMP, CODI_SAI.

- **Chave:** `CODI_EMP, CODI_SAI`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 9.364 linhas, 129 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_sai` | integer(4) |  |  | Código |
| base_de_calculo | `base_calculo_icms_sn` | numeric(13) |  |  | Base de Cálculo |
| aliquota | `aliquota_icms_sn` | numeric(5) |  |  | Alíquota |
| valor | `valor_icms_sn` | numeric(13) |  |  | Valor |
| valor_dispensado_de_escrituracao_dipam | `valor_dispensado_dipam` | numeric(13) |  |  | Valor dispensado de Escrituração DIPAM |

**Filtros:** `codigo` (eq/in)

## efsaidas_estadual_rj

**Notas Fiscais de Saídas - Dados estaduais - RJ** — tabela `EFSAIDAS_ESTADUAL_RJ` (8.745 linhas)

Notas Fiscais de Saídas - Dados estaduais - RJ. 8.745 linhas no catálogo; chave: CODI_EMP, CODI_SAI.

- **Chave:** `CODI_EMP, CODI_SAI`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 8.745 linhas, 8 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): outros_beneficios_para_informacao_no_dub.
- Vínculo eftabela_rj_dub_icms (EFTABELA_RJ_DUB_ICMS): 75 de 75 linhas sem registro relacionado (empresa 1682).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_da_saida | `codi_sai` | integer(4) |  |  | Código da saída |
| codigo_do_valor_adicionado_para_a_declan | `codigo_valor_adicionado` | integer(4) |  |  | Código do valor adicionado para a DECLAN-IPM |
| valor_adicionado_para_a_declan_ipm | `valor_adicionado` | numeric(13) |  |  | Valor adicionado para a DECLAN-IPM |
| preco_da_mercadoria_sem_abatimento | `preco_sem_abatimento` | numeric(13) |  |  | Preço da mercadoria sem abatimento |
| valor_do_icms_abatido | `valor_icms_abatido` | numeric(13) |  |  | Valor do ICMS abatido |
| outros_beneficios_para_informacao_no_dub | `i_dub_icms` | integer(4) |  |  | Outros benefícios para informação no DUB-ICMS - Código |
| dub_icms_valor_operacao | `dub_icms_valor_operacao` | numeric(13) |  |  | Outros benefícios para informação no DUB-ICMS - Valor da operação |
| dub_icms_aliquota | `dub_icms_aliquota` | numeric(5) |  |  | Outros benefícios para informação no DUB-ICMS - Alíquota |
| dub_icms_valor_icms_nao_recolhido | `dub_icms_valor_icms_nao_recolhido` | numeric(13) |  |  | Outros benefícios para informação no DUB-ICMS - Valor do ICMS não recolhido |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `eftabela_rj_dub_icms` → `EFTABELA_RJ_DUB_ICMS` por `codi_emp` = `codi_emp` e `i_dub_icms` = `i_dub_icms`; colunas: `eftabela_rj_dub_icms_nome`

**Filtros:** `codigo_da_saida` (eq/in), `codigo_do_valor_adicionado_para_a_declan` (eq/in), `outros_beneficios_para_informacao_no_dub` (eq/in)

## efsaidas_inss_rb

**Notas Fiscais de Saídas - INSS Receita Bruta** — tabela `EFSAIDAS_INSS_RB` (2.296 linhas)

Notas Fiscais de Saídas - INSS Receita Bruta. 2.296 linhas no catálogo; chave: CODI_EMP, CODI_SAI.

- **Chave:** `CODI_EMP, CODI_SAI`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2.296 linhas, 114 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_sai` | integer(4) |  |  | Codigo |
| valor_contabil | `valor_contabil_inss_rb` | numeric(13) |  |  | Valor Contábil |
| deducoes | `deducoes_inss_rb` | numeric(13) |  |  | Deduções |
| receita_bruta | `receita_bruta_inss_rb` | numeric(13) |  |  | Receita Bruta |
| valor_desonerada | `desonerada_inss_rb` | numeric(13) |  |  | Valor Desonerada |
| valor_nao_desonerada | `nao_desonerada_inss_rb` | numeric(13) |  |  | Valor Não Desonerada |
| valor_total | `total_inss_rb` | numeric(13) |  |  | Valor Total |
| receita_bruta_reinf | `receita_bruta_total_reinf` | numeric(13) |  |  | Receita Bruta REINF |
| desconto_reinf | `desconto_reinf` | numeric(13) |  |  | Desconto REINF |
| valor_desonerada_reinf | `desonerada_inss_rb_reinf` | numeric(13) |  |  | Valor Desonerada REINF |
| valor_nao_desonerada_reinf | `nao_desonerada_inss_rb_reinf` | numeric(13) |  |  | Valor Não Desonerada REINF |
| valor_total_reinf | `total_inss_rb_reinf` | numeric(13) |  |  | Valor Total REINF |

**Filtros:** `codigo` (eq/in)

## efsaidas_efd_reinf

**Notas Fiscais de Saída - EFD Reinf** — tabela `EFSAIDAS_EFD_REINF` (961 linhas)

Notas Fiscais de Saída - EFD Reinf. 961 linhas no catálogo; chave: CODI_EMP, CODI_SAI.

- **Chave:** `CODI_EMP, CODI_SAI`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 961 linhas, 8 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_sai` | integer(4) |  |  | Código |
| tipo_de_servico | `tipo_servico` | varchar(10) |  |  | Tipo de serviço |
| indicativo_de_prestacao_de_servico | `indicativo_prestacao_servicos` | integer(4) |  |  | Indicativo de Prestação de Serviço |
| possui_paj | `possui_paj_sai` | char(1) |  |  | Possui PAJ |

**Filtros:** `codigo` (eq/in), `tipo_de_servico` (eq/in), `possui_paj` (eq/in)

## efsaidas_documentos_fiscais_referenciados

**Notas Fiscais de Saída - Documentos fiscais referenciados** — tabela `EFSAIDAS_DOCUMENTOS_FISCAIS_REFERENCIADOS` (618 linhas)

Notas Fiscais de Saída - Documentos fiscais referenciados. 618 linhas no catálogo; chave: CODI_EMP, CODI_SAI, DOCUMENTO_DFSAI.

- **Chave:** `CODI_EMP, CODI_SAI, DOCUMENTO_DFSAI`
- **Empresa:** `CODI_EMP`
- **Período:** `EMISSAO_DFSAI`
- **Ordem padrão:** `EMISSAO_DFSAI desc`, `CODI_SAI asc`, `DOCUMENTO_DFSAI asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 618 linhas, 1 empresa(s), EMISSAO_DFSAI de 2025-05-01 a 2025-06-01.
- operacao_0_entrada_1_saida: todos os valores reais estão no comentário do banco (1=618).
- emitente_0_emissao_propria_1_terceiros: todos os valores reais estão no comentário do banco (0=618).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_sai` | integer(4) |  |  | Código |
| sequencial | `documento_dfsai` | integer(4) |  |  | Sequencial |
| operacao_0_entrada_1_saida | `operacao_dfsai` | char(1) |  | efsaidas_documentos_fiscais_referenciados_operacao_0_ | Operação (0 - Entrada/1 - Saída) |
| emitente_0_emissao_propria_1_terceiros | `emitente_dfsai` | char(1) |  | efsaidas_documentos_fiscais_referenciados_emitente_0_ | Emitente (0 - Emissão própria/1 - Terceiros) |
| participante | `participante_dfsai` | integer(4) |  |  | Participante |
| modelo_da_especie | `especie_dfsai` | integer(4) |  |  | Modelo da espécie |
| serie | `serie_dfsai` | char(4) |  |  | Série |
| sub_serie | `subserie_dfsai` | integer(4) |  |  | Sub-série |
| numero_do_documento | `numero_dfsai` | integer(4) |  |  | Número do documento |
| data_de_emissao | `emissao_dfsai` | date(4) |  |  | Data de emissão |
| saida | `saida_dfsai` | date(4) |  |  | Saída |
| valor_da_nota | `valor_nota_dfsai` | numeric(13) |  |  | Valor da nota |
| situacao | `situacao_dfsai` | integer(4) |  |  | Situação |
| valor_do_iss | `valor_iss_dfsai` | numeric(13) |  |  | Valor do ISS |
| valor_do_iss_retido | `valor_iss_retido_dfsai` | numeric(13) |  |  | Valor do ISS Retido |
| valor_do_icms | `valor_icms_dfsai` | numeric(13) |  |  | Valor do ICMS |
| valor_do_icms_st | `valor_icms_st_dfsai` | numeric(13) |  |  | Valor do ICMS ST |
| valor_do_ipi | `valor_ipi_dfsai` | numeric(13) |  |  | Valor do IPI |
| chave_nfe_ou_cte | `chave_nfe_cte` | varchar(44) |  |  | Chave NFe ou CTe |

**Filtros:** `codigo` (eq/in), `sequencial` (eq/in), `data_de_emissao` (entre/gte/lte), `saida` (entre/gte/lte), `operacao_0_entrada_1_saida` (eq/in), `emitente_0_emissao_propria_1_terceiros` (eq/in), `serie` (eq/in), `situacao` (eq/in), `chave_nfe_ou_cte` (contem/prefixo)

## efsaidas_estadual_pe

**Notas Fiscais de Saídas - Dados estaduais - PE** — tabela `EFSAIDAS_ESTADUAL_PE` (102 linhas)

Notas Fiscais de Saídas - Dados estaduais - PE. 102 linhas no catálogo; chave: CODI_EMP, CODI_SAI.

- **Chave:** `CODI_EMP, CODI_SAI`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 102 linhas, 3 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da Empresa |
| codigo_da_nota | `codi_sai` | integer(4) |  |  | Código da Nota |
| tipo_combustivel | `tipo_combustivel` | integer(4) |  |  | Tipo combustível |

**Filtros:** `codigo_da_nota` (eq/in), `tipo_combustivel` (eq/in)

## efsaidas_icms_desonerado

**ICMS desonerado** — tabela `EFSAIDAS_ICMS_DESONERADO` (72 linhas)

ICMS desonerado. 72 linhas no catálogo; chave: CODI_EMP, CODI_SAI, I_ICMS_DESONERADO.

- **Chave:** `CODI_EMP, CODI_SAI, I_ICMS_DESONERADO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `I_ICMS_DESONERADO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 72 linhas, 7 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_da_nota | `codi_sai` | integer(4) |  |  | Código da nota |
| sequencial | `i_icms_desonerado` | integer(4) |  |  | Sequencial |
| cst_do_icms_desonerado | `cst_icms_desonerado` | integer(4) |  |  | CST do ICMS desonerado |
| valor_desonerado | `valor_desonerado` | numeric(13) |  |  | Valor desonerado |
| i_motivo_desoneracao | `i_motivo_desoneracao` | integer(4) |  |  | Motivo da desoneração (1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) |

**Filtros:** `codigo_da_nota` (eq/in), `sequencial` (eq/in), `i_motivo_desoneracao` (eq/in)

## efsaidas_frete

**Saidas - Dados do frete** — tabela `efsaidas_frete` (61 linhas)

Saidas - Dados do frete. 61 linhas no catálogo; chave: codi_emp, codi_sai.

- **Chave:** `codi_emp, codi_sai`
- **Empresa:** `codi_emp`
- **Período:** `—`
- **Ordem padrão:** `codi_sai asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 61 linhas, 1 empresa(s).
- Colunas expostas nulas em 100% das linhas (25): uf_do_transportador, placa1_saif, uf_placa1_saif, placa2_saif, uf_placa2_saif, placa3_saif, uf_placa3_saif, cnpj_do_local_do_recebimento, uf_do_local_do_recebimento, inscricao_estadual_do_local_do_recebimen, cnpj_do_local_da_saida, uf_do_local_da_saida ....
- tipo_da_inscricao_1_cnpj_2_cpf: todos os valores reais estão no comentário do banco (1=61).
- tipo_da_inscricao_1_cnpj_2_cpf_3_cei_4_o: coluna sem nenhum valor preenchido; o domínio do comentário do banco não pôde ser verificado.
- tipo_insc_local_saif: coluna sem nenhum valor preenchido; o domínio do comentário do banco não pôde ser verificado.
- Vínculo gemunicipio (gemunicipio): 0 de 61 linhas sem registro relacionado (empresa 10).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_sai` | integer(4) |  |  | Codigo |
| modalidade_do_frete_cif_fob | `modfrete_saif` | char(1) |  |  | Modalidade do Frete (Cif / Fob) |
| modtransp_saif | `modtransp_saif` | tinyint(1) |  |  | Modalidade do Transporte (1-Rodoviario,2-Ferroviario,3-Rodo-Ferroviario,4-Aquaviario,5-Dutoviario,6-Aereo,7-Outro) |
| transportador_emitente_destinatario_outr | `transportador_saif` | char(1) |  |  | Transportador ( Emitente / Destinatário / Outro) |
| cnpj_do_transportador 🔒 | `cnpj_transp_saif` | char(14) |  |  | Cnpj do Transportador |
| uf_do_transportador | `uf_transp_saif` | char(2) |  |  | UF do Transportador |
| inscricao_estadual_do_transportador 🔒 | `iest_transp_saif` | char(20) |  |  | Inscricao Estadual do Transportador |
| placa1_saif | `placa1_saif` | char(8) |  |  | Placa do transportador (1) |
| uf_placa1_saif | `uf_placa1_saif` | char(2) |  |  | UF da Placa do transportador (1) |
| placa2_saif | `placa2_saif` | char(8) |  |  | Placa do transportador (2) |
| uf_placa2_saif | `uf_placa2_saif` | char(2) |  |  | UF da Placa do transportador (2) |
| placa3_saif | `placa3_saif` | char(8) |  |  | Placa do transportador (3) |
| uf_placa3_saif | `uf_placa3_saif` | char(2) |  |  | UF da Placa do transportador (3) |
| local_recebimento_destinatario_outro | `local_saif` | char(1) |  |  | Local Recebimento ( Destinatário / Outro ) |
| cnpj_do_local_do_recebimento 🔒 | `cnpj_local_saif` | char(14) |  |  | Cnpj do local do Recebimento |
| uf_do_local_do_recebimento | `uf_local_saif` | char(2) |  |  | UF do local do Recebimento |
| inscricao_estadual_do_local_do_recebimen 🔒 | `iest_local_saif` | char(20) |  |  | Inscricao Estadual do local do Recebimento |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| local_da_saida_emitente_outro | `local_saida_saif` | char(1) |  |  | Local da Saida ( Emitente / Outro ) |
| cnpj_do_local_da_saida 🔒 | `cnpj_local_saida_saif` | char(14) |  |  | Cnpj do local da Saida |
| uf_do_local_da_saida | `uf_local_saida_saif` | char(2) |  |  | UF do local da Saida |
| inscricao_estadual_do_local_da_saida 🔒 | `iest_local_saida_saif` | char(20) |  |  | Inscricao Estadual do local da Saida |
| valor_do_frete | `valor_frete_saif` | numeric(13) |  |  | Valor do frete |
| aliquota_do_icms_do_frete | `aliq_icms_frete_saif` | numeric(5) |  |  | Aliquota do ICMS do frete |
| valor_do_icms_do_frete | `icms_frete_saif` | numeric(13) |  |  | Valor do ICMS do frete |
| codigo_do_municipio | `codigo_municipio` | integer(4) |  |  | Codigo do municipio |
| razao_social 🔒 | `razao_social_saif` | char(60) |  |  | Razao social |
| endereco 🔒 | `endereco_saif` | char(60) |  |  | Endereco |
| numero | `numero_saif` | integer(4) |  |  | Numero |
| bairro 🔒 | `bairro_saif` | char(60) |  |  | Bairro |
| complemento | `complemento_saif` | char(40) |  |  | Complemento |
| cep 🔒 | `cep_saif` | char(8) |  |  | CEP |
| quantidade | `quantidade_saif` | numeric(15) |  |  | Quantidade |
| especie | `especie_saif` | char(60) |  |  | Especie |
| marca | `marca_saif` | char(60) |  |  | Marca |
| numeracao | `numeracao_saif` | char(60) |  |  | Numeracao |
| peso_liquido | `peso_liquido_saif` | numeric(15) |  |  | Peso liquido |
| peso_bruto | `peso_bruto_saif` | numeric(15) |  |  | Peso bruto |
| tipo_da_inscricao_1_cnpj_2_cpf 🔒 | `tipo_insc_saif` | integer(4) |  | efsaidas_frete_tipo_da_inscricao_1_cnpj_2_c | Tipo da inscrição (1 - CNPJ/2 - CPF) |
| tipo_da_inscricao_1_cnpj_2_cpf_3_cei_4_o 🔒 | `tipo_insc_local_saida_saif` | integer(4) |  | efsaidas_frete_tipo_da_inscricao_1_cnpj_2_c | Tipo da inscrição (1 - CNPJ/2 - CPF/3 - CEI/4 - Outros) - Local da Coleta |
| tipo_insc_local_saif 🔒 | `tipo_insc_local_saif` | integer(4) |  | efsaidas_frete_tipo_da_inscricao_1_cnpj_2_c | Tipo da inscrição (1 - CNPJ/2 - CPF/3 - CEI/4 - Outros) - Local da Entraga |
| codigo_do_municipio_local_da_coleta | `codigo_municipio_local_saida_saif` | integer(4) |  |  | Código do Município - Local da Coleta |
| codigo_do_municipio_local_da_entrega | `codigo_municipio_local_saif` | integer(4) |  |  | Código do Município - Local da Entrega |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `gemunicipio` → `gemunicipio` por `codigo_municipio` = `codigo_municipio`; colunas: `gemunicipio_nome`

**Filtros:** `codigo` (eq/in), `modalidade_do_frete_cif_fob` (eq/in), `transportador_emitente_destinatario_outr` (eq/in), `cnpj_do_transportador` (eq/in), `uf_do_transportador` (eq/in), `inscricao_estadual_do_transportador` (eq/in), `placa1_saif` (eq/in), `uf_placa1_saif` (eq/in), `placa2_saif` (eq/in), `uf_placa2_saif` (eq/in), `placa3_saif` (eq/in), `uf_placa3_saif` (eq/in), `local_recebimento_destinatario_outro` (eq/in), `cnpj_do_local_do_recebimento` (eq/in)

## efsaidas_exportacao

**Notas Fiscais de Saida - Exportacao do PER/DCOMP** — tabela `efsaidas_exportacao` (53 linhas)

Notas Fiscais de Saida - Exportacao do PER/DCOMP. 53 linhas no catálogo; chave: codi_emp, codi_sai.

- **Chave:** `codi_emp, codi_sai`
- **Empresa:** `codi_emp`
- **Período:** `data_declaracao`
- **Ordem padrão:** `data_declaracao desc`, `codi_sai asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 53 linhas, 11 empresa(s).
- Colunas expostas nulas em 100% das linhas (6): data_do_embarque, data_da_declaracao_de_exportacao, data_de_averbacao, data_do_registro_de_exportacao, sequencial_do_siscomex, pais_destino_diferente_cliente.
- natureza_de_exportacao_d_direta_i_indire: todos os valores reais estão no comentário do banco (DD=45, D=8).
- Vínculo eftabela_tipo_conhecimen (eftabela_tipo_conhecimento): 0 de 3 linhas sem registro relacionado (empresa 1359).
- Vínculo eftabela_siscomex (EFTABELA_SISCOMEX): 0 de 3 linhas sem registro relacionado (empresa 1359).
- Vínculo gepais (gepais): 0 de 3 linhas sem registro relacionado (empresa 1359).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| saida | `codi_sai` | integer(4) |  |  | Saida |
| numero_re | `numero_re` | numeric(12) |  |  | Numero RE |
| codigo_do_pais | `cod_pais` | integer(4) |  |  | Codigo do pais |
| numero_do_despacho | `despacho` | varchar(14) |  |  | Numero do despacho |
| data_do_embarque | `embarque` | date(4) |  |  | Data do embarque |
| valor_do_despacho | `valor_despacho` | numeric(13) |  |  | Valor do despacho |
| codigo_da_moeda | `cod_moeda` | integer(4) |  |  | Codigo da moeda |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| data_da_declaracao_de_exportacao | `data_declaracao` | date(4) |  |  | Data da declaracao de exportacao |
| data_de_averbacao | `data_averbacao` | date(4) |  |  | Data de averbacao |
| natureza_de_exportacao_d_direta_i_indire | `natureza_exportacao` | char(2) |  | efsaidas_exportacao_natureza_de | NATUREZA DE EXPORTACAO (D - DIRETA/I - INDIRETA/DS - DIRETA SIMPLIFICADA/IS - INDIRETA SIMPLIFICADA/S - SEM DECLARAÇÃO/DD - E DIRETA/DI - E INDIRETA ) |
| numero_do_embarque | `numero_embarque` | char(19) |  |  | Numero do embarque |
| tipo_do_conhecimento | `tipo` | integer(4) |  |  | Tipo do conhecimento |
| data_do_registro_de_exportacao | `data_registro` | date(4) |  |  | Data do registro de exportacao |
| sequencial_do_siscomex | `i_siscomex` | integer(4) |  |  | Sequencial do SISCOMEX |
| peso_liquido | `peso_liquido` | numeric(18) |  |  | Peso Líquido |
| exportacao_concluida | `exportacao_concluida` | char(1) |  |  | Exportação concluída |
| destino_diferente_cliente | `destino_difere_cliente` | char(1) |  |  | Destino diferente cliente |
| pais_destino_diferente_cliente | `destino_difere_cliente_pais` | integer(4) |  |  | Pais destino diferente cliente |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `eftabela_tipo_conhecimen` → `eftabela_tipo_conhecimento` por `tipo` = `codigo`; colunas: `eftabela_tipo_conhecimen_nome`
- `eftabela_siscomex` → `EFTABELA_SISCOMEX` por `i_siscomex` = `i_siscomex`; colunas: `eftabela_siscomex_nome`
- `gepais` → `gepais` por `destino_difere_cliente_pais` = `codigo_pais`; colunas: `gepais_nome`

**Filtros:** `saida` (eq/in), `data_do_embarque` (entre/gte/lte), `data_da_declaracao_de_exportacao` (entre/gte/lte), `data_de_averbacao` (entre/gte/lte), `data_do_registro_de_exportacao` (entre/gte/lte), `codigo_do_pais` (eq/in), `numero_do_despacho` (eq/in), `codigo_da_moeda` (eq/in), `natureza_de_exportacao_d_direta_i_indire` (eq/in), `numero_do_embarque` (eq/in), `tipo_do_conhecimento` (eq/in), `sequencial_do_siscomex` (eq/in), `exportacao_concluida` (eq/in), `destino_diferente_cliente` (eq/in)

## efsaidas_estadual_mg

**Notas Fiscais de Saídas - Dados estaduais - MG** — tabela `EFSAIDAS_ESTADUAL_MG` (35 linhas)

Notas Fiscais de Saídas - Dados estaduais - MG. 35 linhas no catálogo; chave: CODI_EMP, CODI_SAI.

- **Chave:** `CODI_EMP, CODI_SAI`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 35 linhas, 3 empresa(s).
- tipo_do_transporte_realizado_c_com_conhe: todos os valores reais estão no comentário do banco (S=35).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_da_saida | `codi_sai` | integer(4) |  |  | Código da saída |
| tipo_do_transporte_realizado_c_com_conhe | `tipo_transporte_realizado` | char(1) |  | efsaidas_estadual_mg_tipo_do_tra | Tipo do transporte realizado(C - Com Conhecimento de Transportes - CTRC/S - Sem Conhecimento de Transportes - CTRC) |
| base_de_calculo | `base_calculo_icms_sn` | numeric(13) |  |  | Base de Cálculo |
| aliquota | `aliquota_icms_sn` | numeric(5) |  |  | Alíquota |
| valor | `valor_icms_sn` | numeric(13) |  |  | Valor |

**Filtros:** `codigo_da_saida` (eq/in), `tipo_do_transporte_realizado_c_com_conhe` (eq/in)

## efsaidas_estadual_sc

**Notas Fiscais de Saídas - Dados estaduais - SC** — tabela `EFSAIDAS_ESTADUAL_SC` (34 linhas)

Notas Fiscais de Saídas - Dados estaduais - SC. 34 linhas no catálogo; chave: CODI_EMP, CODI_SAI.

- **Chave:** `CODI_EMP, CODI_SAI`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 34 linhas, 6 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): informacoes_para_dime_tipo_de_atividade.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_da_saida | `codi_sai` | integer(4) |  |  | Código da saída |
| detalhamento_de_outros_do_icms_diferidas | `diferidas` | numeric(13) |  |  | Detalhamento de outros do ICMS - Diferidas |
| detalhamento_de_outros_do_icms_suspencao | `suspensao` | numeric(13) |  |  | Detalhamento de outros do ICMS - Suspenção |
| detalhamento_de_outros_do_icms_substitui | `substituicao_tributaria` | numeric(13) |  |  | Detalhamento de outros do ICMS - Substituição Tributária |
| detalhamento_de_outros_do_icms_outras | `outras` | numeric(13) |  |  | Detalhamento de outros do ICMS - Outras |
| detalhamento_de_outros_do_icms_total | `total_outras` | numeric(13) |  |  | Detalhamento de outros do ICMS - Total |
| informacoes_para_dime_tipo_de_atividade | `sc_tipo_atividade_valor_adicionado_dime` | integer(4) |  |  | Informações para DIME - Tipo de atividade para o rateio do Valor Adicionado |

**Filtros:** `codigo_da_saida` (eq/in), `informacoes_para_dime_tipo_de_atividade` (eq/in)

## efsaidas_estadual_ba

**Notas Fiscais de Saídas - Dados estaduais - BA** — tabela `EFSAIDAS_ESTADUAL_BA` (13 linhas)

Notas Fiscais de Saídas - Dados estaduais - BA. 13 linhas no catálogo; chave: CODI_EMP, CODI_SAI.

- **Chave:** `CODI_EMP, CODI_SAI`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 13 linhas, 3 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): codigo_sequencial_do_municipio.
- Vínculo gemunicipio (gemunicipio): 0 de 3 linhas sem registro relacionado (empresa 9999).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_da_saida | `codi_sai` | integer(4) |  |  | Código da saída |
| tipo_da_operacao | `tipo_operacao` | integer(4) |  |  | Tipo da operação |
| aquisicao_efetuada_com_recursos_convenia | `aquisicao_efetuada_recurso_conveniado` | char(1) |  |  | Aquisição efetuada com recursos conveniados |
| aquisicao_efetuada_recurso_conveniado_ti | `aquisicao_efetuada_recurso_conveniado_tipo` | integer(4) |  |  | Aquisição efetuada com recursos conveniados - Tipo (1/2/3) |
| numero_convenio | `numero_convenio` | varchar(16) |  |  | Número Convênio |
| numero_empenho | `numero_empenho` | varchar(9) |  |  | Número Empenho |
| codigo_sequencial_do_municipio | `codigo_municipio` | integer(4) |  |  | Codigo sequencial do Município |
| base_de_calculo | `base_calculo_icms_sn` | numeric(13) |  |  | Base de Cálculo |
| aliquota | `aliquota_icms_sn` | numeric(5) |  |  | Alíquota |
| valor | `valor_icms_sn` | numeric(13) |  |  | Valor |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `gemunicipio` → `gemunicipio` por `codigo_municipio` = `codigo_municipio`; colunas: `gemunicipio_nome`

**Filtros:** `codigo_da_saida` (eq/in), `tipo_da_operacao` (eq/in), `aquisicao_efetuada_com_recursos_convenia` (eq/in), `aquisicao_efetuada_recurso_conveniado_ti` (eq/in), `numero_convenio` (eq/in), `numero_empenho` (eq/in), `codigo_sequencial_do_municipio` (eq/in)

## efsaidas_nota_devolvida

**Notas Fiscais de Saída - Complementar - Geral - Nota Devolvida** — tabela `EFSAIDAS_NOTA_DEVOLVIDA` (8 linhas)

Notas Fiscais de Saída - Complementar - Geral - Nota Devolvida. 8 linhas no catálogo; chave: CODI_EMP, CODI_SAI, I_NOTA_DEVOLVIDA.

- **Chave:** `CODI_EMP, CODI_SAI, I_NOTA_DEVOLVIDA`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_DEVOLVIDA`
- **Ordem padrão:** `DATA_DEVOLVIDA desc`, `CODI_SAI asc`, `I_NOTA_DEVOLVIDA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 8 linhas, 4 empresa(s), DATA_DEVOLVIDA de 2023-04-27 a 2024-08-22.
- Colunas expostas nulas em 100% das linhas (1): codigo_da_entrada.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_da_saida | `codi_sai` | integer(4) |  |  | Código da Saída |
| sequencial | `i_nota_devolvida` | integer(4) |  |  | Sequencial |
| codigo_da_entrada | `i_entrada_devolvida` | integer(4) |  |  | Código da Entrada |
| data_da_devolucao | `data_devolvida` | date(4) |  |  | Data da Devolução |
| valor_da_nota | `valor_nota` | numeric(13) |  |  | Valor da Nota |
| valor_pago | `valor_pago` | numeric(13) |  |  | Valor Pago |
| valor_em_aberto | `valor_aberto` | numeric(13) |  |  | Valor em Aberto |
| valor_da_devolucao | `valor_devolucao` | numeric(13) |  |  | Valor da Devolução |
| valor_da_deducao | `valor_deducao` | numeric(13) |  |  | Valor da Dedução |
| valor_baixa | `valor_baixa` | numeric(13) |  |  | Valor Baixa |
| valor_ja_devolvido | `valor_ja_devolvido` | numeric(13) |  |  | Valor já Devolvido |
| valor_retencoes | `valor_retencoes` | numeric(13) |  |  | Valor Retenções |

**Filtros:** `codigo_da_saida` (eq/in), `sequencial` (eq/in), `data_da_devolucao` (entre/gte/lte), `codigo_da_entrada` (eq/in)

## efsaidas_valor_presente_provisao

**Notas Fiscais de Saida - Valor Presente Provisao** — tabela `EFSAIDAS_VALOR_PRESENTE_PROVISAO` (5 linhas)

Notas Fiscais de Saida - Valor Presente Provisao. 5 linhas no catálogo; chave: CODI_EMP, CODI_SAI, DATA_PROVISAO.

- **Chave:** `CODI_EMP, CODI_SAI, DATA_PROVISAO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_LANCAMENTO`
- **Ordem padrão:** `DATA_LANCAMENTO desc`, `CODI_SAI asc`, `DATA_PROVISAO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 5 linhas, 2 empresa(s), DATA_LANCAMENTO de 2013-02-28 a 2013-05-31.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_da_nota_de_saida | `codi_sai` | integer(4) |  |  | Codigo da nota de saida |
| data_da_provisao | `data_provisao` | date(4) |  |  | Data da provisao |
| data_do_lancamento | `data_lancamento` | date(4) |  |  | Data do lancamento |
| numero_de_dias | `numero_dias` | integer(4) |  |  | Numero de dias |
| valor_presente | `valor_presente` | numeric(13) |  |  | Valor presente |
| valor_da_taxa | `valor_taxa` | numeric(13) |  |  | Valor da taxa |
| valor_de_juros | `valor_juros` | numeric(13) |  |  | Valor de juros |
| valor_de_devolucao | `valor_devolucao` | numeric(13) |  |  | Valor de devolucao |
| valor_futuro | `valor_futuro` | numeric(13) |  |  | Valor futuro |
| valor_de_saldo_juros | `valor_saldo_juros` | numeric(13) |  |  | Valor de saldo juros |

**Filtros:** `codigo_da_nota_de_saida` (eq/in), `data_da_provisao` (eq/in), `data_do_lancamento` (entre/gte/lte)

## efsaidas_estadual_ro

**Notas Fiscais de Saídas - Dados Estaduais - RO** — tabela `EFSAIDAS_ESTADUAL_RO` (2 linhas)

Notas Fiscais de Saídas - Dados Estaduais - RO. 2 linhas no catálogo; chave: CODI_EMP, CODI_SAI.

- **Chave:** `CODI_EMP, CODI_SAI`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 1 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_sai` | integer(4) |  |  | Codigo |
| transferencia_de_credito_de_icms_numero | `numero_cnd` | numeric(14) |  |  | Transferência de Crédito de ICMS - Número da Certidão Negativa de Tributos Estaduais - CND |
| transferencia_de_credito_de_icms_no_ato | `transferencia_credito_icms_ato_concessorio` | numeric(14) |  |  | Transferência de Crédito de ICMS - Nº Ato Concessório |

**Filtros:** `codigo` (eq/in)

## efsaidas_observacao_fisco

**Notas Fiscais de Saídas - Observação de interesse do fisco** — tabela `EFSAIDAS_OBSERVACAO_FISCO` (1 linhas)

Notas Fiscais de Saídas - Observação de interesse do fisco. 1 linhas no catálogo; chave: CODI_EMP, CODI_SAI, I_SEQUENCIAL_FISCO.

- **Chave:** `CODI_EMP, CODI_SAI, I_SEQUENCIAL_FISCO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `I_SEQUENCIAL_FISCO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): codigo_da_observacao.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_sai` | integer(4) |  |  | Codigo |
| sequencial | `i_sequencial_fisco` | integer(4) |  |  | Sequencial |
| codigo_da_observacao | `i_observacao_fisco` | integer(4) |  |  | Código da Observação |
| descricao_da_observacao | `descricao_fisco` | varchar(300) |  |  | Descrição da Observação |

**Filtros:** `codigo` (eq/in), `sequencial` (eq/in), `codigo_da_observacao` (eq/in), `descricao_da_observacao` (contem/prefixo)

## efsaidas_estadual_ac

**Notas Fiscais de Sa?das - Dados Estaduais - AC** — tabela `EFSAIDAS_ESTADUAL_AC` (1 linhas)

Notas Fiscais de Sa?das - Dados Estaduais - AC. 1 linhas no catálogo; chave: CODI_EMP, CODI_SAI.

- **Chave:** `CODI_EMP, CODI_SAI`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_sai` | integer(4) |  |  | Codigo |
| base_de_calculo | `base_calculo_icms_sn` | numeric(13) |  |  | Base de Calculo |
| aliquota | `aliquota_icms_sn` | numeric(5) |  |  | Aliquota |
| valor | `valor_icms_sn` | numeric(13) |  |  | Valor |

**Filtros:** `codigo` (eq/in)

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

### efsaidas_documentos_fiscais_referenciados_operacao_0_

Confirmado: sim

> Todos os valores observados em EFSAIDAS_DOCUMENTOS_FISCAIS_REFERENCIADOS.OPERACAO_DFSAI estão no comentário do banco (2026-10-18). Distribuição: 1=618.

| Código | Significado |
|---|---|
| 0 | Entrada |
| 1 | Saída |

### efsaidas_documentos_fiscais_referenciados_emitente_0_

Confirmado: sim

> Todos os valores observados em EFSAIDAS_DOCUMENTOS_FISCAIS_REFERENCIADOS.EMITENTE_DFSAI estão no comentário do banco (2026-10-18). Distribuição: 0=618.

| Código | Significado |
|---|---|
| 0 | Emissão própria |
| 1 | Terceiros |

### efsaidas_frete_tipo_da_inscricao_1_cnpj_2_c

Confirmado: parcial

> Coluna efsaidas_frete.TIPO_INSC_LOCAL_SAIF só tem valores nulos na data da medição (2026-10-18): sem evidência para confirmar o comentário do banco.

| Código | Significado |
|---|---|
| 1 | CNPJ |
| 2 | CPF |
| 3 | CEI |
| 4 | Outros |

### efsaidas_exportacao_natureza_de

Confirmado: sim

> Todos os valores observados em efsaidas_exportacao.natureza_exportacao estão no comentário do banco (2026-10-18). Distribuição: DD=45, D=8.

| Código | Significado |
|---|---|
| D | DIRETA |
| I | INDIRETA |
| DS | DIRETA SIMPLIFICADA |
| IS | INDIRETA SIMPLIFICADA |
| S | SEM DECLARAÇÃO |
| DD | E DIRETA |
| DI | E INDIRETA |

### efsaidas_estadual_mg_tipo_do_tra

Confirmado: sim

> Todos os valores observados em EFSAIDAS_ESTADUAL_MG.TIPO_TRANSPORTE_REALIZADO estão no comentário do banco (2026-10-18). Distribuição: S=35.

| Código | Significado |
|---|---|
| C | Com Conhecimento de Transportes - CTRC |
| S | Sem Conhecimento de Transportes - CTRC |

