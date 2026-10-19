# FOFORMAS_AJUSTE_PARCELAMENTO_COMPETENCIAS — Formas de ajustes conforme parcelamento - Competências
653 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_FORMA_AJUSTE_PARCELAMENTO | integer(4) | PK |  | Código da forma de ajuste conforme parcelamento |
| I_PARCELA | integer(4) | PK |  | Número da parcela. |
| COMPETENCIA | date(4) |  | S | Competência origem da diferença |
| COMPETENCIA_PAGAMENTO | date(4) |  |  | Competência para pagamento |
| TIPO_FOLHA | smallint(2) |  |  | Tipo da folha: (11=Mensal, 42=Complementar) |
| GERAR_FOLHA_COMPLEMENTAR_ESPECIFICA | smallint(2) |  |  | Gerar folhas complementares específicas para esta alteração salarial: (0=Não, 1=Sim) |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro: (0=Sistema, 1=Importação de tabelas, 2=Importação de leiaute, 3=Conversão) |
| PERCENTUAL | numeric(5) |  | S | Percentual de diferença pago na parcela da competência. |
| DIFERENCA_13_SALARIO | smallint(2) |  |  | Diferença 13º salário. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
