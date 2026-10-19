# foprovisoes — Provisoes
154.110 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_empregados | integer(4) | PK |  | Empregado |
| competencia | date(4) | PK |  | Competencia |
| tipo | tinyint(1) | PK |  | Tipo provisao |
| i_filiais | integer(4) |  |  | Filial |
| i_depto | integer(4) |  |  | Departamento |
| i_ccustos | integer(4) |  |  | Centro de custos |
| i_servicos | integer(4) |  |  | Servico |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| salario | numeric(13) |  |  | Salario |
| medias | numeric(13) |  | S | ** SEM USO ** Médias |
| ferias_adic | numeric(13) |  | S | ** SEM USO ** 1/3 de ferias(adicional de ferias) |
| adiant_13 | numeric(13) |  | S | ** SEM USO ** Valor do adiantamento de 13o |
| valor_devido | numeric(13) |  | S | ** SEM USO ** Valor total |
| valor_mes | numeric(13) |  | S | ** SEM USO ** Valor do mes |
| valor_total | numeric(13) |  | S | ** SEM USO ** Valor total |
| avos | integer(4) |  |  | Numero de avos |
| dias_ferias | numeric(13) |  |  | Numero de dias |
| vencto_ferias | date(4) |  | S | Vencimento de ferias |
| faltas | integer(4) |  |  | Numero de dias de faltas |
| inss_mes | numeric(13) |  | S | ** SEM USO ** INSS do mes |
| fgts_mes | numeric(13) |  | S | ** SEM USO ** FGTS do mes |
| pis_mes | numeric(13) |  | S | ** SEM USO ** PIS do mes |
| inss_total | numeric(13) |  | S | ** SEM USO ** INSS total |
| fgts_total | numeric(13) |  | S | ** SEM USO ** FGTS total |
| pis_total | numeric(13) |  | S | ** SEM USO ** PIS total |
| valor_dif | numeric(13) |  | S | ** SEM USO ** Valor diferenca |
| inss_dif | numeric(13) |  | S | ** SEM USO ** INSS diferenca |
| fgts_dif | numeric(13) |  | S | ** SEM USO ** FGTS diferenca |
| pis_dif | numeric(13) |  | S | ** SEM USO ** PIS diferenca |
| perdeu_periodo | tinyint(1) |  |  | O empregado perdeu direito ao periodo |
| AFASTAMENTO_PREVIDENCIA | integer(4) |  |  | Dias afastados pela previdência |
| AFASTAMENTO_SEM_REMUNERACAO | integer(4) |  |  | Dias afastados sem remuneração |
| AFASTAMENTO_COM_REMUNERACAO | integer(4) |  |  | Dias afastados com remuneração |
| SALARIO_MES_ANTERIOR | numeric(13) |  |  | Salário do mês anterior |
| MESES_PERDIDOS_POR_FALTAS | smallint(2) |  | S | Meses perdidos por faltas |
| MESES_PERDIDOS_POR_AFASTAMENTO | smallint(2) |  | S | Meses perdidos por afastamento |
| TAXA_INSS_EMPRESA | numeric(17) |  |  | Taxa INSS Empresa. |
| TAXA_INSS_RAT | numeric(17) |  |  | Taxa INSS RAT. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
