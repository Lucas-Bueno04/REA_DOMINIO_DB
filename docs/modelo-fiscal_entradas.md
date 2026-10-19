# Modelo — Fiscal - entradas (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/fiscal_entradas.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

26 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [efentradas_info_comp_contrib](#efentradas_info_comp_contrib) | `EFENTRADAS_INFO_COMP_CONTRIB` | 199.625 | medio | empresa |
| [efentradas_efd_reinf](#efentradas_efd_reinf) | `EFENTRADAS_EFD_REINF` | 152.216 | medio | empresa |
| [efentradas_info_comp_fisco](#efentradas_info_comp_fisco) | `EFENTRADAS_INFO_COMP_FISCO` | 51.117 | medio | empresa |
| [efentradas_observacao_contrib](#efentradas_observacao_contrib) | `EFENTRADAS_OBSERVACAO_CONTRIB` | 50.852 | medio | empresa |
| [efentradas_pis_cofins](#efentradas_pis_cofins) | `EFENTRADAS_PIS_COFINS` | 31.339 | medio | empresa |
| [efentradas_pis_cofins_base_piscofins](#efentradas_pis_cofins_base_piscofins) | `EFENTRADAS_PIS_COFINS_BASE_PISCOFINS` | 24.348 | medio | empresa |
| [efentradas_observacao_fisco](#efentradas_observacao_fisco) | `EFENTRADAS_OBSERVACAO_FISCO` | 18.632 | medio | empresa |
| [efentradas_inss_rb](#efentradas_inss_rb) | `EFENTRADAS_INSS_RB` | 16.526 | medio | empresa |
| [efentradas_mva](#efentradas_mva) | `efentradas_mva` | 12.109 | medio | empresa |
| [efentradas_estadual_rj](#efentradas_estadual_rj) | `EFENTRADAS_ESTADUAL_RJ` | 5.110 | pequeno | empresa |
| [efentradas_detalhamento_mg](#efentradas_detalhamento_mg) | `efentradas_detalhamento_mg` | 4.899 | pequeno | empresa |
| [efentradas_estadual_sc](#efentradas_estadual_sc) | `EFENTRADAS_ESTADUAL_SC` | 2.875 | pequeno | empresa |
| [efentradas_irrf_apf](#efentradas_irrf_apf) | `EFENTRADAS_IRRF_APF` | 1.778 | pequeno | empresa |
| [efentradas_info_pag](#efentradas_info_pag) | `EFENTRADAS_INFO_PAG` | 1.701 | pequeno | empresa |
| [efentradas_estadual_mg](#efentradas_estadual_mg) | `EFENTRADAS_ESTADUAL_MG` | 1.586 | pequeno | empresa |
| [efentradas_estadual_ba](#efentradas_estadual_ba) | `EFENTRADAS_ESTADUAL_BA` | 1.308 | pequeno | empresa |
| [efentradas_estadual_ro](#efentradas_estadual_ro) | `EFENTRADAS_ESTADUAL_RO` | 695 | pequeno | empresa |
| [efentradas_estadual_rs](#efentradas_estadual_rs) | `EFENTRADAS_ESTADUAL_RS` | 105 | pequeno | empresa |
| [efentradas_estadual_ac](#efentradas_estadual_ac) | `EFENTRADAS_ESTADUAL_AC` | 82 | pequeno | empresa |
| [efentradas_valor_presente_provisao](#efentradas_valor_presente_provisao) | `EFENTRADAS_VALOR_PRESENTE_PROVISAO` | 69 | pequeno | empresa |
| [efentradas_estadual_sp](#efentradas_estadual_sp) | `EFENTRADAS_ESTADUAL_SP` | 37 | pequeno | empresa |
| [efentradas_difal_nc](#efentradas_difal_nc) | `EFENTRADAS_DIFAL_NC` | 11 | pequeno | empresa |
| [efentradas_nota_devolvida](#efentradas_nota_devolvida) | `EFENTRADAS_NOTA_DEVOLVIDA` | 10 | pequeno | empresa |
| [efentradas_nota_devolvida_csoc_irpj](#efentradas_nota_devolvida_csoc_irpj) | `EFENTRADAS_NOTA_DEVOLVIDA_CSOC_IRPJ` | 10 | pequeno | empresa |
| [efentradas_nota_devolvida_pis_cofins](#efentradas_nota_devolvida_pis_cofins) | `EFENTRADAS_NOTA_DEVOLVIDA_PIS_COFINS` | 8 | pequeno | empresa |
| [efentradas_estadual_pe](#efentradas_estadual_pe) | `EFENTRADAS_ESTADUAL_PE` | 3 | pequeno | empresa |

## efentradas_info_comp_contrib

**Notas Fiscais de Entradas - Informação complementar de interesse do contribuinte** — tabela `EFENTRADAS_INFO_COMP_CONTRIB` (199.625 linhas)

Notas Fiscais de Entradas - Informação complementar de interesse do contribuinte. 199.625 linhas no catálogo; chave: CODI_EMP, CODI_ENT, I_SEQUENCIAL_CONTRIB.

- **Chave:** `CODI_EMP, CODI_ENT, I_SEQUENCIAL_CONTRIB`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `I_SEQUENCIAL_CONTRIB asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 200.887 linhas, 208 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): codigo_da_informacao_complementar.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_ent` | integer(4) |  |  | Codigo |
| sequencial | `i_sequencial_contrib` | integer(4) |  |  | Sequencial |
| codigo_da_informacao_complementar | `i_info_comp_contrib` | integer(4) |  |  | Código da Informação Complementar |
| descricao_da_informacao_complementar | `descricao_contrib` | varchar(1000) |  |  | Descrição da Informação Complementar |

**Filtros:** `codigo` (eq/in), `sequencial` (eq/in), `codigo_da_informacao_complementar` (eq/in), `descricao_da_informacao_complementar` (contem/prefixo)

## efentradas_efd_reinf

**Notas Fiscais de Entrada - EFD Reinf** — tabela `EFENTRADAS_EFD_REINF` (152.216 linhas)

Notas Fiscais de Entrada - EFD Reinf. 152.216 linhas no catálogo; chave: CODI_EMP, CODI_ENT.

- **Chave:** `CODI_EMP, CODI_ENT`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 152.254 linhas, 827 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_ent` | integer(4) |  |  | Código |
| tipo_de_servico | `tipo_servico` | varchar(10) |  |  | Tipo de serviço |
| possui_processo_administrativo_judicial | `possui_paj_ent` | char(1) |  |  | Possui Processo Administrativo Judicial |
| indicativo_de_prestacao_de_servico | `indicativo_prestacao_servicos` | integer(4) |  |  | Indicativo de Prestação de Serviço |

**Filtros:** `codigo` (eq/in), `tipo_de_servico` (eq/in), `possui_processo_administrativo_judicial` (eq/in)

## efentradas_info_comp_fisco

**Notas Fiscais de Entradas - Informação complementar de interesse do fisco** — tabela `EFENTRADAS_INFO_COMP_FISCO` (51.117 linhas)

Notas Fiscais de Entradas - Informação complementar de interesse do fisco. 51.117 linhas no catálogo; chave: CODI_EMP, CODI_ENT, I_SEQUENCIAL_FISCO.

- **Chave:** `CODI_EMP, CODI_ENT, I_SEQUENCIAL_FISCO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `I_SEQUENCIAL_FISCO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 51.724 linhas, 157 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): codigo_da_informacao_complementar.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_ent` | integer(4) |  |  | Codigo |
| sequencial | `i_sequencial_fisco` | integer(4) |  |  | Sequencial |
| codigo_da_informacao_complementar | `i_info_comp_fisco` | integer(4) |  |  | Código da Informação Complementar |
| descricao_da_informacao_complementar | `descricao_fisco` | varchar(1000) |  |  | Descrição da Informação Complementar |

**Filtros:** `codigo` (eq/in), `sequencial` (eq/in), `codigo_da_informacao_complementar` (eq/in), `descricao_da_informacao_complementar` (contem/prefixo)

## efentradas_observacao_contrib

**Notas Fiscais de Entradas - Obseração de interesse do contribuinte** — tabela `EFENTRADAS_OBSERVACAO_CONTRIB` (50.852 linhas)

Notas Fiscais de Entradas - Obseração de interesse do contribuinte. 50.852 linhas no catálogo; chave: CODI_EMP, CODI_ENT, I_SEQUENCIAL_CONTRIB.

- **Chave:** `CODI_EMP, CODI_ENT, I_SEQUENCIAL_CONTRIB`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `I_SEQUENCIAL_CONTRIB asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 50.852 linhas, 142 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): codigo_da_observacao.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_ent` | integer(4) |  |  | Codigo |
| sequencial | `i_sequencial_contrib` | integer(4) |  |  | Sequencial |
| codigo_da_observacao | `i_observacao_contrib` | integer(4) |  |  | Código da Observação |
| descricao_da_observacao | `descricao_contrib` | varchar(300) |  |  | Descrição da Observação |

**Filtros:** `codigo` (eq/in), `sequencial` (eq/in), `codigo_da_observacao` (eq/in), `descricao_da_observacao` (contem/prefixo)

## efentradas_pis_cofins

**Notas Fiscais de Entrada - PIS/COFINS** — tabela `EFENTRADAS_PIS_COFINS` (31.339 linhas)

Notas Fiscais de Entrada - PIS/COFINS. 31.339 linhas no catálogo; chave: CODI_EMP, CODI_ENT, I_PIS_COFINS.

- **Chave:** `CODI_EMP, CODI_ENT, I_PIS_COFINS`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `I_PIS_COFINS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 32.079 linhas, 45 empresa(s).
- Colunas expostas nulas em 100% das linhas (5): numero_do_processo_ou_ato_concessorio, origem_1_justica_federal_2_secretaria_da, codigo_sequencial_do_recolhimento_do_pis, codigo_sequencial_do_recolhimento_do_cof, codigo_do_beneficio_dirbi.
- origem_1_justica_federal_2_secretaria_da: coluna sem nenhum valor preenchido; o domínio do comentário do banco não pôde ser verificado.
- aproveitar_credito_proporcional_n_credit: todos os valores reais estão no comentário do banco (N=32.079).
- Vínculo eftabela_natureza_receit (EFTABELA_NATUREZA_RECEITA): 0 de 19 linhas sem registro relacionado (empresa 1077).
- Vínculo eftabela_codigo_base_cal (EFTABELA_CODIGO_BASE_CALCULO_CREDITO): 0 de 19 linhas sem registro relacionado (empresa 1077).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_da_entrada | `codi_ent` | integer(4) |  |  | Código da entrada |
| sequencial | `i_pis_cofins` | integer(4) |  |  | Sequencial |
| cst | `cst` | integer(4) |  |  | CST |
| base_do_credito | `base_credito` | integer(4) |  |  | Base do crédito |
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
| natureza_do_frete | `natureza_frete` | integer(4) |  |  | Natureza do frete |
| numero_do_processo_ou_ato_concessorio | `nro_processo` | char(20) |  |  | Número do processo ou ato concessório |
| origem_1_justica_federal_2_secretaria_da | `origem` | tinyint(1) |  | efentradas_pis_cofins_origem_1_justi | Origem (1=Justiça Federal/ 2=Secretaria da Receita Federal do Brasil/ 9=Outros) |
| aproveitar_credito_proporcional_n_credit | `aproveitar_credito_proporcional` | char(1) |  | efentradas_pis_cofins_aproveitar_cre | Aproveitar crédito proporcional(N=Crédito vinculado somente as receitas Não Cumulativas/ S=Crédito vinculado as receitas Cumulativas e Não Cumulativas) |
| vinculo_do_credito | `vinculo_credito` | integer(4) |  |  | Vínculo do Crédito |
| percentual_reducao_base_calculo | `percentual_reducao_bc` | numeric(5) |  |  | Percentual Redução Base Cálculo |
| codigo_sequencial_do_recolhimento_do_pis | `i_recolhimento_pis` | integer(4) |  |  | Código Sequencial do Recolhimento do PIS |
| codigo_do_recolhimento_do_pis | `codigo_recolhimento_pis` | char(6) |  |  | Código do Recolhimento do PIS |
| codigo_sequencial_do_recolhimento_do_cof | `i_recolhimento_cofins` | integer(4) |  |  | Código Sequencial do Recolhimento do COFINS |
| codigo_do_recolhimento_do_cofins | `codigo_recolhimento_cofins` | char(6) |  |  | Código do Recolhimento do COFINS |
| codigo_do_beneficio_dirbi | `codigo_beneficio_dirbi` | integer(4) |  |  | Código do Benefício DIRBI |
| calcular_reducao_linear_lc224 | `calcular_reducao_linear_lc224` | char(1) |  |  | Calcular redução conf. LC 224/2025 |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `eftabela_natureza_receit` → `EFTABELA_NATUREZA_RECEITA` por `natureza_receita` = `codigo` e `cst` = `codigo_cst`; colunas: `eftabela_natureza_receit_nome`
- `eftabela_codigo_base_cal` → `EFTABELA_CODIGO_BASE_CALCULO_CREDITO` por `base_credito` = `codigo`; colunas: `eftabela_codigo_base_cal_nome`

**Filtros:** `codigo_da_entrada` (eq/in), `sequencial` (eq/in), `numero_do_processo_ou_ato_concessorio` (eq/in), `aproveitar_credito_proporcional_n_credit` (eq/in), `codigo_sequencial_do_recolhimento_do_pis` (eq/in), `codigo_do_recolhimento_do_pis` (eq/in), `codigo_sequencial_do_recolhimento_do_cof` (eq/in), `codigo_do_recolhimento_do_cofins` (eq/in), `codigo_do_beneficio_dirbi` (eq/in), `calcular_reducao_linear_lc224` (eq/in)

## efentradas_pis_cofins_base_piscofins

**Notas Fiscais de Entrada - PIS/COFINS - Base PIS COFINS** — tabela `EFENTRADAS_PIS_COFINS_BASE_PISCOFINS` (24.348 linhas)

Notas Fiscais de Entrada - PIS/COFINS - Base PIS COFINS. 24.348 linhas no catálogo; chave: CODI_EMP, CODI_ENT, I_PIS_COFINS, CODI_IMP, TIPO_CREDITO.

- **Chave:** `CODI_EMP, CODI_ENT, I_PIS_COFINS, CODI_IMP, TIPO_CREDITO`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `CODI_ENT asc`, `I_PIS_COFINS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 24.348 linhas, 12 empresa(s), COMPETENCIA de 2021-11-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_da_entrada | `codi_ent` | integer(4) |  |  | Código da entrada |
| sequencial | `i_pis_cofins` | integer(4) |  |  | Sequencial |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| tipo_de_credito | `tipo_credito` | integer(4) |  |  | Tipo de crédito |
| receita_cumulativa | `receita_cumulativa` | numeric(13) |  |  | Receita cumulativa |
| receita_nao_cumulativa | `receita_nao_cumulativa` | numeric(13) |  |  | Receita não cumulativa |
| interna_tributada | `interna_tributada` | numeric(13) |  |  | Interna tributada |
| interna_nao_tributada | `interna_nao_tributada` | numeric(13) |  |  | Interna não tributada |
| externa | `externa` | numeric(13) |  |  | Externa |
| competencia | `competencia` | date(4) |  |  | Competencia |

**Filtros:** `codigo_da_entrada` (eq/in), `sequencial` (eq/in), `imposto` (eq/in), `tipo_de_credito` (eq/in), `competencia` (entre/gte/lte)

## efentradas_observacao_fisco

**Notas Fiscais de Entradas - Observação de interesse do fisco** — tabela `EFENTRADAS_OBSERVACAO_FISCO` (18.632 linhas)

Notas Fiscais de Entradas - Observação de interesse do fisco. 18.632 linhas no catálogo; chave: CODI_EMP, CODI_ENT, I_SEQUENCIAL_FISCO.

- **Chave:** `CODI_EMP, CODI_ENT, I_SEQUENCIAL_FISCO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `I_SEQUENCIAL_FISCO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 18.632 linhas, 245 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): codigo_da_observacao.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_ent` | integer(4) |  |  | Codigo |
| sequencial | `i_sequencial_fisco` | integer(4) |  |  | Sequencial |
| codigo_da_observacao | `i_observacao_fisco` | integer(4) |  |  | Código da Observação |
| descricao_da_observacao | `descricao_fisco` | varchar(300) |  |  | Descrição da Observação |

**Filtros:** `codigo` (eq/in), `sequencial` (eq/in), `codigo_da_observacao` (eq/in), `descricao_da_observacao` (contem/prefixo)

## efentradas_inss_rb

**Notas Fiscais de Entradas - INSS Receita Bruta** — tabela `EFENTRADAS_INSS_RB` (16.526 linhas)

Notas Fiscais de Entradas - INSS Receita Bruta. 16.526 linhas no catálogo; chave: CODI_EMP, CODI_ENT.

- **Chave:** `CODI_EMP, CODI_ENT`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 16.536 linhas, 593 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_ent` | integer(4) |  |  | Codigo |
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

## efentradas_mva

**Notas Fiscais de Entradas - MVA** — tabela `efentradas_mva` (12.109 linhas)

Notas Fiscais de Entradas - MVA. 12.109 linhas no catálogo; chave: codi_emp, codi_ent, codi_imp, sequencial.

- **Chave:** `codi_emp, codi_ent, codi_imp, sequencial`
- **Empresa:** `codi_emp`
- **Período:** `—`
- **Ordem padrão:** `codi_ent asc`, `codi_imp asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 12.109 linhas, 69 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| nota | `codi_ent` | integer(4) |  |  | Nota |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| aliquota | `aliquota` | numeric(5) |  |  | Aliquota |
| valor_do_produto | `valor_produto` | numeric(13) |  |  | Valor do produto |
| percentual_mva | `mva` | numeric(5) |  |  | Percentual MVA |
| percentual_de_reducao_do_mva | `reducao_mva` | numeric(7) |  |  | Percentual de reducao do MVA |
| valor_contabil | `valor_contabil` | numeric(13) |  |  | Valor Contábil |
| percentual_mva_fidelidade | `mva_fidelidade` | numeric(5) |  |  | Percentual MVA Fidelidade |

**Filtros:** `nota` (eq/in), `imposto` (eq/in), `sequencial` (eq/in)

## efentradas_estadual_rj

**Notas Fiscais de Entradas - Dados estaduais - RJ** — tabela `EFENTRADAS_ESTADUAL_RJ` (5.110 linhas)

Notas Fiscais de Entradas - Dados estaduais - RJ. 5.110 linhas no catálogo; chave: CODI_EMP, CODI_ENT.

- **Chave:** `CODI_EMP, CODI_ENT`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 5.111 linhas, 26 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): outros_beneficios_para_informacao_no_dub.
- Vínculo eftabela_rj_dub_icms (EFTABELA_RJ_DUB_ICMS): 41 de 41 linhas sem registro relacionado (empresa 1328).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_da_entrada | `codi_ent` | integer(4) |  |  | Código da entrada |
| codigo_do_valor_adicionado_para_a_declan | `codigo_valor_adicionado` | integer(4) |  |  | Código do valor adicionado para a DECLAN-IPM |
| valor_adicionado_para_a_declan_ipm | `valor_adicionado` | numeric(13) |  |  | Valor adicionado para a DECLAN-IPM |
| outros_beneficios_para_informacao_no_dub | `i_dub_icms` | integer(4) |  |  | Outros benefícios para informação no DUB-ICMS - Código |
| dub_icms_valor_operacao | `dub_icms_valor_operacao` | numeric(13) |  |  | Outros benefícios para informação no DUB-ICMS - Valor da operação |
| dub_icms_aliquota | `dub_icms_aliquota` | numeric(5) |  |  | Outros benefícios para informação no DUB-ICMS - Alíquota |
| dub_icms_valor_icms_nao_recolhido | `dub_icms_valor_icms_nao_recolhido` | numeric(13) |  |  | Outros benefícios para informação no DUB-ICMS - Valor do ICMS não recolhido |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `eftabela_rj_dub_icms` → `EFTABELA_RJ_DUB_ICMS` por `codi_emp` = `codi_emp` e `i_dub_icms` = `i_dub_icms`; colunas: `eftabela_rj_dub_icms_nome`

**Filtros:** `codigo_da_entrada` (eq/in), `codigo_do_valor_adicionado_para_a_declan` (eq/in), `outros_beneficios_para_informacao_no_dub` (eq/in)

## efentradas_detalhamento_mg

**Notas Fiscais de Entradas - Detalhamentos - MG** — tabela `efentradas_detalhamento_mg` (4.899 linhas)

Notas Fiscais de Entradas - Detalhamentos - MG. 4.899 linhas no catálogo; chave: codi_emp, codi_ent.

- **Chave:** `codi_emp, codi_ent`
- **Empresa:** `codi_emp`
- **Período:** `—`
- **Ordem padrão:** `codi_ent asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4.899 linhas, 15 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| nota | `codi_ent` | integer(4) |  |  | Nota |
| imposto_sem_aproveitamento_de_credito | `sem_aproveitamento` | numeric(13) |  |  | Imposto sem aproveitamento de credito |
| isentas | `isentas` | numeric(13) |  |  | Isentas |
| nao_tributadas | `nao_tributadas` | numeric(13) |  |  | Nao tributadas |
| parcela_de_base_de_calculo_reduzida | `base_reduzida` | numeric(13) |  |  | Parcela de base de calculo reduzida |
| diferidas | `diferidas` | numeric(13) |  |  | Diferidas |
| suspensas | `suspensas` | numeric(13) |  |  | Suspensas |
| substituicao_tributaria | `substituicao` | numeric(13) |  |  | Substituicao tributaria |
| outras | `outras` | numeric(13) |  |  | Outras |
| gerar_no_informativo_dapi | `gerar_no_informativo_dapi` | char(1) |  |  | Gerar no informativo DAPI |
| gerar_no_informativo_dapi_mg | `gerar_no_informativo_dapi_operacao` | char(1) |  |  | Gerar no informativo DAPI MG |

**Filtros:** `nota` (eq/in), `gerar_no_informativo_dapi` (eq/in), `gerar_no_informativo_dapi_mg` (eq/in)

## efentradas_estadual_sc

**Notas Fiscais de Entradas - Dados estaduais - SC** — tabela `EFENTRADAS_ESTADUAL_SC` (2.875 linhas)

Notas Fiscais de Entradas - Dados estaduais - SC. 2.875 linhas no catálogo; chave: CODI_EMP, CODI_ENT.

- **Chave:** `CODI_EMP, CODI_ENT`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2.876 linhas, 43 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): tipo_de_atividade_para_rateio_do_valor_a.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da Empresa |
| codigo_da_nota | `codi_ent` | integer(4) |  |  | Codigo da Nota |
| tipo_de_atividade_para_rateio_do_valor_a | `sc_tipo_atividade_rateio_valor_adicionado_dime` | integer(4) |  |  | Tipo de atividade para rateio do Valor Adicionado |

**Filtros:** `codigo_da_nota` (eq/in), `tipo_de_atividade_para_rateio_do_valor_a` (eq/in)

## efentradas_irrf_apf

**Notas Fiscais de Entrada - Dados IRRF** — tabela `EFENTRADAS_IRRF_APF` (1.778 linhas)

Notas Fiscais de Entrada - Dados IRRF. 1.778 linhas no catálogo; chave: CODI_EMP, CODI_ENT, CODI_IMP.

- **Chave:** `CODI_EMP, CODI_ENT, CODI_IMP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `CODI_IMP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.782 linhas, 40 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_nota | `codi_ent` | integer(4) |  |  | Codigo Nota |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| tipo_de_deducao_aplicada_na_base_de_calc | `tipo_deducao_base_calculo` | integer(4) |  |  | Tipo de dedução aplicada na base de calculo |
| valor_da_deducao | `valor_deducao_base_calculo` | numeric(13) |  |  | Valor da dedução |

**Filtros:** `codigo_nota` (eq/in), `imposto` (eq/in), `tipo_de_deducao_aplicada_na_base_de_calc` (eq/in)

## efentradas_info_pag

**Notas Fiscais de Entradas - Informação Pagamento** — tabela `EFENTRADAS_INFO_PAG` (1.701 linhas)

Notas Fiscais de Entradas - Informação Pagamento. 1.701 linhas no catálogo; chave: CODI_EMP, CODI_ENT, I_SEQUENCIAL.

- **Chave:** `CODI_EMP, CODI_ENT, I_SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `I_SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2.345 linhas, 58 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_ent` | integer(4) |  |  | Codigo |
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

## efentradas_estadual_mg

**Notas Fiscais de Entradas - Dados Estaduais - MG** — tabela `EFENTRADAS_ESTADUAL_MG` (1.586 linhas)

Notas Fiscais de Entradas - Dados Estaduais - MG. 1.586 linhas no catálogo; chave: CODI_EMP, CODI_ENT.

- **Chave:** `CODI_EMP, CODI_ENT`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.586 linhas, 22 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_ent` | integer(4) |  |  | Codigo |
| base_de_calculo | `base_calculo_icms_sn` | numeric(13) |  |  | Base de Cálculo |
| aliquota | `aliquota_icms_sn` | numeric(5) |  |  | Alíquota |
| valor | `valor_icms_sn` | numeric(13) |  |  | Valor |

**Filtros:** `codigo` (eq/in)

## efentradas_estadual_ba

**Notas Fiscais de Entradas - Dados estaduais - BA** — tabela `EFENTRADAS_ESTADUAL_BA` (1.308 linhas)

Notas Fiscais de Entradas - Dados estaduais - BA. 1.308 linhas no catálogo; chave: CODI_EMP, CODI_ENT.

- **Chave:** `CODI_EMP, CODI_ENT`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_EMISSAO_MDFE`
- **Ordem padrão:** `DATA_EMISSAO_MDFE desc`, `CODI_ENT asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.309 linhas, 15 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): data_de_emissao_mdf_e.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_da_entrada | `codi_ent` | integer(4) |  |  | Código da entrada |
| tipo_da_operacao | `tipo_operacao` | integer(4) |  |  | Tipo da operação |
| base_de_calculo | `base_calculo_icms_sn` | numeric(13) |  |  | Base de Cálculo |
| aliquota | `aliquota_icms_sn` | numeric(5) |  |  | Alíquota |
| valor | `valor_icms_sn` | numeric(13) |  |  | Valor |
| data_de_emissao_mdf_e | `data_emissao_mdfe` | date(4) |  |  | Data de emissão MDF-e |

**Filtros:** `codigo_da_entrada` (eq/in), `data_de_emissao_mdf_e` (entre/gte/lte), `tipo_da_operacao` (eq/in)

## efentradas_estadual_ro

**Notas Fiscais de Entradas - Dados Estaduais - RO** — tabela `EFENTRADAS_ESTADUAL_RO` (695 linhas)

Notas Fiscais de Entradas - Dados Estaduais - RO. 695 linhas no catálogo; chave: CODI_EMP, CODI_ENT.

- **Chave:** `CODI_EMP, CODI_ENT`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_LEVANTAMENTO`
- **Ordem padrão:** `DATA_LEVANTAMENTO desc`, `CODI_ENT asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 695 linhas, 2 empresa(s).
- Colunas expostas nulas em 100% das linhas (2): codigo_do_lancamento_do_estoque, data_do_levantamento_do_estoque.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da Empresa |
| codigo_da_nota_de_entrada | `codi_ent` | integer(4) |  |  | Código da Nota de Entrada |
| codigo_do_lancamento_do_estoque | `i_estoque` | integer(4) |  |  | Código do Lançamento do Estoque |
| data_do_levantamento_do_estoque | `data_levantamento` | date(4) |  |  | Data do Levantamento do Estoque |
| valor_total_do_icms_sobre_o_estoque | `valor_total_icms_sobre_estoque` | numeric(13) |  |  | Valor total do ICMS sobre o Estoque |
| valor_da_parcela_do_credito_do_estoque | `valor_parcela_credito` | numeric(13) |  |  | Valor da parcela do crédito do Estoque |
| base_de_calculo_icms_simples_nacional | `base_calculo_icms_sn` | numeric(13) |  |  | Base de Cálculo ICMS Simples Nacional |
| aliquota_icms_simples_nacional | `aliquota_icms_sn` | numeric(5) |  |  | Alíquota ICMS Simples Nacional |
| valor_icms_simples_nacional | `valor_icms_sn` | numeric(13) |  |  | Valor ICMS Simples Nacional |

**Filtros:** `codigo_da_nota_de_entrada` (eq/in), `data_do_levantamento_do_estoque` (entre/gte/lte), `codigo_do_lancamento_do_estoque` (eq/in)

## efentradas_estadual_rs

**Notas Fiscais de Entradas - Dados estaduais - RS** — tabela `EFENTRADAS_ESTADUAL_RS` (105 linhas)

Notas Fiscais de Entradas - Dados estaduais - RS. 105 linhas no catálogo; chave: CODI_EMP, CODI_ENT.

- **Chave:** `CODI_EMP, CODI_ENT`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_LEVANTAMENTO`
- **Ordem padrão:** `DATA_LEVANTAMENTO desc`, `CODI_ENT asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 106 linhas, 5 empresa(s).
- Colunas expostas nulas em 100% das linhas (5): sequencial, dispositivo_do_credito_presumido, codigo_do_lancamento, data_do_levantamento, visto_eletronico.
- Vínculo eftabela_rs_utilizacao_c (EFTABELA_RS_UTILIZACAO_CREDITO): 0 de 21 linhas sem registro relacionado (empresa 1316).
- Vínculo eftabela_dispositivo_cre (EFTABELA_DISPOSITIVO_CREDITO_PRESUMIDO_RS): 0 de 21 linhas sem registro relacionado (empresa 1316).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_ent` | integer(4) |  |  | Codigo |
| sequencial | `i_utilizacao_credito` | integer(4) |  |  | Sequencial |
| dispositivo_do_credito_presumido | `dispositivo_credito_presumido` | integer(4) |  |  | Dispositivo do crédito presumido |
| limitar_o_aproveitamento_do_credito_de_i | `limitar_credito_icms` | char(1) |  |  | Limitar o aproveitamento do crédito de ICMS conforme Art.37 2 do Livro I RICMS/RS |
| percentual_de_limitar_o_aproveitamento_d | `limitar_credito_icms_percentual` | integer(4) |  |  | Percentual de limitar o aproveitamento do crédito de ICMS conforme Art.37 2 do Livro I RICMS/RS |
| chp | `chp` | varchar(12) |  |  | CHP |
| codigo_do_lancamento | `i_estoque` | integer(4) |  |  | Código do lançamento |
| data_do_levantamento | `data_levantamento` | date(4) |  |  | Data do levantamento |
| valor_total_do_icms_sobre_estoque | `valor_total_icms_sobre_estoque` | numeric(13) |  |  | Valor total do ICMS sobre estoque |
| valor_da_parcela_do_credito | `valor_parcela_credito` | numeric(13) |  |  | Valor da parcela do crédito |
| valor_do_icms_destacado_a_maior | `valor_icms_destacado_a_maior` | numeric(13) |  |  | Valor do ICMS destacado a maior |
| valor_do_icms_estorno_de_debito_decorren | `valor_icms_estorno_debito_devolucao_material_uso_consumo` | numeric(13) |  |  | Valor do ICMS Estorno de débito decorrente a devolução de materiais adquiridos para uso e consumo |
| visto_eletronico | `visto_eletronico` | varchar(12) |  |  | Visto Eletronico |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `eftabela_rs_utilizacao_c` → `EFTABELA_RS_UTILIZACAO_CREDITO` por `i_utilizacao_credito` = `i_utilizacao_credito`; colunas: `eftabela_rs_utilizacao_c_nome`
- `eftabela_dispositivo_cre` → `EFTABELA_DISPOSITIVO_CREDITO_PRESUMIDO_RS` por `dispositivo_credito_presumido` = `i_dispositivo`; colunas: `eftabela_dispositivo_cre_nome`

**Filtros:** `codigo` (eq/in), `data_do_levantamento` (entre/gte/lte), `sequencial` (eq/in), `limitar_o_aproveitamento_do_credito_de_i` (eq/in), `chp` (eq/in), `codigo_do_lancamento` (eq/in), `visto_eletronico` (eq/in)

## efentradas_estadual_ac

**Notas Fiscais de Entradas - Dados Estaduais - AC** — tabela `EFENTRADAS_ESTADUAL_AC` (82 linhas)

Notas Fiscais de Entradas - Dados Estaduais - AC. 82 linhas no catálogo; chave: CODI_EMP, CODI_ENT.

- **Chave:** `CODI_EMP, CODI_ENT`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 82 linhas, 1 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_ent` | integer(4) |  |  | Codigo |
| base_de_calculo | `base_calculo_icms_sn` | numeric(13) |  |  | Base de Calculo |
| aliquota | `aliquota_icms_sn` | numeric(5) |  |  | Aliquota |
| valor | `valor_icms_sn` | numeric(13) |  |  | Valor |

**Filtros:** `codigo` (eq/in)

## efentradas_valor_presente_provisao

**Notas Fiscais de Entrada - Valor Presente Provisao** — tabela `EFENTRADAS_VALOR_PRESENTE_PROVISAO` (69 linhas)

Notas Fiscais de Entrada - Valor Presente Provisao. 69 linhas no catálogo; chave: CODI_EMP, CODI_ENT, DATA_PROVISAO.

- **Chave:** `CODI_EMP, CODI_ENT, DATA_PROVISAO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_LANCAMENTO`
- **Ordem padrão:** `DATA_LANCAMENTO desc`, `CODI_ENT asc`, `DATA_PROVISAO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 69 linhas, 11 empresa(s), DATA_LANCAMENTO de 2013-01-31 a 2017-08-31.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_da_nota_de_entrada | `codi_ent` | integer(4) |  |  | Codigo da nota de entrada |
| data_da_provisao | `data_provisao` | date(4) |  |  | Data da provisao |
| data_do_lancamento | `data_lancamento` | date(4) |  |  | Data do lancamento |
| numero_de_dias | `numero_dias` | integer(4) |  |  | Numero de dias |
| valor_presente | `valor_presente` | numeric(13) |  |  | Valor presente |
| valor_da_taxa | `valor_taxa` | numeric(13) |  |  | Valor da taxa |
| valor_de_juros | `valor_juros` | numeric(13) |  |  | Valor de juros |
| valor_de_devolucao | `valor_devolucao` | numeric(13) |  |  | Valor de devolucao |
| valor_futuro | `valor_futuro` | numeric(13) |  |  | Valor futuro |
| valor_de_saldo_juros | `valor_saldo_juros` | numeric(13) |  |  | Valor de saldo juros |

**Filtros:** `codigo_da_nota_de_entrada` (eq/in), `data_da_provisao` (eq/in), `data_do_lancamento` (entre/gte/lte)

## efentradas_estadual_sp

**Notas Fiscais de Entradas - Dados Estaduais - SP** — tabela `EFENTRADAS_ESTADUAL_SP` (37 linhas)

Notas Fiscais de Entradas - Dados Estaduais - SP. 37 linhas no catálogo; chave: CODI_EMP, CODI_ENT.

- **Chave:** `CODI_EMP, CODI_ENT`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 37 linhas, 1 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_ent` | integer(4) |  |  | Código |
| base_de_calculo | `base_calculo_icms_sn` | numeric(13) |  |  | Base de Cálculo |
| aliquota | `aliquota_icms_sn` | numeric(5) |  |  | Alíquota |
| valor | `valor_icms_sn` | numeric(13) |  |  | Valor |
| valor_dispensado_de_escrituracao_dipam | `valor_dispensado_dipam` | numeric(13) |  |  | Valor dispensado de Escrituração DIPAM |

**Filtros:** `codigo` (eq/in)

## efentradas_difal_nc

**Notas Fiscais de Entrada - DIFAL NC** — tabela `EFENTRADAS_DIFAL_NC` (11 linhas)

Notas Fiscais de Entrada - DIFAL NC. 11 linhas no catálogo; chave: CODI_EMP, CODI_ENT.

- **Chave:** `CODI_EMP, CODI_ENT`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 11 linhas, 1 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_ent` | integer(4) |  |  | Código |
| base_calculo | `base_calculo` | numeric(15) |  |  | Base Cálculo |
| aliquota | `aliquota` | numeric(5) |  |  | Alíquota |
| valor_uf_origem | `valor_uf_origem` | numeric(15) |  |  | Valor UF Origem |
| valor_uf_destino | `valor_uf_destino` | numeric(15) |  |  | Valor UF Destino |
| valor_total | `valor_total` | numeric(15) |  |  | Valor Total |
| valor_fcp | `valor_fcp` | numeric(15) |  |  | Valor FCP |

**Filtros:** `codigo` (eq/in)

## efentradas_nota_devolvida

**Notas Fiscais de Entrada - Complementar - Geral - Nota Devolvida** — tabela `EFENTRADAS_NOTA_DEVOLVIDA` (10 linhas)

Notas Fiscais de Entrada - Complementar - Geral - Nota Devolvida. 10 linhas no catálogo; chave: CODI_EMP, CODI_ENT, I_NOTA_DEVOLVIDA.

- **Chave:** `CODI_EMP, CODI_ENT, I_NOTA_DEVOLVIDA`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_DEVOLVIDA`
- **Ordem padrão:** `DATA_DEVOLVIDA desc`, `CODI_ENT asc`, `I_NOTA_DEVOLVIDA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 10 linhas, 2 empresa(s), DATA_DEVOLVIDA de 2023-01-31 a 2025-03-17.
- Colunas expostas nulas em 100% das linhas (3): codigo_da_reducaoz, codigo_do_cupom_fiscal, codigo_da_cfe.
- tipo_do_documento_fiscal_s_saida_c_cupom: todos os valores reais estão no comentário do banco (S=8, nulo=2).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_da_entrada | `codi_ent` | integer(4) |  |  | Código da Entrada |
| sequencial | `i_nota_devolvida` | integer(4) |  |  | Sequencial |
| tipo_do_documento_fiscal_s_saida_c_cupom | `tipo_doc_devolvido` | char(1) |  | efentradas_nota_devolvida_tipo_do_docu | TIPO DO DOCUMENTO FISCAL(S-SAÍDA/C-CUPOM FISCAL/F-CFE/Z-REDUÇÃO Z 2D) |
| codigo_da_saida | `i_saida_devolvida` | integer(4) |  |  | Código da Saída |
| codigo_da_reducaoz | `i_reducao_devolvida` | integer(4) |  |  | Código da ReduçãoZ |
| codigo_do_cupom_fiscal | `i_cupom_devolvido` | integer(4) |  |  | Código do Cupom Fiscal |
| data_da_devolucao | `data_devolvida` | date(4) |  |  | Data da Devolução |
| valor_da_nota | `valor_nota` | numeric(13) |  |  | Valor da Nota |
| valor_pago | `valor_pago` | numeric(13) |  |  | Valor Pago |
| valor_em_aberto | `valor_aberto` | numeric(13) |  |  | Valor em Aberto |
| valor_da_devolucao | `valor_devolucao` | numeric(13) |  |  | Valor da Devolução |
| valor_da_deducao | `valor_deducao` | numeric(13) |  |  | Valor da Dedução |
| valor_baixa | `valor_baixa` | numeric(13) |  |  | Valor Baixa |
| valor_ja_devolvido | `valor_ja_devolvido` | numeric(13) |  |  | Valor já Devolvido |
| valor_retencoes | `valor_retencoes` | numeric(13) |  |  | Valor Retenções |
| codigo_da_cfe | `i_cfe_devolvida` | integer(4) |  |  | Código da CFE |

**Filtros:** `codigo_da_entrada` (eq/in), `sequencial` (eq/in), `data_da_devolucao` (entre/gte/lte), `tipo_do_documento_fiscal_s_saida_c_cupom` (eq/in), `codigo_da_saida` (eq/in), `codigo_da_reducaoz` (eq/in), `codigo_do_cupom_fiscal` (eq/in), `codigo_da_cfe` (eq/in)

## efentradas_nota_devolvida_csoc_irpj

**Notas Fiscais de Entrada - Complementar - Geral - Nota Devolvida - CSOC/IRPJ** — tabela `EFENTRADAS_NOTA_DEVOLVIDA_CSOC_IRPJ` (10 linhas)

Notas Fiscais de Entrada - Complementar - Geral - Nota Devolvida - CSOC/IRPJ. 10 linhas no catálogo; chave: CODI_EMP, CODI_ENT, I_NOTA_DEVOLVIDA, I_CSOC_IRPJ.

- **Chave:** `CODI_EMP, CODI_ENT, I_NOTA_DEVOLVIDA, I_CSOC_IRPJ`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `I_NOTA_DEVOLVIDA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 10 linhas, 2 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da Empresa |
| codigo_da_nota_de_entrada | `codi_ent` | integer(4) |  |  | Código da Nota de Entrada |
| sequencial_da_nota_devolvida | `i_nota_devolvida` | integer(4) |  |  | Sequencial da Nota Devolvida |
| sequencial_do_csoc_irpj | `i_csoc_irpj` | integer(4) |  |  | Sequencial do CSOC/IRPJ |
| valor_da_recducao | `valor_deducao` | numeric(13) |  |  | Valor da recdução |
| base_de_calculo_csoc | `percentual_bc_csoc` | numeric(5) |  |  | % Base de calculo CSOC |
| base_de_calculo_irpj | `percentual_bc_irpj` | numeric(5) |  |  | % Base de calculo IRPJ |
| base_calculo_csoc | `base_calculo_csoc` | numeric(13) |  |  | Base calculo CSOC |
| base_calculo_irpj | `base_calculo_irpj` | numeric(13) |  |  | Base calculo IRPJ |
| valor_ipi | `valor_ipi` | numeric(13) |  |  | Valor IPI |
| valor_subtri | `valor_subtri` | numeric(13) |  |  | Valor Subtri |
| valor_icms | `valor_icms` | numeric(13) |  |  | Valor ICMS |

**Filtros:** `codigo_da_nota_de_entrada` (eq/in), `sequencial_da_nota_devolvida` (eq/in), `sequencial_do_csoc_irpj` (eq/in)

## efentradas_nota_devolvida_pis_cofins

**Notas Fiscais de Entrada - Complementar - Geral - Nota Devolvida - PIS/COFINS** — tabela `EFENTRADAS_NOTA_DEVOLVIDA_PIS_COFINS` (8 linhas)

Notas Fiscais de Entrada - Complementar - Geral - Nota Devolvida - PIS/COFINS. 8 linhas no catálogo; chave: CODI_EMP, CODI_ENT, I_NOTA_DEVOLVIDA, I_PIS_COFINS.

- **Chave:** `CODI_EMP, CODI_ENT, I_NOTA_DEVOLVIDA, I_PIS_COFINS`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `I_NOTA_DEVOLVIDA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 8 linhas, 1 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_da_entrada | `codi_ent` | integer(4) |  |  | Código da Entrada |
| sequencial_da_nota_devolvida | `i_nota_devolvida` | integer(4) |  |  | Sequencial da Nota Devolvida |
| sequencial | `i_pis_cofins` | integer(4) |  |  | Sequencial |
| cst | `cst` | integer(4) |  |  | CST |
| valor_da_deducao | `valor_deducao` | numeric(13) |  |  | Valor da Dedução |
| base_de_calculo | `base_calculo` | numeric(13) |  |  | Base de Cálculo |
| aliquota_do_pis | `aliquota_pis` | numeric(7) |  |  | Alíquota do PIS |
| aliquota_da_cofins | `aliquota_cofins` | numeric(7) |  |  | Alíquota da COFINS |
| quantidade_tributada | `quantidade_tributada` | numeric(13) |  |  | Quantidade Tributada |
| valor_unidade_medida_pis | `valor_unidade_medida_pis` | numeric(13) |  |  | Valor Unidade Medida PIS |
| valor_unidade_medida_cofins | `valor_unidade_medida_cofins` | numeric(13) |  |  | Valor Unidade Medida COFINS |
| valor_pis | `valor_pis` | numeric(13) |  |  | Valor PIS |
| valor_cofins | `valor_cofins` | numeric(13) |  |  | Valor COFINS |
| exclusao | `exclusao` | numeric(13) |  |  | Exclusão |
| percentual_reducao_base_calculo | `percentual_reducao_bc` | numeric(5) |  |  | Percentual Redução Base Cálculo |

**Filtros:** `codigo_da_entrada` (eq/in), `sequencial_da_nota_devolvida` (eq/in), `sequencial` (eq/in)

## efentradas_estadual_pe

**Notas Fiscais de Entradas - Dados estaduais - PE** — tabela `EFENTRADAS_ESTADUAL_PE` (3 linhas)

Notas Fiscais de Entradas - Dados estaduais - PE. 3 linhas no catálogo; chave: CODI_EMP, CODI_ENT.

- **Chave:** `CODI_EMP, CODI_ENT`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3 linhas, 1 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da Empresa |
| codigo_da_nota | `codi_ent` | integer(4) |  |  | Codigo da Nota |
| tipo_combustivel | `tipo_combustivel` | integer(4) |  |  | Tipo combustível |

**Filtros:** `codigo_da_nota` (eq/in), `tipo_combustivel` (eq/in)

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

### efentradas_pis_cofins_origem_1_justi

Confirmado: parcial

> Coluna EFENTRADAS_PIS_COFINS.ORIGEM só tem valores nulos na data da medição (2026-10-18): sem evidência para confirmar o comentário do banco.

| Código | Significado |
|---|---|
| 1 | Justiça Federal |
| 2 | Secretaria da Receita Federal do Brasil |
| 9 | Outros |

### efentradas_pis_cofins_aproveitar_cre

Confirmado: sim

> Todos os valores observados em EFENTRADAS_PIS_COFINS.APROVEITAR_CREDITO_PROPORCIONAL estão no comentário do banco (2026-10-18). Distribuição: N=32.079.

| Código | Significado |
|---|---|
| N | Crédito vinculado somente as receitas Não Cumulativas |
| S | Crédito vinculado as receitas Cumulativas e Não Cumulativas |

### efentradas_nota_devolvida_tipo_do_docu

Confirmado: sim

> Todos os valores observados em EFENTRADAS_NOTA_DEVOLVIDA.TIPO_DOC_DEVOLVIDO estão no comentário do banco (2026-10-18). Distribuição: S=8, nulo=2.

| Código | Significado |
|---|---|
| S | SAÍDA |
| C | CUPOM FISCAL |
| F | CFE |
| Z | REDUÇÃO Z 2D |

