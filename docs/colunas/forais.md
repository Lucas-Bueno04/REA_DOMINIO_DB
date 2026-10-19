# forais — Dados RAIS
48 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_filiais | integer(4) | PK |  | Filial |
| mes_base | tinyint(1) |  |  | Mes base |
| pat | char(1) |  |  | Participa do PAT |
| uso_exclusivo | char(13) |  |  | Uso exclusivo |
| vinc_pat | numeric(6) |  | S | Vinculo PAT |
| vinc_pat_ac | numeric(6) |  | S | Vinculo PAT acima de 5 sm |
| porc_serv_proprio | numeric(3) |  | S | % servicos próprios |
| porc_adm_cozinha | numeric(3) |  | S | % administracao cozinha |
| porc_ref_conv | numeric(3) |  | S | % refeicao convenio |
| porc_ref_trans | numeric(3) |  | S | % refeicao transportada |
| porc_cesta_alim | numeric(3) |  | S | % cesta alimento |
| porc_alim_conv | numeric(3) |  | S | % alimentacao convenio |
| dt_encerr_ativ | date(4) |  | S | Data encerramento atividade |
| encerr_ativ | tinyint(1) |  | S | Encerramento atividade |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| valor_contr_sind | numeric(13) |  | S | Valor contribuicao sindical |
| valor_contr_asso | numeric(13) |  | S | Valor contribuicao associativa |
| valor_contr_assi | numeric(13) |  | S | Valor contribuicao assistencial |
| valor_contr_conf | numeric(13) |  | S | Valor contribuicao confederativa |
| cgc_sind | char(14) |  | S | CNPJ contribuicao sindical |
| cgc_asso | char(14) |  | S | CNPJ contribuicao associativa |
| cgc_assi | char(14) |  | S | CNPJ contribuicao assistencial |
| cgc_conf | char(14) |  | S | CNPJ contribuicao confederativa |
| exerceu_ativ | tinyint(1) |  | S | Exerceu atividade durante o ano-base |
| sindicalizada | tinyint(1) |  | S | Sindicalizada (1=Sim/0=Nao |
| SISTEMA_CONTROLE_PONTO | smallint(2) |  | S | Sistema de controle de ponto. (0=Não possui/1=Manual/2=Mecânico/3=Registro eletrônico de acordo com a  Portaria 1.510/2009/4=Não eletrônico alternativo de acordo com a Portaria 373/2011/5=Eletrônico alternativo de acordo com a Portaria 373/2011) |
| QUANTIDADE_COOPERADOS | integer(4) |  | S | Quantidade de cooperados. |
| GERAR_DATA_DESLIGAMENTO_CONFORME_PROJECAO_AVISO_PREVIO | smallint(2) |  |  | Gerar a data de desligamento conforme a data da projeção do aviso prévio indenizado (0=Não/1=Sim) |
| ANO_INICIO_GERAR_DATA_DESLIGAMENTO_CONFORME_PROJECAO_AVISO_PREVIO | smallint(2) |  | S | Ano início para gerar a data do desligamento conforme data da projeção do aviso prévio indenizado |
| ANO_BASE_ENCERRAMENTO_GERAR | smallint(2) |  | S | Ano base para gerar a RAIS, quando houver encerramento da empresa. |
