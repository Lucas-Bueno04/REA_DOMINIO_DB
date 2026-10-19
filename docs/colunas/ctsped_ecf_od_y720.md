# CTSPED_ECF_OD_Y720 — SPED ECF - Outros Dados - Registro Y720
2.531 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_OUTROS_DADOS | integer(4) | PK |  | Sequencial Outros Dados |
| GERAR_INFORMACAO_PERIODO_ANTERIOR | char(1) |  |  | Gerar informações de períodos anteriores |
| VALOR_LUCRO_LIQUIDO_PELA_TAXA_SELIC | numeric(14) |  |  | Valor lucro líquido do último período de apuração antes do IR e da CSLL atualizado pela taxa Selic |
| DATA_FINAL_PERIODO_APURACAO_LUCRO_LIQUIDO | date(4) |  | S | Data final do período de apuração do lucro líquido informado |
| VALOR_RECEITA_BRUTA_PERIODO_ANTERIOR | numeric(14) |  |  | Receita Bruta do período anterior |
| HOUVE_TERMO_INTIMACAO_RFB_ENTREGA_DESTE_ECF | char(1) |  | S | Houve termo de intimação pela RFB para entrega desta ECF |
| TRANSMISSAO_DESTA_ECF_DENTRO_PRAZO_PREVISTO_INTIMACAO | char(1) |  | S | A transmissão desta ECF está dentro do prazo previsto na intimação |
