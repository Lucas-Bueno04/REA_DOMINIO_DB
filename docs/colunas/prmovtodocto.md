# prMovtoDocto — Movimento de documentos
10.747 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| nume_mod | integer(4) | PK |  | Nro. Protocolo |
| codi_emp | integer(4) |  | S | Cliente |
| codi_fun | integer(4) |  |  | Funcionario |
| dsai_mod | timestamp(8) |  |  | Data de saida |
| dret_mod | date(4) |  | S | Data de retorno, se ouver retorno |
| comp_mod | date(4) |  | S | Competencia |
| stat_mod | tinyint(1) |  |  | Tipo (1=Saiu, 2=Entrou) |
| codi_cev | integer(4) |  | S | Cliente Eventual |
| tipo_cli | char(1) |  | S | Tipo de Cliente (N=Normal, E=Eventual) |
| obs_mod | varchar(600) |  | S | Observacao |
| baix_mod | tinyint(1) |  | S | Baixado (Nulo=Pendente, 1=Total, 0=Parcial) |
| recb_mod | char(50) |  | S | Recebido por |
| CODI_USU | char(30) |  |  | Usuário |
| CODI_OBS | integer(4) |  | S | Código da Observação |
