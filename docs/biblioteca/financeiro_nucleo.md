# Módulo `financeiro_nucleo`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `hnagencias_consultar` | consultar | hnagencias | — | ✔ |
| `hnagencias_obter` | obter | hnagencias | sequencial | ✔ |
| `hnbancos_consultar` | consultar | hnbancos | — | ✔ |
| `hnbancos_obter` | obter | hnbancos | sequencial | ✔ |
| `hnclassificacoes_consultar` | consultar | hnclassificacoes | — | ✔ |
| `hnclassificacoes_obter` | obter | hnclassificacoes | codigo | ✔ |
| `hneventos_consultar` | consultar | hneventos | — | ✔ |
| `hneventos_obter` | obter | hneventos | codigo | ✔ |
| `hntipocontrato_consultar` | consultar | hntipocontrato | — | ✔ |
| `hntipocontrato_obter` | obter | hntipocontrato | codigo_do_tipo_de_contrato | ✔ |
| `hradiantamento_consultar` | consultar | hradiantamento | empresa | ✔ |
| `hradiantamento_obter` | obter | hradiantamento | empresa, codigo | ✔ |
| `hradiantamento_totais` | totais | hradiantamento | empresa | ✔ |
| `hraviso_consultar` | consultar | hraviso | — | ✔ |
| `hraviso_obter` | obter | hraviso | usuario, tipo_do_aviso_p_contas_a_pagar_v_convers | ✔ |
| `hrconversao_consultar` | consultar | hrconversao | — | ✔ |
| `hrconversao_obter` | obter | hrconversao | indica_como_esta_o_processo_de_conversao | ✔ |
| `hrobservacao_consultar` | consultar | hrobservacao | — | ✔ |
| `hrobservacao_obter` | obter | hrobservacao | codigo | ✔ |
| `hrpagamento_consultar` | consultar | hrpagamento | empresa | ✔ |
| `hrpagamento_obter` | obter | hrpagamento | empresa, lancamento_a_pagar, parcela, codigo | ✔ |
| `hrpagamento_totais` | totais | hrpagamento | empresa | ✔ |
| `hrparametro_consultar` | consultar | hrparametro | empresa | ✔ |
| `hrrenegociacao_consultar` | consultar | hrrenegociacao | empresa | ✔ |
| `hrrenegociacao_obter` | obter | hrrenegociacao | empresa, codigo | ✔ |
| `hrrenegociacao_totais` | totais | hrrenegociacao | empresa | ✔ |
