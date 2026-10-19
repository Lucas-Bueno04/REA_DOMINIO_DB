# Módulo `contabil_tabela`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `cttabela_diops_od_registro_consultar` | consultar | cttabela_diops_od_registro | — | ✔ |
| `cttabela_diops_od_registro_obter` | obter | cttabela_diops_od_registro | registro, codigo_do_registro, vigencia_do_registro | ✔ |
| `cttabela_natureza_subconta_correlata_consultar` | consultar | cttabela_natureza_subconta_correlata | — | ✔ |
| `cttabela_natureza_subconta_correlata_obter` | obter | cttabela_natureza_subconta_correlata | codigo | ✔ |
| `cttabela_sped_ecf_jurisdicao_consultar` | consultar | cttabela_sped_ecf_jurisdicao | — | ✔ |
| `cttabela_sped_ecf_jurisdicao_obter` | obter | cttabela_sped_ecf_jurisdicao | sequencial | ✔ |
| `cttabela_sped_ecf_natureza_operacao_consultar` | consultar | cttabela_sped_ecf_natureza_operacao | — | ✔ |
| `cttabela_sped_ecf_natureza_operacao_obter` | obter | cttabela_sped_ecf_natureza_operacao | codigo_da_natureza, data_de_inicio | ✔ |
| `cttabela_sped_ecf_receita_consultar` | consultar | cttabela_sped_ecf_receita | — | ✔ |
| `cttabela_sped_ecf_receita_obter` | obter | cttabela_sped_ecf_receita | codigo_da_receita | ✔ |
| `cttabela_sped_ecf_tipo_moeda_consultar` | consultar | cttabela_sped_ecf_tipo_moeda | — | ✔ |
| `cttabela_sped_ecf_tipo_moeda_obter` | obter | cttabela_sped_ecf_tipo_moeda | sequencial | ✔ |
| `cttabela_x300_cnc_consultar` | consultar | cttabela_x300_cnc | — | ✔ |
| `cttabela_x300_cnc_obter` | obter | cttabela_x300_cnc | sequencial | ✔ |
| `lrtabela_grupo_adicao_lucro_exploracao_consultar` | consultar | lrtabela_grupo_adicao_lucro_exploracao | — | ✔ |
| `lrtabela_grupo_adicao_lucro_exploracao_obter` | obter | lrtabela_grupo_adicao_lucro_exploracao | codigo | ✔ |
| `lrtabela_grupo_adicao_lucro_exploracao_vigencia_consultar` | consultar | lrtabela_grupo_adicao_lucro_exploracao_vigencia | — | ✔ |
| `lrtabela_grupo_adicao_lucro_exploracao_vigencia_obter` | obter | lrtabela_grupo_adicao_lucro_exploracao_vigencia | codigo_sequencial_com_referencia_a_tabel, vigencia_da_descricao | ✔ |
| `lrtabela_grupo_csll_adicao_geral_consultar` | consultar | lrtabela_grupo_csll_adicao_geral | — | ✔ |
| `lrtabela_grupo_csll_adicao_geral_obter` | obter | lrtabela_grupo_csll_adicao_geral | codigo | ✔ |
| `lrtabela_grupo_csll_adicao_geral_vigencia_consultar` | consultar | lrtabela_grupo_csll_adicao_geral_vigencia | — | ✔ |
| `lrtabela_grupo_csll_adicao_geral_vigencia_obter` | obter | lrtabela_grupo_csll_adicao_geral_vigencia | codigo_sequencial_com_referencia_a_tabel, vigencia_da_descricao | ✔ |
| `lrtabela_grupo_csll_adicao_seguradora_consultar` | consultar | lrtabela_grupo_csll_adicao_seguradora | — | ✔ |
| `lrtabela_grupo_csll_adicao_seguradora_obter` | obter | lrtabela_grupo_csll_adicao_seguradora | codigo | ✔ |
| `lrtabela_grupo_csll_adicao_seguradora_vigencia_consultar` | consultar | lrtabela_grupo_csll_adicao_seguradora_vigencia | — | ✔ |
| `lrtabela_grupo_csll_adicao_seguradora_vigencia_obter` | obter | lrtabela_grupo_csll_adicao_seguradora_vigencia | codigo_sequencial_com_referencia_a_tabel, vigencia_da_descricao | ✔ |
| `lrtabela_grupo_csll_adicao_sistema_financeiro_consultar` | consultar | lrtabela_grupo_csll_adicao_sistema_financeiro | — | ✔ |
| `lrtabela_grupo_csll_adicao_sistema_financeiro_obter` | obter | lrtabela_grupo_csll_adicao_sistema_financeiro | codigo | ✔ |
| `lrtabela_grupo_csll_adicao_sistema_financeiro_vigencia_consultar` | consultar | lrtabela_grupo_csll_adicao_sistema_financeiro_vigencia | — | ✔ |
| `lrtabela_grupo_csll_adicao_sistema_financeiro_vigencia_obter` | obter | lrtabela_grupo_csll_adicao_sistema_financeiro_vigencia | codigo_sequencial_com_referencia_a_tabel, vigencia_da_descricao | ✔ |
| `lrtabela_grupo_csll_exclusao_geral_consultar` | consultar | lrtabela_grupo_csll_exclusao_geral | — | ✔ |
| `lrtabela_grupo_csll_exclusao_geral_obter` | obter | lrtabela_grupo_csll_exclusao_geral | codigo | ✔ |
| `lrtabela_grupo_csll_exclusao_geral_vigencia_consultar` | consultar | lrtabela_grupo_csll_exclusao_geral_vigencia | — | ✔ |
| `lrtabela_grupo_csll_exclusao_geral_vigencia_obter` | obter | lrtabela_grupo_csll_exclusao_geral_vigencia | codigo_sequencial_com_referencia_a_tabel, vigencia_da_descricao | ✔ |
| `lrtabela_grupo_csll_exclusao_seguradora_consultar` | consultar | lrtabela_grupo_csll_exclusao_seguradora | — | ✔ |
| `lrtabela_grupo_csll_exclusao_seguradora_obter` | obter | lrtabela_grupo_csll_exclusao_seguradora | codigo | ✔ |
| `lrtabela_grupo_csll_exclusao_seguradora_vigencia_consultar` | consultar | lrtabela_grupo_csll_exclusao_seguradora_vigencia | — | ✔ |
| `lrtabela_grupo_csll_exclusao_seguradora_vigencia_obter` | obter | lrtabela_grupo_csll_exclusao_seguradora_vigencia | codigo_sequencial_com_referencia_a_tabel, vigencia_da_descricao | ✔ |
| `lrtabela_grupo_csll_exclusao_sistema_financeiro_consultar` | consultar | lrtabela_grupo_csll_exclusao_sistema_financeiro | — | ✔ |
| `lrtabela_grupo_csll_exclusao_sistema_financeiro_obter` | obter | lrtabela_grupo_csll_exclusao_sistema_financeiro | codigo | ✔ |
| `lrtabela_grupo_csll_exclusao_sistema_financeiro_v_3ee8_consultar` | consultar | lrtabela_grupo_csll_exclusao_sistema_financeiro_vigencia | — | ✔ |
| `lrtabela_grupo_csll_exclusao_sistema_financeiro_vigencia_obter` | obter | lrtabela_grupo_csll_exclusao_sistema_financeiro_vigencia | codigo_sequencial_com_referencia_a_tabel, vigencia_da_descricao | ✔ |
| `lrtabela_grupo_dirbi_consultar` | consultar | lrtabela_grupo_dirbi | — | ✔ |
| `lrtabela_grupo_dirbi_obter` | obter | lrtabela_grupo_dirbi | codigo_grupo_dirbi | ✔ |
| `lrtabela_grupo_ecf_csll_dirbi_consultar` | consultar | lrtabela_grupo_ecf_csll_dirbi | — | ✔ |
| `lrtabela_grupo_ecf_csll_dirbi_obter` | obter | lrtabela_grupo_ecf_csll_dirbi | codigo_grupo_dirbi, codigo_ecf, tipo_grupo_ecf | ✔ |
| `lrtabela_grupo_ecf_irpj_dirbi_consultar` | consultar | lrtabela_grupo_ecf_irpj_dirbi | — | ✔ |
| `lrtabela_grupo_ecf_irpj_dirbi_obter` | obter | lrtabela_grupo_ecf_irpj_dirbi | codigo_grupo_dirbi, codigo_ecf, tipo_grupo_ecf | ✔ |
| `lrtabela_grupo_exclusao_lucro_exploracao_consultar` | consultar | lrtabela_grupo_exclusao_lucro_exploracao | — | ✔ |
| `lrtabela_grupo_exclusao_lucro_exploracao_obter` | obter | lrtabela_grupo_exclusao_lucro_exploracao | codigo | ✔ |
| `lrtabela_grupo_exclusao_lucro_exploracao_vigencia_consultar` | consultar | lrtabela_grupo_exclusao_lucro_exploracao_vigencia | — | ✔ |
| `lrtabela_grupo_exclusao_lucro_exploracao_vigencia_obter` | obter | lrtabela_grupo_exclusao_lucro_exploracao_vigencia | codigo_sequencial_com_referencia_a_tabel, vigencia_da_descricao | ✔ |
| `lrtabela_grupo_irpj_adicao_geral_consultar` | consultar | lrtabela_grupo_irpj_adicao_geral | — | ✔ |
| `lrtabela_grupo_irpj_adicao_geral_obter` | obter | lrtabela_grupo_irpj_adicao_geral | codigo | ✔ |
| `lrtabela_grupo_irpj_adicao_geral_vigencia_consultar` | consultar | lrtabela_grupo_irpj_adicao_geral_vigencia | — | ✔ |
| `lrtabela_grupo_irpj_adicao_geral_vigencia_obter` | obter | lrtabela_grupo_irpj_adicao_geral_vigencia | codigo_sequencial_com_referencia_a_tabel, vigencia_da_descricao | ✔ |
| `lrtabela_grupo_irpj_adicao_seguradora_consultar` | consultar | lrtabela_grupo_irpj_adicao_seguradora | — | ✔ |
| `lrtabela_grupo_irpj_adicao_seguradora_obter` | obter | lrtabela_grupo_irpj_adicao_seguradora | codigo | ✔ |
| `lrtabela_grupo_irpj_adicao_seguradora_vigencia_consultar` | consultar | lrtabela_grupo_irpj_adicao_seguradora_vigencia | — | ✔ |
| `lrtabela_grupo_irpj_adicao_seguradora_vigencia_obter` | obter | lrtabela_grupo_irpj_adicao_seguradora_vigencia | codigo_sequencial_com_referencia_a_tabel, vigencia_da_descricao | ✔ |
| `lrtabela_grupo_irpj_adicao_sistema_financeiro_consultar` | consultar | lrtabela_grupo_irpj_adicao_sistema_financeiro | — | ✔ |
| `lrtabela_grupo_irpj_adicao_sistema_financeiro_obter` | obter | lrtabela_grupo_irpj_adicao_sistema_financeiro | codigo | ✔ |
| `lrtabela_grupo_irpj_adicao_sistema_financeiro_vigencia_consultar` | consultar | lrtabela_grupo_irpj_adicao_sistema_financeiro_vigencia | — | ✔ |
| `lrtabela_grupo_irpj_adicao_sistema_financeiro_vigencia_obter` | obter | lrtabela_grupo_irpj_adicao_sistema_financeiro_vigencia | codigo_sequencial_com_referencia_a_tabel, vigencia_da_descricao | ✔ |
| `lrtabela_grupo_irpj_exclusao_geral_consultar` | consultar | lrtabela_grupo_irpj_exclusao_geral | — | ✔ |
| `lrtabela_grupo_irpj_exclusao_geral_obter` | obter | lrtabela_grupo_irpj_exclusao_geral | codigo | ✔ |
| `lrtabela_grupo_irpj_exclusao_geral_vigencia_consultar` | consultar | lrtabela_grupo_irpj_exclusao_geral_vigencia | — | ✔ |
| `lrtabela_grupo_irpj_exclusao_geral_vigencia_obter` | obter | lrtabela_grupo_irpj_exclusao_geral_vigencia | codigo_sequencial_com_referencia_a_tabel, vigencia_da_descricao | ✔ |
| `lrtabela_grupo_irpj_exclusao_seguradora_consultar` | consultar | lrtabela_grupo_irpj_exclusao_seguradora | — | ✔ |
| `lrtabela_grupo_irpj_exclusao_seguradora_obter` | obter | lrtabela_grupo_irpj_exclusao_seguradora | codigo | ✔ |
| `lrtabela_grupo_irpj_exclusao_seguradora_vigencia_consultar` | consultar | lrtabela_grupo_irpj_exclusao_seguradora_vigencia | — | ✔ |
| `lrtabela_grupo_irpj_exclusao_seguradora_vigencia_obter` | obter | lrtabela_grupo_irpj_exclusao_seguradora_vigencia | codigo_sequencial_com_referencia_a_tabel, vigencia_da_descricao | ✔ |
| `lrtabela_grupo_irpj_exclusao_sistema_financeiro_consultar` | consultar | lrtabela_grupo_irpj_exclusao_sistema_financeiro | — | ✔ |
| `lrtabela_grupo_irpj_exclusao_sistema_financeiro_obter` | obter | lrtabela_grupo_irpj_exclusao_sistema_financeiro | codigo | ✔ |
| `lrtabela_grupo_irpj_exclusao_sistema_financeiro_v_497b_consultar` | consultar | lrtabela_grupo_irpj_exclusao_sistema_financeiro_vigencia | — | ✔ |
| `lrtabela_grupo_irpj_exclusao_sistema_financeiro_vigencia_obter` | obter | lrtabela_grupo_irpj_exclusao_sistema_financeiro_vigencia | codigo_sequencial_com_referencia_a_tabel, vigencia_da_descricao | ✔ |
| `lrtabela_padrao_rfb_parte_b_consultar` | consultar | lrtabela_padrao_rfb_parte_b | — | ✔ |
| `lrtabela_padrao_rfb_parte_b_obter` | obter | lrtabela_padrao_rfb_parte_b | sequencial | ✔ |
