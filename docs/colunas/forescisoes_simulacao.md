# FORESCISOES_SIMULACAO — Simulação da rescisão
1.902 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Codigo empresa |
| I_EMPREGADOS | integer(4) | PK |  | Empregado |
| DEMISSAO | date(4) |  |  | Data Demissao |
| MOTIVO | integer(4) |  |  | Motivo |
| DATA_AVISO | date(4) |  | S | Data aviso |
| AVISO_INDENIZADO | char(1) |  |  | Aviso indenizado |
| AVOS_PAGO_13 | smallint(2) |  |  | Avos pago 13 |
| NUM_FER_VENC | smallint(2) |  |  | No. ferias vencidas |
| MESES_FER_PROP | smallint(2) |  |  | Meses ferias prop. |
| CODIGO_SAQUE_FGTS | char(2) |  | S | Codigo saque FGTS |
| SALDO_FGTS | numeric(15) |  |  | Saldo FGTS |
| FGTS_MES_ANT_DEP | char(1) |  |  | FGTS mes anterior depositado |
| SALARIO | numeric(13) |  |  | Salario |
| PROVENTOS | numeric(13) |  |  | Provento |
| DESCONTOS | numeric(13) |  |  | Desconto |
| MED_FER_VEN_I | numeric(13) |  |  | Media ferias vencidas |
| MED_FER_PRO_I | numeric(13) |  |  | Media ferias prop. |
| MED_13_I | numeric(13) |  |  | Media 13 |
| VAL_FGTS_ANT | numeric(13) |  |  | Valor FGTS anteriro |
| VAL_FGTS_RES | numeric(13) |  |  | Valor FGTS rescisao |
| PAGO_MEDIAS | char(1) |  |  | Pago medias |
| PAGO_ADICIONAIS | char(1) |  |  | Pago adicionais |
| DESC_OUTR_MOTIVO | char(30) |  | S | Desconto outro motivo |
| MIN_MES_RES | integer(4) |  |  | Minimo mes rescisao |
| DATA_PAGTO | date(4) |  |  | Data pagamento |
| RECOLHER_GRFP | char(1) |  |  | Recolher GRFC |
| DESC_FALTA | char(1) |  | S | Desconto faltas |
| BASE_FGTS_13 | numeric(13) |  |  | Base FGTS 13 |
| MAIOR_REMUNERACAO | numeric(13) |  |  | Maior remuneracao |
| BASE_IRRF_FER | numeric(13) |  |  | Base IRRF ferias |
| ABAT_IRRF_FER | numeric(13) |  |  | Abatimento IRRF ferias |
| TAXA_IRRF_FER | numeric(5) |  |  | Taxa IRRF ferias |
| BASE_IRRF_13 | numeric(13) |  |  | Base IRRF 13 |
| ABAT_IRRF_13 | numeric(13) |  |  | Abatimento IRRF 13 |
| TAXA_IRRF_13 | numeric(5) |  |  | Taxa IRRF 13 |
| VALOR_IRRF_FER | numeric(13) |  |  | Valor IRRF ferias |
| DED_IRRF_FER | numeric(13) |  |  | Deducao IRRF ferias |
| VALOR_IRRF_13 | numeric(13) |  |  | Valor IRRF 13 |
| DED_IRRF_13 | numeric(13) |  |  | Deducao IRRF 13 |
| DIAS_ESTAB | integer(4) |  |  | Dias estabilidade |
| MEDIA_INFORMADA | tinyint(1) |  |  | Media informada |
| DIAS_AVISO | numeric(5) |  | S | Dias aviso |
| VALOR_MED_AVISO | numeric(13) |  | S | Valor media do aviso |
| TIPO | integer(4) | PK |  | Tipo de cálculo de rescisão. (1=Normal/2=Complementar/3=Parcial/4=Simulação) |
| DISSIDIO_ACORDO_DATA | date(4) |  | S | Data acordo dissidio |
| INSS_EMPRESA_13 | numeric(13) |  | S | INSS empresa 13 |
| ACID_TRAB_13 | numeric(13) |  | S | Acid. trabalho 13 |
| INSS_TERC_13 | numeric(13) |  | S | INSS terceiro 13 |
| VALOR_PIS_13 | numeric(13) |  | S | Valor PIS 13 |
| DESC_LEI_IRRF_13 | numeric(13) |  | S | Desconto IRRF 13 |
| DESC_LEI_IRRF_FER | numeric(13) |  | S | Desconto IRRF ferias |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| I_PAGTO | integer(4) |  | S | Sequencial de pagamento |
| DSR_SEMANA_RESC | tinyint(1) |  |  | Indica se é para calcular DSR na semana da rescisao |
| AVISO_PREVIO | tinyint(1) |  |  | Aviso Previo (1=trab,2=indeizado,3=ausencia/dispensa) |
| REPOSICAO_VAGA | tinyint(1) |  |  | A vaga sera reposta (1=sim, 0=nao) |
| COMPLEMENTO_SALDO_FGTS | numeric(15) |  |  | Complemento do saldo do fgts |
| COMPETENCIA | date(4) |  | S | Competência da rescisão |
| TIPO_PROCESS | integer(4) |  | S | Tipo de processo da rescisão |
| COMPROVOU_NOVO_EMPREGO | smallint(2) |  |  | EMPREGADO COMPROVOU TER NOVO EMPREGO DURANTE O PERIODO 1 SIM 2 NAO |
| DISPENSOU_EPR | smallint(2) |  |  | EMPREGADOR DISPENSOU O EMPREGADO 1 SIM 2 NAO |
| PENS_ALIM_REMUN | numeric(5) |  |  | PENSAO ALIMENTICIA REMUNERACAO |
| PENS_ALIM_FGTS | numeric(5) |  |  | PENSAO ALIMENTICIA FGTS |
| SABADO_COMPENSADO | smallint(2) |  |  | SABADO COMPENSADO 1 SIM 2 NAO |
| TIPO_COMPLEMENTO | tinyint(1) |  |  | Tipo do complemento. (1=Dissídio/2=Acordo/3=CCT/4=Outros/5=Comissões) |
| CODIGO_AFASTAMENTO | char(3) |  | S | Código do afastamento: SJ2, JC2, RA2, FE2, FE1, RA1, SJ1, FT1, PD0, RI2, CR0, FM0, N1, N2, ACO |
| CALCULAR_MULTA_ATRASO_PAGAMENTO | smallint(2) |  | S | Calcular multa em decorrência de atraso no pagamento art. 477, § 8°/CLT (0=Não/1=Sim) |
| GERAR_LIQUIDO_MES_ANTERIOR | smallint(2) |  |  | Gerar liquido mês anterior: 0=Não/2=Sim |
| MEDIAS_CONSIDEROU_MES_RESCISAO | smallint(2) |  |  | Considerou mês da rescisão para calculo de médias. |
| DESCONTAR_ESTOURO_RESCISAO | smallint(2) |  | S | Efetuar desconto do estouro calculado na rescisão: (0=Não/1=Sim) |
| EMPREGADOR_IMPEDIU_TRABALHO_AVISO_PREVIO | smallint(2) |  | S | Empregador impediu o trabalho durante o aviso prévio: (0=Não/1=Sim) |
| DIAS_INDENIZADOS | numeric(5) |  | S | Dias indenizados |
| TOTAL_MESES_SALDO_BANCO_HORAS | smallint(2) |  |  | Total de meses para saldo de banco de horas. |
| TOTAL_MESES_GRATIFICACOES | smallint(2) |  |  | Total de meses para gratificações |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo - Renomeado |
| DESCONTAR_FALTA_DSR_POSTERIOR_RESCISAO | smallint(2) |  |  | Descontar as faltas DSR após a data de demissão. (0=Não/1=Sim) |
| REGISTRO_OBITO | varchar(32) |  | S | Registro de óbito. |
| ESTORNAR_DESCONTO_FALTA_DSR_DATA_POSTERIOR_RESCISAO | smallint(2) |  |  | Estornar o desconto da falta DSR com data posterior a rescisão. (0=Não/1=Sim) |
| CODIGO_AFASTAMENTO_RAIS | smallint(2) |  | S | Código do afastamento da RAIS. |
| RESCISAO_MOTIVO_30_COM_CALCULO_REDUCAO | smallint(2) |  |  | 0=Não / 1=Sim |
| GERAR_TERMO_RESCISAO_CONTRATO_TRABALHO | smallint(2) |  |  | Gerar termo de rescisão do contrato de trabalho. (0=Não/1=Sim) |
| ZERAR_VERBAS_RESCISORIAS_DEVIDO_RECLAMATORIA_TRABALHISTA | smallint(2) |  |  | Zerar as verbas rescisórias devido a reclamatória trabalhista. (0=Não/1=Sim) |
| PAGAR_VALORES_PARCELAS_DIFERENCAS_SALARIAIS_EMPRESA_DESTINO | smallint(2) |  |  | Pagar os valores de parcelas das diferenças salariais na empresa destino. (0=Não/1=Sim) |
| PAGAR_VALOR_PROPORCIONAL_PARCELA_COMPETENCIA_RESCISAO | smallint(2) |  |  | Pagar o valor proporcional da parcela da competência da rescisão. (0=Não/1=Sim) |
| DATA_COMPLEMENTO | date(4) |  | S | Data do complemento. |
| DATA_PROJECAO_AVISO_PREVIO | date(4) |  | S | Data de projeção do aviso prévio indenizado. |
| CONSIDERAR_FGTS_CCT_PARCTO_CALC_FGTS_MULTA_RESC_CONTRIB_SOCIAL | smallint(2) |  |  | Considerar o valor do FGTS CCT do parcelamento para o cálculo de FGTS multa rescisão e Contribuição Social. (0=Não/1=Sim) |
| GRAVOU_DADOS_FERIAS_VENCIDAS_PROPORCIONAIS | smallint(2) |  |  | Gravou os dados para memória de cálculo das férias vencidas/proporcionais. (0=Não/1=Sim) |
| INDICATIVO_PENSAO_ALIMENTICIA | smallint(2) |  |  | Indicativo de pensão alimentícia. (0=Não existe/1=Percentual/2=Valor/3=Percentual e valor) |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| MOTIVO_COMPLEMENTO | varchar(256) |  | S | Motivo do complemento. |
| POSSUI_EMPRESTIMO_CONSIGNADO_GARANTIA_FGTS | smallint(2) |  |  | Possui empréstimo consignado com garantia de FGTS. (0=Não/1=Sim) |
| MATRICULA_INSTITUICAO_EMPRESTIMO_CONSIGNADO_FGTS | varchar(5) |  | S | Matrícula da instituição do empréstimo consignado FGTS. |
| NUMERO_CONTRATO_EMPRESTIMO_CONSIGNADO_FGTS | varchar(15) |  | S | Núemro do contrato do empréstimo consignado FGTS. |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| MOTIVO_ESOCIAL | integer(4) |  | S | Motivo eSocial |
| DIAS_ESTABILIDADE_MP_936 | integer(4) |  | S | Dias de estabilidade devido a medidas de proteção de empregado MP 936 |
| CALCULAR_SALDO_SALARIO_MP_936 | smallint(2) |  |  | Calcular saldo de salário proporcional a redução da MP 936. 0=Não/1=Sim |
| ANTES_IMPLANTACAO_DECRETO_10060_2019 | smallint(2) |  |  | Anterior a implantação de verificação do decreto 10060/2019. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| DESCONTAR_FERIAS_PAGAS_MAIOR | smallint(2) |  |  | Descontar férias pagas a maior. 0=Não/1=Sim |
| DESLIGAMENTO_DECISAO_JUDICIAL | smallint(2) |  |  | Desligamento por decisão judicial |
| NUMERO_PROCESSO_DESLIGAMENTO | varchar(20) |  | S | Número do processo - desligamento judicial. |
| NOVO_CPF | char(11) |  | S | Novo CPF usado na mudança de CPF. |
| I_TABCALCINSS | date(4) |  | S | Tabela de cálculo INSS |
| REENVIAR_ROTINA_AUTOMATICA_S2299 | smallint(2) |  |  | Reenviar Rotina Automática S2299 para o eSocial. (0=Não/1=Sim) |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo |
| ANTECIPAR_VENCIMENTO_DEBITO_MES_ANTERIOR | smallint(2) |  | S | Antecipar vencimento do débito do mês anterior. (0=Não/1=Sim) |
| CALCULAR_MULTA_CARGA_HORARIA_VARIAVEL_HORAS_INFORMADAS | numeric(5) |  | S | Calcular multa - Art. 479/480 para carga horária variável sobre: |
| CONSIDERAR_SABADO_COMPENSADO_AVO_13_FERIAS | smallint(2) |  | S | Considerar o sabado compensado para contagem de avos de 13 e ferias: 0=Não/1=Sim |
| VALOR_PENSAO_ALIM | numeric(14) |  |  | Valor do Indicativo de pensão alimentícia para fins de retenção de FGTS |
| DATA_REGISTRO_RESCISAO | timestamp(8) |  | S | Data/hora UTC do cadastro da rescisão no sistema (ISO 8601) |
