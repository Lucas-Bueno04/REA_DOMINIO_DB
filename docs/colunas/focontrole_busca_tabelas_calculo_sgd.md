# FOCONTROLE_BUSCA_TABELAS_CALCULO_SGD — Tabela de controle para buscar atualizações das tabelas de cálculo da Folha no SGD por dia.
15.280 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| DATA_BUSCA | date(4) | PK |  | Data da busca. |
| HORARIO_BUSCA | time(8) | PK |  | Horário da busca. |
| TIPO_TABELA_CALCULO | smallint(2) | PK |  | Tipo da tabela de cálculo. (1=IRRF Progressiva/2=INSS e Salário Família/3=Salário Mínimo/4=IRRF PLR) |
