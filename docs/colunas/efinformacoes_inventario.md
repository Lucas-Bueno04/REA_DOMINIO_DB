# EFINFORMACOES_INVENTARIO — Tabela de Informações do Inventário
153 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| COMPETENCIA | date(4) | PK |  | Competência |
| GERAR_INVENTARIO | char(1) |  |  | Gerar inventário (S/N) |
| DATA_LEVANTAMENTO | date(4) |  |  | Data do levantamento |
| MOTIVO | integer(4) |  |  | Motivo (1/3/5) |
| TIPO_SALDO | char(1) |  |  | Tipo de saldo (M - Saldo do movimento/P - Saldo do produto) |
| GERAR_INVENTARIO_INCLUIDAS_SUBTRI | char(1) |  |  | Gerar inventário SUBTRI (S/N) |
| DATA_LEVANTAMENTO_INCLUIDAS_SUBTRI | date(4) |  |  | Data do levantamento SUBTRI |
| GERAR_INVENTARIO_EXCLUIDAS_SIMPLES_NACIONAL | char(1) |  |  | Gerar inventário SN (S/N) |
| DATA_LEVANTAMENTO_EXCLUIDAS_SIMPLES_NACIONAL | date(4) |  |  | Data do levantamento SN |
| GERAR_INVENTARIO_INCLUIDOS_CREDITO_PRESUMIDO | char(1) |  |  | Gerar o inventário dos produtos incluídos no Crédito Presumido |
| DATA_LEVANTAMENTO_INCLUIDOS_CREDITO_PRESUMIDO | date(4) |  |  | Mês do levantamento dos estoques Crédito Presumido |
| LISTA_TIPO_ITEM | char(50) |  |  | Tipo Item |
| GERAR_INVENTARIO_MERCADORIAS_TRIBUTADAS_REGIME_ESTIMATIVA_SIMPLIFICADO | char(1) |  |  | Gerar o inventário das mercadorias tributadas pelo regime de Estimativa Simplificado |
| DATA_LEVANTAMENTO_MERCADORIAS_TRIBUTADAS_REGIME_ESTIMATIVA_SIMPLIFICADO | date(4) |  |  | Data das mercadorias tributadas pelo regime de Estimativa Simplificado |
| GERAR_INVENTARIO_PRODUTOS_TRIBUTADOS_ANTES_REGIME_ESPECIAL | char(1) |  |  | Gerar o inventário dos produtos tributados antes do Regime Especial - Dec. 22.199/11 |
| DATA_LEVANTAMENTO_PRODUTOS_TRIBUTADOS_ANTES_REGIME_ESPECIAL | date(4) |  |  | Data dos produtos tributados antes do Regime Especial - Dec. 22.199/11 |
| MG_GERAR_REGISTRO_INVENTARIO_MENSAL_ANUAL | char(1) |  |  | Gerar registro de inventário mensal e anual empresa Atacadista - Decreto n 48.244/2021 |
| GERAR_INVENTARIO_PRODUTOS_INCLUIDOS_REGIME_TRIB_MONOFASICA_ICMS | char(1) |  |  | Gerar o inventário dos produtos incluídos no regime de trib. Monofásica do ICMS |
| DATA_LEVANTAMENTO_PRODUTOS_INCLUIDOS_REGIME_TRIB_MONOFASICA_ICMS | date(4) |  |  | Data dos produtos incluídos no regime de trib. Monofásica do ICMS |
| GERAR_SOMA_ICMS_RECUPERAVEL | char(1) |  |  | Somar o ICMS Recuperável ao valor final do produto no campo 6 do H010 |
| GERAR_INVENTARIO_PRODUTOS_SISTEMATICA_ESPECIAL_DECRETO_38455_12 | char(1) |  |  | Gerar o inventário dos produtos incluídos na sistematica do decreto 38.455/2012 |
| DATA_LEVANTAMENTO_PRODUTOS_SISTEMATICA_ESPECIAL_DECRETO_38455_12 | date(4) |  |  | Data do inventário dos produtos incluídos na sistematica do decreto 38.455/2012 |
| SC_GERAR_REGISTRO_INVENTARIO_MENSAL_ANUAL | char(1) |  |  | Gerar registro de inventário mensal e anual - Art. 24, §9, do Anexo 11, do RICMS/SC |
