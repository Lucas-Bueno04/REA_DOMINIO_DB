# Módulo `financeiro_outros`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `hradiantamento_aproveitamento_consultar` | consultar | hradiantamento_aproveitamento | empresa | ✔ |
| `hradiantamento_aproveitamento_obter` | obter | hradiantamento_aproveitamento | empresa, adiantamento, faturamento, parcela, recebimento, evento, pago_pelo_escritorio_s_n | ✔ |
| `hradiantamento_aproveitamento_totais` | totais | hradiantamento_aproveitamento | empresa | ✔ |
| `hradiantamento_evento_consultar` | consultar | hradiantamento_evento | empresa | ✔ |
| `hradiantamento_evento_obter` | obter | hradiantamento_evento | empresa, adiantamento, evento | ✔ |
| `hradiantamento_lancto_consultar` | consultar | hradiantamento_lancto | empresa | ✔ |
| `hradiantamento_lancto_obter` | obter | hradiantamento_lancto | empresa, adiantamento, empresa_do_lancamento_contabil, numero_do_lancamento_contabil | ✔ |
| `hrcategoria_pagar_consultar` | consultar | hrcategoria_pagar | empresa | ✔ |
| `hrcategoria_pagar_obter` | obter | hrcategoria_pagar | empresa, codigo | ✔ |
| `hrcategoria_receber_consultar` | consultar | hrcategoria_receber | empresa | ✔ |
| `hrcategoria_receber_obter` | obter | hrcategoria_receber | empresa, codigo | ✔ |
| `hrclassificacao_tributaria_ibs_cbs_consultar` | consultar | hrclassificacao_tributaria_ibs_cbs | — | ✔ |
| `hrclassificacao_tributaria_ibs_cbs_obter` | obter | hrclassificacao_tributaria_ibs_cbs | codigo_da_classificacao_tributaria | ✔ |
| `hrcliente_conta_despesa_consultar` | consultar | hrcliente_conta_despesa | empresa | ✔ |
| `hrcliente_conta_despesa_obter` | obter | hrcliente_conta_despesa | empresa, cliente, evento | ✔ |
| `hrcliente_conta_despesa_totais` | totais | hrcliente_conta_despesa | empresa | ✔ |
| `hrcodigo_cancelamento_nfse_consultar` | consultar | hrcodigo_cancelamento_nfse | empresa | ✔ |
| `hrcodigo_cancelamento_nfse_obter` | obter | hrcodigo_cancelamento_nfse | empresa, codigo_de_cancelamento | ✔ |
| `hrconta_corrente_escritorio_impostos_consultar` | consultar | hrconta_corrente_escritorio_impostos | empresa | ✔ |
| `hrconta_corrente_escritorio_impostos_obter` | obter | hrconta_corrente_escritorio_impostos | empresa, codigo_movimentacao_financeira, sequencial | ✔ |
| `hrconta_corrente_escritorio_impostos_totais` | totais | hrconta_corrente_escritorio_impostos | empresa | ✔ |
| `hrconta_corrente_escritorio_lancto_consultar` | consultar | hrconta_corrente_escritorio_lancto | empresa | ✔ |
| `hrconta_corrente_escritorio_lancto_obter` | obter | hrconta_corrente_escritorio_lancto | empresa, conta_corrente_escritorio, empresa_do_lancamento_contabil, numero_do_lancamento_contabil | ✔ |
| `hrconta_financeira_intervalo_consultar` | consultar | hrconta_financeira_intervalo | empresa | ✔ |
| `hrconta_financeira_intervalo_obter` | obter | hrconta_financeira_intervalo | empresa, conta_financeira, codigo | ✔ |
| `hrcustos_geral_consultar` | consultar | hrcustos_geral | — | ✔ |
| `hrcustos_geral_obter` | obter | hrcustos_geral | chave | ✔ |
| `hrcustos_itens_automaticos_consultar` | consultar | hrcustos_itens_automaticos | — | ✔ |
| `hrcustos_itens_automaticos_obter` | obter | hrcustos_itens_automaticos | codigo_do_item_automatico | ✔ |
| `hrdocumento_ole_modelo_consultar` | consultar | hrdocumento_ole_modelo | — | ✔ |
| `hrdocumento_ole_modelo_obter` | obter | hrdocumento_ole_modelo | codigo, tipo | ✔ |
| `hrdocumento_ole_tipo_consultar` | consultar | hrdocumento_ole_tipo | — | ✔ |
| `hrdocumento_ole_tipo_obter` | obter | hrdocumento_ole_tipo | codigo | ✔ |
| `hrhistorico_consultar` | consultar | hrhistorico | empresa | ✔ |
| `hrhistorico_obter` | obter | hrhistorico | empresa, codigo | ✔ |
| `hrindicador_operacoes_ibs_cbs_consultar` | consultar | hrindicador_operacoes_ibs_cbs | — | ✔ |
| `hrindicador_operacoes_ibs_cbs_obter` | obter | hrindicador_operacoes_ibs_cbs | codigo_sequencial_do_registro | ✔ |
| `hrlote_nfse_consultar` | consultar | hrlote_nfse | empresa | ✔ |
| `hrlote_nfse_obter` | obter | hrlote_nfse | empresa, lote | ✔ |
| `hrnota_nfse_gerar_tag_cfps_cst_consultar` | consultar | hrnota_nfse_gerar_tag_cfps_cst | — | ✔ |
| `hrnota_nfse_gerar_tag_cfps_cst_obter` | obter | hrnota_nfse_gerar_tag_cfps_cst | codigo_do_municipio_srf, cst_codigos_de_situacao_tributaria, cfps_codigo_fiscal_de_prestacao_de_servi | ✔ |
| `hrnumero_utilizado_recebimento_consultar` | consultar | hrnumero_utilizado_recebimento | empresa | ✔ |
| `hrnumero_utilizado_recebimento_obter` | obter | hrnumero_utilizado_recebimento | empresa, numero | ✔ |
| `hrorcado_pagar_consultar` | consultar | hrorcado_pagar | empresa | ✔ |
| `hrorcado_pagar_obter` | obter | hrorcado_pagar | empresa, codigo | ✔ |
| `hrorcado_pagar_totais` | totais | hrorcado_pagar | empresa | ✔ |
| `hrpagamento_lancto_consultar` | consultar | hrpagamento_lancto | empresa | ✔ |
| `hrpagamento_lancto_obter` | obter | hrpagamento_lancto | empresa, lancamento_a_pagar, parcela, pagamento, empresa_do_lancamento_contabil, numero_do_lancamento_contabil | ✔ |
| `hrreajuste_contrato_consultar` | consultar | hrreajuste_contrato | empresa | ✔ |
| `hrreajuste_contrato_obter` | obter | hrreajuste_contrato | empresa, contrato, competencia | ✔ |
| `hrreajuste_contrato_totais` | totais | hrreajuste_contrato | empresa | ✔ |
| `hrrecebimento_lancto_consultar` | consultar | hrrecebimento_lancto | empresa | ✔ |
| `hrrecebimento_lancto_obter` | obter | hrrecebimento_lancto | empresa, faturamento, parcela, recebimento, empresa_do_lancamento_contabil, numero_do_lancamento_contabil | ✔ |
| `hrrenegociacao_faturamento_consultar` | consultar | hrrenegociacao_faturamento | empresa | ✔ |
| `hrrenegociacao_faturamento_obter` | obter | hrrenegociacao_faturamento | empresa, renegociacao, faturamento_origem, parcela_origem, faturamento_destino, parcela_destino | ✔ |
| `hrrenegociacao_recebimento_consultar` | consultar | hrrenegociacao_recebimento | empresa | ✔ |
| `hrrenegociacao_recebimento_obter` | obter | hrrenegociacao_recebimento | empresa, renegociacao, faturamento, parcela, recebimento | ✔ |
| `hrservico_prestado_consultar` | consultar | hrservico_prestado | empresa | ✔ |
| `hrservico_prestado_obter` | obter | hrservico_prestado | empresa, sequencial | ✔ |
| `hrtipo_contrato_consultar` | consultar | hrtipo_contrato | empresa | ✔ |
| `hrtipo_contrato_obter` | obter | hrtipo_contrato | empresa, codigo | ✔ |
| `hrurl_nfse_consultar` | consultar | hrurl_nfse | — | ✔ |
| `hrurl_nfse_obter` | obter | hrurl_nfse | codigo_do_municipio_da_secretaria_da_rec, acao_1_consulta_situacao_nfse_2_consulta, tipo_da_url_o_oficial_t_teste, vigencia_da_url | ✔ |
