# PCVINCULO_PROCESSO — Vínculo entre processos e empresas
3 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_VINCULO | integer(4) | PK |  | Código |
| ORDEM | integer(4) |  |  | Ordem |
| CODI_EMP | integer(4) |  |  | Código do processo |
| I_PROCESSO | integer(4) |  |  | Código da empresa |
| COMPETENCIA_INICIO | date(4) |  |  | A partir de |
| ENCERRAR | char(1) |  |  | Encerrar (S/N) |
| COMPETENCIA_ENCERRAMENTO | date(4) |  | S | Competência de encerramento |
| USUARIO_ENCERRAMENTO | varchar(30) |  | S | Usuário que encerrou |
