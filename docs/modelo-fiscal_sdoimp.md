# Modelo — Fiscal - sdoimp (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/fiscal_sdoimp.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

82 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [efsdoimp_subtri_por_uf_sp](#efsdoimp_subtri_por_uf_sp) | `EFSDOIMP_SUBTRI_POR_UF_SP` | 473.587 | medio | empresa |
| [efsdoimp_pis_cofins_contabilizacao](#efsdoimp_pis_cofins_contabilizacao) | `EFSDOIMP_PIS_COFINS_CONTABILIZACAO` | 169.720 | medio | empresa |
| [efsdoimp_lancto](#efsdoimp_lancto) | `efsdoimp_lancto` | 74.436 | medio | empresa |
| [efsdoimp_por_recolhimento_por_fornecedor](#efsdoimp_por_recolhimento_por_fornecedor) | `EFSDOIMP_POR_RECOLHIMENTO_POR_FORNECEDOR` | 46.930 | medio | empresa |
| [efsdoimp_pis_cofins_detalhamento_debito](#efsdoimp_pis_cofins_detalhamento_debito) | `EFSDOIMP_PIS_COFINS_DETALHAMENTO_DEBITO` | 29.018 | medio | empresa |
| [efsdoimp_pis_cofins_detalhamento_debito_por_filial](#efsdoimp_pis_cofins_detalhamento_debito_por_filial) | `EFSDOIMP_PIS_COFINS_DETALHAMENTO_DEBITO_POR_FILIAL` | 25.497 | medio | empresa |
| [efsdoimp_pis_cofins_detalhamento_retencao](#efsdoimp_pis_cofins_detalhamento_retencao) | `EFSDOIMP_PIS_COFINS_DETALHAMENTO_RETENCAO` | 20.569 | medio | empresa |
| [efsdoimp_estadual_sp](#efsdoimp_estadual_sp) | `EFSDOIMP_ESTADUAL_SP` | 19.335 | medio | empresa |
| [efsdoimp_por_uf_por_nota](#efsdoimp_por_uf_por_nota) | `EFSDOIMP_POR_UF_POR_NOTA` | 19.146 | medio | empresa |
| [efsdoimp_simples_nacional_base_negativa](#efsdoimp_simples_nacional_base_negativa) | `EFSDOIMP_SIMPLES_NACIONAL_BASE_NEGATIVA` | 13.429 | medio | empresa |
| [efsdoimp_simples_nacional_salao_parceiro](#efsdoimp_simples_nacional_salao_parceiro) | `EFSDOIMP_SIMPLES_NACIONAL_SALAO_PARCEIRO` | 13.043 | medio | empresa |
| [efsdoimp_pis_cofins_detalhamento](#efsdoimp_pis_cofins_detalhamento) | `EFSDOIMP_PIS_COFINS_DETALHAMENTO` | 10.242 | medio | empresa |
| [efsdoimp_por_uf](#efsdoimp_por_uf) | `EFSDOIMP_POR_UF` | 6.997 | pequeno | empresa |
| [efsdoimp_pis_cofins_reducao_linear_aproveitamento_credito](#efsdoimp_pis_cofins_reducao_linear_aproveitamento_credito) | `EFSDOIMP_PIS_COFINS_REDUCAO_LINEAR_APROVEITAMENTO_CREDITO` | 5.990 | pequeno | empresa |
| [efsdoimp_parcelas](#efsdoimp_parcelas) | `efsdoimp_parcelas` | 4.469 | pequeno | empresa |
| [efsdoimp_por_uf_sp](#efsdoimp_por_uf_sp) | `EFSDOIMP_POR_UF_SP` | 4.073 | pequeno | empresa |
| [efsdoimp_irpj_irrf_retido](#efsdoimp_irpj_irrf_retido) | `EFSDOIMP_IRPJ_IRRF_RETIDO` | 4.062 | pequeno | empresa |
| [efsdoimp_por_recolhimento_por_data](#efsdoimp_por_recolhimento_por_data) | `EFSDOIMP_POR_RECOLHIMENTO_POR_DATA` | 2.557 | pequeno | empresa |
| [efsdoimp_csll_csll_retido](#efsdoimp_csll_csll_retido) | `EFSDOIMP_CSLL_CSLL_RETIDO` | 2.466 | pequeno | empresa |
| [efsdoimp_pis_cofins_reducao_linear_por_nota](#efsdoimp_pis_cofins_reducao_linear_por_nota) | `EFSDOIMP_PIS_COFINS_REDUCAO_LINEAR_POR_NOTA` | 2.420 | pequeno | empresa |
| [efsdoimp_pis_cofins_contabilizacao_detalhamento_credito](#efsdoimp_pis_cofins_contabilizacao_detalhamento_credito) | `EFSDOIMP_PIS_COFINS_CONTABILIZACAO_DETALHAMENTO_CREDITO` | 2.339 | pequeno | empresa |
| [efsdoimp_pis_cofins_detalhamento_credito](#efsdoimp_pis_cofins_detalhamento_credito) | `EFSDOIMP_PIS_COFINS_DETALHAMENTO_CREDITO` | 2.209 | pequeno | empresa |
| [efsdoimp_scp](#efsdoimp_scp) | `EFSDOIMP_SCP` | 2.041 | pequeno | empresa |
| [efsdoimp_pis_cofins_detalhamento_debito_devolucao](#efsdoimp_pis_cofins_detalhamento_debito_devolucao) | `EFSDOIMP_PIS_COFINS_DETALHAMENTO_DEBITO_DEVOLUCAO` | 1.786 | pequeno | empresa |
| [efsdoimp_pis_cofins_detalhamento_credito_bases](#efsdoimp_pis_cofins_detalhamento_credito_bases) | `EFSDOIMP_PIS_COFINS_DETALHAMENTO_CREDITO_BASES` | 1.551 | pequeno | empresa |
| [efsdoimp_subtri_por_uf_pr](#efsdoimp_subtri_por_uf_pr) | `EFSDOIMP_SUBTRI_POR_UF_PR` | 1.443 | pequeno | empresa |
| [efsdoimp_pis_cofins_detalhamento_debito_devolucao_aproveitam](#efsdoimp_pis_cofins_detalhamento_debito_devolucao_aproveitam) | `EFSDOIMP_PIS_COFINS_DETALHAMENTO_DEBITO_DEVOLUCAO_APROVEITAMENTO` | 1.352 | pequeno | empresa |
| [efsdoimp_receita_impostos_majoracao](#efsdoimp_receita_impostos_majoracao) | `EFSDOIMP_RECEITA_IMPOSTOS_MAJORACAO` | 1.000 | pequeno | empresa |
| [efsdoimp_simples_nacional_prorrogacao](#efsdoimp_simples_nacional_prorrogacao) | `EFSDOIMP_SIMPLES_NACIONAL_PRORROGACAO` | 640 | pequeno | empresa |
| [efsdoimp_estadual_mg](#efsdoimp_estadual_mg) | `EFSDOIMP_ESTADUAL_MG` | 535 | pequeno | empresa |
| [efsdoimp_estadual_rj](#efsdoimp_estadual_rj) | `EFSDOIMP_ESTADUAL_RJ` | 523 | pequeno | empresa |
| [efsdoimp_subtri_por_uf_rj](#efsdoimp_subtri_por_uf_rj) | `EFSDOIMP_SUBTRI_POR_UF_RJ` | 508 | pequeno | empresa |
| [efsdoimp_subtri_por_uf_mg](#efsdoimp_subtri_por_uf_mg) | `EFSDOIMP_SUBTRI_POR_UF_MG` | 431 | pequeno | empresa |
| [efsdoimp_estadual_pe](#efsdoimp_estadual_pe) | `EFSDOIMP_ESTADUAL_PE` | 418 | pequeno | empresa |
| [efsdoimp_estadual_ba](#efsdoimp_estadual_ba) | `EFSDOIMP_ESTADUAL_BA` | 348 | pequeno | empresa |
| [efsdoimp_subtri_por_uf_ba](#efsdoimp_subtri_por_uf_ba) | `EFSDOIMP_SUBTRI_POR_UF_BA` | 344 | pequeno | empresa |
| [efsdoimp_inss_rb_por_recolhimento](#efsdoimp_inss_rb_por_recolhimento) | `EFSDOIMP_INSS_RB_POR_RECOLHIMENTO` | 338 | pequeno | empresa |
| [efsdoimp_estadual_pr](#efsdoimp_estadual_pr) | `EFSDOIMP_ESTADUAL_PR` | 281 | pequeno | empresa |
| [efsdoimp_nao_cumulativos](#efsdoimp_nao_cumulativos) | `efsdoimp_nao_cumulativos` | 274 | pequeno | empresa |
| [efsdoimp_inss_rb_por_recolhimento_cno](#efsdoimp_inss_rb_por_recolhimento_cno) | `EFSDOIMP_INSS_RB_POR_RECOLHIMENTO_CNO` | 266 | pequeno | empresa |
| [efsdoimp_pis_cofins_importacao_por_nota](#efsdoimp_pis_cofins_importacao_por_nota) | `EFSDOIMP_PIS_COFINS_IMPORTACAO_POR_NOTA` | 209 | pequeno | empresa |
| [efsdoimp_inss_rb_receita](#efsdoimp_inss_rb_receita) | `EFSDOIMP_INSS_RB_RECEITA` | 169 | pequeno | empresa |
| [efsdoimp_inss_rb_por_recolhimento_por_atividade](#efsdoimp_inss_rb_por_recolhimento_por_atividade) | `EFSDOIMP_INSS_RB_POR_RECOLHIMENTO_POR_ATIVIDADE` | 146 | pequeno | empresa |
| [efsdoimp_pis_cofins_reducao_linear](#efsdoimp_pis_cofins_reducao_linear) | `EFSDOIMP_PIS_COFINS_REDUCAO_LINEAR` | 144 | pequeno | empresa |
| [efsdoimp_aproveitamento_credito](#efsdoimp_aproveitamento_credito) | `efsdoimp_aproveitamento_credito` | 136 | pequeno | empresa |
| [efsdoimp_estadual_ce](#efsdoimp_estadual_ce) | `EFSDOIMP_ESTADUAL_CE` | 129 | pequeno | empresa |
| [efsdoimp_subtri_por_uf_sc](#efsdoimp_subtri_por_uf_sc) | `EFSDOIMP_SUBTRI_POR_UF_SC` | 122 | pequeno | empresa |
| [efsdoimp_inss_rb_por_recolhimento_por_atividade_cno](#efsdoimp_inss_rb_por_recolhimento_por_atividade_cno) | `EFSDOIMP_INSS_RB_POR_RECOLHIMENTO_POR_ATIVIDADE_CNO` | 111 | pequeno | empresa |
| [efsdoimp_estadual_ro](#efsdoimp_estadual_ro) | `EFSDOIMP_ESTADUAL_RO` | 88 | pequeno | empresa |
| [efsdoimp_estadual_ac](#efsdoimp_estadual_ac) | `EFSDOIMP_ESTADUAL_AC` | 78 | pequeno | empresa |
| [efsdoimp_por_uf_mg](#efsdoimp_por_uf_mg) | `EFSDOIMP_POR_UF_MG` | 71 | pequeno | empresa |
| [efsdoimp_estadual_es](#efsdoimp_estadual_es) | `EFSDOIMP_ESTADUAL_ES` | 67 | pequeno | empresa |
| [efsdoimp_es_compete](#efsdoimp_es_compete) | `EFSDOIMP_ES_COMPETE` | 67 | pequeno | empresa |
| [efsdoimp_estadual_pi](#efsdoimp_estadual_pi) | `EFSDOIMP_ESTADUAL_PI` | 65 | pequeno | empresa |
| [efsdoimp_subtri_por_uf_pi](#efsdoimp_subtri_por_uf_pi) | `EFSDOIMP_SUBTRI_POR_UF_PI` | 65 | pequeno | empresa |
| [efsdoimp_simples_nacional_controle_base_negativa_devolucao_s](#efsdoimp_simples_nacional_controle_base_negativa_devolucao_s) | `EFSDOIMP_SIMPLES_NACIONAL_CONTROLE_BASE_NEGATIVA_DEVOLUCAO_SECUNDARIA` | 63 | pequeno | empresa |
| [efsdoimp_estadual_sc](#efsdoimp_estadual_sc) | `EFSDOIMP_ESTADUAL_SC` | 61 | pequeno | empresa |
| [efsdoimp_subtri_por_uf_es](#efsdoimp_subtri_por_uf_es) | `EFSDOIMP_SUBTRI_POR_UF_ES` | 61 | pequeno | empresa |
| [efsdoimp_pis_cofins_reducao_linear_natureza](#efsdoimp_pis_cofins_reducao_linear_natureza) | `EFSDOIMP_PIS_COFINS_REDUCAO_LINEAR_NATUREZA` | 60 | pequeno | empresa |
| [efsdoimp_estadual_am](#efsdoimp_estadual_am) | `EFSDOIMP_ESTADUAL_AM` | 56 | pequeno | empresa |
| [efsdoimp_pis_cofins_reducao_linear_filial](#efsdoimp_pis_cofins_reducao_linear_filial) | `EFSDOIMP_PIS_COFINS_REDUCAO_LINEAR_FILIAL` | 56 | pequeno | empresa |
| [efsdoimp_estadual_mt](#efsdoimp_estadual_mt) | `EFSDOIMP_ESTADUAL_MT` | 49 | pequeno | empresa |
| [efsdoimp_por_uf_rj](#efsdoimp_por_uf_rj) | `EFSDOIMP_POR_UF_RJ` | 39 | pequeno | empresa |
| [efsdoimp_mg_sub_apuracao](#efsdoimp_mg_sub_apuracao) | `EFSDOIMP_MG_SUB_APURACAO` | 34 | pequeno | empresa |
| [efsdoimp_mg_sub_apuracao_incentivo_ret](#efsdoimp_mg_sub_apuracao_incentivo_ret) | `EFSDOIMP_MG_SUB_APURACAO_INCENTIVO_RET` | 34 | pequeno | empresa |
| [efsdoimp_estadual_df](#efsdoimp_estadual_df) | `EFSDOIMP_ESTADUAL_DF` | 28 | pequeno | empresa |
| [efsdoimp_subtri_por_uf_df](#efsdoimp_subtri_por_uf_df) | `EFSDOIMP_SUBTRI_POR_UF_DF` | 28 | pequeno | empresa |
| [efsdoimp_estadual_rn](#efsdoimp_estadual_rn) | `EFSDOIMP_ESTADUAL_RN` | 23 | pequeno | empresa |
| [efsdoimp_estadual_al](#efsdoimp_estadual_al) | `EFSDOIMP_ESTADUAL_AL` | 23 | pequeno | empresa |
| [efsdoimp_subtri_por_uf_se](#efsdoimp_subtri_por_uf_se) | `EFSDOIMP_SUBTRI_POR_UF_SE` | 17 | pequeno | empresa |
| [efsdoimp_pis_cofins_detalhamento_debito_imobiliario](#efsdoimp_pis_cofins_detalhamento_debito_imobiliario) | `EFSDOIMP_PIS_COFINS_DETALHAMENTO_DEBITO_IMOBILIARIO` | 14 | pequeno | empresa |
| [efsdoimp_pis_cofins_detalhamento_extemporaneo_ctb](#efsdoimp_pis_cofins_detalhamento_extemporaneo_ctb) | `EFSDOIMP_PIS_COFINS_DETALHAMENTO_EXTEMPORANEO_CTB` | 8 | pequeno | empresa |
| [efsdoimp_estadual_to](#efsdoimp_estadual_to) | `EFSDOIMP_ESTADUAL_TO` | 6 | pequeno | empresa |
| [efsdoimp_por_uf_es](#efsdoimp_por_uf_es) | `EFSDOIMP_POR_UF_ES` | 5 | pequeno | empresa |
| [efsdoimp_pis_cofins_detalhamento_retencao_nao_considerado](#efsdoimp_pis_cofins_detalhamento_retencao_nao_considerado) | `EFSDOIMP_PIS_COFINS_DETALHAMENTO_RETENCAO_NAO_CONSIDERADO` | 4 | pequeno | empresa |
| [efsdoimp_estadual_pa](#efsdoimp_estadual_pa) | `EFSDOIMP_ESTADUAL_PA` | 3 | pequeno | empresa |
| [efsdoimp_subtri_por_uf_pa](#efsdoimp_subtri_por_uf_pa) | `EFSDOIMP_SUBTRI_POR_UF_PA` | 3 | pequeno | empresa |
| [efsdoimp_subtri_por_uf_to](#efsdoimp_subtri_por_uf_to) | `EFSDOIMP_SUBTRI_POR_UF_TO` | 3 | pequeno | empresa |
| [efsdoimp_scp_csll_csll_retido](#efsdoimp_scp_csll_csll_retido) | `EFSDOIMP_SCP_CSLL_CSLL_RETIDO` | 2 | pequeno | empresa |
| [efsdoimp_simples_nacional_detalhamento](#efsdoimp_simples_nacional_detalhamento) | `EFSDOIMP_SIMPLES_NACIONAL_DETALHAMENTO` | 1 | pequeno | empresa |
| [efsdoimp_por_recolhimento_por_nota](#efsdoimp_por_recolhimento_por_nota) | `EFSDOIMP_POR_RECOLHIMENTO_POR_NOTA` | 1 | pequeno | empresa |
| [efsdoimp_subtri_por_uf_rj_compl_rest_icms_st](#efsdoimp_subtri_por_uf_rj_compl_rest_icms_st) | `EFSDOIMP_SUBTRI_POR_UF_RJ_COMPL_REST_ICMS_ST` | 1 | pequeno | empresa |

## efsdoimp_subtri_por_uf_sp

**Saldo dos Impostos - Substituição Tributária Por SP** — tabela `EFSDOIMP_SUBTRI_POR_UF_SP` (473.587 linhas)

Saldo dos Impostos - Substituição Tributária Por SP. 473.587 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 474.019 linhas, 564 empresa(s), DATA_SIM de 2007-04-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| sigla_da_uf | `sigla_uf` | char(2) |  |  | Sigla da UF |
| recolhimento | `i_recolhimento` | integer(4) |  |  | Recolhimento |
| debito_icms_sobre_estoque | `debito_icms_sobre_estoque` | numeric(13) |  |  | Débito ICMS Sobre Estoque |
| transferencia_do_icms_st_devido_ao_fecoe | `outro_credito_transf_icms_st_fecoep` | numeric(13) |  |  | Transferência do ICMS ST devido ao FECOEP para apuração específica |
| estorno_de_debitos_de_ajuste_do_subitem | `estorno_debito_subitem_1499` | numeric(13) |  |  | Estorno de débitos de ajuste do subitem 1499 |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `sigla_da_uf` (eq/in), `recolhimento` (eq/in)

## efsdoimp_pis_cofins_contabilizacao

**Saldo do Impostos - ContabilizaÃ§Ã£o do PIS/COFINS** — tabela `EFSDOIMP_PIS_COFINS_CONTABILIZACAO` (169.720 linhas)

Saldo do Impostos - ContabilizaÃ§Ã£o do PIS/COFINS. 169.720 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SCP, I_RECOLHIMENTO, CONSOLIDADO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SCP, I_RECOLHIMENTO, CONSOLIDADO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 169.894 linhas, 925 empresa(s), DATA_SIM de 2007-04-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| scp | `i_scp` | integer(4) |  |  | SCP |
| recolhimento | `i_recolhimento` | integer(4) |  |  | Recolhimento |
| consolidado | `consolidado` | char(1) |  |  | Consolidado |
| saldo_devedor | `saldo_devedor` | numeric(13) |  |  | Saldo devedor |
| saldo_credor | `saldo_credor` | numeric(13) |  |  | Saldo credor |
| total_dabitos | `valor_total_debitos` | numeric(13) |  |  | Total dÃ©bitos |
| total_craditos | `valor_total_creditos` | numeric(13) |  |  | Total crÃ©ditos |
| devoluaao | `valor_devolucao` | numeric(13) |  |  | DevoluÃ§Ã£o |
| estorno_de_dabito_diferido_no_peraodo | `estorno_debito_diferido_no_periodo` | numeric(13) |  |  | Estorno de dÃ©bito diferido no perÃ­odo |
| dabito_diferido_a_pagar_no_peraodo | `debito_diferido_a_pagar_no_periodo` | numeric(13) |  |  | DÃ©bito diferido a pagar no perÃ­odo |
| valor_das_retenaaes_a_serem_utilizadas_n | `valor_retencoes_utilizadas_periodo` | numeric(13) |  |  | Valor das retenÃ§Ãµes a serem utilizadas no perÃ­odo |
| cradito_presumido_na_aquisiaao_de_bebida | `valor_credito_presumido_bebida_fria_13097` | numeric(13) |  |  | CrÃ©dito presumido na aquisiÃ§Ã£o de bebidas frias |
| ajuste_de_reduaao_devoluaaes_de_craditos | `ajuste_reducao_dev_cre_empre_imobiliario` | numeric(13) |  |  | Ajuste de reduÃ§Ã£o - DevoluÃ§Ãµes de crÃ©ditos empreendimentos imobiliÃ¡rio utilizado no perÃ­odo |
| ajuste_de_reduaao_devoluaaes_de_vendas_u | `ajuste_reducao_devolucao_venda` | numeric(13) |  |  | Ajuste de reduÃ§Ã£o - DevoluÃ§Ãµes de vendas utilizado no perÃ­odo |
| valor_de_estorno_de_cradito_diferido_no | `valor_estorno_credito_diferido` | numeric(13) |  |  | Valor de estorno de crÃ©dito diferido no perÃ­odo |
| valor_de_cradito_diferido_utilizado_no_p | `valor_credito_diferido_utilizado_no_periodo` | numeric(13) |  |  | Valor de crÃ©dito diferido utilizado no perÃ­odo |
| valor_de_cradito_e_dabito_diferido_utili | `valor_diferido_utilizado_no_periodo` | numeric(13) |  |  | Valor de crÃ©dito e dÃ©bito diferido utilizado no perÃ­odo |
| cradito_presumido_importador_ou_produtor | `credito_presumido_alcool_12859` | numeric(13) |  |  | CrÃ©dito presumido importador ou produtor de Ã¡lcool - Lei 12.859/2013 |
| ajuste_de_acrascimo_cradito_presumido_im | `valor_dev_cre_presumido_alcool_12859` | numeric(13) |  |  | Ajuste de AcrÃ©scimo - CrÃ©dito presumido importador ou produtor de Ã¡lcool - Lei 12.859/2013 |
| cradito_sobre_estoque | `credito_sobre_estoque` | numeric(13) |  |  | CrÃ©dito sobre estoque |
| total_de_dabitos_soma_do_campos_01_alaqu | `total_debitos_contribuicao` | numeric(13) |  |  | Total de dÃ©bitos: Soma do campos "01 - AlÃ­quota bÃ¡sica", "02 - AlÃ­quotas diferenciadas", "03 - AlÃ­quota por unidade de medida de produto" e "04 - Atividade imobiliÃ¡ria" |
| estorno_debito_diferido | `estorno_debito_diferido` | numeric(13) |  |  | Estorno de dÃ©bito diferido no perÃ­odo |
| devoluaao_de_venda | `devolucao_venda` | numeric(13) |  |  | DevoluÃ§Ã£o de venda |
| retenaaes | `valor_retencao_aproveitada` | numeric(13) |  |  | RetenÃ§Ãµes |
| credito_prescrito_prazo_decadencial | `credito_prescrito_prazo_decadencial` | numeric(13) |  |  | Credito prescrito prazo decadencial |
| dabito | `valor_saida` | numeric(13) |  |  | DÃ©bito |
| devolucoes_de_vendas_realizadas_no_perio | `devolucao_venda_realizada_no_periodo` | numeric(13) |  |  | Devoluções de vendas realizadas no período |
| credito_presumido_sobre_as_receitas_art | `credito_presumido_sobre_receita` | numeric(13) |  |  | Crédito presumido sobre as receitas - Art. 31, Lei 12.865/2013 |
| receita_financeira_documento_nao_fiscal | `receita_financeira_documento_nao_fiscal` | numeric(13) |  |  | Receita financeira documento não fiscal |
| acrescimo_reducao_linear_isencao_aliquot | `acrescimo_reducao_linear_isencao_aliquota_zero` | numeric(13) |  |  | Acrescimo Reducao Linear da LC 224-2025 |
| reducao_reducao_linear_da_lc_224_2025_de | `reducao_reducao_linear_isencao_aliquota_zero` | numeric(13) |  |  | Reducao Reducao Linear da LC 224-2025 - Devolucao |
| credito_presumido_sobre_as_receitas_redu | `credito_presumido_sobre_receita_reducao_linear` | numeric(13) |  |  | Credito Presumido sobre as receitas Reducao Linear da LC 224-2025 |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `scp` (eq/in), `recolhimento` (eq/in), `consolidado` (eq/in)

## efsdoimp_lancto

**Apuracao X Lancamentos contabeis** — tabela `efsdoimp_lancto` (74.436 linhas)

Apuracao X Lancamentos contabeis. 74.436 linhas no catálogo; chave: codi_emp, nume_lan, fili_lan, codi_imp, data_sim, pdic_sim.

- **Chave:** `codi_emp, nume_lan, fili_lan, codi_imp, data_sim, pdic_sim`
- **Empresa:** `codi_emp`
- **Período:** `data_sim`
- **Ordem padrão:** `data_sim desc`, `nume_lan asc`, `fili_lan asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 74.478 linhas, 795 empresa(s), data_sim de 2013-01-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa_do_lancamento | `codi_emp` | integer(4) |  |  | Empresa do lancamento |
| numero_do_lancamento | `nume_lan` | integer(4) |  |  | Numero do lancamento |
| empresa_do_imposto | `fili_lan` | integer(4) |  |  | Empresa do imposto |
| codigo_do_imposto | `codi_imp` | integer(4) |  |  | Codigo do imposto |
| competencia_do_imposto | `data_sim` | date(4) |  |  | Competencia do imposto |
| periodicidade_do_imposto | `pdic_sim` | integer(4) |  |  | Periodicidade do imposto |

**Filtros:** `numero_do_lancamento` (eq/in), `empresa_do_imposto` (eq/in), `codigo_do_imposto` (eq/in), `competencia_do_imposto` (eq/in), `periodicidade_do_imposto` (eq/in)

## efsdoimp_por_recolhimento_por_fornecedor

**Saldo dos Impostos - Detalhamento por Recolhimento - Por Fornecedor** — tabela `EFSDOIMP_POR_RECOLHIMENTO_POR_FORNECEDOR` (46.930 linhas)

Saldo dos Impostos - Detalhamento por Recolhimento - Por Fornecedor. 46.930 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_RECOLHIMENTO, TIPO_INSCRICAO, INSCRICAO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_RECOLHIMENTO, TIPO_INSCRICAO, INSCRICAO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_VENCIMENTO`
- **Ordem padrão:** `DATA_VENCIMENTO desc`, `CODI_IMP asc`, `DATA_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 46.991 linhas, 939 empresa(s), DATA_VENCIMENTO de 2017-07-25 a 2026-10-23.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| codigo_do_recolhimento | `codigo_recolhimento` | char(6) |  |  | Código do recolhimento |
| tipo_da_inscricao_do_fornecedor 🔒 | `tipo_inscricao` | integer(4) |  |  | Tipo da inscrição do fornecedor |
| inscricao_do_fornecedor 🔒 | `inscricao` | char(14) |  |  | Inscrição do fornecedor |
| valor_contabil_entrada | `valor_contabil_entrada` | numeric(13) |  |  | Valor Contábil Entrada |
| base_calculo_entrada | `base_calculo_entrada` | numeric(13) |  |  | Base Cálculo Entrada |
| valor_imposto_entrada | `valor_imposto_entrada` | numeric(13) |  |  | Valor Imposto Entrada |
| valor_isentas_entrada | `valor_isentas_entrada` | numeric(13) |  |  | Valor Isentas Entrada |
| valor_outras_entrada | `valor_outras_entrada` | numeric(13) |  |  | Valor Outras Entrada |
| base_calculo | `base_calculo` | numeric(13) |  |  | Base Cálculo |
| saldo_devedor | `saldo_devedor` | numeric(13) |  |  | Saldo Devedor |
| valor_a_recolher | `valor_a_recolher` | numeric(13) |  |  | Valor a Recolher |
| valor_diferido | `valor_diferido` | numeric(13) |  |  | Valor Diferido |
| valor_diferido_anterior | `valor_diferido_anterior` | numeric(13) |  |  | Valor Diferido Anterior |
| parcela | `parcela` | integer(4) |  |  | Parcela |
| valor_pago | `valor_pago` | numeric(13) |  |  | Valor pago |
| data_do_vencimento | `data_vencimento` | date(4) |  |  | Data do vencimento |
| debito_adicional_retencao_pelas_entradas | `valor_adicional_retencao_entrada` | numeric(13) |  |  | Débito adicional retenção pelas entradas - Lei 9.711/98 |
| debito_retencao_pelas_entradas | `valor_deducao_retencao_entrada` | numeric(13) |  |  | Débito retenção pelas entradas |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `codigo_do_recolhimento` (eq/in), `tipo_da_inscricao_do_fornecedor` (eq/in), `inscricao_do_fornecedor` (eq/in), `data_do_vencimento` (entre/gte/lte)

## efsdoimp_pis_cofins_detalhamento_debito

**Saldo do Impostos - Detalhamentos do PIS/COFINS - Débitos** — tabela `EFSDOIMP_PIS_COFINS_DETALHAMENTO_DEBITO` (29.018 linhas)

Saldo do Impostos - Detalhamentos do PIS/COFINS - Débitos. 29.018 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_CONTRIBUICAO, ALIQUOTA_PERCENTUAL, ALIQUOTA_VALOR, I_SCP, I_RECOLHIMENTO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_CONTRIBUICAO, ALIQUOTA_PERCENTUAL, ALIQUOTA_VALOR, I_SCP, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 29.054 linhas, 417 empresa(s), DATA_SIM de 2013-01-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| codigo_da_contribuicao | `codigo_contribuicao` | integer(4) |  |  | Código da contribuição |
| valor_da_aliquota_do_imposto | `aliquota_percentual` | numeric(7) |  |  | Valor da alíquota do imposto |
| aliquota_em_moeda_quando_o_calculo_e_por | `aliquota_valor` | numeric(13) |  |  | Alíquota em moeda (quando o cálculo é por unidade de medida) |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |
| sequencial_do_recolhimento | `i_recolhimento` | integer(4) |  |  | Sequencial do Recolhimento |
| valor_da_receita_bruta | `receita_bruta` | numeric(13) |  |  | Valor da receita bruta |
| valor_da_base_de_calculo | `base_calculo` | numeric(13) |  |  | Valor da base de cálculo |
| quantidade_base_de_calculo_quando_o_calc | `quantidade_base_calculo` | numeric(13) |  |  | Quantidade - base de cálculo (quando o cálculo é por unidade de medida) |
| valor_do_imposto_apurado | `valor_apurado` | numeric(13) |  |  | Valor do imposto apurado |
| valor_dos_ajustes_de_acrescimo | `valor_acrescimo` | numeric(13) |  |  | Valor dos ajustes de acréscimo |
| valor_dos_ajustes_de_reducao | `valor_reducao` | numeric(13) |  |  | Valor dos ajustes de redução |
| valor_do_imposto_a_pagar_no_periodo | `valor_contribuicao` | numeric(13) |  |  | Valor do imposto a pagar no período |
| valor_contabil | `valor_contabil` | numeric(13) |  |  | Valor contábil |
| indicador_do_tipo_de_sociedade_cooperati | `tipo_sociedade_cooperativa` | tinyint(1) |  |  | Indicador do Tipo de Sociedade Cooperativa |
| valor_da_base_de_calculo_da_contribuicao | `base_calculo_antes_exclusao_cooperativa` | numeric(13) |  |  | Valor da Base de Cálculo da Contribuição antes das Exclusões das Cooperativas |
| valor_de_exclusao_especifica_das_coopera | `valor_exclusao_geral_cooperativa` | numeric(13) |  |  | Valor de Exclusão Especifica das Cooperativas em Geral |
| valor_das_exclusoes_da_base_de_calculo_e | `valor_exclusao_especifica_cooperativa` | numeric(13) |  |  | Valor das Exclusões da Base de Cálculo Especifica do Tipo da Sociedade Cooperativa |
| valor_da_base_de_calculo_apos_as_excluso | `base_calculo_cooperativa` | numeric(13) |  |  | Valor da Base de Cálculo, Após as Exclusões Especificas da Sociedade Cooperativa |
| valor_da_contribuicao_diferida | `valor_diferido` | numeric(13) |  |  | Valor da contribuição diferida |
| valor_da_contribuicao_diferida_em_period | `valor_diferido_anterior` | numeric(13) |  |  | Valor da contribuição diferida em períodos anteriores |
| valor_da_devolucao | `valor_devolucao` | numeric(13) |  |  | Valor da devolução |
| ajuste_de_reducao_scp | `valor_reducao_scp` | numeric(13) |  |  | Ajuste de redução - SCP |
| credito_presumido_na_aquisicao_de_bebida | `valor_credito_presumido_bebida_fria_13097` | numeric(13) |  |  | Crédito Presumido na aquisição de bebidas frias - Art. 31 da Lei 13.097/2015 |
| base_de_calculo_da_devolucao_em_periodo | `base_devolucao_credito_presumido_alcool_12859` | numeric(13) |  |  | Base de cálculo da Devolução em período diferente do Crédito presumido importador ou produtor de álcool - Lei 12.859/2013 |
| devolucao_em_periodo_diferente_do_credit | `valor_devolucao_credito_presumido_alcool_12859` | numeric(13) |  |  | Devolução em período diferente do Crédito presumido importador ou produtor de álcool - Lei 12.859/2013 |
| valor_total_do_produto | `valor_produto` | numeric(13) |  |  | Valor Total do Produto |
| base_de_calculo_da_devolucao_da_cfe | `base_calculo_devolucao_cfe` | numeric(13) |  |  | Base de cálculo da devolução da CFE |
| quantidade_base_de_calculo_da_devolucao | `quantidade_base_calculo_devolucao_cfe` | numeric(13) |  |  | Quantidade - base de cálculo da devolução da CFE (quando o cálculo é por unidade de medida) |
| valor_do_imposto_apurado_da_devolucao_da | `valor_apurado_devolucao_cfe` | numeric(13) |  |  | Valor do imposto apurado da devolucao da CFE |
| estorno_de_creditos_devolucao_custo_inco | `valor_devolucao_custo_incorrido` | numeric(13) |  |  | Estorno de créditos - Devolução Custo Incorrido |
| valor_reducao_recisao_contrato_imobiliar | `valor_reducao_rescisao_contrato_imobiliario` | numeric(13) |  |  | Valor redução recisão contrato imobiliário |
| valor_ajuste_de_acrecimo_na_base_de_calc | `valor_ajuste_acrescimo_base_calculo` | numeric(13) |  |  | Valor ajuste de acrécimo na base de cálculo |
| valor_ajuste_de_reducao_na_base_de_calcu | `valor_ajuste_reducao_base_calculo` | numeric(13) |  |  | Valor ajuste de redução na base de cálculo |
| valor_base_calculo_devolucao | `base_calculo_devolucao` | numeric(13) |  |  | Valor Base Calculo Devolução |
| valor_frete_seguro_e_despesas_acessorias | `valor_frete_seguro_despesas_acessorias_saida` | numeric(13) |  |  | Valor frete, seguro e despesas acessórias - Saída |
| base_de_calculo_da_devolucao_de_cte | `base_calculo_devolucao_cte` | numeric(13) |  |  | Base de cálculo da devolução de CTE |
| valor_pis_da_devolucao_de_cte | `valor_pis_devolucao_cte` | numeric(13) |  |  | Valor PIS da devolução de CTE |
| valor_cofins_da_devolucao_de_cte | `valor_cofins_devolucao_cte` | numeric(13) |  |  | Valor COFINS da devolução de CTE |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `codigo_da_contribuicao` (eq/in), `valor_da_aliquota_do_imposto` (eq/in), `aliquota_em_moeda_quando_o_calculo_e_por` (eq/in), `sequencial_do_scp` (eq/in), `sequencial_do_recolhimento` (eq/in), `indicador_do_tipo_de_sociedade_cooperati` (eq/in)

## efsdoimp_pis_cofins_detalhamento_debito_por_filial

**Saldo do Impostos - Detalhamentos do PIS/COFINS - Débitos - Por filial** — tabela `EFSDOIMP_PIS_COFINS_DETALHAMENTO_DEBITO_POR_FILIAL` (25.497 linhas)

Saldo do Impostos - Detalhamentos do PIS/COFINS - Débitos - Por filial. 25.497 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_CONTRIBUICAO, ALIQUOTA_PERCENTUAL, ALIQUOTA_VALOR, I_SCP, I_RECOLHIMENTO, FILIAL.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_CONTRIBUICAO, ALIQUOTA_PERCENTUAL, ALIQUOTA_VALOR, I_SCP, I_RECOLHIMENTO, FILIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 25.533 linhas, 384 empresa(s), DATA_SIM de 2017-01-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| codigo_da_contribuicao | `codigo_contribuicao` | integer(4) |  |  | Código da contribuição |
| valor_da_aliquota_do_imposto | `aliquota_percentual` | numeric(7) |  |  | Valor da alíquota do imposto |
| aliquota_em_moeda_quando_o_calculo_e_por | `aliquota_valor` | numeric(13) |  |  | Alíquota em moeda (quando o cálculo é por unidade de medida) |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |
| sequencial_do_recolhimento | `i_recolhimento` | integer(4) |  |  | Sequencial do Recolhimento |
| filial | `filial` | integer(4) |  |  | Filial |
| valor_de_exclusao_especifica_das_coopera | `valor_exclusao_geral_cooperativa` | numeric(13) |  |  | Valor de Exclusão Especifica das Cooperativas em Geral |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `codigo_da_contribuicao` (eq/in), `valor_da_aliquota_do_imposto` (eq/in), `aliquota_em_moeda_quando_o_calculo_e_por` (eq/in), `sequencial_do_scp` (eq/in), `sequencial_do_recolhimento` (eq/in), `filial` (eq/in)

## efsdoimp_pis_cofins_detalhamento_retencao

**Saldo do Impostos - Detalhamentos do PIS/COFINS - Retenções** — tabela `EFSDOIMP_PIS_COFINS_DETALHAMENTO_RETENCAO` (20.569 linhas)

Saldo do Impostos - Detalhamentos do PIS/COFINS - Retenções. 20.569 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, NATUREZA_RETENCAO, PERIODO_APURACAO, I_SCP, I_RECOLHIMENTO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, NATUREZA_RETENCAO, PERIODO_APURACAO, I_SCP, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 20.578 linhas, 207 empresa(s), DATA_SIM de 2017-01-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| natureza_da_retencao | `natureza_retencao` | integer(4) |  |  | Natureza da retenção |
| periodo_de_apuracao_da_retencao | `periodo_apuracao` | date(4) |  |  | Período de apuração da retenção |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |
| sequencial_do_recolhimento | `i_recolhimento` | integer(4) |  |  | Sequencial do Recolhimento |
| valor_disponivel | `valor_disponivel` | numeric(13) |  |  | Valor disponível |
| valor_utilizado | `valor_utilizado` | numeric(13) |  |  | Valor utilizado |
| valor_a_transportar | `valor_a_transportar` | numeric(13) |  |  | Valor a transportar |
| valor_da_retencao_da_restituicao_restitu | `valor_restituicao` | numeric(13) |  |  | Valor da retenção da restituição - Restituição, Ressarcimento e Compensação |
| valor_da_retencao_da_compensacao_restitu | `valor_compensacao` | numeric(13) |  |  | Valor da retenção da compensação - Restituição, Ressarcimento e Compensação |
| saldo_recebido_por_transferencia | `saldo_recebido_por_transferencia` | numeric(13) |  |  | Saldo Recebido por Transferência |
| saldo_enviado_por_transferencia | `saldo_enviado_por_transferencia` | numeric(13) |  |  | Saldo Enviado por Transferência |
| valor_postergado | `valor_postergado` | numeric(13) |  |  | Valor Postergado |
| valor_total_das_retencoes_no_mes | `valor_total_retencao_mes` | numeric(13) |  |  | Valor Total das Retenções no Mês |
| valor_de_devolucoes_de_vendas | `valor_devolucoes_vendas` | numeric(13) |  |  | Valor de devoluções de vendas |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `natureza_da_retencao` (eq/in), `periodo_de_apuracao_da_retencao` (eq/in), `sequencial_do_scp` (eq/in), `sequencial_do_recolhimento` (eq/in)

## efsdoimp_estadual_sp

**Saldo dos Impostos - Estadual SP** — tabela `EFSDOIMP_ESTADUAL_SP` (19.335 linhas)

Saldo dos Impostos - Estadual SP. 19.335 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 19.343 linhas, 414 empresa(s), DATA_SIM de 2007-04-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| credito_de_icms_conforme_aliquota_do_sim | `credito_conforme_aliquota_sn` | numeric(13) |  |  | Crédito de ICMS conforme alíquota do Simples Nacional |
| devolucao_de_mercadoria_adquirida_de_sim | `devolucao_mercadoria_adquirida_sn` | numeric(13) |  |  | Devolução de mercadoria adquirida de Simples Nacional |
| outros_debitos_remessa_para_venda_fora_d | `outros_debitos_remessa_para_venda_fora_estab` | numeric(13) |  |  | Outros débitos - Remessa para venda fora do estabelecimento |
| estorno_de_debitos_remessa_para_venda_fo | `estorno_debitos_remessa_para_venda_fora_estab` | numeric(13) |  |  | Estorno de débitos - Remessa para venda fora do estabelecimento |
| debito_de_icms_sobre_estoque_incluidas_s | `debito_icms_sobre_estoque_incluidas_subtri_cat_26_15` | numeric(13) |  |  | Débito de ICMS sobre estoque incluídas Sub. Trib. CAT 26/15 |
| credito_de_icms_sobre_estoque_excluidos | `credito_icms_sobre_estoque_excluidas_subtri` | numeric(13) |  |  | Crédito de ICMS sobre estoque excluídos Sub. Trib. |
| credito_de_icms_sobre_estoque_aproveitad | `credito_estoque_aproveitado_cat_26_15` | numeric(13) |  |  | Crédito de ICMS sobre estoque aproveitado CAT 26/15 |
| trasferencia_de_saldo_credor_atraves_das | `transferencia_saldo_credor_entrada` | numeric(13) |  |  | Trasferência de saldo credor através das entradas com CFOP 1602 |
| trasferencia_de_saldo_devedor_atraves_da | `transferencia_saldo_devedor_entrada` | numeric(13) |  |  | Trasferência de saldo devedor através das entradas com CFOP 1605 |
| transferencia_saldo_credor_saida | `transferencia_saldo_credor_saida` | numeric(13) |  |  | Trasferência de saldo credor através das saídas com CFOP 5602 |
| transferencia_saldo_devedor_saida | `transferencia_saldo_devedor_saida` | numeric(13) |  |  | Trasferência de saldo devedor através das saídas com CFOP 5605 |
| credito_de_icms_proprio_na_venda_para_ou | `credito_icms_prop_venda_outra_uf_port_cat_158_2015` | numeric(13) |  |  | Crédito de ICMS próprio na venda para outra UF - CAT |
| ressarcimento_de_icms_st_cat | `ressarcimento_icms_st_portaria_cat_158_2015` | numeric(13) |  |  | Ressarcimento de ICMS ST - CAT |
| credito_outorgado_art_41_anexo_iii_do_ri | `credito_outorgado_empresas_texteis` | numeric(13) |  |  | Crédito Outorgado - art. 41, Anexo III, do RICMS |
| estorno_de_credito_art_41_anexo_iii_do_r | `estorno_credito_outorgado_empresas_texteis` | numeric(13) |  |  | Estorno de Crédito - art. 41, Anexo III, do RICMS |
| credito_outorgado_empresas_texteis_saida | `credito_outorgado_empresas_texteis_saidas` | numeric(13) |  |  | Crédito Outorgado - art. 41, Anexo III, do RICMS - Saídas |
| credito_outorgado_empresas_texteis_devol | `credito_outorgado_empresas_texteis_devolucao` | numeric(13) |  |  | Crédito Outorgado - art. 41, Anexo III, do RICMS - Devolução |
| estorno_credito_outorgado_empresas_texte | `estorno_credito_outorgado_empresas_texteis_letra_b` | numeric(13) |  |  | Estorno Crédito Outorgado Empresas Texteis Letra B |
| estorno_credito_outorgado_empresas_texte_c | `estorno_credito_outorgado_empresas_texteis_letra_c` | numeric(13) |  |  | Estorno Crédito Outorgado Empresas Texteis Letra C |
| estorno_credito_outorgado_empresas_texte_c_c | `estorno_credito_outorgado_empresas_texteis_letra_t` | numeric(13) |  |  | Estorno Crédito Outorgado Empresas Texteis Letra T |
| estorno_credito_de_icms_proprio_na_venda | `estorno_credito_icms_prop_venda_outra_uf_port_cat_158_2015` | numeric(13) |  |  | Estorno Crédito de ICMS próprio na venda para outra UF - CAT |
| estorno_ressarcimento_de_icms_st_cat | `estorno_ressarcimento_icms_st_portaria_cat_158_2015` | numeric(13) |  |  | Estorno Ressarcimento de ICMS ST - CAT |
| valor_ressarcimento | `valor_ressarcimento` | numeric(13) |  |  | Valor Ressarcimento |
| valor_complemento | `valor_complemento` | numeric(13) |  |  | Valor Complemento |
| valor_icms_credito | `valor_icms_credito` | numeric(13) |  |  | Valor ICMS Crédito |
| valor_icms_estorno_credito | `valor_icms_estorno_credito` | numeric(13) |  |  | Valor ICMS Estorno Crédito |
| estorno_de_credito_pelas_devolucoes_reto | `estorno_credito_devolucoes_retorno_outorgado_empresas_texteis` | numeric(13) |  |  | Estorno de Crédito pelas Devoluções/Retorno - art. 41, Anexo III, do RICMS |
| regime_especial_de_tributacao_no_forneci | `outros_debitos_regime_esp_tributa_icms_forneci_alimentacao` | numeric(13) |  |  | Regime especial de tributação no fornecimento de alimentação - Dec. 51.597/07 |
| credito_de_insumos_nas_operacoes_com_for | `outros_creditos_insumo_oper_forneci_alimentacao` | numeric(13) |  |  | Crédito de insumos nas operações com fornec. de alimentação - Dec. 51.597/07 |
| creditos_de_icms_de_ativo_imobilizado_na | `credito_ativo_imobilizado_anterior` | numeric(13) |  |  | Créditos de ICMS de Ativo Imobilizado não utilizados em períodos anteriores |
| exclusao_de_mercadorias_da_substituicao | `exclusao_mercadoria_subtri_port_cat_28_2020` | numeric(13) |  |  | Exclusão de mercadorias da substituição tributária - Art. 3º, Port CAT-28/2020 |
| credito_na_aquisicao_de_combustiveis_par | `credito_aquisicao_combustivel_para_insumo_conv_icms_199_22_e_15_23` | numeric(13) |  |  | Crédito na aquisição de combustíveis para insumo - Conv. ICMS nº 199/22 e 15/23 |
| estorno_de_debito_nas_operacoes_com_ct_e | `estorno_debito_operacoes_cte_substituto` | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |
| estorno_de_credito_presumido_transportes | `estorno_credito_presumido_transporte_operacores_cte_substituto` | numeric(13) |  |  | Estorno de crédito presumido transportes - Operações com CT-e e/ou CT-eOS |
| credito_outorgado_art_40_anexo_iii_do_ri | `credito_outorgado_saidas_internas_carne` | numeric(13) |  |  | Crédito Outorgado - art. 40, Anexo III, do RICMS |
| estorno_de_credito_art_40_anexo_iii_do_r | `estorno_credito_outorgado_saidas_internas_carne` | numeric(13) |  |  | Estorno de Crédito - art. 40, Anexo III, do RICMS |
| estorno_credito_outorgado_devolucoes_ret | `estorno_credito_outorgado_devolucoes_retorno_saidas_internas_carne` | numeric(13) |  |  | Estorno de Crédito pelas Devoluções/Retorno - art. 40, Anexo III, do RICMS |
| credito_outorgado_saidas_internas_carne | `credito_outorgado_saidas_internas_carne_saidas` | numeric(13) |  |  | Crédito Outorgado - art. 40, Anexo III, do RICMS - Saídas |
| credito_outorgado_saidas_internas_carne_c | `credito_outorgado_saidas_internas_carne_devolucao` | numeric(13) |  |  | Crédito Outorgado - art. 40, Anexo III, do RICMS - Devolução |
| estorno_credito_outorgado_saidas_interna | `estorno_credito_outorgado_saidas_internas_carne_letra_b` | numeric(13) |  |  | Estorno Crédito Outorgado Saídas internas Carne Letra B |
| estorno_credito_outorgado_saidas_interna_c | `estorno_credito_outorgado_saidas_internas_carne_letra_c` | numeric(13) |  |  | Estorno Crédito Outorgado Saídas internas Carne Letra C |
| estorno_credito_outorgado_saidas_interna_c_c | `estorno_credito_outorgado_saidas_internas_carne_letra_t` | numeric(13) |  |  | Estorno Crédito Outorgado Saídas internas Carne Letra T |
| lancamento_extemp_ref_exclusao_de_merc_d | `lancamento_extemp_ref_exclusao_merc_subtri` | numeric(13) |  |  | Lançamento Extemp. ref. exclusão de merc. da subst. trib. - Art. 2º, Port SRE-07/2026 |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in)

## efsdoimp_por_uf_por_nota

**Saldo dos Impostos - Por UF - Por Nota** — tabela `EFSDOIMP_POR_UF_POR_NOTA` (19.146 linhas)

Saldo dos Impostos - Por UF - Por Nota. 19.146 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, CODIGO_NOTA, TIPO_DOCUMENTO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, CODIGO_NOTA, TIPO_DOCUMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 19.271 linhas, 19 empresa(s), DATA_SIM de 2018-03-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| sigla_da_uf | `sigla_uf` | char(2) |  |  | Sigla da UF |
| codigo_nota | `codigo_nota` | integer(4) |  |  | Código Nota |
| tipo_do_documento | `tipo_documento` | char(1) |  |  | Tipo do Documento |
| saldo_devedor | `saldo_devedor` | numeric(15) |  |  | Saldo Devedor |
| debitos_saidas | `valor_debito_saidas` | numeric(15) |  |  | Débitos Saídas |
| valor_pago | `valor_pago` | numeric(15) |  |  | Valor Pago |
| parcela | `parcela` | integer(4) |  |  | Parcela |
| vencimento | `vencimento` | date(4) |  |  | Vencimento |
| debitos_servicos_de_transp_icms_dif_de_a | `debito_servicos_transporte_origem` | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF origem |
| debito_servicos_transporte_destino | `debito_servicos_transporte_destino` | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF destino |
| debito_servicos_transporte_origem_uf_emp | `debito_servicos_transporte_origem_uf_empresa` | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF origem (UF da empresa ativa) |
| debito_servicos_transporte_destino_uf_cl | `debito_servicos_transporte_destino_uf_cliente` | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF destino (UF do cliente) |
| debito_servicos_transporte_origem_uf_emp_c | `debito_servicos_transporte_origem_uf_empresa_igual` | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF origem (UF da empresa ativa nota com UF do cliente igual empresa) |
| debito_servicos_transporte_origem_uf_emp_c_c | `debito_servicos_transporte_origem_uf_empresa_diferente` | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF origem (UF da empresa ativa nota com UF do cliente diferente empresa) |
| debito_servicos_transporte_destino_uf_cl_c | `debito_servicos_transporte_destino_uf_cliente_igual` | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF destino (UF do cliente com UF do cliente igual empresa) |
| debito_servicos_transporte_destino_uf_cl_c_c | `debito_servicos_transporte_destino_uf_cliente_diferente` | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF destino (UF do cliente com UF do cliente diferente empresa) |
| debitos_entradas | `valor_debitos_entradas` | numeric(13) |  |  | Débitos Entradas |
| estorno_de_debitos_recolhimento_junto_ao | `estorno_debito_recolhimento_junto_icms_st` | numeric(13) |  |  | Estorno de débitos recolhimento junto ao ICMS ST |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `sigla_da_uf` (eq/in), `codigo_nota` (eq/in), `tipo_do_documento` (eq/in), `vencimento` (entre/gte/lte)

## efsdoimp_simples_nacional_base_negativa

**Saldo dos Impostos - Detalhamento do Simples Nacional - Base negativa** — tabela `EFSDOIMP_SIMPLES_NACIONAL_BASE_NEGATIVA` (13.429 linhas)

Saldo dos Impostos - Detalhamento do Simples Nacional - Base negativa. 13.429 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, PERIODO_APURACAO, ANEXO, SECAO, TABELA, FILIAL, ARBCISS, TIPO_RECEITA, ARBCPIS, ARBCCOFINS, SITUACOES, ARBCICMS, SEQUENCIAL, MUNICIPIO, CONSIDERAR_ALIQUOTA_REDUCAO_ICMS, ANEXO_ORIGEM, SECAO_ORIGEM, TABELA_ORIGEM, APLICA_REDUCAO_BASE_CALCULO_ICMS, APLICA_REDUCAO_ISS.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, PERIODO_APURACAO, ANEXO, SECAO, TABELA, FILIAL, ARBCISS, TIPO_RECEITA, ARBCPIS, ARBCCOFINS, SITUACOES, ARBCICMS, SEQUENCIAL, MUNICIPIO, CONSIDERAR_ALIQUOTA_REDUCAO_ICMS, ANEXO_ORIGEM, SECAO_ORIGEM, TABELA_ORIGEM, APLICA_REDUCAO_BASE_CALCULO_ICMS, APLICA_REDUCAO_ISS`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 13.455 linhas, 442 empresa(s), DATA_SIM de 2016-07-01 a 2026-09-01.
- tipo_receita_1_mercado_interno_2_exporta: todos os valores reais estão no comentário do banco (1=12.925, 2=530).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da Empresa |
| codigo_do_imposto | `codi_imp` | integer(4) |  |  | Código do Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| periodo_da_origem_da_base_negativa | `periodo_apuracao` | date(4) |  |  | Período da Origem da Base Negativa |
| anexo | `anexo` | tinyint(1) |  |  | Anexo |
| secao | `secao` | tinyint(1) |  |  | SECAO |
| tabela | `tabela` | tinyint(1) |  |  | Tabela |
| codigo_empresa_filial | `filial` | integer(4) |  |  | Código Empresa Filial |
| aliquota_de_reducao_da_base_de_calculo_d | `arbciss` | numeric(13) |  |  | Aliquota de reducao da base de calculo do ISS |
| tipo_receita_1_mercado_interno_2_exporta | `tipo_receita` | integer(4) |  | efsdoimp_simples_nacional_base_negativa_tipo_receit | Tipo Receita (1- Mercado Interno / 2- Exportação) |
| aliquota_de_reducao_de_base_de_calculo_d | `arbcpis` | numeric(13) |  |  | Alíquota de Redução de Base de Cálculo do PIS |
| arbccofins | `arbccofins` | numeric(13) |  |  | Alíquota de Redução de Base de Cálculo do COFINS |
| situacoes_fiscais | `situacoes` | char(16) |  |  | Situacoes fiscais |
| arbcicms | `arbcicms` | numeric(13) |  |  | Aliquota de reducao da base de calculo do ICMS |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| codigo_do_municipio | `municipio` | integer(4) |  |  | Código do município |
| considerar_aliquota_reducao_icms | `considerar_aliquota_reducao_icms` | char(1) |  |  | CONSIDERAR ALÍQUOTA REDUCÃO ICMS |
| anexo_origem | `anexo_origem` | integer(4) |  |  | Anexo Origem |
| secao_origem | `secao_origem` | integer(4) |  |  | Seção Origem |
| tabela_origem | `tabela_origem` | integer(4) |  |  | Tabela Origem |
| aplica_reducao_na_base_de_calculo_do_icm | `aplica_reducao_base_calculo_icms` | char(1) |  |  | Aplica redução na base de calculo do ICMS |
| reducao_do_iss_aplicado_na_aliquota_ou_n | `aplica_reducao_iss` | char(1) |  |  | Redução do ISS aplicado na Alíquota ou na Base de Calculo |
| base_de_calculo_total | `base_calculo_total` | numeric(13) |  |  | Base de Cálculo Total |
| valor_da_deducao_do_periodo_anterior | `valor_deducao_periodo_anterior` | numeric(13) |  |  | Valor da Dedução do Período Anterior |
| valor_da_deducao_do_periodo_atual | `valor_deducao_periodo_atual` | numeric(13) |  |  | Valor da Dedução do Período Atual |
| valor_deduzido | `valor_deduzido` | numeric(13) |  |  | Valor Deduzido |
| base_de_calculo_final | `base_calculo_final` | numeric(13) |  |  | Base de Cálculo Final |
| valor_a_deduzir | `valor_a_deduzir` | numeric(13) |  |  | Valor a Deduzir |
| valor_transferido_outra_tabela | `valor_transferido_outra_tabela` | numeric(13) |  |  | Valor transferido outra tabela |
| transferido_para_outra_tabela_s_n | `transferido` | char(1) |  |  | Transferido para outra tabela(S/N) |
| valor_salao_parceiro | `valor_salao_parceiro` | numeric(13) |  |  | Valor salão-parceiro |

**Filtros:** `codigo_do_imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `periodo_da_origem_da_base_negativa` (eq/in), `anexo` (eq/in), `secao` (eq/in), `tabela` (eq/in), `codigo_empresa_filial` (eq/in), `aliquota_de_reducao_da_base_de_calculo_d` (eq/in), `tipo_receita_1_mercado_interno_2_exporta` (eq/in), `aliquota_de_reducao_de_base_de_calculo_d` (eq/in), `arbccofins` (eq/in), `situacoes_fiscais` (eq/in), `arbcicms` (eq/in)

## efsdoimp_simples_nacional_salao_parceiro

**Saldo dos Impostos - Detalhamento do Simples Nacional - Salão-parceiro** — tabela `EFSDOIMP_SIMPLES_NACIONAL_SALAO_PARCEIRO` (13.043 linhas)

Saldo dos Impostos - Detalhamento do Simples Nacional - Salão-parceiro. 13.043 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, PERIODO_APURACAO, ANEXO, SECAO, TABELA, FILIAL, ARBCISS, TIPO_RECEITA, ARBCPIS, ARBCCOFINS, SITUACOES, ARBCICMS, SEQUENCIAL, MUNICIPIO, CONSIDERAR_ALIQUOTA_REDUCAO_ICMS, ANEXO_ORIGEM, SECAO_ORIGEM, TABELA_ORIGEM, APLICA_REDUCAO_BASE_CALCULO_ICMS, APLICA_REDUCAO_ISS.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, PERIODO_APURACAO, ANEXO, SECAO, TABELA, FILIAL, ARBCISS, TIPO_RECEITA, ARBCPIS, ARBCCOFINS, SITUACOES, ARBCICMS, SEQUENCIAL, MUNICIPIO, CONSIDERAR_ALIQUOTA_REDUCAO_ICMS, ANEXO_ORIGEM, SECAO_ORIGEM, TABELA_ORIGEM, APLICA_REDUCAO_BASE_CALCULO_ICMS, APLICA_REDUCAO_ISS`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 13.069 linhas, 433 empresa(s), DATA_SIM de 2018-01-01 a 2026-09-01.
- tipo_receita_1_mercado_interno_2_exporta: todos os valores reais estão no comentário do banco (1=12.544, 2=525).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| periodo_da_origem_do_valor_salao_parceir | `periodo_apuracao` | date(4) |  |  | Período da Origem do valor salão-parceiro |
| anexo | `anexo` | integer(4) |  |  | Anexo |
| secao | `secao` | integer(4) |  |  | Seção |
| tabela | `tabela` | integer(4) |  |  | Tabela |
| codigo_empresa_filial | `filial` | integer(4) |  |  | Código Empresa Filial |
| aliquota_de_reducao_da_base_de_calculo_d | `arbciss` | numeric(13) |  |  | Aliquota de reducao da base de calculo do ISS |
| tipo_receita_1_mercado_interno_2_exporta | `tipo_receita` | integer(4) |  | efsdoimp_simples_nacional_salao_parceiro_tipo_receit | Tipo Receita (1- Mercado Interno / 2- Exportação) |
| aliquota_de_reducao_de_base_de_calculo_d | `arbcpis` | numeric(13) |  |  | Alíquota de Redução de Base de Cálculo do PIS |
| arbccofins | `arbccofins` | numeric(13) |  |  | Alíquota de Redução de Base de Cálculo do COFINS |
| situacoes_fiscais | `situacoes` | char(16) |  |  | Situacoes fiscais |
| arbcicms | `arbcicms` | numeric(13) |  |  | Aliquota de reducao da base de calculo do ICMS |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| codigo_do_municipio | `municipio` | integer(4) |  |  | Código do município |
| considerar_aliquota_reducao_icms | `considerar_aliquota_reducao_icms` | char(1) |  |  | Considerar alíquota reducão ICMS |
| anexo_origem | `anexo_origem` | integer(4) |  |  | Anexo Origem |
| secao_origem | `secao_origem` | integer(4) |  |  | Seção Origem |
| tabela_origem | `tabela_origem` | integer(4) |  |  | Tabela Origem |
| aplica_reducao_na_base_de_calculo_do_icm | `aplica_reducao_base_calculo_icms` | char(1) |  |  | Aplica redução na base de calculo do ICMS |
| reducao_do_iss_aplicado_na_aliquota_ou_n | `aplica_reducao_iss` | char(1) |  |  | Redução do ISS aplicado na Alíquota ou na Base de Calculo |
| base_de_calculo_total | `base_calculo_total` | numeric(13) |  |  | Base de Cálculo Total |
| valor_da_deducao_do_periodo_anterior | `valor_deducao_periodo_anterior` | numeric(13) |  |  | Valor da Dedução do Período Anterior |
| valor_da_deducao_do_periodo_atual | `valor_deducao_periodo_atual` | numeric(13) |  |  | Valor da Dedução do Período Atual |
| valor_deduzido | `valor_deduzido` | numeric(13) |  |  | Valor Deduzido |
| base_de_calculo_final | `base_calculo_final` | numeric(13) |  |  | Base de Cálculo Final |
| valor_a_deduzir | `valor_a_deduzir` | numeric(13) |  |  | Valor a Deduzir |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `periodo_da_origem_do_valor_salao_parceir` (eq/in), `anexo` (eq/in), `secao` (eq/in), `tabela` (eq/in), `codigo_empresa_filial` (eq/in), `aliquota_de_reducao_da_base_de_calculo_d` (eq/in), `tipo_receita_1_mercado_interno_2_exporta` (eq/in), `aliquota_de_reducao_de_base_de_calculo_d` (eq/in), `arbccofins` (eq/in), `situacoes_fiscais` (eq/in), `arbcicms` (eq/in)

## efsdoimp_pis_cofins_detalhamento

**Saldo do Impostos - Detalhamentos do PIS/COFINS** — tabela `EFSDOIMP_PIS_COFINS_DETALHAMENTO` (10.242 linhas)

Saldo do Impostos - Detalhamentos do PIS/COFINS. 10.242 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SCP, I_RECOLHIMENTO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SCP, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 10.249 linhas, 209 empresa(s), DATA_SIM de 2012-12-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |
| sequencial_do_recolhimento | `i_recolhimento` | integer(4) |  |  | Sequencial do Recolhimento |
| receita_tributada_do_mercado_interno | `receita_tributada` | numeric(13) |  |  | Receita tributada do mercado interno |
| receita_do_mercado_externo | `receita_exportacao` | numeric(13) |  |  | Receita do mercado externo |
| receita_nao_tributada | `receita_isenta` | numeric(13) |  |  | Receita não tributada |
| receita_cumulativa | `receita_cumulativa` | numeric(13) |  |  | Receita cumulativa |
| receita_total | `receita_total` | numeric(13) |  |  | Receita total |
| tem_receita_cumulativa_e_nao_cumulativa | `tem_receita_cum_ncum` | char(1) |  |  | Tem Receita Cumulativa e Não Cumulativa - Marcação Produto |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `sequencial_do_scp` (eq/in), `sequencial_do_recolhimento` (eq/in), `tem_receita_cumulativa_e_nao_cumulativa` (eq/in)

## efsdoimp_por_uf

**Saldo dos Impostos - Por UF** — tabela `EFSDOIMP_POR_UF` (6.997 linhas)

Saldo dos Impostos - Por UF. 6.997 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 7.007 linhas, 166 empresa(s), DATA_SIM de 2017-01-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| sigla_da_uf | `sigla_uf` | char(2) |  |  | Sigla da UF |
| saldo_devedor | `saldo_devedor` | numeric(15) |  |  | Saldo Devedor |
| debitos_saidas | `valor_debito_saidas` | numeric(15) |  |  | Débitos Saídas |
| valor_pago | `valor_pago` | numeric(15) |  |  | Valor Pago |
| vencimento | `vencimento` | date(4) |  |  | Vencimento |
| saldo_credor | `saldo_credor` | numeric(15) |  |  | Saldo Credor |
| saldo_credor_anterior | `saldo_credor_anterior` | numeric(15) |  |  | Saldo Credor Anterior |
| outros_debitos | `outros_debitos` | numeric(15) |  |  | Outros Débitos |
| outros_creditos | `outros_creditos` | numeric(15) |  |  | Outros Créditos |
| estorno_debitos | `estorno_debitos` | numeric(15) |  |  | Estorno Débitos |
| estorno_creditos | `estorno_creditos` | numeric(15) |  |  | Estorno Créditos |
| outras_deducoes | `outras_deducoes` | numeric(15) |  |  | Outras Deduções |
| creditos_pelas_devolucoes_de_vendas_icms | `credito_devolucao` | numeric(15) |  |  | Créditos pelas devoluções de vendas ICMS diferencial alíq. UF destino |
| debitos_servicos_de_transp_icms_dif_de_a | `debito_servicos_transporte_origem` | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF destino |
| debito_servicos_transporte_destino | `debito_servicos_transporte_destino` | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF destino |
| creditos_pelas_anulacoes_de_servicos_de | `credito_anulacao_servicos_transporte_origem` | numeric(13) |  |  | Créditos pelas anulações de serviços de transp. iniciados em outra UF - ICMS dif. de alíq. |
| credito_anulacao_servicos_transporte_des | `credito_anulacao_servicos_transporte_destino` | numeric(13) |  |  | Créditos pelas anulações de serviços de transp. iniciados em outra UF - ICMS dif. de alíq. |
| debito_servicos_transporte_origem_uf_emp | `debito_servicos_transporte_origem_uf_empresa` | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF origem (UF da empresa ativa) |
| debito_servicos_transporte_destino_uf_cl | `debito_servicos_transporte_destino_uf_cliente` | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF destino (UF do cliente) |
| debito_servicos_transporte_origem_uf_emp_c | `debito_servicos_transporte_origem_uf_empresa_igual` | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF origem (UF da empresa ativa nota com UF do cliente igual empresa) |
| debito_servicos_transporte_origem_uf_emp_c_c | `debito_servicos_transporte_origem_uf_empresa_diferente` | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF origem (UF da empresa ativa nota com UF do cliente diferente empresa) |
| debito_servicos_transporte_destino_uf_cl_c | `debito_servicos_transporte_destino_uf_cliente_igual` | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF destino (UF do cliente com UF do cliente igual empresa) |
| debito_servicos_transporte_destino_uf_cl_c_c | `debito_servicos_transporte_destino_uf_cliente_diferente` | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF destino (UF do cliente com UF do cliente diferente empresa) |
| uf_envolvida_na_operacao_de_transporte | `uf_envolvida_operacao_transporte` | char(1) |  |  | UF envolvida na operação de transporte |
| transf_saldo_credor_icms_difal_uf_origem | `transferencia_saldo_credor_icms_difal_uf` | numeric(13) |  |  | Transf. saldo credor ICMS DIFAL UF origem/destino para apuração no ICMS próprio |
| transf_saldo_devedor_icms_difal_uf_orige | `transferencia_saldo_devedor_icms_difal_uf` | numeric(13) |  |  | Transf. saldo devedor ICMS DIFAL UF origem/destino para apuração no ICMS próprio |
| debitos_entradas | `valor_debitos_entradas` | numeric(13) |  |  | Débitos Entradas |
| estorno_conforme_beneficio_art_530_lri_r | `estorno_conforme_beneficio_art_530_lri_ricms` | numeric(13) |  |  | Estorno Conforme Benefício Art. 530-LRI RICMS |
| estorno_conforme_beneficio_art_530_lri_r_c | `estorno_conforme_beneficio_art_530_lri_ricms_devolucao` | numeric(13) |  |  | Estorno Conforme Benefício Art. 530-LRI RICMS - Devolução |
| estorno_de_debitos_recolhimento_junto_ao | `estorno_debito_recolhimento_junto_icms_st` | numeric(13) |  |  | Estorno de débitos recolhimento junto ao ICMS ST |
| estorno_credito_devolucoes_recolhimento | `estorno_credito_devolucoes_recolhimento_junto_icms_st` | numeric(13) |  |  | Estorno credito devolucoes recolhimento junto ICMS ST |
| outros_craditos_lanaados | `outros_creditos_lancado` | numeric(15) |  |  | Outros CrÃ©ditos - LanÃ§ados |
| outros_debitos_lancados | `outros_debitos_lancado` | numeric(15) |  |  | Outros Débitos - Lançados |
| soma_dos_valores_a_recolher_e_credito_pe | `valor_recolher_credito_devolucoes` | numeric(13) |  |  | Soma dos valores (a recolher e crédito pelas devoluções de vendas) para geração de relatório |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `sigla_da_uf` (eq/in), `vencimento` (entre/gte/lte), `uf_envolvida_na_operacao_de_transporte` (eq/in)

## efsdoimp_pis_cofins_reducao_linear_aproveitamento_credito

**SALDO DOS IMPOSTOS - PIS/COFINS REDUCAO LINEAR - APROVEITAMENTO DE CREDITO** — tabela `EFSDOIMP_PIS_COFINS_REDUCAO_LINEAR_APROVEITAMENTO_CREDITO` (5.990 linhas)

SALDO DOS IMPOSTOS - PIS/COFINS REDUCAO LINEAR - APROVEITAMENTO DE CREDITO. 5.990 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SCP, I_RECOLHIMENTO, CST.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SCP, I_RECOLHIMENTO, CST`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 6.150 linhas, 420 empresa(s), DATA_SIM de 2026-04-01 a 2026-09-01.
- cst_06_aliquota_zero_07_isencao: valores reais fora do comentário do banco (6=3.075, 7=3.075); tratar o domínio como hipótese.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | EMPRESA |
| imposto | `codi_imp` | integer(4) |  |  | IMPOSTO |
| competencia | `data_sim` | date(4) |  |  | COMPETENCIA |
| periodicidade | `pdic_sim` | integer(4) |  |  | PERIODICIDADE |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | SEQUENCIAL DO SCP |
| sequencial_do_recolhimento | `i_recolhimento` | integer(4) |  |  | SEQUENCIAL DO RECOLHIMENTO |
| cst_06_aliquota_zero_07_isencao | `cst` | tinyint(1) |  | efsdoimp_pis_cofins_reducao_linear_aproveitamento_credito_cst_06_aliqu | CST (06-ALIQUOTA ZERO/07-ISENCAO) |
| saldo_disponivel | `saldo_disponivel` | numeric(13) |  |  | SALDO DISPONIVEL |
| saldo_disponivel_base | `saldo_disponivel_base` | numeric(13) |  |  | SALDO DISPONIVEL - BASE |
| saldo_utilizado | `saldo_utilizado` | numeric(13) |  |  | SALDO UTILIZADO |
| saldo_utilizado_base | `saldo_utilizado_base` | numeric(13) |  |  | SALDO UTILIZADO - BASE |
| saldo_a_transportar | `saldo_atransportar` | numeric(13) |  |  | SALDO A TRANSPORTAR |
| saldo_a_transportar_base | `saldo_atransportar_base` | numeric(13) |  |  | SALDO A TRANSPORTAR - BASE |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `sequencial_do_scp` (eq/in), `sequencial_do_recolhimento` (eq/in), `cst_06_aliquota_zero_07_isencao` (eq/in)

## efsdoimp_parcelas

**Saldo dos Impostos Parcelados** — tabela `efsdoimp_parcelas` (4.469 linhas)

Saldo dos Impostos Parcelados. 4.469 linhas no catálogo; chave: codi_emp, codi_imp, data_sim, pdic_sim, parc_simp.

- **Chave:** `codi_emp, codi_imp, data_sim, pdic_sim, parc_simp`
- **Empresa:** `codi_emp`
- **Período:** `data_sim`
- **Ordem padrão:** `data_sim desc`, `codi_imp asc`, `pdic_sim asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4.469 linhas, 63 empresa(s), data_sim de 2017-12-01 a 2026-03-01.
- Colunas expostas nulas em 100% das linhas (3): numero_do_acordo, codigo_da_receita, descricao_complementar.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| parcela_do_imposto | `parc_simp` | integer(4) |  |  | Parcela do imposto |
| valor_da_parcela | `valor_simp` | numeric(13) |  |  | Valor da Parcela |
| vencimento_da_parcela | `vcto_simp` | date(4) |  |  | Vencimento da Parcela |
| valor_pago_do_imposto | `vlrpago_simp` | numeric(13) |  |  | Valor pago do imposto |
| classe_de_vencimento | `classe_simp` | integer(4) |  |  | Classe de vencimento |
| numero_do_acordo | `acordo_simp` | char(15) |  |  | Numero do acordo |
| codigo_da_receita | `codigo_receita` | char(6) |  |  | Código da receita |
| descricao_complementar | `descricao_complementar` | varchar(255) |  |  | Descrição complementar |
| parcelar_o_imposto_icms_diferencial_de_a | `parcelar_difali` | char(1) |  |  | Parcelar o imposto ICMS diferencial de alíquota - DIFALI |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `parcela_do_imposto` (eq/in), `vencimento_da_parcela` (entre/gte/lte), `numero_do_acordo` (eq/in), `codigo_da_receita` (eq/in), `descricao_complementar` (contem/prefixo), `parcelar_o_imposto_icms_diferencial_de_a` (eq/in)

## efsdoimp_por_uf_sp

**Saldo dos Impostos - Por UF - SP** — tabela `EFSDOIMP_POR_UF_SP` (4.073 linhas)

Saldo dos Impostos - Por UF - SP. 4.073 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4.075 linhas, 155 empresa(s), DATA_SIM de 2017-01-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| sigla_da_uf | `sigla_uf` | char(2) |  |  | Sigla da UF |
| outros_debitos | `outros_debitos_lancado` | numeric(15) |  |  | Outros débitos |
| outros_creditos | `outros_creditos_lancado` | numeric(15) |  |  | Outros créditos |
| estorno_de_debitos | `estorno_debitos_lancado` | numeric(15) |  |  | Estorno de débitos |
| estorno_de_creditos | `estorno_creditos_lancado` | numeric(15) |  |  | Estorno de créditos |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `sigla_da_uf` (eq/in)

## efsdoimp_irpj_irrf_retido

**Saldo dos Impostos - IRRF Retido** — tabela `EFSDOIMP_IRPJ_IRRF_RETIDO` (4.062 linhas)

Saldo dos Impostos - IRRF Retido. 4.062 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, NATUREZA, PERIODO_APURACAO, TIPO_RETENCAO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, NATUREZA, PERIODO_APURACAO, TIPO_RETENCAO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4.071 linhas, 298 empresa(s), DATA_SIM de 2017-03-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| data | `data_sim` | date(4) |  |  | Data |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| natureza | `natureza` | integer(4) |  |  | Natureza |
| periodo_de_apuracao_da_retencao | `periodo_apuracao` | date(4) |  |  | Período de apuração da retenção |
| tipo_retencao_1_retido_2_propaganda | `tipo_retencao` | integer(4) |  |  | Tipo retenção - 1-Retido / 2-Propaganda |
| valor_retido | `valor_retido` | numeric(13) |  |  | Valor Retido |
| valor_retido_utilizado | `valor_retido_utilizado` | numeric(13) |  |  | Valor Retido Utilizado |
| valor_retido_disponivel | `valor_retido_disponivel` | numeric(13) |  |  | Valor Retido Disponível |

**Filtros:** `imposto` (eq/in), `data` (eq/in), `periodicidade` (eq/in), `natureza` (eq/in), `periodo_de_apuracao_da_retencao` (eq/in), `tipo_retencao_1_retido_2_propaganda` (eq/in)

## efsdoimp_por_recolhimento_por_data

**Saldo dos Impostos - Detalhamento dos Impostos por Código de Recolhimento - Por Data** — tabela `EFSDOIMP_POR_RECOLHIMENTO_POR_DATA` (2.557 linhas)

Saldo dos Impostos - Detalhamento dos Impostos por Código de Recolhimento - Por Data. 2.557 linhas no catálogo; chave: CODI_IMP, PDIC_SIM, CODI_EMP, DATA_SIM, I_RECOLHIMENTO, PERIODO.

- **Chave:** `CODI_IMP, PDIC_SIM, CODI_EMP, DATA_SIM, I_RECOLHIMENTO, PERIODO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_VENCIMENTO`
- **Ordem padrão:** `DATA_VENCIMENTO desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2.557 linhas, 2 empresa(s), DATA_VENCIMENTO de 2020-01-16 a 2026-02-13.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| sequencial_do_recolhimento | `i_recolhimento` | integer(4) |  |  | Sequencial do Recolhimento |
| periodo | `periodo` | date(4) |  |  | Período |
| codigo_do_recolhimento | `codigo_recolhimento` | char(6) |  |  | Código do recolhimento |
| valor_contabil_entrada | `valor_contabil_entrada` | numeric(13) |  |  | Valor Contábil Entrada |
| base_calculo_entrada | `base_calculo_entrada` | numeric(13) |  |  | Base Cálculo Entrada |
| valor_imposto_entrada | `valor_imposto_entrada` | numeric(13) |  |  | Valor Imposto Entrada |
| valor_isentas_entrada | `valor_isentas_entrada` | numeric(13) |  |  | Valor Isentas Entrada |
| valor_outras_entrada | `valor_outras_entrada` | numeric(13) |  |  | Valor Outras Entrada |
| base_calculo | `base_calculo` | numeric(13) |  |  | Base Cálculo |
| saldo_devedor | `saldo_devedor` | numeric(13) |  |  | Saldo Devedor |
| valor_a_recolher | `valor_a_recolher` | numeric(13) |  |  | Valor a Recolher |
| valor_diferido | `valor_diferido` | numeric(13) |  |  | Valor Diferido |
| valor_diferido_anterior | `valor_diferido_anterior` | numeric(13) |  |  | Valor Diferido Anterior |
| valor_da_compensacao_de_pagamento_indevi | `compensacao_pagamento_indevido_maior` | numeric(13) |  |  | Valor da Compensação de pagamento indevido ou a maior |
| valor_de_ressarcimento_compensacao_de_pi | `ressarcimento_compensacao_pis_cofins` | numeric(13) |  |  | Valor de Ressarcimento/Compensação de PIS/COFINS |
| parcela | `parcela` | integer(4) |  |  | Parcela |
| valor_pago | `valor_pago` | numeric(13) |  |  | Valor pago |
| data_do_vencimento | `data_vencimento` | date(4) |  |  | Data do vencimento |
| outras_compensacoes | `outras_compensacoes` | numeric(13) |  |  | Outras compensações |

**Filtros:** `imposto` (eq/in), `pdic_sim` (eq/in), `competencia` (eq/in), `sequencial_do_recolhimento` (eq/in), `periodo_referencia` (eq/in), `data_do_vencimento` (entre/gte/lte), `codigo_do_recolhimento` (eq/in)

## efsdoimp_csll_csll_retido

**Saldo dos Impostos - CSLL Retido** — tabela `EFSDOIMP_CSLL_CSLL_RETIDO` (2.466 linhas)

Saldo dos Impostos - CSLL Retido. 2.466 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, NATUREZA, PERIODO_APURACAO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, NATUREZA, PERIODO_APURACAO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2.471 linhas, 188 empresa(s), DATA_SIM de 2017-06-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| data | `data_sim` | date(4) |  |  | Data |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| natureza | `natureza` | integer(4) |  |  | Natureza |
| periodo_de_apuracao_da_retencao | `periodo_apuracao` | date(4) |  |  | Período de apuração da retenção |
| valor_retido | `valor_retido` | numeric(13) |  |  | Valor Retido |
| valor_retido_utilizado | `valor_retido_utilizado` | numeric(13) |  |  | Valor Retido Utilizado |
| valor_retido_disponivel | `valor_retido_disponivel` | numeric(13) |  |  | Valor Retido Disponível |

**Filtros:** `imposto` (eq/in), `data` (eq/in), `periodicidade` (eq/in), `natureza` (eq/in), `periodo_de_apuracao_da_retencao` (eq/in)

## efsdoimp_pis_cofins_reducao_linear_por_nota

**Saldo do Impostos - PIS/COFINS Reducao Linear por Nota** — tabela `EFSDOIMP_PIS_COFINS_REDUCAO_LINEAR_POR_NOTA` (2.420 linhas)

Saldo do Impostos - PIS/COFINS Reducao Linear por Nota. 2.420 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SCP, I_RECOLHIMENTO, FILIAL, CST, ALIQUOTA, PERCENTUAL_LINEAR, OPERACAO, TIPO_MOV, DOCUMENTO, CHAVE.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SCP, I_RECOLHIMENTO, FILIAL, CST, ALIQUOTA, PERCENTUAL_LINEAR, OPERACAO, TIPO_MOV, DOCUMENTO, CHAVE`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_MOV`
- **Ordem padrão:** `DATA_MOV desc`, `CODI_IMP asc`, `DATA_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2.420 linhas, 7 empresa(s), DATA_MOV de 2026-04-01 a 2026-09-30.
- operacao_a_acrescimo_r_reducao: todos os valores reais estão no comentário do banco (A=2.358, R=62).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |
| sequencial_do_recolhimento | `i_recolhimento` | integer(4) |  |  | Sequencial do Recolhimento |
| codigo_filial | `filial` | integer(4) |  |  | Código Filial |
| cst | `cst` | integer(4) |  |  | CST |
| aliquota_do_imposto | `aliquota` | numeric(7) |  |  | Aliquota do Imposto |
| percentual_da_reducao_linear | `percentual_linear` | numeric(5) |  |  | Percentual da Reducao Linear |
| operacao_a_acrescimo_r_reducao | `operacao` | char(1) |  | efsdoimp_pis_cofins_reducao_linear_por_nota_operacao_a_ | Operacao (A - Acrescimo / R - Reducao) |
| tipo_do_movimento_tipo_mov_in_s_v_b_cfe | `tipo_mov` | char(3) |  |  | Tipo do Movimento TIPO_MOV IN (S, V, B, CFE, ED, Z, ZB, RMD) |
| documento | `documento` | numeric(15) |  |  | Documento |
| chave_de_acesso | `chave` | varchar(255) |  |  | Chave de acesso |
| data_movimento | `data_mov` | date(4) |  |  | Data movimento |
| base_de_calculo | `base_calculo` | numeric(13) |  |  | Base de Calculo |
| valor_do_imposto | `valor_imposto` | numeric(13) |  |  | Valor do Imposto |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `sequencial_do_scp` (eq/in), `sequencial_do_recolhimento` (eq/in), `codigo_filial` (eq/in), `cst` (eq/in), `aliquota_do_imposto` (eq/in), `percentual_da_reducao_linear` (eq/in), `operacao_a_acrescimo_r_reducao` (eq/in), `tipo_do_movimento_tipo_mov_in_s_v_b_cfe` (eq/in), `documento` (eq/in), `chave_de_acesso` (eq/in), `data_movimento` (entre/gte/lte)

## efsdoimp_pis_cofins_contabilizacao_detalhamento_credito

**Saldo do Impostos - Contabilização do PIS/COFINS Crédito** — tabela `EFSDOIMP_PIS_COFINS_CONTABILIZACAO_DETALHAMENTO_CREDITO` (2.339 linhas)

Saldo do Impostos - Contabilização do PIS/COFINS Crédito. 2.339 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SCP, I_RECOLHIMENTO, CONSOLIDADO, CODIGO_CREDITO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SCP, I_RECOLHIMENTO, CONSOLIDADO, CODIGO_CREDITO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2.345 linhas, 53 empresa(s), DATA_SIM de 2017-07-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| scp | `i_scp` | integer(4) |  |  | SCP |
| recolhimento | `i_recolhimento` | integer(4) |  |  | Recolhimento |
| consolidado | `consolidado` | char(1) |  |  | Consolidado |
| codigo_do_credito | `codigo_credito` | integer(4) |  |  | Código do crédito |
| credito_pelas_entradas | `credito_pelas_entradas` | numeric(13) |  |  | Crédito pelas entradas |
| valor_credito_extemporaneo | `valor_credito_extemporaneo` | numeric(13) |  |  | Valor crédito extemporaneo |
| devolucao_compras | `devolucao_compras` | numeric(13) |  |  | Devolução compras |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `scp` (eq/in), `recolhimento` (eq/in), `consolidado` (eq/in), `codigo_do_credito` (eq/in)

## efsdoimp_pis_cofins_detalhamento_credito

**Saldo do Impostos - Detalhamentos do PIS/COFINS - Créditos** — tabela `EFSDOIMP_PIS_COFINS_DETALHAMENTO_CREDITO` (2.209 linhas)

Saldo do Impostos - Detalhamentos do PIS/COFINS - Créditos. 2.209 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_CREDITO, PERIODO_APURACAO, ALIQUOTA_PERCENTUAL, ALIQUOTA_VALOR, I_SCP, I_RECOLHIMENTO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_CREDITO, PERIODO_APURACAO, ALIQUOTA_PERCENTUAL, ALIQUOTA_VALOR, I_SCP, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2.211 linhas, 36 empresa(s), DATA_SIM de 2017-07-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| codigo_do_credito | `codigo_credito` | integer(4) |  |  | Código do crédito |
| periodo_em_que_o_credito_foi_apurado | `periodo_apuracao` | date(4) |  |  | Período em que o crédito foi apurado |
| valor_da_aliquota_do_imposto | `aliquota_percentual` | numeric(7) |  |  | Valor da alíquota do imposto |
| aliquota_em_moeda_quando_o_calculo_e_por | `aliquota_valor` | numeric(13) |  |  | Alíquota em moeda (quando o cálculo é por unidade de medida) |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |
| sequencial_do_recolhimento | `i_recolhimento` | integer(4) |  |  | Sequencial do Recolhimento |
| valor_da_base_de_calculo | `base_calculo` | numeric(13) |  |  | Valor da base de cálculo |
| quantidade_base_de_calculo_quando_o_calc | `quantidade_base_calculo` | numeric(13) |  |  | Quantidade - base de cálculo (quando o cálculo é por unidade de medida) |
| valor_do_imposto_apurado | `valor_apurado` | numeric(13) |  |  | Valor do imposto apurado |
| valor_dos_ajustes_de_acrescimo | `valor_acrescimo` | numeric(13) |  |  | Valor dos ajustes de acréscimo |
| valor_dos_ajustes_de_reducao | `valor_reducao` | numeric(13) |  |  | Valor dos ajustes de redução |
| valor_do_credito_disponivel | `valor_disponivel` | numeric(13) |  |  | Valor do crédito disponível |
| valor_do_credito_utilizado_no_periodo | `valor_utilizado` | numeric(13) |  |  | Valor do crédito utilizado no período |
| valor_do_credito_a_trasportar_para_o_per | `valor_a_transportar` | numeric(13) |  |  | Valor do crédito a trasportar para o período seguinte |
| valor_do_credito_das_devolucoes_de_venda | `valor_devolucao_venda` | numeric(13) |  |  | Valor do crédito das devoluções de venda |
| valor_do_credito_diferido | `valor_diferido` | numeric(13) |  |  | Valor do crédito diferido |
| valor_da_base_de_calculo_credito_vincula | `base_calculo_receita_cumulativa` | numeric(13) |  |  | Valor da base de cálculo - Crédito vinculado Receita Cumulativa |
| quantidade_base_calculo_receita_cumulati | `quantidade_base_calculo_receita_cumulativa` | numeric(13) |  |  | Quantidade - base de cálculo (quando o cálculo é por unidade de medida) - Crédito vinculado Receita Cumulativa |
| valor_dos_ajustes_de_reducao_credito_vin | `valor_reducao_receita_cumulativa` | numeric(13) |  |  | Valor dos ajustes de redução - Crédito vinculado Receita Cumulativa |
| valor_do_credito_de_ressarcimento_restit | `valor_ressarcimento` | numeric(13) |  |  | Valor do crédito de ressarcimento - Restituição, Ressarcimento e Compensação |
| valor_do_credito_do_compensacao_restitui | `valor_compensacao` | numeric(13) |  |  | Valor do crédito do compensação - Restituição, Ressarcimento e Compensação |
| valor_total_do_credito_apurado_na_escrit | `valor_credito_normal_apurado` | numeric(13) |  |  | Valor total do crédito apurado na Escrituração Fiscal Digital |
| valor_de_credito_extemporaneo_apurado | `valor_credito_extemporaneo_apurado` | numeric(13) |  |  | Valor de Crédito Extemporâneo Apurado |
| ajuste_de_reducao_scp | `valor_reducao_scp` | numeric(13) |  |  | Ajuste de redução - SCP |
| creditos_prescritos_em_decorrencia_do_te | `valor_credito_prescrito` | numeric(13) |  |  | Créditos prescritos em decorrência do término do prazo decadencial |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `codigo_do_credito` (eq/in), `periodo_em_que_o_credito_foi_apurado` (eq/in), `valor_da_aliquota_do_imposto` (eq/in), `aliquota_em_moeda_quando_o_calculo_e_por` (eq/in), `sequencial_do_scp` (eq/in), `sequencial_do_recolhimento` (eq/in)

## efsdoimp_scp

**Saldo dos Impostos - SCP** — tabela `EFSDOIMP_SCP` (2.041 linhas)

Saldo dos Impostos - SCP. 2.041 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SCP.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SCP`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_VENCIMENTO`
- **Ordem padrão:** `DATA_VENCIMENTO desc`, `CODI_IMP asc`, `DATA_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2.041 linhas, 4 empresa(s), DATA_VENCIMENTO de 2015-02-13 a 2026-10-30.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |
| parcela | `parcela` | integer(4) |  |  | Parcela |
| saldo_a_recolher | `saldo_recolher` | numeric(13) |  |  | Saldo a recolher |
| saldo_devedor | `saldo_devedor` | numeric(13) |  |  | Saldo devedor |
| saldo_credor | `saldo_credor` | numeric(13) |  |  | Saldo credor |
| saldo_diferido | `saldo_diferido` | numeric(13) |  |  | Saldo diferido |
| saldo_credor_anterior | `saldo_credor_anterior` | numeric(13) |  |  | Saldo credor anterior |
| saldo_diferido_anterior | `saldo_diferido_anterior` | numeric(13) |  |  | Saldo diferido anterior |
| valor_pago | `valor_pago` | numeric(13) |  |  | Valor pago |
| data_do_vencimento | `data_vencimento` | date(4) |  |  | Data do vencimento |
| ajuste_de_reducao_devolucoes_de_debitos | `devolucao_empreen_periodo_final` | numeric(13) |  |  | Ajuste de redução - Devoluções de débitos empreendimento imobiliário utilizado no período |
| ajuste_de_reducao_periodo_anterior_devol | `devolucao_empreen_periodo_anterior` | numeric(13) |  |  | Ajuste de redução período anterior - Devolução |
| ajuste_de_reducao_devolucao | `devolucao_empreen_periodo_atual` | numeric(13) |  |  | Ajuste de redução - Devolução |
| ajuste_de_reducao_para_o_periodo_seguint | `devolucao_empreen_periodo_seguinte` | numeric(13) |  |  | Ajuste de redução para o período seguinte - Devolução |
| ajuste_de_reducao_devolucoes_de_vendas_u | `devolucao_venda_periodo_final` | numeric(13) |  |  | Ajuste de redução - Devoluções de vendas utilizado no período |
| devolucao_venda_periodo_anterior | `devolucao_venda_periodo_anterior` | numeric(13) |  |  | Ajuste de redução período anterior - Devolução |
| devolucao_venda_periodo_atual | `devolucao_venda_periodo_atual` | numeric(13) |  |  | Ajuste de redução - Devolução |
| devolucao_venda_periodo_seguinte | `devolucao_venda_periodo_seguinte` | numeric(13) |  |  | Ajuste de redução para o período seguinte - Devolução |
| retencoes | `retencao` | numeric(13) |  |  | Retenções |
| compensacao_de_pagamento_indevido_ou_a_m | `compensacao_pagamento_a_maior` | numeric(13) |  |  | Compensação de pagamento indevido ou a maior |
| compensacao_de_ressarcimento_de_ipi | `compensacao_ressarcimento_ipi` | numeric(13) |  |  | Compensação de ressarcimento de IPI |
| compensacao_de_saldo_negativo_de_irpj | `compensacao_ressarcimento_irpj` | numeric(13) |  |  | Compensação de saldo negativo de IRPJ |
| compensacao_de_saldo_negativo_de_csll | `compensacao_ressarcimento_csll` | numeric(13) |  |  | Compensação de saldo negativo de CSLL |
| compensacao_de_irrf_cooperativas_de_trab | `compensacao_irrf_cooperativa` | numeric(13) |  |  | Compensação de IRRF cooperativas de trabalho |
| compensacao_de_irrf_juros_sobre_capital | `compensacao_irrf_juro_capital` | numeric(13) |  |  | Compensação de IRRF juros sobre capital próprio |
| debito_unidade_imobiliaria | `debito_unidade_imobiliaria` | numeric(13) |  |  | Débito unidade imobiliária |
| devolucao_de_venda | `devolucao_venda` | numeric(13) |  |  | Devolução de venda |
| retencao_aproveitada | `retencao_aproveitada` | numeric(13) |  |  | Retenção aproveitada |
| debito_para_contabilizacao | `debito_contabilizacao` | numeric(13) |  |  | Débito para contabilização |
| total_de_creditos | `credito_periodo_final` | numeric(13) |  |  | Total de créditos |
| ajuste_de_acrescimo_periodo_anterior_scp | `credito_periodo_anterior` | numeric(13) |  |  | Ajuste de acréscimo período anterior - SCP |
| ajuste_de_acrescimo_scp | `credito_periodo_atual` | numeric(13) |  |  | Ajuste de acréscimo - SCP |
| ajuste_de_acrescimo_para_o_periodo_segui | `credito_periodo_seguinte` | numeric(13) |  |  | Ajuste de acréscimo para o período seguinte - SCP |
| ajuste_de_reducao_devolucoes_de_creditos | `credito_devolucao_empreen_periodo_final` | numeric(13) |  |  | Ajuste de redução - Devoluções de créditos empreendimentos imobiliário utilizado no período |
| credito_devolucao_empreen_periodo_anteri | `credito_devolucao_empreen_periodo_anterior` | numeric(13) |  |  | Ajuste de redução período anterior - Devolução |
| credito_devolucao_empreen_periodo_atual | `credito_devolucao_empreen_periodo_atual` | numeric(13) |  |  | Ajuste de redução - Devolução |
| credito_devolucao_empreen_periodo_seguin | `credito_devolucao_empreen_periodo_seguinte` | numeric(13) |  |  | Ajuste de redução para o período seguinte - Devolução |
| ajuste_de_reducao_devolucoes_de_compras | `credito_devolucao_compra_periodo_final` | numeric(13) |  |  | Ajuste de redução - Devoluções de compras utilizado no período |
| credito_devolucao_compra_periodo_anterio | `credito_devolucao_compra_periodo_anterior` | numeric(13) |  |  | Ajuste de redução período anterior - Devolução |
| credito_devolucao_compra_periodo_atual | `credito_devolucao_compra_periodo_atual` | numeric(13) |  |  | Ajuste de redução - Devolução |
| credito_devolucao_compra_periodo_seguint | `credito_devolucao_compra_periodo_seguinte` | numeric(13) |  |  | Ajuste de redução para o período seguinte - Devolução |
| saidas_para_contabilizacao | `saida_contabilizacao` | numeric(13) |  |  | Saídas para contabilização |
| devolucao_de_compra_fora_do_periodo_para | `devolucao_compra_fora_periodo_contabilizacao` | numeric(13) |  |  | Devolução de compra fora do período para contabilização |
| devolucao_de_compra_para_contabilizacao | `devolucao_compra_periodo_contabilizacao` | numeric(13) |  |  | Devolução de compra para contabilização |
| devolucao_de_venda_para_contabilizacao | `devolucao_venda_contabilizacao` | numeric(13) |  |  | Devolução de venda para contabilização |
| credito_custo_incorrido | `credito_custo_incorrido` | numeric(13) |  |  | Crédito custo incorrido |
| credito_presumido_orcado | `credito_presumido_orcado` | numeric(13) |  |  | Crédito presumido orçado |
| reducao_receita_cumulativa | `reducao_receita_cumulativa` | numeric(13) |  |  | Redução receita cumulativa |
| credito_devolucao_de_compra_no_periodo | `credito_devolucao_compra_periodo` | numeric(13) |  |  | Crédito devolução de compra no período |
| saida_valor_receita | `irpj_saida_valor_receita` | numeric(13) |  |  | Saída valor receita |
| saida_valor_contabil | `irpj_saida_valor_contabil` | numeric(13) |  |  | Saída valor contábil |
| saida_base_de_calculo | `irpj_saida_base_calculo` | numeric(13) |  |  | Saída base de cálculo |
| servico_valor_receita | `irpj_servico_valor_receita` | numeric(13) |  |  | Serviço valor receita |
| servico_valor_contabil | `irpj_servico_valor_contabil` | numeric(13) |  |  | Serviço valor contábil |
| servico_base_de_calculo | `irpj_servico_base_calculo` | numeric(13) |  |  | Serviço base de cálculo |
| entrada_valor_receita | `irpj_entrada_valor_receita` | numeric(13) |  |  | Entrada valor receita |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `sequencial_do_scp` (eq/in), `data_do_vencimento` (entre/gte/lte)

## efsdoimp_pis_cofins_detalhamento_debito_devolucao

**Saldo do Impostos - Detalhamentos do PIS/COFINS - Déditos - Devoluçoes** — tabela `EFSDOIMP_PIS_COFINS_DETALHAMENTO_DEBITO_DEVOLUCAO` (1.786 linhas)

Saldo do Impostos - Detalhamentos do PIS/COFINS - Déditos - Devoluçoes. 1.786 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_CONTRIBUICAO, ALIQUOTA_PERCENTUAL, ALIQUOTA_VALOR, PERIODO_APURACAO, CODI_ENT, FILIAL, I_SCP, I_RECOLHIMENTO, CODI_SAI.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_CONTRIBUICAO, ALIQUOTA_PERCENTUAL, ALIQUOTA_VALOR, PERIODO_APURACAO, CODI_ENT, FILIAL, I_SCP, I_RECOLHIMENTO, CODI_SAI`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.786 linhas, 13 empresa(s), DATA_SIM de 2018-05-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| codigo_da_contribuicao | `codigo_contribuicao` | integer(4) |  |  | Código da contribuição |
| valor_da_aliquota_do_imposto | `aliquota_percentual` | numeric(7) |  |  | Valor da alíquota do imposto |
| aliquota_em_moeda_quando_o_calculo_e_por | `aliquota_valor` | numeric(13) |  |  | Alíquota em moeda (quando o cálculo é por unidade de medida) |
| periodo_em_que_o_dedito_foi_apurado | `periodo_apuracao` | date(4) |  |  | Período em que o dédito foi apurado |
| codigo_da_nota_de_entrada | `codi_ent` | integer(4) |  |  | Código da nota de entrada |
| filial | `filial` | integer(4) |  |  | Filial |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |
| sequencial_do_recolhimento | `i_recolhimento` | integer(4) |  |  | Sequencial do Recolhimento |
| codigo_da_nota_de_saida | `codi_sai` | integer(4) |  |  | Código da nota de saída |
| valor_base_de_calculo | `base_calculo` | numeric(13) |  |  | Valor base de cálculo |
| quantidade_base_de_calculo_quando_o_calc | `quantidade_base_calculo` | numeric(13) |  |  | Quantidade - base de cálculo (quando o cálculo é por unidade de medida) |
| valor_do_imposto | `valor` | numeric(13) |  |  | Valor do imposto |
| valor_disponivel_em_periodo_anterior | `valor_disponivel_anterior` | numeric(13) |  |  | Valor disponível em período anterior |
| valor_disponivel_no_periodo | `valor_disponivel` | numeric(13) |  |  | Valor disponível no período |
| valor_utilizado_no_periodo | `valor_utilizado` | numeric(13) |  |  | Valor utilizado no período |
| valor_a_transportar_para_o_periodo_segui | `valor_a_transportar` | numeric(13) |  |  | Valor a transportar para o período seguinte |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `codigo_da_contribuicao` (eq/in), `valor_da_aliquota_do_imposto` (eq/in), `aliquota_em_moeda_quando_o_calculo_e_por` (eq/in), `periodo_em_que_o_dedito_foi_apurado` (eq/in), `codigo_da_nota_de_entrada` (eq/in), `filial` (eq/in), `sequencial_do_scp` (eq/in), `sequencial_do_recolhimento` (eq/in), `codigo_da_nota_de_saida` (eq/in)

## efsdoimp_pis_cofins_detalhamento_credito_bases

**Saldo do Impostos - Detalhamentos do PIS/COFINS - Créditos - Bases do imposto** — tabela `EFSDOIMP_PIS_COFINS_DETALHAMENTO_CREDITO_BASES` (1.551 linhas)

Saldo do Impostos - Detalhamentos do PIS/COFINS - Créditos - Bases do imposto. 1.551 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_CREDITO, PERIODO_APURACAO, ALIQUOTA_PERCENTUAL, ALIQUOTA_VALOR, NATUREZA_BASE_CREDITO, CST, I_SCP, I_RECOLHIMENTO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_CREDITO, PERIODO_APURACAO, ALIQUOTA_PERCENTUAL, ALIQUOTA_VALOR, NATUREZA_BASE_CREDITO, CST, I_SCP, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.555 linhas, 35 empresa(s), DATA_SIM de 2018-01-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| codigo_do_credito | `codigo_credito` | integer(4) |  |  | Código do crédito |
| periodo_em_que_o_credito_foi_apurado | `periodo_apuracao` | date(4) |  |  | Período em que o crédito foi apurado |
| valor_da_aliquota_do_imposto | `aliquota_percentual` | numeric(7) |  |  | Valor da alíquota do imposto |
| aliquota_em_moeda_quando_o_calculo_e_por | `aliquota_valor` | numeric(13) |  |  | Alíquota em moeda (quando o cálculo é por unidade de medida) |
| natureza_da_base_de_calculo_do_credito | `natureza_base_credito` | integer(4) |  |  | Natureza da base de cálculo do crédito |
| cst_vinculado_ao_credito | `cst` | integer(4) |  |  | CST vinculado ao crédito |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |
| sequencial_do_recolhimento | `i_recolhimento` | integer(4) |  |  | Sequencial do Recolhimento |
| base_de_calculo_total | `base_total` | numeric(13) |  |  | Base de cálculo total |
| base_de_calculo_cumulativa | `base_cumulativa` | numeric(13) |  |  | Base de cálculo cumulativa |
| base_de_calculo_nao_cumulativa | `base_nao_cumulativa` | numeric(13) |  |  | Base de cálculo não cumulativa |
| base_de_calculo_vinculada_a_receita | `base_vinculada` | numeric(13) |  |  | Base de cálculo vinculada a receita |
| base_de_calculo_total_quando_o_calculo_e | `quantidade_base_calculo` | numeric(13) |  |  | Base de cálculo total (quando o cálculo é por unidade de medida) |
| base_de_calculo_vinculada_quando_o_calcu | `quantidade_base_calculo_vinculado` | numeric(13) |  |  | Base de cálculo vinculada (quando o cálculo é por unidade de medida) |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `codigo_do_credito` (eq/in), `periodo_em_que_o_credito_foi_apurado` (eq/in), `valor_da_aliquota_do_imposto` (eq/in), `aliquota_em_moeda_quando_o_calculo_e_por` (eq/in), `natureza_da_base_de_calculo_do_credito` (eq/in), `cst_vinculado_ao_credito` (eq/in), `sequencial_do_scp` (eq/in), `sequencial_do_recolhimento` (eq/in)

## efsdoimp_subtri_por_uf_pr

**Saldo dos Impostos - Substituição Tributária Por PR** — tabela `EFSDOIMP_SUBTRI_POR_UF_PR` (1.443 linhas)

Saldo dos Impostos - Substituição Tributária Por PR. 1.443 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.443 linhas, 7 empresa(s), DATA_SIM de 2010-01-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| sigla_da_uf | `sigla_uf` | char(2) |  |  | Sigla da UF |
| recolhimento | `i_recolhimento` | integer(4) |  |  | Recolhimento |
| valor_do_icms_sobre_estoque_produtos_inc | `debito_icms_sobre_estoque` | numeric(13) |  |  | Valor do ICMS sobre estoque - Produtos incluídos SUBTRI |
| debito_referente_ao_fecop_pr_icms_st | `debito_fecop_icms_st` | numeric(13) |  |  | Débito referente ao FECOP-PR - ICMS ST |
| devolucao_referente_ao_fecop_pr_icms_st | `devolucao_fecop_icms_st` | numeric(13) |  |  | Devolução referente ao FECOP-PR - ICMS ST |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `sigla_da_uf` (eq/in), `recolhimento` (eq/in)

## efsdoimp_pis_cofins_detalhamento_debito_devolucao_aproveitam

**Saldo do Impostos - Detalhamentos do PIS/COFINS - Déditos - Devoluçoes - Aproveitamento** — tabela `EFSDOIMP_PIS_COFINS_DETALHAMENTO_DEBITO_DEVOLUCAO_APROVEITAMENTO` (1.352 linhas)

Saldo do Impostos - Detalhamentos do PIS/COFINS - Déditos - Devoluçoes - Aproveitamento. 1.352 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_CONTRIBUICAO, ALIQUOTA_PERCENTUAL, ALIQUOTA_VALOR, PERIODO_APURACAO, CODI_ENT, FILIAL, CODIGO_CONTRIBUICAO_APROVEITADO, ALIQUOTA_PERCENTUAL_APROVEITADO, ALIQUOTA_VALOR_APROVEITADO, I_SCP, I_RECOLHIMENTO, CODI_SAI.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_CONTRIBUICAO, ALIQUOTA_PERCENTUAL, ALIQUOTA_VALOR, PERIODO_APURACAO, CODI_ENT, FILIAL, CODIGO_CONTRIBUICAO_APROVEITADO, ALIQUOTA_PERCENTUAL_APROVEITADO, ALIQUOTA_VALOR_APROVEITADO, I_SCP, I_RECOLHIMENTO, CODI_SAI`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.352 linhas, 12 empresa(s), DATA_SIM de 2018-05-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| codigo_da_contribuicao | `codigo_contribuicao` | integer(4) |  |  | Código da contribuição |
| valor_da_aliquota_do_imposto | `aliquota_percentual` | numeric(7) |  |  | Valor da alíquota do imposto |
| aliquota_em_moeda_quando_o_calculo_e_por | `aliquota_valor` | numeric(13) |  |  | Alíquota em moeda (quando o cálculo é por unidade de medida) |
| periodo_em_que_o_dedito_foi_apurado | `periodo_apuracao` | date(4) |  |  | Período em que o dédito foi apurado |
| codigo_da_nota_de_entrada | `codi_ent` | integer(4) |  |  | Código da nota de entrada |
| filial | `filial` | integer(4) |  |  | Filial |
| codigo_da_contribuicao_aproveitada | `codigo_contribuicao_aproveitado` | integer(4) |  |  | Código da contribuição aproveitada |
| valor_da_aliquota_do_imposto_aproveitado | `aliquota_percentual_aproveitado` | numeric(7) |  |  | Valor da alíquota do imposto aproveitado |
| aliquota_valor_aproveitado | `aliquota_valor_aproveitado` | numeric(13) |  |  | Alíquota em moeda (quando o cálculo é por unidade de medida) aproveitado |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |
| sequencial_do_recolhimento | `i_recolhimento` | integer(4) |  |  | Sequencial do Recolhimento |
| codigo_da_nota_de_saida | `codi_sai` | integer(4) |  |  | Código da nota de saída |
| valor_aproveitado | `valor_aproveitado` | numeric(13) |  |  | Valor aproveitado |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `codigo_da_contribuicao` (eq/in), `valor_da_aliquota_do_imposto` (eq/in), `aliquota_em_moeda_quando_o_calculo_e_por` (eq/in), `periodo_em_que_o_dedito_foi_apurado` (eq/in), `codigo_da_nota_de_entrada` (eq/in), `filial` (eq/in), `codigo_da_contribuicao_aproveitada` (eq/in), `valor_da_aliquota_do_imposto_aproveitado` (eq/in), `aliquota_valor_aproveitado` (eq/in), `sequencial_do_scp` (eq/in), `sequencial_do_recolhimento` (eq/in)

## efsdoimp_receita_impostos_majoracao

**Saldo dos Impostos - Receita Impostos Majoração** — tabela `EFSDOIMP_RECEITA_IMPOSTOS_MAJORACAO` (1.000 linhas)

Saldo dos Impostos - Receita Impostos Majoração. 1.000 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, PERIODO_APURACAO, ALIQUOTA_BASE_CALCULO_CSLL, ALIQUOTA_BASE_CALCULO_IRPJ.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, PERIODO_APURACAO, ALIQUOTA_BASE_CALCULO_CSLL, ALIQUOTA_BASE_CALCULO_IRPJ`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.030 linhas, 242 empresa(s), DATA_SIM de 2026-03-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| periodo | `data_sim` | date(4) |  |  | Período |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| periodo_origem_base_majorada | `periodo_apuracao` | date(4) |  |  | Período origem base majorada |
| aliquota_da_base_de_calculo_csll | `aliquota_base_calculo_csll` | numeric(7) |  |  | Alíquota da base de cálculo CSLL |
| aliquota_da_base_de_calculo_irpj | `aliquota_base_calculo_irpj` | numeric(7) |  |  | Alíquota da base de cálculo IRPJ |
| aliquota_da_base_de_calculo_csll_exceden | `aliquota_base_calculo_csll_excedente` | numeric(7) |  |  | Alíquota da base de cálculo CSLL excedente |
| aliquota_da_base_de_calculo_irpj_exceden | `aliquota_base_calculo_irpj_excedente` | numeric(7) |  |  | Alíquota da base de cálculo IRPJ excedente |
| valor_da_base_de_calculo | `valor_base_calculo` | numeric(13) |  |  | Valor da base de cálculo |
| valor_da_base_de_calculo_nao_excedente | `valor_base_calculo_nao_excedente` | numeric(13) |  |  | Valor da base de cálculo não excedente |
| valor_da_base_de_calculo_excedente | `valor_base_calculo_excedente` | numeric(13) |  |  | Valor da base de cálculo excedente |
| valor_da_base_de_calculo_reduzida_nao_ex | `valor_base_calculo_reduzida_nao_excedente` | numeric(13) |  |  | Valor da base de cálculo reduzida não Excedente |
| valor_da_base_de_calculo_reduzida_excede | `valor_base_calculo_reduzida_excedente` | numeric(13) |  |  | Valor da base de cálculo reduzida excedente |
| valor_credito_limite_trimestral | `valor_credito_limite_trimestral` | numeric(13) |  |  | Valor da base de cálculo reduzida excedente |
| valor_da_base_de_calculo_excedente_com_a | `valor_base_calculo_excedente_com_aliquota` | numeric(13) |  |  | Valor da base de cálculo excedente com alíquota do imposto aplicada |

**Filtros:** `imposto` (eq/in), `periodo` (eq/in), `periodicidade` (eq/in), `periodo_origem_base_majorada` (eq/in), `aliquota_da_base_de_calculo_csll` (eq/in), `aliquota_da_base_de_calculo_irpj` (eq/in)

## efsdoimp_simples_nacional_prorrogacao

**Saldo dos Impostos - Simples Nacional Prorrogação** — tabela `EFSDOIMP_SIMPLES_NACIONAL_PRORROGACAO` (640 linhas)

Saldo dos Impostos - Simples Nacional Prorrogação. 640 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, TIPO_PRORROGACAO, VENCIMENTO, PRORROGACAO, FILIAL.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, TIPO_PRORROGACAO, VENCIMENTO, PRORROGACAO, FILIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 640 linhas, 110 empresa(s), DATA_SIM de 2020-03-01 a 2021-05-01.
- tipo_prorrogacao_1_federais_2_estaduais: valores reais fora do comentário do banco (5=231); tratar o domínio como hipótese.
- prorrogacao_f_federais_e_estaduais_m_mun: valores reais fora do comentário do banco (Q=231, ME=63); tratar o domínio como hipótese.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| periodo | `data_sim` | date(4) |  |  | Período |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| tipo_prorrogacao_1_federais_2_estaduais | `tipo_prorrogacao` | integer(4) |  | efsdoimp_simples_nacional_prorrogacao_tipo_prorro | Tipo Prorrogação (1-FEDERAIS / 2-ESTADUAIS / 3-MUNICIPAIS / 4-OUTROS) |
| vencimento | `vencimento` | date(4) |  |  | Vencimento |
| prorrogacao_f_federais_e_estaduais_m_mun | `prorrogacao` | char(3) |  | efsdoimp_simples_nacional_prorrogacao_prorrogacao | Prorrogação (F-Federais / E-Estaduais / M-Municipais) |
| filial | `filial` | integer(4) |  |  | Filial |
| saldo_devedor | `saldo_devedor` | numeric(13) |  |  | Saldo devedor |
| valor_pago | `valor_pago` | numeric(13) |  |  | Valor Pago |
| saldo_diferido | `saldo_diferido` | numeric(13) |  |  | Saldo diferido |
| saldo_diferido_anterior | `saldo_diferido_anterior` | numeric(13) |  |  | Saldo diferido anterior |

**Filtros:** `imposto` (eq/in), `periodo` (eq/in), `periodicidade` (eq/in), `tipo_prorrogacao_1_federais_2_estaduais` (eq/in), `vencimento` (eq/in), `prorrogacao_f_federais_e_estaduais_m_mun` (eq/in), `filial` (eq/in)

## efsdoimp_estadual_mg

**Saldo dos Impostos - Estadual MG** — tabela `EFSDOIMP_ESTADUAL_MG` (535 linhas)

Saldo dos Impostos - Estadual MG. 535 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 536 linhas, 19 empresa(s), DATA_SIM de 2017-07-01 a 2026-09-01.
- n_apurado_antes_da_sai_56215_s_apurado_d: todos os valores reais estão no comentário do banco (S=435, N=101).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| credito_presumido_transporte_rodoviario | `credito_presumido_transporte_rodoviario` | numeric(13) |  |  | Crédito presumido transporte rodoviário de passageiros - Art. 75, XXXI |
| ctrc_emitido_pelo_transportador_c_icms_r | `ctrc_emitido_pelo_transportador` | numeric(13) |  |  | CTRC emitido pelo transportador, c/ ICMS responsabilidade do remetente/alienante |
| credito_presumido_bares_rest_e_similares | `credito_presumido_bar_rest_fornec_refeicoes` | numeric(13) |  |  | Crédito presumido bares, rest. e similares no fornec. de refeições - Art. 75, XXXIX |
| credito_presumido_bar_rest_demais_operac | `credito_presumido_bar_rest_demais_operacoes` | numeric(13) |  |  | Crédito presumido bares, rest. e similares nas demais operações - Art. 75, XXXIX |
| devolucao_cred_pres_bares_rest_e_similar | `devolucao_cred_presu_bar_rest_fornec_refeicoes` | numeric(13) |  |  | Devolução créd. pres. bares, rest. e similares fornec. de refeições - Art. 75, XXXIX |
| devolucao_cred_presu_bar_rest_demais_ope | `devolucao_cred_presu_bar_rest_demais_operacoes` | numeric(13) |  |  | Devolução créd. pres. bares, rest. e similares demais operações - Art. 75, XXXIX |
| credito_de_icms_conf_aliquota_do_simples | `credito_conforme_aliquota_sn` | numeric(13) |  |  | Crédito de ICMS conf. alíquota do Simples Nacional - Art. 23, LC 123/06 |
| devolucao_de_mercadoria_adquirida_de_sim | `devolucao_mercadoria_adquirida_sn` | numeric(13) |  |  | Devolução de mercadoria adquirida de Simples Nacional |
| credito_de_icms_recebido_de_produtor_rur | `credito_icms_recebido_produtor_rural` | numeric(13) |  |  | Crédito de ICMS recebido de Produtor Rural em transferência - Art. 75, XXXIII |
| estorno_credito_de_icms_recebido_de_prod | `estorno_credito_icms_recebido_produtor_rural` | numeric(13) |  |  | Estorno Crédito de ICMS recebido de Produtor Rural em transferência - Art. 75, XXXIII |
| credito_presumido_de_peixes_abate_ou_pro | `credito_presumido_carnes` | numeric(13) |  |  | Crédito presumido de peixes, abate ou proces. de aves e de gado - Art. 75, IV RICMS |
| devolucao_cred_pres_peixes_abate_ou_proc | `credito_presumido_carnes_devolucao` | numeric(13) |  |  | Devolução créd. pres. peixes, abate ou proces. de aves e de gado - Art. 75, IV RICMS |
| credito_presumido_com_carga_tributaria_e | `credito_presumido_carga_tributaria` | numeric(13) |  |  | Crédito presumido com carga tributária equivalente a 3% - Art. 75, XIV |
| devolucao_de_credito_presumido_com_carga | `credito_presumido_carga_tributaria_devolucao` | numeric(13) |  |  | Devolução de crédito presumido com carga tributária equivalente a 3% - Art. 75, XIV |
| estorno_do_icms_nas_operacoes_com_carga | `credito_presumido_carga_tributaria_estorno` | numeric(13) |  |  | Estorno do ICMS nas operações com carga tributária equivalente a 3% - Art. 75, XIV |
| credito_presumido_ao_fabricante_de_alcoo | `credito_presumido_acucar_alcool` | numeric(13) |  |  | Crédito presumido ao fabricante de álcool ou açúcar - Art.75, XXXII |
| devolucao_do_credito_presumido_ao_fabric | `credito_presumido_acucar_alcool_devolucao` | numeric(13) |  |  | Devolução do crédito presumido ao fabricante de álcool ou açúcar - Art.75, XXXII |
| estorno_do_icms_nas_operacoes_do_fabrica | `credito_presumido_acucar_alcool_estorno` | numeric(13) |  |  | Estorno do ICMS nas operações do fabricante de álcool ou açúcar - Art.75, XXXII |
| credito_presumido_de_polpas_doces_conser | `credito_presumido_doces` | numeric(13) |  |  | Crédito presumido de polpas, doces, conservas, molhos e outros - Art.75, XII |
| devolucao_do_credito_pres_de_polpas_doce | `credito_presumido_doces_devolucao` | numeric(13) |  |  | Devolução do crédito pres. de polpas, doces, conservas, molhos e outros - Art.75, XII |
| estorno_do_icms_nas_operacoes_de_polpas | `credito_presumido_doces_estorno` | numeric(13) |  |  | Estorno do ICMS nas operações de polpas, doces, conservas, molhos e outros - Art.75, XII |
| credito_icms_antecipado_aquisicao_de_arr | `credito_icms_antecipado_aquisicao_arroz` | numeric(13) |  |  | Crédito ICMS antecipado aquisição de arroz |
| credito_icms_antecipado_outras_antecipac | `credito_icms_antecipado_outras_antecipacoes` | numeric(13) |  |  | Crédito ICMS antecipado outras antecipações |
| utilizacao_de_saldo_credor_de_icms_para | `utilizacao_saldo_credor_icms_extincao_debitos_fiscais` | numeric(13) |  |  | Utilização de saldo credor de ICMS para extinção de débitos fiscais |
| valor_a_ser_deduzido_do_icms_st_sobre_es | `valor_deduzido_icms_st_estoque` | numeric(13) |  |  | Valor a ser deduzido do ICMS ST sobre estoques - Art. 7° da Resolução 4.855/15 |
| credito_de_icms_sobre_estoques_na_exclus | `credito_icms_st_estoque_exclusao` | numeric(13) |  |  | Crédito de ICMS sobre estoques na exclusão merc. da ST - Art. 23 da Res. 4.855/15 |
| credito_icms_st_estoque_exclusao_disponi | `credito_icms_st_estoque_exclusao_disponivel` | numeric(13) |  |  | Crédito de ICMS sobre estoques na exclusão merc. da ST - Art. 23 da Res. 4.855/15 para mês seguinte |
| credito_icms_st_estoque_exclusao_anterio | `credito_icms_st_estoque_exclusao_anterior` | numeric(13) |  |  | Crédito de ICMS sobre estoques na exclusão merc. da ST - Art. 23 da Res. 4.855/15 anterior |
| credito_presumido_artefatos_joalheria_co | `credito_presumido_artefatos_joalheria_saida` | numeric(13) |  |  | Crédito presumido artefatos joalheria com carga tributária de 5%-Art.75,XXVIII,RICMS - Saída |
| credito_presumido_artefatos_joalheria_re | `credito_presumido_artefatos_joalheria_reducao_z` | numeric(13) |  |  | Crédito presumido artefatos joalheria com carga tributária de 5%-Art.75,XXVIII,RICMS - Redução Z |
| credito_presumido_artefatos_joalheria_de | `credito_presumido_artefatos_joalheria_devolucao` | numeric(13) |  |  | Crédito presumido artefatos joalheria com carga tributária de 5%-Art.75,XXVIII,RICMS - Devolução |
| estorno_do_credito_estimulo_devolucao_da | `valor_estorno_credito_estimulo` | numeric(13) |  |  | Estorno do Crédito Estímulo (Devolução da compra) |
| credito_ativo_imobilizado_de_periodos_an | `credito_ativo_imobilizado_anterior` | numeric(13) |  |  | Crédito Ativo Imobilizado de períodos anteriores |
| desconto_conforme_termo_de_aceite_da_lei | `desconto_conforme_termo_aceite_lei_22549_17` | numeric(13) |  |  | Desconto conforme Termo de Aceite da Lei 22.549/17 e Decreto 47.226/17 |
| outros_creditos_devolucao_difali | `outros_creditos_devolucao_difali` | numeric(13) |  |  | Outros créditos devolução DIFALI |
| estorno_debitos_devolucao_compra | `estorno_debito_devolucao_compra` | numeric(13) |  |  | Estorno debitos devolução compra |
| n_apurado_antes_da_sai_56215_s_apurado_d | `ncal_bares_restaurantes_e_similares` | char(1) |  | efsdoimp_estadual_mg_n_apurado_antes_da_ | (N = Apurado antes da SAI 56215 / S = Apurado depois da SAI 56215) |
| estorno_do_fem_de_mercadorias_alcancadas | `estorno_fem_mercadorias_credito_presumido` | numeric(13) |  |  | Estorno do FEM de mercadorias alcançadas pelo crédito presumido |
| recebimento_de_credito_por_transferencia | `recebimento_credito_por_transferencia` | numeric(13) |  |  | Recebimento de crédito por Transferência |
| estorno_de_credito_de_icms_conforme_art | `estorno_credito_icms_art_71_ricms` | numeric(13) |  |  | Estorno de crédito de ICMS conforme Art. 71 do RICMS |
| restituicao_de_icms_op_10_art_66_do_rimc | `restituicao_icms_op_art_66` | numeric(13) |  |  | Restituição de ICMS OP - §10 Art. 66 do RIMCS |
| restituicao_de_icms_st_art_23_anexo_xv_d | `restituicao_icms_st_art_23` | numeric(13) |  |  | Restituição de ICMS ST - Art. 23, Anexo XV do RICMS |
| estorno_de_debito_nas_operacoes_com_ct_e | `estorno_debito_operacoes_cte_substituto` | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |
| credito_na_aquisicao_de_combustiveis_par | `credito_aquisicao_combustivel_insumo` | numeric(13) |  |  | Crédito na aquisição de combustíveis para insumo - Conv. ICMS nº 199/22 e 15/23 |
| estorno_do_fem_de_mercadorias_devolvidas | `estorno_fem_mercadorias_credito_presumido_devolucao` | numeric(13) |  |  | Estorno do FEM de mercadorias devolvidas alcançadas pelo crédito presumido |
| estorno_do_fem_fundo_de_erradicacao_da_m | `estorno_credito_fem_icms_devolucao` | numeric(13) |  |  | Estorno do FEM - Fundo de Erradicação da Miséria - devolução |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `n_apurado_antes_da_sai_56215_s_apurado_d` (eq/in)

## efsdoimp_estadual_rj

**Saldo dos Impostos - Estadual RJ** — tabela `EFSDOIMP_ESTADUAL_RJ` (523 linhas)

Saldo dos Impostos - Estadual RJ. 523 linhas no catálogo; chave: CODI_EMP, DATA_SIM, PDIC_SIM, CODI_IMP.

- **Chave:** `CODI_EMP, DATA_SIM, PDIC_SIM, CODI_IMP`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_VENCIMENTO_ICMS_DOCUMENTOS_EXTEMPORANEOS`
- **Ordem padrão:** `DATA_VENCIMENTO_ICMS_DOCUMENTOS_EXTEMPORANEOS desc`, `DATA_SIM asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 523 linhas, 18 empresa(s), DATA_VENCIMENTO_ICMS_DOCUMENTOS_EXTEMPORANEOS de 2021-02-01 a 2026-10-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| credito_presumido_saidas_internas_e_inte | `credito_presumido_informatica_importados` | numeric(13) |  |  | Crédito presumido saídas internas e interestaduais de produtos importados |
| credito_presumido_saidas_interestaduais | `credito_presumido_informatica_nacionais` | numeric(13) |  |  | Crédito presumido saídas interestaduais de produtos nacionais |
| credito_presumido_saidas_de_produto_indu | `credito_presumido_informatica_fluminense` | numeric(13) |  |  | Crédito presumido saídas de produto industrializado no estabelecimento Fluminense |
| devolucao_produto_informatica_eletronico | `estorno_credito_informatica_importados` | numeric(13) |  |  | Devolução produto informática, eletrônicos e eletrodomésticos Importados |
| estorno_credito_informatica_nacionais | `estorno_credito_informatica_nacionais` | numeric(13) |  |  | Devolução produto informática, eletrônicos e eletrodomésticos Nacionais |
| estorno_credito_informatica_fluminense | `estorno_credito_informatica_fluminense` | numeric(13) |  |  | Devolução produto informática, eletrônicos e eletrodomésticos Fluminense |
| estorno_credito_informatica_total | `estorno_credito_informatica_total` | numeric(13) |  |  | Devolução produto informática, eletrônicos e eletrodomésticos |
| credito_presumido_nas_saidas_com_embarca | `credito_presumido_embarcacoes_nauticas` | numeric(13) |  |  | Crédito presumido nas saídas com embarcações náuticas - Dec. 41.681/2009 |
| devolucao_do_cred_presumido_nas_saidas_c | `devolucao_credito_presumido_embarcacoes_nauticas` | numeric(13) |  |  | Devolução do créd. presumido nas saídas com embarcações náuticas - Dec. 41.681/2009 |
| fecp_pelas_saidas_com_embarcacoes_nautic | `deducao_fecp_embarcacoes_nauticas` | numeric(13) |  |  | FECP pelas saídas com embarcações náuticas - Dec. 41.681/2009 |
| credito_presumido_transporte | `credito_presumido_transporte` | numeric(13) |  |  | Crédito presumido transporte 20% |
| credito_de_icms_conf_aliquota_do_simples | `credito_conforme_aliquota_sn` | numeric(13) |  |  | Crédito de ICMS conf. Alíquota do Simples Nacional - Art.23, LC 123/06 |
| devolucao_de_mercadoria_adquirida_de_sim | `devolucao_mercadoria_adquirida_sn` | numeric(13) |  |  | Devolução de mercadoria adquirida de Simples Nacional |
| transferencia_de_saldo_credor_art_1_livr | `transferencia_saldo_credor` | numeric(13) |  |  | Transferência de saldo credor - Art. 1, Livro III do RICMS |
| recebimento_de_saldo_credor_art_1_livro | `recebimento_saldo_credor` | numeric(13) |  |  | Recebimento de saldo credor - Art. 1, Livro III do RICMS |
| estorno_proporcional_saidas_isentas_nao | `saidas_icms_prop_isenta_nao_trib` | numeric(13) |  |  | Estorno Proporcional - Saídas isentas não tributadas |
| estorno_proporcional_icms_servicos_isent | `servicos_icms_prop_isenta_nao_trib` | numeric(13) |  |  | Estorno Proporcional - ICMS Serviços isentas não tributadas |
| estorno_proporcional_saidas_totais_isent | `saidas_totais_icms_prop_isenta_nao_trib` | numeric(13) |  |  | Estorno Proporcional - Saídas totais isentas não tributadas |
| estorno_proporcional_proporcao_saidas_se | `prop_saidas_serv_icms_prop_isenta_nao_trib` | numeric(5) |  |  | Estorno Proporcional - Proporção Saídas/Serviços isentas não tributadas |
| estorno_proporcional_total_creditos_icms | `total_creditos_icms_prop_isenta_nao_trib` | numeric(13) |  |  | Estorno Proporcional - Total Créditos ICMS |
| estorno_proporcional_estorno_credito_icm | `estorno_credito_icms_prop_isenta_nao_trib` | numeric(13) |  |  | Estorno Proporcional - Estorno Credito ICMS |
| credito_presumido_saidas_plasticos_proce | `credito_presumido_saidas_plasticos_processo_fabril` | numeric(13) |  |  | Crédito Presumido Saídas Plásticos Processo Fabril |
| devolucao_credito_presumido_saidas_plast | `credito_presumido_saidas_plasticos_processo_fabril_devolucao` | numeric(13) |  |  | Devolução Crédito Presumido Saídas Plásticos Processo Fabril |
| credito_presumido_saidas_plasticos_consu | `credito_presumido_saidas_plasticos_consumidor_final` | numeric(13) |  |  | Crédito Presumido Saídas Plásticos Consumidor Final |
| credito_presumido_saidas_plasticos_consu_c | `credito_presumido_saidas_plasticos_consumidor_final_devolucao` | numeric(13) |  |  | Devolução Crédito Presumido Saídas Plásticos Consumidor Final |
| estorno_do_icms_nas_operacoes_com_credit | `estorno_icms_oper_cred_presumido_dec_42649_2010` | numeric(13) |  |  | Estorno do ICMS nas operações com crédito presumido conforme Dec. 42.649/2010 |
| credito_ref_ao_icms_proprio_nao_apropria | `credito_icms_nao_apropriado_aquisicao_merc_icms_st` | numeric(13) |  |  | Crédito ref. ao ICMS próprio não apropriado na aquisição de merc. sujeita ao ICMS-ST devolvida |
| estorno_de_icms_nas_operacoes_com_credit | `estorno_credito_presumido_transporte` | numeric(13) |  |  | Estorno de ICMS nas operações com Crédito Presumido Transportes |
| saidas_inter_riolog_lei_4173_03_art_3_i | `saidas_inter_riolog_lei_4173_03_art_3_i` | numeric(13) |  |  | Saídas interestaduais - RIOLOG - Lei 4.173/03, Art.3º, I |
| entradas_inter_riolog_lei_4173_03_art_3 | `entradas_inter_riolog_lei_4173_03_art_3_ii` | numeric(13) |  |  | Entradas interestaduais - RIOLOG - Lei 4.173/03, Art.3º, II |
| entradas_por_transf_riolog_lei_4173_03_a | `entradas_por_transf_riolog_lei_4173_03_art_3_iii` | numeric(13) |  |  | Entradas por transferência - RIOLOG - Lei 4.173/03, Art.3º, III |
| entradas_internas_riolog_lei_4_173_03_ar | `entradas_internas_riolog_lei_4173_03_art_3_iv` | numeric(13) |  |  | Entradas internas - RIOLOG - Lei 4.173/03, Art.3º, IV |
| devolucao_cred_pres_saidas_interest_riol | `devolucao_cred_pres_saidas_inter_riolog_lei_4173_03_art_3_i` | numeric(13) |  |  | Devolução créd. pres. saídas interest. - RIOLOG - Lei 4.173/03, Art.3º, I |
| devolucao_cred_pres_entradas_interest_ri | `devolucao_cred_pres_entradas_inter_riolog_lei_4173_03_art_3_ii` | numeric(13) |  |  | Devolução créd. pres. entradas interest. - RIOLOG - Lei 4.173/03, Art.3º, II |
| devolucao_cred_pres_entradas_transfer_ri | `devolucao_cred_pres_entradas_por_transf_riolog_lei_4173_03_art_3_iii` | numeric(13) |  |  | Devolução créd. pres. entradas transfer. - RIOLOG - Lei 4.173/03, Art.3º, III |
| devolucao_cred_pres_entradas_internas_ri | `devolucao_cred_pres_entradas_internas_riolog_lei_4173_03_art_3_iv` | numeric(13) |  |  | Devolução créd. pres. entradas internas - RIOLOG - Lei 4.173/03, Art.3º, IV |
| icms_minimo_a_recolher_conforme_art_5o_d | `valor_icms_minimo_riolog` | numeric(13) |  |  | ICMS mínimo a recolher conforme Art. 5º da Lei 4.173/2003 - RIOLOG |
| icms_minimo_pago_conforme_art_5o_da_lei | `valor_pago_icms_minimo_riolog` | numeric(13) |  |  | ICMS mínimo pago conforme Art. 5º da Lei 4.173/2003 - RIOLOG |
| devolucao_mercadoria_adquirida_simples_n | `devolucao_mercadoria_adquirida_simples_nacional` | numeric(13) |  |  | Devolução de mercadoria adquirida de Simples Nacional |
| credito_icms_devolucao_de_compra_uso_e_c | `outros_creditos_cred_icms_dev_compra` | numeric(13) |  |  | Crédito ICMS - Devolução de compra uso e consumo ou imobilizado |
| recuperacao_do_difali_devolucao_de_compr | `outros_creditos_recup_difali_dev_compra` | numeric(13) |  |  | Recuperação do Difali - Devolução de compra |
| estorno_proporcional_saida_com_reducao_d | `estorno_credito_icms_prop_possuir_red_bc` | numeric(13) |  |  | Estorno proporcional saída com redução da base de cálculo – Produtos da cesta básica |
| estorno_do_icms_complementar | `estorno_icms_complementar` | numeric(13) |  |  | Estorno do ICMS Complementar |
| icms_complementar_valor_a_recolher | `icms_complementar_valor_recolher` | numeric(13) |  |  | ICMS Complementar - valor a recolher |
| icms_complementar_valor_pago | `icms_complementar_valor_pago` | numeric(13) |  |  | ICMS Complementar - valor pago |
| icms_complementar_data_de_vencimento | `icms_complementar_data_vencimento` | date(4) |  |  | ICMS Complementar - data de vencimento |
| icms_complementar_codigo_de_recolhimento | `icms_complementar_codigo_recolhimento` | char(6) |  |  | ICMS Complementar - código de recolhimento |
| estorno_icms_documentos_extemporaneo | `estorno_icms_documentos_extemporaneos` | numeric(13) |  |  | Estorno ICMS documentos extemporaneo |
| icms_documentos_extemporaneo_recolher | `icms_documentos_extemporaneos_recolher` | numeric(13) |  |  | ICMS documentos extemporaneo recolher |
| valor_pago_icms_documento_extemporaneo | `valor_pago_icms_documentos_extemporaneos` | numeric(13) |  |  | Valor pago ICMS documento extemporaneo |
| data_vencimento_icms_documentos_extempor | `data_vencimento_icms_documentos_extemporaneos` | date(4) |  |  | Data vencimento ICMS documentos extemporaneo |
| credito_presumido_fornecimento_de_refeic | `credito_presumido_fornecimento_refeicoes` | numeric(13) |  |  | Crédito Presumido Fornecimento de refeições - Lei 9.355/2021 |
| credito_presumido_demais_operacoes | `credito_presumido_demais_operacoes` | numeric(13) |  |  | Crédito Presumido Demais operações - Lei 9.355/2021 |
| devolucao_credito_presumido_fornecimento | `devolucao_credito_presumido_fornecimento_refeicoes` | numeric(13) |  |  | Devolução Crédito Presumido Fornecimento de refeições - Lei 9.355/2021 |
| devolucao_credito_presumido_demais_opera | `devolucao_credito_presumido_demais_operacoes` | numeric(13) |  |  | Devolução Crédito Presumido Demais operações - Lei 9.355/2021 |
| estorno_credito_presumido_pelas_entradas | `estorno_credito_presumido_pelas_entradas` | numeric(13) |  |  | Estorno do ICMS nas operações com crédito presumido - Lei 9.355/2021 |

**Filtros:** `competencia` (eq/in), `pdic_sim` (eq/in), `imposto` (eq/in), `icms_complementar_data_de_vencimento` (entre/gte/lte), `data_vencimento_icms_documentos_extempor` (entre/gte/lte), `icms_complementar_codigo_de_recolhimento` (eq/in)

## efsdoimp_subtri_por_uf_rj

**Saldo dos Impostos - Substituição Tributária Por RJ** — tabela `EFSDOIMP_SUBTRI_POR_UF_RJ` (508 linhas)

Saldo dos Impostos - Substituição Tributária Por RJ. 508 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 508 linhas, 22 empresa(s), DATA_SIM de 2010-01-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| sigla_da_uf | `sigla_uf` | char(2) |  |  | Sigla da UF |
| recolhimento | `i_recolhimento` | integer(4) |  |  | Recolhimento |
| debito_icms_sobre_estoque | `debito_icms_sobre_estoque` | numeric(13) |  |  | Débito ICMS Sobre Estoque |
| debito_fecp_st | `debito_fecp_st` | numeric(13) |  |  | Débito FECP/ST |
| saldo_devedor_fecp_st | `saldo_devedor_fecp_st` | numeric(13) |  |  | Saldo devedor FECP/ST |
| valor_fecp_st_aproveitado | `valor_fecp_st_aproveitado` | numeric(13) |  |  | Valor FECP/ST Aproveitado |
| valor_st_at_responsavel_solidario | `valor_stat_devolucao_resp_solidario` | numeric(13) |  |  | Valor ST/AT Responsavel Solidario |
| complemento_de_icms_st | `complemento_subtri` | numeric(13) |  |  | Complemento de ICMS ST |
| ressarcimento_de_icms_st | `ressarcimento_subtri` | numeric(13) |  |  | Ressarcimento de ICMS ST |
| ressarcimento_de_icms_st_periodo_anterio | `ressarcimento_subtri_periodo_anterior` | numeric(13) |  |  | Ressarcimento de ICMS ST período anterior |
| ressarcimento_de_icms_st_periodo_seguint | `ressarcimento_subtri_periodo_seguinte` | numeric(13) |  |  | Ressarcimento de ICMS ST período seguinte |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `sigla_da_uf` (eq/in), `recolhimento` (eq/in)

## efsdoimp_subtri_por_uf_mg

**Saldo dos Impostos - Substituição Tributária Por MG** — tabela `EFSDOIMP_SUBTRI_POR_UF_MG` (431 linhas)

Saldo dos Impostos - Substituição Tributária Por MG. 431 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 432 linhas, 17 empresa(s), DATA_SIM de 2017-07-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| sigla_da_uf | `sigla_uf` | char(2) |  |  | Sigla da UF |
| recolhimento | `i_recolhimento` | integer(4) |  |  | Recolhimento |
| estorno_de_fem_fundo_de_erradicacao_da_m | `estorno_fem` | numeric(13) |  |  | Estorno de FEM - Fundo de Erradicação da Miséria |
| valor_do_ressarcimento_de_icms_de_substi | `valor_ressarcimento_cfop_1603` | numeric(13) |  |  | Valor do ressarcimento de ICMS de Substituição Tributária |
| saldo_antes_do_ressarcimento | `saldo_antes_do_ressarcimento` | numeric(13) |  |  | Saldo Antes do Ressarcimento |
| debito_icms_sobre_estoques_na_inclusao_m | `debito_icms_sobre_estoque_inclusao` | numeric(13) |  |  | Débito ICMS sobre estoques na inclusão merc. na ST - Art. 4° da Res. 4.855/15 |
| debito_icms_st_sobre_estoques_da_majorac | `debito_icms_sobre_estoque_majoracao` | numeric(13) |  |  | Débito ICMS ST sobre estoques da majoração de alíq. - Art. 5°, I da Res. 4.855/15 |
| debito_icms_st_sobre_estoques_do_adicion | `debito_icms_sobre_estoque_adicional` | numeric(13) |  |  | Débito ICMS ST sobre estoques do adicional de alíq. - Art. 5°, I da Res. 4.855/15 |
| complemento_de_icms_st_art_31_a_anexo_xv | `complemento_icms_st_art_31_anexo_xv_ricms` | numeric(13) |  |  | Complemento de ICMS ST - Art. 31-A, Anexo XV do RICMS |
| complemento_do_fem_art_31_b_3o_anexo_xv | `complemento_fem_art_31_anexo_xv_ricms` | numeric(13) |  |  | Complemento do FEM - Art. 31-B, § 3º, Anexo XV do RICMS |
| restituicao_de_icms_st_art_31_c_anexo_xv | `restituicao_icms_st_art_31_anexo_xv_ricms` | numeric(13) |  |  | Restituição de ICMS ST - Art. 31-C, Anexo XV do RICMS |
| restituicao_do_fem_art_31_d_3o_anexo_xv | `restituicao_fem_art_31_anexo_xv_ricms` | numeric(13) |  |  | Restituição do FEM - Art. 31-D, § 3º, Anexo XV do RICMS |
| parcela_correspondente_a_restituicao_do | `parcela_correspondente_restituicao_fem_art_31_anexo_xv_ricms` | numeric(13) |  |  | Parcela correspondente à restituição do FEM - Art. 31-D, § 3º, Anexo XV do RICMS |
| complemento_do_fem_adicionado_ao_icms_st | `complemento_fem_adicionado_icms_st_art_31_anexo_xv_ricms` | numeric(13) |  |  | Complemento do FEM adicionado ao ICMS ST - Art. 31-B, § 3º, Anexo XV do RICMS |
| restituicao_de_icms_st_art_23_anexo_xv_d | `restituicao_icms_st_art_23` | numeric(13) |  |  | Restituição de ICMS ST - Art. 23, Anexo XV do RICMS |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `sigla_da_uf` (eq/in), `recolhimento` (eq/in)

## efsdoimp_estadual_pe

**Saldo dos Impostos - Estadual PE** — tabela `EFSDOIMP_ESTADUAL_PE` (418 linhas)

Saldo dos Impostos - Estadual PE. 418 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_VENCIMENTO_ICMS_DOCUMENTOS_EXTEMPORANEOS`
- **Ordem padrão:** `DATA_VENCIMENTO_ICMS_DOCUMENTOS_EXTEMPORANEOS desc`, `CODI_IMP asc`, `DATA_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 418 linhas, 8 empresa(s), DATA_VENCIMENTO_ICMS_DOCUMENTOS_EXTEMPORANEOS de 2017-11-20 a 2026-10-20.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| valor_credito_presumido_transporte | `credito_presumido_transporte` | numeric(13) |  |  | Valor Crédito Presumido Transporte |
| cradito_icms_antecipado | `icms_antecipado_credito` | numeric(13) |  |  | CrÃ©dito ICMS Antecipado |
| estorno_cradito_icms_antecipado | `icms_antecipado_estorno_credito` | numeric(13) |  |  | Estorno crÃ©dito ICMS Antecipado |
| cradito_icms_antecipado_pelos_pagamentos | `icms_antecipado_credito_pagamentos` | numeric(13) |  |  | CrÃ©dito ICMS Antecipado pelos pagamentos |
| transf_saldo_credor_mes_seguinte_prodepe | `transf_saldo_credor_mes_seg_prodepe_industria` | numeric(13) |  |  | Transf. Saldo Credor Mês Seguinte PRODEPE Indústria |
| transf_saldo_credor_mes_seg_prodepe_cent | `transf_saldo_credor_mes_seg_prodepe_central_ent` | numeric(13) |  |  | Transf. Saldo Credor Mês Seguinte PRODEPE Central Entradas |
| transf_saldo_credor_mes_seg_prodepe_cent_c | `transf_saldo_credor_mes_seg_prodepe_central_sai` | numeric(13) |  |  | Transf. Saldo Credor Mês Seguinte PRODEPE Central Saídas |
| transf_saldo_credor_mes_anterior_prodepe | `transf_saldo_credor_mes_ant_prodepe_industria` | numeric(13) |  |  | Transf. Saldo Credor Mês Anterior PRODEPE Indústria |
| transf_saldo_credor_mes_ant_prodepe_cent | `transf_saldo_credor_mes_ant_prodepe_central_ent` | numeric(13) |  |  | Transf. Saldo Credor Mês Anterior PRODEPE Central Entradas |
| transf_saldo_credor_mes_ant_prodepe_cent_c | `transf_saldo_credor_mes_ant_prodepe_central_sai` | numeric(13) |  |  | Transf. Saldo Credor Mês Anterior PRODEPE Central Saídas |
| credito_presumido_prodepe_industria | `credito_presumido_prodepe_industria` | numeric(13) |  |  | Crédito Presumido PRODEPE Indústria |
| credito_presumido_prodepe_central_entrad | `credito_presumido_prodepe_central_entradas` | numeric(13) |  |  | Crédito Presumido PRODEPE Central Entradas |
| credito_presumido_prodepe_central_saidas | `credito_presumido_prodepe_central_saidas` | numeric(13) |  |  | Crédito Presumido PRODEPE Central Saídas |
| credito_presumido_prodeauto | `credito_presumido_prodeauto` | numeric(13) |  |  | Crédito Presumido PRODEAUTO |
| credito_presumido_prodepe_importacao_sai | `credito_presumido_prodepe_importacao_saidas_internas` | numeric(13) |  |  | Crédito Presumido PRODEPE Importação Saídas Internas |
| credito_presumido_prodepe_importacao_sai_c | `credito_presumido_prodepe_importacao_saidas_interestaduais` | numeric(13) |  |  | Crédito Presumido PRODEPE Importação Saídas Interestaduais |
| credito_presumido_prodepe_importacao_icm | `credito_presumido_prodepe_importacao_icms_entradas_importacao` | numeric(13) |  |  | Crédito Presumido PRODEPE Importação ICMS Entradas Importação |
| credito_ativo_imobilizado | `credito_ativo_imobilizado` | numeric(13) |  |  | Crédito Ativo Imobilizado |
| estorno_icms_documentos_extemporaneo | `estorno_icms_documentos_extemporaneos` | numeric(13) |  |  | Estorno ICMS documentos extemporaneo |
| icms_documentos_extemporaneo_recolher | `icms_documentos_extemporaneos_recolher` | numeric(13) |  |  | ICMS documentos extemporaneo recolher |
| valor_pago_icms_documento_extemporaneo | `valor_pago_icms_documentos_extemporaneos` | numeric(13) |  |  | Valor pago ICMS documento extemporaneo |
| data_vencimento_imcs_documentos_extempor | `data_vencimento_icms_documentos_extemporaneos` | date(4) |  |  | Data vencimento IMCS documentos extemporaneo |
| icms_st_creditado_nas_aquisicoes_interna | `outros_creditos_icms_st_creditado_aquis_internas` | numeric(13) |  |  | ICMS-ST creditado nas aquisições internas |
| icms_st_antecipacao_creditado_nas_aquisi | `outros_creditos_icms_st_creditado_aquis_interestaduais` | numeric(13) |  |  | ICMS-ST antecipação creditado nas aquisições interestaduais |
| estorno_de_debito_nas_operacoes_com_ct_e | `estorno_debito_operacoes_cte_substituto` | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |
| estorno_credito_presumido_atacadista | `estorno_credito_presumido_atacadista` | numeric(13) |  |  | Estorno de crédito presumido Decreto 38455/2012 |
| saldo_de_credito_presumido_periodo_anter | `saldo_credito_presumido_periodo_anterior_atacadista` | numeric(13) |  |  | Saldo de crédito presumido período anterior Decreto 38455/2012 |
| credituo_presumido_comercio_atacadista_d | `credito_presumido_comercio_atacadista` | numeric(13) |  |  | Crédituo presumido comércio atacadista Decreto 38455/2012 |
| recolhimento_especifico_sobre_vendas_a_c 🔒 | `recolhimento_especifico_vendas_consumidor_final` | numeric(13) |  |  | Recolhimento específico sobre vendas a consumidor final não inscrito no CNPJ |
| coluna_para_salvar_o_valor_amp_para_util | `aliquota_amp_atacadista` | numeric(11) |  |  | Coluna para salvar o valor AMP para utilizar nos relatórios |
| coluna_para_gravar_o_icms_antecipado_e_u | `icms_antecipado_atacadista` | numeric(13) |  |  | Coluna para gravar o icms antecipado e utilizar nos relatórios |
| credito_presumido_atacadista_que_nao_foi | `credito_presumido_atacadista_nao_aproveitado` | numeric(13) |  |  | Crédito Presumido Atacadista que não foi usado para utilizar no mes seguinte |
| credito_de_icms_monofasico_na_aquisicao | `credito_icms_monofasico_aquisicao_combustivel_insumo` | numeric(13) |  |  | Crédito de ICMS monofásico na aquisição de combustíveis para insumos conforme Convênios ICMS nº 199/2022 e 15/2023 |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `data_vencimento_imcs_documentos_extempor` (entre/gte/lte)

## efsdoimp_estadual_ba

**Saldo dos Impostos - Estadual BA** — tabela `EFSDOIMP_ESTADUAL_BA` (348 linhas)

Saldo dos Impostos - Estadual BA. 348 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 348 linhas, 12 empresa(s), DATA_SIM de 2013-01-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| valor_recebimento_por_transferencia_sald | `recebimento_por_transferencia_saldo_credor` | numeric(13) |  |  | Valor Recebimento por Transferência Saldo Credor |
| recebimento_por_transferencia_saldo_deve | `recebimento_por_transferencia_saldo_devedor` | numeric(13) |  |  | Valor Recebimento por Transferência Saldo Devedor |
| valor_transferencia_saldo_credor | `transferencia_saldo_credor` | numeric(13) |  |  | Valor Transferência Saldo Credor |
| valor_transferencia_saldo_devedor | `transferencia_saldo_devedor` | numeric(13) |  |  | Valor Transferência Saldo Devedor |
| recebimento_por_transferencia_saldo_cred | `recebimento_por_transferencia_saldo_credor_entrada` | numeric(13) |  |  | Valor Recebimento por Transferência Saldo Credor Entrada |
| recebimento_por_transferencia_saldo_deve_c | `recebimento_por_transferencia_saldo_devedor_entrada` | numeric(13) |  |  | Valor Recebimento por Transferência Saldo Devedor Entrada |
| valor_transferencia_saldo_credor_saida | `transferencia_saldo_credor_saida` | numeric(13) |  |  | Valor Transferência Saldo Credor Saída |
| valor_transferencia_saldo_devedor_saida | `transferencia_saldo_devedor_saida` | numeric(13) |  |  | Valor Transferência Saldo Devedor Saída |
| recebimento_por_transferencia_saldo_cred_c | `recebimento_por_transferencia_saldo_credor_outros` | numeric(13) |  |  | Valor Recebimento por Transferência Saldo Credor Outros |
| recebimento_por_transferencia_saldo_deve_c_c | `recebimento_por_transferencia_saldo_devedor_outros` | numeric(13) |  |  | Valor Recebimento por Transferência Saldo Devedor Outros |
| valor_transferencia_saldo_credor_outros | `transferencia_saldo_credor_outros` | numeric(13) |  |  | Valor Transferência Saldo Credor Outros |
| valor_transferencia_saldo_devedor_outros | `transferencia_saldo_devedor_outros` | numeric(13) |  |  | Valor Transferência Saldo Devedor Outros |
| valor_estorno_dedito_funcep | `estorno_debitos_fundo_combate_erradicacao_pobreza` | numeric(13) |  |  | Valor Estorno Dédito FUNCEP |
| estorno_de_credito_presumido_de_confecca | `estorno_credito_presumido_confeccao` | numeric(13) |  |  | Estorno de crédito presumido de confecção |
| credito_presumido_de_confeccao | `credito_presumido_confeccao` | numeric(13) |  |  | Crédito presumido de confecção |
| credito_de_icms_conf_aliquota_do_simples | `credito_icms_conforme_aliquota_sn` | numeric(13) |  |  | Crédito de ICMS conf. alíquota do Simples Nacional - Art. 23, LC 123/06 |
| cred_presumido_na_aquisicao_de_industria | `credito_presumido_aquisicao_industrias_sn_1` | numeric(13) |  |  | Créd. Presumido na aquisição de Indústrias Simples Nacional - Art. 269, X, a, 1, RICMS |
| credito_presumido_aquisicao_industrias_s | `credito_presumido_aquisicao_industrias_sn_2` | numeric(13) |  |  | Créd. Presumido na aquisição de Indústrias Simples Nacional - Art. 269, X, a, 2, RICMS |
| devolucao_de_mercadoria_adquirida_de_sim | `devolucao_mercadoria_adquirida_sn` | numeric(13) |  |  | Devolução de mercadoria adquirida de Simples Nacional |
| devolucao_de_mercadoria_conf_aliquota_do | `devolucao_mercadoria_conforme_aliquota_sn` | numeric(13) |  |  | Devolução de mercadoria conf. alíquota do Simples Nacional |
| devolucao_de_mercadoria_com_credito_pres | `devolucao_credito_presumido_industrias_sn_1` | numeric(13) |  |  | Devolução de mercadoria com crédito presumido de Indústrias Simples Nacional - Art. 269, X, a, 1, RICMS |
| devolucao_credito_presumido_industrias_s | `devolucao_credito_presumido_industrias_sn_2` | numeric(13) |  |  | Devolução de mercadoria com crédito presumido de Indústrias Simples Nacional - Art. 269, X, a, 2, RICMS |
| credito_presumido_de_vestuario_calcados | `credito_presumido_vestuario` | numeric(13) |  |  | Crédito Presumido de vestuário, calçados e artefatos de tecidos - Art. 270, V |
| devolucao_credito_presumido_de_vestuario | `devolucao_credito_presumido_vestuario` | numeric(13) |  |  | Devolução Crédito Presumido de vestuário, calçados e artefatos de tecidos - Art. 270, V |
| transferencia_de_creditos_acumulados_a_t | `transferencia_creditos_acumulados_terc_art_314` | numeric(13) |  |  | Transferência de Créditos Acumulados a terceiros - Art. 314 § 4º |
| credito_presumido_de_20_para_transportad | `credito_presumido_transporte` | numeric(13) |  |  | Crédito presumido de 20% para transportadoras - Art. 270, III, B, do RICMS/BA |
| credito_presumido_aos_fabricantes_de_lei | `credito_presumido_leite_de_coco` | numeric(13) |  |  | Crédito presumido aos fabricantes de leite de coco - Art. 270, VI |
| credito_presumido_leite_de_coco_saidas | `credito_presumido_leite_de_coco_saidas` | numeric(13) |  |  | Crédito presumido aos fabricantes de leite de coco - Art. 270, VI - Saídas |
| credito_presumido_leite_de_coco_reducao | `credito_presumido_leite_de_coco_reducao` | numeric(13) |  |  | Crédito presumido aos fabricantes de leite de coco - Art. 270, VI - Redução |
| devolucao_credito_presumido_aos_fabrican | `devolucao_credito_presumido_leite_de_coco` | numeric(13) |  |  | Devolução crédito presumido aos fabricantes de leite de coco - Art. 270, VI |
| estorno_de_creditos_art_312_i_do_ricms_s | `estorno_credito_icms_art_312_saida` | numeric(13) |  |  | Estorno de créditos - Art. 312, I do RICMS - Saída |
| estorno_de_creditos_art_312_i_do_ricms_r | `estorno_credito_icms_art_312_reducao_z` | numeric(13) |  |  | Estorno de créditos - Art. 312, I do RICMS - Redução Z |
| estorno_de_debito_nas_operacoes_com_ct_e | `estorno_debito_operacoes_cte_substituto` | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |
| valor_do_estorno_de_creditos_art_312_i_d | `estorno_credito_icms_art_312_saida_transporte` | numeric(13) |  |  | Valor do estorno de créditos - Art. 312. I do RICMS - Transportes |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in)

## efsdoimp_subtri_por_uf_ba

**Saldo dos Impostos - Substituição Tributária Por BA** — tabela `EFSDOIMP_SUBTRI_POR_UF_BA` (344 linhas)

Saldo dos Impostos - Substituição Tributária Por BA. 344 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 344 linhas, 8 empresa(s), DATA_SIM de 2013-01-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| sigla_da_uf | `sigla_uf` | char(2) |  |  | Sigla da UF |
| recolhimento | `i_recolhimento` | integer(4) |  |  | Recolhimento |
| estorno_funcep | `estorno_funcep` | numeric(13) |  |  | Estorno FUNCEP |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `sigla_da_uf` (eq/in), `recolhimento` (eq/in)

## efsdoimp_inss_rb_por_recolhimento

**Saldo dos Impostos - INSS Receita Bruta - Por Recolhimento** — tabela `EFSDOIMP_INSS_RB_POR_RECOLHIMENTO` (338 linhas)

Saldo dos Impostos - INSS Receita Bruta - Por Recolhimento. 338 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_RECOLHIMENTO, I_SCP.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_RECOLHIMENTO, I_SCP`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_VENCIMENTO`
- **Ordem padrão:** `DATA_VENCIMENTO desc`, `CODI_IMP asc`, `DATA_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 338 linhas, 4 empresa(s), DATA_VENCIMENTO de 2018-02-20 a 2026-10-20.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| codigo_do_recolhimento | `codigo_recolhimento` | char(6) |  |  | Código do Recolhimento |
| sequencial_scp | `i_scp` | integer(4) |  |  | Sequencial SCP |
| valor_da_receita_bruta_total_do_estabele | `receita_bruta_total` | numeric(13) |  |  | Valor da Receita Bruta Total do Estabelecimento no Período |
| valor_da_receita_bruta_real | `receita_bruta_real` | numeric(13) |  |  | Valor da Receita Bruta Real |
| valor_das_devolucoes | `valor_devolucao` | numeric(13) |  |  | Valor das Devoluções |
| valor_das_devolucoes_resto | `valor_devolucao_resto` | numeric(13) |  |  | Valor das Devoluções - Resto |
| valor_da_receita_bruta_do_estabeleciment | `receita_bruta` | numeric(13) |  |  | Valor da Receita Bruta do Estabelecimento, correspondente às atividades/produtos por Recolhimento |
| valor_das_exportacoes | `valor_exportacao` | numeric(13) |  |  | Valor das Exportações |
| valor_das_exportacoes_de_devolucao | `valor_exportacao_devolucao` | numeric(13) |  |  | Valor das Exportações de Devolução |
| valor_das_exclusoes_da_receita_bruta | `valor_exclusao` | numeric(13) |  |  | Valor das Exclusões da Receita Bruta |
| valor_da_base_de_calculo_da_contribuicao | `base_calculo` | numeric(13) |  |  | Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta |
| aliquota_da_contribuicao_previdenciaria | `aliquota` | numeric(8) |  |  | Alíquota da Contribuição Previdenciária sobre a Receita Bruta |
| valor_da_contribuicao_previdenciaria_apu | `valor_contribuicao_apurada` | numeric(13) |  |  | Valor da Contribuição Previdenciária Apurada sobre a Receita Bruta |
| valor_diferido | `valor_diferido` | numeric(13) |  |  | Valor diferido |
| valor_diferido_periodo_anterior | `valor_diferido_anterior` | numeric(13) |  |  | Valor diferido - Período anterior |
| valor_da_contribuicao_previdenciaria_a_p | `valor_contribuicao_a_pagar` | numeric(13) |  |  | Valor da Contribuição Previdenciária a Pagar |
| parcela | `parcela` | integer(4) |  |  | Parcela |
| valor_pago | `valor_pago` | numeric(13) |  |  | Valor Pago |
| data_do_vencimento | `data_vencimento` | date(4) |  |  | Data do vencimento |
| valor_das_devolucoes_relacionada | `valor_devolucao_relacionada` | numeric(13) |  |  | Valor das Devoluções - Relacionada |
| valor_das_devolucoes_resto_relacionada | `valor_devolucao_resto_relacionada` | numeric(13) |  |  | Valor das Devoluções - Resto - Relacionada |
| valor_das_devolucoes_nao_relacionada | `valor_devolucao_nao_relacionada` | numeric(13) |  |  | Valor das Devoluções - Não Relacionada |
| valor_das_devolucoes_resto_nao_relaciona | `valor_devolucao_resto_nao_relacionada` | numeric(13) |  |  | Valor das Devoluções - Resto - Não Relacionada |
| valor_ajuste_reducao | `valor_ajuste_reducao` | numeric(13) |  |  | Valor Ajuste Redução |
| valor_ajuste_acrescimo | `valor_ajuste_acrescimo` | numeric(13) |  |  | Valor Ajuste Acréscimo |
| valor_das_exclusoes_da_receita_bruta_rel | `valor_exclusao_relacionada` | numeric(13) |  |  | Valor das Exclusões da Receita Bruta - Relacionada |
| valor_das_exclusoes_da_receita_bruta_nao | `valor_exclusao_nao_relacionada` | numeric(13) |  |  | Valor das Exclusões da Receita Bruta - Não Relacionada |
| valor_das_exportacoes_relacionada | `valor_exportacao_relacionada` | numeric(13) |  |  | Valor das Exportações - Relacionada |
| valor_das_exportacoes_nao_relacionada | `valor_exportacao_nao_relacionada` | numeric(13) |  |  | Valor das Exportações - Não Relacionada |
| valor_das_exportacoes_de_devolucao_relac | `valor_exportacao_devolucao_relacionada` | numeric(13) |  |  | Valor das Exportações de Devolução - Relacionada |
| valor_das_exportacoes_de_devolucao_nao_r | `valor_exportacao_devolucao_nao_relacionada` | numeric(13) |  |  | Valor das Exportações de Devolução - Não Relacionada |
| compensacao_de_pagamento_indevido_ou_a_m | `compensacao_pagamento_indevido_maior` | numeric(13) |  |  | Compensação de pagamento indevido ou a maior |
| valor_das_exportacoes_de_devolucao_resto | `valor_exportacao_devolucao_resto` | numeric(13) |  |  | Valor das Exportações de Devolução - Resto |
| valor_exportacao_devolucao_resto_nao_rel | `valor_exportacao_devolucao_resto_nao_relacionada` | numeric(13) |  |  | Valor das Exportações de Devolução - Resto - Não Relacionada |
| valor_exportacao_devolucao_resto_relacio | `valor_exportacao_devolucao_resto_relacionada` | numeric(13) |  |  | Valor das Exportações de Devolução - Resto - Relacionada |
| outras_compensacoes | `outras_compensacoes` | numeric(13) |  |  | Outras Compensações |
| valor_cte_substituto_reinf | `valor_cte_substituto_reinf` | numeric(13) |  |  | Valor CTE Substituto REINF |
| aliquota_de_transicao_da_contribuicao_pr | `aliquota_transicao` | numeric(8) |  |  | Alíquota de Transição da Contribuição Previdenciária sobre a Receita Bruta |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `codigo_do_recolhimento` (eq/in), `sequencial_scp` (eq/in), `data_do_vencimento` (entre/gte/lte)

## efsdoimp_estadual_pr

**Saldo dos Impostos - Estadual PR** — tabela `EFSDOIMP_ESTADUAL_PR` (281 linhas)

Saldo dos Impostos - Estadual PR. 281 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 281 linhas, 7 empresa(s), DATA_SIM de 2010-01-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| credito_transferido_ao_estabelecimento_c | `credito_transferido_consolidado` | numeric(13) |  |  | Crédito transferido ao estabelecimento consolidador |
| debito_transferido_ao_estabelecimento_co | `debito_transferido_consolidado` | numeric(13) |  |  | Débito transferido ao estabelecimento consolidador |
| credito_recebido_de_estabelecimento_cons | `credito_recebido_consolidado` | numeric(13) |  |  | Crédito recebido de estabelecimento consolidado |
| debito_recebido_de_estabelecimento_conso | `debito_recebido_consolidado` | numeric(13) |  |  | Débito recebido de estabelecimento consolidado |
| credito_transferido_apuracao_consolidada | `credito_transferido_apuracao_consolidada` | numeric(13) |  |  | Crédito transferido - apuração consolidada |
| debito_transferido_apuracao_consolidada | `debito_transferido_apuracao_consolidada` | numeric(13) |  |  | Débito transferido - apuração consolidada |
| credito_material_de_uso_e_consumo | `credito_material_de_uso_e_consumo` | numeric(13) |  |  | Crédito material de uso e consumo |
| saidas_com_reducao_de_bc_art_71_saidas | `saidas_com_reducao_base_calculo_art_71_saidas` | numeric(13) |  |  | Saídas com Redução de BC Art. 71 - Saídas |
| saidas_com_reducao_de_bc_art_71_reducaoz | `saidas_com_reducao_base_calculo_art_71_reducao_z` | numeric(13) |  |  | Saídas com Redução de BC Art. 71 - ReduçãoZ |
| credito_ativo_imobilizado | `credito_ativo_imobilizado` | numeric(13) |  |  | Crédito Ativo Imobilizado |
| credito_icms_sobre_insumos | `credito_icms_sobre_insumos_prest_serv_transp` | numeric(13) |  |  | Crédito ICMS sobre insumos |
| icmsa_recolhimento_antecipado | `icmsa_recolhimento_antecipado` | numeric(13) |  |  | ICMSA - Recolhimento antecipado |
| icmsa_icms_recolhido_antecipadamente | `icmsa_icms_recolhido_antecipadamente` | numeric(13) |  |  | ICMSA - ICMS recolhido antecipadamente |
| credito_presumido_de_20_para_transportad | `credito_presumido_20_transportadoras_icms` | numeric(13) |  |  | Crédito presumido de 20% para transportadoras - Item 48, Anexo III do RICMS |
| ressarcimento_de_icms_st | `ressarcimento_de_icms_subtri` | numeric(13) |  |  | Ressarcimento de ICMS ST |
| outros_creditos_de_venda_efetuada_fora_d | `outros_creditos_venda_efetuada_fora_estabelecimento` | numeric(13) |  |  | Outros créditos de venda efetuada fora do estabelecimento |
| debito_referente_ao_fecop_pr_icms_propri | `debito_fecop_icms` | numeric(13) |  |  | Débito referente ao FECOP-PR - ICMS Próprio |
| devolucao_referente_ao_fecop_pr_icms_pro | `devolucao_fecop_icms` | numeric(13) |  |  | Devolução referente ao FECOP-PR - ICMS Próprio |
| credito_presumido_textil_saidas | `credito_presumido_textil_saidas` | numeric(13) |  |  | Crédito presumido têxtil - Saídas |
| credito_presumido_textil_reducao_z | `credito_presumido_textil_reducao_z` | numeric(13) |  |  | Crédito presumido têxtil - Redução Z |
| credito_extemporaneo_inciso_i_do_5o_do_a | `credito_extemporaneo_inciso_i_art_23` | numeric(13) |  |  | Crédito extemporâneo - inciso I do § 5º do art. 23 do RICMS |
| credito_de_icms_proprio | `credito_icms_proprio_cfe` | numeric(13) |  |  | Crédito de ICMS Próprio |
| icms_transporte_pago_antecipadamente | `icms_transporte_pago_antecipadamente` | numeric(13) |  |  | ICMS transporte pago antecipadamente |
| credito_presumido_leite_cru_saidas | `credito_presumido_leite_cru_saidas_tributadas` | numeric(13) |  |  | Crédito presumido Leite Cru - Saídas |
| credito_presumido_leite_cru_total_saidas | `credito_presumido_leite_cru_total_saidas` | numeric(13) |  |  | Crédito presumido Leite Cru - Total Saídas |
| credito_presumido_leite_cru_proporcao_sa | `credito_presumido_leite_cru_proporcao_saidas_tributadas` | numeric(13) |  |  | Crédito presumido Leite Cru - Proporção Saídas |
| credito_presumido_leite_cru_entradas | `credito_presumido_leite_cru_entradas` | numeric(13) |  |  | Crédito presumido Leite Cru - Entradas |
| credito_presumido_leite_cru_valor_utiliz | `credito_presumido_leite_cru_valor_utilizado` | numeric(13) |  |  | Crédito presumido Leite Cru - Valor Utilizado |
| credito_presumido_leite_cru_estorno | `credito_presumido_leite_cru_estorno` | numeric(13) |  |  | Crédito presumido Leite Cru - Estorno |
| icms_st_a_recuperar_ressarcir_referente | `icms_st_recup_ressarc_saidas_internas_consu_final` | numeric(13) |  |  | ICMS ST a recuperar/ressarcir referente saídas internas a consumidor final |
| icms_st_a_complementar_referente_saidas | `icms_st_comp_saidas_internas_consu_final` | numeric(13) |  |  | ICMS ST a complementar referente saídas internas a consumidor final |
| icms_st_recup_ressarc_saidas_interestadu | `icms_st_recup_ressarc_saidas_interestaduais` | numeric(13) |  |  | ICMS ST a recuperar/ressarcir referente saídas interestaduais |
| icms_st_recup_ressarc_saidas_internas_ar | `icms_st_recup_ressarc_saidas_internas_art_119_ricms` | numeric(13) |  |  | ICMS ST a recuperar/ressarcir referente saídas internas que trata o art. 119 do RICMS/17 |
| icms_st_recup_ressarc_saidas_internas_co | `icms_st_recup_ressarc_saidas_internas_contrib_sn` | numeric(13) |  |  | ICMS ST a recuperar/ressarcir referente saídas internas a contribuinte do Simples Nacional |
| estorno_de_debito_conforme_2_art_6_do_an | `estorno_debito_anexo_ix_ricms` | numeric(13) |  |  | Estorno de débito conforme 2 art 6 do Anexo IX do RICMS/2017 |
| credito_de_icms_substituicao_tributaria | `credito_icms_st_art_25_ricms` | numeric(13) |  |  | Crédito de ICMS Substituição Tributária - Art. 25 § 11 do RICMS/PR |
| estorno_de_debito_nas_operacoes_com_ct_e | `estorno_debito_operacoes_cte_substituto` | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |
| credito_aquisicao_combustiveis_para_insu | `credito_aquisicao_combustivel_insumo` | numeric(13) |  |  | Crédito aquisição combustíveis para insumos - Art. 25, III do § 4º do RICMS |
| estorno_credito_aquisicao_combustiveis_p | `estorno_credito_aquisicao_combustivel_insumo` | numeric(13) |  |  | Estorno crédito aquisição combustíveis p/ insumos - Art. 25, IV do § 4º e § 5º do RICMS |
| estorno_credito_aquisicao_combustivel_in | `estorno_credito_aquisicao_combustivel_insumo_op_transp_nao_tributada` | numeric(13) |  |  | Estorno crédito aquisição combustíveis p/ insumos - Art. 25, IV do § 4º e § 5º do RICMS - Operações de transporte - Não tributadas |
| estorno_credito_aquisicao_combustivel_in_c | `estorno_credito_aquisicao_combustivel_insumo_op_transp_total` | numeric(13) |  |  | Estorno crédito aquisição combustíveis p/ insumos - Art. 25, IV do § 4º e § 5º do RICMS - Operações de transporte - Total |
| estorno_credito_aquisicao_combustivel_in_c_c | `estorno_credito_aquisicao_combustivel_insumo_proporcao` | numeric(13) |  |  | Estorno crédito aquisição combustíveis p/ insumos - Art. 25, IV do § 4º e § 5º do RICMS - Proporção |
| estorno_de_credito_presumido_com_eletron | `estorno_credito_presumido_com_eletronico_art_11_a_decreto_6434_17` | numeric(13) |  |  | Estorno de crédito presumido com. eletrônico - Art. 11-A Decreto 6434/17 |
| credito_presumido_comercio_eletronico_ar | `credito_presumido_comercio_eletronico_art_11_a_decreto_6434_17` | numeric(13) |  |  | Crédito presumido comércio eletrônico - Art. 11-A Decreto 6.434/17 |
| exclusao_de_mercadoria_da_substituicao_t | `exclusao_mercadoria_subtri_art_19_anexo_ix_ricms` | numeric(13) |  |  | Exclusão de mercadoria da substituição tributária  - Art. 19, anexo IX do RICMS |
| credito_aquisicao_combustivel_insumo_fro | `credito_aquisicao_combustivel_insumo_frota` | numeric(13) |  |  | Crédito aquisição combustíveis para insumos - frota própria - Art. 25, §13º e §14º RICMS |
| estorno_credito_combust_p_insumos_frota | `estorno_credito_aquisicao_combustivel_insumo_frota` | numeric(13) |  |  | Estorno crédito combust. p/ insumos - frota própria - Art. 25, §13º e §14º RICMS |
| estorno_credito_aquisicao_combustivel_in_c_c_c | `estorno_credito_aquisicao_combustivel_insumo_op_frota_nao_tributada` | numeric(13) |  |  | Estorno crédito combust. p/ insumos - frota própria - Art. 25, §13º e §14º RICMS - Operações de frota - Não tributadas |
| estorno_credito_aquisicao_combustivel_in_c_c_c_c | `estorno_credito_aquisicao_combustivel_insumo_op_frota_total` | numeric(13) |  |  | Estorno crédito combust. p/ insumos - frota própria - Art. 25, §13º e §14º RICMS - Operações de frota - Total |
| estorno_credito_aquisicao_combustivel_in_c_c_c_c_c | `estorno_credito_aquisicao_combustivel_insumo_proporcao_frota` | numeric(13) |  |  | Estorno crédito combust. p/ insumos - frota própria - Art. 25, §13º e §14º RICMS - Proporção |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in)

## efsdoimp_nao_cumulativos

**Saldo do Impostos - Detalhamento dos Nao Cumulativos** — tabela `efsdoimp_nao_cumulativos` (274 linhas)

Saldo do Impostos - Detalhamento dos Nao Cumulativos. 274 linhas no catálogo; chave: codi_emp, codi_imp, data_sim, pdic_sim.

- **Chave:** `codi_emp, codi_imp, data_sim, pdic_sim`
- **Empresa:** `codi_emp`
- **Período:** `data_sim`
- **Ordem padrão:** `data_sim desc`, `codi_imp asc`, `pdic_sim asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 274 linhas, 5 empresa(s), data_sim de 2017-07-01 a 2026-09-01.
- metodo_de_determinacao_de_creditos_i_som: todos os valores reais estão no comentário do banco (I=274).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| separa_creditos_de_importacao_s_n | `separa` | char(1) |  |  | Separa creditos de importacao (S/N) |
| metodo_de_determinacao_de_creditos_i_som | `metodo` | char(1) |  | efsdoimp_nao_cumulativos_metodo_de_d | Metodo de determinacao de creditos (I-somente interno/E-interno e externo) |
| receita_do_mercado_interno | `receita_interna` | numeric(13) |  |  | Receita do mercado interno |
| receita_do_mercado_externo | `receita_externa` | numeric(13) |  |  | Receita do mercado externo |
| receita_nao_tributada | `receita_isenta` | numeric(13) |  |  | Receita nao tributada |
| receita_total | `receita_total` | numeric(13) |  |  | Receita total |
| percentual_de_receita_do_mercado_interno | `percentual_interno` | numeric(13) |  |  | Percentual de receita do mercado interno |
| percentual_de_receita_do_mercado_externo | `percentual_externo` | numeric(13) |  |  | Percentual de receita do mercado externo |
| percentual_de_receita_nao_tributada | `percentual_isento` | numeric(13) |  |  | Percentual de receita nao tributada |
| base_total_do_mercado_interno | `base_total_interna` | numeric(13) |  |  | Base total do mercado interno |
| credito_total_do_mercado_interno | `credito_total_interno` | numeric(13) |  |  | Credito total do mercado interno |
| base_total_do_mercado_externo | `base_total_externa` | numeric(13) |  |  | Base total do mercado externo |
| credito_total_do_mercado_externo | `credito_total_externo` | numeric(13) |  |  | Credito total do mercado externo |
| credito_total_do_mercado_interno_com_ali | `credito_dif_total_interno` | numeric(13) |  |  | Credito total do mercado interno com aliquota diferenciada |
| credito_total_do_mercado_externo_com_ali | `credito_dif_total_externo` | numeric(13) |  |  | Credito total do mercado externo com aliquota diferenciada |
| base_do_mercado_interno_vinculada_a_rece | `base_interna_vi` | numeric(13) |  |  | Base do mercado interno vinculada a receita do mercado interno |
| credito_do_mercado_interno_vinculado_a_r | `credito_interno_vi` | numeric(13) |  |  | Credito do mercado interno vinculado a receita do mercado interno |
| base_do_mercado_externo_vinculada_a_rece | `base_externa_vi` | numeric(13) |  |  | Base do mercado externo vinculada a receita do mercado interno |
| credito_externo_vi | `credito_externo_vi` | numeric(13) |  |  | Credito do mercado interno vinculado a receita do mercado interno |
| credito_do_mercado_interno_com_aliquota | `credito_dif_interno_vi` | numeric(13) |  |  | Credito do mercado interno com aliquota diferenciada vinculado a receita do mercado interno |
| credito_do_mercado_externo_com_aliquota | `credito_dif_externo_vi` | numeric(13) |  |  | Credito do mercado externo com aliquota diferenciada vinculado a receita do mercado interno |
| base_interna_vn | `base_interna_vn` | numeric(13) |  |  | Base do mercado interno vinculada a receita nao tributada |
| credito_interno_vn | `credito_interno_vn` | numeric(13) |  |  | Credito do mercado interno vinculado a receita nao tributada |
| base_externa_vn | `base_externa_vn` | numeric(13) |  |  | Base do mercado externo vinculada a receita nao tributada |
| credito_do_mercado_externo_vinculado_a_r | `credito_externo_vn` | numeric(13) |  |  | Credito do mercado externo vinculado a receita nao tributada |
| credito_dif_interno_vn | `credito_dif_interno_vn` | numeric(13) |  |  | Credito do mercado interno com aliquota diferenciada vinculado a receita nao tributada |
| credito_dif_externo_vn | `credito_dif_externo_vn` | numeric(13) |  |  | Credito do mercado externo com aliquota diferenciada vinculado a receita nao tributada |
| base_interna_ve | `base_interna_ve` | numeric(13) |  |  | Base do mercado interno vinculada a receita do mercado externo |
| credito_interno_ve | `credito_interno_ve` | numeric(13) |  |  | Credito do mercado interno vinculado a receita do mercado externo |
| base_externa_ve | `base_externa_ve` | numeric(13) |  |  | Base do mercado externo vinculada a receita do mercado externo |
| credito_externo_ve | `credito_externo_ve` | numeric(13) |  |  | Credito do mercado externo vinculado a receita do mercado externo |
| credito_dif_interno_ve | `credito_dif_interno_ve` | numeric(13) |  |  | Credito do mercado interno com aliquota diferenciada vinculado a receita do mercado externo |
| credito_dif_externo_ve | `credito_dif_externo_ve` | numeric(13) |  |  | Credito do mercado externo com aliquota diferenciada vinculado a receita do mercado externo |
| total_de_outros_creditos_do_mercado_inte | `outros_interno_total` | numeric(13) |  |  | Total de outros creditos do mercado interno |
| total_de_outros_creditos_do_mercado_exte | `outros_externo_total` | numeric(13) |  |  | Total de outros creditos do mercado externo |
| outros_creditos_do_mercado_interno_vincu | `outros_interno_vi` | numeric(13) |  |  | Outros creditos do mercado interno vinculado a receita do mercado interno |
| outros_creditos_do_mercado_externo_vincu | `outros_externo_vi` | numeric(13) |  |  | Outros creditos do mercado externo vinculado a receita do mercado interno |
| outros_interno_vn | `outros_interno_vn` | numeric(13) |  |  | Outros creditos do mercado interno vinculado a receita nao tributada |
| outros_externo_vn | `outros_externo_vn` | numeric(13) |  |  | Outros creditos do mercado externo vinculado a receita nao tributada |
| outros_interno_ve | `outros_interno_ve` | numeric(13) |  |  | Outros creditos do mercado interno vinculado a receita do mercado externo |
| outros_externo_ve | `outros_externo_ve` | numeric(13) |  |  | Outros creditos do mercado externo vinculado a receita do mercado externo |
| credito_negativo_do_mercado_interno | `credito_negativo_interno_total` | numeric(13) |  |  | Crédito negativo do mercado interno |
| credito_negativo_do_mercado_externo | `credito_negativo_externo_total` | numeric(13) |  |  | Crédito negativo do mercado externo |
| credito_negativo_do_mercado_interno_vinc | `credito_negativo_interno_vi` | numeric(13) |  |  | Crédito negativo do mercado interno vinculado a receita do mercado interno |
| credito_negativo_interno_vn | `credito_negativo_interno_vn` | numeric(13) |  |  | Crédito negativo do mercado interno vinculado a receita nAo tributada |
| credito_negativo_interno_ve | `credito_negativo_interno_ve` | numeric(13) |  |  | Crédito negativo do mercado interno vinculado a receita do mercado externo |
| credito_negativo_do_mercado_externo_vinc | `credito_negativo_externo_vi` | numeric(13) |  |  | Crédito negativo do mercado externo vinculado a receita do mercado interno |
| credito_negativo_externo_vn | `credito_negativo_externo_vn` | numeric(13) |  |  | Crédito negativo do mercado externo vinculado a receita nAo tributada |
| credito_negativo_externo_ve | `credito_negativo_externo_ve` | numeric(13) |  |  | Crédito negativo do mercado externo vinculado a receita do mercado externo |
| credito_relativo_ao_estoque_de_abertura | `estoque_abertura_interno_total` | numeric(13) |  |  | Crédito relativo ao estoque de abertura do mercado interno |
| estoque_abertura_externo_total | `estoque_abertura_externo_total` | numeric(13) |  |  | Crédito relativo ao estoque de abertura do mercado externo |
| estoque_abertura_interno_vi | `estoque_abertura_interno_vi` | numeric(13) |  |  | Crédito relativo ao estoque de abertura do mercado interno vinculado a receita do mercado interno |
| estoque_abertura_interno_vn | `estoque_abertura_interno_vn` | numeric(13) |  |  | Crédito relativo ao estoque de abertura do mercado interno vinculado a receita não tributada |
| estoque_abertura_interno_ve | `estoque_abertura_interno_ve` | numeric(13) |  |  | Crédito relativo ao estoque de abertura do mercado interno vinculado a receita do mercado externo |
| estoque_abertura_externo_vi | `estoque_abertura_externo_vi` | numeric(13) |  |  | Crédito relativo ao estoque de abertura do mercado externo vinculado a receita do mercado interno |
| estoque_abertura_externo_vn | `estoque_abertura_externo_vn` | numeric(13) |  |  | Crédito relativo ao estoque de abertura do mercado externo vinculado a receita não tributada |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `separa_creditos_de_importacao_s_n` (eq/in), `metodo_de_determinacao_de_creditos_i_som` (eq/in)

## efsdoimp_inss_rb_por_recolhimento_cno

**Saldo dos Impostos - INSS Receita Bruta - Por Recolhimento - CNO** — tabela `EFSDOIMP_INSS_RB_POR_RECOLHIMENTO_CNO` (266 linhas)

Saldo dos Impostos - INSS Receita Bruta - Por Recolhimento - CNO. 266 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_RECOLHIMENTO, I_SCP, I_CNO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_RECOLHIMENTO, I_SCP, I_CNO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_VENCIMENTO`
- **Ordem padrão:** `DATA_VENCIMENTO desc`, `CODI_IMP asc`, `DATA_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 266 linhas, 3 empresa(s), DATA_VENCIMENTO de 2021-02-19 a 2026-10-20.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| codigo_do_recolhimento | `codigo_recolhimento` | char(6) |  |  | Código do Recolhimento |
| sequencial_scp | `i_scp` | integer(4) |  |  | Sequencial SCP |
| codigo_cno | `i_cno` | integer(4) |  |  | Código CNO |
| valor_da_receita_bruta_total_do_estabele | `receita_bruta_total` | numeric(13) |  |  | Valor da Receita Bruta Total do Estabelecimento no Período |
| valor_da_receita_bruta_real | `receita_bruta_real` | numeric(13) |  |  | Valor da Receita Bruta Real |
| valor_das_devolucoes | `valor_devolucao` | numeric(13) |  |  | Valor das Devoluções |
| valor_das_devolucoes_resto | `valor_devolucao_resto` | numeric(13) |  |  | Valor das Devoluções - Resto |
| valor_da_receita_bruta_do_estabeleciment | `receita_bruta` | numeric(13) |  |  | Valor da Receita Bruta do Estabelecimento, correspondente às atividades/produtos por Recolhimento |
| valor_das_exportacoes | `valor_exportacao` | numeric(13) |  |  | Valor das Exportações |
| valor_das_exportacoes_de_devolucao | `valor_exportacao_devolucao` | numeric(13) |  |  | Valor das Exportações de Devolução |
| valor_das_exclusoes_da_receita_bruta | `valor_exclusao` | numeric(13) |  |  | Valor das Exclusões da Receita Bruta |
| valor_da_base_de_calculo_da_contribuicao | `base_calculo` | numeric(13) |  |  | Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta |
| aliquota_da_contribuicao_previdenciaria | `aliquota` | numeric(8) |  |  | Alíquota da Contribuição Previdenciária sobre a Receita Bruta |
| valor_da_contribuicao_previdenciaria_apu | `valor_contribuicao_apurada` | numeric(13) |  |  | Valor da Contribuição Previdenciária Apurada sobre a Receita Bruta |
| valor_diferido | `valor_diferido` | numeric(13) |  |  | Valor diferido |
| valor_diferido_periodo_anterior | `valor_diferido_anterior` | numeric(13) |  |  | Valor diferido - Período anterior |
| valor_da_contribuicao_previdenciaria_a_p | `valor_contribuicao_a_pagar` | numeric(13) |  |  | Valor da Contribuição Previdenciária a Pagar |
| parcela | `parcela` | integer(4) |  |  | Parcela |
| valor_pago | `valor_pago` | numeric(13) |  |  | Valor Pago |
| data_do_vencimento | `data_vencimento` | date(4) |  |  | Data do vencimento |
| valor_das_devolucoes_relacionada | `valor_devolucao_relacionada` | numeric(13) |  |  | Valor das Devoluções - Relacionada |
| valor_das_devolucoes_resto_relacionada | `valor_devolucao_resto_relacionada` | numeric(13) |  |  | Valor das Devoluções - Resto - Relacionada |
| valor_das_devolucoes_nao_relacionada | `valor_devolucao_nao_relacionada` | numeric(13) |  |  | Valor das Devoluções - Não Relacionada |
| valor_das_devolucoes_resto_nao_relaciona | `valor_devolucao_resto_nao_relacionada` | numeric(13) |  |  | Valor das Devoluções - Resto - Não Relacionada |
| valor_ajuste_reducao | `valor_ajuste_reducao` | numeric(13) |  |  | Valor Ajuste Redução |
| valor_ajuste_acrescimo | `valor_ajuste_acrescimo` | numeric(13) |  |  | Valor Ajuste Acréscimo |
| valor_das_exclusoes_da_receita_bruta_rel | `valor_exclusao_relacionada` | numeric(13) |  |  | Valor das Exclusões da Receita Bruta - Relacionada |
| valor_das_exclusoes_da_receita_bruta_nao | `valor_exclusao_nao_relacionada` | numeric(13) |  |  | Valor das Exclusões da Receita Bruta - Não Relacionada |
| valor_das_exportacoes_relacionada | `valor_exportacao_relacionada` | numeric(13) |  |  | Valor das Exportações - Relacionada |
| valor_das_exportacoes_nao_relacionada | `valor_exportacao_nao_relacionada` | numeric(13) |  |  | Valor das Exportações - Não Relacionada |
| valor_das_exportacoes_de_devolucao_relac | `valor_exportacao_devolucao_relacionada` | numeric(13) |  |  | Valor das Exportações de Devolução - Relacionada |
| valor_das_exportacoes_de_devolucao_nao_r | `valor_exportacao_devolucao_nao_relacionada` | numeric(13) |  |  | Valor das Exportações de Devolução - Não Relacionada |
| compensacao_de_pagamento_indevido_ou_a_m | `compensacao_pagamento_indevido_maior` | numeric(13) |  |  | Compensação de pagamento indevido ou a maior |
| valor_das_exportacoes_de_devolucao_resto | `valor_exportacao_devolucao_resto` | numeric(13) |  |  | Valor das Exportações de Devolução - Resto |
| valor_exportacao_devolucao_resto_nao_rel | `valor_exportacao_devolucao_resto_nao_relacionada` | numeric(13) |  |  | Valor das Exportações de Devolução - Resto - Não Relacionada |
| valor_exportacao_devolucao_resto_relacio | `valor_exportacao_devolucao_resto_relacionada` | numeric(13) |  |  | Valor das Exportações de Devolução - Resto - Relacionada |
| outras_compensacoes | `outras_compensacoes` | numeric(13) |  |  | Outras Compensações |
| valor_cte_substituto_reinf | `valor_cte_substituto_reinf` | numeric(13) |  |  | Valor CTE Substituto REINF |
| aliquota_de_transicao_da_contribuicao_pr | `aliquota_transicao` | numeric(8) |  |  | Alíquota de Transição da Contribuição Previdenciária sobre a Receita Bruta |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `codigo_do_recolhimento` (eq/in), `sequencial_scp` (eq/in), `codigo_cno` (eq/in), `data_do_vencimento` (entre/gte/lte)

## efsdoimp_pis_cofins_importacao_por_nota

**Saldo dos Impostos - PIS/COFINS Importação - Por Nota - Backup** — tabela `EFSDOIMP_PIS_COFINS_IMPORTACAO_POR_NOTA` (209 linhas)

Saldo dos Impostos - PIS/COFINS Importação - Por Nota - Backup. 209 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_NOTA, EMPRESA_NOTA.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_NOTA, EMPRESA_NOTA`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_VENCIMENTO`
- **Ordem padrão:** `DATA_VENCIMENTO desc`, `CODI_IMP asc`, `DATA_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 209 linhas, 5 empresa(s), DATA_VENCIMENTO de 2021-02-05 a 2025-09-26.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| codigo_da_nota | `codigo_nota` | integer(4) |  |  | Código da nota |
| empresa_da_nota | `empresa_nota` | integer(4) |  |  | Empresa da nota |
| saldo_a_recolher | `valor_recolher` | numeric(13) |  |  | Saldo a recolher |
| valor_contabil | `valor_contabil` | numeric(13) |  |  | Valor contábil |
| base_de_calculo | `base_calculo` | numeric(13) |  |  | Base de cálculo |
| valor_do_imposto | `valor_imposto` | numeric(13) |  |  | Valor do imposto |
| parcela | `parcela` | integer(4) |  |  | Parcela |
| valor_pago | `valor_pago` | numeric(13) |  |  | Valor pago |
| data_do_vencimento | `data_vencimento` | date(4) |  |  | Data do vencimento |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `codigo_da_nota` (eq/in), `empresa_da_nota` (eq/in), `data_do_vencimento` (entre/gte/lte)

## efsdoimp_inss_rb_receita

**Saldo dos Impostos - INSS Receita Bruta - Controle de Receita** — tabela `EFSDOIMP_INSS_RB_RECEITA` (169 linhas)

Saldo dos Impostos - INSS Receita Bruta - Controle de Receita. 169 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_FILIAL, I_SCP.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_FILIAL, I_SCP`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 169 linhas, 4 empresa(s), DATA_SIM de 2018-01-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| codigo_da_filial | `i_filial` | integer(4) |  |  | Código da Filial |
| sequencial_scp | `i_scp` | integer(4) |  |  | Sequencial SCP |
| receita_bruta_total | `receita_bruta_total` | numeric(13) |  |  | Receita Bruta Total |
| receita_bruta_relacionada | `receita_bruta_relacionada` | numeric(13) |  |  | Receita Bruta Relacionada |
| receita_bruta_nao_relacionada | `receita_bruta_nao_relacionada` | numeric(13) |  |  | Receita Bruta Não Relacionada |
| receita_bruta_relacionada_exportacao | `receita_bruta_relacionada_exportacao` | numeric(13) |  |  | Receita Bruta Relacionada Exportação |
| receita_bruta_nao_relacionada_exportacao | `receita_bruta_nao_relacionada_exportacao` | numeric(13) |  |  | Receita Bruta Não Relacionada Exportação |
| devolucao_venda_total | `devolucao_venda_total` | numeric(13) |  |  | Devolução Venda Total |
| devolucao_venda_relacionada | `devolucao_venda_relacionada` | numeric(13) |  |  | Devolução Venda Relacionada |
| devolucao_venda_nao_relacionada | `devolucao_venda_nao_relacionada` | numeric(13) |  |  | Devolução Venda Não Relacionada |
| devolucao_venda_relacionada_exportacao | `devolucao_venda_relacionada_exportacao` | numeric(13) |  |  | Devolução Venda Relacionada Exportação |
| devolucao_venda_nao_relacionada_exportac | `devolucao_venda_nao_relacionada_exportacao` | numeric(13) |  |  | Devolução Venda Não Relacionada Exportação |
| resto_devolucao_venda_total | `resto_devolucao_venda_total` | numeric(13) |  |  | Resto Devolução Venda Total |
| resto_devolucao_venda_relacionada | `resto_devolucao_venda_relacionada` | numeric(13) |  |  | Resto Devolução Venda Relacionada |
| resto_devolucao_venda_nao_relacionada | `resto_devolucao_venda_nao_relacionada` | numeric(13) |  |  | Resto Devolução Venda Não Relacionada |
| resto_devolucao_venda_relacionada_export | `resto_devolucao_venda_relacionada_exportacao` | numeric(13) |  |  | Resto Devolução Venda Relacionada Exportação |
| resto_devolucao_venda_nao_relacionada_ex | `resto_devolucao_venda_nao_relacionada_exportacao` | numeric(13) |  |  | Resto Devolução Venda Não Relacionada Exportação |
| receita_bruta_relacionada_exportacao_par | `receita_bruta_relacionada_exportacao_percentual` | numeric(13) |  |  | Receita Bruta Relacionada Exportação para Cálculo do Percentual de Relação |
| receita_bruta_nao_relacionada_exportacao_c | `receita_bruta_nao_relacionada_exportacao_percentual` | numeric(13) |  |  | Receita Bruta Não Relacionada Exportação para Cálculo do Percentual de Relação |
| devolucao_venda_relacionada_exportacao_p | `devolucao_venda_relacionada_exportacao_percentual` | numeric(13) |  |  | Devolução Venda Relacionada Exportação para Cálculo do Percentual de Relação |
| devolucao_venda_nao_relacionada_exportac_c | `devolucao_venda_nao_relacionada_exportacao_percentual` | numeric(13) |  |  | Devolução Venda Não Relacionada Exportação para Cálculo do Percentual de Relação |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `codigo_da_filial` (eq/in), `sequencial_scp` (eq/in)

## efsdoimp_inss_rb_por_recolhimento_por_atividade

**Saldo dos Impostos - INSS Receita Bruta - Por Recolhimento - Por Atividade** — tabela `EFSDOIMP_INSS_RB_POR_RECOLHIMENTO_POR_ATIVIDADE` (146 linhas)

Saldo dos Impostos - INSS Receita Bruta - Por Recolhimento - Por Atividade. 146 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_RECOLHIMENTO, I_FILIAL, I_ATIVIDADE, I_SCP.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_RECOLHIMENTO, I_FILIAL, I_ATIVIDADE, I_SCP`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 146 linhas, 4 empresa(s), DATA_SIM de 2018-01-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| codigo_do_recolhimento | `codigo_recolhimento` | char(6) |  |  | Código do Recolhimento |
| codigo_da_filial | `i_filial` | integer(4) |  |  | Código da Filial |
| atividade_inss_receita_bruta | `i_atividade` | char(8) |  |  | Atividade INSS Receita Bruta |
| sequencial_scp | `i_scp` | integer(4) |  |  | Sequencial SCP |
| valor_da_receita_bruta_total_do_estabele | `receita_bruta_total` | numeric(13) |  |  | Valor da Receita Bruta Total do Estabelecimento no Período |
| valor_da_receita_bruta_real_nao_relacion | `receita_bruta_nao_relacionada` | numeric(13) |  |  | Valor da Receita Bruta Real - Não Relacionada |
| valor_da_receita_bruta_real | `receita_bruta_real` | numeric(13) |  |  | Valor da Receita Bruta Real |
| valor_das_devolucoes | `valor_devolucao` | numeric(13) |  |  | Valor das Devoluções |
| valor_das_devolucoes_resto | `valor_devolucao_resto` | numeric(13) |  |  | Valor das Devoluções - Resto |
| valor_da_receita_bruta_do_estabeleciment | `receita_bruta` | numeric(13) |  |  | Valor da Receita Bruta do Estabelecimento, correspondente às atividades/produtos |
| valor_das_exportacoes | `valor_exportacao` | numeric(13) |  |  | Valor das Exportações |
| valor_das_exportacoes_de_devolucao | `valor_exportacao_devolucao` | numeric(13) |  |  | Valor das Exportações de Devolução |
| valor_das_exclusoes_da_receita_bruta | `valor_exclusao` | numeric(13) |  |  | Valor das Exclusões da Receita Bruta |
| valor_da_base_de_calculo_da_contribuicao | `base_calculo` | numeric(13) |  |  | Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta |
| aliquota_da_contribuicao_previdenciaria | `aliquota` | numeric(8) |  |  | Alíquota da Contribuição Previdenciária sobre a Receita Bruta |
| valor_da_contribuicao_previdenciaria_apu | `valor_contribuicao_apurada` | numeric(13) |  |  | Valor da Contribuição Previdenciária Apurada sobre a Receita Bruta |
| valor_das_devolucoes_relacionada | `valor_devolucao_relacionada` | numeric(13) |  |  | Valor das Devoluções - Relacionada |
| valor_das_devolucoes_resto_relacionada | `valor_devolucao_resto_relacionada` | numeric(13) |  |  | Valor das Devoluções - Resto - Relacionada |
| valor_das_devolucoes_nao_relacionada | `valor_devolucao_nao_relacionada` | numeric(13) |  |  | Valor das Devoluções - Não Relacionada |
| valor_das_devolucoes_resto_nao_relaciona | `valor_devolucao_resto_nao_relacionada` | numeric(13) |  |  | Valor das Devoluções - Resto - Não Relacionada |
| valor_das_exclusoes_da_receita_bruta_rel | `valor_exclusao_relacionada` | numeric(13) |  |  | Valor das Exclusões da Receita Bruta - Relacionada |
| valor_das_exclusoes_da_receita_bruta_nao | `valor_exclusao_nao_relacionada` | numeric(13) |  |  | Valor das Exclusões da Receita Bruta - Não Relacionada |
| valor_das_exportacoes_relacionada | `valor_exportacao_relacionada` | numeric(13) |  |  | Valor das Exportações - Relacionada |
| valor_das_exportacoes_nao_relacionada | `valor_exportacao_nao_relacionada` | numeric(13) |  |  | Valor das Exportações - Não Relacionada |
| valor_das_exportacoes_de_devolucao_relac | `valor_exportacao_devolucao_relacionada` | numeric(13) |  |  | Valor das Exportações de Devolução - Relacionada |
| valor_das_exportacoes_de_devolucao_nao_r | `valor_exportacao_devolucao_nao_relacionada` | numeric(13) |  |  | Valor das Exportações de Devolução - Não Relacionada |
| valor_das_exportacoes_de_devolucao_resto | `valor_exportacao_devolucao_resto` | numeric(13) |  |  | Valor das Exportações de Devolução - Resto |
| valor_exportacao_devolucao_resto_nao_rel | `valor_exportacao_devolucao_resto_nao_relacionada` | numeric(13) |  |  | Valor das Exportações de Devolução - Resto - Não Relacionada |
| valor_exportacao_devolucao_resto_relacio | `valor_exportacao_devolucao_resto_relacionada` | numeric(13) |  |  | Valor das Exportações de Devolução - Resto - Relacionada |
| receita_bruta_total_reinf | `receita_bruta_total_reinf` | numeric(13) |  |  | Valor da Receita Bruta Total do Estabelecimento no Período REINF |
| receita_bruta_reinf | `receita_bruta_reinf` | numeric(13) |  |  | Valor da Receita Bruta do Estabelecimento, correspondente às atividades/produtos REINF |
| valor_das_exclusoes_da_receita_bruta_rei | `valor_exclusao_receita_bruta_reinf` | numeric(13) |  |  | Valor das Exclusões da Receita Bruta - REINF |
| acrescimo_da_receita_bruta_reinf | `acrescimo_receita_bruta_reinf` | numeric(13) |  |  | Acréscimo da Receita Bruta - REINF |
| reducao_da_receita_bruta_reinf | `reducao_receita_bruta_reinf` | numeric(13) |  |  | Redução da Receita Bruta - REINF |
| base_calculo_reinf | `base_calculo_reinf` | numeric(13) |  |  | Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta REINF |
| valor_contribuicao_apurada_reinf | `valor_contribuicao_apurada_reinf` | numeric(13) |  |  | Valor Contribuição Apurada REINF |
| valor_desconto_reinf | `desconto_reinf` | numeric(13) |  |  | Valor Desconto REINF |
| valor_ipi_reinf | `ipi_reinf` | numeric(13) |  |  | Valor IPI REINF |
| valor_icms_st_reinf | `icms_st_reinf` | numeric(13) |  |  | Valor ICMS ST REINF |
| valor_da_receita_bruta_real_reinf | `receita_bruta_real_reinf` | numeric(13) |  |  | Valor da Receita Bruta Real REINF |
| valor_das_devolucoes_reinf | `valor_devolucao_reinf` | numeric(13) |  |  | Valor das Devoluções REINF |
| valor_das_exportacoes_reeinf | `valor_exportacao_reinf` | numeric(13) |  |  | Valor das Exportações REEINF |
| valor_das_exportacoes_de_devolucao_reinf | `valor_exportacao_devolucao_reinf` | numeric(13) |  |  | Valor das Exportações de Devolução REINF |
| valor_das_devolucao_resto_reinf | `valor_devolucao_resto_reinf` | numeric(13) |  |  | Valor das Devolução Resto REINF |
| valor_das_devolucoes_relacionada_reinf | `valor_devolucao_relacionada_reinf` | numeric(13) |  |  | Valor das Devoluções - Relacionada REINF |
| valor_das_devolucoes_resto_relacionada_r | `valor_devolucao_resto_relacionada_reinf` | numeric(13) |  |  | Valor das Devoluções - Resto - Relacionada REINF |
| valor_das_devolucoes_nao_relacionada_rei | `valor_devolucao_nao_relacionada_reinf` | numeric(13) |  |  | Valor das Devoluções - Não Relacionada REINF |
| valor_devolucao_resto_nao_relacionada_re | `valor_devolucao_resto_nao_relacionada_reinf` | numeric(13) |  |  | Valor das Devoluções - Resto - Não Relacionada REINF |
| valor_exclusao_relacionada_reinf | `valor_exclusao_relacionada_reinf` | numeric(13) |  |  | Valor das Exclusões da Receita Bruta - Relacionada REINF |
| valor_exclusao_nao_relacionada_reinf | `valor_exclusao_nao_relacionada_reinf` | numeric(13) |  |  | Valor das Exclusões da Receita Bruta - Não Relacionada REINF |
| valor_das_exportacoes_relacionada_reinf | `valor_exportacao_relacionada_reinf` | numeric(13) |  |  | Valor das Exportações - Relacionada REINF |
| valor_das_exportacoes_de_devolucoes_rest | `valor_exportacao_nao_relacionada_reinf` | numeric(13) |  |  | Valor das Exportações de Devoluções - Resto REINF |
| valor_das_exportacoes_nao_relacionada_re | `valor_exportacao_devolucao_resto_reinf` | numeric(13) |  |  | Valor das Exportações - Não Relacionada REINF |
| valor_exportacao_devolucao_relacionada_r | `valor_exportacao_devolucao_relacionada_reinf` | numeric(13) |  |  | Valor das Exportações de Devolução - Relacionada REINF |
| valor_exportacao_devolucao_nao_relaciona | `valor_exportacao_devolucao_nao_relacionada_reinf` | numeric(13) |  |  | Valor das Exportações de Devolução - Não Relacionada REINF |
| receita_bruta_nao_relacionada_reinf | `receita_bruta_nao_relacionada_reinf` | numeric(13) |  |  | Valor da Receita Bruta Real - Não Relacionada REINF |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `codigo_do_recolhimento` (eq/in), `codigo_da_filial` (eq/in), `atividade_inss_receita_bruta` (eq/in), `sequencial_scp` (eq/in)

## efsdoimp_pis_cofins_reducao_linear

**Saldo do Impostos - PIS/COFINS Reducao Linear** — tabela `EFSDOIMP_PIS_COFINS_REDUCAO_LINEAR` (144 linhas)

Saldo do Impostos - PIS/COFINS Reducao Linear. 144 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SCP, I_RECOLHIMENTO, CST, ALIQUOTA, PERCENTUAL_LINEAR, OPERACAO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SCP, I_RECOLHIMENTO, CST, ALIQUOTA, PERCENTUAL_LINEAR, OPERACAO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 144 linhas, 17 empresa(s), DATA_SIM de 2026-04-01 a 2026-09-01.
- operacao_a_acrescimo_r_reducao: todos os valores reais estão no comentário do banco (A=88, R=56).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |
| sequencial_do_recolhimento | `i_recolhimento` | integer(4) |  |  | Sequencial do Recolhimento |
| cst | `cst` | integer(4) |  |  | CST |
| aliquota_do_imposto | `aliquota` | numeric(7) |  |  | Aliquota do Imposto |
| percentual_da_reducao_linear | `percentual_linear` | numeric(5) |  |  | Percentual da Reducao Linear |
| operacao_a_acrescimo_r_reducao | `operacao` | char(1) |  | efsdoimp_pis_cofins_reducao_linear_operacao_a_ | Operacao (A - Acrescimo / R - Reducao) |
| base_de_calculo | `base_calculo` | numeric(13) |  |  | Base de Calculo |
| valor_do_imposto | `valor_imposto` | numeric(13) |  |  | Valor do Imposto |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `sequencial_do_scp` (eq/in), `sequencial_do_recolhimento` (eq/in), `cst` (eq/in), `aliquota_do_imposto` (eq/in), `percentual_da_reducao_linear` (eq/in), `operacao_a_acrescimo_r_reducao` (eq/in)

## efsdoimp_aproveitamento_credito

**Saldo dos impostos - Aproveitamento de credito** — tabela `efsdoimp_aproveitamento_credito` (136 linhas)

Saldo dos impostos - Aproveitamento de credito. 136 linhas no catálogo; chave: codi_emp, codi_imp, data_sim, pdic_sim, origem, tipo, periodo.

- **Chave:** `codi_emp, codi_imp, data_sim, pdic_sim, origem, tipo, periodo`
- **Empresa:** `codi_emp`
- **Período:** `data_sim`
- **Ordem padrão:** `data_sim desc`, `codi_imp asc`, `pdic_sim asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 136 linhas, 3 empresa(s), data_sim de 2024-03-01 a 2026-01-01.
- origem_do_credito_1_interno_2_externo: todos os valores reais estão no comentário do banco (1=136).
- tipo_1_interno_2_nao_tributado_3_externo: todos os valores reais estão no comentário do banco (1=136).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| origem_do_credito_1_interno_2_externo | `origem` | tinyint(1) |  | efsdoimp_aproveitamento_credito_origem_do_c | Origem do credito(1-interno/2-externo) |
| tipo_1_interno_2_nao_tributado_3_externo | `tipo` | tinyint(1) |  | efsdoimp_aproveitamento_credito_tipo_1_inte | Tipo (1-interno/2-nao tributado/3-externo) |
| periodo_de_apuracao_do_credito | `periodo` | date(4) |  |  | Periodo de apuracao do credito |
| saldo_disponivel | `saldo_disponivel` | numeric(13) |  |  | Saldo disponivel |
| saldo_utilizado | `saldo_utilizado` | numeric(13) |  |  | Saldo utilizado |
| saldo_a_transportar | `saldo_atransportar` | numeric(13) |  |  | Saldo a transportar |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `origem_do_credito_1_interno_2_externo` (eq/in), `tipo_1_interno_2_nao_tributado_3_externo` (eq/in), `periodo_de_apuracao_do_credito` (eq/in)

## efsdoimp_estadual_ce

**Saldo dos Impostos - Estadual CE** — tabela `EFSDOIMP_ESTADUAL_CE` (129 linhas)

Saldo dos Impostos - Estadual CE. 129 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 129 linhas, 3 empresa(s), DATA_SIM de 2017-10-01 a 2026-04-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| valor_credito_presumido_transporte | `credito_presumido_transporte` | numeric(13) |  |  | Valor Crédito Presumido Transporte |
| valor_credito_presumido_suinos | `credito_presumido_suinos` | numeric(13) |  |  | Valor Crédito Presumido Suínos |
| valor_credito_presumido_suinos_estorno_e | `credito_presumido_suinos_estorno_entradas` | numeric(13) |  |  | Valor Crédito Presumido Suínos Estorno Entradas |
| valor_credito_presumido_suinos_estorno_d | `credito_presumido_suinos_estorno_devolucao` | numeric(13) |  |  | Valor Crédito Presumido Suínos Estorno Devolução |
| estorno_saldo_credor_estimativa_fixa | `estorno_saldo_credor_estimativa_fixa` | numeric(13) |  |  | Estorno do saldo credor de ICMS - Art. 4º, § 3º da IN nº 15/2005 |
| parcela_mensal_estimativa_fixa | `parcela_mensal_estimativa_fixa` | numeric(13) |  |  | Parcela mensal da Estimativa Fixa - Art. 805 do RICMS |
| credito_icms_recolhido_antecipadamente | `credito_icms_recolhido_antecipadamente` | numeric(13) |  |  | Crédito ICMS recolhido antecipadamente |
| transferencia_de_saldo_credor_art_59_a_d | `transferencia_saldo_credito_art_59_outros_debitos` | numeric(13) |  |  | Transferência de saldo credor - Art. 59-A do RICMS - Outros débitos |
| transferencia_saldo_credito_art_59_outro | `transferencia_saldo_credito_art_59_outros_creditos` | numeric(13) |  |  | Transferência de saldo credor - Art. 59-A do RICMS - Outros créditos |
| fecop_ce_debitos_pelas_saidas | `debito_fecop_icms` | numeric(13) |  |  | FECOP-CE - Débitos pelas saídas |
| transferencia_de_credito_de_icms_acumula | `transferencia_credito_icms_acumulado_outros_debitos` | numeric(13) |  |  | Transferência de crédito de ICMS acumulado - Outros débitos |
| transferencia_credito_icms_acumulado_out | `transferencia_credito_icms_acumulado_outros_creditos` | numeric(13) |  |  | Transferência de crédito de ICMS acumulado - Outros créditos |
| estorno_de_debito_nas_operacoes_com_ct_e | `estorno_debito_operacoes_cte_substituto` | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in)

## efsdoimp_subtri_por_uf_sc

**Saldo dos Impostos - Substituição Tributária Por SC** — tabela `EFSDOIMP_SUBTRI_POR_UF_SC` (122 linhas)

Saldo dos Impostos - Substituição Tributária Por SC. 122 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_VENCIMENTO_COMPLEMENTACAO`
- **Ordem padrão:** `DATA_VENCIMENTO_COMPLEMENTACAO desc`, `CODI_IMP asc`, `DATA_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 122 linhas, 6 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): data_de_vencimento_complementacao.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| sigla_da_uf | `sigla_uf` | char(2) |  |  | Sigla da UF |
| recolhimento | `i_recolhimento` | integer(4) |  |  | Recolhimento |
| debito_icms_sobre_estoque | `debito_icms_sobre_estoque` | numeric(13) |  |  | Débito ICMS Sobre Estoque |
| base_de_calculo_icms_st_sobre_estoque_fa | `base_calculo_icms_st_estoque_farmacia` | numeric(13) |  |  | Base de Cálculo ICMS ST Sobre Estoque - Farmácia |
| valor_icms_st_sobre_estoque_farmacia | `valor_icms_st_estoque_farmacia` | numeric(13) |  |  | Valor ICMS ST Sobre Estoque - Farmácia |
| valor_icms_sobre_frete | `valor_icms_sobre_frete` | numeric(13) |  |  | Valor ICMS Sobre Frete |
| base_calculo_icms_sobre_frete | `base_calculo_icms_sobre_frete` | numeric(13) |  |  | Base Cálculo ICMS Sobre Frete |
| base_calculo_icms_st_sobre_estoque | `base_calculo_icms_st_sobre_estoque` | numeric(13) |  |  | Base Cálculo ICMS ST Sobre Estoque |
| valor_icms_st_sobre_estoque | `valor_icms_st_sobre_estoque` | numeric(13) |  |  | Valor ICMS ST Sobre Estoque |
| base_calculo_icms_st_sobre_estoque_nao_d | `base_calculo_icms_st_sobre_estoque_nao_demonstrada` | numeric(13) |  |  | Base Cálculo ICMS ST Sobre Estoque - Não Demonstrada na DIME |
| valor_icms_st_sobre_estoque_nao_demonstr | `valor_icms_st_sobre_estoque_nao_demonstrada` | numeric(13) |  |  | Valor ICMS ST Sobre Estoque - Não Demonstrada na DIME |
| valor_do_fundosocial_st | `valor_fundosocial_st` | numeric(13) |  |  | Valor do FUNDOSOCIAL - ST |
| credito_adicional_do_fundosocial_st | `credito_adicional_fundosocial_st` | numeric(13) |  |  | Crédito Adicional do FUNDOSOCIAL - ST |
| saldo_st_sc | `saldo_st_sc` | numeric(13) |  |  | Saldo ST SC |
| st_antecipada_combustiveis | `st_antecipada_combustiveis` | numeric(13) |  |  | ST Antecipada Combustíveis |
| base_de_calculo_do_fundosocial_st | `base_calculo_fundosocial_st` | numeric(13) |  |  | Base de Cálculo do FUNDOSOCIAL - ST |
| credito_transferido_ao_estabelecimento_c | `credito_transferido_estabelecimento_consolidador` | numeric(13) |  |  | Crédito transferido ao estabelecimento consolidador |
| debitos_recebidos_de_estabelecimentos_co | `debito_recebido_estabelecimento_consolidador` | numeric(13) |  |  | Débitos recebidos de estabelecimentos consolidados |
| creditos_recebidos_de_estabelecimentos_c | `credito_recebido_estabelecimento_consolidador` | numeric(13) |  |  | Créditos recebidos de estabelecimentos consolidados |
| debito_transferido_ao_estabelecimento_co | `debito_transferido_estabelecimento_consolidador` | numeric(13) |  |  | Débito transferido ao estabelecimento consolidador |
| ressarcimento_de_icms_st_nas_vendas_para | `ressarcimento_icms_st_vendas_simples_nacional` | numeric(13) |  |  | Ressarcimento de ICMS ST nas vendas para Simples Nacional |
| ressarcimento_icms_st_vendas_outras_uf | `ressarcimento_icms_st_vendas_outras_uf` | numeric(13) |  |  | Ressarcimento de ICMS ST nas vendas para outras UF |
| credito_devolucao_st | `credito_devolucao_st` | numeric(13) |  |  | Crédito Devolução ST |
| valor_do_icms_sobre_estoque_produtos_exc | `valor_icms_sobre_estoque_produtos_excluidos_subtri` | numeric(13) |  |  | Valor do ICMS sobre estoque - Produtos excluídos SUBTRI |
| apropriacao_de_credito_por_devolucao_suj | `apropriacao_credito_devolucao_st` | numeric(13) |  |  | Apropriação de crédito por devolução sujeita à Subt. Trib. An. 3, art. 23 |
| estorno_de_credito_referente_ressarcimen | `estorno_credito_ressarcimento_st_vendas_simples_nacional` | numeric(13) |  |  | Estorno de crédito referente ressarcimento de ICMS ST nas vendas para SN - Decreto 3.509/10 |
| debito_referente_ao_fecop_pr_icms_st | `debito_fecop_icms_st` | numeric(13) |  |  | Débito referente ao FECOP-PR - ICMS ST |
| devolucao_referente_ao_fecop_pr_icms_st | `devolucao_fecop_icms_st` | numeric(13) |  |  | Devolução referente ao FECOP-PR - ICMS ST |
| valor_fundosocial_st_confeccao_art_21_es | `valor_fundosocial_st_confeccao_art_21_estab_centralizador` | numeric(13) |  |  | Valor do FUNDOSOCIAL - ST - Confecção Art 21 - Centralizador |
| valor_fundosocial_st_confeccao_art_21_es_c | `valor_fundosocial_st_confeccao_art_21_estab_centralizadora` | numeric(13) |  |  | Valor do FUNDOSOCIAL - ST - Confecção Art 21 - Centralizadora |
| ressarcimento_de_icms_st_acobertado_por | `ressarcimento_icms_st_acobertado_nfe` | numeric(13) |  |  | Ressarcimento de ICMS ST acobertado por NF-e |
| credito_icms_proprio_nas_vendas_para_out | `credito_icms_venda_outra_uf` | numeric(13) |  |  | Crédito ICMS Próprio nas vendas para outras UFs |
| valor_de_complementacao_do_icms_st | `valor_complementacao_icms_st` | numeric(13) |  |  | Valor de Complementação do ICMS ST |
| data_de_vencimento_complementacao | `data_vencimento_complementacao` | date(4) |  |  | Data de Vencimento Complementação |
| valor_pago | `valor_pago` | numeric(13) |  |  | Valor pago |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `sigla_da_uf` (eq/in), `recolhimento` (eq/in), `data_de_vencimento_complementacao` (entre/gte/lte)

## efsdoimp_inss_rb_por_recolhimento_por_atividade_cno

**Saldo dos Impostos - INSS Receita Bruta - Por Recolhimento - Por Atividade - CNO** — tabela `EFSDOIMP_INSS_RB_POR_RECOLHIMENTO_POR_ATIVIDADE_CNO` (111 linhas)

Saldo dos Impostos - INSS Receita Bruta - Por Recolhimento - Por Atividade - CNO. 111 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_RECOLHIMENTO, I_FILIAL, I_ATIVIDADE, I_SCP, I_CNO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_RECOLHIMENTO, I_FILIAL, I_ATIVIDADE, I_SCP, I_CNO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 111 linhas, 3 empresa(s), DATA_SIM de 2021-01-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| codigo_do_recolhimento | `codigo_recolhimento` | char(6) |  |  | Código do Recolhimento |
| codigo_da_filial | `i_filial` | integer(4) |  |  | Código da Filial |
| atividade_inss_receita_bruta | `i_atividade` | char(8) |  |  | Atividade INSS Receita Bruta |
| sequencial_scp | `i_scp` | integer(4) |  |  | Sequencial SCP |
| codigo_cno | `i_cno` | integer(4) |  |  | Código CNO |
| valor_da_receita_bruta_total_do_estabele | `receita_bruta_total` | numeric(13) |  |  | Valor da Receita Bruta Total do Estabelecimento no Período |
| valor_da_receita_bruta_real_nao_relacion | `receita_bruta_nao_relacionada` | numeric(13) |  |  | Valor da Receita Bruta Real - Não Relacionada |
| valor_da_receita_bruta_real | `receita_bruta_real` | numeric(13) |  |  | Valor da Receita Bruta Real |
| valor_das_devolucoes | `valor_devolucao` | numeric(13) |  |  | Valor das Devoluções |
| valor_das_devolucoes_resto | `valor_devolucao_resto` | numeric(13) |  |  | Valor das Devoluções - Resto |
| valor_da_receita_bruta_do_estabeleciment | `receita_bruta` | numeric(13) |  |  | Valor da Receita Bruta do Estabelecimento, correspondente às atividades/produtos |
| valor_das_exportacoes | `valor_exportacao` | numeric(13) |  |  | Valor das Exportações |
| valor_das_exportacoes_de_devolucao | `valor_exportacao_devolucao` | numeric(13) |  |  | Valor das Exportações de Devolução |
| valor_das_exclusoes_da_receita_bruta | `valor_exclusao` | numeric(13) |  |  | Valor das Exclusões da Receita Bruta |
| valor_da_base_de_calculo_da_contribuicao | `base_calculo` | numeric(13) |  |  | Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta |
| aliquota_da_contribuicao_previdenciaria | `aliquota` | numeric(8) |  |  | Alíquota da Contribuição Previdenciária sobre a Receita Bruta |
| valor_da_contribuicao_previdenciaria_apu | `valor_contribuicao_apurada` | numeric(13) |  |  | Valor da Contribuição Previdenciária Apurada sobre a Receita Bruta |
| valor_das_devolucoes_relacionada | `valor_devolucao_relacionada` | numeric(13) |  |  | Valor das Devoluções - Relacionada |
| valor_das_devolucoes_resto_relacionada | `valor_devolucao_resto_relacionada` | numeric(13) |  |  | Valor das Devoluções - Resto - Relacionada |
| valor_das_devolucoes_nao_relacionada | `valor_devolucao_nao_relacionada` | numeric(13) |  |  | Valor das Devoluções - Não Relacionada |
| valor_das_devolucoes_resto_nao_relaciona | `valor_devolucao_resto_nao_relacionada` | numeric(13) |  |  | Valor das Devoluções - Resto - Não Relacionada |
| valor_das_exclusoes_da_receita_bruta_rel | `valor_exclusao_relacionada` | numeric(13) |  |  | Valor das Exclusões da Receita Bruta - Relacionada |
| valor_das_exclusoes_da_receita_bruta_nao | `valor_exclusao_nao_relacionada` | numeric(13) |  |  | Valor das Exclusões da Receita Bruta - Não Relacionada |
| valor_das_exportacoes_relacionada | `valor_exportacao_relacionada` | numeric(13) |  |  | Valor das Exportações - Relacionada |
| valor_das_exportacoes_nao_relacionada | `valor_exportacao_nao_relacionada` | numeric(13) |  |  | Valor das Exportações - Não Relacionada |
| valor_das_exportacoes_de_devolucao_relac | `valor_exportacao_devolucao_relacionada` | numeric(13) |  |  | Valor das Exportações de Devolução - Relacionada |
| valor_das_exportacoes_de_devolucao_nao_r | `valor_exportacao_devolucao_nao_relacionada` | numeric(13) |  |  | Valor das Exportações de Devolução - Não Relacionada |
| valor_das_exportacoes_de_devolucao_resto | `valor_exportacao_devolucao_resto` | numeric(13) |  |  | Valor das Exportações de Devolução - Resto |
| valor_exportacao_devolucao_resto_nao_rel | `valor_exportacao_devolucao_resto_nao_relacionada` | numeric(13) |  |  | Valor das Exportações de Devolução - Resto - Não Relacionada |
| valor_exportacao_devolucao_resto_relacio | `valor_exportacao_devolucao_resto_relacionada` | numeric(13) |  |  | Valor das Exportações de Devolução - Resto - Relacionada |
| receita_bruta_total_reinf | `receita_bruta_total_reinf` | numeric(13) |  |  | Valor da Receita Bruta Total do Estabelecimento no Período REINF |
| receita_bruta_reinf | `receita_bruta_reinf` | numeric(13) |  |  | Valor da Receita Bruta do Estabelecimento, correspondente às atividades/produtos REINF |
| valor_das_exclusoes_da_receita_bruta_rei | `valor_exclusao_receita_bruta_reinf` | numeric(13) |  |  | Valor das Exclusões da Receita Bruta - REINF |
| acrescimo_da_receita_bruta_reinf | `acrescimo_receita_bruta_reinf` | numeric(13) |  |  | Acréscimo da Receita Bruta - REINF |
| reducao_da_receita_bruta_reinf | `reducao_receita_bruta_reinf` | numeric(13) |  |  | Redução da Receita Bruta - REINF |
| base_calculo_reinf | `base_calculo_reinf` | numeric(13) |  |  | Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta REINF |
| valor_contribuicao_apurada_reinf | `valor_contribuicao_apurada_reinf` | numeric(13) |  |  | Valor Contribuição Apurada REINF |
| valor_desconto_reinf | `desconto_reinf` | numeric(13) |  |  | Valor Desconto REINF |
| valor_ipi_reinf | `ipi_reinf` | numeric(13) |  |  | Valor IPI REINF |
| valor_icms_st_reinf | `icms_st_reinf` | numeric(13) |  |  | Valor ICMS ST REINF |
| valor_da_receita_bruta_real_reinf | `receita_bruta_real_reinf` | numeric(13) |  |  | Valor da Receita Bruta Real REINF |
| valor_das_devolucoes_reinf | `valor_devolucao_reinf` | numeric(13) |  |  | Valor das Devoluções REINF |
| valor_das_exportacoes_reeinf | `valor_exportacao_reinf` | numeric(13) |  |  | Valor das Exportações REEINF |
| valor_das_exportacoes_de_devolucao_reinf | `valor_exportacao_devolucao_reinf` | numeric(13) |  |  | Valor das Exportações de Devolução REINF |
| valor_das_devolucao_resto_reinf | `valor_devolucao_resto_reinf` | numeric(13) |  |  | Valor das Devolução Resto REINF |
| valor_das_devolucoes_relacionada_reinf | `valor_devolucao_relacionada_reinf` | numeric(13) |  |  | Valor das Devoluções - Relacionada REINF |
| valor_das_devolucoes_resto_relacionada_r | `valor_devolucao_resto_relacionada_reinf` | numeric(13) |  |  | Valor das Devoluções - Resto - Relacionada REINF |
| valor_das_devolucoes_nao_relacionada_rei | `valor_devolucao_nao_relacionada_reinf` | numeric(13) |  |  | Valor das Devoluções - Não Relacionada REINF |
| valor_devolucao_resto_nao_relacionada_re | `valor_devolucao_resto_nao_relacionada_reinf` | numeric(13) |  |  | Valor das Devoluções - Resto - Não Relacionada REINF |
| valor_exclusao_relacionada_reinf | `valor_exclusao_relacionada_reinf` | numeric(13) |  |  | Valor das Exclusões da Receita Bruta - Relacionada REINF |
| valor_exclusao_nao_relacionada_reinf | `valor_exclusao_nao_relacionada_reinf` | numeric(13) |  |  | Valor das Exclusões da Receita Bruta - Não Relacionada REINF |
| valor_das_exportacoes_relacionada_reinf | `valor_exportacao_relacionada_reinf` | numeric(13) |  |  | Valor das Exportações - Relacionada REINF |
| valor_das_exportacoes_de_devolucoes_rest | `valor_exportacao_nao_relacionada_reinf` | numeric(13) |  |  | Valor das Exportações de Devoluções - Resto REINF |
| valor_das_exportacoes_nao_relacionada_re | `valor_exportacao_devolucao_resto_reinf` | numeric(13) |  |  | Valor das Exportações - Não Relacionada REINF |
| valor_exportacao_devolucao_relacionada_r | `valor_exportacao_devolucao_relacionada_reinf` | numeric(13) |  |  | Valor das Exportações de Devolução - Relacionada REINF |
| valor_exportacao_devolucao_nao_relaciona | `valor_exportacao_devolucao_nao_relacionada_reinf` | numeric(13) |  |  | Valor das Exportações de Devolução - Não Relacionada REINF |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `codigo_do_recolhimento` (eq/in), `codigo_da_filial` (eq/in), `atividade_inss_receita_bruta` (eq/in), `sequencial_scp` (eq/in), `codigo_cno` (eq/in)

## efsdoimp_estadual_ro

**Saldo dos Impostos - Estadual RO** — tabela `EFSDOIMP_ESTADUAL_RO` (88 linhas)

Saldo dos Impostos - Estadual RO. 88 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_VENCIMENTO_ICMS_DOCUMENTOS_EXTEMPORANEOS`
- **Ordem padrão:** `DATA_VENCIMENTO_ICMS_DOCUMENTOS_EXTEMPORANEOS desc`, `CODI_IMP asc`, `DATA_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 88 linhas, 1 empresa(s), DATA_VENCIMENTO_ICMS_DOCUMENTOS_EXTEMPORANEOS de 2019-02-20 a 2025-05-20.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| credito_presumido_bares_e_restaurantes | `credito_presumido_bar_restaurante` | numeric(13) |  |  | Crédito Presumido Bares e Restaurantes |
| estorno_de_credito_presumido_bares_e_res | `estorno_credito_presumido_bar_restaurante` | numeric(13) |  |  | Estorno de Crédito Presumido Bares e Restaurantes |
| credito_presumido_bares_e_restaurantes_o | `credito_presumido_bar_restaurante_saida` | numeric(13) |  |  | Crédito Presumido Bares e Restaurantes - Origem Saída |
| credito_presumido_bar_restaurante_reduca | `credito_presumido_bar_restaurante_reducao_z` | numeric(13) |  |  | Crédito Presumido Bares e Restaurantes - Origem Redução Z |
| credito_presumido_transportes | `credito_presumido_transporte` | numeric(13) |  |  | Crédito Presumido Transportes |
| credito_presumido_transportes_conhecimen | `credito_presumido_transporte_ct_conv_106` | numeric(13) |  |  | Crédito Presumido Transportes - Conhecimento de Transporte |
| credito_presumido_transportes_bilhete_de | `credito_presumido_transporte_bp_conv_106` | numeric(13) |  |  | Crédito Presumido Transportes - Bilhete de Passagem |
| estorno_de_debito_icmsfg | `estorno_debito_icms_fg` | numeric(13) |  |  | Estorno de Débito ICMSFG |
| credito_presumido_industrias_torrefadora | `credito_presumido_ind_torrefadoras` | numeric(13) |  |  | Crédito Presumido Indústrias Torrefadoras |
| devolucao_credito_presumido_industrias_t | `devolucao_credito_presumido_ind_torrefadoras` | numeric(13) |  |  | Devolução Crédito Presumido Indústrias Torrefadoras |
| credito_presumido_ind_torrefadoras_saida | `credito_presumido_ind_torrefadoras_saida` | numeric(13) |  |  | Crédito Presumido Indústrias Torrefadoras - Origem Saídas |
| credito_presumido_ind_torrefadoras_reduc | `credito_presumido_ind_torrefadoras_reducao_z` | numeric(13) |  |  | Crédito Presumido Indústrias Torrefadoras - Origem Reduções Z |
| credito_icms_antecipado | `credito_icms_antecipado` | numeric(13) |  |  | Crédito ICMS Antecipado |
| transferencias_de_credito_de_icms_transf | `transferencia_saldo_credor` | numeric(13) |  |  | Transferências de crédito de ICMS - Transferido |
| transferencias_de_credito_de_icms_recebi | `recebimento_saldo_credor` | numeric(13) |  |  | Transferências de crédito de ICMS - Recebido |
| credito_presumido_bar_restaurante_nfc | `credito_presumido_bar_restaurante_nfc` | numeric(13) |  |  | Crédito Presumido Bares e Restaurantes - Origem Saída |
| devolucao_cred_presum_saidas_interest_in | `credito_pres_leite_item15_tabela1_anexoiv` | numeric(13) |  |  | Devolução créd. presum. saídas interest. indust. leite - Item 15, Tabela 1, Anexo IV |
| saidas_interestaduais_de_indust_do_leite | `estorno_credito_pres_leite_item15_tabela1_anexoiv` | numeric(13) |  |  | Saídas interestaduais de indust. do leite - Item 15, Tabela 1, Anexo IV |
| credito_pres_leite_item6_tabela1_anexoiv | `credito_pres_leite_item6_tabela1_anexoiv` | numeric(13) |  |  | Devolução créd. presum. saídas interest. indust. leite - Item 6, Tabela 1, Anexo IV |
| estorno_credito_pres_leite_item6_tabela1 | `estorno_credito_pres_leite_item6_tabela1_anexoiv` | numeric(13) |  |  | Saídas interestaduais de indust. do leite - Item 6, Tabela 1, Anexo IV |
| credito_de_icms_conf_aliquota_do_simples | `credito_conforme_aliquota_sn` | numeric(13) |  |  | Crédito de ICMS conf. alíquota do Simples Nacional - Art. 23, LC 123/06 |
| credito_presumido_nas_saidas_interest_de | `credito_presumido_mercadoria_imp_ext_lei_1473_2005` | numeric(13) |  |  | Crédito presumido nas saídas interest. de mercadoria importada do exterior - Lei nº. 1.473/2005 |
| devolucao_cred_presumido_saidas_interest | `devolucao_credito_presumido_mercadoria_imp_ext_lei_1473_2005` | numeric(13) |  |  | Devolução créd. presumido saídas interest. de mercadoria importada - Lei nº. 1.473/2005 |
| estorno_de_icms_dos_documentos_extempora | `estorno_icms_documentos_extemporaneos` | numeric(13) |  |  | Estorno de ICMS dos documentos extemporâneos |
| icms_dos_documentos_extemporaneos_a_reco | `icms_documentos_extemporaneos_recolher` | numeric(13) |  |  | ICMS dos documentos extemporâneos a recolher |
| icms_pago_dos_documentos_extemporaneos_a | `valor_pago_icms_documentos_extemporaneos` | numeric(13) |  |  | ICMS pago dos documentos extemporâneos a recolher |
| data_de_vencimento_icms_dos_documentos_e | `data_vencimento_icms_documentos_extemporaneos` | date(4) |  |  | Data de vencimento - ICMS dos documentos extemporâneos a recolher |
| credito_de_icms_proprio | `credito_icms_proprio_st_in_22_2018` | numeric(13) |  |  | Crédito de ICMS Próprio |
| ressarcimento_de_icms_st | `ressarcimento_icms_st_in_22_2018` | numeric(13) |  |  | Ressarcimento de ICMS ST |
| credito_presumido_consit_projeto_implant | `credito_presumido_consit_projeto_implantacao` | numeric(13) |  |  | Crédito presumido CONSIT, Decreto nº 12.988/2007, art. 2º, II |
| devolucao_do_credito_presumido_consit_de | `devolucao_credito_presumido_consit_projeto_implantacao` | numeric(13) |  |  | Devolução do crédito presumido CONSIT, Decreto nº 12.988/2007, art. 2º, II |
| estorno_de_credito_presumido_consit_decr | `estorno_credito_presumido_consit_projeto_implantacao` | numeric(13) |  |  | Estorno de Crédito presumido CONSIT, Decreto nº 12.988/2007, art. 2º, II |
| estorno_de_debito_icms_incentivado_consi | `estorno_debito_icms_incentivado_consit_projeto_implantacao` | numeric(13) |  |  | Estorno de Débito ICMS incentivado CONSIT, Decreto nº 12.988/2007, art. 2º, II |
| credito_presumido_saidas_internas_de_ovo | `credito_presumido_saidas_internas_ovo` | numeric(13) |  |  | Crédito presumido saídas internas de ovo - Item 10, Parte 2, Anexo IV |
| devolucao_cred_presumido_saidas_internas | `devolucao_credito_presumido_saidas_internas_ovo` | numeric(13) |  |  | Devolução créd. presumido saídas internas de ovo - Item 10, Parte 2, Anexo IV |
| exclusao_de_mercadorias_da_substituicao | `exclusao_mercadoria_subtri_decreto_22721_2018` | numeric(13) |  |  | Exclusão de mercadorias da substituição tributária - Dec. nº 22.721/18 |
| estorno_de_debito_nas_operacoes_com_ct_e | `estorno_debito_operacoes_cte_substituto` | numeric(13) |  |  | Estorno de débito nas operações com CT-e e/ou CT-eOS substituto |
| estorno_de_credito_presumido_ct_e_e_ou_c | `estorno_credito_presumido_cte_substituido` | numeric(13) |  |  | Estorno de Crédito Presumido CT-e e/ou CT-eOS Substituído - Item 3 - Parte 2 - Anexo IV |
| estorno_de_debito_referente_transferenci | `estorno_debito_referente_transferencia_creditos_icms_item_40_33_2018` | numeric(13) |  |  | Estorno de débito referente transferência de créditos de ICMS - Item 40 da IN 33/2018 |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `data_de_vencimento_icms_dos_documentos_e` (entre/gte/lte)

## efsdoimp_estadual_ac

**Saldo dos Impostos - Estadual AC** — tabela `EFSDOIMP_ESTADUAL_AC` (78 linhas)

Saldo dos Impostos - Estadual AC. 78 linhas no catálogo; chave: CODI_EMP, CODI_IMP, PDIC_SIM, DATA_SIM.

- **Chave:** `CODI_EMP, CODI_IMP, PDIC_SIM, DATA_SIM`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 78 linhas, 2 empresa(s), DATA_SIM de 2019-02-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| credito_ativo_imobilizado | `credito_ativo_imobilizado` | numeric(13) |  |  | Crédito Ativo Imobilizado |
| credito_icms_proprio_decreto_6875_2017 | `credito_icms_proprio_decreto_6875_2017` | numeric(13) |  |  | Crédito de ICMS Próprio conforme Art. 36-D, § 2º do Decreto 6.875/2017 |
| ressarcimento_icms_st_decreto_6875_2017 | `ressarcimento_icms_st_decreto_6875_2017` | numeric(13) |  |  | Ressarcimento de ICMS ST conforme Art. 36-D, § 2º do Decreto 6.875/2017 |
| estorno_de_credito_de_icms_nos_termos_do | `estorno_credito_icms_art_48_iv` | numeric(13) |  |  | Estorno de crédito de ICMS nos termos do artigo 48, IV do RICMS |
| credito_presumido_alcb_e_alccs_art_45_do | `credito_presumido_alcb_alccs` | numeric(13) |  |  | Crédito presumido  ALCB e ALCCS - Art. 45 do RICMS |
| devolucao_credito_presumido_alcb_e_alccs | `credito_presumido_alcb_alccs_devolucao` | numeric(13) |  |  | Devolução crédito presumido ALCB e ALCCS - Art. 45 do RICMS |
| credito_de_icms_conf_aliquota_do_simples | `credito_conforme_aliquota_sn` | numeric(13) |  |  | Credito de ICMS conf. alíquota do Simples Nacional - Art. 23, LC 123/06 |
| devolucao_de_mercadoria_adquirida_de_sim | `devolucao_mercadoria_adquirida_sn` | numeric(13) |  |  | Devolucao de mercadoria adquirida de Simples Nacional |

**Filtros:** `imposto` (eq/in), `periodicidade` (eq/in), `competencia` (eq/in)

## efsdoimp_por_uf_mg

**Saldo dos Impostos - Por UF - MG** — tabela `EFSDOIMP_POR_UF_MG` (71 linhas)

Saldo dos Impostos - Por UF - MG. 71 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 71 linhas, 2 empresa(s), DATA_SIM de 2021-07-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| sigla_da_uf | `sigla_uf` | char(2) |  |  | Sigla da UF |
| outros_debitos | `outros_debitos_lancado` | numeric(15) |  |  | Outros débitos |
| outros_creditos | `outros_creditos_lancado` | numeric(15) |  |  | Outros créditos |
| estorno_de_debitos | `estorno_debitos_lancado` | numeric(15) |  |  | Estorno de débitos |
| estorno_de_creditos | `estorno_creditos_lancado` | numeric(15) |  |  | Estorno de créditos |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `sigla_da_uf` (eq/in)

## efsdoimp_estadual_es

**Saldo dos Impostos - Estadual ES** — tabela `EFSDOIMP_ESTADUAL_ES` (67 linhas)

Saldo dos Impostos - Estadual ES. 67 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 67 linhas, 7 empresa(s), DATA_SIM de 2017-10-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| valor_credito_presumido_transporte | `credito_presumido_transporte` | numeric(13) |  |  | Valor Crédito Presumido Transporte |
| estorno_de_debito_da_apuracao_propria_pa | `estorno_debito_apuracao_propria_fundap` | numeric(13) |  |  | Estorno de débito da apuração própria para apuração em separado-ICMS FUNDAP Art. 757 RICMS |
| credito_presumido_beneficio_art_530_lri | `credito_presumido_beneficio_art_530_lri_ricms` | numeric(13) |  |  | Crédito Presumido - Benefício Art. 530-LRI RICMS |
| estorno_do_icms_das_ope_beneficiadas_art | `estorno_icms_ope_beneficiadas_art_530_lri_ricms` | numeric(13) |  |  | Estorno do ICMS das ope. Beneficiadas - Art. 530-LRI RICMS |
| estorno_credito_presumido_beneficio_art | `estorno_credito_presumido_beneficio_art_530_lri_ricms_devolucao` | numeric(13) |  |  | Estorno Crédito Presumido - Benefício Art. 530-LRI RICMS - Devolução |
| estorno_do_icms_a_recolher_das_oper_bene | `estorno_icms_recolher_oper_beneficiadas_art_530_lri_icms` | numeric(13) |  |  | Estorno do ICMS a recolher das Oper. beneficiadas Art.530-LRI RICMS |
| debito_de_diferencial_de_aliquota_parece | `debito_diferencial_aliquota_parecer_norm_003_2013` | numeric(13) |  |  | Débito de diferencial de alíquota - Parecer Norm. Nº 003/2013 |
| est_credito_operacao_da_apuracao_propria | `estorno_credito_operacao_apuracao_propria_fundap` | numeric(13) |  |  | Est. crédito operação da apuração própria para apuração em separado - ICMS FUNDAP |
| est_credito_prestacao_da_apuracao_propri | `estorno_credito_prestacao_apuracao_propria_fundap` | numeric(13) |  |  | Est. crédito prestação da apuração própria para apuração em separado - ICMS FUNDAP |
| funcop_es_debitos_pelas_saidas | `debito_funcop_icms` | numeric(13) |  |  | FUNCOP-ES - Débitos pelas saídas |
| credito_presumido_nas_saidas_interestadu | `credito_presumido_interestaduais_ind_metalmecanica_beneficio_art_530_lfii_ricms` | numeric(13) |  |  | Crédito presumido nas saídas interestaduais - Art. 530-LF, II RICMS |
| estorno_devolucao_cred_presumido_benefic | `estorno_devolucao_credito_presumido_interestaduais_ind_metalmecanica_beneficio_art_530_lfii_ricms` | numeric(13) |  |  | Estorno devolução créd. presumido - Benefício Art. 530-LF, II RICMS |
| estorno_do_icms_saidas_interestaduais_ar | `estorno_icms_saidas_interestaduais_ind_metalmecanica_beneficio_art_530_lfii_ricms` | numeric(13) |  |  | Estorno do ICMS saídas interestaduais - Art. 530-LF, § 1º, III RICMS |
| estorno_icms_saidas_internas_ind_metalme | `estorno_icms_saidas_internas_ind_metalmecanica_beneficio_art_530_lfii_ricms` | numeric(13) |  |  | Estorno do ICMS saídas internas - Art. 530-LF, § 1º, II RICMS |
| estorno_icms_recolher_oper_beneficio_art | `estorno_icms_recolher_oper_beneficio_art_530_lf_ricms` | numeric(13) |  |  | Estorno do ICMS a recolher das Oper. beneficiadas - Art. 530-LF, § 1º RICMS |
| estorno_de_debito_nas_operacoes_com_ct_e | `estorno_debito_operacoes_cte_substituto` | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in)

## efsdoimp_es_compete

**Saldo dos Impostos - COMPETE - ES** — tabela `EFSDOIMP_ES_COMPETE` (67 linhas)

Saldo dos Impostos - COMPETE - ES. 67 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 67 linhas, 7 empresa(s), DATA_SIM de 2017-10-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| periodo | `data_sim` | date(4) |  |  | Período |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| vencimento | `vencimento` | date(4) |  |  | Vencimento |
| codigo_recolhimento | `codigo_recolhimento` | char(6) |  |  | Código recolhimento |
| valor_a_recolher | `valor_recolher` | numeric(13) |  |  | Valor a recolher |
| valor_pago | `valor_pago` | numeric(13) |  |  | Valor pago |
| deducao_credito_art_534_zza | `deducao_credito_art_534_zza` | numeric(13) |  |  | Dedução do crédito total - Art. 534-Z-Z-A, §2°, III, a |
| deducao_credito_art_530_lrk | `deducao_credito_art_530_lrk` | numeric(13) |  |  | Dedução do crédito total - Art. 530-L-R-K, §4, III, a |
| outros_debitos_devolucoes_de_vendas_inte | `outros_debitos_devolucao_venda_interna` | numeric(13) |  |  | Outros Débitos - Devoluções de vendas internas |
| outros_debitos_devolucao_venda_interesta | `outros_debitos_devolucao_venda_interestaduais` | numeric(13) |  |  | Outros Débitos - Devoluções de vendas interestaduais |
| outros_debitos_devolucoes_de_compras_int | `outros_debitos_devolucao_compra_interna` | numeric(13) |  |  | Outros Débitos - Devoluções de compras internas |
| outros_debitos_devolucao_compra_interest | `outros_debitos_devolucao_compra_interestaduais` | numeric(13) |  |  | Outros Débitos - Devoluções de compras interestaduais |
| estorno_de_creditos_devolucoes_de_vendas | `estorno_creditos_devolucao_venda_interna` | numeric(13) |  |  | Estorno de Créditos - Devoluções de vendas internas |
| estorno_creditos_devolucao_venda_interes | `estorno_creditos_devolucao_venda_interestaduais` | numeric(13) |  |  | Estorno de Créditos - Devoluções de vendas interestaduais |
| estorno_de_creditos_devolucoes_de_compra | `estorno_creditos_devolucao_compra_interna` | numeric(13) |  |  | Estorno de Créditos - Devoluções de compras internas |
| estorno_creditos_devolucao_compra_intere | `estorno_creditos_devolucao_compra_interestaduais` | numeric(13) |  |  | Estorno de Créditos - Devoluções de compras interestaduais |
| outros_creditos_devolucoes_de_vendas_int | `outros_creditos_devolucao_venda_interna` | numeric(13) |  |  | Outros Créditos - Devoluções de vendas internas |
| outros_creditos_devolucao_venda_interest | `outros_creditos_devolucao_venda_interestaduais` | numeric(13) |  |  | Outros Créditos - Devoluções de vendas interestaduais |
| outros_creditos_devolucoes_de_compras_in | `outros_creditos_devolucao_compra_interna` | numeric(13) |  |  | Outros Créditos - Devoluções de compras internas |
| outros_creditos_devolucao_compra_interes | `outros_creditos_devolucao_compra_interestaduais` | numeric(13) |  |  | Outros Créditos - Devoluções de compras interestaduais |
| estorno_de_debitos_devolucoes_de_vendas | `estorno_debitos_devolucao_venda_interna` | numeric(13) |  |  | Estorno de Débitos - Devoluções de vendas internas |
| estorno_debitos_devolucao_venda_interest | `estorno_debitos_devolucao_venda_interestaduais` | numeric(13) |  |  | Estorno de Débitos - Devoluções de vendas interestaduais |
| estorno_de_debitos_devolucoes_de_compras | `estorno_debitos_devolucao_compra_interna` | numeric(13) |  |  | Estorno de Débitos - Devoluções de compras internas |
| estorno_debitos_devolucao_compra_interes | `estorno_debitos_devolucao_compra_interestaduais` | numeric(13) |  |  | Estorno de Débitos - Devoluções de compras interestaduais |
| credito_registrado_ou_limitado_base_redu | `credito_base_reduzida` | numeric(13) |  |  | Crédito registrado ou limitado - Base Reduzida - Art. 534-Z-Z-A, §2°, III, b |
| credito_registrado_ou_limitado_fora_do_e | `credito_fora_estado` | numeric(13) |  |  | Crédito registrado ou limitado - Fora do Estado - Art. 530-L-R-K, §4°, III, b |
| ajsute_para_recolher_o_imposto_devido_na | `ajuste_recolher_imposto_operacao_art_530_lrk` | numeric(13) |  |  | Ajsute para recolher o imposto devido nas operações do Art. 530-L-R-K |
| estorno_adicional_de_debito_das_saidas_i | `estorno_adicional_saidas_interestaduais` | numeric(13) |  |  | Estorno adicional de débito das saídas interestaduais - Art. 530-L-R-K |
| saldo_credor_apuracao_operacoes_internas | `saldo_credor_apuracao_operacoes_internas` | numeric(13) |  |  | Saldo credor Apuração operações internas |
| saldo_devedor_apuracao_operacoes_interes | `saldo_devedor_apuracao_operacoes_interestaduais` | numeric(13) |  |  | Saldo devedor Apuração operações interestaduais |
| saldo_credor_anterior_internas | `saldo_credor_anterior_internas` | numeric(13) |  |  | Saldo credor Anterior Internas |
| saidas_sem_beneficio_com_partic_proporca | `vendas_sem_beneficio` | numeric(13) |  |  | Saídas sem benefício com partic. proporção |
| total_saidas | `vendas_totais_tributada` | numeric(13) |  |  | Total Saídas |
| saidas_com_reducao_b_c_art_534_zza | `vendas_internas_beneficiadas` | numeric(13) |  |  | Saídas com Redução B.C. - Art. 534-ZZA |
| saidas_interestaduais_art_530_lrk | `vendas_interestaduais_beneficiadas` | numeric(13) |  |  | Saídas interestaduais - Art. 530-LRK |
| saidas_com_reducao_b_c_art_534_zza_propo | `proporcao_vib` | numeric(13) |  |  | Saídas com Redução B.C. - Art. 534-ZZA / Proporção |
| saidas_interestaduais_art_530_lrk_propor | `proporcao_vintb` | numeric(13) |  |  | Saídas interestaduais - Art. 530-LRK / Proporção |
| proporcao_vsb | `proporcao_vsb` | numeric(13) |  |  | Saídas sem benefício com partic. proporção / Proporção |
| limite_de_credito_das_entradas_proporcio | `base_calculo_entradas_proporcao_sem_7_porcento_vib` | numeric(13) |  |  | Limite de crédito das entradas proporcionais/Base cálculo ICMS VIB |
| base_calculo_entradas_proporcao_com_7_po | `base_calculo_entradas_proporcao_com_7_porcento_vib` | numeric(13) |  |  | Limite de crédito das entradas proporcionais/Limite de 7% VIB |
| base_calculo_entradas_proporcao_sem_7_po | `base_calculo_entradas_proporcao_sem_7_porcento_vintb` | numeric(13) |  |  | Limite de crédito das entradas proporcionais/Base cálculo ICMS VINTB |
| base_calculo_entradas_proporcao_com_7_po_c | `base_calculo_entradas_proporcao_com_7_porcento_vintb` | numeric(13) |  |  | Limite de crédito das entradas proporcionais/Limite de 7% VINTB |
| base_calculo_entradas_proporcao_sem_7_po_c | `base_calculo_entradas_proporcao_sem_7_porcento_vsb` | numeric(13) |  |  | Limite de crédito das entradas proporcionais/Base cálculo ICMS VSB |
| valor_imposto_rateio_vib | `valor_imposto_rateio_vib` | numeric(13) |  |  | Limite de crédito das entradas proporcionais/Crédito p/Rateio VIB |
| valor_imposto_rateio_vintb | `valor_imposto_rateio_vintb` | numeric(13) |  |  | Limite de crédito das entradas proporcionais/Crédito p/Rateio VINTB |
| limite_credito_vib | `limite_credito_vib` | numeric(13) |  |  | Limite de crédito das entradas proporcionais/Limite de crédito total VIB |
| limite_credito_vintb | `limite_credito_vintb` | numeric(13) |  |  | Limite de crédito das entradas proporcionais/Limite de crédito total VINTB |
| credito_total | `credito_registrados_proporcionais_valor_entradas` | numeric(13) |  |  | Crédito Total |
| credito_proporcional_vsb | `credito_vsb` | numeric(13) |  |  | Crédito proporcional VSB |
| saldo_credor_anterior_pessoa_fisica | `saldo_credor_anterior_pessoa_fisica` | numeric(13) |  |  | Saldo credor Anterior Pessoa Física |
| valor_saidas_internas | `valor_saidas_internas` | numeric(13) |  |  | Valor Saídas Internas |
| saldo_devedor_apuracao_operacoes_interna | `saldo_devedor_apuracao_operacoes_internas` | numeric(13) |  |  | Saldo devedor Apuração operações internas |
| base_calculo_carga_efetiva_ind_com | `base_calculo_ind_com` | numeric(13) |  |  | Base Calculo Carga Efetiva Ind Com |
| carga_efetiva_ind_com | `percentual_carga_efetiva_ind_com` | numeric(13) |  |  | % Carga Efetiva Ind Com |
| valor_carga_efetiva_ind_com | `valor_carga_efetiva_ind_com` | numeric(13) |  |  | Valor Carga Efetiva Ind Com |
| base_calculo_carga_efetiva_cf | `base_calculo_cf` | numeric(13) |  |  | Base Calculo Carga Efetiva CF |
| carga_efetiva_cf | `percentual_carga_efetiva_cf` | numeric(13) |  |  | % Carga Efetiva CF |
| valor_carga_efetiva_cf | `valor_carga_efetiva_cf` | numeric(13) |  |  | Valor Carga Efetiva CF |

**Filtros:** `imposto` (eq/in), `periodo` (eq/in), `periodicidade` (eq/in), `vencimento` (entre/gte/lte), `codigo_recolhimento` (eq/in)

## efsdoimp_estadual_pi

**Saldo dos Impostos - Estadual PI** — tabela `EFSDOIMP_ESTADUAL_PI` (65 linhas)

Saldo dos Impostos - Estadual PI. 65 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_VENCIMENTO_ICMS_DOCUMENTOS_EXTEMPORANEOS`
- **Ordem padrão:** `DATA_VENCIMENTO_ICMS_DOCUMENTOS_EXTEMPORANEOS desc`, `CODI_IMP asc`, `DATA_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 65 linhas, 1 empresa(s), DATA_VENCIMENTO_ICMS_DOCUMENTOS_EXTEMPORANEOS de 2023-05-15 a 2025-04-15.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| credito_ativo_imobilizado | `credito_ativo_imobilizado` | numeric(13) |  |  | Crédito Ativo Imobilizado |
| credito_presumido_de_20_para_transportad | `credito_presumido_20_transportadoras_icms` | numeric(13) |  |  | Crédito presumido de 20% para transportadoras - Art. 56, III do RICMS |
| fecop_pi_valor | `debito_fecop_icms` | numeric(13) |  |  | FECOP PI - Valor |
| credito_icms_antecipacao_parcial | `credito_icms_antecipacao_parcial` | numeric(13) |  |  | Antecipação Parcial - RICMS Art. 771 |
| regime_especial_de_tributacao_base_entra | `produtos_farmaceuticos_base_entradas_internas_3_art_791` | numeric(13) |  |  | Regime especial de tributação - Base Entradas internas 3%, Art. 791-F, I, b |
| produtos_farmaceuticos_base_entradas_int | `produtos_farmaceuticos_base_entradas_interestaduais_63_art_791` | numeric(13) |  |  | Regime especial de tributação - Base Entradas interest. 6,3%, Art. 791-F, I, a |
| regime_especial_de_tributacao_base_adici | `produtos_farmaceuticos_base_adicional_excedente_5_art_791` | numeric(13) |  |  | Regime especial de tributação - Base Adicional excedente 5% PF, Art. 791-M |
| regime_especial_de_tributacao_entradas_i | `produtos_farmaceuticos_entradas_internas_3_art_791` | numeric(13) |  |  | Regime especial de tributação - Entradas internas 3%, Art. 791-F, I, b |
| produtos_farmaceuticos_entradas_interest | `produtos_farmaceuticos_entradas_interestaduais_63_art_791` | numeric(13) |  |  | Regime especial de tributação - Entradas interest. 6,3%, Art. 791-F, I, a |
| regime_especial_de_tributacao_adicional | `produtos_farmaceuticos_adicional_excedente_5_art_791` | numeric(13) |  |  | Regime especial de tributação - Adicional excedente 5% PF, Art. 791-M |
| estorno_de_credito_resultante_da_sistema | `produtos_farmaceuticos_estorno_credito` | numeric(13) |  |  | Estorno de crédito resultante da sistemática normal - Produtos farmacêuticos |
| estorno_de_debito_resultante_da_sistemat | `produtos_farmaceuticos_estorno_debito` | numeric(13) |  |  | Estorno de débito resultante da sistemática normal - Produtos farmacêuticos |
| a_saldo_credor_do_periodo_anterior_produ | `produtos_farmaceuticos_a_saldo_credor_anterior` | numeric(13) |  |  | A - Saldo credor do período anterior - Produtos farmacêuticos |
| b_valor_saldo_credor_do_periodo_produtos | `produtos_farmaceuticos_b_saldo_credor_periodo` | numeric(13) |  |  | B - Valor Saldo credor do período - Produtos farmacêuticos |
| c_antecipacao_parcial_produtos_farmaceut | `produtos_farmaceuticos_c_antecipacao_parcial` | numeric(13) |  |  | C - Antecipação Parcial - Produtos farmacêuticos |
| d_valor_saldo_devedor_do_periodo_produto | `produtos_farmaceuticos_d_valor_saldo_devedor_periodo` | numeric(13) |  |  | D - Valor Saldo devedor do período - Produtos farmacêuticos |
| resultante_debito_produtos_farmaceuticos | `produtos_farmaceuticos_resultante_debito` | numeric(13) |  |  | Resultante - Débito - Produtos farmacêuticos |
| resultante_credito_produtos_farmaceutico | `produtos_farmaceuticos_resultante_credito` | numeric(13) |  |  | Resultante - Crédito - Produtos farmacêuticos |
| icms_a_recolher_no_regime_especial_de_tr | `produtos_farmaceuticos_icms_a_recolher` | numeric(13) |  |  | ICMS a recolher no Regime Especial de Tributação - Produtos farmacêuticos |
| valor_pago_de_icms_do_regime_especial_de | `produtos_farmaceuticos_icms_valor_pago` | numeric(13) |  |  | Valor Pago de ICMS do Regime Especial de Tributação - Produtos farmacêuticos |
| juros_e_multa_por_escrituracao_extempora | `juros_multa_icms_documentos_extemporaneos` | numeric(13) |  |  | Juros e multa por escrituração extemporânea de documentos fiscais |
| estorno_de_icms_dos_documentos_extempora | `estorno_icms_documentos_extemporaneos` | numeric(13) |  |  | Estorno de ICMS dos documentos extemporâneos |
| estorno_icms_documentos_extemporaneos_se | `estorno_icms_documentos_extemporaneos_sem_juros_multa` | numeric(13) |  |  | Estorno de ICMS dos documentos extemporâneos (Sem juros e multa) |
| icms_dos_documentos_extemporaneos_a_reco | `icms_documentos_extemporaneos_recolher` | numeric(13) |  |  | ICMS dos documentos extemporâneos a recolher |
| valor_pago_icms_documentos_extemporaneos | `valor_pago_icms_documentos_extemporaneos` | numeric(13) |  |  | Valor pago ICMS documentos extemporâneos |
| data_vencimento_icms_documentos_extempor | `data_vencimento_icms_documentos_extemporaneos` | date(4) |  |  | Data vencimento ICMS documentos extemporâneos |
| estorno_de_debito_nas_operacoes_com_ct_e | `estorno_debito_operacoes_cte_substituto` | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `data_vencimento_icms_documentos_extempor` (entre/gte/lte)

## efsdoimp_subtri_por_uf_pi

**Saldo dos Impostos - Substituição Tributária Por PI** — tabela `EFSDOIMP_SUBTRI_POR_UF_PI` (65 linhas)

Saldo dos Impostos - Substituição Tributária Por PI. 65 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 65 linhas, 1 empresa(s), DATA_SIM de 2019-11-01 a 2025-03-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| sigla_da_uf | `sigla_uf` | char(2) |  |  | Sigla da UF |
| recolhimento | `i_recolhimento` | integer(4) |  |  | Recolhimento |
| adicional_fecop_icms_st_saidas_internas | `adicional_fecop` | numeric(13) |  |  | Adicional FECOP - ICMS ST - Saídas Internas |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `sigla_da_uf` (eq/in), `recolhimento` (eq/in)

## efsdoimp_simples_nacional_controle_base_negativa_devolucao_s

**Saldo Simples Nacional Controle Base de Base Negativa Devolução Secundária 2025** — tabela `EFSDOIMP_SIMPLES_NACIONAL_CONTROLE_BASE_NEGATIVA_DEVOLUCAO_SECUNDARIA` (63 linhas)

Saldo Simples Nacional Controle Base de Base Negativa Devolução Secundária 2025. 63 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, PERIODO_APURACAO, ANEXO, SECAO, TABELA, FILIAL, ARBCISS, TIPO_RECEITA, ARBCPIS, ARBCCOFINS, SITUACOES, ARBCICMS, SEQUENCIAL, MUNICIPIO, CONSIDERAR_ALIQUOTA_REDUCAO_ICMS, ANEXO_ORIGEM, SECAO_ORIGEM, TABELA_ORIGEM, APLICA_REDUCAO_BASE_CALCULO_ICMS, APLICA_REDUCAO_ISS.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, PERIODO_APURACAO, ANEXO, SECAO, TABELA, FILIAL, ARBCISS, TIPO_RECEITA, ARBCPIS, ARBCCOFINS, SITUACOES, ARBCICMS, SEQUENCIAL, MUNICIPIO, CONSIDERAR_ALIQUOTA_REDUCAO_ICMS, ANEXO_ORIGEM, SECAO_ORIGEM, TABELA_ORIGEM, APLICA_REDUCAO_BASE_CALCULO_ICMS, APLICA_REDUCAO_ISS`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 63 linhas, 4 empresa(s), DATA_SIM de 2025-01-01 a 2026-09-01.
- tipo_receita_1_mercado_interno_2_exporta: todos os valores reais estão no comentário do banco (2=33, 1=30).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da Empresa |
| codigo_do_imposto | `codi_imp` | integer(4) |  |  | Código do Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| periodo_da_origem_da_base_negativa_deevo | `periodo_apuracao` | date(4) |  |  | Período da Origem da Base Negativa Deevolução Secundária |
| anexo | `anexo` | tinyint(1) |  |  | ANEXO |
| secao | `secao` | tinyint(1) |  |  | SECAO |
| tabela | `tabela` | tinyint(1) |  |  | TABELA |
| codigo_empresa_filial | `filial` | integer(4) |  |  | Código Empresa Filial |
| aliquota_de_reducao_da_base_de_calculo_d | `arbciss` | numeric(13) |  |  | Aliquota de reducao da base de calculo do ISS |
| tipo_receita_1_mercado_interno_2_exporta | `tipo_receita` | integer(4) |  | efsdoimp_simples_nacional_controle_base_negativa_devolucao_s_tipo_receit | Tipo Receita (1- Mercado Interno / 2- Exportação) |
| aliquota_de_reducao_de_base_de_calculo_d | `arbcpis` | numeric(13) |  |  | Alíquota de Redução de Base de Cálculo do PIS |
| arbccofins | `arbccofins` | numeric(13) |  |  | Alíquota de Redução de Base de Cálculo do COFINS |
| situacoes_fiscais | `situacoes` | char(16) |  |  | Situacoes fiscais |
| arbcicms | `arbcicms` | numeric(13) |  |  | Aliquota de reducao da base de calculo do ICMS |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| codigo_do_municipio | `municipio` | integer(4) |  |  | Código do município |
| considerar_aliquota_reducao_icms | `considerar_aliquota_reducao_icms` | char(1) |  |  | CONSIDERAR ALÍQUOTA REDUCÃO ICMS |
| anexo_origem | `anexo_origem` | integer(4) |  |  | Anexo Origem |
| secao_origem | `secao_origem` | integer(4) |  |  | Seção Origem |
| tabela_origem | `tabela_origem` | integer(4) |  |  | Tabela Origem |
| aplica_reducao_na_base_de_calculo_do_icm | `aplica_reducao_base_calculo_icms` | char(1) |  |  | Aplica redução na base de calculo do ICMS |
| reducao_do_iss_aplicado_na_aliquota_ou_n | `aplica_reducao_iss` | char(1) |  |  | Redução do ISS aplicado na Alíquota ou na Base de Calculo |
| valor_da_base_secundaria_a_descontar_da | `valor_base_descontar` | numeric(13) |  |  | Valor da base secundaria a descontar da devolução |

**Filtros:** `codigo_do_imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `periodo_da_origem_da_base_negativa_deevo` (eq/in), `anexo` (eq/in), `secao` (eq/in), `tabela` (eq/in), `codigo_empresa_filial` (eq/in), `aliquota_de_reducao_da_base_de_calculo_d` (eq/in), `tipo_receita_1_mercado_interno_2_exporta` (eq/in), `aliquota_de_reducao_de_base_de_calculo_d` (eq/in), `arbccofins` (eq/in), `situacoes_fiscais` (eq/in), `arbcicms` (eq/in)

## efsdoimp_estadual_sc

**Saldo dos Impostos - Estadual SC** — tabela `EFSDOIMP_ESTADUAL_SC` (61 linhas)

Saldo dos Impostos - Estadual SC. 61 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 61 linhas, 6 empresa(s), DATA_SIM de 2021-01-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| base_calculo_devolucao_ttd_409_410_411 | `base_calculo_devolucao_ttd_409_410_411` | numeric(13) |  |  | Base de Calculo de ICMS Devolução TTD 409, 410 ou 411 |
| base_calculo_saida_ttd_409_410_411 | `base_calculo_saida_ttd_409_410_411` | numeric(13) |  |  | Base de Calculo de ICMS Saída TTD 409, 410 ou 411 |
| credito_presumido_ttd_409_410_411 | `credito_presumido_ttd_409_410_411` | numeric(13) |  |  | Valor Crédito Presumido TTD 409, 410 ou 411 |
| valor_devolucao_de_credito_presumido_ttd | `devolucao_credito_presumido_ttd_409_410_411` | numeric(13) |  |  | Valor Devolução de Crédito Presumido TTD 409, 410 ou 411 |
| valor_de_estorno_de_debito_ttd_409_410_o | `estorno_debito_ttd_409_410_411` | numeric(13) |  |  | Valor de Estorno de Débito TTD 409, 410 ou 411 |
| valor_de_devolucao_de_estorno_de_debito | `devolucao_estorno_debito_ttd_409_410_411` | numeric(13) |  |  | Valor de Devolução de Estorno de Débito TTD 409, 410 ou 411 |
| devolucao_fundec_ttd_409_410_411 | `devolucao_fundec_ttd_409_410_411` | numeric(13) |  |  | Valor Devolução FUNDEC TTD 409, 410 ou 411 |
| devolucao_fundo_educacao_ttd_409_410_411 | `devolucao_fundo_educacao_ttd_409_410_411` | numeric(13) |  |  | Valor Devolução Fundo Educação TTD 409, 410 ou 411 |
| devolucao_pro_emprego_ttd_409_410_411 | `devolucao_pro_emprego_ttd_409_410_411` | numeric(13) |  |  | Valor Devolução Pró-Emprego TTD 409, 410 ou 411 |
| valor_credito_presumido_gado | `credito_presumido_gado` | numeric(13) |  |  | Valor Crédito Presumido Gado |
| valor_credito_presumido_gado_tipo_1_oper | `credito_presumido_gado_tipo_1_interno` | numeric(13) |  |  | Valor Crédito Presumido Gado Tipo 1 Operação Estadual |
| valor_credito_presumido_gado_tipo_2_oper | `credito_presumido_gado_tipo_2_interno` | numeric(13) |  |  | Valor Crédito Presumido Gado Tipo 2 Operação Estadual |
| valor_credito_presumido_gado_tipo_3_oper | `credito_presumido_gado_tipo_3_interno` | numeric(13) |  |  | Valor Crédito Presumido Gado Tipo 3 Operação Estadual |
| credito_presumido_gado_tipo_1_externo | `credito_presumido_gado_tipo_1_externo` | numeric(13) |  |  | Valor Crédito Presumido Gado Tipo 1 Operação Interestadual |
| credito_presumido_gado_tipo_2_externo | `credito_presumido_gado_tipo_2_externo` | numeric(13) |  |  | Valor Crédito Presumido Gado Tipo 2 Operação Interestadual |
| credito_presumido_gado_tipo_3_externo | `credito_presumido_gado_tipo_3_externo` | numeric(13) |  |  | Valor Crédito Presumido Gado Tipo 3 Operação Interestadual |
| valor_estorno_credito_presumido_gado | `estorno_credito_presumido_gado` | numeric(13) |  |  | Valor Estorno Crédito Presumido Gado |
| valor_estorno_credito_presumido_gado_tip | `estorno_credito_presumido_gado_tipo_1_interno` | numeric(13) |  |  | Valor Estorno Crédito Presumido Gado Tipo 1 Operação Estadual |
| estorno_credito_presumido_gado_tipo_2_in | `estorno_credito_presumido_gado_tipo_2_interno` | numeric(13) |  |  | Valor Estorno Crédito Presumido Gado Tipo 2 Operação Estadual |
| estorno_credito_presumido_gado_tipo_3_in | `estorno_credito_presumido_gado_tipo_3_interno` | numeric(13) |  |  | Valor Estorno Crédito Presumido Gado Tipo 3 Operação Estadual |
| estorno_credito_presumido_gado_tipo_1_ex | `estorno_credito_presumido_gado_tipo_1_externo` | numeric(13) |  |  | Valor Estorno Crédito Presumido Gado Tipo 1 Operação Interestadual |
| estorno_credito_presumido_gado_tipo_2_ex | `estorno_credito_presumido_gado_tipo_2_externo` | numeric(13) |  |  | Valor Estorno Crédito Presumido Gado Tipo 2 Operação Interestadual |
| estorno_credito_presumido_gado_tipo_3_ex | `estorno_credito_presumido_gado_tipo_3_externo` | numeric(13) |  |  | Valor Estorno Crédito Presumido Gado Tipo 3 Operação Interestadual |
| valor_credito_presumido_madeira_serrada | `credito_presumido_madeira_serrada` | numeric(13) |  |  | Valor Crédito Presumido Madeira Serrada |
| valor_devolucao_credito_presumido_madeir | `devolucao_credito_presumido_madeira_serrada` | numeric(13) |  |  | Valor Devolução Crédito Presumido Madeira Serrada |
| valor_credito_pro_emprego | `credito_pro_emprego` | numeric(13) |  |  | Valor Crédito Pro Emprego |
| valor_estorno_credito_pro_emprego | `estorno_credito_pro_emprego` | numeric(13) |  |  | Valor Estorno Crédito Pro Emprego |
| prazo_de_carencia_pro_emprego | `carencia_pro_emprego` | integer(4) |  |  | Prazo de Carencia Pro Emprego |
| classe_de_vencimento_pro_emprego | `classe_pro_emprego` | integer(4) |  |  | Classe de Vencimento Pro Emprego |
| devolucao_fundo_social_ttd_409_410_411 | `devolucao_fundo_social_ttd_409_410_411` | numeric(13) |  |  | Valor Devolução Fundo Social - TTD 409, 410 ou 411 |
| ressarcimento_nas_vendas_com_subst_tribu | `ressarcimento_venda_subtri_outras_uf` | numeric(13) |  |  | Ressarcimento nas vendas com Subst. Tributária para outras UF - An. 3, Art. 25, RICMS |
| ressarcimento_de_icms_st_nas_vendas_para | `ressarcimento_icms_st_venda_simples_nacional` | numeric(13) |  |  | Ressarcimento de ICMS ST nas vendas para Simples Nacional - Decreto n° 3.509/10 |
| ressarcimento_icms_st_venda_outras_uf | `ressarcimento_icms_st_venda_outras_uf` | numeric(13) |  |  | Ressarcimento de ICMS ST nas vendas para outras UF - An. 3, Art. 25, RICMS |
| valor_devolucao_credito_presumido_materi | `devolucao_credito_presumido_material_reciclavel` | numeric(13) |  |  | Valor Devolução Crédito Presumido Material Reciclado |
| valor_credito_presumido_material_recicla | `credito_presumido_material_reciclavel` | numeric(13) |  |  | Valor Crédito Presumido Material Reciclado |
| credito_presumido_confeccao_an2_art_15_x | `credito_confeccao_produto` | numeric(13) |  |  | Crédito presumido confecção - An2, Art. 15, XXXIX |
| estorno_limite_do_credito_presumido_conf | `estorno_credito_confeccao_produto` | numeric(13) |  |  | Estorno limite do crédito presumido confecção - An2, Art. 15, XXXIX |
| devolucao_do_credito_presumido_confeccao | `devolucao_credito_confeccao_produto` | numeric(13) |  |  | Devolução do crédito presumido confecção - An2, Art. 15, XXXIX |
| creditos_de_pagamentos_devidos_por_ocasi | `creditos_pagamentos_devidos_por_fato_gerador` | numeric(13) |  |  | Créditos de pagamentos devidos por ocasião do Fato Gerador |
| credito_confeccao_produto_reducao_z | `credito_confeccao_produto_reducao_z` | numeric(13) |  |  | Crédito presumido confecção - An2. Art. 15, XXXIX - Redução Z |
| credito_confeccao_produto_demais_saidas | `credito_confeccao_produto_demais_saidas` | numeric(13) |  |  | Crédito presumido confecção - An2. Art. 15, XXXIX - Demais Saídas |
| credito_presumido_arroz_entradas_do_esta | `credito_presumido_arroz_entradas_estado` | numeric(13) |  |  | Crédito presumido arroz entradas do estado |
| credito_presumido_arroz_total_das_entrad | `credito_presumido_arroz_total_entradas` | numeric(13) |  |  | Crédito presumido arroz total das entradas |
| credito_presumido_arroz_proporcao_entrad | `credito_presumido_arroz_proporcao_entradas_estado` | numeric(13) |  |  | Crédito presumido arroz proporção entradas estado |
| base_calculo_credito_presumido_arroz | `credito_presumido_arroz_base_calculo_interestaduais` | numeric(13) |  |  | Base calculo crédito presumido arroz |
| percentual_credito_presumido_arroz | `credito_presumido_arroz_percentual` | numeric(13) |  |  | Percentual crédito presumido arroz |
| credito_presumido_nas_saidas_arroz_benef | `credito_presumido_arroz_valor` | numeric(13) |  |  | Crédito presumido nas saídas arroz beneficiado |
| devolucao_credito_presumido_nas_saidas_a | `credito_presumido_arroz_devolucao` | numeric(13) |  |  | Devolução crédito presumido nas saídas arroz beneficiado |
| credito_presumido_bares_restaurantes_e_s | `credito_presumido_bares_restaurantes` | numeric(13) |  |  | Crédito Presumido Bares, Restaurantes e Similares - An2, Art. 21, IV |
| estorno_de_icms_dos_optante_do_cred_pres | `estorno_credito_presumido_bares_restaurantes` | numeric(13) |  |  | Estorno de ICMS dos optante do Cred. Presumido Bares, Restaurantes e Similares, An2.Art. 21 |
| devolucao_de_credito_presumido_bares_res | `devolucao_credito_presumido_bares_restaurantes` | numeric(13) |  |  | Devolução de Crédito Presumido - Bares, Restaurantes e Similares, An2, Art.21, IV |
| credito_presumido_leite_saidas_tributada | `credito_presumido_leite_saidas_tributadas` | numeric(13) |  |  | Crédito presumido leite Saídas Tributadas |
| credito_presumido_leite_total_saidas | `credito_presumido_leite_total_saidas` | numeric(13) |  |  | Crédito presumido leite Total Saídas |
| credito_presumido_leite_proporcao_saidas | `credito_presumido_leite_proporcao_saidas_tributadas` | numeric(13) |  |  | Crédito presumido leite Proporção Saídas Tributadas |
| credito_presumido_leite_entradas | `credito_presumido_leite_entradas` | numeric(13) |  |  | Crédito presumido leite Entradas |
| credito_presumido_leite_valor_utilizado | `credito_presumido_leite_valor_utilizado` | numeric(13) |  |  | Crédito presumido leite Valor Utilizado |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in)

## efsdoimp_subtri_por_uf_es

**Saldo dos Impostos - Substituição Tributária Por ES** — tabela `EFSDOIMP_SUBTRI_POR_UF_ES` (61 linhas)

Saldo dos Impostos - Substituição Tributária Por ES. 61 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 61 linhas, 6 empresa(s), DATA_SIM de 2017-10-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| sigla_da_uf | `sigla_uf` | char(2) |  |  | Sigla da UF |
| recolhimento | `i_recolhimento` | integer(4) |  |  | Recolhimento |
| adicional_funcop_icms_st_saidas_internas | `adicional_funcop` | numeric(13) |  |  | Adicional FUNCOP - ICMS ST - Saídas Internas |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `sigla_da_uf` (eq/in), `recolhimento` (eq/in)

## efsdoimp_pis_cofins_reducao_linear_natureza

**Saldo do Impostos - PIS/COFINS Reducao Linear por natureza** — tabela `EFSDOIMP_PIS_COFINS_REDUCAO_LINEAR_NATUREZA` (60 linhas)

Saldo do Impostos - PIS/COFINS Reducao Linear por natureza. 60 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SCP, I_RECOLHIMENTO, FILIAL, CST, NATUREZA, ALIQUOTA, PERCENTUAL_LINEAR, OPERACAO, CODIGO_BENEFICIO_DIRBI.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SCP, I_RECOLHIMENTO, FILIAL, CST, NATUREZA, ALIQUOTA, PERCENTUAL_LINEAR, OPERACAO, CODIGO_BENEFICIO_DIRBI`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 60 linhas, 7 empresa(s), DATA_SIM de 2026-04-01 a 2026-09-01.
- operacao_a_acrescimo_r_reducao: todos os valores reais estão no comentário do banco (A=48, R=12).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |
| sequencial_do_recolhimento | `i_recolhimento` | integer(4) |  |  | Sequencial do Recolhimento |
| codigo_filial | `filial` | integer(4) |  |  | Código Filial |
| cst | `cst` | integer(4) |  |  | CST |
| natureza | `natureza` | integer(4) |  |  | Natureza |
| aliquota_do_imposto | `aliquota` | numeric(7) |  |  | Aliquota do Imposto |
| percentual_da_reducao_linear | `percentual_linear` | numeric(5) |  |  | Percentual da Reducao Linear |
| operacao_a_acrescimo_r_reducao | `operacao` | char(1) |  | efsdoimp_pis_cofins_reducao_linear_natureza_operacao_a_ | Operacao (A - Acrescimo / R - Reducao) |
| codigo_beneficio_dirbi | `codigo_beneficio_dirbi` | integer(4) |  |  | Codigo Beneficio DIRBI |
| base_de_calculo | `base_calculo` | numeric(13) |  |  | Base de Calculo |
| valor_do_imposto | `valor_imposto` | numeric(13) |  |  | Valor do Imposto |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `sequencial_do_scp` (eq/in), `sequencial_do_recolhimento` (eq/in), `codigo_filial` (eq/in), `cst` (eq/in), `natureza` (eq/in), `aliquota_do_imposto` (eq/in), `percentual_da_reducao_linear` (eq/in), `operacao_a_acrescimo_r_reducao` (eq/in), `codigo_beneficio_dirbi` (eq/in)

## efsdoimp_estadual_am

**Saldo dos Impostos - Estadual AM** — tabela `EFSDOIMP_ESTADUAL_AM` (56 linhas)

Saldo dos Impostos - Estadual AM. 56 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 56 linhas, 2 empresa(s), DATA_SIM de 2020-12-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| debito_recebido | `debito_recebido` | numeric(13) |  |  | Débito Recebido |
| credito_recebido | `credito_recebido` | numeric(13) |  |  | Crédito Recebido |
| debito_transferido | `debito_transferido` | numeric(13) |  |  | Débito Transferido |
| credito_transferido | `credito_transferido` | numeric(13) |  |  | Crédito Transferido |
| parcela_mensal_estimativa | `parcela_mensal_estimativa` | numeric(13) |  |  | Parcela Mensal Estimativa |
| saldo_a_transportar_estimativa | `saldo_a_transportar_estimativa` | numeric(13) |  |  | Saldo a Transportar Estimativa |
| saldo_anterior_estimativa | `saldo_anterior_estimativa` | numeric(13) |  |  | Saldo Anterior Estimativa |
| credito_presumido_de_20_para_transportad | `credito_presumido_20_transportadoras_icms` | numeric(13) |  |  | Crédito presumido de 20% para transportadoras - Art. 20, V do RICMS/AM |
| base_credito_presumido_de_20_para_transp | `base_credito_presumido_20_transportadoras_icms` | numeric(13) |  |  | Base Crédito presumido de 20% para transportadoras - Art. 20, V do RICMS/AM |
| credito_ativo_imobilizado | `credito_ativo_imobilizado` | numeric(13) |  |  | Crédito Ativo Imobilizado |
| estorno_de_debito_nas_operacoes_com_ct_e | `estorno_debito_operacoes_cte_substituto` | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in)

## efsdoimp_pis_cofins_reducao_linear_filial

**Saldo do Impostos - PIS/COFINS Reducao Linear por filial** — tabela `EFSDOIMP_PIS_COFINS_REDUCAO_LINEAR_FILIAL` (56 linhas)

Saldo do Impostos - PIS/COFINS Reducao Linear por filial. 56 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SCP, I_RECOLHIMENTO, FILIAL, CST, ALIQUOTA, PERCENTUAL_LINEAR, OPERACAO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SCP, I_RECOLHIMENTO, FILIAL, CST, ALIQUOTA, PERCENTUAL_LINEAR, OPERACAO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 56 linhas, 7 empresa(s), DATA_SIM de 2026-04-01 a 2026-09-01.
- operacao_a_acrescimo_r_reducao: todos os valores reais estão no comentário do banco (A=44, R=12).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |
| sequencial_do_recolhimento | `i_recolhimento` | integer(4) |  |  | Sequencial do Recolhimento |
| codigo_filial | `filial` | integer(4) |  |  | Código Filial |
| cst | `cst` | integer(4) |  |  | CST |
| aliquota_do_imposto | `aliquota` | numeric(7) |  |  | Aliquota do Imposto |
| percentual_da_reducao_linear | `percentual_linear` | numeric(5) |  |  | Percentual da Reducao Linear |
| operacao_a_acrescimo_r_reducao | `operacao` | char(1) |  | efsdoimp_pis_cofins_reducao_linear_filial_operacao_a_ | Operacao (A - Acrescimo / R - Reducao) |
| base_de_calculo | `base_calculo` | numeric(13) |  |  | Base de Calculo |
| valor_do_imposto | `valor_imposto` | numeric(13) |  |  | Valor do Imposto |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `sequencial_do_scp` (eq/in), `sequencial_do_recolhimento` (eq/in), `codigo_filial` (eq/in), `cst` (eq/in), `aliquota_do_imposto` (eq/in), `percentual_da_reducao_linear` (eq/in), `operacao_a_acrescimo_r_reducao` (eq/in)

## efsdoimp_estadual_mt

**Saldo dos Impostos - Estadual MT** — tabela `EFSDOIMP_ESTADUAL_MT` (49 linhas)

Saldo dos Impostos - Estadual MT. 49 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 49 linhas, 3 empresa(s), DATA_SIM de 2018-01-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| valor_devolucao_do_credito_presumido_pro | `devolucao_credito_presumido_prodeic` | numeric(13) |  |  | Valor Devolução do Crédito Presumido PRODEIC |
| valor_credito_presumido_transporte | `credito_presumido_transporte` | numeric(13) |  |  | Valor Crédito Presumido Transporte |
| valor_credito_presumido_prodeic | `credito_presumido_prodeic` | numeric(13) |  |  | Valor Crédito Presumido PRODEIC |
| valor_credito_presumido_algodao | `credito_presumido_algodao` | numeric(13) |  |  | VAlor Crédito Presumido Algodão |
| valor_devolucao_do_credito_presumido_alg | `devolucao_credito_presumido_algodao` | numeric(13) |  |  | Valor Devolução do Crédito Presumido Algodão |
| valor_estorno_credito_presumido_algod_ap | `estorno_credito_presumido_algodao` | numeric(13) |  |  | Valor Estorno Crédito Presumido Algod]ap |
| valor_estorno_credito_presumido_transpor | `estorno_credito_presumido_transporte` | numeric(13) |  |  | Valor Estorno Crédito Presumido Transporte |
| estorno_credito_presumido_prodeic | `estorno_credito_presumido_prodeic` | numeric(13) |  |  | Estorno Crédito Presumido PRODEIC |
| credito_presumido_prodeic_parte_01 | `credito_presumido_prodeic_parte_01` | numeric(13) |  |  | Valor Crédito Presumido PRODEIC - Parte 01 |
| credito_presumido_prodeic_parte_02 | `credito_presumido_prodeic_parte_02` | numeric(13) |  |  | Valor Crédito Presumido PRODEIC - Parte 02 |
| credito_presumido_prodeic_parte_03 | `credito_presumido_prodeic_parte_03` | numeric(13) |  |  | Valor Crédito Presumido PRODEIC - Parte 03 |
| creditos_de_pagamentos_devidos_por_ocasi | `credito_pagamentos_fator_gerador` | numeric(13) |  |  | Créditos de pagamentos devidos por ocasião do Fato Gerador |
| credito_icms_estimativa_simplificado | `credito_icms_estimativa_simplificado` | numeric(13) |  |  | Crédito ICMS Estimativa Simplificado |
| ajuste_referente_reducao_da_base_de_calc | `ajuste_base_calculo_icms_prodeic` | numeric(13) |  |  | Ajuste referente redução da base de cálculo do ICMS - PRODEIC |
| valor_debito_fecep_icms | `debito_fecep_icms` | numeric(13) |  |  | Valor débito FECEP ICMS |
| credito_outorgado_estabelecimento_comerc | `credito_outorgado_estab_comer_varejista` | numeric(13) |  |  | Crédito outorgado estabelecimento comercial varejista - Art. 2º, I, An. XVII, RICMS |
| credito_sobre_estoque_operacao_de_entrad | `credito_sobre_estoque_operacao_de_entrada` | numeric(13) |  |  | Crédito sobre estoque operação de entrada - Art.8º, §2º, An.XVII do RICMS |
| credito_sobre_estoque_icms_efetivamente | `credito_sobre_estoque_icms_efetivamente_pago` | numeric(13) |  |  | Crédito sobre estoque ICMS efetivamente pago - Art.8º, §3º, An.XVII do RICMS |
| estab_comercial_atacadista_saidas_intern | `credito_outorgado_estab_comer_atac_saidas_internas` | numeric(13) |  |  | Estab. comercial atacadista - Saídas internas - Art. 2°, II, a, An. XVII, RICMS |
| estab_comercial_atacadista_saidas_intere | `credito_outorgado_estab_comer_atac_saidas_interestaduais` | numeric(13) |  |  | Estab. comercial atacadista - Saídas interest. - Art. 2°, II, b, An. XVII, RICMS |
| devolucao_cred_outorgado_saidas_internas | `estorno_credito_outorgado_estab_comer_atac_saidas_internas` | numeric(13) |  |  | Devolução créd. outorgado saídas internas - Art. 2°, II, a, An. XVII, RICMS |
| devolucao_cred_outorgado_saidas_interest | `estorno_credito_outorgado_estab_comer_atac_saidas_interestaduais` | numeric(13) |  |  | Devolução créd. outorgado saídas interest. - Art. 2°, II, b, An. XVII, RICMS |
| estorno_cred_excedente_7_nas_entradas_ar | `estorno_credito_outorgado_estab_comer_atac_entradas` | numeric(13) |  |  | Estorno créd. excedente 7% nas entradas - Art. 2°, §2º, I, An. XVII, RICMS |
| limite_do_credito_outorgado | `limite_credito_outorgado` | numeric(13) |  |  | Limite do crédito outorgado |
| estorno_de_debito_regime_simplificado_de | `estorno_debito_regime_simplificado_tributacao_restaurantes_bares` | numeric(13) |  |  | Estorno de Debito Regime simplificado de tributação - Art. 1o, Anexo XVIII do RICMS |
| credito_out_prodeic_credito_escriturado | `credito_out_prodeic_credito_escriturado` | numeric(13) |  |  | Crédito Out Prodeic - Crédito Escriturado |
| credito_out_prodeic_total_saidas | `credito_out_prodeic_total_saidas` | numeric(13) |  |  | Crédito Out Prodeic - Total Saídas |
| credito_out_prodeic_debitos_operacoes_in | `credito_out_prodeic_debitos_op_internas` | numeric(13) |  |  | Crédito Out Prodeic - Débitos Operações Internas |
| credito_out_prodeic_debitos_op_interesta | `credito_out_prodeic_debitos_op_interestaduais` | numeric(13) |  |  | Crédito Out Prodeic - Débitos Operações Interestaduais |
| credito_out_prodeic_estorno_cedito_perio | `credito_out_prodeic_estorno_cred_periodo_anterior_internas` | numeric(13) |  |  | Crédito Out Prodeic - Estorno Cédito Período Anterior Operações Internas |
| credito_out_prodeic_estorno_cred_periodo | `credito_out_prodeic_estorno_cred_periodo_anterior_interestaduais` | numeric(13) |  |  | Crédito Out Prodeic - Estorno Cédito Período Anterior Operações Interestaduais |
| credito_out_prodeic_estorno_cedito_para | `credito_out_prodeic_estorno_cred_periodo_seguinte_internas` | numeric(13) |  |  | Crédito Out Prodeic - Estorno Cédito para o Período Seguinte Operações Internas |
| credito_out_prodeic_estorno_cred_periodo_c | `credito_out_prodeic_estorno_cred_periodo_seguinte_interestaduais` | numeric(13) |  |  | Crédito Out Prodeic - Estorno Cédito para o Período Seguinte Operações Interestaduais |
| credito_out_prodeic_percentual_de_propor | `credito_out_prodeic_perc_proporcao_op_internas` | numeric(5) |  |  | Crédito Out Prodeic - Percentual de Proporção para Op. Internas relativo as Saídas |
| credito_out_prodeic_perc_proporcao_op_in | `credito_out_prodeic_perc_proporcao_op_interestaduais` | numeric(5) |  |  | Crédito Out Prodeic - Percentual de Proporção para Op. Interestaduais relativo as Saídas |
| credito_out_prodeic_perc_proporcao_demai | `credito_out_prodeic_perc_proporcao_demais_produtos` | numeric(5) |  |  | Crédito Out Prodeic - Percentual de Proporção para Demais Produtos relativo as Saídas |
| credito_out_prodeic_perc_proporcao_op_is | `credito_out_prodeic_perc_proporcao_op_isentas` | numeric(5) |  |  | Crédito Out Prodeic - Percentual de Proporção para Op. Isentas relativo as Saídas |
| credito_out_prodeic_perc_proporcao_op_ex | `credito_out_prodeic_perc_proporcao_op_exportacao` | numeric(5) |  |  | Crédito Out Prodeic - Percentual de Proporção para Op. Exportação relativo as Saídas |
| credito_out_prodeic_credito_proporcional | `credito_out_prodeic_cred_proporcional_op_internas` | numeric(13) |  |  | Crédito Out Prodeic - Crédito Proporcional Op. Internas |
| credito_out_prodeic_cred_proporcional_op | `credito_out_prodeic_cred_proporcional_op_interestaduais` | numeric(13) |  |  | Crédito Out Prodeic - Crédito Proporcional Op. Interestaduais |
| credito_out_prodeic_cred_proporcional_de | `credito_out_prodeic_cred_proporcional_demais_produtos` | numeric(13) |  |  | Crédito Out Prodeic - Crédito Proporcional Demais Produtos |
| credito_out_prodeic_cred_proporcional_op_c | `credito_out_prodeic_cred_proporcional_op_isentas` | numeric(13) |  |  | Crédito Out Prodeic - Crédito Proporcional Op. Isentas |
| credito_out_prodeic_cred_proporcional_op_c_c | `credito_out_prodeic_cred_proporcional_op_exportacao` | numeric(13) |  |  | Crédito Out Prodeic - Crédito Proporcional Op. Exportação |
| credito_out_prodeic_credito_outorgado_na | `credito_out_prodeic_credito_outorgado_op_internas` | numeric(13) |  |  | Crédito Out Prodeic - Crédito Outorgado nas Op. Internas |
| credito_out_prodeic_credito_outorgado_op | `credito_out_prodeic_credito_outorgado_op_interestaduais` | numeric(13) |  |  | Crédito Out Prodeic - Crédito Outorgado nas Op. Interestaduais |
| credito_out_prodeic_estorno_credito_op_i | `credito_out_prodeic_estorno_cred_op_isentas` | numeric(13) |  |  | Crédito Out Prodeic - Estorno Crédito Op. Isentas |
| credito_out_prodeic_estorno_debitos_do_s | `credito_out_prodeic_estorno_debitos_saldo_credor` | numeric(13) |  |  | Crédito Out Prodeic - Estorno Débitos do Saldo Credor |
| estorno_de_debito_nas_operacoes_com_ct_e | `estorno_debito_operacoes_cte_substituto` | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |
| estorno_de_debito_de_icms_de_devolucao_c | `estorno_debito_icms_devolucao_entrada_sem_aproveitamento` | numeric(13) |  |  | Estorno de débito de ICMS de devolução, cuja entrada ocorreu sem o aproveitamento |
| estorno_debito_icms_devolucao_entrada_se | `estorno_debito_icms_devolucao_ativo_imob_uso_consumo` | numeric(13) |  |  | Estorno débito ICMS devolução, entrada sem aproveitamento-Ativo Imob/Uso e Consumo |
| credito_na_aquisicao_de_combustiveis_par | `credito_aquisicao_combustivel_insumo` | numeric(13) |  |  | Crédito na aquisição de combustíveis para insumo - Conv. ICMS nº 199/22 e 26/23 |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in)

## efsdoimp_por_uf_rj

**Saldo dos Impostos - Por UF - RJ** — tabela `EFSDOIMP_POR_UF_RJ` (39 linhas)

Saldo dos Impostos - Por UF - RJ. 39 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 39 linhas, 5 empresa(s), DATA_SIM de 2019-04-01 a 2025-10-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| sigla_da_uf | `sigla_uf` | char(2) |  |  | Sigla da UF |
| outros_debitos | `outros_debitos_lancado` | numeric(15) |  |  | Outros débitos |
| outros_creditos | `outros_creditos_lancado` | numeric(15) |  |  | Outros créditos |
| estorno_de_debitos | `estorno_debitos_lancado` | numeric(15) |  |  | Estorno de débitos |
| estorno_de_creditos | `estorno_creditos_lancado` | numeric(15) |  |  | Estorno de créditos |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `sigla_da_uf` (eq/in)

## efsdoimp_mg_sub_apuracao

**Saldo dos Impostos - Sub Apuração MG** — tabela `EFSDOIMP_MG_SUB_APURACAO` (34 linhas)

Saldo dos Impostos - Sub Apuração MG. 34 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SUB_APURACAO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SUB_APURACAO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_VENCIMENTO`
- **Ordem padrão:** `DATA_VENCIMENTO desc`, `CODI_IMP asc`, `DATA_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 34 linhas, 1 empresa(s), DATA_VENCIMENTO de 2025-06-08 a 2026-10-20.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| sequencial_sub_apuracao | `i_sub_apuracao` | integer(4) |  |  | Sequencial sub apuração |
| valor_contabil_saida | `valor_contabil_saida` | numeric(13) |  |  | Valor contábil saída |
| base_de_calculo_saidas | `base_calculo_saida` | numeric(13) |  |  | Base de cálculo saídas |
| valor_saidas | `valor_saida` | numeric(13) |  |  | Valor saídas |
| base_de_calculo_entradas_proporcao | `base_calculo_entrada_proporcao` | numeric(13) |  |  | Base de cálculo entradas - Proporção |
| proporcao_acabados | `proporcao_acabado` | numeric(5) |  |  | Proporção acabados |
| valor_entradas_proporcao | `valor_entrada_proporcao` | numeric(13) |  |  | Valor entradas - Proporção |
| valor_contabil_entrada | `valor_contabil_entrada` | numeric(13) |  |  | Valor contábil entrada |
| base_de_calculo_entrada | `base_calculo_entrada` | numeric(13) |  |  | Base de cálculo entrada |
| valor_entradas | `valor_entrada` | numeric(13) |  |  | Valor entradas |
| valor_devolucao | `valor_devolucao` | numeric(13) |  |  | Valor devolução |
| valor_credito_estorno | `valor_credito_estorno` | numeric(13) |  |  | Valor crédito estorno |
| valor_total_do_recolhimento_efetivo_pela | `valor_recolhimento_efetivo_saida` | numeric(13) |  |  | Valor total do recolhimento efetivo pelas saídas |
| valor_credito_presumido | `valor_credito_presumido` | numeric(13) |  |  | Valor crédito presumido |
| saldo_a_recolher | `saldo_recolher` | numeric(13) |  |  | Saldo a recolher |
| saldo_credor | `saldo_credor` | numeric(13) |  |  | Saldo credor |
| saldo_credor_anterior | `saldo_credor_anterior` | numeric(13) |  |  | Saldo credor anterior |
| parcela | `parcela` | integer(4) |  |  | Parcela |
| valor_pago | `valor_pago` | numeric(13) |  |  | Valor pago |
| data_vencimento | `data_vencimento` | date(4) |  |  | Data vencimento |
| valor_do_estorno_do_credito_estorno_devo | `valor_estorno_credito_estorno` | numeric(13) |  |  | Valor do estorno do crédito estorno (Devolução da compra) |
| outros_debitos | `outros_debitos` | numeric(13) |  |  | Outros débitos |
| estorno_creditos | `estorno_creditos` | numeric(13) |  |  | Estorno créditos |
| outros_creditos | `outros_creditos` | numeric(13) |  |  | Outros créditos |
| estorno_debitos | `estorno_debitos` | numeric(13) |  |  | Estorno débitos |
| desconto_conforme_termo_de_aceite_da_lei | `desconto_conforme_termo_aceite_lei_22549_17` | numeric(13) |  |  | Desconto conforme Termo de Aceite da Lei 22.549/17 e Decreto 47.226/17 |
| saldo_devedor | `saldo_devedor` | numeric(13) |  |  | Saldo Devedor |
| estorno_do_fem_de_mercadorias_alcancadas | `estorno_fem_mercadorias_credito_presumido` | numeric(13) |  |  | Estorno do FEM de mercadorias alcançadas pelo crédito presumido |
| valor_contabil_reducao_z | `valor_contabil_reducao_z` | numeric(13) |  |  | Valor Contábil Redução Z |
| base_de_calculo_reducao_z | `base_calculo_reducao_z` | numeric(13) |  |  | base de Cálculo Redução Z |
| valor_reducao_z | `valor_reducao_z` | numeric(13) |  |  | Valor Redução Z |
| estorno_fem_mercadorias_credito_presumid | `estorno_fem_mercadorias_credito_presumido_saidas` | numeric(13) |  |  | Estorno do FEM de mercadorias alcançadas pelo crédito presumido - Saídas |
| estorno_fem_mercadorias_credito_presumid_c | `estorno_fem_mercadorias_credito_presumido_reducao_z` | numeric(13) |  |  | Estorno do FEM de mercadorias alcançadas pelo crédito presumido - Redução Z |
| estorno_do_fem_de_mercadorias_devolvidas | `estorno_fem_mercadorias_credito_presumido_devolucao` | numeric(13) |  |  | Estorno do FEM de mercadorias devolvidas alcançadas pelo crédito presumido |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `sequencial_sub_apuracao` (eq/in), `data_vencimento` (entre/gte/lte)

## efsdoimp_mg_sub_apuracao_incentivo_ret

**Saldo dos Impostos - Sub Apuração MG - Incentivo RET** — tabela `EFSDOIMP_MG_SUB_APURACAO_INCENTIVO_RET` (34 linhas)

Saldo dos Impostos - Sub Apuração MG - Incentivo RET. 34 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SUB_APURACAO, I_SUB_APURACAO_CONSULTA_APURACAO, I_SEQUENCIAL_INCENTIVO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SUB_APURACAO, I_SUB_APURACAO_CONSULTA_APURACAO, I_SEQUENCIAL_INCENTIVO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 34 linhas, 1 empresa(s), DATA_SIM de 2025-05-01 a 2026-09-01.
- sequencial_sub_apuracao_0_apuracao_norma: todos os valores reais estão no comentário do banco (0=17, 1=17).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| sequencial_sub_apuracao | `i_sub_apuracao` | integer(4) |  |  | Sequencial sub apuração |
| sequencial_sub_apuracao_0_apuracao_norma | `i_sub_apuracao_consulta_apuracao` | integer(4) |  | efsdoimp_mg_sub_apuracao_incentivo_ret_sequencial_ | Sequencial sub apuração (0-Apuração normal/1-N-sub apuração) |
| sequencial_incentivo | `i_sequencial_incentivo` | integer(4) |  |  | Sequencial incentivo |
| e_pta_re_no | `e_pta_re` | char(15) |  |  | E-PTA-RE nº |
| credito_da_devolucao_de_merc_com_credito | `credito_devolucao_mercadoria_cred_pres_ret` | numeric(13) |  |  | Crédito da devolução de merc. com crédito presumido - RET e-PTA |
| credito_vinculado_a_ope_alcancada_pelo_c | `credito_vinculado_op_alcancada_cred_pres_norm_ret` | numeric(13) |  |  | Crédito vinculado à ope. alcançada pelo crédito presumido - RET e-PTA (Cálculo normal) |
| estorno_ref_devolucao_de_merc_com_credit | `estorno_devolucao_mercadoria_alcancada_cred_pres_ret` | numeric(13) |  |  | Estorno ref. devolução de merc. com crédito presumido - RET e-PTA |
| credito_presumido_ret_e_pta | `credito_presumido_ret` | numeric(13) |  |  | Crédito presumido - RET e-PTA |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `sequencial_sub_apuracao` (eq/in), `sequencial_sub_apuracao_0_apuracao_norma` (eq/in), `sequencial_incentivo` (eq/in), `e_pta_re_no` (eq/in)

## efsdoimp_estadual_df

**Saldo dos Impostos - Estadual DF** — tabela `EFSDOIMP_ESTADUAL_DF` (28 linhas)

Saldo dos Impostos - Estadual DF. 28 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 28 linhas, 2 empresa(s), DATA_SIM de 2017-10-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| credito_presumido_de_20_para_transportad | `credito_presumido_transporte` | numeric(13) |  |  | Crédito presumido de 20% para  transportadoras - Item 2,  Anexo I do RICMS |
| lei_5005_total_vendas_internas | `lei_5005_total_vendas_internas` | numeric(13) |  |  | Lei 5005 - Total Vendas Internas |
| lei_5005_total_vendas_interestaduais | `lei_5005_total_vendas_interestaduais` | numeric(13) |  |  | Lei 5005 - Total Vendas Interestaduais |
| lei_5005_proporcao_vendas_internas | `lei_5005_proporcao_vendas_internas` | numeric(7) |  |  | Lei 5005 - Proporção Vendas Internas |
| lei_5005_proporcao_vendas_interestaduais | `lei_5005_proporcao_vendas_interestaduais` | numeric(7) |  |  | Lei 5005 - Proporção Vendas Interestaduais |
| lei_5005_estorno_entradas | `lei_5005_estorno_entradas` | numeric(13) |  |  | Lei 5005 - Estorno Entradas |
| lei_5005_estorno_devolucao_vendas | `lei_5005_estorno_devolucao_vendas` | numeric(13) |  |  | Lei 5005 - Estorno Devolução Vendas |
| lei_5005_base_calculo_compras_internas | `lei_5005_base_calculo_compras_internas` | numeric(13) |  |  | Lei 5005 - Base Cálculo Compras Internas |
| lei_5005_base_calculo_compras_interestad | `lei_5005_base_calculo_compras_interestaduais` | numeric(13) |  |  | Lei 5005 - Base Cálculo Compras Interestaduais |
| lei_5005_base_calculo_devolucao_vendas | `lei_5005_base_calculo_devolucao_vendas` | numeric(13) |  |  | Lei 5005 - Base Cálculo Devolução Vendas |
| lei_5005_credito_compras_internas | `lei_5005_credito_compras_internas` | numeric(13) |  |  | Lei 5005 - Crédito Compras Internas |
| lei_5005_credito_compras_interestaduais | `lei_5005_credito_compras_interestaduais` | numeric(13) |  |  | Lei 5005 - Crédito Compras Interestaduais |
| lei_5005_credito_devolucao_vendas | `lei_5005_credito_devolucao_vendas` | numeric(13) |  |  | Lei 5005 - Crédito Devolução Vendas |
| lei_5005_estorno_saidas_icms | `lei_5005_estorno_saidas_icms` | numeric(13) |  |  | Lei 5005 - Estorno Saídas ICMS |
| lei_5005_estorno_saidas_fecop | `lei_5005_estorno_saidas_fecop` | numeric(13) |  |  | Lei 5005 - Estorno Saídas FECOP |
| lei_5005_estorno_devolucao_compras | `lei_5005_estorno_devolucao_compras` | numeric(13) |  |  | Lei 5005 - Estorno Devolução Compras |
| lei_5005_base_calculo_vendas | `lei_5005_base_calculo_vendas` | numeric(13) |  |  | Lei 5005 - Base Cálculo Vendas |
| lei_5005_base_calculo_devolucao_compras | `lei_5005_base_calculo_devolucao_compras_internas` | numeric(13) |  |  | Lei 5005 - Base Cálculo Devolução Compras Internas |
| lei_5005_base_calculo_devolucao_compras_c | `lei_5005_base_calculo_devolucao_compras_interestaduais` | numeric(13) |  |  | Lei 5005 - Base Cálculo Devolução Compras Interestaduais |
| lei_5005_debito_vendas | `lei_5005_debito_vendas` | numeric(13) |  |  | Lei 5005 - Débito Vendas |
| lei_5005_debito_devolucao_compras_intern | `lei_5005_debito_devolucao_compras_internas` | numeric(13) |  |  | Lei 5005 - Débito Devolução Compras Internas |
| lei_5005_debito_devolucao_compras_intere | `lei_5005_debito_devolucao_compras_interestaduais` | numeric(13) |  |  | Lei 5005 - Débito Devolução Compras Interestaduais |
| lei_5005_estorno_de_debito_para_ajustar | `lei_5005_estorno_debito_para_ajustar_valor_icms` | numeric(13) |  |  | Lei 5005 - Estorno de débito para ajustar o valor do ICMS próprio a recolher ao valor efetivamente recolhido no mês |
| lei_5005_outros_debitos_para_ajustar_o_v | `lei_5005_outros_debitos_para_ajustar_valor_icms` | numeric(13) |  |  | Lei 5005 - Outros débitos para ajustar o valor do ICMS próprio a recolher ao valor efetivamente recolhido no mês |
| lei_5005_cancelamento_do_estorno_de_debi | `lei_5005_canc_estorno_deb_para_ajustar_valor_icms` | numeric(13) |  |  | Lei 5005 - Cancelamento do estorno de débito realizado para ajustar o valor do ICMS a recolher ao valor efetivamente recolhido no mês |
| lei_5005_cancelamento_do_lancamento_de_o | `lei_5005_canc_outros_deb_para_ajustar_valor_icms` | numeric(13) |  |  | Lei 5005 - Cancelamento do lançamento de outros débitos realizado para ajustar o valor do ICMS a recolher ao valor efetivamente recolhido no mês |
| lei_5005_base_calculo_devolucao_vendas_i | `lei_5005_base_calculo_devolucao_vendas_internas` | numeric(13) |  |  | Lei 5005 - Base Cálculo Devolução Vendas Internas |
| lei_5005_base_calculo_devolucao_vendas_i_c | `lei_5005_base_calculo_devolucao_vendas_interestaduais` | numeric(13) |  |  | Lei 5005 - Base Cálculo Devolução Vendas Interestaduais |
| lei_5005_credito_devolucao_vendas_intern | `lei_5005_credito_devolucao_vendas_internas` | numeric(13) |  |  | Lei 5005 - Crédito Devolução Vendas Internas |
| lei_5005_credito_devolucao_vendas_intere | `lei_5005_credito_devolucao_vendas_interestaduais` | numeric(13) |  |  | Lei 5005 - Crédito Devolução Vendas Interestaduais |
| lei_5005_base_de_calculo_vendas_internas | `lei_5005_base_calculo_vendas_interna` | numeric(13) |  |  | Lei 5005 - Base de cálculo vendas internas |
| lei_5005_base_de_calculo_vendas_interest | `lei_5005_base_calculo_vendas_interestadual` | numeric(13) |  |  | Lei 5005 - Base de cálculo vendas interestaduais |
| lei_5005_debito_vendas_internas | `lei_5005_debito_vendas_interna` | numeric(13) |  |  | Lei 5005 - Débito vendas internas |
| lei_5005_debito_vendas_interestaduais | `lei_5005_debito_vendas_interestadual` | numeric(13) |  |  | Lei 5005 - Débito vendas interestaduais |
| lei_5005_total_vendas_internas_bebidas_a | `lei_5005_total_vendas_internas_bebidas_alcoolicas` | numeric(13) |  |  | Lei 5005 - Total Vendas Internas Bebidas Alcoólicas |
| lei_5005_total_vendas_interestaduais_ent | `lei_5005_total_vendas_interestaduais_12` | numeric(13) |  |  | Lei 5005 - Total Vendas Interestaduais Entrada Igual 12% |
| lei_5005_total_vendas_interestaduais_dif | `lei_5005_total_vendas_interestaduais_diferente_12` | numeric(13) |  |  | Lei 5005 - Total Vendas Interestaduais Entrada Diferente 12% |
| lei_5005_proporcao_vendas_internas_bebid | `lei_5005_proporcao_vendas_internas_bebidas_alcoolicas` | numeric(7) |  |  | Lei 5005 - Proporção Vendas Internas Bebidas Alcoólicas |
| lei_5005_proporcao_vendas_interestaduais_c | `lei_5005_proporcao_vendas_interestaduais_12` | numeric(7) |  |  | Lei 5005 - Proporção Vendas Internas Bebidas Entrada Igual 12% |
| lei_5005_proporcao_vendas_interestaduais_c_c | `lei_5005_proporcao_vendas_interestaduais_diferente_12` | numeric(7) |  |  | Lei 5005 - Proporção Vendas Internas Bebidas Entrada Diferente 12% |
| lei_5005_base_calculo_compras_internas_b | `lei_5005_base_calculo_compras_internas_bebidas_alcoolicas` | numeric(13) |  |  | Lei 5005 - Base Cálculo Compras Internas Bebidas Alcoólicas |
| lei_5005_base_calculo_compras_internas_e | `lei_5005_base_calculo_compras_interestaduais_12` | numeric(13) |  |  | Lei 5005 - Base Cálculo Compras Internas Entrada Igual 12% |
| lei_5005_base_calculo_compras_interestad_c | `lei_5005_base_calculo_compras_interestaduais_diferente_12` | numeric(13) |  |  | Lei 5005 - Base Cálculo Compras Internas Entrada Diferente 12% |
| lei_5005_credito_compras_internas_bebida | `lei_5005_credito_compras_internas_bebidas_alcoolicas` | numeric(13) |  |  | Lei 5005 - Crédito Compras Internas Bebidas Alcoólicas |
| lei_5005_credito_compras_internas_entrad | `lei_5005_credito_compras_interestaduais_12` | numeric(13) |  |  | Lei 5005 - Crédito Compras Internas Entrada Igual 12% |
| lei_5005_credito_compras_interestaduais_c | `lei_5005_credito_compras_interestaduais_diferente_12` | numeric(13) |  |  | Lei 5005 - Crédito Compras Internas Entrada Diferente 12% |
| lei_5005_base_calculo_vendas_internas_be | `lei_5005_base_calculo_vendas_internas_bebidas_alcoolicas` | numeric(13) |  |  | Lei 5005 - Base Cálculo Vendas Internas Bebidas Alcoólicas |
| lei_5005_base_calculo_vendas_internas_en | `lei_5005_base_calculo_vendas_interestadual_12` | numeric(13) |  |  | Lei 5005 - Base Cálculo Vendas Internas Entrada Igual 12% |
| lei_5005_base_calculo_vendas_interestadu | `lei_5005_base_calculo_vendas_interestadual_diferente_12` | numeric(13) |  |  | Lei 5005 - Base Cálculo Vendas Internas Entrada Diferente 12% |
| lei_5005_debito_vendas_internas_bebidas | `lei_5005_debito_vendas_internas_bebidas_alcoolicas` | numeric(13) |  |  | Lei 5005 - Débito Vendas Internas Bebidas Alcoólicas |
| lei_5005_debito_vendas_interestadual_12 | `lei_5005_debito_vendas_interestadual_12` | numeric(13) |  |  | Lei 5005 - Débito Vendas Internas Bebidas Entrada Igual 12% |
| lei_5005_debito_vendas_interestadual_dif | `lei_5005_debito_vendas_interestadual_diferente_12` | numeric(13) |  |  | Lei 5005 - Débito Vendas Internas Bebidas Entrada Diferente 12% |
| lei_5005_base_calculo_devolucao_compras_c_c | `lei_5005_base_calculo_devolucao_compras_internas_bebidas_alcoolicas` | numeric(13) |  |  | Lei 5005 - Base Cálculo Devolução Compras Internas Bebidas Alcoólicas |
| lei_5005_base_calculo_devolucao_compras_c_c_c | `lei_5005_base_calculo_devolucao_compras_interestaduais_12` | numeric(13) |  |  | Lei 5005 - Base Cálculo Devolução Compras Internas Entrada Igual 12% |
| lei_5005_base_calculo_devolucao_compras_c_c_c_c | `lei_5005_base_calculo_devolucao_compras_interestaduais_diferente_12` | numeric(13) |  |  | Lei 5005 - Base Cálculo Devolução Compras Internas Entrada Diferente 12% |
| lei_5005_debito_devolucao_compras_intern_c | `lei_5005_debito_devolucao_compras_internas_bebidas_alcoolicas` | numeric(13) |  |  | Lei 5005 - Débito Devolução Compras Internas Bebidas Alcoólicas |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in)

## efsdoimp_subtri_por_uf_df

**Saldo dos Impostos - Substituição Tributária Por DF** — tabela `EFSDOIMP_SUBTRI_POR_UF_DF` (28 linhas)

Saldo dos Impostos - Substituição Tributária Por DF. 28 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 28 linhas, 2 empresa(s), DATA_SIM de 2017-10-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| sigla_da_uf | `sigla_uf` | char(2) |  |  | Sigla da UF |
| recolhimento | `i_recolhimento` | integer(4) |  |  | Recolhimento |
| debito_icms_sobre_estoque | `debito_icms_sobre_estoque` | numeric(13) |  |  | Debito ICMS Sobre Estoque |
| reducao_debito_fecop | `reducao_debito_fecop` | numeric(13) |  |  | Redução Debito FECOP |
| fecop_st_sobre_devolucao_de_vendas_inter | `fecop_st_devolucao_vendas_internas` | numeric(13) |  |  | FECOP ST sobre devolução de vendas internas |
| reducao_de_creditos_fundo_de_combate_a_p | `reducao_credito_fecop` | numeric(13) |  |  | Redução de créditos - Fundo de combate a pobreza |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `sigla_da_uf` (eq/in), `recolhimento` (eq/in)

## efsdoimp_estadual_rn

**Saldo dos Impostos - Estadual RN** — tabela `EFSDOIMP_ESTADUAL_RN` (23 linhas)

Saldo dos Impostos - Estadual RN. 23 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 23 linhas, 1 empresa(s), DATA_SIM de 2018-01-01 a 2019-11-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| credito_de_icms_conforme_aliquota_do_sim | `credito_conforme_aliquota_sn` | numeric(13) |  |  | Crédito de ICMS conforme alíquota do Simples Nacional - Art. 23, LC 123/06 |
| credito_presumido_na_aquisicao_de_indust | `credito_aquisicao_industria_sn` | numeric(13) |  |  | Crédito Presumido na aquisição de Indústrias Simples Nacional - Art. 112, XXIII, RICMS |
| devolucao_credito_de_icms_conforme_aliqu | `devolucao_conforme_aliquota_sn` | numeric(13) |  |  | Devolução Crédito de ICMS conforme alíquota do Simples Nacional - Art. 23, LC 123/06 |
| devolucao_credito_presumido_na_aquisicao | `devolucao_aquisicao_industria_sn` | numeric(13) |  |  | Devolução Crédito Presumido na aquisição de Indústrias Simples Nacional - Art. 112, XXIII, RICMS |
| devolucao_de_mercadoria_adquirida_de_sim | `devolucao_mercadoria_adquirida_sn` | numeric(13) |  |  | Devolução de mercadoria adquirida de Simples Nacional |
| estorno_de_debito_devolucao_simples_naci | `estorno_debito_devolucao_simples_nacional` | numeric(13) |  |  | Estorno de Débito Devolução Simples Nacional |
| estorno_icms_st_transportes | `estorno_icms_st_transporte` | numeric(13) |  |  | Estorno ICMS ST Transportes |
| credito_presumido_de_20_para_transportad | `credito_presumido_20_transportadoras_icms` | numeric(13) |  |  | Crédito presumido de 20 para transportadoras |
| regime_atacadista_saidas_interestaduais | `regime_atacadista_saidas_interestaduais_art_16b_i_base_calculo` | numeric(13) |  |  | Regime Atacadista - Saídas interestaduais, Art. 16-B, I - Base de cálculo |
| regime_atacadista_saidas_interestaduais_c | `regime_atacadista_saidas_interestaduais_art_16b_i_valor` | numeric(13) |  |  | Regime Atacadista - Saídas interestaduais, Art. 16-B, I - Valor |
| regime_atacadista_saidas_internas_a_aliq | `regime_atacadista_saidas_internas_aliquota_18_art_16b_iii_base_calculo` | numeric(13) |  |  | Regime Atacadista - Saídas internas à alíquota de 18%, Art. 16-B, III - Base de cálculo |
| regime_atacadista_saidas_internas_aliquo | `regime_atacadista_saidas_internas_aliquota_18_art_16b_iii_valor` | numeric(13) |  |  | Regime Atacadista - Saídas internas à alíquota de 18%, Art. 16-B, III - Valor |
| regime_atacadista_saidas_internas_aliquo_c | `regime_atacadista_saidas_internas_aliquota_25_ou_27_art_16b_iv_base_calculo` | numeric(13) |  |  | Regime Atacadista - Saídas internas à alíquota de 25% ou 27%, Art. 16-B, IV - Base de cálculo |
| regime_atacadista_saidas_internas_aliquo_c_c | `regime_atacadista_saidas_internas_aliquota_25_ou_27_art_16b_iv_valor` | numeric(13) |  |  | Regime Atacadista - Saídas internas à alíquota de 25% ou 27%, Art. 16-B, IV - Valor |
| regime_atacadista_adicional_pf_art_16_c | `regime_atacadista_adicional_pf_art_16c_i_base_calculo` | numeric(13) |  |  | Regime Atacadista - Adicional PF, Art. 16-C, I - Base de cálculo |
| regime_atacadista_adicional_pf_art_16c_i | `regime_atacadista_adicional_pf_art_16c_i_valor` | numeric(13) |  |  | Regime Atacadista - Adicional PF, Art. 16-C, I - Valor |
| regime_atacadista_adicional_pf_art_16c_i_c | `regime_atacadista_adicional_pf_art_16c_ii_base_calculo` | numeric(13) |  |  | Regime Atacadista - Adicional PF, Art. 16-C, II - Base de cálculo |
| regime_atacadista_adicional_pf_art_16c_i_c_c | `regime_atacadista_adicional_pf_art_16c_ii_valor` | numeric(13) |  |  | Regime Atacadista - Adicional PF, Art. 16-C, II - Valor |
| regime_atacadista_adicional_excedente_20_c | `regime_atacadista_adicional_excedente_20_pf_art_16c_base_calculo` | numeric(13) |  |  | Regime Atacadista - Adicional excedente 20% PF, Art. 16-C, § Único - Base de cálculo |
| regime_atacadista_adicional_excedente_20_c_c | `regime_atacadista_adicional_excedente_20_pf_art_16c_valor` | numeric(13) |  |  | Regime Atacadista - Adicional excedente 20% PF, Art. 16-C, § Único - Valor |
| regime_atacadista_adicional_saida_em_tra | `regime_atacadista_adicional_saida_transferencia_18_art_16d_i_base_calculo` | numeric(13) |  |  | Regime Atacadista - Adicional saída em transferência 18%, Art. 16-D, I - Base de cálculo |
| regime_atacadista_adicional_saida_transf | `regime_atacadista_adicional_saida_transferencia_18_art_16d_i_valor` | numeric(13) |  |  | Regime Atacadista - Adicional saída em transferência 18%, Art. 16-D, I - Valor |
| regime_atacadista_adicional_saida_transf_c | `regime_atacadista_adicional_saida_transferencia_25_ou_27_art_16d_ii_base_calculo` | numeric(13) |  |  | Regime Atacadista - Adicional saída em transferência 25% ou 27%, Art. 16-D, II - Base de cálculo |
| regime_atacadista_adicional_saida_transf_c_c | `regime_atacadista_adicional_saida_transferencia_25_ou_27_art_16d_ii_valor` | numeric(13) |  |  | Regime Atacadista - Adicional saída em transferência 25% ou 27%, Art. 16-D, II - Valor |
| regime_atacadista_adicional_excedente_20_c_c_c | `regime_atacadista_adicional_excedente_20_saida_transferencia_art_16d_base_calculo` | numeric(13) |  |  | Regime Atacadista - Adicional excedente 20% saída transferência, Art. 16-D, § Único - Base de cálculo |
| regime_atacadista_adicional_excedente_20_c_c_c_c | `regime_atacadista_adicional_excedente_20_saida_transferencia_art_16d_valor` | numeric(13) |  |  | Regime Atacadista - Adicional excedente 20% saída transferência, Art. 16-D, § Único - Valor |
| regime_atacadista_credito_aquisicoes_de | `regime_atacadista_credito_aquisicoes_fornecedor_atacadista_18_art_16b_base_calculo` | numeric(13) |  |  | Regime Atacadista - Crédito aquisições de fornecedor atacadista(18%), Art. 16-B, §3º - Base de cálculo |
| regime_atacadista_credito_aquisicoes_for_c | `regime_atacadista_credito_aquisicoes_fornecedor_atacadista_18_art_16b_valor` | numeric(13) |  |  | Regime Atacadista - Crédito aquisições de fornecedor atacadista(18%), Art. 16-B, §3º - Valor |
| regime_atacadista_credito_aquisicoes_for | `regime_atacadista_credito_aquisicoes_fornecedor_atacadista_25_ou_27_art_16b_base_calculo` | numeric(13) |  |  | Regime Atacadista - Crédito aquisições fornec. atacadista(25% ou 27%),Art. 16-B, §3 - Base de cálculo |
| regime_atacadista_credito_aquisicoes_for_c_c | `regime_atacadista_credito_aquisicoes_fornecedor_atacadista_25_ou_27_art_16b_valor` | numeric(13) |  |  | Regime Atacadista - Crédito aquisições fornec. atacadista(25% ou 27%),Art. 16-B, §3 - Valor |
| regime_atacadista_credito_aquisic_produt | `regime_atacadista_credito_aquisic_produtos_industria_local_art_16b_i_base_calculo` | numeric(13) |  |  | Regime Atacadista - Crédito aquisiç. produtos da indústria local, Art. 16-B, §16º, I - Base de cálculo |
| regime_atacadista_credito_aquisic_produt_c | `regime_atacadista_credito_aquisic_produtos_industria_local_art_16b_i_valor` | numeric(13) |  |  | Regime Atacadista - Crédito aquisiç. produtos da indústria local, Art. 16-B, §16º, I - Valor |
| regime_atacadista_credito_aquisic_produt_c_c | `regime_atacadista_credito_aquisic_produtos_industria_local_art_16b_ii_base_calculo` | numeric(13) |  |  | Regime Atacadista - Crédito aquisiç. produtos da indústria local, Art. 16-B, §16º, II - Base de cálculo |
| regime_atacadista_credito_aquisic_produt_c_c_c | `regime_atacadista_credito_aquisic_produtos_industria_local_art_16b_ii_valor` | numeric(13) |  |  | Regime Atacadista - Crédito aquisiç. produtos da indústria local, Art. 16-B, §16º, II - Valor |
| regime_atacadista_credito_aquisic_produt_c_c_c_c | `regime_atacadista_credito_aquisic_produtos_cesta_basica_art_16b_i_base_calulo` | numeric(13) |  |  | Regime Atacadista - Crédito aquisiç. produtos da Cesta Básica, Art. 16-B, §16º, I - Base de cálculo |
| regime_atacadista_credito_aquisic_produt_c_c_c_c_c | `regime_atacadista_credito_aquisic_produtos_cesta_basica_art_16b_i_valor` | numeric(13) |  |  | Regime Atacadista - Crédito aquisiç. produtos da Cesta Básica, Art. 16-B, §16º, I - Valor |
| regime_atacadista_estorno_de_credito_res | `regime_atacadista_estorno_credito_resultante_sistematica_normal_apuracao_base_calculo` | numeric(13) |  |  | Regime Atacadista - Estorno de crédito resultante da sistemática normal de apuração - Base de cálculo |
| regime_atacadista_estorno_credito_result | `regime_atacadista_estorno_credito_resultante_sistematica_normal_apuracao_valor` | numeric(13) |  |  | Regime Atacadista - Estorno de crédito resultante da sistemática normal de apuração - Valor |
| regime_atacadista_estorno_de_debito_resu | `regime_atacadista_estorno_debito_resultante_sistematica_normal_apuracao_base_calculo` | numeric(13) |  |  | Regime Atacadista - Estorno de débito resultante da sistemática normal de apuração - Base de cálculo |
| regime_atacadista_estorno_debito_resulta | `regime_atacadista_estorno_debito_resultante_sistematica_normal_apuracao_valor` | numeric(13) |  |  | Regime Atacadista - Estorno de débito resultante da sistemática normal de apuração - Valor |
| regime_atacadista_ajuste_na_carga_saida | `regime_atacadista_ajuste_carga_saida_cesta_basica_produtos_industria_rn_18_base_calculo` | numeric(13) |  |  | Regime Atacadista - Ajuste na carga saída Cesta Básica e Produtos Indústria RN - 18% - Base de cálculo |
| regime_atacadista_ajuste_carga_saida_ces | `regime_atacadista_ajuste_carga_saida_cesta_basica_produtos_industria_rn_18_valor` | numeric(13) |  |  | Regime Atacadista - Ajuste na carga saída Cesta Básica e Produtos Indústria RN - 18% - Valor |
| regime_atacadista_ajuste_carga_saida_pro | `regime_atacadista_ajuste_carga_saida_produtos_industria_rn_25_ou_27_base_calculo` | numeric(13) |  |  | Regime Atacadista - Ajuste na carga saída Produtos Indústria RN - 25 ou 27% - Base de cálculo |
| regime_atacadista_ajuste_carga_saida_pro_c | `regime_atacadista_ajuste_carga_saida_produtos_industria_rn_25_ou_27_valor` | numeric(13) |  |  | Regime Atacadista - Ajuste na carga saída Produtos Indústria RN - 25 ou 27% - Valor |
| regime_atacadista_credito_2_sobre_os_est | `credito_sobre_estoque_operacao_de_entrada` | numeric(13) |  |  | Regime Atacadista - Crédito 2% sobre os estoques - Art. 16-J, Dec. 22.199/2011 |
| transferencia_de_credito_de_icms_acumula | `transferencia_credito_icms_acumulado` | numeric(13) |  |  | Transferência de crédito de ICMS acumulado |
| regime_atacadista_considerar_no_calculo | `regime_atacadista_credito_aquisicoes_fornecedor_atacadista_7oumaior_16b_interestadual_base_calculo` | numeric(13) |  |  | Regime Atacadista - Considerar no cálculo as entradas interestaduais - Art. 16-B 7% ou maior Base calculo |
| regime_atacadista_credito_aquisicoes_for_c_c_c | `regime_atacadista_credito_aquisicoes_fornecedor_atacadista_7oumaior_16b_interestadual_valor` | numeric(13) |  |  | Regime Atacadista - Considerar no cálculo as entradas interestaduais - Art. 16-B 7% ou maior Valor |
| regime_atacadista_credito_aquisicoes_for_c_c_c_c | `regime_atacadista_credito_aquisicoes_fornecedor_atacadista_7oumenor_16b_interestadual_base_calculo` | numeric(13) |  |  | Regime Atacadista - Considerar no cálculo as entradas interestaduais - Art. 16-B 7% ou menor Base calculo |
| regime_atacadista_credito_aquisicoes_for_c_c_c_c_c | `regime_atacadista_credito_aquisicoes_fornecedor_atacadista_7oumenor_16b_interestadual_valor` | numeric(13) |  |  | Regime Atacadista - Considerar no cálculo as entradas interestaduais - Art. 16-B 7% ou menor Valor |
| icms_a_recolher_nas_vendas_efetuadas_com | `saldo_icms_vendas_com_cartao_sem_documento` | numeric(13) |  |  | ICMS a recolher nas vendas efetuadas com cartão de crédito sem documento fiscal |
| regime_atacadista_saidas_internas_aliquo_c_c_c | `regime_atacadista_saidas_internas_aliquota_20_art_16b_iii_base_calculo` | numeric(13) |  |  | Regime Atacadista - Saídas internas à alíquota de 20%, Art. 16-B, III - Base de cálculo |
| regime_atacadista_saidas_internas_aliquo_c_c_c_c | `regime_atacadista_saidas_internas_aliquota_20_art_16b_iii_valor` | numeric(13) |  |  | Regime Atacadista - Saídas internas à alíquota de 20%, Art. 16-B, III - Valor |
| regime_atacadista_adicional_saida_transf_c_c_c | `regime_atacadista_adicional_saida_transferencia_20_art_16d_i_base_calculo` | numeric(13) |  |  | Regime Atacadista - Adicional saída em transferência 20%, Art. 16-D, I - Base de cálculo |
| regime_atacadista_adicional_saida_transf_c_c_c_c | `regime_atacadista_adicional_saida_transferencia_20_art_16d_i_valor` | numeric(13) |  |  | Regime Atacadista - Adicional saída em transferência 20%, Art. 16-D, I - Valor |
| regime_atacadista_credito_aquisicoes_for_c_c_c_c_c_c | `regime_atacadista_credito_aquisicoes_fornecedor_atacadista_20_art_16b_base_calculo` | numeric(13) |  |  | Regime Atacadista - Crédito aquisições de fornecedor atacadista(20%), Art. 16-B, §3º - Base de cálculo |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in)

## efsdoimp_estadual_al

**Saldo dos Impostos - Estadual AL** — tabela `EFSDOIMP_ESTADUAL_AL` (23 linhas)

Saldo dos Impostos - Estadual AL. 23 linhas no catálogo; chave: CODI_EMP, CODI_IMP, PDIC_SIM, DATA_SIM.

- **Chave:** `CODI_EMP, CODI_IMP, PDIC_SIM, DATA_SIM`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 23 linhas, 1 empresa(s), DATA_SIM de 2018-01-01 a 2019-11-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| credito_presumido_nos_termos_do_item_8_a | `credito_presumido_20_transportadoras_icms` | numeric(13) |  |  | Crédito Presumido - Nos termos do Item 8 Anexo III/RICMS |
| outros_creditos_nas_operacoes_com_ct_e_s | `outros_creditos_nas_operacoes_com_cte_substituto` | numeric(13) |  |  | Outros créditos nas operações com CT-e substituto |

**Filtros:** `imposto` (eq/in), `periodicidade` (eq/in), `competencia` (eq/in)

## efsdoimp_subtri_por_uf_se

**Saldo dos Impostos - Substituição Tributária Por SE** — tabela `EFSDOIMP_SUBTRI_POR_UF_SE` (17 linhas)

Saldo dos Impostos - Substituição Tributária Por SE. 17 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 17 linhas, 1 empresa(s), DATA_SIM de 2018-01-01 a 2019-05-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| sigla_da_uf | `sigla_uf` | char(2) |  |  | Sigla da UF |
| recolhimento | `i_recolhimento` | integer(4) |  |  | Recolhimento |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `sigla_da_uf` (eq/in), `recolhimento` (eq/in)

## efsdoimp_pis_cofins_detalhamento_debito_imobiliario

**Saldo do Impostos - Detalhamentos do PIS/COFINS - Débito Imobiliário** — tabela `EFSDOIMP_PIS_COFINS_DETALHAMENTO_DEBITO_IMOBILIARIO` (14 linhas)

Saldo do Impostos - Detalhamentos do PIS/COFINS - Débito Imobiliário. 14 linhas no catálogo; chave: CODI_EMP, FILIAL, I_EMPREENDIMENTO, I_UNIDADE, CODI_IMP, DATA_SIM, PDIC_SIM, I_CONTRATO, I_SCP, I_RECOLHIMENTO.

- **Chave:** `CODI_EMP, FILIAL, I_EMPREENDIMENTO, I_UNIDADE, CODI_IMP, DATA_SIM, PDIC_SIM, I_CONTRATO, I_SCP, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `FILIAL asc`, `I_EMPREENDIMENTO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 14 linhas, 2 empresa(s), DATA_SIM de 2021-06-01 a 2021-10-01.
- Vínculo efempreendimentos_imobil (EFEMPREENDIMENTOS_IMOBILIARIOS_UNIDADES): 0 de 8 linhas sem registro relacionado (empresa 741).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_da_filial | `filial` | integer(4) |  |  | Código da Filial |
| codigo_do_empreendimento | `i_empreendimento` | integer(4) |  |  | Código do empreendimento |
| codigo_da_unidade | `i_unidade` | integer(4) |  |  | Código da unidade |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| codigo_do_contrato | `i_contrato` | integer(4) |  |  | Código do contrato |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |
| sequencial_do_recolhimento | `i_recolhimento` | integer(4) |  |  | Sequencial do Recolhimento |
| valor_total_da_unidade_imobiliaria_vendi | `valor_total_venda` | numeric(13) |  |  | Valor total da unidade imobiliária vendida atualizado até o período da escrituração |
| valor_recebido_acumulado_ate_o_mes_anter | `valor_recebido_acumulado` | numeric(13) |  |  | Valor recebido acumulado até o mês anterior ao da escrituração |
| valor_total_recebido_no_mes_da_escritura | `valor_total_recebido` | numeric(13) |  |  | Valor total recebido no mês da escrituração |
| codigo_da_situacao_tributaria | `cst` | integer(4) |  |  | Código da Situação Tributária |
| base_de_calculo | `base_calculo` | numeric(13) |  |  | Base de Cálculo |
| aliquota | `aliquota` | numeric(12) |  |  | Alíquota |
| valor | `valor` | numeric(13) |  |  | Valor |
| percentual_da_receita_total_recebida_ate | `percentual_receita_recebida` | numeric(13) |  |  | Percentual da receita total recebida até o mês |
| valor_da_correcao | `valor_correcao` | numeric(13) |  |  | Valor da correção |
| valor_dos_juros | `valor_juros` | numeric(13) |  |  | Valor dos juros |
| valor_da_multa | `valor_multa` | numeric(13) |  |  | Valor da multa |
| valor_do_desconto | `valor_desconto` | numeric(13) |  |  | Valor do desconto |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efempreendimentos_imobil` → `EFEMPREENDIMENTOS_IMOBILIARIOS_UNIDADES` por `filial` = `codi_emp` e `i_empreendimento` = `i_empreendimento` e `i_unidade` = `i_unidade`; colunas: `efempreendimentos_imobil_nome`

**Filtros:** `codigo_da_filial` (eq/in), `codigo_do_empreendimento` (eq/in), `codigo_da_unidade` (eq/in), `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `codigo_do_contrato` (eq/in), `sequencial_do_scp` (eq/in), `sequencial_do_recolhimento` (eq/in)

## efsdoimp_pis_cofins_detalhamento_extemporaneo_ctb

**Saldo do Impostos - Detalhamentos do PIS/COFINS - Créditos - Extemporâneo - Contabilização** — tabela `EFSDOIMP_PIS_COFINS_DETALHAMENTO_EXTEMPORANEO_CTB` (8 linhas)

Saldo do Impostos - Detalhamentos do PIS/COFINS - Créditos - Extemporâneo - Contabilização. 8 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_CREDITO, ALIQUOTA_PERCENTUAL, ALIQUOTA_VALOR, I_SCP, I_RECOLHIMENTO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_CREDITO, ALIQUOTA_PERCENTUAL, ALIQUOTA_VALOR, I_SCP, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 8 linhas, 3 empresa(s), DATA_SIM de 2018-07-01 a 2026-06-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| codigo_do_credito | `codigo_credito` | integer(4) |  |  | Código do crédito |
| valor_da_aliquota_do_imposto | `aliquota_percentual` | numeric(7) |  |  | Valor da alíquota do imposto |
| aliquota_em_moeda_quando_o_calculo_e_por | `aliquota_valor` | numeric(13) |  |  | Alíquota em moeda (quando o cálculo é por unidade de medida) |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |
| sequencial_do_recolhimento | `i_recolhimento` | integer(4) |  |  | Sequencial do Recolhimento |
| valor_apurado | `valor_apurado` | numeric(13) |  |  | Valor apurado |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `codigo_do_credito` (eq/in), `valor_da_aliquota_do_imposto` (eq/in), `aliquota_em_moeda_quando_o_calculo_e_por` (eq/in), `sequencial_do_scp` (eq/in), `sequencial_do_recolhimento` (eq/in)

## efsdoimp_estadual_to

**Saldo dos Impostos - Estadual TO** — tabela `EFSDOIMP_ESTADUAL_TO` (6 linhas)

Saldo dos Impostos - Estadual TO. 6 linhas no catálogo; chave: CODI_IMP, CODI_EMP, DATA_SIM, PDIC_SIM.

- **Chave:** `CODI_IMP, CODI_EMP, DATA_SIM, PDIC_SIM`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 6 linhas, 1 empresa(s), DATA_SIM de 2026-07-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| credito_presumido_atacadista_st_sul_e_su | `credito_presumido_atacadista_st_sul_sudeste` | numeric(13) |  |  | Crédito Presumido Atacadista ST Sul e Suldeste |
| credito_presumido_atacadista_st_demais_e | `credito_presumido_atacadista_st_demais_estados` | numeric(13) |  |  | Crédito Presumido Atacadista ST Demais Estados |
| devolucao_credito_presumido_atacadista_s | `devolucao_credito_presumido_atacadista_st_sul_sudeste` | numeric(13) |  |  | Devolução Crédito Presumido Atacadista ST Sul e Suldeste |
| devolucao_credito_presumido_atacadista_s_c | `devolucao_credito_presumido_atacadista_st_demais_estados` | numeric(13) |  |  | Devolução Crédito Presumido Atacadista ST Demais Estados |
| devolucao_credito_presumido_atacadista_s_c_c | `devolucao_credito_presumido_atacadista_st` | numeric(13) |  |  | Devolução Crédito Presumido Atacadista ST |
| credito_presumido_75_icms_apurado | `credito_presumido_75_icms_apurado` | numeric(13) |  |  | Crédito presumido de 75% - Lei Nº 1.201/2000, Art. 1º, I |
| credito_de_icms_conf_aliquota_do_simples | `credito_conforme_aliquota_sn` | numeric(13) |  |  | Crédito de ICMS conf. alíquota do Simples Nacional - Art. 23, LC 123/06 |
| devolucao_de_mercadoria_adquirida_de_sim | `devolucao_mercadoria_adquirida_sn` | numeric(13) |  |  | Devolução de mercadoria adquirida de Simples Nacional |
| credito_exclusao_simples_nacional | `credito_exclusao_simples_nacional` | numeric(13) |  |  | Crédito Exclusão Simples Nacional |
| credito_ativo_imobilizado | `credito_ativo_imobilizado` | numeric(13) |  |  | Crédito Ativo Imobilizado |
| saldo_inferior_a_quantidade_minima_para | `saldo_inferior_quant_minima_recolhimento_sst` | numeric(13) |  |  | Saldo inferior a quantidade mínima para recolhimento |
| saldo_anterior_inferior_a_quantidade_min | `saldo_ant_inferior_quant_minima_recolhimento_sst` | numeric(13) |  |  | Saldo anterior inferior a quantidade mínima para recolhimento |
| credito_presumido_de_70_sobre_o_icms_apu | `credito_presumido_70_icms_apurado` | numeric(13) |  |  | Crédito presumido de 70% sobre o ICMS apurado |
| credito_presumido_nas_operacoes_internas | `credito_presumido_atacadista_op_internas` | numeric(13) |  |  | Crédito presumido nas operações internas de comércio atacadista - Lei Nº 1.201/2000, Art. 1º, I |
| credito_presumido_nas_operacoes_interest | `credito_presumido_atacadista_op_interestaduais` | numeric(13) |  |  | Crédito presumido nas operações interestaduais de comércio atacadista - Lei Nº 1.201/2000, Art. 1º, I |
| estorno_de_credito_operacoes_comercio_at | `credito_presumido_atacadista_estorno_credito` | numeric(13) |  |  | Estorno de crédito operações comércio atacadista - Lei 1.201/00, Art. 1º, I |
| credito_presumido_50_icms_apurado | `credito_presumido_50_icms_apurado` | numeric(13) |  |  | Crédito presumido de 50% - Lei Nº 1.201/2000, Art. 1º, III |
| credito_presumido_80_icms_apurado | `credito_presumido_80_icms_apurado` | numeric(13) |  |  | Crédito presumido de 80% - Lei Nº 1.201/2000, Art. 1º, I |
| credito_presumido_80_iii_icms_apurado | `credito_presumido_80_iii_icms_apurado` | numeric(13) |  |  | Crédito presumido de 80% - Lei Nº 1.201/2000, Art. 1º, III |
| credito_presumido_75_iii_icms_apurado | `credito_presumido_75_iii_icms_apurado` | numeric(13) |  |  | Crédito presumido de 75% - Lei Nº 1.201/2000, Art. 1º, III |
| credito_presumido_de_20_para_transportad | `credito_presumido_20_transportadora_convenio_icms_106_96` | numeric(13) |  |  | Crédito presumido de 20% para transportadoras -  Art. 9º, III do RICMS |
| estorno_de_debito_nas_operacoes_com_ct_e | `estorno_debito_operacoes_cte_substituto` | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |
| estorno_de_credito_presumido_transportes | `estorno_credito_presumido_transporte_cte_cteos_substituto` | numeric(13) |  |  | Estorno de crédito presumido transportes - Operações com CT-e e/ou CT-eOS substituto |
| credito_presumido_op_interestaduais_come | `credito_presumido_lei_1790_2007_op_interestaduais` | numeric(13) |  |  | Crédito presumido op. interestaduais comércio atacadista - Lei 1.790/2007, Art. 1º, I |
| credito_presumido_op_internas_comercio_a | `credito_presumido_lei_1790_2007_op_internas` | numeric(13) |  |  | Crédito presumido op. Internas comércio atacadista - Lei 1.790/2007, Art. 1º, I |
| credito_presumido_lei_1790_2007_estorno | `credito_presumido_lei_1790_2007_estorno_credito` | numeric(13) |  |  | Estorno de crédito operações comércio atacadista - Lei Nº 1.790/2007, Art. 1º, §7º |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in)

## efsdoimp_por_uf_es

**Saldo dos Impostos - Por UF - RS** — tabela `EFSDOIMP_POR_UF_ES` (5 linhas)

Saldo dos Impostos - Por UF - RS. 5 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 5 linhas, 1 empresa(s), DATA_SIM de 2026-05-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| sigla_da_uf | `sigla_uf` | char(2) |  |  | Sigla da UF |
| estorno_debitos_lancados | `estorno_debitos_lancado` | numeric(13) |  |  | Estorno Débitos - Lançados |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `sigla_da_uf` (eq/in)

## efsdoimp_pis_cofins_detalhamento_retencao_nao_considerado

**Saldo do Impostos - Detalhamentos do PIS/COFINS - Retencoes não consideradas** — tabela `EFSDOIMP_PIS_COFINS_DETALHAMENTO_RETENCAO_NAO_CONSIDERADO` (4 linhas)

Saldo do Impostos - Detalhamentos do PIS/COFINS - Retencoes não consideradas. 4 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, NATUREZA_RETENCAO, PERIODO_APURACAO, I_SCP, I_RECOLHIMENTO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, NATUREZA_RETENCAO, PERIODO_APURACAO, I_SCP, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4 linhas, 1 empresa(s), DATA_SIM de 2025-01-01 a 2025-02-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| natureza_da_retencao | `natureza_retencao` | integer(4) |  |  | Natureza da retencao |
| periodo_de_apuracao_da_retencao | `periodo_apuracao` | date(4) |  |  | Periodo de apuracao da retencao |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |
| sequencial_do_recolhimento | `i_recolhimento` | integer(4) |  |  | Sequencial do Recolhimento |
| valor_disponivel | `valor_disponivel` | numeric(13) |  |  | Valor disponivel |
| valor_utilizado | `valor_utilizado` | numeric(13) |  |  | Valor utilizado |
| valor_transportar | `valor_a_transportar` | numeric(13) |  |  | Valor transportar |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `natureza_da_retencao` (eq/in), `periodo_de_apuracao_da_retencao` (eq/in), `sequencial_do_scp` (eq/in), `sequencial_do_recolhimento` (eq/in)

## efsdoimp_estadual_pa

**Saldo dos Impostos - Estadual PA** — tabela `EFSDOIMP_ESTADUAL_PA` (3 linhas)

Saldo dos Impostos - Estadual PA. 3 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3 linhas, 1 empresa(s), DATA_SIM de 2026-07-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| credito_presumido_de_20_para_transportad | `credito_presumido_transporte` | numeric(13) |  |  | Crédito presumido de 20% para transportadoras - Art. 7, Anexo IV do RICMS |
| credito_presumido_transporte_ct_conv_106 | `credito_presumido_transporte_ct_conv_106` | numeric(13) |  |  | Crédito presumido de 20% para transportadoras - Art. 7, Anexo IV do RICMS - Conhecimento de transporte |
| credito_presumido_transporte_bp_conv_106 | `credito_presumido_transporte_bp_conv_106` | numeric(13) |  |  | Crédito presumido de 20% para transportadoras - Art. 7, Anexo IV do RICMS - Bilhete de passagem |
| valor_taxa_servico_arrecadacao_dae | `valor_taxa_servico_arrecadacao_dae` | numeric(13) |  |  | Valor Taxa serviço arrecadação DAE |
| mercadorias_sujeitas_a_antecip_nas_opera | `mercadorias_sujeitas_antecip_oper_inter` | numeric(13) |  |  | Mercadorias sujeitas à Antecip. nas Operaç. Interestaduais - Art. 115, An I, RICMS |
| transferencia_de_credito_de_icms_acumula | `transferencia_credito_icms_acumulado_outros_debitos` | numeric(13) |  |  | Transferência de crédito de ICMS acumulado - Outros débitos |
| transferencia_credito_icms_acumulado_out | `transferencia_credito_icms_acumulado_outros_creditos` | numeric(13) |  |  | Transferência de crédito de ICMS acumulado - Outros créditos |
| estorno_de_debito_nas_operacoes_com_ct_e | `estorno_debito_operacoes_cte_substituto` | numeric(13) |  |  | Estorno de débito nas operações com CT-e e/ou CT-eOS substituto |
| credito_presumido_saida_interna_produtos | `credito_presumido_saida_interna_cesta_basica_art126` | numeric(13) |  |  | Crédito Presumido saída interna produtos cesta básica - Art. 126 do RICMS |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in)

## efsdoimp_subtri_por_uf_pa

**Saldo dos Impostos - Substituição Tributária Por PA** — tabela `EFSDOIMP_SUBTRI_POR_UF_PA` (3 linhas)

Saldo dos Impostos - Substituição Tributária Por PA. 3 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3 linhas, 1 empresa(s), DATA_SIM de 2026-07-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| sigla_da_uf | `sigla_uf` | char(2) |  |  | Sigla da UF |
| recolhimento | `i_recolhimento` | integer(4) |  |  | Recolhimento |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `sigla_da_uf` (eq/in), `recolhimento` (eq/in)

## efsdoimp_subtri_por_uf_to

**Saldo dos Impostos - Substituição Tributária Por TO** — tabela `EFSDOIMP_SUBTRI_POR_UF_TO` (3 linhas)

Saldo dos Impostos - Substituição Tributária Por TO. 3 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3 linhas, 1 empresa(s), DATA_SIM de 2026-07-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| sigla_da_uf | `sigla_uf` | char(2) |  |  | Sigla da UF |
| recolhimento | `i_recolhimento` | integer(4) |  |  | Recolhimento |
| saldo_inferior_a_quantidade_minima_de_re | `saldo_inferior_quant_minima_recolhimento` | numeric(13) |  |  | Saldo inferior a quantidade mínima de recolhimento |
| saldo_de_periodo_anterior_inferior_a_qua | `saldo_ant_inferior_quant_minima_recolhimento` | numeric(13) |  |  | Saldo de período anterior inferior a quantidade mínima de recolhimento |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `sigla_da_uf` (eq/in), `recolhimento` (eq/in)

## efsdoimp_scp_csll_csll_retido

**Saldo dos Impostos - CSLL Retido** — tabela `EFSDOIMP_SCP_CSLL_CSLL_RETIDO` (2 linhas)

Saldo dos Impostos - CSLL Retido. 2 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SCP, NATUREZA, PERIODO_APURACAO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, I_SCP, NATUREZA, PERIODO_APURACAO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 1 empresa(s), DATA_SIM de 2021-09-01 a 2021-12-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| data | `data_sim` | date(4) |  |  | Data |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| scp | `i_scp` | integer(4) |  |  | SCP |
| natureza | `natureza` | integer(4) |  |  | Natureza |
| periodo_de_apuracao_da_retencao | `periodo_apuracao` | date(4) |  |  | Período de apuração da retenção |
| valor_retido | `valor_retido` | numeric(13) |  |  | Valor Retido |
| valor_retido_utilizado | `valor_retido_utilizado` | numeric(13) |  |  | Valor Retido Utilizado |
| valor_retido_disponivel | `valor_retido_disponivel` | numeric(13) |  |  | Valor Retido Disponível |

**Filtros:** `imposto` (eq/in), `data` (eq/in), `periodicidade` (eq/in), `scp` (eq/in), `natureza` (eq/in), `periodo_de_apuracao_da_retencao` (eq/in)

## efsdoimp_simples_nacional_detalhamento

**Saldo dos Impostos - Simples Nacional - Exigibilidade Suspensa** — tabela `EFSDOIMP_SIMPLES_NACIONAL_DETALHAMENTO` (1 linhas)

Saldo dos Impostos - Simples Nacional - Exigibilidade Suspensa. 1 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, FILIAL, ANEXO, SECAO, TABELA, ARBCICMS, ARBCISS, SITUACOES, SEQUENCIAL, IMPOSTO, MUNICIPIO, ARBCPIS, ARBCCOFINS, TIPO_RECEITA, ANEXO_ORIGEM, SECAO_ORIGEM, TABELA_ORIGEM, APLICA_REDUCAO_BASE_CALCULO_ICMS, APLICA_REDUCAO_ISS.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, FILIAL, ANEXO, SECAO, TABELA, ARBCICMS, ARBCISS, SITUACOES, SEQUENCIAL, IMPOSTO, MUNICIPIO, ARBCPIS, ARBCCOFINS, TIPO_RECEITA, ANEXO_ORIGEM, SECAO_ORIGEM, TABELA_ORIGEM, APLICA_REDUCAO_BASE_CALCULO_ICMS, APLICA_REDUCAO_ISS`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s), DATA_SIM de 2023-11-01 a 2023-11-01.
- imposto_com_exigibilidade_suspensa_1_icm: todos os valores reais estão no comentário do banco (3=1).
- tipo_receita_1_mercado_interno_2_exporta: todos os valores reais estão no comentário do banco (1=1).
- motivo_1_liminar_em_mandado_de_seguranca: todos os valores reais estão no comentário do banco (6=1).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competencia |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| codigo_da_filial | `filial` | integer(4) |  |  | Codigo da filial |
| anexo | `anexo` | tinyint(1) |  |  | Anexo |
| secao | `secao` | tinyint(1) |  |  | Secao |
| tabela | `tabela` | tinyint(1) |  |  | Tabela |
| aliquota_de_reducao_da_base_de_calculo_d | `arbcicms` | numeric(13) |  |  | Aliquota de reducao da base de calculo do ICMS |
| arbciss | `arbciss` | numeric(13) |  |  | Aliquota de reducao da base de calculo do ISS |
| situacoes_fiscais | `situacoes` | char(16) |  |  | Situacoes fiscais |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| imposto_com_exigibilidade_suspensa_1_icm | `imposto` | integer(4) |  | efsdoimp_simples_nacional_detalhamento_imposto_com | Imposto com exigibilidade suspensa(1 - ICMS/2 -IPI/3 - ISS/4 - PIS/5 - COFINS/6 - CSLL/7 - IRPJ/8 - INSS) |
| codigo_do_municipio | `municipio` | integer(4) |  |  | Código do município |
| aliquota_de_reducao_de_base_de_calculo_d | `arbcpis` | numeric(13) |  |  | Alíquota de Redução de Base de Cálculo do PIS |
| arbccofins | `arbccofins` | numeric(13) |  |  | Alíquota de Redução de Base de Cálculo do COFINS |
| tipo_receita_1_mercado_interno_2_exporta | `tipo_receita` | integer(4) |  | efsdoimp_simples_nacional_detalhamento_tipo_receit | Tipo Receita (1- Mercado Interno / 2- Exportação) |
| anexo_origem | `anexo_origem` | integer(4) |  |  | Anexo Origem |
| secao_origem | `secao_origem` | integer(4) |  |  | Seção Origem |
| tabela_origem | `tabela_origem` | integer(4) |  |  | Tabela Origem |
| aplica_reducao_na_base_de_calculo_do_icm | `aplica_reducao_base_calculo_icms` | char(1) |  |  | Aplica redução na base de calculo do ICMS |
| reducao_do_iss_aplicado_na_aliquota_ou_n | `aplica_reducao_iss` | char(1) |  |  | Redução do ISS aplicado na Alíquota ou na Base de Calculo |
| motivo_1_liminar_em_mandado_de_seguranca | `motivo` | char(1) |  | efsdoimp_simples_nacional_detalhamento_motivo_1_li | Motivo(1 - Liminar em Mandado de Seguranca/2 - Deposito Judicial/3 - Antecipacao de Tutela/4 - Liminar em Medida Cautelar/5 - Deposito Administrativo/6 - Outros) |
| numero_do_processo | `processo` | char(20) |  |  | Numero do processo |
| vara | `vara` | integer(4) |  |  | Vara |
| municipio | `codigo_municipio` | integer(4) |  |  | Municipio |
| uf | `uf` | char(2) |  |  | UF |
| com_deposito_s_n | `deposito` | char(1) |  |  | Com deposito(S/N) |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `codigo_da_filial` (eq/in), `anexo` (eq/in), `secao` (eq/in), `tabela` (eq/in), `aliquota_de_reducao_da_base_de_calculo_d` (eq/in), `arbciss` (eq/in), `situacoes_fiscais` (eq/in), `sequencial` (eq/in), `imposto_com_exigibilidade_suspensa_1_icm` (eq/in), `codigo_do_municipio` (eq/in), `aliquota_de_reducao_de_base_de_calculo_d` (eq/in)

## efsdoimp_por_recolhimento_por_nota

**Saldo dos impostos - detalhamento dos impostos por nota e por código de recolhimento** — tabela `EFSDOIMP_POR_RECOLHIMENTO_POR_NOTA` (1 linhas)

Saldo dos impostos - detalhamento dos impostos por nota e por código de recolhimento. 1 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_NOTA, I_RECOLHIMENTO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, CODIGO_NOTA, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_VENCIMENTO`
- **Ordem padrão:** `DATA_VENCIMENTO desc`, `CODI_IMP asc`, `DATA_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s), DATA_VENCIMENTO de 2024-05-26 a 2024-05-26.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| pdic_sim | `pdic_sim` | integer(4) |  |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=COMPLEMENTAR, 52=13SAL) |
| codigo_da_nota_de_entrada | `codigo_nota` | integer(4) |  |  | Código da nota de entrada |
| sequencial_do_codigo_de_recolhimento | `i_recolhimento` | integer(4) |  |  | Sequencial do código de recolhimento |
| codigo_de_recolhimento | `codigo_recolhimento` | char(6) |  |  | Código de recolhimento |
| parcela | `parcela` | integer(4) |  |  | Parcela |
| saldo_a_recolher | `valor_recolher` | numeric(13) |  |  | Saldo a recolher |
| valor_contabil | `valor_contabil` | numeric(13) |  |  | Valor contábil |
| base_de_calculo | `base_calculo` | numeric(13) |  |  | Base de cálculo |
| valor_do_imposto | `valor_imposto` | numeric(13) |  |  | Valor do imposto |
| valor_pago | `valor_pago` | numeric(13) |  |  | Valor pago |
| data_do_vencimento | `data_vencimento` | date(4) |  |  | Data do vencimento |
| classe_do_vencimento | `classe_vencimento` | integer(4) |  |  | Classe do vencimento |
| valor_regime_especial | `valor_regime_especial` | numeric(13) |  |  | Valor regime especial |
| valor_credito_presumido | `valor_credito_presumido` | numeric(13) |  |  | Valor crédito presumido |
| valor_estorno_regime_especial | `valor_estorno_regime_especial` | numeric(13) |  |  | Valor estorno regime especial |
| valor_estorno_credito_presumido | `valor_estorno_credito_presumido` | numeric(13) |  |  | Valor estorno crédito presumido |
| valor_isentas | `valor_isentas` | numeric(13) |  |  | Valor isentas |
| valor_outras | `valor_outras` | numeric(13) |  |  | Valor outras |
| debitos_pelas_saidas | `debitos_saidas` | numeric(13) |  |  | Débitos pelas saídas |
| debitos_pelas_entradas | `debitos_entradas` | numeric(13) |  |  | Débitos pelas entradas |
| creditos_pelas_devolucoes_de_saidas | `creditos_devolucoes_saidas` | numeric(13) |  |  | Créditos pelas devoluções de saídas |
| creditos_pelas_devolucoes_de_entradas | `creditos_devolucoes_entradas` | numeric(13) |  |  | Créditos pelas devoluções de entradas |
| ressarcimento_de_icms_substituicao_tribu | `ressarcimento_icms_st_acobertado_nfe` | numeric(13) |  |  | Ressarcimento de ICMS Substituição Tributária acobertado por NF-e |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `pdic_sim` (eq/in), `codigo_da_nota_de_entrada` (eq/in), `sequencial_do_codigo_de_recolhimento` (eq/in), `data_do_vencimento` (entre/gte/lte), `codigo_de_recolhimento` (eq/in)

## efsdoimp_subtri_por_uf_rj_compl_rest_icms_st

**Saldo dos Impostos - Substituição Tributária Por RJ - Complemento/Restituição de ICMS ST** — tabela `EFSDOIMP_SUBTRI_POR_UF_RJ_COMPL_REST_ICMS_ST` (1 linhas)

Saldo dos Impostos - Substituição Tributária Por RJ - Complemento/Restituição de ICMS ST. 1 linhas no catálogo; chave: CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO.

- **Chave:** `CODI_EMP, CODI_IMP, DATA_SIM, PDIC_SIM, SIGLA_UF, I_RECOLHIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_SIM`
- **Ordem padrão:** `DATA_SIM desc`, `CODI_IMP asc`, `PDIC_SIM asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s), DATA_SIM de 2024-08-01 a 2024-08-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| competencia | `data_sim` | date(4) |  |  | Competência |
| periodicidade | `pdic_sim` | integer(4) |  |  | Periodicidade |
| sigla_da_uf | `sigla_uf` | char(2) |  |  | Sigla da UF |
| recolhimento | `i_recolhimento` | integer(4) |  |  | Recolhimento |
| debitos_pelas_saidas | `debitos_saidas` | numeric(13) |  |  | Débitos pelas saídas |
| creditos_pelas_entradas | `creditos_entradas` | numeric(13) |  |  | Créditos pelas entradas |
| complemento_de_icms_st | `complemento_subtri` | numeric(13) |  |  | Complemento de ICMS ST |
| ressarcimento_de_icms_st | `ressarcimento_subtri` | numeric(13) |  |  | Ressarcimento de ICMS ST |
| ressarcimento_de_icms_st_periodo_anterio | `ressarcimento_subtri_periodo_anterior` | numeric(13) |  |  | Ressarcimento de ICMS ST período anterior |
| ressarcimento_de_icms_st_periodo_seguint | `ressarcimento_subtri_periodo_seguinte` | numeric(13) |  |  | Ressarcimento de ICMS ST período seguinte |
| sequencial_indicador_do_valor_de_ressarc | `sequencial_ressarcimento_acumulado` | integer(4) |  |  | Sequencial indicador do valor de ressarcimento acumulado |

**Filtros:** `imposto` (eq/in), `competencia` (eq/in), `periodicidade` (eq/in), `sigla_da_uf` (eq/in), `recolhimento` (eq/in)

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

### efsdoimp_pis_cofins_reducao_linear_aproveitamento_credito_cst_06_aliqu

Confirmado: parcial

> Valores em EFSDOIMP_PIS_COFINS_REDUCAO_LINEAR_APROVEITAMENTO_CREDITO.CST fora do comentário do banco: 6=3.075, 7=3.075. Distribuição: 6=3.075, 7=3.075 (2026-10-18).

| Código | Significado |
|---|---|
| 06 | ALIQUOTA ZERO |
| 07 | ISENCAO |

### efsdoimp_pis_cofins_reducao_linear_por_nota_operacao_a_

Confirmado: sim

> Todos os valores observados em EFSDOIMP_PIS_COFINS_REDUCAO_LINEAR_POR_NOTA.OPERACAO estão no comentário do banco (2026-10-18). Distribuição: A=2.358, R=62.

| Código | Significado |
|---|---|
| A | Acrescimo |
| R | Reducao |

### efsdoimp_estadual_mg_n_apurado_antes_da_

Confirmado: sim

> Todos os valores observados em EFSDOIMP_ESTADUAL_MG.NCAL_BARES_RESTAURANTES_E_SIMILARES estão no comentário do banco (2026-10-18). Distribuição: S=435, N=101.

| Código | Significado |
|---|---|
| N | Apurado antes da SAI 56215 |
| S | Apurado depois da SAI 56215 |

### efsdoimp_nao_cumulativos_metodo_de_d

Confirmado: sim

> Todos os valores observados em efsdoimp_nao_cumulativos.metodo estão no comentário do banco (2026-10-18). Distribuição: I=274.

| Código | Significado |
|---|---|
| I | somente interno |
| E | interno e externo |

### efsdoimp_pis_cofins_reducao_linear_operacao_a_

Confirmado: sim

> Todos os valores observados em EFSDOIMP_PIS_COFINS_REDUCAO_LINEAR.OPERACAO estão no comentário do banco (2026-10-18). Distribuição: A=88, R=56.

| Código | Significado |
|---|---|
| A | Acrescimo |
| R | Reducao |

### efsdoimp_aproveitamento_credito_origem_do_c

Confirmado: sim

> Todos os valores observados em efsdoimp_aproveitamento_credito.origem estão no comentário do banco (2026-10-18). Distribuição: 1=136.

| Código | Significado |
|---|---|
| 1 | interno |
| 2 | externo |

### efsdoimp_aproveitamento_credito_tipo_1_inte

Confirmado: sim

> Todos os valores observados em efsdoimp_aproveitamento_credito.tipo estão no comentário do banco (2026-10-18). Distribuição: 1=136.

| Código | Significado |
|---|---|
| 1 | interno |
| 2 | nao tributado |
| 3 | externo |

### efsdoimp_pis_cofins_reducao_linear_natureza_operacao_a_

Confirmado: sim

> Todos os valores observados em EFSDOIMP_PIS_COFINS_REDUCAO_LINEAR_NATUREZA.OPERACAO estão no comentário do banco (2026-10-18). Distribuição: A=48, R=12.

| Código | Significado |
|---|---|
| A | Acrescimo |
| R | Reducao |

### efsdoimp_pis_cofins_reducao_linear_filial_operacao_a_

Confirmado: sim

> Todos os valores observados em EFSDOIMP_PIS_COFINS_REDUCAO_LINEAR_FILIAL.OPERACAO estão no comentário do banco (2026-10-18). Distribuição: A=44, R=12.

| Código | Significado |
|---|---|
| A | Acrescimo |
| R | Reducao |

### efsdoimp_mg_sub_apuracao_incentivo_ret_sequencial_

Confirmado: sim

> Todos os valores observados em EFSDOIMP_MG_SUB_APURACAO_INCENTIVO_RET.I_SUB_APURACAO_CONSULTA_APURACAO estão no comentário do banco (2026-10-18). Distribuição: 0=17, 1=17.

| Código | Significado |
|---|---|
| 0 | Apuração normal |
| 1 | N-sub apuração |

### efsdoimp_simples_nacional_base_negativa_tipo_receit

Confirmado: sim

> Todos os valores observados em EFSDOIMP_SIMPLES_NACIONAL_BASE_NEGATIVA.TIPO_RECEITA estão no comentário do banco (2026-10-18). Distribuição: 1=12.925, 2=530.

| Código | Significado |
|---|---|
| 1 | Mercado Interno |
| 2 | Exportação |

### efsdoimp_simples_nacional_salao_parceiro_tipo_receit

Confirmado: sim

> Todos os valores observados em EFSDOIMP_SIMPLES_NACIONAL_SALAO_PARCEIRO.TIPO_RECEITA estão no comentário do banco (2026-10-18). Distribuição: 1=12.544, 2=525.

| Código | Significado |
|---|---|
| 1 | Mercado Interno |
| 2 | Exportação |

### efsdoimp_simples_nacional_prorrogacao_tipo_prorro

Confirmado: parcial

> Valores em EFSDOIMP_SIMPLES_NACIONAL_PRORROGACAO.TIPO_PRORROGACAO fora do comentário do banco: 5=231. Distribuição: 5=231, 1=207, 3=106, 4=63, 2=33 (2026-10-18).

| Código | Significado |
|---|---|
| 1 | FEDERAIS |
| 2 | ESTADUAIS |
| 3 | MUNICIPAIS |
| 4 | OUTROS |

### efsdoimp_simples_nacional_prorrogacao_prorrogacao

Confirmado: parcial

> Valores em EFSDOIMP_SIMPLES_NACIONAL_PRORROGACAO.PRORROGACAO fora do comentário do banco: Q=231, ME=63. Distribuição: Q=231, F=207, M=106, ME=63, E=33 (2026-10-18).

| Código | Significado |
|---|---|
| F | Federais |
| E | Estaduais |
| M | Municipais |

### efsdoimp_simples_nacional_controle_base_negativa_devolucao_s_tipo_receit

Confirmado: sim

> Todos os valores observados em EFSDOIMP_SIMPLES_NACIONAL_CONTROLE_BASE_NEGATIVA_DEVOLUCAO_SECUNDARIA.TIPO_RECEITA estão no comentário do banco (2026-10-18). Distribuição: 2=33, 1=30.

| Código | Significado |
|---|---|
| 1 | Mercado Interno |
| 2 | Exportação |

### efsdoimp_simples_nacional_detalhamento_imposto_com

Confirmado: sim

> Todos os valores observados em EFSDOIMP_SIMPLES_NACIONAL_DETALHAMENTO.IMPOSTO estão no comentário do banco (2026-10-18). Distribuição: 3=1.

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

### efsdoimp_simples_nacional_detalhamento_tipo_receit

Confirmado: sim

> Todos os valores observados em EFSDOIMP_SIMPLES_NACIONAL_DETALHAMENTO.TIPO_RECEITA estão no comentário do banco (2026-10-18). Distribuição: 1=1.

| Código | Significado |
|---|---|
| 1 | Mercado Interno |
| 2 | Exportação |

### efsdoimp_simples_nacional_detalhamento_motivo_1_li

Confirmado: sim

> Todos os valores observados em EFSDOIMP_SIMPLES_NACIONAL_DETALHAMENTO.MOTIVO estão no comentário do banco (2026-10-18). Distribuição: 6=1.

| Código | Significado |
|---|---|
| 1 | Liminar em Mandado de Seguranca |
| 2 | Deposito Judicial |
| 3 | Antecipacao de Tutela |
| 4 | Liminar em Medida Cautelar |
| 5 | Deposito Administrativo |
| 6 | Outros |

