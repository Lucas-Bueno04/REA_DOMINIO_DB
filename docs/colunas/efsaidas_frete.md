# efsaidas_frete — Saidas - Dados do frete
61 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_sai | integer(4) | PK |  | Codigo |
| modfrete_saif | char(1) |  |  | Modalidade do Frete (Cif / Fob) |
| modtransp_saif | tinyint(1) |  |  | Modalidade do Transporte (1-Rodoviario,2-Ferroviario,3-Rodo-Ferroviario,4-Aquaviario,5-Dutoviario,6-Aereo,7-Outro) |
| transportador_saif | char(1) |  |  | Transportador ( Emitente / Destinatário / Outro) |
| cnpj_transp_saif | char(14) |  | S | Cnpj do Transportador |
| uf_transp_saif | char(2) |  | S | UF do Transportador |
| iest_transp_saif | char(20) |  | S | Inscricao Estadual do Transportador |
| placa1_saif | char(8) |  | S | Placa do transportador (1) |
| uf_placa1_saif | char(2) |  | S | UF da Placa do transportador (1) |
| placa2_saif | char(8) |  | S | Placa do transportador (2) |
| uf_placa2_saif | char(2) |  | S | UF da Placa do transportador (2) |
| placa3_saif | char(8) |  | S | Placa do transportador (3) |
| uf_placa3_saif | char(2) |  | S | UF da Placa do transportador (3) |
| local_saif | char(1) |  |  | Local Recebimento ( Destinatário / Outro ) |
| cnpj_local_saif | char(14) |  | S | Cnpj do local do Recebimento |
| uf_local_saif | char(2) |  | S | UF do local do Recebimento |
| iest_local_saif | char(20) |  | S | Inscricao Estadual do local do Recebimento |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| local_saida_saif | char(1) |  |  | Local da Saida ( Emitente / Outro ) |
| cnpj_local_saida_saif | char(14) |  | S | Cnpj do local da Saida |
| uf_local_saida_saif | char(2) |  | S | UF do local da Saida |
| iest_local_saida_saif | char(20) |  | S | Inscricao Estadual do local da Saida |
| valor_frete_saif | numeric(13) |  | S | Valor do frete |
| aliq_icms_frete_saif | numeric(5) |  | S | Aliquota do ICMS do frete |
| icms_frete_saif | numeric(13) |  | S | Valor do ICMS do frete |
| codigo_municipio | integer(4) |  | S | Codigo do municipio |
| razao_social_saif | char(60) |  | S | Razao social |
| endereco_saif | char(60) |  | S | Endereco |
| numero_saif | integer(4) |  | S | Numero |
| bairro_saif | char(60) |  | S | Bairro |
| complemento_saif | char(40) |  | S | Complemento |
| cep_saif | char(8) |  | S | CEP |
| quantidade_saif | numeric(15) |  | S | Quantidade |
| especie_saif | char(60) |  | S | Especie |
| marca_saif | char(60) |  | S | Marca |
| numeracao_saif | char(60) |  | S | Numeracao |
| peso_liquido_saif | numeric(15) |  | S | Peso liquido |
| peso_bruto_saif | numeric(15) |  | S | Peso bruto |
| TIPO_INSC_SAIF | integer(4) |  | S | Tipo da inscrição (1 - CNPJ/2 - CPF) |
| TIPO_INSC_LOCAL_SAIDA_SAIF | integer(4) |  | S | Tipo da inscrição (1 - CNPJ/2 - CPF/3 - CEI/4 - Outros) - Local da Coleta |
| TIPO_INSC_LOCAL_SAIF | integer(4) |  | S | Tipo da inscrição (1 - CNPJ/2 - CPF/3 - CEI/4 - Outros) - Local da Entraga |
| CODIGO_MUNICIPIO_LOCAL_SAIDA_SAIF | integer(4) |  | S | Código do Município - Local da Coleta |
| CODIGO_MUNICIPIO_LOCAL_SAIF | integer(4) |  | S | Código do Município - Local da Entrega |
