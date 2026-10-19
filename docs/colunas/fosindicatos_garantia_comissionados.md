# FOSINDICATOS_GARANTIA_COMISSIONADOS — Regras para o cálculo da garantia mínima para empregados comissionados.
4 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_SINDICATOS | integer(4) | PK |  | Código do sindicato. |
| I_REGRA | integer(4) | PK |  | Sequencial da regra. |
| COMPETENCIA_INICIO | date(4) |  |  | Competência de início da regra. |
| FORMA_CALCULO | smallint(2) |  |  | Forma de cálculo. (1=Piso salarial/2=Valor informado/3=Salário mínimo |
| VALOR | numeric(30) |  | S | Valor da garantia mínima da regra. |
| CALCULAR_NO_13_SALARIO | smallint(2) |  |  | Calcular no 13º salário. (0=Não/1=Sim) |
| CALCULAR_NAS_FERIAS | smallint(2) |  |  | Calcular nas férias. (0=Não/1=Sim) |
| CALCULAR_NO_AVISO_PREVIO | smallint(2) |  |  | Calcular no aviso prévio. (0=Não/1=Sim) |
| DETERMINAR_FIM | smallint(2) |  |  | Determinar competência para o fim da regra. (0=Não/1=Sim) |
| COMPETENCIA_FIM | date(4) |  | S | Competência para o fim da regra. |
| ORIGEM_REG | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| CALCULAR_NO_13_ADIANTAMENTO | smallint(2) |  |  | Calcular no 13º adiantamento. (0=Não/1=Sim) |
| CALCULAR_MULTA_ESTABILIDADE | smallint(2) |  |  | Calcular multa por estabilidade. (0=Não/1=Sim) |
| UTILIZAR_PARA_FALTAS | smallint(2) |  |  | Utilizar para o cálculo de rubricas de faltas. (0=Não/1=Sim) |
| REGIME_FEDERAL | smallint(2) |  | S | Regime federal. (1=Normal/2=Microempresa/3=Empresa de pequeno porte) |
| CALCULAR_NO_AVISO_PREVIO_REAVIDO | smallint(2) |  |  | Calcular no aviso prévio reavido. (0=Não/1=Sim) |
| CAMPO | smallint(2) |  | S | Campo. (1=Meses trabalhados) |
| OPERADOR_COMPARACAO | smallint(2) |  | S | Operador de comparação. (1=Igual/3=Maior que/4=Menor que/5=Maior igual/6=Menor igual) |
| VALOR_COMPARACAO | numeric(13) |  | S | Valor de comparação. |
| CALCULAR_PROPORCIONAL_MP_936 | smallint(2) |  |  | Calcula proporcional à redução MP 936. 0=Não/1=Sim |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
