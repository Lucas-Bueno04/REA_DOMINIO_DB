# GEIMPOSTO_VIGENCIA_PARCELAMENTO_CTB — Impostos - Cadastro - Contas para Parcelamento
35.396 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| VIGENCIA_IMP | date(4) | PK |  | Vigência |
| GERAR_LANCAMENTO_PARTIDA_SIMPLES | char(1) |  | S | Gerar lançamentos de partida simples (S/N) |
| CTPROVISAO | integer(4) |  | S | Conta da provisão |
| HTPROVISAO | integer(4) |  | S | Histórico padrão da provisão |
| CTJUROSPROVISAO | integer(4) |  | S | Conta provisão dos juros |
| CTJUROSDESPESA | integer(4) |  | S | Conta despesa dos juros |
| HTJUROS | integer(4) |  | S | Histórico padrão dos juros |
| CTMULTAPROVISAO | integer(4) |  | S | Conta provisão da multa |
| CTMULTADESPESA | integer(4) |  | S | Conta despesa da multa |
| HTMULTA | integer(4) |  | S | Histórico padrão da multa |
| CT_ENCARGOS_PROVISAO | integer(4) |  | S | Conta provisão de encargos |
| CT_ENCARGOS_DESPESA | integer(4) |  | S | Conta despesa de encargos |
| HT_ENCARGOS | integer(4) |  | S | Histórico padrão de encargos |
