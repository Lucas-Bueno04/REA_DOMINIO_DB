# FOCONTROLE_ATUALIZACAO_TABELAS_CALCULO_SGD — Tabela de controle para verificação de novas versões das tabelas de cálculo da folha no SGD.
4 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| TIPO_TABELA_CALCULO | smallint(2) | PK |  | Tipo da tabela de cálculo. (1=IRRF Progressiva/2=INSS e Salário Família/3=Salário Mínimo/4=IRRF PLR) |
| ATUALIZAR | smallint(2) |  |  | Atualizar. (0=Não/1=Sim) |
