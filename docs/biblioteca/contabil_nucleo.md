# Módulo `contabil_nucleo`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `ctabreviaturas_consultar` | consultar | ctabreviaturas | empresa | ✔ |
| `ctabreviaturas_obter` | obter | ctabreviaturas | empresa, sequencial | ✔ |
| `ctbaklanctodfc_consultar` | consultar | ctbaklanctodfc | empresa | ✔ |
| `ctbaklanctodfc_obter` | obter | ctbaklanctodfc | empresa, codigo_do_lote, sequencial | ✔ |
| `ctbaklanctodfc_totais` | totais | ctbaklanctodfc | empresa | ✔ |
| `ctbaklanctodmpl_consultar` | consultar | ctbaklanctodmpl | empresa | ✔ |
| `ctbaklanctodmpl_obter` | obter | ctbaklanctodmpl | empresa, numero_lancamento, codigo_tipo_lancamento | ✔ |
| `ctbaklanctodmpl_totais` | totais | ctbaklanctodmpl | empresa | ✔ |
| `ctbaklanctolote_consultar` | consultar | ctbaklanctolote | empresa | ✔ |
| `ctbaklanctolote_obter` | obter | ctbaklanctolote | empresa, codigo | ✔ |
| `ctbalancosocial_consultar` | consultar | ctbalancosocial | empresa | ✔ |
| `ctbalancosocial_obter` | obter | ctbalancosocial | empresa, codigo_do_item | ✔ |
| `ctcoeficiente_consultar` | consultar | ctcoeficiente | — | ✔ |
| `ctcoeficiente_obter` | obter | ctcoeficiente | codigo | ✔ |
| `ctcontacaixa_consultar` | consultar | ctcontacaixa | empresa | ✔ |
| `ctcontacaixa_obter` | obter | ctcontacaixa | empresa, conta | ✔ |
| `ctcrateio_consultar` | consultar | ctcrateio | empresa | ✔ |
| `ctcrateio_obter` | obter | ctcrateio | empresa, centro_de_custo, conta_contabil, filial | ✔ |
| `ctgruposdmpl_consultar` | consultar | ctgruposdmpl | empresa | ✔ |
| `ctgruposdmpl_obter` | obter | ctgruposdmpl | empresa, codigo_grupo | ✔ |
| `ctgruposdra_consultar` | consultar | ctgruposdra | empresa | ✔ |
| `ctgruposdra_obter` | obter | ctgruposdra | empresa, codigo | ✔ |
| `ctgruposdsp_consultar` | consultar | ctgruposdsp | empresa | ✔ |
| `ctgruposdsp_obter` | obter | ctgruposdsp | empresa, codigo | ✔ |
| `ctgruposdsp_totais` | totais | ctgruposdsp | empresa | ✔ |
| `ctgruposdva_consultar` | consultar | ctgruposdva | empresa | ✔ |
| `ctgruposdva_obter` | obter | ctgruposdva | empresa, codigo | ✔ |
| `ctidiomas_consultar` | consultar | ctidiomas | — | ✔ |
| `ctidiomas_obter` | obter | ctidiomas | codigo | ✔ |
| `ctlanctodfc_consultar` | consultar | ctlanctodfc | empresa | ✔ |
| `ctlanctodfc_obter` | obter | ctlanctodfc | empresa, codigo_do_lote, sequencial | ✔ |
| `ctlanctodfc_totais` | totais | ctlanctodfc | empresa | ✔ |
| `ctlanctodmpl_consultar` | consultar | ctlanctodmpl | empresa | ✔ |
| `ctlanctodmpl_obter` | obter | ctlanctodmpl | empresa, numero_lancamento, codigo_tipo_lancamento | ✔ |
| `ctlanctodmpl_totais` | totais | ctlanctodmpl | empresa | ✔ |
| `ctplanocontas_consultar` | consultar | ctplanocontas | empresa | ✔ |
| `ctplanocontas_obter` | obter | ctplanocontas | empresa, codigo, codigo_do_plano_de_contas_1_antigo_2_nov | ✔ |
| `ctresumobal_consultar` | consultar | ctresumobal | empresa | ✔ |
| `ctresumobal_obter` | obter | ctresumobal | empresa, filtro_ordem | ✔ |
| `cttipolancto_consultar` | consultar | cttipolancto | empresa | ✔ |
| `cttipolancto_obter` | obter | cttipolancto | empresa, codigo_tipo_lancamento | ✔ |
| `ctzeramento_consultar` | consultar | ctzeramento | empresa | ✔ |
| `ctzeramento_obter` | obter | ctzeramento | empresa, conta | ✔ |
| `lacsadex_consultar` | consultar | lacsadex | empresa | ✔ |
| `lacsadex_obter` | obter | lacsadex | empresa, codigo_da_adicao_e_exclusao | ✔ |
| `lacsaliquotas_consultar` | consultar | lacsaliquotas | empresa | ✔ |
| `lacsaliquotas_obter` | obter | lacsaliquotas | empresa, data_que_inicia | ✔ |
| `lacsaliquotas_totais` | totais | lacsaliquotas | empresa | ✔ |
| `lairadex_consultar` | consultar | lairadex | empresa | ✔ |
| `lairadex_obter` | obter | lairadex | empresa, codigo_adicao_ou_exclusao | ✔ |
| `lairadexrel_consultar` | consultar | lairadexrel | empresa | ✔ |
| `lairadexrel_obter` | obter | lairadexrel | empresa, codigo_adicao_ou_exclusao, codigo_relacionamento | ✔ |
| `lairgruposadex_consultar` | consultar | lairgruposadex | — | ✔ |
| `lairgruposadex_obter` | obter | lairgruposadex | grupo | ✔ |
| `lairincentivo_consultar` | consultar | lairincentivo | — | ✔ |
| `lairincentivo_obter` | obter | lairincentivo | incentivo | ✔ |
| `lairparteb_consultar` | consultar | lairparteb | — | ✔ |
| `lairparteb_obter` | obter | lairparteb | codigo_parte_b | ✔ |
| `laparmto_consultar` | consultar | laparmto | empresa | ✔ |
| `lradicao_consultar` | consultar | lradicao | empresa | ✔ |
| `lradicao_obter` | obter | lradicao | empresa, codigo | ✔ |
| `lrconversao_consultar` | consultar | lrconversao | — | ✔ |
| `lrexclusao_consultar` | consultar | lrexclusao | empresa | ✔ |
| `lrexclusao_obter` | obter | lrexclusao | empresa, codigo | ✔ |
| `lrganho_consultar` | consultar | lrganho | empresa | ✔ |
| `lrganho_obter` | obter | lrganho | empresa, codigo | ✔ |
| `lrparametro_consultar` | consultar | lrparametro | empresa | ✔ |
| `pabasicm_consultar` | consultar | pabasicm | empresa | ✔ |
| `pabasicm_obter` | obter | pabasicm | empresa, bem, competencia | ✔ |
| `pabasicm_totais` | totais | pabasicm | empresa | ✔ |
| `pacalmes_consultar` | consultar | pacalmes | empresa | ✔ |
| `pacalmes_obter` | obter | pacalmes | empresa, bem, competencia_do_calculo, tipo | ✔ |
| `pacalmes_totais` | totais | pacalmes | empresa | ✔ |
| `pacfghistorico_consultar` | consultar | pacfghistorico | empresa | ✔ |
| `pacfghistorico_obter` | obter | pacfghistorico | empresa, tipo_1_correcao_do_periodo_2_depreciacao | ✔ |
| `pacontas_consultar` | consultar | pacontas | empresa | ✔ |
| `pacontas_obter` | obter | pacontas | empresa, codigo | ✔ |
| `pacontas_totais` | totais | pacontas | empresa | ✔ |
| `padadfat_consultar` | consultar | padadfat | empresa | ✔ |
| `padadfat_obter` | obter | padadfat | empresa, data | ✔ |
| `padadfat_totais` | totais | padadfat | empresa | ✔ |
| `pagrucon_consultar` | consultar | pagrucon | empresa | ✔ |
| `pagrucon_obter` | obter | pagrucon | empresa, codigo | ✔ |
| `paparmto_consultar` | consultar | paparmto | empresa | ✔ |
| `pmbaixa_consultar` | consultar | pmbaixa | empresa | ✔ |
| `pmbaixa_obter` | obter | pmbaixa | empresa, codigo | ✔ |
| `pmbaixa_totais` | totais | pmbaixa | empresa | ✔ |
| `pmcalculo_consultar` | consultar | pmcalculo | empresa | ✔ |
| `pmcalculo_obter` | obter | pmcalculo | empresa, codigo | ✔ |
| `pmconversao_consultar` | consultar | pmconversao | — | ✔ |
| `pmhistorico_consultar` | consultar | pmhistorico | empresa | ✔ |
| `pmhistorico_obter` | obter | pmhistorico | empresa, codigo | ✔ |
| `pmparametro_consultar` | consultar | pmparametro | empresa | ✔ |
| `pmparametro_totais` | totais | pmparametro | empresa | ✔ |
