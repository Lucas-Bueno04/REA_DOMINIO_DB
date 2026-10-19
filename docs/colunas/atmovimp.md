# atmovimp — Movimentacao dos Impostos em atraso
3.412 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| comp_mov | date(4) | PK |  | Competencia |
| vecn_mov | date(4) |  | S | Vencimento |
| pgto_mov | date(4) |  | S | Data Pagamento |
| vldv_mov | numeric(13) |  | S | Valor devido |
| vreal_mov | numeric(13) |  | S | Valor em Real |
| vlatua_mov | numeric(13) |  | S | Atualizacao monetaria |
| vljuro_mov | numeric(13) |  | S | Juros |
| vlmult_mov | numeric(13) |  | S | Multa |
| vlto_mov | numeric(13) |  | S | Valor Total |
| juro_mov | numeric(13) |  | S | Percentual de juros |
| mult_mov | numeric(13) |  | S | Percentual de multa |
| pdic_imp | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=1Q, 6=Mensal, 7=Tri, 8=Sem, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Comp, 52=13Sal) |
| codi_imp | integer(4) | PK |  | Imposto |
| voutent_mov | numeric(13) |  | S | Valor de Outras Entidades |
| vrealent_mov | numeric(13) |  | S | Valor Real de Outras Entidades |
| vatuaent_mov | numeric(13) |  | S | Atualizacao  Monetaria de Outras Entidades |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| codigorec_mov | integer(4) | PK |  | Codigo de recolhimento GPS |
| codigofilial_mov | integer(4) | PK |  | Codigo da filial da folha |
| codigoservico_mov | integer(4) | PK |  | Codigo do servico da folha |
| tiposervico_mov | integer(4) | PK |  | Tipo do servico |
| tipoguia_mov | integer(4) | PK |  | Tipo da guia |
| CODI_REC | varchar(6) | PK |  | Codigo de Recolhimento |
| CODI_FOR | integer(4) | PK |  | Código do fornecedor |
| DOCUMENTO_ENTRADA | numeric(15) | PK |  | Número do documento da nota de entrada |
| NUMERO_PARCELA | integer(4) | PK |  | Número da parcela |
| I_SCP | integer(4) | PK |  | Código do SCP |
| I_EMPREGADO | integer(4) | PK |  | Código do Empregado |
| I_SINDICATO | integer(4) | PK |  | Código do Sindicato |
