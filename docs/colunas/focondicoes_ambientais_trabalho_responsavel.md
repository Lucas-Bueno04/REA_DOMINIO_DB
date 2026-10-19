# FOCONDICOES_AMBIENTAIS_TRABALHO_RESPONSAVEL — Ambiente de trabalho.
62 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| DATA_INICIO | date(4) | PK |  | Data início da condição. |
| SEQUENCIAL | integer(4) | PK |  | Código Sequencial |
| CPF | varchar(11) |  |  | CPF do responsável. |
| NIS_PIS | varchar(11) |  | S | NIS/PIS do responsável. |
| NOME | varchar(70) |  | S | Nome do responsável. |
| ORGAO_CLASSE | smallint(2) |  | S | Orgão de classe (1=CRM/2=CREA/3=Outros). |
| DESCRICAO_ORGAO_CLASSE | varchar(20) |  | S | Descrição do órgão de classe |
| NUMERO_ORGAO_CLASSE | varchar(14) |  | S | Número do órgão de classe |
| UF_ORGAO_CLASSE | integer(4) |  | S | UF do órgão de classe |
