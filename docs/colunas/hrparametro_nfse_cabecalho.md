# HRPARAMETRO_NFSE_CABECALHO — Parametro Honorarios - Imagem e textos para NFSe
3 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| TEXTO_RPS | varchar(512) |  |  | Texto para RPS |
| TEXTO_NFSE | varchar(512) |  |  | Texto para NFS-e |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
