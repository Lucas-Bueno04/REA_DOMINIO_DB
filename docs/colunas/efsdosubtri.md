# efsdosubtri — Saldo da Substituicao Tributaria por Estado
28.512 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_imp | integer(4) | PK |  | Imposto |
| data_sim | date(4) | PK |  | Competencia |
| pdic_sim | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S) |
| sigl_est | char(2) | PK |  | Estado |
| sdev_sst | numeric(13) |  | S | Saldo devedor |
| scre_sst | numeric(13) |  | S | Saldo Credor |
| vcoe_sst | numeric(13) |  | S | Valor Contabil das Entradas |
| bcae_sst | numeric(13) |  | S | Base Calculo das Entradas |
| vime_sst | numeric(13) |  | S | Valor Imposto das Entradas |
| vcos_sst | numeric(13) |  | S | Valor Contabil das Saidas |
| bcas_sst | numeric(13) |  | S | Base Calculo das Saidas |
| vims_sst | numeric(13) |  | S | Valor Imposto das Saidas |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| RESSARCIMENTO_SST | numeric(13) |  | S | Valor do ressarcimento |
| RESSARCIMENTO_ICMS_SST | numeric(13) |  | S | Valor do ressarcimento ICMS ST |
| SALDO_INFERIOR_QUANT_MINIMA_RECOLHIMENTO_SST | numeric(13) |  |  | Saldo inferior a quantidade mínima para recolhimento |
| SALDO_ANT_INFERIOR_QUANT_MINIMA_RECOLHIMENTO_SST | numeric(13) |  |  | Saldo anterior inferior a quantidade mínima para recolhimento |
| SALDO_CREDOR_ANT_UTIL_PARA_COMP_DEB_ICMS_PROPRIO | numeric(13) |  |  | Saldo credor anterior de ICMS ST utilizado para compensar débitos de ICMS próprio |
