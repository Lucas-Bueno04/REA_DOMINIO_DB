# Módulo `pessoal_emprestimos`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `foemprestimos_consignados_consultar` | consultar | foemprestimos_consignados | empresa | ✔ |
| `foemprestimos_consignados_obter` | obter | foemprestimos_consignados | empresa, codigo_do_empregado, codigo_do_emprestimo | ✔ |
| `foemprestimos_consignados_totais` | totais | foemprestimos_consignados | empresa | ✔ |
| `foemprestimos_consignados_importacao_consultar` | consultar | foemprestimos_consignados_importacao | empresa | ✔ |
| `foemprestimos_consignados_importacao_obter` | obter | foemprestimos_consignados_importacao | empresa, codigo_do_empregado, codigo_do_banco, competencia_de_desconto, numero_do_contrato | ✔ |
| `foemprestimos_consignados_importacao_totais` | totais | foemprestimos_consignados_importacao | empresa | ✔ |
| `foemprestimos_consignados_importacao_erros_consultar` | consultar | foemprestimos_consignados_importacao_erros | empresa | ✔ |
| `foemprestimos_consignados_importacao_erros_obter` | obter | foemprestimos_consignados_importacao_erros | empresa, competencia_de_desconto, codigo_sequencial_da_tabela | ✔ |
| `foemprestimos_consignados_parcelas_consultar` | consultar | foemprestimos_consignados_parcelas | empresa | ✔ |
| `foemprestimos_consignados_parcelas_obter` | obter | foemprestimos_consignados_parcelas | empresa, codigo_do_empregado, codigo_do_emprestimo, numero_da_parcela | ✔ |
| `foemprestimos_consignados_parcelas_totais` | totais | foemprestimos_consignados_parcelas | empresa | ✔ |
| `foemprestimos_cred_trab_rescisao_consultar` | consultar | foemprestimos_cred_trab_rescisao | empresa | ✔ |
| `foemprestimos_cred_trab_rescisao_obter` | obter | foemprestimos_cred_trab_rescisao | empresa, codigo_do_empregado, competencia_da_rescisao, numero_do_contrato | ✔ |
| `foemprestimos_cred_trab_rescisao_totais` | totais | foemprestimos_cred_trab_rescisao | empresa | ✔ |
| `foemprestimos_cred_trab_rescisao_api_retorno_consultar` | consultar | foemprestimos_cred_trab_rescisao_api_retorno | empresa | ✔ |
| `foemprestimos_cred_trab_rescisao_api_retorno_obter` | obter | foemprestimos_cred_trab_rescisao_api_retorno | empresa, codigo_sequencial_da_tabela | ✔ |
