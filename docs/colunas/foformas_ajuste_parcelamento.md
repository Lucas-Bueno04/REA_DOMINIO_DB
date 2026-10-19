# FOFORMAS_AJUSTE_PARCELAMENTO — Formas de ajustes conforme parcelamento
331 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_FORMA_AJUSTE_PARCELAMENTO | integer(4) | PK |  | Código |
| FORMA_PARCELAMENTO | smallint(2) |  |  | Forma de parcelamento: (1=Conforme quantidade de parcelas, 2=Conforme competência informada) |
| PAGAR_SALDO_DIFERENCA_RESCISAO | smallint(2) |  |  | Efetuar o pagamento do saldo das diferenças salariais no cálculo de rescisão: (0=Não, 1=Sim) |
| TOTAL_PARCELAS | integer(4) |  | S | Total de parcelas: (1-999) |
| INICIO_PARCELAMENTO | smallint(2) |  | S | Início do parcelamento: (1=No mês seguinte a alteração salarial, 2=No mês da alteração salarial/3=Conforme definido pelo usuário) |
| TIPO_FOLHA | smallint(2) |  | S | Tipo da folha para pagamento: (11=Mensal, 42=Complementar) |
| GERAR_FOLHA_COMPLEMENTAR_ESPECIFICA | smallint(2) |  | S | Gerar folhas complementares específicas para esta alteração salarial: (0=Não, 1=Sim) |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro: (0=Sistema, 1=Importação de tabelas, 2=Importação de leiaute, 3=Conversão) |
| FORMA_CALCULO_ENCARGOS_PATRONAIS_CCT_DCTF_WEB | smallint(2) |  |  | Forma do cálculo dos encargos patronais CCT conforme DCTFWeb: (1=Cálculo na competência da alteração salarial, 2=Cálculo na competência do pagamento da parcela) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
