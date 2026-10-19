# EFTABELA_MG_INCENTIVO_RET_FAIXAS — Tabela de incentivos do Crédito Estímulo MG - Faixas
15 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| VIGENCIA_PAR | date(4) | PK |  | Vigência |
| SEQUENCIAL | integer(4) | PK |  | Sequencial incentivo faixa |
| TIPO_PRODUTO | char(1) |  |  | Tipo de produto (I-Inferior/S-Superior/P-Importados/D-Demais) |
| OPERACOES_INTERNAS | numeric(5) |  |  | Operações internas |
| OPERACOES_INTERESTADUAIS | numeric(5) |  |  | Operações interestaduais |
| DESTINO_OPERACAO | integer(4) |  |  | Destino da operação (0-Todos/1-Contribuinte/2-Não contribuinte/3-PJ não contribuinte/4-Transf. matriz/filial) |
| SUB_GRUPO | integer(4) |  |  | SUB-GRUPO (1-IMPORTADOS/2-DEMAIS/3-ELETRÔNICOS/4-FIOS/5-CAFÉ/6-SUCOS/7-CHÁ/8-TOMATE/9-FRUTAS/10-EXTRATOS/11-CEREAIS/12-MEDICAMENTOS) |
| CRITERIO_ICMS | integer(4) |  |  | Criterio de utilização da aliquota destacado |
| ALIQUOTA_ICMS | numeric(5) |  | S | Aliquota ICMS Destacado |
| I_SEQUENCIAL_INCENTIVO | integer(4) | PK |  | Sequencial incentivo |
