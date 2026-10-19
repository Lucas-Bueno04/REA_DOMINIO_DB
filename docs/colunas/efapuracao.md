# efapuracao — Parametros de Apuracao
63.964 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| data_apu | date(4) | PK |  | Data da apuracao. |
| fundosocial_apu | char(1) |  |  | Calcula Fundosocial |
| seitec_apu | char(1) |  | S | Calcula SEITEC |
| FUNDOSOCIAL_SUBTRI_APU | char(1) |  |  | Efetua doação para o Fundosocial - Substituição tributária (S/N) |
| ADICIONAL_FUNDOSOCIAL_APU | char(1) |  |  | Calcular crédito adicional FundoSocial - ICMS Normal |
| CALCULA_ESTOQUE_DIARIO | char(1) |  |  | Calcula estoque diário |
| REALIZA_APURACAO_PREVIDENCIARIA | char(1) |  |  | Realizar apuração previdenciária |
| CALCULA_ADICIONAL_ICMS_ESTIMATIVA | char(1) |  |  | Calcular adicional de ICMS Estimativa - Art. 157-A, II, RICMS/MT |
| PERIODO_APURADO | char(1) |  |  | Período apurado |
| PRODEC_APU | char(1) |  |  | Calcula PRODEC |
