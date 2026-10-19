# GECHECKPOINT_COMPARATIVO_REGIME_TRIBUTACAO_SALDO — Checkpoint - Comparativo de Regime de Tributação - Informações saldos
40 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CAMPO | varchar(100) | PK |  | Coluna |
| DETERMINAR_FORMA_IMPORTACAO_SALDO | char(1) |  |  | Determinar a forma de importar o saldo das contas contábeis (S/N) |
| TIPO_SALDO_IMPORTACAO | smallint(2) |  |  | Forma de importar o saldo das contas contábeis |
| ORIGEM_IMPORTAR_VALORES | char(1) |  |  | Importar valores C - Das contas contÃ¡beis / R - Das rubricas do mÃ³dulo folha. |
