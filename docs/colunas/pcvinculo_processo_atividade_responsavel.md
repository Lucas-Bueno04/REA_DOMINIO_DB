# PCVINCULO_PROCESSO_ATIVIDADE_RESPONSAVEL — Vínculo entre processos e empresas - Atividades - Responsáveis
3 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_VINCULO | integer(4) | PK |  | Código do vínculo |
| I_SEQUENCIAL_ATIVIDADE | integer(4) | PK |  | Sequencial da atividade |
| I_SEQUENCIAL_RESPONSAVEL | integer(4) | PK |  | Sequencial |
| I_RESPONSAVEL | integer(4) |  |  | Código do responsável |
| RESPONSAVEL_TIPO | smallint(2) |  |  | Tipo do responsável (Fixo 1) |
| A_PARTIR_DE | date(4) |  | S | A partir de |
| ENCERRADO_EM | date(4) |  | S | Encerrado em |
