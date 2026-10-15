# ctcontas — Contas Contabeis - Cadastro
1.574.175 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_cta | integer(4) | PK |  | Codigo |
| nome_cta | varchar(150) |  |  | Descricao |
| clas_cta | char(20) |  |  | Classificacao |
| tipo_cta | char(1) |  |  | Tipo (A=Analitico/S=Sintetico) |
| grdre_cta | integer(4) |  | S | Grupo DRE |
| dlpa_cta | integer(4) |  | S | Grupo DLPA |
| doar_cta | integer(4) |  | S | Grupo DOAR |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes, 4 - Iceberg |
| dmpl_cta | integer(4) |  | S | Grupo DMPL |
| DATA_CTA | date(4) |  |  | Data cadastro |
| SITUACAO_CTA | char(1) |  |  | Situacao (A-Ativa/I-Inativa) |
| DATAINATIVA_CTA | date(4) |  | S | Data da inativacao |
| DRA_CTA | integer(4) |  | S | Grupo DRA |
| DSP_CTA | integer(4) |  | S | Grupo DSP |
| DSP_ATO_CTA | char(1) |  | S | Grupo DSP - Ato (C=Cooperado/ N=Não cooperado/ A=Ambos) |
| CARNE_LEAO_CTA | tinyint(1) |  |  | Grupo Carnê Leão |
| EBITDA_CTA | integer(4) |  | S | Grupo EBITDA |
| LCDPR_CTA | integer(4) |  | S | Grupo LCDPR |
| CARNE_LEAO_GERAR_WEB | char(1) |  |  | Gerar no Carnê Leão Web |
| CARNE_LEAO_TIPO | integer(4) |  | S | Tipo Carnê Leão |
| CARNE_LEAO_CODIGO | varchar(12) |  | S | Código Carnê Leão |
| CARNE_LEAO_OCUPACAO_PADRAO | integer(4) |  | S | Ocupação Carnê Leão |
