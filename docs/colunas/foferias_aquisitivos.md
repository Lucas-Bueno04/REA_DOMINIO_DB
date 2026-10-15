# FOFERIAS_AQUISITIVOS — CADASTRO DE PERIODOS ARQUISITIVOS
23.266 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | CODIGO EMPRESA |
| I_EMPREGADOS | integer(4) | PK |  | CODIGO |
| I_FERIAS_AQUISITIVOS | integer(4) | PK |  | SEQUENCIA DE PERIODOS AQUISITIVOS |
| DATA_INICIO | date(4) |  |  | DATA DO INICIO DO PERIODO AQUISITIVO |
| DATA_FIM | date(4) |  |  | DATA DO FIM DO PERIODO AQUISITIVO |
| SITUACAO | integer(4) |  |  | SITUACAO (GOZADO, PERDIDA ETC...) |
| AFAST_PREVIDENCIA | integer(4) |  |  | DIAS AFASTADOS PELA PREVIDENCIA |
| AFAST_SEM_REMUNERACAO | integer(4) |  |  | DIAS AFASTADOS SEM RECEBER REMUNERACAO |
| AFAST_COM_REMUNERACAO | integer(4) |  |  | DIAS AFASTADOS RECEBENDO REMUNERACAO |
| DIAS_FALTAS | integer(4) |  |  | NUMERO DE DIAS DE FALTAS |
| DIAS_DIREITO | numeric(10) |  |  | NUMERO DE DIAS DE DIREITO |
| DIAS_GOZADOS | numeric(10) |  |  | NUMERO DE DIAS GOZADOS |
| DIAS_ABONO | numeric(10) |  |  | NUMERO DE DIAS CONVERTIDOS EM ABONO |
| AVOS_ADQUIRIDOS | integer(4) |  |  | NUMERO DE AVOS ADQUIRIDOS |
| LIMITE_PARA_GOZO | date(4) |  |  | DIA MAXIMO PARA INICIO O GOZO SEM MULTA |
| DATA_FIM_PERDIDA | date(4) |  | S | BACKUP DA DATA FIM QUANDO PERDIDO DIREITO A FERIAS |
| ATUALIZOU_DATA_FIM | smallint(2) |  | S | COLUNA AUXILIAR DE ALTERAÇÃO DO PERIODO AQUISITIVO |
| TIPO | smallint(2) |  |  | TIPO DE CONTROLE DO PERIODO AQUISITIVO |
| DESCONTAR_FALTAS | char(1) |  |  | DESCONTAR FALTAS |
| DIAS_DIREITO_ALTERADO | smallint(2) |  |  | INDICA SE OS DIAS DE DIREITO DO PERÍODO AQUISITIVO FORAM ALTERADOS MANUALMENTE |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| DESCONSIDERAR_AFASTAMENTO | char(1) |  |  | DESCONSIDERAR AFASTAMENTO |
| SITUACAO_ALTERADA | smallint(2) |  |  | Indica se a situação foi alterada manualmente. (0=Não/1=Sim) |
| DIAS_LICENCA_REMUNERADA_PERDA_FALTAS | numeric(10) |  |  | Dias de licença remunerada devido a perda por faltas. |
| DESCONTAR_FALTAS_NOTURNAS | char(1) |  |  | Descontar faltas noturnas. (S=Sim/N=Não/P=Parâmetro) |
| DESCONTAR_FALTAS_SUSPENSAO | char(1) |  |  | Descontar faltas por suspensão. (N=Não/S=Sim/P=Parêmetros) |
| DESCONTAR_FALTAS_PARCIAIS | char(1) |  |  | Descontar faltas parciais. (S=Sim/N=Não/P=Parâmetro) |
| HABILITAR_PERIODO_FIM_AJUSTE_ATUALIZACAO | integer(4) |  |  | Será alimentado apenas em comando de atualização onde deve ser habilitado a data fim para o usuario corrigir manualmente. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
