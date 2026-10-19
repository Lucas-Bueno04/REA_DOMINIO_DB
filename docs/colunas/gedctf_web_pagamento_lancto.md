# GEDCTF_WEB_PAGAMENTO_LANCTO — DCTF Web - Pagamentos X Lançamentos contábeis
84 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa do lançamento |
| NUME_LAN | integer(4) | PK |  | Número lançamento |
| FILI_LAN | integer(4) | PK |  | Empresa do pagamento |
| COMPETENCIA | date(4) | PK |  | Competência |
| TIPO_GUIA | smallint(2) | PK |  | Tipo de guia. (1=Mensal/2=13º salário/3=Tributos federais) |
| CODI_IMP | integer(4) |  |  | Imposto |
| I_PAGAMENTO | integer(4) | PK |  | Sequencial do pagamento |
| GRUPO | integer(4) |  |  | Grupo do lançamento |
| TIPO | integer(4) |  |  | Tipo do lançamento (0 - Usuário/1 - Principal/2 - Juros/3 - Multa/4-Valor pago a maior/5 - Correção) |
| CONTRA_PARTIDA | integer(4) |  |  | Código do lançamento contrapartida para pagamentos em grupo |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro (0=Sistema/1=Imp. tabelas/2=Imp. layout/3=Imp. tabelas concorrentes/5=Digital Bank) |
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| LANCAMENTO_DISCRIMINADO_POR_IMPOSTO | smallint(2) |  |  | Lançamento discriminado por imposto. (0=Não/1=Sim) |
| ORDEM_GRAVACAO | integer(4) |  |  | Ordem do lançamento no momento da gravação |
