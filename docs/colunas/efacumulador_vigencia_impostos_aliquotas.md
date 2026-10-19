# EFACUMULADOR_VIGENCIA_IMPOSTOS_ALIQUOTAS — Acumuladores - Cadastro - Aliquotas
379.002 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_ACU | integer(4) | PK |  | Acumulador |
| VIGENCIA_ACU | date(4) | PK |  | Vigencia |
| CODI_IMP | integer(4) | PK |  | Imposto |
| SEQU_IMP | integer(4) | PK |  | Sequencial |
| ALIQUOTA_IMP | numeric(5) |  |  | Aliquotas pre-definidas |
| PERCENTUALBC_IMP | numeric(7) |  |  | Percentual da base de calculo |
| TIPO_ALIQUOTA_ICMS | char(1) |  | S | Tipo Alíquota do ICMS (A- Informar Alíquota / T= Informar Tabela) |
| I_TABELA_ICMS | integer(4) |  | S | Sequencial tabela de ICMS |
| ADICIONAL_ALIQUOTA_IMP | numeric(5) |  | S |  |
| PERCENTUAL_CARGA_TRIBUTARIA | numeric(5) |  |  | Carga tributária % |
| VALOR_COEFICIENTE | numeric(5) |  |  | Coeficiente |
