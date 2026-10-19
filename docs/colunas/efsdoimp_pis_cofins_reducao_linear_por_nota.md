# EFSDOIMP_PIS_COFINS_REDUCAO_LINEAR_POR_NOTA — Saldo do Impostos - PIS/COFINS Reducao Linear por Nota
2.420 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| I_SCP | integer(4) | PK |  | Sequencial do SCP |
| I_RECOLHIMENTO | integer(4) | PK |  | Sequencial do Recolhimento |
| FILIAL | integer(4) | PK |  | Código Filial |
| CST | integer(4) | PK |  | CST |
| ALIQUOTA | numeric(7) | PK |  | Aliquota do Imposto |
| PERCENTUAL_LINEAR | numeric(5) | PK |  | Percentual da Reducao Linear |
| OPERACAO | char(1) | PK |  | Operacao (A - Acrescimo / R - Reducao) |
| TIPO_MOV | char(3) | PK |  | Tipo do Movimento TIPO_MOV IN (S, V, B, CFE, ED, Z, ZB, RMD) |
| DOCUMENTO | numeric(15) | PK |  | Documento |
| CHAVE | varchar(255) | PK |  | Chave de acesso |
| DATA_MOV | date(4) |  |  | Data movimento |
| BASE_CALCULO | numeric(13) |  |  | Base de Calculo |
| VALOR_IMPOSTO | numeric(13) |  |  | Valor do Imposto |
