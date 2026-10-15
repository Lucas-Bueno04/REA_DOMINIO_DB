# gesocios — Socios - Cadastro
2.316 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_socio | integer(4) | PK |  | Codigo socio |
| nome | char(60) |  |  | Nome |
| sexo | char(1) |  | S | Sexo (M - Masculino/F - Feminino) |
| endereco | char(40) |  | S | Endereco |
| bairro | char(40) |  | S | Bairro |
| cidade | char(40) |  | S | Cidade |
| cep | char(8) |  | S | CEP |
| numero | integer(4) |  | S | Numero |
| uf | char(2) |  | S | UF |
| complemento | char(30) |  | S | Complemento |
| tipo_imovel | tinyint(1) |  | S | Tipo do imovel (1 - Proprio Quitado/2 - Proprio Fianciado/3 - Alugado/4 - Familiar/5 - Cedido) |
| profissao | char(40) |  | S | Profissao |
| pai | char(40) |  | S | Pai |
| mae | char(40) |  | S | Mae |
| emancipado | char(1) |  | S | Emancipado (S - Sim/N - Nao) |
| forma_emancipacao | tinyint(1) |  | S | Forma de emancipacao (1 - Casamento/2 - Ato judicial/3 - Concessão dos pais/4 - Colação de grau/5 - Emprego público efetivo/6 - Estabelecimento civil ou comercial/7 - Relação de emprego) |
| ddd_fone | integer(4) |  | S | DDD |
| fone_com | char(14) |  | S | Telefone comercial |
| fone_res | char(14) |  | S | Telefone residencial |
| fone_cel | char(14) |  | S | Telefone celular |
| fone_fax | char(14) |  | S | Telefone fax |
| nacionalidade | char(40) |  | S | Nacionalidade |
| naturalidade | char(40) |  | S | Naturalidade |
| estado_civil | tinyint(1) |  | S | Estado civil: 1=Solteiro/2=Casado/3=Viúvo/4=Divorciado/5=Concubinato/6=Separado judicialmente/7=União estável) |
| regime_casamento | tinyint(1) |  | S | Regime de Casamento (1 - Comunhao Total/2 - Comunhao Parcial/3 - Separacao Total) |
| dtnascimento | date(4) |  | S | Data de nascimento |
| tipo_insc | tinyint(1) |  |  | Tipo de inscricao (1 - CNPJ/2 - CPF) |
| inscricao | char(14) |  | S | CPF ou CNPJ |
| identidade | char(15) |  | S | Identidade |
| orgao_emissor_ident | char(14) |  | S | Orgao emissor |
| uf_ident | char(2) |  | S | UF identidade |
| data_emissao_ident | date(4) |  | S | Data emissao da identidade |
| cart_reservista | char(12) |  | S | Carteira de reservista |
| cart_ident_profissional | char(30) |  | S | Carteira profisional |
| cart_trabalho | char(7) |  | S | Carteira de trabalho |
| cart_motorista | char(15) |  | S | Carteira de motorista |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| nome_conjuge | char(40) |  | S | Nome do conjuge |
| cpf_conjuge | char(11) |  | S | CPF do conjuge |
| identidade_conjuge | char(15) |  | S | Identidade do conjuge |
| orgao_emissor_conjuge | char(14) |  | S | Orgao emisor do conjuge |
| emissao_ident_conjuge | date(4) |  | S | Data emissao da identidade do conjuge |
| uf_ident_conjuge | char(2) |  | S | UF identidade do conjuge |
| dtnascimento_conjuge | date(4) |  | S | Data de nascimento do conjuge |
| profissao_conjuge | char(40) |  | S | Profissao do conjuge |
| renda_conjuge | numeric(13) |  | S | Renda do conjuge |
| endereco_com | char(40) |  | S | Endereco comercial |
| bairro_com | char(40) |  | S | Bairro comercial |
| cidade_com | char(40) |  | S | Cidade comercial |
| cep_com | char(8) |  | S | CEP |
| uf_com | char(2) |  | S | UF comercial |
| complemento_com | char(30) |  | S | Complemento comercial |
| numero_com | integer(4) |  | S | Numero comercial |
| ddd_com | integer(4) |  | S | DDD do fone comercial |
| escolaridade | tinyint(1) |  | S | Escolaridade |
| formacao_academ | char(30) |  | S | Formacao academica |
| nivel_academ | tinyint(1) |  | S | Nivel academico (1 - Graduacao/ 2 - Pos-Graducao/3 - Mestrado/4 - Doutorado) |
| cnpj_escola | char(14) |  | S | CNPJ da escola |
| previsao_conclusao | date(4) |  | S | Previsao para conclusao |
| valor_aluguel_finan | numeric(13) |  | S | Valor do aluguel/financiamento |
| cartao_credito | char(30) |  | S | Bandeira do cartao de credito |
| plano_saude | char(40) |  | S | Plano de saude |
| plano_previdencia | char(40) |  | S | Plano de previdencia |
| hobby | char(40) |  | S | Hobby |
| recursos_tecnologicos | char(40) |  | S | Recursos tecnologicos |
| naturalidade_uf | char(2) |  | S | Estado da Naturalidade |
| codigo_pais | integer(4) |  | S | Codigo pais |
| CERTIFICADO_DIGITAL | char(1) |  | S | Possui o Certificado digital para assinatura dos atos da Junta Comercial(S/N) |
| TITULO_ELEITORAL | char(12) |  | S | Título Eleitoral |
| ZONA_ELEITORAL | char(3) |  | S | Zona Eleitoral |
| SECAO_ELEITORAL | char(4) |  | S | Secao Eleitoral |
| TITULO_ELEITORAL_CONJUGE | char(12) |  | S | Título Eleitoral do Conjuge |
| ZONA_ELEITORAL_CONJUGE | char(3) |  | S | Zona Eleitoral do Conjuge |
| SECAO_ELEITORAL_CONJUGE | char(4) |  | S | Secao Eleitoral do Conjuge |
| EMAIL | char(70) |  | S | Email |
| RESPONSAVEL_LEGAL_EMPRESA_JUNTO_BASE_RFB | char(1) |  |  | É responsável legal da empresa junto as bases da RFB |
| GUID_BRCLIENT | uniqueidentifier(16) |  | S | Id do Socio no BR Client Services |
