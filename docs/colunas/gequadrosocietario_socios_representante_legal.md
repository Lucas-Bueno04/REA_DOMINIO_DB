# GEQUADROSOCIETARIO_SOCIOS_REPRESENTANTE_LEGAL — Empresa - Cadastro - Quadro Societario - Socios - Representante Legal
34 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| DATA | date(4) | PK |  | Data |
| I_SOCIO | integer(4) | PK |  | Sócio |
| TIPO | char(1) | PK |  | Tipo (S - Sócio/A - Administrador/R - Representante Legal/ E - Empresário) |
| I_REPRESENTANTE | integer(4) | PK |  | Sequencial |
| CPF | varchar(11) |  |  | CPF |
| NOME | varchar(40) |  |  | Nome |
| QUALIFICACAO | integer(4) |  |  | Qualificação (1-Procurador/2-Curador/3-Mãe/4-Pai/5-Tutor/6-Outro) |
