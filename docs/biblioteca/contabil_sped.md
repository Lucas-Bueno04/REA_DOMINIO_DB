# Módulo `contabil_sped`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `ctsped_contabil_od_consultar` | consultar | ctsped_contabil_od | empresa | ✔ |
| `ctsped_contabil_od_obter` | obter | ctsped_contabil_od | empresa, sequencial_dos_outros_dados | ✔ |
| `ctsped_contabil_od_alteracao_plano_conta_consultar` | consultar | ctsped_contabil_od_alteracao_plano_conta | empresa | ✔ |
| `ctsped_contabil_od_alteracao_plano_conta_obter` | obter | ctsped_contabil_od_alteracao_plano_conta | empresa, sequencial_dos_outros_dados, sequencial | ✔ |
| `ctsped_contabil_od_alteracao_plano_conta_anterior_consultar` | consultar | ctsped_contabil_od_alteracao_plano_conta_anterior | empresa | ✔ |
| `ctsped_contabil_od_alteracao_plano_conta_anterior_obter` | obter | ctsped_contabil_od_alteracao_plano_conta_anterior | empresa, sequencial_dos_outros_dados, sequencial_da_tabela_pai, sequencial | ✔ |
| `ctsped_contabil_od_alteracao_plano_conta_anterior_totais` | totais | ctsped_contabil_od_alteracao_plano_conta_anterior | empresa | ✔ |
| `ctsped_contabil_od_signatario_consultar` | consultar | ctsped_contabil_od_signatario | empresa | ✔ |
| `ctsped_contabil_od_signatario_obter` | obter | ctsped_contabil_od_signatario | empresa, sequencial_dos_outros_dados, sequencial_do_signatario | ✔ |
| `ctsped_ecf_od_l200_consultar` | consultar | ctsped_ecf_od_l200 | empresa | ✔ |
| `ctsped_ecf_od_l200_obter` | obter | ctsped_ecf_od_l200 | empresa, sequencial, competencia | ✔ |
| `ctsped_ecf_od_l200_totais` | totais | ctsped_ecf_od_l200 | empresa | ✔ |
| `ctsped_ecf_od_m010_consultar` | consultar | ctsped_ecf_od_m010 | empresa | ✔ |
| `ctsped_ecf_od_m010_obter` | obter | ctsped_ecf_od_m010 | empresa, sequencial_outros_dados, codigo_da_parte_b_ou_base_negativa, tipo_da_conta_b_base_negativa_p_parte_b | ✔ |
| `ctsped_ecf_od_m010_totais` | totais | ctsped_ecf_od_m010 | empresa | ✔ |
| `ctsped_ecf_od_m410_consultar` | consultar | ctsped_ecf_od_m410 | empresa | ✔ |
| `ctsped_ecf_od_m410_obter` | obter | ctsped_ecf_od_m410 | empresa, sequencial_outros_dados, competencia, sequencial_interno, tipo_da_conta_b_base_negativa_p_parte_b | ✔ |
| `ctsped_ecf_od_m410_totais` | totais | ctsped_ecf_od_m410 | empresa | ✔ |
| `ctsped_ecf_od_m410_origem_importacao_consultar` | consultar | ctsped_ecf_od_m410_origem_importacao | empresa | ✔ |
| `ctsped_ecf_od_m410_origem_importacao_obter` | obter | ctsped_ecf_od_m410_origem_importacao | empresa, mes_competencia_da_origem, ano_competencia_da_origem, a_lacs_u_lalur, a_anual_m_mensal_t_trimestral | ✔ |
| `ctsped_ecf_od_w100_consultar` | consultar | ctsped_ecf_od_w100 | empresa | ✔ |
| `ctsped_ecf_od_w100_obter` | obter | ctsped_ecf_od_w100 | empresa, sequencial_outros_dados | ✔ |
| `ctsped_ecf_od_x360_consultar` | consultar | ctsped_ecf_od_x360 | empresa | ✔ |
| `ctsped_ecf_od_x360_obter` | obter | ctsped_ecf_od_x360 | empresa, sequencial, data_de_competencia | ✔ |
| `ctsped_ecf_od_x430_consultar` | consultar | ctsped_ecf_od_x430 | empresa | ✔ |
| `ctsped_ecf_od_x430_obter` | obter | ctsped_ecf_od_x430 | empresa, sequencial_outros_dados, sequencial_interno | ✔ |
| `ctsped_ecf_od_x430_totais` | totais | ctsped_ecf_od_x430 | empresa | ✔ |
| `ctsped_ecf_od_x450_consultar` | consultar | ctsped_ecf_od_x450 | empresa | ✔ |
| `ctsped_ecf_od_x450_obter` | obter | ctsped_ecf_od_x450 | empresa, sequencial_outros_dados, sequencial_interno | ✔ |
| `ctsped_ecf_od_x450_totais` | totais | ctsped_ecf_od_x450 | empresa | ✔ |
| `ctsped_ecf_od_x450_registro_consultar` | consultar | ctsped_ecf_od_x450_registro | empresa | ✔ |
| `ctsped_ecf_od_x450_registro_obter` | obter | ctsped_ecf_od_x450_registro | empresa, sequencial, pagamento_remessa_servico, competencia, registro, codigo_do_registro, vigencia_do_registro | ✔ |
| `ctsped_ecf_od_x450_registro_totais` | totais | ctsped_ecf_od_x450_registro | empresa | ✔ |
| `ctsped_ecf_od_y540_consultar` | consultar | ctsped_ecf_od_y540 | empresa | ✔ |
| `ctsped_ecf_od_y540_obter` | obter | ctsped_ecf_od_y540 | empresa, sequencial_outros_dados, sequencial_interno | ✔ |
| `ctsped_ecf_od_y540_totais` | totais | ctsped_ecf_od_y540 | empresa | ✔ |
| `ctsped_ecf_od_y570_consultar` | consultar | ctsped_ecf_od_y570 | empresa | ✔ |
| `ctsped_ecf_od_y570_obter` | obter | ctsped_ecf_od_y570 | empresa, sequencial_outros_dados, sequencial_interno | ✔ |
| `ctsped_ecf_od_y570_totais` | totais | ctsped_ecf_od_y570 | empresa | ✔ |
| `ctsped_ecf_od_y600_consultar` | consultar | ctsped_ecf_od_y600 | empresa | ✔ |
| `ctsped_ecf_od_y600_obter` | obter | ctsped_ecf_od_y600 | empresa, sequencial_outros_dados, sequencial_interno | ✔ |
| `ctsped_ecf_od_y600_totais` | totais | ctsped_ecf_od_y600 | empresa | ✔ |
| `ctsped_ecf_od_y612_consultar` | consultar | ctsped_ecf_od_y612 | empresa | ✔ |
| `ctsped_ecf_od_y612_obter` | obter | ctsped_ecf_od_y612 | empresa, sequencial_outros_dados, sequencial_interno | ✔ |
| `ctsped_ecf_od_y612_totais` | totais | ctsped_ecf_od_y612 | empresa | ✔ |
| `ctsped_ecf_od_y620_consultar` | consultar | ctsped_ecf_od_y620 | empresa | ✔ |
| `ctsped_ecf_od_y620_obter` | obter | ctsped_ecf_od_y620 | empresa, sequencial_outros_dados, sequencial_interno | ✔ |
| `ctsped_ecf_od_y620_totais` | totais | ctsped_ecf_od_y620 | empresa | ✔ |
| `ctsped_ecf_od_y671_consultar` | consultar | ctsped_ecf_od_y671 | empresa | ✔ |
| `ctsped_ecf_od_y671_obter` | obter | ctsped_ecf_od_y671 | empresa, sequencial_outros_dados | ✔ |
| `ctsped_ecf_od_y672_consultar` | consultar | ctsped_ecf_od_y672 | empresa | ✔ |
| `ctsped_ecf_od_y672_obter` | obter | ctsped_ecf_od_y672 | empresa, sequencial_outros_dados | ✔ |
| `ctsped_ecf_od_y672_totais` | totais | ctsped_ecf_od_y672 | empresa | ✔ |
| `ctsped_ecf_od_y720_consultar` | consultar | ctsped_ecf_od_y720 | empresa | ✔ |
| `ctsped_ecf_od_y720_obter` | obter | ctsped_ecf_od_y720 | empresa, sequencial_outros_dados | ✔ |
| `ctsped_ecf_od_y720_totais` | totais | ctsped_ecf_od_y720 | empresa | ✔ |
| `ctsped_ecf_od_y800_consultar` | consultar | ctsped_ecf_od_y800 | empresa | ✔ |
| `ctsped_ecf_od_y800_obter` | obter | ctsped_ecf_od_y800 | empresa, sequencial_outros_dados | ✔ |
