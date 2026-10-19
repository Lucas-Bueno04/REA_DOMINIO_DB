# PCVINCULO_PROCESSO_ATIVIDADE — Vínculo entre processos e empresas - Atividades
3 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_VINCULO | integer(4) | PK |  | Código do vínculo |
| I_SEQUENCIAL_ATIVIDADE | integer(4) | PK |  | Sequencial |
| ORDEM | integer(4) |  |  | Ordem |
| I_ATIVIDADE | integer(4) |  |  | Código da atividade |
| COMPETENCIA_INICIO | date(4) |  |  | A partir de |
| VENCIMENTO_DIA | tinyint(1) |  |  | Vencimento - Dias |
| VENCIMENTO_TIPO | tinyint(1) |  |  | Vencimento - Tipo (1=Dias corridos direto/ 2=Dias corridos antecipados/ 3=Dias corridos adiado/ 4=Dias úteis) |
| VENCIMENTO_BIMESTRE1 | tinyint(1) |  |  | Vencimento - Mês 1o Bimestre |
| VENCIMENTO_BIMESTRE2 | tinyint(1) |  |  | Vencimento - Mês 2o Bimestre |
| VENCIMENTO_BIMESTRE3 | tinyint(1) |  |  | Vencimento - Mês 3o Bimestre |
| VENCIMENTO_BIMESTRE4 | tinyint(1) |  |  | Vencimento - Mês 4o Bimestre |
| VENCIMENTO_BIMESTRE5 | tinyint(1) |  |  | Vencimento - Mês 5o Bimestre |
| VENCIMENTO_BIMESTRE6 | tinyint(1) |  |  | Vencimento - Mês 6o Bimestre |
| VENCIMENTO_TRIMESTRE1 | tinyint(1) |  |  | Vencimento - Mês 1o Trimestre |
| VENCIMENTO_TRIMESTRE2 | tinyint(1) |  |  | Vencimento - Mês 2o Trimestre |
| VENCIMENTO_TRIMESTRE3 | tinyint(1) |  |  | Vencimento - Mês 3o Trimestre |
| VENCIMENTO_TRIMESTRE4 | tinyint(1) |  |  | Vencimento - Mês 4o Trimestre |
| VENCIMENTO_QUADRIMESTRE1 | tinyint(1) |  |  | Vencimento - Mês 1o Quadrimestre |
| VENCIMENTO_QUADRIMESTRE2 | tinyint(1) |  |  | Vencimento - Mês 2o Quadrimestre |
| VENCIMENTO_QUADRIMESTRE3 | tinyint(1) |  |  | Vencimento - Mês 3o Quadrimestre |
| VENCIMENTO_SEMESTRE1 | tinyint(1) |  |  | Vencimento - Mês 1o Semestre |
| VENCIMENTO_SEMESTRE2 | tinyint(1) |  |  | Vencimento - Mês 2o Semestre |
| VENCIMENTO_ANUAL | tinyint(1) |  |  | Vencimento - Mês Ano |
| INICIO_DIA | tinyint(1) |  |  | Início - Dias |
| INICIO_MES | tinyint(1) |  |  | Início - Mês (1=Anterior ao vencimento/ 2=Informar quantidade de meses anteriores ao vencimento/ 3=No mesmo do vencimento) |
| INICIO_MES_ANTERIOR | tinyint(1) |  |  | Início - Meses anteriores |
| COMPETENCIA_MES | tinyint(1) |  |  | Competência de referencia - Mês (1=Anterior ao vencimento/ 2=Informar quantidade de meses anteriores ao vencimento/ 3=No mesmo do vencimento) |
| COMPETENCIA_MES_ANTERIOR | tinyint(1) |  |  | Competência de referencia - Meses anteriores |
| DEPENDENTE | char(1) |  |  | Atividade dependente (S/N) |
| ENCERRAR | char(1) |  |  | Encerrar (S/N) |
| COMPETENCIA_ENCERRAMENTO | date(4) |  | S | Competência de encerramento |
| USUARIO_ENCERRAMENTO | varchar(30) |  | S | Usuário que encerrou |
| VENCIMENTO_MES | integer(4) |  |  | Vencimento - Mês |
| VENCIMENTO_ANO | integer(4) |  |  | Vencimento - Ano |
