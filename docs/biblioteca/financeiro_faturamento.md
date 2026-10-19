# Módulo `financeiro_faturamento`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `hrfaturamento_adicional_consultar` | consultar | hrfaturamento_adicional | empresa | ✔ |
| `hrfaturamento_adicional_obter` | obter | hrfaturamento_adicional | empresa, faturamento, contrato | ✔ |
| `hrfaturamento_adicional_totais` | totais | hrfaturamento_adicional | empresa | ✔ |
| `hrfaturamento_contrato_consultar` | consultar | hrfaturamento_contrato | empresa | ✔ |
| `hrfaturamento_contrato_obter` | obter | hrfaturamento_contrato | empresa, faturamento | ✔ |
| `hrfaturamento_contrato_totais` | totais | hrfaturamento_contrato | empresa | ✔ |
| `hrfaturamento_evento_consultar` | consultar | hrfaturamento_evento | empresa | ✔ |
| `hrfaturamento_evento_obter` | obter | hrfaturamento_evento | empresa, faturamento, cliente, lancamento_receber | ✔ |
| `hrfaturamento_evento_totais` | totais | hrfaturamento_evento | empresa | ✔ |
| `hrfaturamento_evento_renegociacao_consultar` | consultar | hrfaturamento_evento_renegociacao | empresa | ✔ |
| `hrfaturamento_evento_renegociacao_obter` | obter | hrfaturamento_evento_renegociacao | empresa, faturamento, evento, pago_pelo_escritorio_s_n | ✔ |
| `hrfaturamento_evento_renegociacao_totais` | totais | hrfaturamento_evento_renegociacao | empresa | ✔ |
| `hrfaturamento_lancto_consultar` | consultar | hrfaturamento_lancto | empresa | ✔ |
| `hrfaturamento_lancto_obter` | obter | hrfaturamento_lancto | empresa, faturamento, empresa_do_lancamento_contabil, numero_do_lancamento_contabil | ✔ |
| `hrfaturamento_parcela_emissao_consultar` | consultar | hrfaturamento_parcela_emissao | empresa | ✔ |
| `hrfaturamento_parcela_emissao_obter` | obter | hrfaturamento_parcela_emissao | empresa, faturamento, parcela, tipo_do_relatorio_b_boleto_d_documento_d, data_e_hora_da_emissao_ou_da_exclusao, acao_e_emissao_x_exclusao | ✔ |
| `hrfaturamento_parcela_item_detalhamento_consultar` | consultar | hrfaturamento_parcela_item_detalhamento | empresa | ✔ |
| `hrfaturamento_parcela_item_detalhamento_obter` | obter | hrfaturamento_parcela_item_detalhamento | empresa, faturamento, parcela, evento, sequencial, pago_pelo_escritorio_s_n | ✔ |
| `hrfaturamento_parcela_item_detalhamento_totais` | totais | hrfaturamento_parcela_item_detalhamento | empresa | ✔ |
