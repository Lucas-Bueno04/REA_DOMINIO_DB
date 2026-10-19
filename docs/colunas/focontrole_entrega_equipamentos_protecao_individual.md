# FOCONTROLE_ENTREGA_EQUIPAMENTOS_PROTECAO_INDIVIDUAL — Equipamento de proteção individual - Empregado
8 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| I_EPI | integer(4) | PK |  | Código do EPI. |
| DATA_ENTREGA | date(4) | PK |  | Data da entrega. |
| QUANTIDADE | integer(4) |  |  | Quantidade. |
| OBSERVACAO | varchar(150) |  | S | Observação. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
| DATA_VENCIMENTO | date(4) |  | S | Data de vencimento. |
