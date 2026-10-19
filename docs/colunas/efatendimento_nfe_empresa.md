# EFATENDIMENTO_NFE_EMPRESA — Dados da empresa referente a NFe - Domínio Atendimento
1.515 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| DATA_ATIVACAO | date(4) |  | S | Data de ativação da empresa no BOX-e |
| ATIVADO | smallint(2) |  |  | Ativado (0=Não/1=Sim) |
| ORIGEM_ATENDIMENTO | integer(4) |  |  | Flag que indica se o registro vem do DA(1) ou não (0) |
| GUID_ONVIO_EMPRESA | uniqueidentifier(16) |  | S | Identificador único da empresa banco do Atendimento Onvio |
| UTILIZA_BOXE | bit(1) |  |  | Informa se esta ativo Box-e no Onvio para a empresa. |
| UTILIZA_MANIFESTO | bit(1) |  |  | Informa se esta ativo o manifesto no Onvio para a empresa. |
