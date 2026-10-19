# Modelo — Fiscal - acumulador (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/fiscal_acumulador.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

7 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [efacumulador_vigencia_pis_cofins_saidas](#efacumulador_vigencia_pis_cofins_saidas) | `EFACUMULADOR_VIGENCIA_PIS_COFINS_SAIDAS` | 70.702 | medio | empresa |
| [efacumulador_vigencia_impostos_funrural](#efacumulador_vigencia_impostos_funrural) | `EFACUMULADOR_VIGENCIA_IMPOSTOS_FUNRURAL` | 53 | pequeno | empresa |
| [efacumulador_vigencia_cfps](#efacumulador_vigencia_cfps) | `EFACUMULADOR_VIGENCIA_CFPS` | 33 | pequeno | empresa |
| [efacumulador_vigencia_pis_cofins_entradas](#efacumulador_vigencia_pis_cofins_entradas) | `EFACUMULADOR_VIGENCIA_PIS_COFINS_ENTRADAS` | 21 | pequeno | empresa |
| [efacumulador_vigencia_tabela_mg_incentivo_ret_faixas](#efacumulador_vigencia_tabela_mg_incentivo_ret_faixas) | `EFACUMULADOR_VIGENCIA_TABELA_MG_INCENTIVO_RET_FAIXAS` | 21 | pequeno | empresa |
| [efacumulador_vigencia_inss_rb_ncm_servicos](#efacumulador_vigencia_inss_rb_ncm_servicos) | `EFACUMULADOR_VIGENCIA_INSS_RB_NCM_SERVICOS` | 2 | pequeno | empresa |
| [efacumulador_vigencia_impostos_simplesn](#efacumulador_vigencia_impostos_simplesn) | `EFACUMULADOR_VIGENCIA_IMPOSTOS_SIMPLESN` | 1 | pequeno | empresa |

## efacumulador_vigencia_pis_cofins_saidas

**Acumuladores - Cadastro - PIS/COFINS - Saídas** — tabela `EFACUMULADOR_VIGENCIA_PIS_COFINS_SAIDAS` (70.702 linhas)

Acumuladores - Cadastro - PIS/COFINS - Saídas. 70.702 linhas no catálogo; chave: CODI_EMP, CODI_ACU, VIGENCIA_ACU, I_PIS_COFINS_SAIDAS.

- **Chave:** `CODI_EMP, CODI_ACU, VIGENCIA_ACU, I_PIS_COFINS_SAIDAS`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA_ACU`
- **Ordem padrão:** `VIGENCIA_ACU desc`, `CODI_ACU asc`, `I_PIS_COFINS_SAIDAS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 70.702 linhas, 1.357 empresa(s), VIGENCIA_ACU de 1964-06-01 a 2026-09-01.
- Colunas expostas nulas em 100% das linhas (3): codigo_sequencial_do_recolhimento_do_pis, codigo_sequencial_do_recolhimento_do_cof, codigo_do_beneficio_dirbi.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| acumulador | `codi_acu` | integer(4) |  |  | Acumulador |
| vigencia_do_acumulador | `vigencia_acu` | date(4) |  |  | Vigência do acumulador |
| sequencial | `i_pis_cofins_saidas` | integer(4) |  |  | Sequencial |
| cst | `cst` | integer(4) |  |  | CST |
| natureza_da_receita | `natureza_receita` | integer(4) |  |  | Natureza da receita |
| aliquota_do_pis | `aliquota_pis` | numeric(7) |  |  | Alíquota do PIS |
| aliquota_do_cofins | `aliquota_cofins` | numeric(7) |  |  | Alíquota do COFINS |
| valor_do_pis_por_unidade_de_medida | `valor_pis_unidade_medida` | numeric(13) |  |  | Valor do PIS por unidade de medida |
| valor_da_cofins_por_unidade_de_medida | `valor_cofins_unidade_medida` | numeric(13) |  |  | Valor da COFINS por unidade de medida |
| percentual_de_reducao_da_base_de_calculo | `percentual_reducao_base_calculo_pis_cofins_saida` | numeric(5) |  |  | Percentual de Redução da Base de Cálculo |
| codigo_sequencial_do_recolhimento_do_pis | `i_recolhimento_pis` | integer(4) |  |  | Código Sequencial do Recolhimento do PIS |
| codigo_do_recolhimento_do_pis | `codigo_recolhimento_pis` | char(6) |  |  | Código do Recolhimento do PIS |
| codigo_sequencial_do_recolhimento_do_cof | `i_recolhimento_cofins` | integer(4) |  |  | Código Sequencial do Recolhimento do COFINS |
| codigo_do_recolhimento_do_cofins | `codigo_recolhimento_cofins` | char(6) |  |  | Código do Recolhimento do COFINS |
| codigo_do_beneficio_dirbi | `codigo_beneficio_dirbi` | integer(4) |  |  | Código do Benefício DIRBI |
| calcular_piscofins_reducao_linear_lc224 | `calcular_piscofins_reducao_linear_lc224` | char(1) |  |  | Calcular redução conf. LC 224/2025 |

**Filtros:** `acumulador` (eq/in), `vigencia_do_acumulador` (eq/in), `sequencial` (eq/in), `codigo_sequencial_do_recolhimento_do_pis` (eq/in), `codigo_do_recolhimento_do_pis` (eq/in), `codigo_sequencial_do_recolhimento_do_cof` (eq/in), `codigo_do_recolhimento_do_cofins` (eq/in), `codigo_do_beneficio_dirbi` (eq/in), `calcular_piscofins_reducao_linear_lc224` (eq/in)

## efacumulador_vigencia_impostos_funrural

**Acumuladores - Cadastro - Aliquotas FUNRURAL** — tabela `EFACUMULADOR_VIGENCIA_IMPOSTOS_FUNRURAL` (53 linhas)

Acumuladores - Cadastro - Aliquotas FUNRURAL. 53 linhas no catálogo; chave: CODI_EMP, CODI_ACU, VIGENCIA_ACU, CODI_IMP.

- **Chave:** `CODI_EMP, CODI_ACU, VIGENCIA_ACU, CODI_IMP`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA_ACU`
- **Ordem padrão:** `VIGENCIA_ACU desc`, `CODI_ACU asc`, `CODI_IMP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 53 linhas, 7 empresa(s), VIGENCIA_ACU de 2019-01-01 a 2026-04-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| acumulador | `codi_acu` | integer(4) |  |  | Acumulador |
| vigencia | `vigencia_acu` | date(4) |  |  | Vigencia |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| aliquota_do_funrural | `aliq_imp` | numeric(6) |  |  | Aliquota do FUNRURAL |
| aliquota_do_inss | `aliq_inss` | numeric(5) |  |  | Aliquota do INSS |
| aliquota_outras_entidades | `aliq_outras` | numeric(6) |  |  | Aliquota outras entidades |
| percentual_da_base_de_calculo | `percentualbc_imp` | numeric(7) |  |  | Percentual da base de calculo |
| aliquota_rat | `aliquota_rat` | numeric(5) |  |  | Alíquota RAT |
| comercializacao_da_producao_isenta_lei_n | `comercializacao_producao_isenta_funrural` | char(1) |  |  | Comercialização da Produção Isenta - Lei nº 13.606/2018 |

**Filtros:** `acumulador` (eq/in), `vigencia` (eq/in), `imposto` (eq/in), `comercializacao_da_producao_isenta_lei_n` (eq/in)

## efacumulador_vigencia_cfps

**Acumuladores - Vigência - CFPS** — tabela `EFACUMULADOR_VIGENCIA_CFPS` (33 linhas)

Acumuladores - Vigência - CFPS. 33 linhas no catálogo; chave: CODI_EMP, CODI_ACU, VIGENCIA_ACU, CFPS_ACU.

- **Chave:** `CODI_EMP, CODI_ACU, VIGENCIA_ACU, CFPS_ACU`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA_ACU`
- **Ordem padrão:** `VIGENCIA_ACU desc`, `CODI_ACU asc`, `CFPS_ACU asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 33 linhas, 26 empresa(s), VIGENCIA_ACU de 2015-01-01 a 2025-03-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| acumulador | `codi_acu` | integer(4) |  |  | Acumulador |
| vigencia | `vigencia_acu` | date(4) |  |  | Vigencia |
| cfps | `cfps_acu` | integer(4) |  |  | CFPS |

**Filtros:** `acumulador` (eq/in), `vigencia` (eq/in), `cfps` (eq/in)

## efacumulador_vigencia_pis_cofins_entradas

**Acumuladores - Cadastro - PIS/COFINS - Entradas** — tabela `EFACUMULADOR_VIGENCIA_PIS_COFINS_ENTRADAS` (21 linhas)

Acumuladores - Cadastro - PIS/COFINS - Entradas. 21 linhas no catálogo; chave: CODI_EMP, CODI_ACU, VIGENCIA_ACU, I_PIS_COFINS_ENTRADAS.

- **Chave:** `CODI_EMP, CODI_ACU, VIGENCIA_ACU, I_PIS_COFINS_ENTRADAS`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA_ACU`
- **Ordem padrão:** `VIGENCIA_ACU desc`, `CODI_ACU asc`, `I_PIS_COFINS_ENTRADAS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 21 linhas, 12 empresa(s), VIGENCIA_ACU de 2021-10-01 a 2026-03-01.
- Colunas expostas nulas em 100% das linhas (2): codigo_sequencial_do_recolhimento_do_pis, codigo_sequencial_do_recolhimento_do_cof.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_acu` | integer(4) |  |  | Codigo |
| vigencia | `vigencia_acu` | date(4) |  |  | Vigencia |
| sequencial | `i_pis_cofins_entradas` | integer(4) |  |  | Sequencial |
| cst | `cst` | integer(4) |  |  | CST |
| base_do_credito | `base_credito` | integer(4) |  |  | Base do crédito |
| natureza_do_frete | `natureza_frete` | integer(4) |  |  | Natureza do frete |
| aliquota_do_pis | `aliquota_pis` | numeric(7) |  |  | Alíquota do PIS |
| aliquota_do_cofins | `aliquota_cofins` | numeric(7) |  |  | Alíquota do COFINS |
| vinculo_do_credito | `vinculo_credito` | integer(4) |  |  | Vínculo do Crédito |
| codigo_sequencial_do_recolhimento_do_pis | `i_recolhimento_pis` | integer(4) |  |  | Código Sequencial do Recolhimento do PIS |
| codigo_do_recolhimento_do_pis | `codigo_recolhimento_pis` | char(6) |  |  | Código do Recolhimento do PIS |
| codigo_sequencial_do_recolhimento_do_cof | `i_recolhimento_cofins` | integer(4) |  |  | Código Sequencial do Recolhimento do COFINS |
| codigo_do_recolhimento_do_cofins | `codigo_recolhimento_cofins` | char(6) |  |  | Código do Recolhimento do COFINS |

**Filtros:** `codigo` (eq/in), `vigencia` (eq/in), `sequencial` (eq/in), `codigo_sequencial_do_recolhimento_do_pis` (eq/in), `codigo_do_recolhimento_do_pis` (eq/in), `codigo_sequencial_do_recolhimento_do_cof` (eq/in), `codigo_do_recolhimento_do_cofins` (eq/in)

## efacumulador_vigencia_tabela_mg_incentivo_ret_faixas

**Acumulador - Tabela de incentivos do Crédito Estímulo MG - Faixas** — tabela `EFACUMULADOR_VIGENCIA_TABELA_MG_INCENTIVO_RET_FAIXAS` (21 linhas)

Acumulador - Tabela de incentivos do Crédito Estímulo MG - Faixas. 21 linhas no catálogo; chave: CODI_EMP, CODI_ACU, VIGENCIA_ACU, SEQUENCIAL.

- **Chave:** `CODI_EMP, CODI_ACU, VIGENCIA_ACU, SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA_ACU`
- **Ordem padrão:** `VIGENCIA_ACU desc`, `CODI_ACU asc`, `SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 21 linhas, 1 empresa(s), VIGENCIA_ACU de 2025-05-01 a 2026-07-01.
- tipo_de_produto_i_inferior_s_superior_p: todos os valores reais estão no comentário do banco (D=21).
- destino_da_operacao_0_todos_1_contribuin: todos os valores reais estão no comentário do banco (0=21).
- sub_grupo_1_importados_2_demais_3_eletro: todos os valores reais estão no comentário do banco (2=21).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| acumulador | `codi_acu` | integer(4) |  |  | Acumulador |
| vigencia | `vigencia_acu` | date(4) |  |  | Vigência |
| sequencial_incentivo_faixa | `sequencial` | integer(4) |  |  | Sequencial incentivo faixa |
| tipo_de_produto_i_inferior_s_superior_p | `tipo_produto` | char(1) |  | efacumulador_vigencia_tabela_mg_incentivo_ret_faixas_tipo_de_pro | Tipo de produto (I-Inferior/S-Superior/P-Importados/D-Demais) |
| operacoes_internas | `operacoes_internas` | numeric(5) |  |  | Operações internas |
| operacoes_interestaduais | `operacoes_interestaduais` | numeric(5) |  |  | Operações interestaduais |
| destino_da_operacao_0_todos_1_contribuin | `destino_operacao` | integer(4) |  | efacumulador_vigencia_tabela_mg_incentivo_ret_faixas_destino_da_ | Destino da operação (0-Todos/1-Contribuinte/2-Não contribuinte/3-PJ não contribuinte/4-Transf. matriz/filial) |
| sub_grupo_1_importados_2_demais_3_eletro | `sub_grupo` | integer(4) |  | efacumulador_vigencia_tabela_mg_incentivo_ret_faixas_sub_grupo_1 | Sub-grupo (1-IMPORTADOS/2-DEMAIS/3-ELETRÔNICOS/4-FIOS/5-CAFÉ/6-SUCOS/7-CHÁ/8-TOMATE/9-FRUTAS/10-EXTRATOS/11-CEREAIS/12-MEDICAMENTOS) |
| criterio_de_utilizacao_da_aliquota_desta | `criterio_icms` | integer(4) |  |  | Criterio de utilização da aliquota destacado |
| aliquota_icms_destacado | `aliquota_icms` | numeric(5) |  |  | Aliquota ICMS Destacado |

**Filtros:** `acumulador` (eq/in), `vigencia` (eq/in), `sequencial_incentivo_faixa` (eq/in), `tipo_de_produto_i_inferior_s_superior_p` (eq/in)

## efacumulador_vigencia_inss_rb_ncm_servicos

**Acumuladores - Cadastro - INSS Receita Bruta - NCM e Serviços** — tabela `EFACUMULADOR_VIGENCIA_INSS_RB_NCM_SERVICOS` (2 linhas)

Acumuladores - Cadastro - INSS Receita Bruta - NCM e Serviços. 2 linhas no catálogo; chave: CODI_EMP, CODI_ACU, VIGENCIA_ACU, I_SEQUENCIAL.

- **Chave:** `CODI_EMP, CODI_ACU, VIGENCIA_ACU, I_SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA_ACU`
- **Ordem padrão:** `VIGENCIA_ACU desc`, `CODI_ACU asc`, `I_SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 1 empresa(s), VIGENCIA_ACU de 2020-01-01 a 2021-12-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codi_acu` | integer(4) |  |  | Codigo |
| vigencia | `vigencia_acu` | date(4) |  |  | Vigencia |
| sequencial | `i_sequencial` | integer(4) |  |  | Sequencial |
| codigo_da_atividade | `i_atividade` | char(8) |  |  | Código da atividade |
| aliquota | `aliquota` | numeric(7) |  |  | Aliquota |

**Filtros:** `codigo` (eq/in), `vigencia` (eq/in), `sequencial` (eq/in), `codigo_da_atividade` (eq/in)

## efacumulador_vigencia_impostos_simplesn

**Acumuladores - Cadastro - Impostos - Simples Nacional** — tabela `EFACUMULADOR_VIGENCIA_IMPOSTOS_SIMPLESN` (1 linhas)

Acumuladores - Cadastro - Impostos - Simples Nacional. 1 linhas no catálogo; chave: CODI_EMP, CODI_ACU, VIGENCIA_ACU, CODI_IMP, IMPOSTO.

- **Chave:** `CODI_EMP, CODI_ACU, VIGENCIA_ACU, CODI_IMP, IMPOSTO`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA_ACU`
- **Ordem padrão:** `VIGENCIA_ACU desc`, `CODI_ACU asc`, `CODI_IMP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s), VIGENCIA_ACU de 2023-11-01 a 2023-11-01.
- imposto_com_exigibilidade_suspensa_1_icm: todos os valores reais estão no comentário do banco (3=1).
- motivo_1_liminar_em_mandado_de_seguranca: todos os valores reais estão no comentário do banco (6=1).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| acumulador | `codi_acu` | integer(4) |  |  | Acumulador |
| vigencia | `vigencia_acu` | date(4) |  |  | Vigencia |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| imposto_com_exigibilidade_suspensa_1_icm | `imposto` | integer(4) |  | efacumulador_vigencia_impostos_simplesn_imposto_com | Imposto com exigibilidade suspensa(1 - ICMS/2 -IPI/3 - ISS/4 - PIS/5 - COFINS/6 - CSLL/7 - IRPJ/8 - INSS) |
| motivo_1_liminar_em_mandado_de_seguranca | `motivo` | char(1) |  | efacumulador_vigencia_impostos_simplesn_motivo_1_li | Motivo(1 - Liminar em Mandado de Seguranca/2 - Deposito Judicial/3 - Antecipacao de Tutela/4 - Liminar em Medida Cautelar/5 - Deposito Administrativo/6 - Outros) |
| numero_do_processo | `processo` | char(20) |  |  | Numero do processo |
| vara | `vara` | integer(4) |  |  | Vara |
| municipio | `codigo_municipio` | integer(4) |  |  | Municipio |
| uf | `uf` | char(2) |  |  | UF |
| com_deposito_s_n | `deposito` | char(1) |  |  | Com deposito(S/N) |

**Filtros:** `acumulador` (eq/in), `vigencia` (eq/in), `imposto` (eq/in), `imposto_com_exigibilidade_suspensa_1_icm` (eq/in), `motivo_1_liminar_em_mandado_de_seguranca` (eq/in), `numero_do_processo` (eq/in), `municipio` (eq/in), `uf` (eq/in), `com_deposito_s_n` (eq/in)

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

### efacumulador_vigencia_tabela_mg_incentivo_ret_faixas_tipo_de_pro

Confirmado: sim

> Todos os valores observados em EFACUMULADOR_VIGENCIA_TABELA_MG_INCENTIVO_RET_FAIXAS.TIPO_PRODUTO estão no comentário do banco (2026-10-18). Distribuição: D=21.

| Código | Significado |
|---|---|
| I | Inferior |
| S | Superior |
| P | Importados |
| D | Demais |

### efacumulador_vigencia_tabela_mg_incentivo_ret_faixas_destino_da_

Confirmado: sim

> Todos os valores observados em EFACUMULADOR_VIGENCIA_TABELA_MG_INCENTIVO_RET_FAIXAS.DESTINO_OPERACAO estão no comentário do banco (2026-10-18). Distribuição: 0=21.

| Código | Significado |
|---|---|
| 0 | Todos |
| 1 | Contribuinte |
| 2 | Não contribuinte |
| 3 | PJ não contribuinte |
| 4 | Transf. matriz |

### efacumulador_vigencia_tabela_mg_incentivo_ret_faixas_sub_grupo_1

Confirmado: sim

> Todos os valores observados em EFACUMULADOR_VIGENCIA_TABELA_MG_INCENTIVO_RET_FAIXAS.SUB_GRUPO estão no comentário do banco (2026-10-18). Distribuição: 2=21.

| Código | Significado |
|---|---|
| 1 | IMPORTADOS |
| 2 | DEMAIS |
| 3 | ELETRÔNICOS |
| 4 | FIOS |
| 5 | CAFÉ |
| 6 | SUCOS |
| 7 | CHÁ |
| 8 | TOMATE |
| 9 | FRUTAS |
| 10 | EXTRATOS |
| 11 | CEREAIS |
| 12 | MEDICAMENTOS |

### efacumulador_vigencia_impostos_simplesn_imposto_com

Confirmado: sim

> Todos os valores observados em EFACUMULADOR_VIGENCIA_IMPOSTOS_SIMPLESN.IMPOSTO estão no comentário do banco (2026-10-18). Distribuição: 3=1.

| Código | Significado |
|---|---|
| 1 | ICMS |
| 2 | IPI |
| 3 | ISS |
| 4 | PIS |
| 5 | COFINS |
| 6 | CSLL |
| 7 | IRPJ |
| 8 | INSS |

### efacumulador_vigencia_impostos_simplesn_motivo_1_li

Confirmado: sim

> Todos os valores observados em EFACUMULADOR_VIGENCIA_IMPOSTOS_SIMPLESN.MOTIVO estão no comentário do banco (2026-10-18). Distribuição: 6=1.

| Código | Significado |
|---|---|
| 1 | Liminar em Mandado de Seguranca |
| 2 | Deposito Judicial |
| 3 | Antecipacao de Tutela |
| 4 | Liminar em Medida Cautelar |
| 5 | Deposito Administrativo |
| 6 | Outros |

