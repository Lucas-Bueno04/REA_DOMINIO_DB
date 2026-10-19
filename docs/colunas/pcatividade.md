# PCATIVIDADE — Atividades
20 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_ATIVIDADE | integer(4) | PK |  | Código |
| NOME | varchar(60) |  |  | Nome |
| PERIODICIDADE | tinyint(1) |  |  | PERIODICIDADE (1=MENSAL/ 2=BIMESTRAL/ 3=TRIMESTRAL/ 4=QUADRIMESTRAL/ 6=SEMESTRAL/ 12=ANUAL / 24=BIENAL / 36=TRIENAL / 48=QUADRIENAL / 60=QUINQUENAL / 98=DIÁRIA / 99=SEM PERIODICIDADE) |
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
| ATIVIDADE_SISTEMA | char(1) |  |  | É uma atividade executada e concluída no sistema (S/N) |
| AGENDA_OBRIGACAO | char(1) |  |  | Faz parte da agenda de obrigação da empresa (S/N) |
| VENCIMENTO_LEGAL_DIA | tinyint(1) |  |  | Vencimento legal - Dias |
| VENCIMENTO_LEGAL_TIPO | tinyint(1) |  |  | Vencimento legal - Tipo (1=Dias corridos direto/ 2=Dias corridos antecipados/ 3=Dias corridos adiado/ 4=Dias úteis) |
| VENCIMENTO_LEGAL_MES | tinyint(1) |  |  | Vencimento legal - Mês (1=Anterior ao vencimento/ 2=Informar quantidade de meses anteriores ao vencimento/ 3=No mesmo do vencimento) |
| VENCIMENTO_LEGAL_MES_ANTERIOR | tinyint(1) |  |  | Vencimento legal - Meses anteriores |
| VENCIMENTO_LEGAL_BIMESTRE1 | tinyint(1) |  |  | Vencimento legal - Mês 1o Bimestre |
| VENCIMENTO_LEGAL_BIMESTRE2 | tinyint(1) |  |  | Vencimento legal - Mês 2o Bimestre |
| VENCIMENTO_LEGAL_BIMESTRE3 | tinyint(1) |  |  | Vencimento legal - Mês 3o Bimestre |
| VENCIMENTO_LEGAL_BIMESTRE4 | tinyint(1) |  |  | Vencimento legal - Mês 4o Bimestre |
| VENCIMENTO_LEGAL_BIMESTRE5 | tinyint(1) |  |  | Vencimento legal - Mês 5o Bimestre |
| VENCIMENTO_LEGAL_BIMESTRE6 | tinyint(1) |  |  | Vencimento legal - Mês 6o Bimestre |
| VENCIMENTO_LEGAL_TRIMESTRE1 | tinyint(1) |  |  | Vencimento legal - Mês 1o Trimestre |
| VENCIMENTO_LEGAL_TRIMESTRE2 | tinyint(1) |  |  | Vencimento legal - Mês 2o Trimestre |
| VENCIMENTO_LEGAL_TRIMESTRE3 | tinyint(1) |  |  | Vencimento legal - Mês 3o Trimestre |
| VENCIMENTO_LEGAL_TRIMESTRE4 | tinyint(1) |  |  | Vencimento legal - Mês 4o Trimestre |
| VENCIMENTO_LEGAL_QUADRIMESTRE1 | tinyint(1) |  |  | Vencimento legal - Mês 1o Quadrimestre |
| VENCIMENTO_LEGAL_QUADRIMESTRE2 | tinyint(1) |  |  | Vencimento legal - Mês 2o Quadrimestre |
| VENCIMENTO_LEGAL_QUADRIMESTRE3 | tinyint(1) |  |  | Vencimento legal - Mês 3o Quadrimestre |
| VENCIMENTO_LEGAL_SEMESTRE1 | tinyint(1) |  |  | Vencimento legal - Mês 1o Semestre |
| VENCIMENTO_LEGAL_SEMESTRE2 | tinyint(1) |  |  | Vencimento legal - Mês 2o Semestre |
| VENCIMENTO_LEGAL_ANUAL | tinyint(1) |  |  | Vencimento legal - Mês Ano |
| AVISO_INICIO_ATIVIDADE | char(1) |  |  | Emitir avisos sobre início da atividade ao acessar o sistema (S/N) |
| AVISO_INICIO_ATIVIDADE_DIA | tinyint(1) |  |  | Número de dias úteis de antecedência - Início |
| AVISO_VENCIMENTO_ATIVIDADE | char(1) |  |  | Emitir avisos sobre vencimento da atividade ao acessar o sistema (S/N) |
| AVISO_VENCIMENTO_ATIVIDADE_DIA | tinyint(1) |  |  | Número de dias úteis de antecedência - Vencimento |
| I_MODULO | integer(4) |  | S | Código do módulo |
| I_MENU | integer(4) |  | S | Código do menu |
| I_SUBMENU | integer(4) |  | S | Código da opção |
| I_UF | integer(4) |  | S | Código da UF |
| I_OPCAO | integer(4) |  | S | Código da opção |
| CONSIDERAR_SABADO_DIA_UTIL | char(1) |  |  | Considerar sábado como dia útil (S/N) |
| VENCIMENTO_LEGAL_CONSIDERAR_SABADO_DIA_UTIL | char(1) |  |  | Vencimento legal - Considerar sábado como dia útil (S/N) |
| PERMITIR_ANEXAR_COMPROVANTE | char(1) |  |  | Permite anexar comprovante |
| VERIFICAR_COMPROVANTE | char(1) |  |  | Verificar comprovante |
| PARTE_TEXTO_COMPROVANTE | varchar(100) |  |  | Parte do texto no comprovante |
| VALIDAR_COMPETENCIA_CONFORME_DATA_COMPROVANTE | char(1) |  |  | Validar competência referência conforme data do comprovante |
