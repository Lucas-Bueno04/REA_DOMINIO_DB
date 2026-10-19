# CTEXTRATO_BANCARIO_CONFIGURACAO — Configuração para contabilizar extrato bancário
1.611 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CONFIGURACAO | integer(4) | PK |  | Código |
| CODI_CTA_BANCO | integer(4) |  |  | Conta contábil do banco |
| PARTE_HISTORICO | varchar(100) |  |  | Parte do histórico |
| CODI_CTA_CONTRA_PARTIDA | integer(4) |  |  | Conta de contra partida |
| CODI_HIS | integer(4) |  |  | Código do histórico |
| HISTORICO | varchar(512) |  |  | Histórico |
| TIPO | char(1) |  |  | Tipo (D=Soma/C=Subtrai/A=Ambos) |
| NUMERO_DOCUMENTO | varchar(100) |  | S | Número do documento |
| TIPO_FILTRO_NUMERO_DOCUMENTO | varchar(1) |  |  | Tipo do Filtro do NÃºmero do Documento (P=Parcial/C=Completo) |
