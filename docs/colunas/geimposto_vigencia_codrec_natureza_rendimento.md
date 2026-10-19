# GEIMPOSTO_VIGENCIA_CODREC_NATUREZA_RENDIMENTO — Tabela com as naturezas de rendimento dos impostos
48 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| VIGENCIA_IMP | date(4) | PK |  | Vigencia |
| CODI_REC | char(6) | PK |  | Codigo do recolhimento |
| I_SEQUENCIAL_NATUREZA | integer(4) | PK |  | Sequencial do recolhimento x natureza de rendimento |
| CODI_NAT_RENDIMENTO | integer(4) |  |  | Código da Natureza de Rendimento |
| TIPO_ISENCAO | integer(4) |  | S | Tipo de isenção para rendimentos isentos |
| DESCRICAO_ISENCAO | varchar(100) |  | S | Descrição de isenção para rendimentos isentos |
