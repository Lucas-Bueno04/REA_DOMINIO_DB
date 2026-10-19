# EFTABELA_ALIQUOTA_ICMS — Tabela de Alíquota Interestadual de ICMS
1.970 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da Empresa |
| I_TABELA_ICMS | integer(4) | PK |  | Sequencial |
| DESCRICAO | varchar(130) |  |  | Descrição |
| GUID_CONTABIL | uniqueidentifier(16) |  | S | Identificador Único do registro no banco do Contábil |
| GUID_ONVIO | uniqueidentifier(16) |  | S | Identificador Único do registro no banco do Atendimento Onvio |
