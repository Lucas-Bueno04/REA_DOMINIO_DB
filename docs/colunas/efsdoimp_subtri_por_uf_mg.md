# EFSDOIMP_SUBTRI_POR_UF_MG — Saldo dos Impostos - Substituição Tributária Por MG
431 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| SIGLA_UF | char(2) | PK |  | Sigla da UF |
| ESTORNO_FEM | numeric(13) |  |  | Estorno de FEM - Fundo de Erradicação da Miséria |
| VALOR_RESSARCIMENTO_CFOP_1603 | numeric(13) |  |  | Valor do ressarcimento de ICMS de Substituição Tributária |
| SALDO_ANTES_DO_RESSARCIMENTO | numeric(13) |  |  | Saldo Antes do Ressarcimento |
| DEBITO_ICMS_SOBRE_ESTOQUE_INCLUSAO | numeric(13) |  |  | Débito ICMS sobre estoques na inclusão merc. na ST - Art. 4° da Res. 4.855/15 |
| DEBITO_ICMS_SOBRE_ESTOQUE_MAJORACAO | numeric(13) |  |  | Débito ICMS ST sobre estoques da majoração de alíq. - Art. 5°, I da Res. 4.855/15 |
| DEBITO_ICMS_SOBRE_ESTOQUE_ADICIONAL | numeric(13) |  |  | Débito ICMS ST sobre estoques do adicional de alíq. - Art. 5°, I da Res. 4.855/15 |
| COMPLEMENTO_ICMS_ST_ART_31_ANEXO_XV_RICMS | numeric(13) |  |  | Complemento de ICMS ST - Art. 31-A, Anexo XV do RICMS |
| COMPLEMENTO_FEM_ART_31_ANEXO_XV_RICMS | numeric(13) |  |  | Complemento do FEM - Art. 31-B, § 3º, Anexo XV do RICMS |
| RESTITUICAO_ICMS_ST_ART_31_ANEXO_XV_RICMS | numeric(13) |  |  | Restituição de ICMS ST - Art. 31-C, Anexo XV do RICMS |
| RESTITUICAO_FEM_ART_31_ANEXO_XV_RICMS | numeric(13) |  |  | Restituição do FEM - Art. 31-D, § 3º, Anexo XV do RICMS |
| PARCELA_CORRESPONDENTE_RESTITUICAO_FEM_ART_31_ANEXO_XV_RICMS | numeric(13) |  |  | Parcela correspondente à restituição do FEM - Art. 31-D, § 3º, Anexo XV do RICMS |
| COMPLEMENTO_FEM_ADICIONADO_ICMS_ST_ART_31_ANEXO_XV_RICMS | numeric(13) |  |  | Complemento do FEM adicionado ao ICMS ST - Art. 31-B, § 3º, Anexo XV do RICMS |
| I_RECOLHIMENTO | integer(4) | PK |  | Recolhimento |
| RESTITUICAO_ICMS_ST_ART_23 | numeric(13) |  |  | Restituição de ICMS ST - Art. 23, Anexo XV do RICMS |
