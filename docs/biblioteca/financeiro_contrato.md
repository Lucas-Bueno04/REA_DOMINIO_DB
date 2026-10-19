# Módulo `financeiro_contrato`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `hrcontrato_adicional_competencia_consultar` | consultar | hrcontrato_adicional_competencia | empresa | ✔ |
| `hrcontrato_adicional_competencia_obter` | obter | hrcontrato_adicional_competencia | empresa, contrato, mes_de_faturamento | ✔ |
| `hrcontrato_alteracao_consultar` | consultar | hrcontrato_alteracao | empresa | ✔ |
| `hrcontrato_alteracao_obter` | obter | hrcontrato_alteracao | empresa, codigo_do_contrato, data_da_alteracao, campo_alterado | ✔ |
| `hrcontrato_alteracao_campos_consultar` | consultar | hrcontrato_alteracao_campos | — | ✔ |
| `hrcontrato_alteracao_campos_obter` | obter | hrcontrato_alteracao_campos | codigo_do_campo | ✔ |
| `hrcontrato_competencia_consultar` | consultar | hrcontrato_competencia | empresa | ✔ |
| `hrcontrato_competencia_obter` | obter | hrcontrato_competencia | empresa, contrato, mes_de_faturamento | ✔ |
| `hrcontrato_excedente_faturamento_consultar` | consultar | hrcontrato_excedente_faturamento | empresa | ✔ |
| `hrcontrato_excedente_faturamento_obter` | obter | hrcontrato_excedente_faturamento | empresa, codigo_contrato, sequencial | ✔ |
| `hrcontrato_excedente_faturamento_totais` | totais | hrcontrato_excedente_faturamento | empresa | ✔ |
| `hrcontrato_faturamento_consultar` | consultar | hrcontrato_faturamento | empresa | ✔ |
| `hrcontrato_faturamento_obter` | obter | hrcontrato_faturamento | empresa, contrato, competencia | ✔ |
| `hrcontrato_historico_consultar` | consultar | hrcontrato_historico | empresa | ✔ |
| `hrcontrato_historico_obter` | obter | hrcontrato_historico | empresa, contrato, sequencial | ✔ |
