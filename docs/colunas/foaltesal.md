# foaltesal — Salarios - Processos
27.782 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_empregados | integer(4) | PK |  | Empregado |
| competencia | date(4) | PK |  | Data |
| tipo_alt_grade | smallint(2) | PK |  | Tipo da alteração salarial: (1=Normal, 2=Valor hora-aula, 3=Grade salarial, 4=Resilição Professor) |
| novo_salario | numeric(30) |  |  | Valor |
| motivo | integer(4) |  |  | Motivo |
| nivel_anterior | integer(4) |  |  | Nivel anterior |
| classe_anterior | char(1) |  |  | Classe anterior |
| referencia_anterior | integer(4) |  |  | Ref. anterior |
| novo_nivel | integer(4) |  |  | Nivel novo |
| nova_classe | char(1) |  |  | Classe nova |
| nova_referencia | integer(4) |  |  | Ref. nova |
| retroativo | tinyint(1) |  |  | Aumento retroativo |
| retroativo_data | date(4) |  |  | Data retroativa |
| retroativo_ajuste | tinyint(1) |  |  | Forma do ajuste: (0-4) |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| forma_alteracao | tinyint(1) |  |  | Forma de alteração: (1=Novo salário/2=Adicionar valor/3=Percentual de aumento/4=Nível/5=Percentual CCT/6=Valor antecipação/7=Percentual CCT/8=Percentual variável/9=Conforme índice) |
| valor_adicionado | numeric(30) |  | S | Valor adicionado |
| perc_aumento | numeric(30) |  | S | Percentual de aumento |
| periodo_inicio | date(4) |  |  | Periodo inicial |
| periodo_fim | date(4) |  |  | Periodo final |
| periodo_ctrl | tinyint(1) |  |  | Controle do 1=ativo 0 = inativo |
| periodo_inicio_ret | date(4) |  |  | Periodo inicial retroativo |
| periodo_fim_ret | date(4) |  |  | Periodo final retroativo |
| periodo_ctrl_ret | tinyint(1) |  |  | Controle do 1=ativo 0 = inativo |
| salario_anterior | numeric(30) |  | S | Salario anterior |
| display | tinyint(1) |  |  | Mostrar alteração |
| GERAR_GFIP | tinyint(1) |  |  | Coluna que informa se gera GEFIP |
| ALTERACAO_CADASTRAL | smallint(2) |  |  | Alteração cadastral: (0=Não, 1=Sim) |
| ANTECIPACAO_SALARIAL | smallint(2) |  |  | Antecipação salarial: (0=Não, 1=Sim) |
| DESCONTAR_ANTECIPACAO_SALARIAL | smallint(2) |  |  | Descontar valores de antecipação salarial: (0=Não, 1=Sim) |
| CONSIDERAR_SOMENTE_PAGAMENTO_RETROATIVO | smallint(2) |  |  | Considerar a alteração somente para pagamento retroativo: (0=Não, 1=Sim) |
| GERAR_FOLHA_COMPLEMENTAR_ESPECIFICA | smallint(2) |  | S | Gerar folhas complementares específicas para esta alteração salarial: (0=Não, 1=Sim) |
| TIPO_FOLHA_PAGAMENTO_MES_ALTERACAO | smallint(2) |  |  | Tipo da folha para pagamento do mês da alteração: (11=Mensal, 42=Complementar) |
| GERAR_FOLHA_COMPLEMENTAR_ESPECIFICA_MES_ALTERACAO | smallint(2) |  | S | Gerar em folhas complementares específicas para esta alteração salarial: (0=Não, 1=Sim) |
| COMPLEMENTO_CALCULO_MES_ALTERACAO | smallint(2) |  |  | Complemento de cálculo do mês da alteração: (1=Gerar novo complemento, 2=Último complemento calculado) |
| I_FORMA_AJUSTE_PARCELAMENTO | integer(4) |  | S | Código da forma de ajuste conforme parcelamento |
| ALTERACAO_CONFORME_CONVENCAO_COLETIVA_TRABALHO | smallint(2) |  |  | Alteração salarial conforme convenção coletiva de trabalho. (0=Não/1=Sim) |
| TIPO_ALTERACAO_REMUNERACAO_DIRIGENTE_SINDICAL | smallint(2) |  | S | Tipo de alteração da remuneração do dirigente sindical. (1=Sindicato/2=Empresa) |
| REMUNERACAO_EMPRESA_DIRIGENTE_SINDICAL | numeric(30) |  | S | Remuneração da empresa para dirigente sindical. |
| REMUNERACAO_SINDICATO_DIRIGENTE_SINDICAL | numeric(30) |  | S | Remuneração do sindicato para dirigente sindical. |
| SUSPENDER_ANTECIPACAO_SALARIAL | smallint(2) |  |  | Suspender a antecipação salarial. (0=Não/1=Sim) |
| SOMAR_VALOR_ANTECIPACAO_SALARIAL_ANTERIOR | smallint(2) |  |  | Somar o valor da antecipação anterior. (0=Não/1=Sim) |
| I_INDICE_CORRECAO | integer(4) |  | S | Índice de correção. |
| CALCULAR_RESCISAO_PARCIAL_DIMINUICAO_GRADE_SALARIAL | smallint(2) |  |  | Calcular rescisão parcial devido a diminuição da grade salarial. (0=Não/1=Sim) |
| ARREDONDAMENTO | numeric(30) |  | S | Arredondamento. |
| CALCULAR_DESCONTO_ANTECIPACAO_MENOR_ANTECIPACAO | smallint(2) |  |  | Descontar a antecipação quando o valor da alteração salarial for menor que a antecipação. (0=Não/1=Sim) |
| DETALHAR_COMPETENCIAS_DESCONTAR_ANTECIPACAO_SALARIAL | smallint(2) |  |  | Detalhar as competências utilizadas para descontar a antecipação. (0=Não/1=Sim) |
| LIMITAR_VALOR_NOVO_SALARIO_VALOR_PISO_SALARIAL | smallint(2) |  |  | Limitar o valor do novo salário ao valor do piso salarial. (0=Não/1=Sim) |
| LIMITAR_DESCONTO_ANTECIPACAO_SALARIAL_VALOR_DIFERENCA | smallint(2) |  |  | Limitar o desconto de antecipação salarial ao valor das diferenças salariais. (0=Não/1=Sim) |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| DATA_PAGAMENTO | date(4) |  | S | Data de Pagamento |
| CONSIDERAR_COMPETENCIA_ALTERACAO_SALARIAL_DATA_EFEITO | smallint(2) |  |  | Considerar a competência da alteração salarial como Data Efeito. (0=Não/1=Sim) |
