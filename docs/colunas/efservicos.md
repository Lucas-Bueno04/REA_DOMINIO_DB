# efservicos — Notas Fiscais de Servico
585.771 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_esp | integer(4) |  |  | Especie |
| codi_cli | integer(4) |  |  | Cliente |
| codi_emp | integer(4) | PK |  | Empresa |
| codi_ser | integer(4) | PK |  | Codigo |
| sigl_est | char(2) |  |  | Estado |
| codi_acu | integer(4) |  |  | Acumulador |
| seri_ser | char(7) |  |  | Serie |
| nume_ser | numeric(15) |  |  | Documento |
| segi_ser | integer(4) |  |  | Segmento |
| atex_ser | numeric(15) |  | S | Documento final |
| dser_ser | date(4) |  |  | Data do servico |
| ddoc_ser | date(4) |  |  | Data de emissao |
| vcon_ser | numeric(13) |  | S | Valor contabil |
| obse_ser | varchar(300) |  | S | Observacao |
| situ_ser | char(1) |  | S | Campo nao utilizado |
| codm_ser | integer(4) |  | S | Municipio |
| codi_usu | char(30) |  | S | Usuario |
| dorig_ser | date(4) |  |  | Data de origem da nota |
| codi_obs | integer(4) |  | S | Codigo da observacao |
| fatocrf_ser | char(1) |  |  | Fato Gerador da CRF(E-emissao/P-pagamento) |
| fatoirrf_ser | char(1) |  |  | Fato Gerador do IRRF(E-emissao/P-pagamento) |
| cancelada_ser | char(1) |  | S | Nota cancelada(S/N) |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| fatocrfop_ser | char(1) |  | S | Fato gerador da CRFOP(E - emissão/P - pagamento) |
| fatoirrfp_ser | char(1) |  | S | Fato gerador da IRRFP(E - emissão/P - pagamento) |
| codigo_municipio | integer(4) |  |  | Codigo do municipio |
| situacao_ser | tinyint(1) |  | S | Codigo do modelo do documento fiscal |
| cfps_ser | integer(4) |  | S | Codigo fiscal da prestacao de servicos |
| sub_serie_ser | char(3) |  |  | Sub Serie |
| serie_old_ser | char(7) |  | S | Serie backup |
| deducao_ser | numeric(13) |  | S | Valor da deducao |
| chave_eletronica | varchar(50) |  | S | Chave eletronica |
| SERI_IDX_SER | char(7) |  |  | Serie sem espacos |
| VALOR_PRESENTE_SER | numeric(13) |  |  | Valor presente |
| VALOR_PRESENTE_TAXA_SER | numeric(13) |  |  | Taxa valor presente |
| VALOR_PRESENTE_JUROS_SER | numeric(13) |  |  | Juros valor presente |
| VALOR_PRESENTE_TIPO_TAXA_SER | char(1) |  |  | Tipo taxa valor presente (M=Mensal/ A=Anual/ D=Diario) |
| TIPO_TITULO_SER | tinyint(1) |  |  | Tipo do Titulo (0=Duplicata/1=Cheque/2=Promissória/3=Recibo/4=Clientes/5=Documento Fiscal/99=Outros) |
| IDENTIFICACAO_SER | varchar(255) |  | S | Identificacao do titulo |
| CODIGO_INFORMACAO | integer(4) |  | S | Código da informação complementar |
| INFORMACAO_COMPLEMENTAR | varchar(255) |  | S | Informação complementar |
| DATA_SERVICO | date(4) |  |  | Data de serviço da nota |
| I_SCP | integer(4) |  | S | Sequencial do SCP |
| SUB_SERIE_IDX_SER | char(3) |  | S | Sub Serie sem espaços |
| RN_CODIGO_TRIBUTACAO | integer(4) |  | S | RN - Tributação |
| CONFERIDO | char(1) |  |  | Conferido (S/N) |
| VALOR_SERVICOS_SER | numeric(13) |  |  | Valor de serviço |
| VALOR_DESCONTO_SER | numeric(13) |  |  | Valor de Desconto do serviço |
| VALOR_TOTAL_IBS | numeric(13) |  |  | Valor Total IBS |
| VALOR_TOTAL_CBS | numeric(13) |  |  | Valor Total CBS |
