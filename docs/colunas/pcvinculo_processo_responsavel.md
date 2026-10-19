# PCVINCULO_PROCESSO_RESPONSAVEL — Vínculo entre processos e empresas - Responsáveis
3 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_VINCULO | integer(4) | PK |  | Código do vínculo |
| I_SEQUENCIAL_RESPONSAVEL | integer(4) | PK |  | Sequencial |
| COMPETENCIA | date(4) |  |  | Competência |
| I_RESPONSAVEL | integer(4) |  |  | Código do responsável |
| RESPONSAVEL_TIPO | smallint(2) |  |  | Tipo do responsável (Fixo 1) |
