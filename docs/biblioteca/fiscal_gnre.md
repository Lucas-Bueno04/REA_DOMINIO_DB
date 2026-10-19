# Módulo `fiscal_gnre`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `efgnre_avulsa_receita_consultar` | consultar | efgnre_avulsa_receita | — | ✔ |
| `efgnre_avulsa_receita_obter` | obter | efgnre_avulsa_receita | uf_favorecida, codigo_da_receita | ✔ |
| `efgnre_avulsa_receita_detalhamento_consultar` | consultar | efgnre_avulsa_receita_detalhamento | — | ✔ |
| `efgnre_avulsa_receita_detalhamento_obter` | obter | efgnre_avulsa_receita_detalhamento | uf_favorecida, codigo_da_receita, codigo_do_detalhamento_da_receita | ✔ |
| `efgnre_avulsa_receita_documentos_origem_consultar` | consultar | efgnre_avulsa_receita_documentos_origem | — | ✔ |
| `efgnre_avulsa_receita_documentos_origem_obter` | obter | efgnre_avulsa_receita_documentos_origem | uf_favorecida, codigo_da_receita, codigo_do_documento_de_origem_da_receita | ✔ |
| `efgnre_avulsa_receita_produtos_consultar` | consultar | efgnre_avulsa_receita_produtos | — | ✔ |
| `efgnre_avulsa_receita_produtos_obter` | obter | efgnre_avulsa_receita_produtos | uf_favorecida, codigo_da_receita, codigo_do_produto_da_receitar | ✔ |
| `efgnre_receita_produtos_consultar` | consultar | efgnre_receita_produtos | — | ✔ |
| `efgnre_receita_produtos_obter` | obter | efgnre_receita_produtos | uf_favorecida, codigo_receita, codigo_produto | ✔ |
