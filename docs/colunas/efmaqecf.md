# efmaqecf — Maquinas ECF
8 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | codi_emp |
| codi_mec | integer(4) | PK |  | codi_mec |
| nser_mec | char(21) |  |  | nser_mec |
| desc_mec | char(40) |  | S | desc_mec |
| sald_mec | numeric(16) |  | S | sald_mec |
| contadorf_mec | integer(4) |  | S | Nro do ultimo contador final digitado |
| reducaoz_mec | integer(4) |  | S | Modelo do documento fiscal |
| cro_mec | integer(4) |  | S | Valor Acumulado no Contador de Reinicio de Operacao |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| tipo_mec | tinyint(1) |  |  | Tipo de equipamento (1-ECF-MR/2-ECF-IF-INTERLIGADO A UAP/3-OUTROS/4-ECF-PDV) |
| modelo_mec | char(100) |  | S | Modelo |
| I_MODELO_ESPECIE | char(2) |  |  | Código da espécie |
| DETALHAR_ORDEM_ALIQUOTA | char(1) |  |  | Detalhar a ordem das alíquotas (S/N) |
