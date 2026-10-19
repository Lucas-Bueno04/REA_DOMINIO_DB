# CTPARMTO_DERE_VIGENCIA — Parametros Contabilidade - Vigencia da guia Informativos/DeRE
1.427 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| VIGENCIA | date(4) | PK |  | Vigencia |
| DESCRICAO | varchar(80) |  |  | Descricao |
| PLANO_REFERENCIAL | integer(4) |  |  | Plano referencial (1-Banco Central (COSIF) / 2-ANS - Agencia Nacional de Saude Suplementar / 3-SUSEP - Superintendencia de Seguros Privados / 4-SPED) |
| ENCERRAMENTO_CONTABIL | char(1) |  |  | Encerramento contabil (A-Anual / S-Semestral / Q-Quadrimestral / T-Trimestral / B-Bimestral / M-Mensal) |
| VIGENCIA_BUSCA | integer(4) |  | S | Vigencia no formato AAAAMM para navegacao entre vigencias sem varredura |
