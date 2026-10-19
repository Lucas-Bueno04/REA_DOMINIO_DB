# FOPARMTO_CONFIGURACAO_DATA_PAGAMENTO — Configurações para as datas de pagamento dos cálculos da folha.
20.325 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| TIPO_EMPREGADO | smallint(2) | PK |  | Tipo de empregado. (1=Empregado/2=Contribuinte/3=Estagiário) |
| TIPO_PROCESSO | integer(4) | PK |  | Tipo de cálculo. |
| DECIMO_INTEGRAL_COMPETENCIA_DIFERENTE_DEZEMBRO | smallint(2) | PK |  | Configuração para o 13º integral pago em competência diferente de dezembro. (0=Não/1=Sim) |
| MES_PAGAMENTO | smallint(2) |  |  | Mês paga pagamento. (1=1º Mês subsequente/2=No mesmo mês/3=2º Mês subsequente/4=1ª Quinzena/5=2ª Quinzena) |
| FORMA_VENCIMENTO | smallint(2) |  |  | Forma de vencimento. (1=Dias corridos direto/2=Dias corridos adiados/3=Dias corridos antecipados/4=Dias úteis/5=Último dia útil) |
| TOTAL_DIAS | smallint(2) |  | S | Total de dias para o cálculo da data de pagamento. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout/3=Importação tabelas concorrentes ) |
| ANTECIPAR_DATA_PAGAMENTO_SABADO | smallint(2) |  |  | Antecipar pagamento quando a data do pagamento cair no sábado. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
