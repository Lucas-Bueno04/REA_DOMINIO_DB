# CTGRUPOSDFC_INDIRETO — Estrutura DFC - Metodo Indireto
4.271 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_INDIRETO | integer(4) | PK |  | Codigo |
| ORDEM | integer(4) |  |  | Ordem |
| ATIVIDADE | integer(4) |  |  | Atividade (1=Operacionais/2=Investimento/3=Financiamento) |
| DESCRICAO | varchar(128) |  |  | Descricao |
| NATUREZA | char(1) |  |  | Natureza (A=Analitica/S=Sintetica/V=Atividade) |
| TIPO | char(1) |  | S | Tipo (L=Lancamentos/ P=Saldo Periodo/ D=Total Debito/ J=Lucro-Prejuizo/ S=Sub-Total/ T=Total/ C=Total crédito/ A=Lucro antes do IR/ I=Inverter natureza do saldo/ E=Saldo-Exercício) |
