# CTSPED_ECF_OD_M410_ORIGEM_IMPORTACAO — Tabela de origem da importação registros M410
4.250 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código Empresa |
| ORIGEM_IMPORTACAO | varchar(50) |  |  | Importar prejuízos e outros(M = Origem Manual /A = Origem Automatica |
| MES_COMPETENCIA | integer(4) | PK |  | Mes competencia da origem. |
| ANO_COMPETENCIA | integer(4) | PK |  | Ano competência da origem. |
| TIPO_IMPORTACAO | char(1) | PK |  | A = Lacs / U = Lalur |
| PERIODICIDADE | char(1) | PK |  | A = Anual / M = Mensal / T = Trimestral |
