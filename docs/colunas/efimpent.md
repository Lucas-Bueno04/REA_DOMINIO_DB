# efimpent — Notas Fiscais de Entrada - Impostos
806.969 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_ent | integer(4) | PK |  | Entrada |
| codi_imp | integer(4) | PK |  | Imposto |
| prbc_ien | numeric(7) |  |  | Percentual da base de calculo |
| bcal_ien | numeric(13) |  |  | Base de calculo |
| aliq_ien | numeric(5) |  |  | Aliquota |
| vlor_ien | numeric(13) |  |  | Valor do imposto |
| vise_ien | numeric(13) |  |  | Valor de isentas |
| vout_ien | numeric(13) |  |  | Valor de outras |
| codi_emp | integer(4) | PK |  | Empresa |
| sequ_ien | integer(4) | PK |  | Sequencia do imposto |
| aliqinss_ien | numeric(5) |  | S | Aliquota do INSS para o Funrural |
| aliqoutras_ien | numeric(6) |  | S | Aliquota Outras Entidades para o Funrural |
| vlorinss_ien | numeric(13) |  | S | Valor do INSS para o Funrural |
| vloroutras_ien | numeric(13) |  | S | Valor Outras Entidades para o Funrural |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| vloripi_ien | numeric(13) |  | S | Valor do IPI |
| vlorsubtri_ien | numeric(13) |  | S | Valor da Sub. Tributaria |
| vcon_ien | numeric(13) |  | S | Valor contabil |
| codrec_ien | char(6) |  | S | Codigo de recolhimento do imposto |
| ntri_ien | numeric(13) |  | S | Nao tributadas |
| redu_ien | numeric(13) |  | S | Parcela reduzida |
| I_RECOLHIMENTO | integer(4) |  | S | Sequencial do código de recolhimento |
| ALIQUOTA_INTERESTADUAL | numeric(13) |  | S | Alíquota Interestadual |
| ALIQUOTA_RAT_IEN | numeric(5) |  |  | Alíquota RAT |
| VALOR_RAT_IEN | numeric(13) |  |  | Valor RAT |
| VALOR_TARE_IEN | numeric(13) |  |  | Valor TARE |
| ALIQUOTA_TARE_IEN | numeric(5) |  |  | Alíquota TARE |
| APISCRFOP_IEN | numeric(5) |  |  | Alíquota PIS CRFOP |
| VPISCRFOP_IEN | numeric(13) |  |  | Valor PIS CRFOP |
| ACOFCRFOP_IEN | numeric(5) |  |  | Alíquota COFINS CRFOP |
| VCOFCRFOP_IEN | numeric(13) |  |  | Valor COFINS CRFOP |
| ACSOCCRFOP_IEN | numeric(5) |  |  | Alíquota CSOC CRFOP |
| VCSOCCRFOP_IEN | numeric(13) |  |  | Valor CSOC CRFOP |
| AIRPJCRFOP_IEN | numeric(5) |  |  | Alíquota IRPJ CRFOP |
| VIRPJCRFOP_IEN | numeric(13) |  |  | Valor IRPJ CRFOP |
| VALOR_FEM_ST_MG_IEN | numeric(13) |  |  | Valor FEM-ST/MG |
| VALOR_ADICIONAL_RETENCAO_IEN | numeric(13) |  |  | Adicional Retenção |
| VALOR_FUNDO_AMPARA_IEN | numeric(13) |  |  | Valor Fundo Ampara |
| ALIQUOTA_FUNRURAL | numeric(6) |  |  | Alíquota Funrural |
| VALOR_DEDUCAO_RETENCAO_IEN | numeric(13) |  |  | Dedução retenção |
| CODI_NAT_RENDIMENTO | integer(4) |  | S | Código da Natureza de Rendimento |
| ALIQUOTA_IRRFP | numeric(6) |  | S | Alíquota IRRFP |
| TIPO_ISENCAO | integer(4) |  | S | Tipo de isenção para rendimentos isentos |
| DESCRICAO_ISENCAO | varchar(100) |  | S | Descrição de isenção para rendimentos isentos |
