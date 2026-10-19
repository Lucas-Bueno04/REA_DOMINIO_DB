# prMovitens — Movimento de documentos - Itens
21.624 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| nume_mod | integer(4) | PK |  | Nro Protocolo |
| codi_ite | integer(4) | PK |  | Item |
| crec_mov | char(6) |  | S | Codigo Receita |
| vcto_mov | date(4) |  | S | Vencimento |
| vlor_mov | numeric(12) |  | S | valor |
| nliv_mov | integer(4) |  | S | Nro Livro |
| obse_imp | char(40) |  | S | Observacao Imposto |
| peri_ini | date(4) |  | S | Periodo Inicial |
| peri_fim | date(4) |  | S | Periodo Final |
| obse_out | char(80) |  | S | Observao Outro |
| dret_mov | date(4) |  | S | Data de Retorno |
| codi_fun | integer(4) |  | S | Funcionario |
| obse_ret | char(200) |  | S | Observacao de Retorno |
| obse_liv | char(40) |  | S | Observao Livro |
| baix_mov | tinyint(1) |  | S | Baixado (1=Sim, 0=Nao) |
| sequ_mov | integer(4) | PK |  | Sequencial |
| COMPETENCIA | date(4) |  | S | Competência |
| HORA_BAIXA | time(8) |  | S | Hora da baixa |
| FUNCIONARIO_RECEPCAO_DOCUMENTO_CLIENTE | varchar(60) |  |  | Recepcao dos documentos no cliente |
| CODI_OBS | integer(4) |  | S | Codigo Observacao |
| COD_USU_BAIXA | varchar(30) |  | S | Usuário da Baixa |
