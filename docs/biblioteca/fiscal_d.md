# Módulo `fiscal_d`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `efd_reinf_envio_arquivos_log_erros_comunicacao_consultar` | consultar | efd_reinf_envio_arquivos_log_erros_comunicacao | empresa | ✔ |
| `efd_reinf_envio_arquivos_log_erros_comunicacao_obter` | obter | efd_reinf_envio_arquivos_log_erros_comunicacao | empresa, codigo_da_empresa_filial, codigo_sequencial_de_envio_dos_arquivos, codigo_sequencial_de_erros | ✔ |
| `efd_reinf_envio_arquivos_xml_consultar` | consultar | efd_reinf_envio_arquivos_xml | empresa | ✔ |
| `efd_reinf_envio_arquivos_xml_obter` | obter | efd_reinf_envio_arquivos_xml | empresa, codigo_sequencial_de_envio_dos_arquivos, codigo_da_filial | ✔ |
| `efd_reinf_eventos_consultar` | consultar | efd_reinf_eventos | — | ✔ |
| `efd_reinf_eventos_obter` | obter | efd_reinf_eventos | codigo_do_evento | ✔ |
| `efd_reinf_retorno_arquivos_r2010_consultar` | consultar | efd_reinf_retorno_arquivos_r2010 | empresa | ✔ |
| `efd_reinf_retorno_arquivos_r2010_obter` | obter | efd_reinf_retorno_arquivos_r2010 | empresa, sequencial, filial, codigo_da_receita | ✔ |
| `efd_reinf_retorno_arquivos_r2010_totais` | totais | efd_reinf_retorno_arquivos_r2010 | empresa | ✔ |
| `efd_reinf_retorno_arquivos_r2020_consultar` | consultar | efd_reinf_retorno_arquivos_r2020 | empresa | ✔ |
| `efd_reinf_retorno_arquivos_r2020_obter` | obter | efd_reinf_retorno_arquivos_r2020 | empresa, sequencial, filial | ✔ |
| `efd_reinf_retorno_arquivos_r2020_totais` | totais | efd_reinf_retorno_arquivos_r2020 | empresa | ✔ |
| `efd_reinf_retorno_arquivos_r2050_consultar` | consultar | efd_reinf_retorno_arquivos_r2050 | empresa | ✔ |
| `efd_reinf_retorno_arquivos_r2050_obter` | obter | efd_reinf_retorno_arquivos_r2050 | empresa, sequencial, filial, codigo_da_receita | ✔ |
| `efd_reinf_retorno_arquivos_r2050_totais` | totais | efd_reinf_retorno_arquivos_r2050 | empresa | ✔ |
| `efd_reinf_retorno_arquivos_r2060_consultar` | consultar | efd_reinf_retorno_arquivos_r2060 | empresa | ✔ |
| `efd_reinf_retorno_arquivos_r2060_obter` | obter | efd_reinf_retorno_arquivos_r2060 | empresa, sequencial, filial, codigo_da_receita | ✔ |
| `efd_reinf_retorno_arquivos_r2060_totais` | totais | efd_reinf_retorno_arquivos_r2060 | empresa | ✔ |
| `efd_reinf_retorno_arquivos_r2099_r2010_consultar` | consultar | efd_reinf_retorno_arquivos_r2099_r2010 | empresa | ✔ |
| `efd_reinf_retorno_arquivos_r2099_r2010_obter` | obter | efd_reinf_retorno_arquivos_r2099_r2010 | empresa, sequencial_envio, filial, sequencial | ✔ |
| `efd_reinf_retorno_arquivos_r2099_r2010_totais` | totais | efd_reinf_retorno_arquivos_r2099_r2010 | empresa | ✔ |
| `efd_reinf_retorno_arquivos_r2099_r2020_consultar` | consultar | efd_reinf_retorno_arquivos_r2099_r2020 | empresa | ✔ |
| `efd_reinf_retorno_arquivos_r2099_r2020_obter` | obter | efd_reinf_retorno_arquivos_r2099_r2020 | empresa, sequencial_envio, filial, sequencial | ✔ |
| `efd_reinf_retorno_arquivos_r2099_r2020_totais` | totais | efd_reinf_retorno_arquivos_r2099_r2020 | empresa | ✔ |
| `efd_reinf_retorno_arquivos_r2099_r2050_consultar` | consultar | efd_reinf_retorno_arquivos_r2099_r2050 | empresa | ✔ |
| `efd_reinf_retorno_arquivos_r2099_r2050_obter` | obter | efd_reinf_retorno_arquivos_r2099_r2050 | empresa, sequencial_envio, filial, sequencial | ✔ |
| `efd_reinf_retorno_arquivos_r2099_r2050_totais` | totais | efd_reinf_retorno_arquivos_r2099_r2050 | empresa | ✔ |
| `efd_reinf_retorno_arquivos_r2099_r2060_consultar` | consultar | efd_reinf_retorno_arquivos_r2099_r2060 | empresa | ✔ |
| `efd_reinf_retorno_arquivos_r2099_r2060_obter` | obter | efd_reinf_retorno_arquivos_r2099_r2060 | empresa, sequencial_envio, filial, sequencial | ✔ |
| `efd_reinf_retorno_arquivos_r2099_r2060_totais` | totais | efd_reinf_retorno_arquivos_r2099_r2060 | empresa | ✔ |
| `efd_reinf_retorno_arquivos_r4099_consultar` | consultar | efd_reinf_retorno_arquivos_r4099 | empresa | ✔ |
| `efd_reinf_retorno_arquivos_r4099_obter` | obter | efd_reinf_retorno_arquivos_r4099 | empresa, sequencial_empresa, filial | ✔ |
| `efd_reinf_retorno_arquivos_r4099_periodo_consultar` | consultar | efd_reinf_retorno_arquivos_r4099_periodo | empresa | ✔ |
| `efd_reinf_retorno_arquivos_r4099_periodo_obter` | obter | efd_reinf_retorno_arquivos_r4099_periodo | empresa, sequencial_de_envio, filial, periodicidade, periodo, codigo_de_receita | ✔ |
| `efd_reinf_retorno_arquivos_r4099_periodo_totais` | totais | efd_reinf_retorno_arquivos_r4099_periodo | empresa | ✔ |
| `efd_reinf_retorno_xml_evento_consultar` | consultar | efd_reinf_retorno_xml_evento | empresa | ✔ |
| `efd_reinf_retorno_xml_evento_obter` | obter | efd_reinf_retorno_xml_evento | empresa, sequencial, filial | ✔ |
