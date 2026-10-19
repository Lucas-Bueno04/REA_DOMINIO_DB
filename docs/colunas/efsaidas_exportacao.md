# efsaidas_exportacao — Notas Fiscais de Saida - Exportacao do PER/DCOMP
53 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_sai | integer(4) | PK |  | Saida |
| numero_re | numeric(12) |  | S | Numero RE |
| cod_pais | integer(4) |  |  | Codigo do pais |
| despacho | varchar(14) |  |  | Numero do despacho |
| embarque | date(4) |  | S | Data do embarque |
| valor_despacho | numeric(13) |  |  | Valor do despacho |
| cod_moeda | integer(4) |  |  | Codigo da moeda |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| data_declaracao | date(4) |  | S | Data da declaracao de exportacao |
| data_averbacao | date(4) |  | S | Data de averbacao |
| natureza_exportacao | char(2) |  |  | NATUREZA DE EXPORTACAO (D - DIRETA/I - INDIRETA/DS - DIRETA SIMPLIFICADA/IS - INDIRETA SIMPLIFICADA/S - SEM DECLARAÇÃO/DD - E DIRETA/DI - E INDIRETA ) |
| numero_embarque | char(19) |  |  | Numero do embarque |
| tipo | integer(4) |  |  | Tipo do conhecimento |
| data_registro | date(4) |  | S | Data do registro de exportacao |
| I_SISCOMEX | integer(4) |  | S | Sequencial do SISCOMEX |
| PESO_LIQUIDO | numeric(18) |  |  | Peso Líquido |
| EXPORTACAO_CONCLUIDA | char(1) |  |  | Exportação concluída |
| DESTINO_DIFERE_CLIENTE | char(1) |  |  | Destino diferente cliente |
| DESTINO_DIFERE_CLIENTE_PAIS | integer(4) |  | S | Pais destino diferente cliente |
