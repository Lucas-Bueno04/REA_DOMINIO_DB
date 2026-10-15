# efimpser — Notas Fiscais de Servico - Impostos
1.155.629 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_ser | integer(4) | PK |  | Servico |
| codi_imp | integer(4) | PK |  | Imposto |
| prbc_ise | numeric(7) |  |  | Percentual da base de calculo |
| bcal_ise | numeric(13) |  |  | Base de calculo |
| aliq_ise | numeric(5) |  |  | Aliquota |
| vlor_ise | numeric(13) |  |  | Valor do imposto |
| vise_ise | numeric(13) |  |  | Valor de isentas |
| vout_ise | numeric(13) |  |  | Valor de outras |
| codi_emp | integer(4) | PK |  | Empresa |
| sequ_ise | integer(4) | PK |  | Sequencia do imposto |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| apiscrfop_ise | numeric(5) |  | S | Aliquota do PIS da CRFOP |
| vpiscrfop_ise | numeric(13) |  | S | Valor do PIS da CRFOP |
| acofcrfop_ise | numeric(5) |  | S | Aliquota da COFINS da CRFOP |
| vcofcrfop_ise | numeric(13) |  | S | Valor da COFINS da CRFOP |
| acsoccrfop_ise | numeric(5) |  | S | Aliquota da CSLL da CRFOP |
| vcsoccrfop_ise | numeric(13) |  | S | Valor da CSLL da CRFOP |
| airpjcrfop_ise | numeric(5) |  | S | Aliquota do IRPJ da CRFOP |
| virpjcrfop_ise | numeric(13) |  | S | Valor do IRPJ da CRFOP |
| vcon_ise | numeric(13) |  | S | Valor contabil |
| CODIGO_RECOLHIMENTO | char(6) |  | S | Código de recolhimento do imposto |
| I_RECOLHIMENTO | integer(4) |  | S | Sequencial do código de recolhimento |
| VALOR_ADICIONAL_RETENCAO_ISE | numeric(13) |  |  | Adicional Retenção |
| VALOR_DEDUCAO_RETENCAO_ISE | numeric(13) |  |  | Dedução retenção |
| CODI_NAT_RENDIMENTO | integer(4) |  | S | Código da Natureza de Rendimento |
