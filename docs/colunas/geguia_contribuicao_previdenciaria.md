# GEGUIA_CONTRIBUICAO_PREVIDENCIARIA — Guia da contribuição previdenciária.
22.483 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| COMPETENCIA | date(4) | PK |  | Competência. |
| TIPO_GUIA | smallint(2) | PK |  | Tipo de guia. (1=Mensal/2=13º salário/3=Tributos federais) |
| DATA_VENCIMENTO | date(4) |  |  |  |
| VALOR_RECOLHER | numeric(13) |  |  |  |
| CODI_EMP_ESCRITA_FISCAL | integer(4) |  | S |  |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Imp. tabelas/2=Imp. layout/3=Imp. tabelas concorrentes) |
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| CONSIDERAR_SALDO_INFERIOR_10_REAIS | char(1) |  | S | Considerar saldo inferior a 10 reais (S/N) |
| MODULO_ORIGEM | smallint(2) |  |  | Modulo origem (5=Escrita Fiscal, 12=Folha, 0=Indefinido) |
| SALDO_DEVEDOR | numeric(13) |  |  | Saldo devedor |
