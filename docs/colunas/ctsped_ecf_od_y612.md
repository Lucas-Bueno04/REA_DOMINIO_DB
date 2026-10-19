# CTSPED_ECF_OD_Y612 — SPED ECF - Outros Dados - Registro Y612
128 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_OUTROS_DADOS | integer(4) | PK |  | Sequencial Outros Dados |
| I_RENDIMENTOS | integer(4) | PK |  | Sequencial Interno |
| DATA | date(4) |  |  | Data |
| TIPO | char(1) |  |  | Tipo (S - Sócio/A - Administrador/R - Representante Legal/E - Empresário) |
| QUALIFICACAO | integer(4) |  |  | Qualificação |
| VALOR_RENDIMENTO_TRABALHO | numeric(14) |  |  | Rendimentos do trabalho |
| VALOR_DEMAIS_RENDIMENTOS | numeric(14) |  |  | Demais rendimentos |
| VALOR_IRRF | numeric(14) |  |  | IRRF |
| I_DIRIGENTE_CONSELHEIRO | integer(4) |  | S | Vinculo com CTDIRIGENTES_CONSELHEIROS |
