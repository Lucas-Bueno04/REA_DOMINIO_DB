# ctlancto — Lancamentos Contabeis
13.712.713 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| nume_lan | integer(4) | PK |  | Numero |
| data_lan | date(4) |  |  | Data |
| vlor_lan | numeric(14) |  |  | Valor |
| cdeb_lan | integer(4) |  |  | Debito |
| ccre_lan | integer(4) |  |  | Credito |
| codi_his | integer(4) |  | S | Codigo Historico |
| chis_lan | varchar(1000) |  | S | Historico |
| codi_usu | char(30) |  |  | Usuario |
| orig_lan | tinyint(1) |  |  | Origem (1=Normal, 2=Zer, 3=Pat, 4=Esc, 5=Sai, 6=Ent, 7=Ser, 8=Aju, 9=Acu, 10=Apu, 11=PgtGuia, 12=Cliente, 13=Folha, 14-19=Hono) |
| ndoc_lan | integer(4) |  | S | Relacao com Escrita Fiscal |
| fili_lan | integer(4) |  |  | Filial |
| dorig_lan | date(4) |  |  | Data Original |
| codi_pad | integer(4) |  | S | Lancamento padrao |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| codi_lote | integer(4) |  | S | Lancamento em lote |
| CONCILIADO_DEB | char(1) |  |  | Lançamento conciliado a débito (S/N) |
| CONCILIADO_CRE | char(1) |  |  | Lançamento conciliado a crédito (S/N) |
| CODI_EMP_PLANO | integer(4) |  |  | Empresa do plano de contas |
| CPF_TITULAR_PAGAMENTO | varchar(14) |  | S | Titular do pagamento |
| CPF_BENEFICIARIO_SERVICO | varchar(11) |  | S | CPF Beneficiário do serviço |
| DATA_LAN_BUSCA | integer(4) |  | S | Data de lançamento para busca |
| DATA_OCORRENCIA | date(4) |  | S | Data de ocorrência |
| CARNE_LEAO_TIPO_INSCRICAO | char(1) |  |  | Tipo de inscrição recebido Carnê Leão Web [1=C.P.F. / 2=C.N.P.J / 3=Exterior] |
| CARNE_LEAO_VALOR_DEDUCAO | numeric(11) |  | S | Valor da dedução Carnê Leão Web |
| CARNE_LEAO_RETENCAO_IRRF | char(1) |  |  | Retenção de IRRF Carnê Leão Web |
| CARNE_LEAO_VALOR_MULTA | numeric(11) |  | S | Valor da multa Carnê Leão Web |
| CARNE_LEAO_VALOR_JUROS | numeric(11) |  | S | Valor dos juros Carnê Leão Web |
| CARNE_LEAO_COMPETENCIA | date(4) |  | S | Competência Carnê Leão Web |
| CARNE_LEAO_VALOR_IRRF | numeric(11) |  | S | Valor do IRRF Carnê Leão Web |
