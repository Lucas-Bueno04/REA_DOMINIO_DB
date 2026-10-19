# GESCP — Sociedade em Conta de Participação - SCP
17 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_SCP | integer(4) | PK |  | Sequencial do SCP |
| DESCRICAO | char(128) |  |  | Descrição |
| CONTA_DESTINO | integer(4) |  |  | Zeramento - Conta destino |
| TRANSFERE_RESULTADO_PL | char(1) |  |  | Zeramento - Transfere automaticamente os lançamentos de zeramento (S/N) |
| CONTA_LUCRO | integer(4) |  |  | Zeramento - Conta Lucro do período |
| CONTA_PREJUIZO | integer(4) |  |  | Zeramento - Conta Prejuízo do período |
| SITUACAO | integer(4) |  |  | Situação (1-Ativa / 2-Inativa) |
| DATA_INATIVO | date(4) |  | S | Data da Situação Inativa |
| CNPJ_SCP | varchar(14) |  |  | CNPJ |
| GERAR_SPED_CONTABIL | char(1) |  |  | Gerar SPED Contábil |
| GERAR_SPED_ECF | char(1) |  |  | Gerar SPED ECF |
| POSSUI_QUADRO_SOCIETARIO_PROPRIO | char(1) |  |  | Possui quadro societário próprio |
| FORMA_ESCRITURACAO_CONTABIL | char(1) |  |  | Forma de escrituração contábil - A partir de 2015 (G - Diário Completo/R - Diário com escrituração resumida/B - Balancetes diários e balanços/A - Diário auxiliar) |
| NOME_LIVRO_DIARIO_COMPLETO | varchar(80) |  |  | Nome Livro Diário Completo |
| NOME_LIVRO_ESCRITURACAO_RESUMIDA | varchar(80) |  |  | Nome Livro com escrituração resumida |
| NOME_LIVRO_BALANCETE_DIARIO_BALANCO | varchar(80) |  |  | Nome Balancetes Diários e Balanços |
| NOME_LIVRO_DIARIO_AUXILIAR | varchar(80) |  |  | Nome Livro Diário Auxiliar |
| DATA_ABERTURA | date(4) |  |  | Data Abertura |
