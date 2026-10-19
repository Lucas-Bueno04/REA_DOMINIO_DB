# Módulo `contabil_transferencia`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `pmtransferencia_centro_custo_consultar` | consultar | pmtransferencia_centro_custo | empresa | ✔ |
| `pmtransferencia_centro_custo_obter` | obter | pmtransferencia_centro_custo | empresa, codigo | ✔ |
| `pmtransferencia_centro_custo_totais` | totais | pmtransferencia_centro_custo | empresa | ✔ |
| `pmtransferencia_conta_patrimonial_consultar` | consultar | pmtransferencia_conta_patrimonial | empresa | ✔ |
| `pmtransferencia_conta_patrimonial_obter` | obter | pmtransferencia_conta_patrimonial | empresa, codigo | ✔ |
| `pmtransferencia_conta_patrimonial_totais` | totais | pmtransferencia_conta_patrimonial | empresa | ✔ |
| `pmtransferencia_matriz_filial_consultar` | consultar | pmtransferencia_matriz_filial | empresa | ✔ |
| `pmtransferencia_matriz_filial_obter` | obter | pmtransferencia_matriz_filial | empresa, sequencial_transferencia | ✔ |
| `pmtransferencia_matriz_filial_totais` | totais | pmtransferencia_matriz_filial | empresa | ✔ |
| `pmtransferencia_matriz_filial_lancto_consultar` | consultar | pmtransferencia_matriz_filial_lancto | empresa | ✔ |
| `pmtransferencia_matriz_filial_lancto_obter` | obter | pmtransferencia_matriz_filial_lancto | empresa, transferencia_de_bens_entre_matriz_filia, empresa_do_lancamento_contabil, numero_do_lancamento_contabil | ✔ |
