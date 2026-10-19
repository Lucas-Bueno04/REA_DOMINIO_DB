# Módulo `geral_empresa`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `geempresa_bloqueada_consultar` | consultar | geempresa_bloqueada | empresa | ✔ |
| `geempresa_bloqueada_obter` | obter | geempresa_bloqueada | empresa, sequencial | ✔ |
| `geempresa_bloqueada_escritorio_consultar` | consultar | geempresa_bloqueada_escritorio | — | ✔ |
| `geempresa_bloqueada_escritorio_obter` | obter | geempresa_bloqueada_escritorio | sequencial, escritorio_que_bloqueou_a_empresa | ✔ |
| `geempresa_bloqueio_historico_consultar` | consultar | geempresa_bloqueio_historico | empresa | ✔ |
| `geempresa_bloqueio_historico_obter` | obter | geempresa_bloqueio_historico | empresa, sequencial | ✔ |
| `geempresa_bloqueio_historico_totais` | totais | geempresa_bloqueio_historico | empresa | ✔ |
| `geempresa_bloqueio_restricao_consultar` | consultar | geempresa_bloqueio_restricao | empresa | ✔ |
| `geempresa_bloqueio_restricao_obter` | obter | geempresa_bloqueio_restricao | empresa, sequencial | ✔ |
