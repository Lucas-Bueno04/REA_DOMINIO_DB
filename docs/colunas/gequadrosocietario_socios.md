# gequadrosocietario_socios — Empresa - Cadastro - Quadro Societario - Socios
4.980 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo da empresa |
| data | date(4) | PK |  | Data |
| i_socio | integer(4) | PK |  | Codigo sequencial |
| tipo | char(1) | PK |  | Tipo (S - Socio/A - Administrador/R - Representante Legal) |
| qdade_quotas | numeric(13) |  |  | Quantidade de quotas |
| integralizar | numeric(13) |  |  | Capital a integralizar |
| participacao | numeric(5) |  |  | Participacao % |
| condicao | integer(4) |  |  | Condicao |
| cargo | char(30) |  |  | Cargo |
| data_ingresso | date(4) |  |  | Data de  ingresso |
| data_saida | date(4) |  | S | Data de saida |
| exerce_atividade | tinyint(1) |  |  | Exerce atividade 1=Sim/0=Nao |
| POSSUI_RESPONSAVEL_LEGAL | char(1) |  |  | Possui responsável legal (S/N) |
| CPF_RESPONSAVEL_LEGAL | char(11) |  |  | CPF do responsável legal |
| NOME_RESPONSAVEL_LEGAL | varchar(40) |  |  | Nome do responsável legal |
| QUALIFICACAO_RESPONSAVEL_LEGAL | integer(4) |  |  | Qualificação do responsável legal (1-Procurador/2-Curador/3-Mãe/4-Pai/5-Tutor/6-Outro) |
| VALOR_QUOTA | numeric(13) |  |  | Valor da quota |
| QUOTA_INTEGRALIZADA | numeric(13) |  |  | Quotas integralizadas |
| QUOTA_A_INTEGRALIZAR | numeric(13) |  |  | Quotas a integralizar |
| CAPITAL_INTEGRALIZADO | numeric(17) |  |  | Capital integralizado |
| MESES_PARA_INTEGRALIZACAO | integer(4) |  |  | Meses para integralização |
| ORDEM | integer(4) |  |  | Ordem da listagem |
| BENEFICIARIO_FINAL | char(1) |  |  | Beneficiario final da empresa |
