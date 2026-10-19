# Módulo `financeiro_lancamento`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `hrlancamento_desconto_consultar` | consultar | hrlancamento_desconto | empresa | ✔ |
| `hrlancamento_desconto_obter` | obter | hrlancamento_desconto | empresa, cliente, codigo | ✔ |
| `hrlancamento_desconto_totais` | totais | hrlancamento_desconto | empresa | ✔ |
| `hrlancamento_pagar_consultar` | consultar | hrlancamento_pagar | empresa | ✔ |
| `hrlancamento_pagar_obter` | obter | hrlancamento_pagar | empresa, codigo | ✔ |
| `hrlancamento_pagar_totais` | totais | hrlancamento_pagar | empresa | ✔ |
| `hrlancamento_pagar_lancto_consultar` | consultar | hrlancamento_pagar_lancto | empresa | ✔ |
| `hrlancamento_pagar_lancto_obter` | obter | hrlancamento_pagar_lancto | empresa, lancamento_a_pagar, empresa_do_lancamento_contabil, numero_do_lancamento_contabil | ✔ |
| `hrlancamento_pagar_parcela_consultar` | consultar | hrlancamento_pagar_parcela | empresa | ✔ |
| `hrlancamento_pagar_parcela_obter` | obter | hrlancamento_pagar_parcela | empresa, lancamento_a_pagar, codigo | ✔ |
| `hrlancamento_pagar_parcela_totais` | totais | hrlancamento_pagar_parcela | empresa | ✔ |
| `hrlancamento_receber_consultar` | consultar | hrlancamento_receber | empresa | ✔ |
| `hrlancamento_receber_obter` | obter | hrlancamento_receber | empresa, cliente, codigo | ✔ |
| `hrlancamento_receber_totais` | totais | hrlancamento_receber | empresa | ✔ |
| `hrlancamento_receber_competencia_consultar` | consultar | hrlancamento_receber_competencia | empresa | ✔ |
| `hrlancamento_receber_competencia_obter` | obter | hrlancamento_receber_competencia | empresa, cliente, lancamento_receber, mes_de_faturamento | ✔ |
