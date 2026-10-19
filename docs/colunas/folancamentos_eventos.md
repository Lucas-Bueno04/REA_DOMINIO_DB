# FOLANCAMENTOS_EVENTOS — Lançamentos de eventos para o cálculo
226.043 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| I_EVENTOS | integer(4) | PK |  | Código do evento |
| TIPO_PROCESSO | smallint(2) | PK |  | Tipo do processo: 11=Mensal/31=1ª semana/32=2ª semana/33=3ª semana/34=4ª semana/35=Última semana/36=Todas as semanas/41=Adiantamento/42=Complementar/51=Adiantamento 13º salário/52=13º salário |
| TIPO_LANCAMENTO | smallint(2) | PK |  | Tipo do lançamento: 1=Mensal/2=Fixo |
| COMPETENCIA_INICIAL | date(4) | PK |  | Competência inicial |
| COMPETENCIA_FINAL | date(4) |  | S | Competência final |
| MESES | smallint(2) |  | S | Meses (Soma binária) |
| PRIORIDADE | integer(4) |  |  | Prioridade do lançamento (Utilizado para definir a prioridade de lançamentos temporários originados na versão 7.4A03 ou anterior) |
| VALOR_INFORMADO | numeric(13) |  |  | Valor informado |
| VALOR_CALCULADO | numeric(13) |  | S | Valor calculado (Alterar Cálculo) |
| FORMA_RATEIO_PLANO_SAUDE | smallint(2) |  | S | Forma do rateio do plano de saúde: 0=Não rateado/1=Quantidade de beneficiários/2=Percentual definido/3=Somente titular |
| ORIGEM_LANCAMENTO | smallint(2) |  |  | Origem do lançamento: 1=Lançamento de eventos/2=Alterar Cálculo/3=Importação de lançamentos/4=Domínio Atendimento/5=Alteração retroativa de rubricas/6=Cadastro de empregados/7=Beneficios Digital Banking/8=RPA/9=Importação API |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro: 0=Sistema/1=Importação de tabelas/2=Importação de leiaute/3=Conversão |
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| FORMA_RATEIO_PENSAO_ALIMENTICIA | smallint(2) |  |  | Frm de rateio da pensão alimentícia. (0=Não rateado/1=Rateio pela qtd de ben/2=Rat do valor da rubrica por percentual definido) |
| COMPETENCIA_ALTERACAO | date(4) |  | S | Competência da alteração. |
| DATA_PAGAMENTO_ALTERA_CALCULO | date(4) |  | S | Data de pagamento gerada no altera cálculo |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
