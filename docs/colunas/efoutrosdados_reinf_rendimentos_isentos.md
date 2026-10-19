# EFOUTROSDADOS_REINF_RENDIMENTOS_ISENTOS — REINF - Outros Dados - Rendimentos Isentos
1.181 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| COMPETENCIA | date(4) | PK |  | Competência |
| I_INFORMATIVOS | integer(4) | PK |  | Informativo |
| I_RENDIMENTO_ISENTO | integer(4) | PK |  | Sequencial rendimento |
| BENEFICIARIO | char(14) |  |  | CPF/CNPJ DO BENEFICIÁRIO |
| CODIGO_PAIS | integer(4) |  |  | País |
| CODI_NAT_RENDIMENTO | integer(4) |  |  | Código natureza de rendimento |
| VALOR | numeric(13) |  |  | Valor |
| IMPORTADO_FOLHA | char(1) |  |  | Controle de informações importadas da folha |
| DATA_RENDIMENTO | date(4) |  | S | Data do rendimento isento |
| ORIGEM_CONTABILIDADE | char(1) |  |  | Beneficiário importado pela contabilidade (S/N) |
| LUCRO_APURADO_ATE_2025 | char(1) |  |  | Lucro apurado ate 2025 (S/N) |
