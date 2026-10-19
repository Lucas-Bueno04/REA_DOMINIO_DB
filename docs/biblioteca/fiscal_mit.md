# Módulo `fiscal_mit`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `efmit_api_bilhetagem_consultar` | consultar | efmit_api_bilhetagem | empresa | ✔ |
| `efmit_api_bilhetagem_obter` | obter | efmit_api_bilhetagem | empresa, codigo_sequencial_de_envio_dos_arquivos, codigo_do_contador, sequencial_bilhetagem | ✔ |
| `efmit_api_envio_arquivos_consultar` | consultar | efmit_api_envio_arquivos | empresa | ✔ |
| `efmit_api_envio_arquivos_obter` | obter | efmit_api_envio_arquivos | empresa, codigo_sequencial_de_envio_dos_arquivos | ✔ |
| `efmit_api_envio_arquivos_json_consultar` | consultar | efmit_api_envio_arquivos_json | empresa | ✔ |
| `efmit_api_envio_arquivos_json_obter` | obter | efmit_api_envio_arquivos_json | empresa, codigo_sequencial_de_envio_dos_arquivos, tipo_do_arquivo | ✔ |
| `efmit_api_envio_arquivos_mensagem_consultar` | consultar | efmit_api_envio_arquivos_mensagem | empresa | ✔ |
| `efmit_api_envio_arquivos_mensagem_obter` | obter | efmit_api_envio_arquivos_mensagem | empresa, codigo_sequencial_de_envio_dos_arquivos, sequencial_mensagem | ✔ |
