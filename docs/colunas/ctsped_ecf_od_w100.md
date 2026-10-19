# CTSPED_ECF_OD_W100 — SPED ECF - Outros Dados - Registro W100
2.531 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_OUTROS_DADOS | integer(4) | PK |  | Sequencial Outros Dados |
| NOME_GRUPO_MULTINACIONAL | varchar(250) |  |  | Nome do grupo multinacional |
| A_PJ_CONTROLADORA_FINAL | char(1) |  |  | A PJ é controladora final (S/N) |
| NOME_CONTROLADORA_FINAL | varchar(250) |  |  | Nome da controladora final |
| I_JURISDICAO_CONTROLADORA_FINAL | integer(4) |  |  | Jurisdição da controladora final |
| TIN_CONTROLADORA_FINAL | varchar(250) |  |  | TIN da controladora final |
| RESPONSAVEL_DECLARACAO | integer(4) |  |  | Responsável pela declaração |
| MODALIDADE | integer(4) |  |  | Modalidade (1-Entidade substituta / 2-Preenchimento local) |
| NOME_ENTIDADE_SUBSTITUTIVA | varchar(250) |  |  | Nome da  entidade substituta/local |
| I_JURISDICAO_ENTIDADE_SUBSTITUTIVA | integer(4) |  |  | Jurisdição entidade substituta/local |
| TIN_ENTIDADE_SUBSTITUTIVA | varchar(250) |  |  | TIN da entidade substituta |
| DATA_INICIO_PERIODO_SOCIETARIO | date(4) |  | S | Data de início período societário |
| DATA_FINAL_PERIODO_SOCIETARIO | date(4) |  | S | Data final período societário |
| I_TIPO_MOEDA | integer(4) |  |  | Moeda |
| IDIOMA | char(2) |  |  | Idioma (EN-Inglês / ES-Espanhol / PT-Português) |
