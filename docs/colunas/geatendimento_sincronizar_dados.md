# GEATENDIMENTO_SINCRONIZAR_DADOS — Tabela para sincronizar dados com o atendimento
68 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_ACOES | integer(4) | PK |  |  |
| CODI_EMP | integer(4) |  | S | Código da empresa |
| CODI_EMP_ATENDIMENTO | integer(4) |  | S | Código da empresa no Domínio atendimento |
| TIPO | integer(4) |  |  | Tipo da informação que será enviada |
| CODIGO | integer(4) |  |  | Código sequencial da tabela que armazena os dados que serão enviados. |
| ACAO | smallint(2) |  |  | Acao 1=Novo/Atualizar - 2=Excluir |
| CONCLUIDO | smallint(2) |  |  |  |
