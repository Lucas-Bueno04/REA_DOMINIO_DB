# hneventos — Eventos - Cadastro - Novo Honorarios
46 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_evento | integer(4) | PK |  | Codigo |
| desc_evt | varchar(80) |  |  | Descricao |
| somafat_evt | char(1) |  |  | Soma no faturamento (S/N) |
| somairrf_evt | char(1) |  |  | Soma IRRF (S/N) |
| somaiss_evt | char(1) |  |  | Soma ISS (S/N) |
| aliqirrf_evt | numeric(5) |  |  | Aliquota do IRRF |
| aliqiss_evt | numeric(5) |  |  | Aliquota ISS |
| provdesc_evt | char(1) |  |  | Provento/Desconto (P/D) |
| formula_evt | varchar(1000) |  | S | Formula do evento |
| conta_evt | integer(4) |  |  | Conta Contabil |
| chis_evt | integer(4) |  |  | Codigo do Historico Padrao |
| somacrf_evt | char(1) |  |  | Soma Contribuicoes Retidas na Fonte (S/N) |
| aliqcrf_evt | numeric(5) |  |  | Aliquota das Contribuicoes Retidas na Fonte |
| compl_evt | varchar(80) |  |  | Complemento do evento |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| somainss_evt | char(1) |  |  | Soma INSS (S/N) |
| aliqinss_evt | numeric(5) |  |  | Aliquota do INSS |
| somaissr_evt | char(1) |  |  | Soma ISS Retido (S/N) |
| aliqissr_evt | numeric(5) |  |  | Aliquota do ISS Retido |
| unidade_evt | char(1) |  |  | Unidade (V=Valor/Q=Quantidade/P=Percentual) |
| referencia_evt | numeric(13) |  | S | Referencia |
