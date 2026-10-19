# GEIMPOSTO_VIGENCIA_SUB_APURACAO — Impostos - Cadastro - AM - Crédito Estímulo
3 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| VIGENCIA_IMP | date(4) | PK |  | Vigência |
| I_SUB_APURACAO | integer(4) | PK |  | Sequencial |
| DESCRICAO | varchar(30) |  |  | Descrição |
| CODIGO_RECOLHIMENTO | char(6) |  |  | Código recolhimento |
| DIA_VENCIMENTO | integer(4) |  | S | Data do vencimento |
| CT_RECOLHER | integer(4) |  | S | Conta a recolher |
| HT_RECOLHER | integer(4) |  | S | Histórico a recolher |
| CT_RECUPERAR | integer(4) |  | S | Conta a recuperar |
| HT_RECUPERAR | integer(4) |  | S | Histórico a recuperar |
| CT_INCENTIVO_FISCAL | integer(4) |  | S | Conta do incentivo fiscal |
| HT_INCENTIVO_FISCAL | integer(4) |  | S | Histórico do incentivo fiscal |
