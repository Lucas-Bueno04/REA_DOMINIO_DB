# pacontas — Contas patrimoniais - Cadastro
4 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_cta | integer(4) | PK |  | Codigo |
| desc_cta | char(40) |  |  | Descricao |
| txdepre_cta | numeric(9) |  |  | Taxa de depreciacao |
| debcre_cta | char(1) |  |  | Natureza da conta (D - devedora/C - credora) |
| corr_cta | char(1) |  |  | Sofre correcao monetaria (S/N) |
| rececorr_cta | char(1) |  |  | Incorpora correcao de outra conta (S/N) |
| ctaori_cta | integer(4) |  | S | Conta origem da correcao |
| codi_grc | integer(4) |  |  | Grupo contabil |
| cta_cor_mon_cta | integer(4) |  |  | Conta da correcao monetaria |
| ctacont_cta | integer(4) |  |  | Conta na contabilidade |
| cta_cor_dep_acum | integer(4) |  |  | Conta da correcao da depreciacao acumulada |
| cta_dep_per | integer(4) |  |  | Conta da depreciacao do periodo |
| cta_cre_dep | integer(4) |  |  | Conta credito da depreciacao |
| dmes1_cta | tinyint(1) |  |  | Coluna nao utilizada |
| dmes2_cta | tinyint(1) |  |  | Coluna nao utilizada |
| dmes3_cta | tinyint(1) |  |  | Coluna nao utilizada |
| dmes4_cta | tinyint(1) |  |  | Coluna nao utilizada |
| dmes5_cta | tinyint(1) |  |  | Coluna nao utilizada |
| dmes6_cta | tinyint(1) |  |  | Coluna nao utilizada |
| dmes7_cta | tinyint(1) |  |  | Coluna nao utilizada |
| dmes8_cta | tinyint(1) |  |  | Coluna nao utilizada |
| dmes9_cta | tinyint(1) |  |  | Coluna nao utilizada |
| dmes10_cta | tinyint(1) |  |  | Coluna nao utilizada |
| dmes11_cta | tinyint(1) |  |  | Coluna nao utilizada |
| dmes12_cta | tinyint(1) |  |  | Coluna nao utilizada |
| cta_cor_dep_per | integer(4) |  |  | Conta da correcao da depreciacao do periodo |
| dt_parou_corr | date(4) |  | S | Data do fim da correcao |
| his_cor_mon_cta | integer(4) |  | S | Historico da Correcao Monetaria |
| his_cor_dep_acum | integer(4) |  | S | Historico da Correcao da Depreciacao Acumulada |
| his_cor_dep_per | integer(4) |  | S | Historico da Correcao da Depreciacao do Periodo |
| his_dep_per | integer(4) |  | S | Historico da Depreciacao do Periodo |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| cta_alienacao | integer(4) |  | S | Conta do custo da alienacao |
| his_alienacao | integer(4) |  | S | Historico do custo da alienacao |
| cta_caixa | integer(4) |  | S | Conta caixa da baixa |
| cta_receita | integer(4) |  | S | Conta receita da baixa |
| his_baixa | integer(4) |  | S | Historico da baixa |
| his_dep_acu | integer(4) |  | S | Historico da depreciacao acumulada |
