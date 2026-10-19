# Módulo `contabil_bem`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `pmbem_documentos_fiscais_consultar` | consultar | pmbem_documentos_fiscais | empresa | ✔ |
| `pmbem_documentos_fiscais_obter` | obter | pmbem_documentos_fiscais | empresa, codigo_do_bem, numero_sequencial | ✔ |
| `pmbem_documentos_fiscais_totais` | totais | pmbem_documentos_fiscais | empresa | ✔ |
| `pmbem_historico_consultar` | consultar | pmbem_historico | empresa | ✔ |
| `pmbem_historico_obter` | obter | pmbem_historico | empresa, bem, sequencial | ✔ |
| `pmbem_lancto_consultar` | consultar | pmbem_lancto | empresa | ✔ |
| `pmbem_lancto_obter` | obter | pmbem_lancto | empresa, bem, empresa_do_lancamento_contabil, numero_do_lancamento_contabil | ✔ |
| `pmbem_taxa_alternativa_consultar` | consultar | pmbem_taxa_alternativa | empresa | ✔ |
| `pmbem_taxa_alternativa_obter` | obter | pmbem_taxa_alternativa | empresa, bem, sequencial | ✔ |
