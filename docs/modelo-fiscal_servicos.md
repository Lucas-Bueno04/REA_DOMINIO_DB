# Modelo — Fiscal - servicos (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/fiscal_servicos.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

10 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [efservicos_pis_cofins](#efservicos_pis_cofins) | `EFSERVICOS_PIS_COFINS` | 364.565 | medio | empresa |
| [efservicos_efd_reinf](#efservicos_efd_reinf) | `EFSERVICOS_EFD_REINF` | 107.871 | medio | empresa |
| [efservicos_observacao_fisco](#efservicos_observacao_fisco) | `EFSERVICOS_OBSERVACAO_FISCO` | 24.222 | medio | empresa |
| [efservicos_inss_rb](#efservicos_inss_rb) | `EFSERVICOS_INSS_RB` | 21.363 | medio | empresa |
| [efservicos_inss_rb_atividades](#efservicos_inss_rb_atividades) | `EFSERVICOS_INSS_RB_ATIVIDADES` | 5.897 | pequeno | empresa |
| [efservicos_valor_presente_provisao](#efservicos_valor_presente_provisao) | `EFSERVICOS_VALOR_PRESENTE_PROVISAO` | 66 | pequeno | empresa |
| [efservicos_iva_ibs](#efservicos_iva_ibs) | `EFSERVICOS_IVA_IBS` | 23 | pequeno | empresa |
| [efservicos_iva_cbs](#efservicos_iva_cbs) | `EFSERVICOS_IVA_CBS` | 23 | pequeno | empresa |
| [efservicos_info_comp_fisco](#efservicos_info_comp_fisco) | `EFSERVICOS_INFO_COMP_FISCO` | 2 | pequeno | empresa |
| [efservicos_observacao_contrib](#efservicos_observacao_contrib) | `EFSERVICOS_OBSERVACAO_CONTRIB` | 1 | pequeno | empresa |

## efservicos_pis_cofins

**Notas Fiscais de Servico - PIS/COFINS** — tabela `EFSERVICOS_PIS_COFINS` (364.565 linhas)

Notas Fiscais de Servico - PIS/COFINS. 364.565 linhas no catálogo; chave: CODI_EMP, CODI_SER, I_PIS_COFINS.

- **Chave:** `CODI_EMP, CODI_SER, I_PIS_COFINS`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SER asc`, `I_PIS_COFINS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 364.701 linhas, 427 empresa(s).
- Colunas expostas nulas em 100% das linhas (3): codigo_sequencial_do_recolhimento_do_pis, codigo_sequencial_do_recolhimento_do_cof, codigo_do_beneficio_dirbi.
- Vínculo eftabela_natureza_receit (EFTABELA_NATUREZA_RECEITA): 0 de 57 linhas sem registro relacionado (empresa 266).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_do_servico | `codi_ser` | integer(4) |  |  | Código do serviço |
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

**Filtros:** `codigo_do_servico` (eq/in), `sequencial` (eq/in), `codigo_sequencial_do_recolhimento_do_pis` (eq/in), `codigo_do_recolhimento_do_pis` (eq/in), `codigo_sequencial_do_recolhimento_do_cof` (eq/in), `codigo_do_recolhimento_do_cofins` (eq/in), `codigo_do_beneficio_dirbi` (eq/in), `calcular_reducao_linear_lc224` (eq/in)

## efservicos_efd_reinf

**Notas Fiscais de Serviço - EFD Reinf** — tabela `EFSERVICOS_EFD_REINF` (107.871 linhas)

Notas Fiscais de Serviço - EFD Reinf. 107.871 linhas no catálogo; chave: CODI_EMP, CODI_SER.

- **Chave:** `CODI_EMP, CODI_SER`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SER asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 107.894 linhas, 72 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_ser` | integer(4) |  |  | Código |
| tipo_de_servico | `tipo_servico` | varchar(10) |  |  | Tipo de serviço |
| indicativo_de_prestacao_de_servico | `indicativo_prestacao_servicos` | integer(4) |  |  | Indicativo de Prestação de Serviço |
| possui_paj | `possui_paj_ser` | char(1) |  |  | Possui PAJ |

**Filtros:** `codigo` (eq/in), `tipo_de_servico` (eq/in), `possui_paj` (eq/in)

## efservicos_observacao_fisco

**Notas Fiscais de Serviços - Observação de interesse do fisco** — tabela `EFSERVICOS_OBSERVACAO_FISCO` (24.222 linhas)

Notas Fiscais de Serviços - Observação de interesse do fisco. 24.222 linhas no catálogo; chave: CODI_EMP, CODI_SER, I_SEQUENCIAL_FISCO.

- **Chave:** `CODI_EMP, CODI_SER, I_SEQUENCIAL_FISCO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SER asc`, `I_SEQUENCIAL_FISCO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 24.248 linhas, 152 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_ser` | integer(4) |  |  | Codigo |
| sequencial | `i_sequencial_fisco` | integer(4) |  |  | Sequencial |
| codigo_da_observacao | `i_observacao_fisco` | integer(4) |  |  | Código da Observação |
| descricao_da_observacao | `descricao_fisco` | varchar(300) |  |  | Descrição da Observação |

**Filtros:** `codigo` (eq/in), `sequencial` (eq/in), `codigo_da_observacao` (eq/in), `descricao_da_observacao` (contem/prefixo)

## efservicos_inss_rb

**Notas Fiscais de Serviço - INSS Receita Bruta** — tabela `EFSERVICOS_INSS_RB` (21.363 linhas)

Notas Fiscais de Serviço - INSS Receita Bruta. 21.363 linhas no catálogo; chave: CODI_EMP, CODI_SER.

- **Chave:** `CODI_EMP, CODI_SER`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SER asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 21.369 linhas, 398 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_ser` | integer(4) |  |  | Codigo |
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

## efservicos_inss_rb_atividades

**Notas Fiscais de Serviço - INSS Receita Bruta - Receitas por Atividade** — tabela `EFSERVICOS_INSS_RB_ATIVIDADES` (5.897 linhas)

Notas Fiscais de Serviço - INSS Receita Bruta - Receitas por Atividade. 5.897 linhas no catálogo; chave: CODI_EMP, CODI_SER, I_SEQUENCIAL.

- **Chave:** `CODI_EMP, CODI_SER, I_SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SER asc`, `I_SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 5.898 linhas, 4 empresa(s).
- Vínculo eftabela_atividade_servi (EFTABELA_ATIVIDADE_SERVICO_FOLHA): 0 de 512 linhas sem registro relacionado (empresa 1046).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_ser` | integer(4) |  |  | Codigo |
| sequencial | `i_sequencial` | integer(4) |  |  | Sequencial |
| codigo_da_atividade | `i_atividade` | char(8) |  |  | Código da atividade |
| aliquota | `aliquota` | numeric(7) |  |  | Aliquota |
| receita_bruta | `receita_bruta` | numeric(13) |  |  | Receita Bruta |
| receita_bruta_reinf | `receita_bruta_total_reinf` | numeric(13) |  |  | Receita Bruta REINF |
| desconto_reinf | `desconto_reinf` | numeric(13) |  |  | Desconto REINF |
| ipi_reinf | `ipi_reinf` | numeric(13) |  |  | IPI REINF |
| icms_st_reinf | `icms_st_reinf` | numeric(13) |  |  | ICMS ST REINF |
| codigo_cno | `i_cno` | integer(4) |  |  | Código CNO |
| dispensa_cno | `dispensa_cno` | char(1) |  |  | Dispensa CNO |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `eftabela_atividade_servi` → `EFTABELA_ATIVIDADE_SERVICO_FOLHA` por `i_atividade` = `i_atividade`; colunas: `eftabela_atividade_servi_nome`

**Filtros:** `codigo` (eq/in), `sequencial` (eq/in), `codigo_da_atividade` (eq/in), `codigo_cno` (eq/in), `dispensa_cno` (eq/in)

## efservicos_valor_presente_provisao

**Notas Fiscais de Servico - Valor Presente Provisao** — tabela `EFSERVICOS_VALOR_PRESENTE_PROVISAO` (66 linhas)

Notas Fiscais de Servico - Valor Presente Provisao. 66 linhas no catálogo; chave: CODI_EMP, CODI_SER, DATA_PROVISAO.

- **Chave:** `CODI_EMP, CODI_SER, DATA_PROVISAO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_LANCAMENTO`
- **Ordem padrão:** `DATA_LANCAMENTO desc`, `CODI_SER asc`, `DATA_PROVISAO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 66 linhas, 3 empresa(s), DATA_LANCAMENTO de 2013-01-31 a 2017-10-31.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_da_nota_de_servico | `codi_ser` | integer(4) |  |  | Codigo da nota de servico |
| data_da_provisao | `data_provisao` | date(4) |  |  | Data da provisao |
| data_do_lancamento | `data_lancamento` | date(4) |  |  | Data do lancamento |
| numero_de_dias | `numero_dias` | integer(4) |  |  | Numero de dias |
| valor_presente | `valor_presente` | numeric(13) |  |  | Valor presente |
| valor_da_taxa | `valor_taxa` | numeric(13) |  |  | Valor da taxa |
| valor_de_juros | `valor_juros` | numeric(13) |  |  | Valor de juros |
| valor_de_devolucao | `valor_devolucao` | numeric(13) |  |  | Valor de devolucao |
| valor_futuro | `valor_futuro` | numeric(13) |  |  | Valor futuro |
| valor_de_saldo_juros | `valor_saldo_juros` | numeric(13) |  |  | Valor de saldo juros |

**Filtros:** `codigo_da_nota_de_servico` (eq/in), `data_da_provisao` (eq/in), `data_do_lancamento` (entre/gte/lte)

## efservicos_iva_ibs

**Notas Fiscais de Serviços - IVA IBS** — tabela `EFSERVICOS_IVA_IBS` (23 linhas)

Notas Fiscais de Serviços - IVA IBS. 23 linhas no catálogo; chave: CODI_EMP, CODI_SER.

- **Chave:** `CODI_EMP, CODI_SER`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SER asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 23 linhas, 1 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_ser` | integer(4) |  |  | Código |
| cclasstrib | `i_cclasstrib` | char(6) |  |  | cClassTrib |
| cst | `cst` | integer(4) |  |  | CST |
| base_de_calculo | `base_calculo` | numeric(13) |  |  | Base de cálculo |
| aliquota | `aliquota` | numeric(5) |  |  | Alíquota |
| valor | `valor` | numeric(13) |  |  | Valor |

**Filtros:** `codigo` (eq/in), `cclasstrib` (eq/in)

## efservicos_iva_cbs

**Notas Fiscais de Serviços - IVA CBS** — tabela `EFSERVICOS_IVA_CBS` (23 linhas)

Notas Fiscais de Serviços - IVA CBS. 23 linhas no catálogo; chave: CODI_EMP, CODI_SER.

- **Chave:** `CODI_EMP, CODI_SER`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SER asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 23 linhas, 1 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_ser` | integer(4) |  |  | Código |
| cclasstrib | `i_cclasstrib` | char(6) |  |  | cClassTrib |
| cst | `cst` | integer(4) |  |  | CST |
| base_de_calculo | `base_calculo` | numeric(13) |  |  | Base de cálculo |
| aliquota | `aliquota` | numeric(5) |  |  | Alíquota |
| valor | `valor` | numeric(13) |  |  | Valor |

**Filtros:** `codigo` (eq/in), `cclasstrib` (eq/in)

## efservicos_info_comp_fisco

**Notas Fiscais de Serviços - Informação complementar de interesse do fisco** — tabela `EFSERVICOS_INFO_COMP_FISCO` (2 linhas)

Notas Fiscais de Serviços - Informação complementar de interesse do fisco. 2 linhas no catálogo; chave: CODI_EMP, CODI_SER, I_SEQUENCIAL_FISCO.

- **Chave:** `CODI_EMP, CODI_SER, I_SEQUENCIAL_FISCO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SER asc`, `I_SEQUENCIAL_FISCO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 2 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): codigo_da_informacao_complementar.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_ser` | integer(4) |  |  | Codigo |
| sequencial | `i_sequencial_fisco` | integer(4) |  |  | Sequencial |
| codigo_da_informacao_complementar | `i_info_comp_fisco` | integer(4) |  |  | Código da Informação Complementar |
| descricao_da_informacao_complementar | `descricao_fisco` | varchar(1000) |  |  | Descrição da Informação Complementar |

**Filtros:** `codigo` (eq/in), `sequencial` (eq/in), `codigo_da_informacao_complementar` (eq/in), `descricao_da_informacao_complementar` (contem/prefixo)

## efservicos_observacao_contrib

**Notas Fiscais de Serviços - Obseração de interesse do contribuinte** — tabela `EFSERVICOS_OBSERVACAO_CONTRIB` (1 linhas)

Notas Fiscais de Serviços - Obseração de interesse do contribuinte. 1 linhas no catálogo; chave: CODI_EMP, CODI_SER, I_SEQUENCIAL_CONTRIB.

- **Chave:** `CODI_EMP, CODI_SER, I_SEQUENCIAL_CONTRIB`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SER asc`, `I_SEQUENCIAL_CONTRIB asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_ser` | integer(4) |  |  | Codigo |
| sequencial | `i_sequencial_contrib` | integer(4) |  |  | Sequencial |
| codigo_da_observacao | `i_observacao_contrib` | integer(4) |  |  | Código da Observação |
| descricao_da_observacao | `descricao_contrib` | varchar(300) |  |  | Descrição da Observação |

**Filtros:** `codigo` (eq/in), `sequencial` (eq/in), `codigo_da_observacao` (eq/in), `descricao_da_observacao` (contem/prefixo)

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

