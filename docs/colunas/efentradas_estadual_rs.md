# EFENTRADAS_ESTADUAL_RS — Notas Fiscais de Entradas - Dados estaduais - RS
105 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_ENT | integer(4) | PK |  | Codigo |
| I_UTILIZACAO_CREDITO | integer(4) |  | S | Sequencial |
| DISPOSITIVO_CREDITO_PRESUMIDO | integer(4) |  | S | Dispositivo do crédito presumido |
| LIMITAR_CREDITO_ICMS | char(1) |  |  | Limitar o aproveitamento do crédito de ICMS conforme Art.37 2 do Livro I RICMS/RS |
| LIMITAR_CREDITO_ICMS_PERCENTUAL | integer(4) |  |  | Percentual de limitar o aproveitamento do crédito de ICMS conforme Art.37 2 do Livro I RICMS/RS |
| CHP | varchar(12) |  | S | CHP |
| I_ESTOQUE | integer(4) |  | S | Código do lançamento |
| DATA_LEVANTAMENTO | date(4) |  | S | Data do levantamento |
| VALOR_TOTAL_ICMS_SOBRE_ESTOQUE | numeric(13) |  |  | Valor total do ICMS sobre estoque |
| VALOR_PARCELA_CREDITO | numeric(13) |  |  | Valor da parcela do crédito |
| VALOR_ICMS_DESTACADO_A_MAIOR | numeric(13) |  |  | Valor do ICMS destacado a maior |
| VALOR_ICMS_ESTORNO_DEBITO_DEVOLUCAO_MATERIAL_USO_CONSUMO | numeric(13) |  |  | Valor do ICMS Estorno de débito decorrente a devolução de materiais adquiridos para uso e consumo |
| VISTO_ELETRONICO | varchar(12) |  | S | Visto Eletronico |
