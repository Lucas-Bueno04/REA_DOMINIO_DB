# EFD_REINF_ENVIO_ARQUIVOS_XML — EFD-Reinf - Envio dos Arquivos - XML
74.952 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_ENVIO | integer(4) | PK |  | Código sequencial de envio dos arquivos |
| ARQUIVO_XML | long binary(32767) |  | S | Arquivo XML |
| ALTERADO_PELO_USUARIO | char(1) |  |  | Arquivo alterado pelo Usuário (S-Sim/N-Não) |
| I_FILIAL | integer(4) | PK |  | Código da filial |
| GERADO_PELO_AUDITOR | char(1) |  |  | Evento gerado ao enviar para o Auditor Fiscal(S/N) |
