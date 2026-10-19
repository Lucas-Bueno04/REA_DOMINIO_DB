# FOSIMULACAO_RESCISAO — Simulação de rescisão
1.100 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_SIMULACAO_RESCISAO | integer(4) | PK |  | Sequencial de simulação da rescisão. |
| DESCRICAO | varchar(100) |  |  | Descrição. |
| DATA_DEMISSAO | date(4) |  |  | Data de demissão. |
| MOTIVO | smallint(2) |  |  | Motivo da rescisão. |
| DATA_AVISO_PREVIO | date(4) |  | S | Data do aviso prévio. |
| TIPO_AVISO_PREVIO | smallint(2) |  |  | Tipo de aviso prévio. (1=Trabalhado/2=Indenizado/3=Ausência/Dispensa) |
| DATA_PAGAMENTO | date(4) |  |  | Data de pagamento. |
| INFORMAR_VALOR_LIQUIDO_MES_ANTERIOR | smallint(2) |  |  | Informar o valor líquido do mês anterior. (0=Não/1=Sim) |
| CUMPRIU_TODA_CARGA_HORARIA_SEMANA_RESCISAO | smallint(2) |  |  | Cumpriu toda a carga horária da semana da rescisão. (0=Não/1=Sim) |
| SABADO_COMPENSADO | smallint(2) |  |  | Sábado compensado. (2=Não/1=Sim) |
| CODIGO_SAQUE_FGTS | char(2) |  |  | Código do saque FGTS. |
| CODIGO_CAUSA_AFASTAMENTO | char(3) |  | S | Código/Causa do afastamento. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
| CALCULAR_SALDO_SALARIO_MP_936 | smallint(2) |  |  | Calcular saldo de salário proporcional a redução da MP 936. 0=Não/1=Sim |
| DESCONTAR_FERIAS_PAGAS_MAIOR | smallint(2) |  |  | Descontar férias pagas a maior. 0=Não/1=Sim |
| CONSIDERAR_SABADO_COMPENSADO_AVO_13_FERIAS | smallint(2) |  | S | Considerar o sabado compensado para contagem de avos de 13 e ferias: 0=Não/1=Sim |
