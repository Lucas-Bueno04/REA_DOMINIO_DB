# EFLANCAMENTOS_LUCROS_DIVIDENDOS_TRIBUTAVEIS_DISTRIBUICAO — Distribuição de lucros e dividendos tributáveis
35 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| DATA_LANCAMENTO | date(4) |  |  | Data do Lancamento |
| I_LANC_LUCROS_DIVIDENDOS_TRIBUTAVEIS | integer(4) | PK |  | Codigo Lançamentos de Distribuição de Lucros e Dividendos Tributáveis |
| I_SEQUENCIAL_DISTRIBUICAO | integer(4) | PK |  | Sequencial |
| CODIGO_PAIS | integer(4) |  |  | País |
| CODI_NAT_RENDIMENTO | integer(4) |  |  | Código natureza de rendimento |
| VALOR_TRIBUTADO | numeric(13) |  |  | Valor |
| ALIQUOTA | numeric(5) |  |  | Alíquota |
| IRRF | numeric(13) |  |  | IRRF |
| I_RECOLHIMENTO | integer(4) |  |  | Sequencial do código de recolhimento |
| CODIGO_RECOLHIMENTO | char(6) |  |  | Codigo Recolhimento |
| ORIGEM_CONTABILIDADE | char(1) |  |  | Importado pela contabilidade (S/N) |
| IMPORTADO_FOLHA | char(1) |  |  | Controle de informações importadas da folha |
| INSCRICAO_BENEFICIARIO | char(14) |  | S | CPF/CNPJ do beneficiário |
| DESCRICAO | char(40) |  | S | Descrição do beneficiário |
| TIPO_INSCRICAO_BENEFICIARIO | integer(4) |  | S | Tipo de inscrição do beneficiário (1-CNPJ/2-CPF) |
