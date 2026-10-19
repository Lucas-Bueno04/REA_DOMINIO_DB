# GEEMPRESA_BLOQUEIO_HISTORICO — Empresas bloqueadas - Históricos
4.461 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_SEQUENCIAL | integer(4) | PK |  | Sequencial |
| CODI_EMP | integer(4) |  |  | Empresa |
| ORIGEM | char(1) |  |  | Origem do histórico (S=Sistema/ U=Usuário) |
| SITUACAO | char(1) |  |  | Situação (B=Bloqueado/ D=Desbloqueado) |
| DATA_HISTORICO | date(4) |  |  | Data |
| USUARIO | varchar(30) |  | S | Usuário |
| DIAS_DESBLOQUEADOS | integer(4) |  | S | Dias desbloquados |
| DATA_FINAL_DESBLOQUEIO | date(4) |  | S | Data final do desbloqueio |
| OBERVACAO_INADIMPLENTE | varchar(200) |  | S | Obervação |
| HISTORICO_CONTRATO | varchar(200) |  |  | Histórico para o contrato |
