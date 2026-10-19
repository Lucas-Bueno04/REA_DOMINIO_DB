# prparam — Parametros - Cadastro - Protocolos
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| emit_par | char(1) |  |  | Protocolar recebimento (S=Sim, N=Nao) |
| mode_par | varchar(80) |  |  | Modelo do relatorio |
| seqn_par | integer(4) | PK |  | Sequencial |
| ulti_par | integer(4) |  | S | Ultimo nro de Protocolo |
| CODI_EMP_ESCRITORIO | integer(4) |  | S | Empresa do escritório |
| EMITIR_COMPROVANTE_EMISSAO_PROTOCOLO | char(1) |  |  | Emitir comprovante na emissão do protocolo (S/N) |
| MODELO_EMISSAO_PROTOCOLO | varchar(80) |  |  | Modelo para a emissão de protocolo |
| CADASTRAR_FUNC_AUTOMATICO | varchar(1) |  |  | Checkbox para cadastrar funcionário automaticamente após cadastro de um usuário do Contábil |
