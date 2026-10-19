# EFSDOIMP_ESTADUAL_AC — Saldo dos Impostos - Estadual AC
78 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| DATA_SIM | date(4) | PK |  | Competencia |
| CREDITO_ATIVO_IMOBILIZADO | numeric(13) |  |  | Crédito Ativo Imobilizado |
| CREDITO_ICMS_PROPRIO_DECRETO_6875_2017 | numeric(13) |  |  | Crédito de ICMS Próprio conforme Art. 36-D, § 2º do Decreto 6.875/2017 |
| RESSARCIMENTO_ICMS_ST_DECRETO_6875_2017 | numeric(13) |  |  | Ressarcimento de ICMS ST conforme Art. 36-D, § 2º do Decreto 6.875/2017 |
| ESTORNO_CREDITO_ICMS_ART_48_IV | numeric(13) |  |  | Estorno de crédito de ICMS nos termos do artigo 48, IV do RICMS |
| CREDITO_PRESUMIDO_ALCB_ALCCS | numeric(13) |  |  | Crédito presumido  ALCB e ALCCS - Art. 45 do RICMS |
| CREDITO_PRESUMIDO_ALCB_ALCCS_DEVOLUCAO | numeric(13) |  |  | Devolução crédito presumido ALCB e ALCCS - Art. 45 do RICMS |
| CREDITO_CONFORME_ALIQUOTA_SN | numeric(13) |  |  | Credito de ICMS conf. alíquota do Simples Nacional - Art. 23, LC 123/06 |
| DEVOLUCAO_MERCADORIA_ADQUIRIDA_SN | numeric(13) |  |  | Devolucao de mercadoria adquirida de Simples Nacional |
