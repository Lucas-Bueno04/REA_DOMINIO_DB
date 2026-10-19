# GESCP_VIGENCIA_LALUR — Sociedade em Conta de Participação - SCP - Vigência - Lalur
17 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_SCP | integer(4) | PK |  | Sequencial do SCP |
| VIGENCIA | date(4) | PK |  | Vigência |
| DESCRICAO | varchar(100) |  |  | Descrição |
| TIPO_CALCULO | tinyint(1) |  |  | Tipo de cálculo (1=Anual/Balanço de Redução e Suspensão/ 2=Trimestral/ 3=Anual/Recolhimento por estimativa/ 4=Não enquadrada) |
| CALCULAR_LUCRO_ESTIMADO | char(1) |  |  | Calcular lucro Estimado (S/N) |
| OPTAR_MENOR_CALCULO_REAL_ESTIMADO | char(1) |  |  | Optar sempre pelo menor valor a recolher entre os cálculos Real e Estimado (S/N) |
| TIPO_ATIVIDADE | char(1) |  |  | Tipo de atividade (G=Atividade geral/ R=Atividade rural/ A=Ambos) |
| CODIGO_RECOLHIMENTO_CSLL | varchar(6) |  | S | Código de recolhimento CSLL |
| CODIGO_RECOLHIMENTO_IRPJ | varchar(6) |  | S | Código de recolhimento IRPJ |
| CONTA_LUCRO_OPERACIONAL_GERAL | integer(4) |  |  | Conta - Lucro operacional gera |
| CONTA_PREJUIZO_OPERACIONAL_GERAL | integer(4) |  |  | Conta - Prejuízo operacional geral |
| CONTA_LUCRO_NAO_OPERACIONAL_GERAL | integer(4) |  |  | Conta - Lucro não operacional geral |
| CONTA_PREJUIZO_NAO_OPERACIONAL_GERAL | integer(4) |  |  | Conta - Prejuízo não operacional geral |
| CONTA_LUCRO_OPERACIONAL_RURAL | integer(4) |  |  | Conta - Lucro operacional rural |
| CONTA_PREJUIZO_OPERACIONAL_RURAL | integer(4) |  |  | Conta - Lucro não operacional rural |
| CALCULAR_LUCRO_EXPLORACAO | char(1) |  |  | Calcular Lucro da Exploração (S/N) |
| CALCULAR_BONUS_ADIMPLENCIA_FISCAL | char(1) |  |  | Calcular Bônus da Adimplência Fiscal (S/N) |
| I_ADICAO_CSLL_PARA_IRPJ | integer(4) |  | S | Adição - Contribuição Social como adição para o cálculo do IRPJ |
| CALCULAR_BONUS_ADIMPLENCIA_FISCAL_SOBRE | char(1) |  |  | Calcular sobre (B - Base de cálculo da CSLL após compensação/N - Receita Bruta) |
| COMPLEMENTO_ADICAO_CSLL_PARA_IRPJ | varchar(100) |  | S | Complemento de ContribuiÃ§Ã£o Social como adiÃ§Ã£o para o cÃ¡lculo IRPJ |
| TIPO_CONSIDERA_VALOR_ADICAO | char(1) |  |  | Valor a ser considerado na adição (CSLL devida/CSLL a recolher |
| DEFINIR_TERMINO_FRUICAO_PERSE_CSLL | char(1) |  |  | Definir término de fruição do Perse para o imposto CSLL |
| DEFINIR_TERMINO_FRUICAO_PERSE_IRPJ | char(1) |  |  | Definir término de fruição do Perse para o imposto IRPJ |
| DATA_TERMINO_FRUICAO_PERSE_CSLL | date(4) |  | S | Data término de fruição do Perse para o imposto CSLL |
| DATA_TERMINO_FRUICAO_PERSE_IRPJ | date(4) |  | S | Data término de fruição do Perse para o imposto IRPJ |
