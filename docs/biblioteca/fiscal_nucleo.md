# Módulo `fiscal_nucleo`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `atferiados_consultar` | consultar | atferiados | — | ✔ |
| `atferiados_obter` | obter | atferiados | data | ✔ |
| `atmovimp_consultar` | consultar | atmovimp | empresa | ✔ |
| `atmovimp_totais` | totais | atmovimp | empresa | ✔ |
| `attab13_consultar` | consultar | attab13 | — | ✔ |
| `attab13_obter` | obter | attab13 | competencia | ✔ |
| `attabinss_consultar` | consultar | attabinss | — | ✔ |
| `attabinss_obter` | obter | attabinss | competencia | ✔ |
| `attabinss_totais` | totais | attabinss | — | ✔ |
| `efalespecies_consultar` | consultar | efalespecies | — | ✔ |
| `efalespecies_obter` | obter | efalespecies | codigo | ✔ |
| `efapuracao_consultar` | consultar | efapuracao | empresa | ✔ |
| `efapuracao_obter` | obter | efapuracao | empresa, data_da_apuracao | ✔ |
| `efcalculando_consultar` | consultar | efcalculando | empresa | ✔ |
| `efcalculando_obter` | obter | efcalculando | empresa, usuario, identificador_da_conexao | ✔ |
| `efceespecies_consultar` | consultar | efceespecies | — | ✔ |
| `efceespecies_obter` | obter | efceespecies | codigo | ✔ |
| `efcfghistorico_consultar` | consultar | efcfghistorico | empresa | ✔ |
| `efcfghistorico_obter` | obter | efcfghistorico | empresa, tipo_1_entradas_2_entradas_sintetica_3_e | ✔ |
| `efconversao_consultar` | consultar | efconversao | — | ✔ |
| `efconversao_obter` | obter | efconversao | indica_como_esta_o_processo_de_conversao | ✔ |
| `efdesenvolve_consultar` | consultar | efdesenvolve | empresa | ✔ |
| `efdesenvolve_obter` | obter | efdesenvolve | empresa, sequencial | ✔ |
| `efestados_consultar` | consultar | efestados | — | ✔ |
| `efestados_obter` | obter | efestados | sigla | ✔ |
| `efexclusoes_consultar` | consultar | efexclusoes | — | ✔ |
| `efexclusoes_obter` | obter | efexclusoes | codigo | ✔ |
| `efgrupopdi_consultar` | consultar | efgrupopdi | empresa | ✔ |
| `efgrupopdi_obter` | obter | efgrupopdi | empresa, codigo | ✔ |
| `efimoveis_consultar` | consultar | efimoveis | empresa | ✔ |
| `efimoveis_obter` | obter | efimoveis | empresa, codigo_do_imovel | ✔ |
| `efimportando_consultar` | consultar | efimportando | empresa | ✔ |
| `efimportando_obter` | obter | efimportando | empresa, usuario, tabela_que_esta_sendo_importada, identificador_da_conexao | ✔ |
| `efincentivosmuni_consultar` | consultar | efincentivosmuni | — | ✔ |
| `efincentivosmuni_obter` | obter | efincentivosmuni | codigo_do_municipio_federal, sigla_do_estado, vigencia | ✔ |
| `efindices_consultar` | consultar | efindices | — | ✔ |
| `efindices_obter` | obter | efindices | data, codigo | ✔ |
| `efindices_totais` | totais | efindices | — | ✔ |
| `efindmed_consultar` | consultar | efindmed | — | ✔ |
| `efindmed_obter` | obter | efindmed | data_ind, codigo | ✔ |
| `efindmed_totais` | totais | efindmed | — | ✔ |
| `efmaqecf_consultar` | consultar | efmaqecf | empresa | ✔ |
| `efmaqecf_obter` | obter | efmaqecf | empresa, codi_mec | ✔ |
| `efmaqecf_totais` | totais | efmaqecf | empresa | ✔ |
| `efmgexclusoes_consultar` | consultar | efmgexclusoes | — | ✔ |
| `efmgexclusoes_obter` | obter | efmgexclusoes | tipo_da_exclusao_e_entradas_s_saidas, regime_da_exclusao_2_me_4_epp, codigo | ✔ |
| `efmgtransferencias_consultar` | consultar | efmgtransferencias | — | ✔ |
| `efmgtransferencias_obter` | obter | efmgtransferencias | codigo | ✔ |
| `efmovacu_consultar` | consultar | efmovacu | empresa | ✔ |
| `efmovacu_obter` | obter | efmovacu | empresa, codigo | ✔ |
| `efmovacu_totais` | totais | efmovacu | empresa | ✔ |
| `efmovaju_consultar` | consultar | efmovaju | empresa | ✔ |
| `efmovaju_obter` | obter | efmovaju | empresa, ajuste, data | ✔ |
| `efmovaju_totais` | totais | efmovaju | empresa | ✔ |
| `efmtisentas_consultar` | consultar | efmtisentas | — | ✔ |
| `efmtisentas_obter` | obter | efmtisentas | codigo | ✔ |
| `efmunici_consultar` | consultar | efmunici | — | ✔ |
| `efmunici_obter` | obter | efmunici | codigo | ✔ |
| `efmunifederal_consultar` | consultar | efmunifederal | — | ✔ |
| `efmunifederal_obter` | obter | efmunifederal | estado, codigo | ✔ |
| `efmvvpro_consultar` | consultar | efmvvpro | empresa | ✔ |
| `efmvvpro_obter` | obter | efmvvpro | empresa, codigo, sequencial | ✔ |
| `efmvvpro_totais` | totais | efmvvpro | empresa | ✔ |
| `efnbs_consultar` | consultar | efnbs | — | ✔ |
| `efnbs_obter` | obter | efnbs | nbs | ✔ |
| `efncm_consultar` | consultar | efncm | — | ✔ |
| `efncm_obter` | obter | efncm | ncm | ✔ |
| `efobsnota_consultar` | consultar | efobsnota | empresa | ✔ |
| `efobsnota_obter` | obter | efobsnota | empresa, codigo | ✔ |
| `efsdosubtri_consultar` | consultar | efsdosubtri | empresa | ✔ |
| `efsdosubtri_obter` | obter | efsdosubtri | empresa, imposto, competencia, pdic_sim, estado | ✔ |
| `efsdosubtri_totais` | totais | efsdosubtri | empresa | ✔ |
| `eftabaju_consultar` | consultar | eftabaju | empresa | ✔ |
| `eftabaju_obter` | obter | eftabaju | empresa, ajuste, codigo, cnpj, data | ✔ |
| `eftabaju_totais` | totais | eftabaju | empresa | ✔ |
| `eftabelamuni_consultar` | consultar | eftabelamuni | — | ✔ |
| `eftabelamuni_obter` | obter | eftabelamuni | codigo | ✔ |
| `eftabelas_consultar` | consultar | eftabelas | — | ✔ |
| `eftabelas_obter` | obter | eftabelas | codigo, vigencia | ✔ |
| `eftabfax_consultar` | consultar | eftabfax | — | ✔ |
| `eftabfax_obter` | obter | eftabfax | codigo_da_tabela, vigencia, faixa | ✔ |
| `efunidades_consultar` | consultar | efunidades | — | ✔ |
| `efunidades_obter` | obter | efunidades | codigo | ✔ |
