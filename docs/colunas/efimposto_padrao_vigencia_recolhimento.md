# EFIMPOSTO_PADRAO_VIGENCIA_RECOLHIMENTO — Tabela de Imposto Padrão - Vigência - Recolhimento
158 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_IMP | integer(4) | PK |  | Codigo |
| UF | char(2) | PK |  | UF |
| VIGENCIA_IMP | date(4) | PK |  | Vigencia |
| I_RECOLHIMENTO | integer(4) | PK |  | Sequencial |
| CODIGO_RECOLHIMENTO | char(6) |  |  | Código do recolhimento |
| GUIA | integer(4) |  |  | Guia (1-GARE-ICMS / 2-GNRE) |
| PERIODICIDADE | integer(4) |  |  | Periodicidade (1-Mensal/2-Quinzenal/3-Decendial/4-Trimestral/5-Semanal/6-Semestral/7-Por Nota/8-Trimestral/Mensal/9-Por Vencimento/10-Diária) |
| PERIODO_SUBSEQUENTE | integer(4) |  |  | Período subsequente |
| FORMA_VENCIMENTO | integer(4) |  |  | Forma de vencimento |
| DIA_VENCIMENTO_1 | integer(4) |  |  | Dia do vencimento 1 |
| DIA_VENCIMENTO_2 | integer(4) |  |  | Dia do vencimento 2 |
| DIA_VENCIMENTO_3 | integer(4) |  |  | Dia do vencimento 3 |
| DIA_VENCIMENTO_4 | integer(4) |  |  | Dia do vencimento 4 |
| DIA_VENCIMENTO_5 | integer(4) |  |  | Dia do vencimento 5 |
| DESCRICAO | varchar(255) |  |  | Descrição |
| CLASSE_VENCIMENTO_1 | integer(4) |  |  | Classe do vencimento 1 |
| CLASSE_VENCIMENTO_2 | integer(4) |  |  | Classe do vencimento 2 |
| CLASSE_VENCIMENTO_3 | integer(4) |  |  | Classe do vencimento 3 |
| CLASSE_VENCIMENTO_4 | integer(4) |  |  | Classe do vencimento 4 |
| CLASSE_VENCIMENTO_5 | integer(4) |  |  | Classe do vencimento 5 |
| NUMERO_TTD_1 | char(20) |  |  | Número do acordo TTD para o primeiro vencimento do imposto |
| NUMERO_TTD_2 | char(20) |  |  | Número do acordo TTD para o segundo vencimento do imposto |
| NUMERO_TTD_3 | char(20) |  |  | Número do acordo TTD para o terceiro vencimento do imposto |
| NUMERO_TTD_4 | char(20) |  |  | Número do acordo TTD para o quarto vencimento do imposto |
| NUMERO_TTD_5 | char(20) |  |  | Número do acordo TTD para o quinto vencimento do imposto |
| I_RECOLHIMENTO_SPED_FISCAL | integer(4) |  | S | Código SPED Fiscal |
| ALIQUOTA | numeric(5) |  |  | Alíquota |
| TIPO | integer(4) |  |  | Tipo(1-Normal / 2-TTD) |
| UTILIZAR_CREDITO_APURACAO_ICMS | integer(4) |  |  | Utilizar o crédito na apuração do ICMS (0/1/2) |
| FORMA_RECOLHIMENTO | integer(4) |  |  | Forma de Recolhimento(1-Junto com o ICMS Normal/2-Guia de Recolhimentos Especiais) |
| DESTDA_ICMSA | integer(4) |  | S | DeSTDA ICMSA |
| GERA_CREDITO_ICMS | char(1) |  |  | Gera crédito ICMS (S-Sim/N-Não) |
| FUNDAMENTACAO_LEGAL | char(194) |  |  | Fundamentação Legal |
| APROPRIACAO_CREDITO | integer(4) |  |  | Apropriação do Crédito (1 - Data do Recolhimento / 2 - Data de Entrada) |
| TIPO_ANTECIPACAO | integer(4) |  |  | Tipo de Antecipação (1-Aquisição de arroz - Art. 4º, Anexo XVI do RICMS/2-Outras antecipações) |
| IRRF_COOPERATIVA | char(1) |  |  | IRRF de cooperativas |
| UF_FAVORECIDA | char(2) |  |  | UF Favorecida |
| CALCULA_ADICIONAL_FCP | char(1) |  |  | Calcula Adicional FCP |
| MG_DESTDA | integer(4) |  |  | DeSTDA |
| I_DETALHAMENTO_RECEITA | integer(4) |  | S | Detalhamento receita |
| CALCULAR_DEVOLUCAO | char(1) |  |  | Calcular na devolução |
| PE_CONSIDERAR_DATA_EMISSAO_PARA_VENCIMENTO_IMPOSTO | char(1) |  |  | PE - Considerar a data de emissão do documento fiscal para o vencimento do imposto |
| CREDITO_PRESUMIDO | integer(4) |  | S | Crédito presumido |
| ALIQUOTA_CREDITO_PRESUMIDO | numeric(5) |  |  | Alíquota Crédito presumido |
| CONSIDERAR_DATA_EMISSAO_PARA_VENCIMENTO_IMPOSTO | char(1) |  |  | PE - Considerar a data de emissão do documento fiscal para o vencimento do imposto |
