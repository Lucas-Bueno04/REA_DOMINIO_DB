# FOATENDIMENTO_ACOES — Acoes Dominio Atendimento
54 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_ACOES | integer(4) | PK |  | Código sequencial da ação |
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| CODI_EMP_ATENDIMENTO | integer(4) | PK |  | Código da empresa do atendimento |
| ACAO | smallint(2) | PK |  | Tipo da ação (1=Inserir/2=Excluir/3=Desabilitar/4=Carga Inicial) |
| CONCLUIDO | smallint(2) |  |  | Ação concluída (0=Não/1=Sim) |
