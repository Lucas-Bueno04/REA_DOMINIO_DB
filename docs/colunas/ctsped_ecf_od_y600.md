# CTSPED_ECF_OD_Y600 — SPED ECF - Outros Dados - Registro Y600
6.663 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_OUTROS_DADOS | integer(4) | PK |  | Sequencial Outros Dados |
| I_SOCIO_TITULAR | integer(4) | PK |  | Sequencial Interno |
| DATA | date(4) |  |  | Data |
| I_SOCIO | integer(4) |  |  | Código do sócio |
| TIPO | char(1) |  |  | Tipo (S - Sócio/A - Administrador/R - Representante Legal/E - Empresário) |
| QUALIFICACAO | integer(4) |  |  | Qualificação |
| VALOR_REMUNERACAO | numeric(14) |  |  | Remuneração |
| VALOR_LUCRO_DIVIDENDO | numeric(14) |  |  | Lucros/Dividendos |
| VALOR_JUROS_CAPITAL_PROPRIO | numeric(14) |  |  | Juros capital próprio |
| VALOR_DEMAIS_RENDIMENTOS | numeric(14) |  |  | Demais rendimentos |
| VALOR_IRRF | numeric(14) |  |  | IRRF |
| CPF_CNPJ | varchar(14) |  |  | CPF/CNPJ |
| DATA_INGRESSO | date(4) |  | S | Data ingresso |
| DATA_SAIDA | date(4) |  | S | Data saída |
| PARTICIPACAO | numeric(15) |  |  | Participação % |
| CAPITAL_VOTANTE | numeric(5) |  |  | Capital votante % |
| TIPO_INDICADOR_QUALIFICACAO | varchar(2) |  | S | Indicador de qualificação |
