# HRCONTRATO_EXCEDENTE_FATURAMENTO — Contrato - Excedentes de faturamento
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_CONTRATO | integer(4) | PK |  | Codigo contrato |
| I_EXCEDENTE | integer(4) | PK |  | Sequencial |
| EXCEDENTE | char(1) |  |  | Execente (C=Lançamentos contábeis/ F=Lançamentos fiscais/ T=Horas trabalhadas/ E=Funcionários) |
| I_EVENTO | integer(4) |  |  | Evento |
| VALOR | numeric(13) |  |  | Valor |
| A_PARTIR_DE | date(4) |  |  | A partir de |
| ENCERRAR | char(1) |  |  | Encerrar (S/N) |
| ENCERRADO_EM | date(4) |  | S | Encerrado em |
