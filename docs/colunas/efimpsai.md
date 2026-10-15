# efimpsai — Notas Fiscais de Saida - Impostos
636.496 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_sai | integer(4) | PK |  | Saida |
| codi_imp | integer(4) | PK |  | Imposto |
| prbc_isa | numeric(7) |  |  | Percentual da base de calculo |
| bcal_isa | numeric(13) |  |  | Base de calculo |
| aliq_isa | numeric(5) |  |  | Aliquota |
| vlor_isa | numeric(13) |  |  | Valor do imposto |
| vise_isa | numeric(13) |  |  | Valor de isentas |
| vout_isa | numeric(13) |  |  | Valor de outras |
| codi_emp | integer(4) | PK |  | Empresa |
| sequ_isa | integer(4) | PK |  | Sequencia do imposto |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| aliqinss_isa | numeric(5) |  | S | Alíquota do INSS para o Funrural |
| aliqoutras_isa | numeric(6) |  | S | Aliquota Outras Entidades para o Funrural |
| vlorinss_isa | numeric(13) |  | S | Valor do INSS para o Funrural |
| vloroutras_isa | numeric(13) |  | S | Valor Outras Entidades para o Funrural |
| apiscrfop_isa | numeric(5) |  | S | Aliquota do PIS da CRFOP |
| vpiscrfop_isa | numeric(13) |  | S | Valor do PIS da CRFOP |
| acofcrfop_isa | numeric(5) |  | S | Aliquota da COFINS da CRFOP |
| vcofcrfop_isa | numeric(13) |  | S | Valor da COFINS da CRFOP |
| acsoccrfop_isa | numeric(5) |  | S | Aliquota da CSLL da CRFOP |
| vcsoccrfop_isa | numeric(13) |  | S | Valor da CSLL da CRFOP |
| airpjcrfop_isa | numeric(5) |  | S | Aliquota do IRPJ da CRFOP |
| virpjcrfop_isa | numeric(13) |  | S | Valor do IRPJ da CRFOP |
| vcon_isa | numeric(13) |  | S | Valor contabil |
| ntri_isa | numeric(13) |  | S | Nao tributadas |
| redu_isa | numeric(13) |  | S | Parcela reduzida |
| VLORIPI_ISA | numeric(13) |  | S | Valor do IPI |
| I_RECOLHIMENTO | integer(4) |  | S | Sequencial do código de recolhimento |
| CODIGO_RECOLHIMENTO | char(6) |  | S | Codigo de recolhimento do imposto |
| ALIQUOTA_RAT_ISA | numeric(5) |  |  | Alíquota RAT |
| VALOR_RAT_ISA | numeric(13) |  |  | Valor RAT |
| VALOR_TARE_ISA | numeric(13) |  |  | Valor TARE |
| ALIQUOTA_TARE_ISA | numeric(5) |  |  | Alíquota TARE |
| VALOR_FUNDO_AMPARA_ISA | numeric(13) |  |  | Fundo Ampara/RS |
| VALOR_ADICIONAL_RETENCAO_ISA | numeric(13) |  |  | Adicional Retenção |
| ALIQUOTA_FUNRURAL | numeric(6) |  |  | Alíquota Funrural |
| VALOR_DEDUCAO_RETENCAO_ISA | numeric(13) |  |  | Dedução retenção |
| CODI_NAT_RENDIMENTO | integer(4) |  | S | Código da Natureza de Rendimento |
| ALIQUOTA_INTERESTADUAL | numeric(13) |  | S | Alíquota Interestadual |
