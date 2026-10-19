# GEGUIA_CONTRIBUICAO_PREVIDENCIARIA_SALDOS_RECOLHER — Guia da contribuição previdenciária - Valores de saldo a recolher.
654.147 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| COMPETENCIA | date(4) | PK |  | Competência. |
| TIPO_GUIA | smallint(2) | PK |  | Tipo de guia. (1=Mensal/2=13º salário/3=Tributos federais) |
| TIPO_SALDO_RECOLHER | smallint(2) | PK |  | Tipo de saldo a recolher. (1=INSS Folha/2=INSS Retido (EF)/3=FUNRURAL (EF)/4=INSS Receita Bruta (EF))/5=INSS Segurado folha/6=INSS Terceiros SEST/SENAT Folha/7=IRRF Folha/8=INSS Empresa e RAT Folha/9=INSS Terceiros Folha/10=IRRF (EF)/11=IRRF PF (EF)/12=IRRF Propaganda (EF)/13=CRF (EF)/14=COFINS Ret. (EF)/15=PIS Ret. (EF)/16=CSLL Ret. (EF)/17=CRF Órgão Públicos/(EF)18=PIS Folha/19=2,30(EF)/20=4,108(EF)/21=5,109(EF)/22=6,110(EF)/23=7,111,33(EF)/24=17,106(EF)/25=19,107(EF)/26=67(EF)/27=68(EF)/28=83,168(EF)/29=84(EF)/30=85(EF)/31=86(EF)/32=87(EF)/33=88,169(EF)/34=89(EF)/35=90(EF)/36=91(EF)/37=92(EF)/38=104(EF)/39=105(EF)/40=117(EF)/41=133(EF)/42=134(EF)/43=138(EF)/44=139(EF)/45=140(EF)/46=141(EF)/47=161(EF)/48=CSLL(LALUR)/49=IRPJ(LALUR)/50=Adicional ao SENAI |
| ALTERADO_MANUALMENTE | smallint(2) |  |  | Valor alterado manualmente. (0=Não/1=Sim) |
| VALOR_DEVIDO | numeric(13) |  |  |  |
| VALOR_COMPENSADO | numeric(13) |  |  |  |
| SALDO_RECOLHER | numeric(13) |  |  |  |
| CODI_EMP_ESCRITA_FISCAL | integer(4) |  | S |  |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Imp. tabelas/2=Imp. layout/3=Imp. tabelas concorrentes) |
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
