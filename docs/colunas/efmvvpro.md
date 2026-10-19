# EFMVVPRO — Notas Fiscais de Serviços - Produtos
53.933 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_PDI | char(14) |  |  | Produto |
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_SER | integer(4) | PK |  | Código |
| NUME_MVP | integer(4) | PK |  | Sequencial |
| DATA_MVP | date(4) |  | S | Data |
| QTDE_MVP | numeric(13) |  |  | Quantidade |
| VPRO_MVP | numeric(13) |  | S | Valor do Produto |
| VDES_MVP | numeric(13) |  | S | Valor do Desconto |
| VALOR_UNIT_MVP | numeric(15) |  | S | Valor unitário |
| CST_ISSQN_MVP | integer(4) |  | S | CST do ISSQN |
| BC_ISSQN_MVP | numeric(13) |  | S | Base de cálculo ISSQN |
| ALIQ_ISSQN_MVP | numeric(5) |  | S | Alíquota de ISSQN |
| VALOR_ISSQN_MVP | numeric(13) |  | S | Valor ISSQN |
| ISENTAS_ISSQN_MVP | numeric(13) |  | S | Isentas de ISS |
| NAO_INCIDENCIA_ISSQN_MVP | numeric(13) |  | S | Não incidência de ISS |
| ISS_RETIDO_MVP | numeric(13) |  | S | ISS retido |
| QTDE_CANCELADA_MVP | numeric(15) |  | S | Quantidade cancelada |
| VALOR_CANCEL_MVP | numeric(13) |  | S | Valor do cancelamento |
| ORIGEM_REG | integer(4) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| CST_PIS_MVP | integer(4) |  | S | CST do PIS |
| BC_PIS_MVP | numeric(13) |  | S | Base de cálculo do PIS |
| ALIQ_PIS_MVP | numeric(7) |  | S | Alíquota do PIS |
| VALOR_PIS_MVP | numeric(13) |  | S | Valor do PIS |
| CST_COFINS_MVP | integer(4) |  | S | CST do COFINS |
| BC_COFINS_MVP | numeric(13) |  | S | Base de cálculo do COFINS |
| ALIQ_COFINS_MVP | numeric(7) |  | S | Alíquota do COFINS |
| VALOR_COFINS_MVP | numeric(13) |  | S | Valor do COFINS |
| VALOR_CONTABIL_MVP | numeric(13) |  | S | Valor contabil produto |
| DADOS_PISCOFINS_OK | char(1) |  |  | Dados referente ao PIS/COFINS OK (S/N) |
| DESCRICAO_COMPLEMENTAR_MVP | varchar(255) |  | S | Descrição complementar |
| NATUREZA_RECEITA_PIS_MVP | integer(4) |  | S | Natureza da receita do PIS |
| NATUREZA_RECEITA_COFINS_MVP | integer(4) |  | S | Natureza da receita do COFINS |
| EXCLUSAO_COOPERATIVA_MVP | numeric(13) |  | S | Exclusão cooperativa |
| PERCENTUAL_REDUCAO_BC_PIS_MVP | numeric(5) |  |  | Percentual Redução Base Cálculo PIS |
| PERCENTUAL_REDUCAO_BC_COFINS_MVP | numeric(5) |  |  | Percentual Redução Base Cálculo COFINS |
| I_RECOLHIMENTO_PIS | integer(4) |  | S | Código Sequencial do Recolhimento do PIS |
| CODIGO_RECOLHIMENTO_PIS | char(6) |  | S | Código do Recolhimento do PIS |
| I_RECOLHIMENTO_COFINS | integer(4) |  | S | Código Sequencial do Recolhimento do COFINS |
| CODIGO_RECOLHIMENTO_COFINS | char(6) |  | S | Código do Recolhimento do COFINS |
| VALOR_ISSRET_MVP | numeric(13) |  | S | Valor ISS Retido |
