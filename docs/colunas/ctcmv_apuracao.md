# CTCMV_APURACAO — CMV - Apuração do Custo das Mercadorias Vendidas
6 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_APURACAO | integer(4) | PK |  | Código |
| CODI_EMP_FILIAL | integer(4) |  |  | Filial |
| ESTOQUE_INICIAL | date(4) |  |  | Data estoque inicial |
| ESTOQUE_FINAL | date(4) |  |  | Data estoque final |
| TIPO_SALDO_ESTOQUE | char(1) |  |  | Estoque final na Escrita Fiscal (P=Saldo do produto/ M=Saldo do movimento) |
| PERIODO | char(1) |  |  | Período (M=Mensal / T=Trimestral / A=Anual) |
| TRIMESTRE | integer(4) |  |  | Trimestre |
