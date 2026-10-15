# efsdoimp — Saldo dos Impostos
791.318 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_imp | integer(4) | PK |  | Imposto |
| data_sim | date(4) | PK |  | Competencia |
| pdic_sim | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| sdev_sim | numeric(13) |  |  | Saldo a Recolher |
| scre_sim | numeric(13) |  |  | Saldo Credor |
| inc1_sim | numeric(13) |  |  | Incentivo 1 ME e EPP |
| inc2_sim | numeric(13) |  |  | Incentivo 2 ME e EPP |
| vcoe_sim | numeric(13) |  |  | Valor contabil de entradas |
| bcae_sim | numeric(13) |  |  | Base de calculo de entradas |
| vime_sim | numeric(13) |  |  | Valor do imposto de entradas |
| vise_sim | numeric(13) |  |  | Valor de isentas de entradas |
| voue_sim | numeric(13) |  |  | Valor de outras de entradas |
| vcos_sim | numeric(13) |  |  | Valor contabil de saidas |
| bcas_sim | numeric(13) |  |  | Base de calculo de saidas |
| vims_sim | numeric(13) |  |  | Valor do imposto de saidas |
| viss_sim | numeric(13) |  |  | Valor de isentas de saidas |
| vous_sim | numeric(13) |  |  | Valor de outras de saidas |
| vcov_sim | numeric(13) |  |  | Valor contabil de servicos |
| bcav_sim | numeric(13) |  |  | Base de calculo de servicos |
| vimv_sim | numeric(13) |  |  | Valor do imposto de servicos |
| visv_sim | numeric(13) |  |  | Valor de isentas de servicos |
| vouv_sim | numeric(13) |  |  | Valor de outras de servicos |
| outc_sim | numeric(13) |  |  | Outros creditos/Outros recolhimentos |
| estd_sim | numeric(13) |  |  | Estorno de debitos/Estorno de despesas |
| outd_sim | numeric(13) |  |  | Outros debitos/Outras despesas |
| estc_sim | numeric(13) |  |  | Estorno de creditos/Estorno de recolhimentos |
| oded_sim | numeric(13) |  |  | Outras deducoes |
| oacr_sim | numeric(13) |  |  | Outros acrescimos |
| vdi1_sim | numeric(13) |  |  | Valor disponivel 1 |
| vdi2_sim | numeric(13) |  |  | Valor disponivel 2 |
| vdi3_sim | numeric(13) |  |  | Valor disponivel 3 |
| vdi4_sim | numeric(13) |  |  | Valor disponivel 4 |
| vdi5_sim | numeric(13) |  |  | Valor disponivel 5 |
| acum_sim | numeric(13) |  |  | Base de calculo acumulada ate o mes anterior |
| fxin_sim | numeric(13) |  |  | Faixa incial do imposto (Simples) |
| fxfi_sim | numeric(13) |  |  | Faixa final do imposto (Simples) |
| aliq_sim | numeric(13) |  |  | Aliquota acumulada do imposto |
| bcal_sim | numeric(13) |  |  | Base de calculo do imposto |
| dvct_sim | date(4) |  |  | Data do vencimento do imposto |
| srec_sim | numeric(13) |  |  | SALDO A RECOLHER ANTES DAS DEDUCOES |
| sdif_sim | numeric(13) |  |  | Saldo a diferir ou a transportar para o periodo seguinte |
| dpag_sim | date(4) |  | S | Data de pagamento do imposto |
| vdi6_sim | numeric(13) |  | S | Valor disponivel 6 |
| outr_sim | numeric(13) |  | S | Outros recolhimentos |
| dfin_sim | date(4) |  |  | Data final do periodo |
| crei_sim | numeric(13) |  | S | Credito por importacao |
| vdi7_sim | numeric(13) |  | S | Valor disponivel 7 |
| vdi8_sim | numeric(13) |  | S | Valor disponivel 8 |
| ncal_sim | char(1) |  | S | PR: Novo Calculo, grava na vdi5_sim o sdo antes do valor minimo) MG: para ME e EPP(S-com FUNDESE, N-sem FUNDESE) e X-sem Movto |
| vdi9_sim | numeric(13) |  | S | Valor disponivel 9 |
| vdi10_sim | numeric(13) |  | S | Valor disponivel 10 |
| vdi11_sim | numeric(13) |  | S | Valor disponivel 11 |
| vdi12_sim | numeric(13) |  | S | Valor disponivel 12 |
| vdi13_sim | numeric(13) |  | S | Valor disponivel 13 |
| vctoprodec_sim | date(4) |  | S | Data de vencimento do Prodec - SC |
| vdi14_sim | numeric(13) |  | S | Valor disponivel 14 |
| vdi15_sim | numeric(13) |  | S | Valor disponivel 15 |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| srecctb_sim | numeric(13) |  | S | Saldo a Recolher Antes das Deducoes - Contabilizado |
| sdevctb_sim | numeric(13) |  | S | Saldo a Recolher - Contabilizado |
| screctb_sim | numeric(13) |  | S | Saldo Credor - Contabilizado |
| sdifctb_sim | numeric(13) |  | S | Saldo a diferir ou a transportar para o periodo seguinte - Contabilizado |
| vdi16_sim | numeric(13) |  | S | Valor disponível 16 |
| vdi17_sim | numeric(13) |  | S | Valor disponível 17 |
| vdi18_sim | numeric(13) |  | S | Valor disponível 18 |
| vdi19_sim | numeric(13) |  | S | Valor disponível 19 |
| vdi20_sim | numeric(13) |  | S | Valor disponível 20 |
| vdi21_sim | numeric(13) |  | S | Valor disponível 21 |
| vdi22_sim | numeric(13) |  | S | Valor disponível 22 |
| vdi23_sim | numeric(13) |  | S | Valor disponível 23 |
| vdi24_sim | numeric(13) |  | S | Valor disponível 24 |
| vdi25_sim | numeric(13) |  | S | Valor disponível 25 |
| vdi26_sim | numeric(13) |  | S | Valor disponível 26 |
| vdi27_sim | numeric(13) |  | S | Valor disponível 27 |
| vdi28_sim | numeric(13) |  | S | Valor disponível 28 |
| vdi29_sim | numeric(13) |  | S | Valor disponível 29 |
| vdi30_sim | numeric(13) |  | S | Valor disponível 30 |
| vdi31_sim | numeric(13) |  | S | Valor disponível 31 |
| vdi32_sim | numeric(13) |  | S | Valor disponível 32 |
| vdi33_sim | numeric(13) |  | S | Valor disponível 33 |
| vdi34_sim | numeric(13) |  | S | Valor disponível 34 |
| fundosocial_sim | char(1) |  | S | Calcula FUNDOSOCIAL |
| parcelado_sim | char(1) |  |  | Imposto parcelado(S/N) |
| vlrpago_sim | numeric(13) |  | S | Valor pago do imposto |
| vdi35_sim | numeric(13) |  | S | Valor disponivel 35 |
| vdi36_sim | numeric(13) |  | S | Valor disponivel 36 |
| vdi37_sim | numeric(13) |  | S | Valor disponivel 37 |
| vdi38_sim | numeric(13) |  | S | Valor disponivel 38 |
| vdi39_sim | numeric(13) |  | S | Valor disponivel 39 |
| vdi40_sim | numeric(13) |  | S | Valor disponivel 40 |
| vdi41_sim | numeric(13) |  | S | Valor disponivel 41 |
| vdi42_sim | numeric(13) |  | S | Valor disponivel 42 |
| vdi43_sim | numeric(13) |  | S | Valor disponivel 43 |
| vdi44_sim | numeric(13) |  | S | Valor disponivel 44 |
| vdi45_sim | numeric(13) |  | S | Valor disponivel 45 |
| vdi46_sim | numeric(13) |  | S | Valor disponivel 46 |
| vdi47_sim | numeric(13) |  | S | Valor disponivel 47 |
| vdi48_sim | numeric(13) |  | S | Valor disponivel 48 |
| vdi49_sim | numeric(13) |  | S | Valor disponivel 49 |
| vdi50_sim | numeric(13) |  | S | Valor disponivel 50 |
| classe_sim | integer(4) |  | S | Classe de vencimento |
| contabiliza_sim | char(1) |  | S | Permite gerar contabilizacao |
| reducao_saidas_sim | numeric(13) |  | S | Reducao do imposto nas saidas |
| reducao_entradas_sim | numeric(13) |  | S | Reducao do imposto nas entradas |
| vdi51_sim | numeric(13) |  | S | Valor disponivel 51 |
| vdi52_sim | numeric(13) |  | S | Valor disponivel 52 |
| vdi53_sim | numeric(13) |  | S | Valor disponivel 53 |
| vdi54_sim | numeric(13) |  | S | Valor disponivel 54 |
| vdi55_sim | numeric(13) |  | S | Valor disponivel 55 |
| rfed_sim | integer(4) |  | S | Regime federal |
| rest_sim | integer(4) |  | S | Regime estadual |
| rmun_sim | integer(4) |  | S | Regime municipal |
| faixa_sim | integer(4) |  | S | Faixa de enquadramento |
| porte_sim | tinyint(1) |  | S | Porte (1=ME/2=EPP/3=Normal) |
| percentual_estorno_sim | numeric(13) |  | S | Percentual de estorno |
| vdi56_sim | numeric(13) |  | S | Valor disponivel 56 |
| vdi57_sim | numeric(13) |  | S | Valor disponivel 57 |
| vdi58_sim | numeric(13) |  | S | Valor disponivel 58 |
| vdi59_sim | numeric(13) |  | S | Valor disponivel 59 |
| vdi60_sim | numeric(13) |  | S | Valor disponivel 60 |
| VDI61_SIM | numeric(13) |  | S | Valor disponível 61 |
| VDI62_SIM | numeric(13) |  | S | Valor disponível 62 |
| VDI63_SIM | numeric(13) |  | S | Valor disponível 63 |
| VDI64_SIM | numeric(13) |  | S | Valor disponível 64 |
| VDI65_SIM | numeric(13) |  | S | Valor disponível 65 |
| VDI66_SIM | numeric(13) |  | S | Valor disponível 66 |
| VDI67_SIM | numeric(13) |  | S | Valor disponível 67 |
| VDI68_SIM | numeric(13) |  | S | Valor disponível 68 |
| VDI69_SIM | numeric(13) |  | S | Valor disponível 69 |
| VDI70_SIM | numeric(13) |  | S | Valor disponível 70 |
| USUARIO | char(128) |  |  | Usuário que fez a apuração dos impostos |
| DATA_HORA | timestamp(8) |  |  | Hora que foi feita a apuração |
| NUMERO_TTD | char(20) |  | S | Número do acordo TTD |
| VDI71_SIM | numeric(13) |  | S | Valor disponível 71 |
| VDI72_SIM | numeric(13) |  | S | Valor disponível 72 |
| VDI73_SIM | numeric(13) |  | S | Valor disponível 73 |
| VDI74_SIM | numeric(13) |  | S | Valor disponível 74 |
| VDI75_SIM | numeric(13) |  | S | Valor disponível 75 |
| VDI76_SIM | numeric(13) |  | S | Valor disponível 76 |
| VDI77_SIM | numeric(13) |  | S | Valor disponível 77 |
| VDI78_SIM | numeric(13) |  | S | Valor disponível 78 |
| VDI79_SIM | numeric(13) |  | S | Valor disponível 79 |
| VDI80_SIM | numeric(13) |  | S | Valor disponível 80 |
| SALDO_CREDOR_ANTERIOR | numeric(13) |  |  | Saldo Credor Anterior |
| SALDO_DIFERIDO_ANTERIOR | numeric(13) |  |  | Saldo Diferido Anterior |
| VDI81_SIM | numeric(13) |  | S | Valor disponível 81 |
| VDI82_SIM | numeric(13) |  | S | Valor disponível 82 |
| VDI83_SIM | numeric(13) |  | S | Valor disponível 83 |
| VDI84_SIM | numeric(13) |  | S | Valor disponível 84 |
| VDI85_SIM | numeric(13) |  | S | Valor disponível 85 |
| VDI86_SIM | numeric(13) |  | S | Valor disponível 86 |
| VDI87_SIM | numeric(13) |  | S | Valor disponível 87 |
| VDI88_SIM | numeric(13) |  | S | Valor disponível 88 |
| VDI89_SIM | numeric(13) |  | S | Valor disponível 89 |
| VDI90_SIM | numeric(13) |  | S | Valor disponível 90 |
| VDI91_SIM | numeric(13) |  | S | Valor disponível 91 |
| VDI92_SIM | numeric(13) |  | S | Valor disponível 92 |
| VDI93_SIM | numeric(13) |  | S | Valor disponível 93 |
| VDI94_SIM | numeric(13) |  | S | Valor disponível 94 |
| VDI95_SIM | numeric(13) |  | S | Valor disponível 95 |
| VDI96_SIM | numeric(13) |  | S | Valor disponível 96 |
| VDI97_SIM | numeric(13) |  | S | Valor disponível 97 |
| VDI98_SIM | numeric(13) |  | S | Valor disponível 98 |
| VDI99_SIM | numeric(13) |  | S | Valor disponível 99 |
| VDI100_SIM | numeric(13) |  | S | Valor disponível 100 |
| VDI101_SIM | numeric(13) |  | S | Valor disponível 101 |
| VDI102_SIM | numeric(13) |  | S | Valor disponível 102 |
| VDI103_SIM | numeric(13) |  | S | Valor disponível 103 |
| VDI104_SIM | numeric(13) |  | S | Valor disponível 104 |
| VDI105_SIM | numeric(13) |  | S | Valor disponível 105 |
| PERCENTUAL_RECEITA_BRUTA_NAO_RELACIONADA | numeric(16) |  | S | % Receita bruta não relacionada |
| VERSAO | varchar(10) |  |  | Versão |
| ARQUIVO | integer(4) |  |  | Arquivo de atualização |
| DEBITO_DIFAL_NC | numeric(13) |  |  | Débito DIFAL NC |
| CREDITO_DIFAL_NC | numeric(13) |  |  | Crédito DIFAL NC |
| MG_DEBITO_TRANSFERENCIA_SALDO_CREDOR | numeric(13) |  |  | Débito Transferência de saldo credor |
| MG_DEDUCAO_TRANSFERENCIA_SALDO_CREDOR | numeric(13) |  |  | Dedução Transferência de saldo credor |
| CALCULOU_DRCST | char(1) |  |  | Calculou DRCST |
| SALDO_DIFERIDO_PRORROGACAO_ANTERIOR | numeric(13) |  |  | Saldo Diferido Anterior prorrogação |
| SALDO_DIFERIDO_PRORROGACAO_TRANSPORTAR | numeric(13) |  |  | Saldo Diferido Anterior prorrogação a transportar |
