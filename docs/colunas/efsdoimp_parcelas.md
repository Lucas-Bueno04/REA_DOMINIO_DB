# efsdoimp_parcelas — Saldo dos Impostos Parcelados
4.469 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_imp | integer(4) | PK |  | Imposto |
| data_sim | date(4) | PK |  | Competencia |
| pdic_sim | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| parc_simp | integer(4) | PK |  | Parcela do imposto |
| valor_simp | numeric(13) |  | S | Valor da Parcela |
| vcto_simp | date(4) |  | S | Vencimento da Parcela |
| vlrpago_simp | numeric(13) |  | S | Valor pago do imposto |
| CLASSE_SIMP | integer(4) |  | S | Classe de vencimento |
| ACORDO_SIMP | char(15) |  | S | Numero do acordo |
| CODIGO_RECEITA | char(6) |  | S | Código da receita |
| DESCRICAO_COMPLEMENTAR | varchar(255) |  | S | Descrição complementar |
| PARCELAR_DIFALI | char(1) |  |  | Parcelar o imposto ICMS diferencial de alíquota - DIFALI |
