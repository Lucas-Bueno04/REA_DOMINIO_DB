# Andamento

Última atualização: 2026-10-15

## Fases
| Fase | Descrição | Situação |
|---|---|---|
| 0 | Preparação (stack, venv, teste de conexão) | **concluída** (falta só `config/.env` e trocar a senha) |
| 1 | Descoberta de tabelas e colunas | **concluída** |
| 2 | Relacionamentos | **concluída** |
| 3 | Engenharia reversa do modelo (entidades de negócio) | **núcleo concluído** — 75 entidades em 6 arquivos (Fiscal 22, Contábil 11, Folha 17, Honorários 13, Geral 11, Comum 1) + 2 consultas agregadas. Faltam módulos menores e as áreas de maior volume ainda sem entidade (ver cobertura) |
| 4 | Camada de consulta | **concluída** (`src/server/motor.py`, `sqlbuilder.py`, `config/seguranca.yaml`) |
| 5 | Servidor MCP | **concluída** (`src/server/mcp_server.py`, 12 ferramentas; stdio e HTTP; `executar_servidor.cmd`) — falta registrar no Claude Code |
| 6 | Qualidade e segurança | **parcial** — 61 testes automatizados + 2 testes ponta a ponta; faltam teste de carga e revisão de papéis/autenticação |
| 7 | Operação | pendente (serviço Windows, rotação de logs, autenticação HTTP) |

Tudo é regenerável em ordem: `catalogo.py` → `indices.py` → `joins_sql.py` → `relacoes.py` → `exportar_grafo.py` (ver "Como regenerar").

## Fase 1 — catálogo (`data/catalog/dominio_catalog.db`)
- 5.140 objetos do owner `bethadba` (4.835 tabelas base, 203 temporárias globais, 102 views); 4.844 na lista do gerador, 4.787 legíveis pelo usuário de leitura.
- 60.381 colunas (tipo, tamanho, nulo, PK, padrão, comentário); 4.997 tabelas e 55.807 colunas com descrição.
- 6.770 FKs declaradas; 12.373 índices (5.028 únicos); 42 tabelas base sem PK (usam índice único quando existe).

## Fase 2 — relacionamentos
**Fonte principal: o que a própria Domínio usa.** Os `.pbd` Unicode (PowerBuilder 12) guardam os DataWindows/SQL em UTF-16LE, em cadeias de blocos `DAT*` de 512 bytes (`4 bytes marca + 4 próximo + 2 tamanho + dados`). O SQL vem entrecortado por separadores binários, então não se reconstrói a instrução inteira: minera-se `alias.coluna = alias.coluna` no texto de cada objeto, resolvendo o alias pela definição mais próxima e **validando as duas colunas contra o catálogo**.

| Resultado | Valor |
|---|---|
| Arquivos analisados | 1.154 (`*.pbd`, `*.exe` de `C:\Contabil`; 1,6 GB; 115 s; 0 erros) |
| Pares de colunas observados | 24.821 (769.004 ocorrências) |
| Pares de tabelas observados | 13.036 |
| FKs declaradas vistas em uso real | 4.285 de 6.490 (66%) |
| Relações usadas pela Domínio sem FK declarada | 8.751 pares de tabelas |
| Mapa programa → tabelas | 36.554 vínculos (942 arquivos × 4.842 tabelas) |

**Grafo final: 13.792 relações** (fora as 797 de tabelas temporárias):

| Origem | Tipo | Relações | Confiança |
|---|---|---|---|
| declarada (+observada) | fk | 6.298 | 1,0 |
| declarada (+observada) | vigência | 471 | 1,0 |
| observada | fk | 2.397 | 0,5–0,9 (pelo nº de usos) |
| observada | vigência | 1.383 | idem |
| observada | ligação (sem chave completa) | 2.721 | idem |
| inferida | fk | 522 | 0,6 |

Cobertura (tabelas base legíveis com ao menos uma relação): Fiscal 97%, Contábil 95%, Societário 94%, Pessoal 93%, Financeiro 91%, Processos 90%, Geral 61%, Sistema 35%. As sem relação (383) são sobretudo configuração, log e suporte — lista em `exports/tabelas_sem_relacao.txt`.

### Calibração da inferência (lição aprendida)
A 1ª versão inferia relações por coincidência de colunas de chave e gerou **153.598** (ruído: `competencia` casava com ~458 tabelas). Usando as FKs declaradas como verdade-terreno (`scripts/calibrar_inferencia.py`):

| Regra | Inferidas | Precisão* | Cobertura |
|---|---|---|---|
| só coincidência de chave (25 filhas máx.) | 8.783 | 17% | 23% |
| + pai único com aquela chave | 2.356 | 45% | 16% |
| **+ nome da filha começa com o do pai (adotada)** | 2.446 | **72%** | 27% |
| ambas | 694 | 74% | 8% |

\*limite inferior: falsos positivos podem ser relações reais não declaradas. As inferidas novas (522) entram com confiança 0,6.

### Verificações de qualidade
- Orientação filha/pai das observadas concorda com a FK declarada em 41 de 42 casos comparáveis.
- Amostra de observadas com confiança ≥ 0,9 conferida manualmente: coerentes (ex.: `eftabecfm.codi_ecm → efsaidas.codi_sai`, `efsdoimp → geempre`).
- Bug corrigido: ligações que omitem `codi_emp` invertiam pai/filha (`GEIMPOSTO_VIGENCIA` aparecia como pai de `ctcontas`); agora a chave do pai é testada sem `codi_emp`.
- Descoberta útil: várias tabelas ligam-se a `ctcontas`/`cthispad` por **várias colunas** (ex.: `ctlancto.cdeb_lan` e `ccre_lan` → `ctcontas.codi_cta`; `GEIMPOSTO_VIGENCIA.ctrc_imp`, `ctvd_imp`… → `ctcontas.codi_cta`). Cada par fica registrado em `relacao_colunas`.

### Limitações conhecidas
- Relações `ligacao` e `vigencia` não têm chave completa de nenhum lado: servem para sugerir JOIN, não garantem cardinalidade.
- Ligações por intervalo de vigência (data entre início e fim) não aparecem como igualdade; o JOIN por período terá de ser modelado na Fase 3.
- JOINs montados dinamicamente em PowerScript (concatenação de strings) podem não aparecer na mineração.
- Relações com a tabela `geempre` por `codi_emp` dominam o grafo (1.390 filhas); ao navegar, trate `codi_emp` como filtro de empresa, não como aresta.

## Fase 3 — módulo Fiscal (concluído em 2026-10-15)
**Entregas:** `src/model/modulos/fiscal.yaml` (22 entidades) e `comum.yaml` (empresa); formato em `docs/formato-modelo.md`; documentação gerada em `docs/modelo-fiscal.md` (diagrama Mermaid, ficha de cada entidade com % de preenchimento por coluna, domínios de códigos); gerador de SQL `src/server/sqlbuilder.py`.

| Grupo | Entidades |
|---|---|
| Cadastros | cliente, fornecedor, produto, acumulador, natureza_operacao (CFOP), especie_documento, imposto, empresa |
| Saídas | nota_saida, item_nota_saida, imposto_nota_saida, parcela_nota_saida, pagamento_nota_saida |
| Entradas | nota_entrada, item_nota_entrada, imposto_nota_entrada, parcela_nota_entrada, pagamento_nota_entrada |
| Serviços | nota_servico, imposto_nota_servico, parcela_nota_servico, pagamento_nota_servico |
| Apuração | apuracao_imposto (saldos por imposto/competência) |

**Como foi validado (4 camadas):**
1. `validar_modelo.py` (catálogo, sem banco): tabelas, colunas, domínios, junções que cobrem a chave única do lado remoto (senão multiplicariam linhas), relação existente no grafo, caminho de acesso eficiente → **0 erros, 0 avisos**; as 22 ligações de vínculo têm respaldo no grafo (as de produto e imposto vêm de relações *observadas* nos programas da Domínio).
2. `testar_entidades.py` (banco real, só leitura): as 23 entidades executam, com empresa escolhida por tabela; **nenhum vínculo multiplica linhas**; 2–20 ms por consulta.
3. `conciliar_fiscal.py` (significado): a soma do modelo **bate centavo a centavo com a apuração da própria Domínio** em 6 de 6 competências para saídas e entradas (ICMS, empresa 1430) e serviços (ISS, empresa 603).
4. `perfil_colunas.py`: taxa de preenchimento de cada coluna exposta (só agregados).

**Descobertas que mudam o uso dos dados:**
- A apuração soma o valor contábil **por imposto** (`imposto_nota_*.valor_contabil`), não o `valor_contabil` do cabeçalho. Somar o cabeçalho das entradas deu 418.479,86 contra 372.995,98 apurados (notas sem ICMS não entram). Para serviços divergiu 5.299,00 em 1 de 6 meses.
- O mês de apuração é o da **data de movimento** (`dsai_sai`/`dent_ent`/`dser_ser`). A coluna `competencia` (`compte_*`) vale `1900-01-01` em 99,9% das notas e não serve como período.
- `situacao` das notas **não é** sinônimo de cancelada: 92% das notas canceladas têm situacao=2, mas só 59% das notas com situacao=2 estão canceladas. Seu significado ficou marcado como **não confirmado**; usar `cancelada`.
- `codigo_municipio` (código interno da Domínio, não IBGE) só é preenchido em ~5–6% das notas; as colunas legadas `codm_*` são sempre 0/nulas.
- `efimpsai`/`efimpent`/`efimpser` têm `codi_emp` no meio da chave primária (não lideram o índice): as consultas dessas entidades **exigem nota ou período** (`exige_algum`).
- O comentário do banco de `situacao_*` ("Codigo do modelo do documento fiscal") está errado em relação aos dados.

**Limites desta entrega (para não superestimar):**
- 23 entidades cobrem o núcleo fiscal, não as ~2.700 tabelas `EF*`; o restante será atendido pela camada genérica `consultar_tabela` (Fase 5).
- A conciliação cobriu 2 empresas e os impostos ICMS (1) e ISS (3); os demais impostos (PIS, COFINS, IRRF…) não foram conferidos.
- Códigos de `origem_registro` (valores até 40) e `situacao` seguem sem significado confirmado; vários domínios estão marcados `confirmado: parcial`.
- O teste de fumaça lê 3 linhas por entidade; não prova que todas as combinações de filtro funcionam (testes de contrato vêm na Fase 6).
- `sensivel` está apenas marcado no modelo; o mascaramento ainda não é aplicado.
- Teste feito só em leitura sem bloqueio (`READ UNCOMMITTED`), mas as varreduras de perfil leem tabelas inteiras (agregados): rodar fora do horário de pico em produção.

## Fase 3 — módulo Contábil (concluído em 2026-10-15)
**Entregas:** `src/model/modulos/contabil.yaml` (11 entidades + consulta `balancete`), `docs/modelo-contabil.md`, `montar_balancete()` em `src/server/sqlbuilder.py`, filtro de várias colunas (OR) no gerador e no validador.

| Grupo | Entidades |
|---|---|
| Plano e cadastros | conta_contabil, historico_padrao, centro_custo, departamento, lancamento_padrao |
| Lançamentos | lote_lancamento, lancamento (livro diário), lancamento_centro_custo |
| Elo Fiscal × Contábil | contabilizacao_nota_saida, contabilizacao_nota_entrada, contabilizacao_nota_servico |
| Consulta agregada | balancete de verificação (saldo anterior, débitos, créditos) |

**Validação:** modelo 0 erros (1 aviso explicado); as 34 entidades dos dois módulos executam no banco real sem multiplicar linhas; balancete testado em 7 empresas de portes diferentes (até 187 mil lançamentos/ano, 1,6 s).

**Descobertas que mudam o uso dos dados:**
- **Conta e histórico pertencem ao PLANO, não à empresa.** 15 empresas usam o plano de outra (3 planos compartilhados, ex.: empresas 1729/1730/1732 usam o da 1733). Ligar por `codi_emp` gera 1.603 contas órfãs contra 166 ligando por `codi_emp_plano`; e o histórico dos 781 lançamentos de plano alheio só é achado por `codi_emp_plano` (781 de 781 faltam por `codi_emp`).
- **Todo lançamento pertence a um lote** (0 sem lote). Lotes tipo `X` = 1 débito × 1 crédito; `D`, `C`, `V` têm linhas com um dos lados zerado (≈1,4 mi de lançamentos). O equilíbrio vale **por lote**.
- **Débitos = créditos em 100% dos lotes** da empresa 1430 (40.317 lotes, tipos X/V/C/D; total 248.988.467,04 nos dois lados) e no balancete das 7 empresas testadas (invariantes: Σ débitos = Σ créditos, Σ saldo anterior = 0, Σ saldo final = 0, e Σ do balancete = soma direta de `ctlancto`).
- **`orig_lan`**: o comentário do banco só cobre 1–19. Confirmados pelos dados: 5 (saídas), 6 (entradas), 7 (serviços), 10 (apuração), 11 (pagamento de guia). O código **49 (54% de todos os lançamentos) é cupom fiscal eletrônico (CF-e)** — inferido: 100% ligado a `EFCUPOM_FISCAL_ELETRONICO_LANCTO`. Outros (20, 39, 70, 34…) seguem desconhecidos.
- **Elo nota × lançamento:** o **maior** lançamento ligado à nota é igual ao valor contábil dela (98,8%–100% em 6 amostras). A **soma** só fecha quando a empresa contabiliza apenas o total (100% em saídas da 1430, mas 65%/33%/64% em outras empresas). Em `efsaidas_lancto`, `codi_emp` é a empresa da nota e `fili_lan` a do lançamento (diferem em 17% das linhas: notas de filiais contabilizadas na matriz).
- **Não existe saldo armazenado:** `CTLANCTO_SALDO` e `CTLANCTO_PROCESSAMENTO` têm 0 linhas. Balancete e razão são sempre calculados dos lançamentos.
- **Dados com erro:** 143 lançamentos com data acima de 2100 (máx. 9282-06-06); 33 lançamentos em contas sintéticas; 166 débitos e 115 créditos apontam para contas inexistentes.
- O índice `(codi_emp, data_lan, orig_lan, …)` sustenta filtro por período; `(codi_emp, codi_emp_plano, cdeb_lan|ccre_lan, data_lan, …)` sustenta o razão por conta.

**Correção de uma generalização minha:** na primeira conferência eu havia concluído que "a soma dos lançamentos de uma nota é igual ao valor da nota" (7.269 de 7.269) — verdade só para a empresa 1430. Ao testar outras empresas e as notas de entrada e serviço, a regra segura passou a ser a do *maior lançamento*, e o modelo foi ajustado.

**Limites:**
- Sem saldo armazenado, o balancete não pôde ser conciliado com um total calculado pela Domínio (como foi feito com a apuração fiscal); a validação é por invariantes contábeis e pela soma direta.
- Balancete só de contas analíticas, sem totalização das sintéticas por prefixo de `clas_cta` e sem filtro por filial já exposto como ferramenta (o parâmetro existe no gerador).
- O razão é obtido com a entidade `lancamento` e o filtro `conta` (débito OU crédito); o saldo acumulado linha a linha ainda não é calculado.
- Não foram modeladas as demonstrações (DRE, DFC, DMPL, DOAR…) nem o SPED/ECD/ECF (`CTSPED_*`, 88 tabelas) nem a conciliação bancária (`CTEXTRATO_*`).
- Relação lançamento↔histórico não aparece nos JOINs dos programas da Domínio (fica como aviso do validador); sustentada pelos dados.

## Fase 3 — módulo Folha (concluído em 2026-10-15)
**Entregas:** `src/model/modulos/folha.yaml` (17 entidades), `docs/modelo-folha.md`; no gerador/validador: colunas **calculadas** (`liquido = proventos − descontos`), **coalescidas** (primeiro valor não nulo entre vínculos) e marcação de **sensibilidade em vínculos**.

| Grupo | Entidades |
|---|---|
| Cadastros | empregado, cargo, departamento_folha, centro_custo_folha, filial_folha, sindicato, servico_folha, evento, evento_padrao |
| Cálculo | movimento_folha (valor por evento), base_folha (proventos, descontos, líquido), liquido_folha |
| Vínculo | rescisao, afastamento, falta, ferias_periodo_aquisitivo, ferias_gozo |

**Validação:** 51 entidades dos 3 módulos passam no validador (0 erros, 2 avisos explicados) e no teste contra o banco real, sem multiplicar linhas.

**Conciliação interna (a Domínio guarda os totais calculados):** em 9 empresas / 65.877 linhas de base, `fobasesserv.proventos` = Σ eventos P → **65.869 (100,0%)**; `descontos` = Σ eventos D → **65.560 (99,5%)**; o líquido registrado em `foliquidosfilepr` bate com proventos − descontos em ≈99,8% dos pares empregado×cálculo. A regra que fecha é: *o evento entra nos totais se `aparece_recibo = 'S'` — no cadastro próprio da empresa ou, na falta, no padrão — ou se não tem cadastro nenhum*.

**Descobertas que mudam o uso dos dados:**
- **Eventos (rubricas) podem não existir na própria empresa.** 208.504 movimentos (7,1%) de 310 empresas não têm evento em `foeventos` da empresa; 309 delas não têm NENHUM evento próprio e usam os **eventos padrão** (`foeventosdef`, global). 92% resolvem pelos padrões; o resto existe só em outras empresas. Ligar movimento→evento só por `codi_emp` deixa nome e flags vazios.
- **Eventos sem cadastro algum CONTAM nos totais** (default 'S'). Sem isso a regra falha nessas empresas (ex.: descontos batendo em 19% na empresa 37; com a regra, 100%).
- **Eventos D que não aparecem no recibo não entram em `descontos`** (ex.: evento auxiliar 9176): somar todos os D diverge em 60% das linhas da folha mensal.
- **`fobasesserv` tem ~25 colunas marcadas "SEM USO"** pelo próprio banco (INSS, IRRF, FGTS ficam em outras tabelas, ainda não modeladas). O modelo expõe só as vivas.
- **Tipos de folha 60, 61 e 92 não são documentados.** A hipótese "60/61 = rescisão" foi testada e **refutada** (1,6% de coincidência com mês de rescisão). Documentados: 11 mensal, 31–36 semanas, 41 adiantamento, 42 complementar, 51/52 13º, 70 PLR, 91 resilição de professor.
- **`forescisoes` tem chave (empresa, cálculo, empregado, tipo)**: pode haver rescisão normal (6.904) e complementar (288) do mesmo empregado. Contar demissões = `tipo = 1`.
- **`foempregados` não tem situação (ativo/demitido)**; vem de `rescisao` e `afastamento`. `categoria`, `vinculo`, `motivo` de rescisão e `situacao_mes` são códigos sem tabela de descrição: significado não confirmado.
- `foferias` (nome óbvio) é uma estrutura vazia; as férias reais estão em `FOFERIAS_AQUISITIVOS`/`FOFERIAS_GOZO` (tipos 5, 7 e 8 de gozo são provisão/simulação, não férias gozadas).

**Privacidade (decisão tomada no modelo, reversível):** a Folha contém dado pessoal e financeiro. O modelo expõe só o necessário a DP e **deixa de fora de propósito** as categorias sensíveis (LGPD art. 5º, II) e de risco: saúde (grupo sanguíneo, RH, deficiência, exames, CID, CAT, acidente), raça/cor, filiação sindical, filiação familiar, dados bancários, endereço, telefone, e-mail, título de eleitor, reservista, habilitação e foto. Colunas marcadas `sensivel` (nome, CPF, PIS, identidade, nascimento, salário, valores pagos): **30 no total nos 3 módulos**, a serem mascaradas por padrão na Fase 4 (política ainda pendente). O perfil de colunas **não guarda mínimo/máximo** dessas colunas (verificado por `scripts/verificar_privacidade_perfil.py`).

**Correções minhas feitas durante o trabalho:**
1. Eu havia lido a chave de `forescisoes` como (empresa, empregado) e escrito "só uma rescisão por empregado"; o validador mostrou a PK real e a regra foi removida.
2. A primeira conciliação da Folha deu "99,99%" porque as 5 empresas escolhidas tinham eventos próprios; ao incluir empresas sem eventos próprios a taxa caiu (proventos 98,2%, descontos 94,9%) e isso revelou o papel dos eventos padrão. Com a regra completa: 100,0% e 99,5%.
3. Uma sonda de estrutura exibiu 1 linha de `foliquidosfilepr` (código de empregado e valor, sem nome); passei a usar só agregados.

**Limites:**
- INSS, IRRF, FGTS, GPS e eSocial da folha não foram modelados (`fobasesirrf`, `fofgtsfilial`, `foguiainss`, `FOESOCIAL_*`, 60 tabelas).
- 317 linhas de base (0,5%) ainda divergem em `descontos`, quase todas na empresa 603 (maior); causa não investigada.
- Provisões (`foprovisoes`), pagamentos, rescisão detalhada, médias e a folha de autônomos/RPA não foram modeladas.
- Não existe tabela de descrição para `categoria`/`vinculo`/`motivo`; a tradução desses códigos depende da Domínio.

## Fase 3 — módulo Honorários (concluído em 2026-10-15)
**Entregas:** `src/model/modulos/honorarios.yaml` (13 entidades + consulta `contas_a_receber`), `docs/modelo-honorarios.md`, `montar_contas_a_receber()` em `src/server/sqlbuilder.py`, `scripts/testar_contas_a_receber.py`.

| Grupo | Entidades |
|---|---|
| Cadastros | cliente_honorarios, classificacao_cliente, evento_honorario, contrato, conta_financeira |
| Faturamento | faturamento, parcela_faturamento, item_parcela |
| Recebimento | recebimento, item_recebimento |
| Razões e fiscal | conta_corrente_cliente, conta_corrente_escritorio, nfse |
| Consulta agregada | contas_a_receber (faturado, recebido e saldo por parcela) |

**Validação:** 64 entidades dos 4 módulos passam (0 erros, 2 avisos explicados) e executam no banco real sem multiplicar linhas.

**Conciliações (a Domínio guarda as baixas e os razões):**
- `valor` (líquido) `= valor_recebido − juros − multa + desconto` em **43.042 de 43.042** recebimentos (100%) e 43.581 de 43.603 itens (99,95%). O `valor_recebido` é o BRUTO (inclui juros e multa).
- Σ itens do recebimento = recebimento: 99,95% (bruto) e 99,998% (líquido).
- **Saldo da parcela = Σ valor dos itens − Σ valor líquido dos recebimentos**: 42.824 quitadas, **399 em aberto**, 1 inconsistente (99,998%). Somar também desconto/quitado/refaturado/reparcelado produz 588 "baixadas a mais" artificiais (testei e descartei).
- A consulta `contas_a_receber` paginada reproduz ao centavo o saldo independente nos 2 escritórios (R$ 240.050,41 e R$ 17.069,53), sem repetir nem pular parcela (41.241 parcelas em 8,8 s).
- Item de faturamento × conta corrente do cliente: valor igual em 99,6%. Recebimento × conta corrente do escritório: igual ao **bruto** em 98,3% (746 recebimentos sem movimento).

**Descobertas que mudam o uso dos dados:**
- **Em `HR*`, `CODI_EMP` é o ESCRITÓRIO**, não a empresa-cliente. Há 2 escritórios (códigos 1 e 930). Clientes fixos (tipo F, 1.644) ligam a `geempre` por `I_CLIENTE_FIXO` (100% existem); eventuais (tipo E, 1.274) não têm empresa.
- **O módulo não tem dados de 2026:** último faturamento em 2025-12-31 e última NFS-e em 2025-04-16. Contas a receber "em aberto" refletem esse corte.
- 1.141 dos 2.918 clientes são **pessoas físicas** (CPF).
- Dos contratos, nenhum com término definido está vigente (481 encerrados); 583 sem término.
- Parcela não guarda valor: o valor faturado é a soma dos itens.

**Privacidade:** não foram expostos endereço, e-mail, telefones, site, caixa postal nem as observações livres do cliente; nome e inscrição (CPF/CNPJ) marcados `sensivel: parcial`; valores cobrados/recebidos marcados `financeiro`. Agência, conta e convênio das contas financeiras do escritório também ficaram de fora.

**Limites:** contas a pagar do escritório (`HRLANCAMENTO_PAGAR*`, `HRPAGAMENTO*`), renegociações, adiantamentos, cheques, parâmetros e a integração contábil (`HR*_LANCTO`) não foram modeladas; o significado de `I_TIPO_CONTRATO` e `I_CATEGORIA_*` (sem tabela descritiva modelada) não foi investigado.

## Fase 3 — módulo Geral (concluído em 2026-10-15)
**Entregas:** `src/model/modulos/geral.yaml` (11 entidades) e `comum.yaml` ampliado (empresa completa), `docs/modelo-geral.md`, `docs/modelo-comum.md`, `scripts/sondar_geral.py`.

| Grupo | Entidades |
|---|---|
| Empresa | empresa (cadastro completo, com município, natureza jurídica e CNAE) |
| Societário | socio, quadro_societario, participante_societario |
| Referências | municipio, estado, pais, cnae, natureza_juridica, atividade_secundaria, feriado |
| Configuração fiscal | imposto_vigencia (impostos por vigência: periodicidade, vencimento, recolhimento, contas) |

**Validação:** 75 entidades dos 6 arquivos passam (0 erros, 2 avisos explicados) e executam no banco real sem multiplicar linhas. **Conciliação societária:** a soma da participação dos sócios é 100% em 1.474 de 1.486 quadros (99,2%; 12 abaixo, nenhum acima) e as quotas dos sócios fecham com as do quadro em 1.472 (99,1%).

**Descobertas:**
- **62% das empresas estão inativas** (1.227 de 1.969), mas as flags `usa_*` seguem ligadas (729 inativas ainda "usam escrita fiscal"); só `status = 'A'` indica cliente atual. Motivos: 636 outros, 307 transferida, 282 baixada, 2 inadimplente.
- `geempre_vigencia` duplica o cadastro com **1 vigência por empresa** (1.967 de 1.968): não virou entidade.
- 61 das 742 empresas ativas são **pessoas físicas** (CPF); 141 no total.
- O tipo de participante `E` (64 linhas) **não é documentado** (o comentário só fala S/A/R, e `R` não existe nos dados).
- 412 de 2.125 sócios aparecem em mais de uma empresa (cadastro global).
- `periodicidade` do imposto na **configuração** (`geimposto_vigencia.pdic_imp`: 1 mensal … 6 semestral) usa codificação **diferente** da apuração (`efsdoimp.pdic_sim`: 6 mensal, 7 trimestral…). Misturar as duas dá resposta errada.
- `municipio.codigo` é um código interno da Domínio (1 a 5.576), não o IBGE (que está em `ibge`).

**Fora do modelo de propósito:** certificados digitais, usuários e grupos do banco, `GELOGUSER` (2 milhões de linhas de horas por usuário), filas de integração (`GEATENDIMENTO*`), preferências de tela, `GERESPONSAVEL`. Sócios: só nome, CPF/CNPJ, sexo e UF (sem endereço, filiação, cônjuge, documentos, telefones). Empresa: sem contatos, endereço, observações livres e dados do responsável legal além do nome.

## Fase 3 — módulo EFD-Reinf (2026-10-15)
**Entregas:** `src/model/modulos/reinf.yaml` (3 entidades), `docs/modelo-reinf.md`. Validado (0 erros, 0 avisos) e executado no banco real (3 de 3, sem multiplicar linhas).

| Entidade | Tabela | Linhas |
|---|---|---|
| envio_reinf | `efd_reinf_envio_arquivos` | 75.187 |
| erro_envio_reinf | `efd_reinf_envio_arquivos_erros` | 12.024 |
| retorno_reinf (+ fechamento R-2099) | `efd_reinf_retorno_arquivos` | 25.231 |

**Descobertas:** situação 1 = recibo (99,7%), 3 = rejeitado (99,8% com erro) — ambos `confirmado: parcial`; `tipo_envio` deduzido do cruzamento com o evento (E=R-9000, F=fechamento, B=reabertura); `i_filial` nunca é 0; `ambiente` O=75.106, T=81.
**Fora de propósito:** XML do evento, log de comunicação, retornos por evento (R-2010/2020/2050/2060) e complementos de nota (`EF*_EFD_REINF`) — próxima rodada.

## Cobertura do modelo (`scripts/cobertura_modelo.py`, 2026-10-15)
O modelo curado toca **75 tabelas (1,6% das 4.727 fontes do gerador)**, que concentram **17,2% das 264,6 milhões de linhas**. Não é objetivo cobrir tudo à mão: as demais tabelas serão atendidas pela **camada genérica** (`consultar_tabela` sobre o catálogo, Fase 5).

| Departamento | Tabelas modeladas / total | % das linhas |
|---|---|---|
| Financeiro do escritório (Honorários) | 13 / 182 | 60,2% |
| Contábil | 8 / 588 | 41,5% |
| Fiscal | 24 / 2.703 | 11,0% |
| Pessoal | 18 / 778 | 10,4% |
| Geral | 12 / 381 | 2,9% |
| Processos · Societário · Sistema | 0 | 0% |

**Maiores lacunas por volume (candidatas à próxima rodada):** cupom fiscal eletrônico CF-e (`EFCUPOM_FISCAL_ELETRONICO*`, 7–12 milhões de linhas por tabela — é a contabilização de origem 49, 54% de todos os lançamentos), auditoria (`audados`, 31,8 mi), SPED ECF (`CTLANCTO_SPED_ECF_GERAL` 21,7 mi, `CTSPED_*`), saldos de produtos (`efsdopro`, 8,4 mi), bases e memória de cálculo da folha (`focalculosbases` 8,5 mi, `foeventosbases` 6,1 mi), INSS/IRRF/FGTS da folha.

## Mapa visual (2026-10-15)
`exports/modelo_relacional.html` (264 KB, arquivo único, funciona sem internet): visão geral (números, cobertura por departamento, ligação entre módulos), **modelo relacional navegável por módulo** (82 tabelas e 106 relações de chave desenhadas, com PK/FK, "pata de galinha", zoom, arrasto, busca e painel de detalhe por tabela e por entidade), lista das 75 entidades, mapa de pastas/arquivos e inventário de funções extraído do próprio código. Gerado por `src/model/gerar_visual.py` a partir do catálogo, dos YAML e da análise sintática do código (nada digitado à mão); links diretos: `#visao`, `#modelo-fiscal`, `#modelo-contabil`, `#modelo-folha`, `#modelo-honorarios`, `#modelo-geral`, `#entidades`, `#onde`, `#funcoes`. Verificado por renderização em navegador sem interface. O desenho mostra só relações de chave (FK declarada ou JOIN usado nos programas com confiança ≥ 0,9) entre as tabelas das entidades; a empresa (`geempre`) fica de fora das linhas por ligar tudo.

## Fases 4 e 5 — consulta e servidor MCP (concluídas em 2026-10-15)
**Decisões do dono do projeto (2026-10-15):** (1) dados **em claro, sem mascaramento** por ora — papéis e restrições virão em **cópias futuras do servidor**; (2) **manter a senha do EXTERNOII** (o sistema já tem travas contra acesso não autorizado), por isso as credenciais foram gravadas em `config/.env` (fora do controle de versão); (3) o servidor MCP é **novo e independente** do `dominio` existente.

**Entregas:** `src/server/motor.py` (descoberta, consulta por entidade, consulta genérica, relacionamentos, caminho entre tabelas, balancete, contas a receber), `src/server/mcp_server.py` (12 ferramentas), `config/seguranca.yaml`, `executar_servidor.cmd`, `docs/uso-mcp.md`, `tests/` (pytest), `scripts/testar_mcp_stdio.py`, `scripts/testar_mcp_http.py`.

**Ferramentas:** `listar_modulos`, `listar_entidades`, `descrever_entidade`, `dominio`, `buscar_tabelas`, `descrever_tabela`, `relacionamentos`, `caminho_entre`, `consultar_entidade`, `consultar_tabela`, `balancete`, `contas_a_receber`.

**Verificação:** 61 testes pytest (injeção de SQL, recusa de qualquer escrita, filtros obrigatórios, limites, credenciais, consistência dos modelos, integração com o banco real) e 17 verificações ponta a ponta pelo protocolo MCP real (processo separado, stdio) **sem variáveis de ambiente** — as credenciais vêm de `config/.env`; o transporte HTTP também responde. As consultas das 75 entidades levam 2–150 ms; o balancete de uma empresa de 187 mil lançamentos/ano, 1,6 s.

**Somente leitura em três camadas:** (a) o servidor só executa `SELECT`/`WITH`, com valores parametrizados e identificadores validados contra o catálogo; (b) cada consulta roda sem travar registros (`READ UNCOMMITTED`); (c) o usuário do banco não tem permissão de escrita (um teste tenta escrever e é recusado pelo próprio banco).

**Achado de segurança que moldou a camada genérica:** **79 tabelas legíveis guardam credenciais em colunas de texto** (senha do certificado digital, senhas de portais e SMTP, tokens e client secrets de APIs, senha de NFS-e). Mesmo com os dados de negócio em claro, o servidor **omite essas colunas** (e recusa pedi-las ou filtrá-las) e **bloqueia 14 tabelas** que são cofres de credenciais/usuários. Isso é salvaguarda de engenharia, independente da política de mascaramento. A lista fica em `config/seguranca.yaml`.

**Defeitos encontrados pelos próprios testes e corrigidos:** (1) com o SDK MCP 2.x só `ToolError` leva a mensagem ao cliente; as recusas intencionais chegavam como "Error executing tool" sem orientação — agora chegam com o motivo e sugestão ("Você quis dizer: nota_saida…"); (2) o `db.py` afirmava rodar em `READ UNCOMMITTED` mas não configurava; (3) um domínio-fantasma e uma nota ausente no modelo foram pegos pelo teste de consistência dos modelos; (4) o carregador de `.env` dependia do diretório atual.

**Limites desta versão:**
- O transporte HTTP **não tem autenticação**: use só em `127.0.0.1` até existir token/papéis.
- Sem teste de carga/concorrência: cada chamada abre uma conexão ODBC nova (simples e segura, mas não é um pool).
- O timeout de consulta (60 s) depende do driver ODBC respeitar `SQL_ATTR_QUERY_TIMEOUT`; não foi comprovado com uma consulta realmente lenta.
- `consultar_tabela` devolve valores monetários como números decimais de ponto flutuante (adequado para consulta, não para somar milhões de linhas fora do banco).
- O servidor ainda **não foi registrado** no Claude Code (comando em `docs/uso-mcp.md`).
- A suíte de integração depende de dados reais (ex.: empresa 879, 1430, 245, escritório 930): se esses dados mudarem os testes podem precisar de ajuste.

## Decisões
- Ghidra não será usado (PowerBuilder p-code; SQL extraído do texto dos `.pbd`).
- Dicionário via `SYS.*` (o usuário de leitura não lê `DSDBA.*`). A coluna `password` de `SYS.SYSUSER` nunca é lida.
- Stack: Python 3.14 + `pyodbc` + SDK `mcp` + `sqlglot` (instalado, ainda não usado), venv em `.venv`.
- Servidor independente por enquanto (decisão provisória).
- Driver ODBC não aceita `timeout` na conexão (`HYC00`); limite de tempo será tratado na camada de consulta.
- Confiança de relação inferida = precisão medida da regra (0,6), não um número arbitrário.

## Pendências / lembretes
- [x] ~~Senha do EXTERNOII~~ — decisão: **manter** (2026-10-15); gravada em `config/.env`. Revisitar se o servidor sair da máquina local.
- [x] ~~Servidor novo ou estender o `dominio`~~ — decisão: **servidor novo** (feito).
- [x] ~~Política de mascaramento~~ — decisão: **tudo em claro por ora**; papéis/restrições em cópias futuras (base: 67 campos `sensivel` nos modelos).
- [ ] Registrar o servidor no Claude Code (comando em `docs/uso-mcp.md`).
- [ ] Confirmar com a Domínio/licenciamento o uso do acesso ODBC somente leitura para este fim.
- [ ] Antes de expor em rede: autenticação do transporte HTTP, papéis e, então, mascaramento por papel.

## Próximo passo
1. **Registrar o servidor no Claude Code** e usá-lo de verdade: o uso real mostra quais entidades faltam e quais respostas confundem o modelo.
2. **Rodadas de modelagem guiadas pelo uso**: (a) lacunas por volume — CF-e, INSS/IRRF/FGTS da folha, saldos de produtos, SPED, auditoria; (b) módulos menores — Patrimônio `PM`, Lalur `LR`, Registro `RG`, Processos `PC`, Ponto `PO`.
3. **Cópias do servidor por papel** (as restrições futuras): autenticação do HTTP, perfil de acesso e mascaramento dos 67 campos `sensivel`.
4. **Operação (Fase 7):** serviço Windows, rotação de `logs/auditoria.jsonl`, rotina para regenerar o catálogo quando a Domínio atualizar a versão do banco. Cada módulo segue o ciclo de `docs/formato-modelo.md`: YAML → validar → testar → conciliar com um total que a própria Domínio calcula → perfil → documentação. Em paralelo, o `sqlbuilder.py` já é a base da Fase 4 (paginação, filtros, proteção de tabelas grandes).

## Como regenerar
```powershell
$env:DOM_UID='<usuario>'; $env:DOM_PWD='<senha>'
.\.venv\Scripts\python.exe src\extractor\catalogo.py      # tabelas, colunas, FKs   (~4 s)
.\.venv\Scripts\python.exe src\extractor\indices.py       # índices                 (~3 s)
.\.venv\Scripts\python.exe src\extractor\joins_sql.py     # minera JOINs dos .pbd   (~2 min, não usa o banco)
.\.venv\Scripts\python.exe src\model\relacoes.py          # consolida relações
.\.venv\Scripts\python.exe src\model\exportar_grafo.py    # grafo.json + docs/relacionamentos.md
.\.venv\Scripts\python.exe scripts\ver_relacoes.py efsaidas ctcontas   # consulta rápida
```

## Diário
- 2026-10-15 — Análise do `geradrel.exe` com REA; conexão ODBC somente leitura validada; inventário das 4.844 fontes; criação do projeto e do plano.
- 2026-10-15 — Fases 0 e 1: venv, `pyodbc`, `mcp`; catálogo completo gerado e validado.
- 2026-10-15 — Fase 2: mineração de JOINs em 1.154 binários, índices, consolidação e calibração das relações; grafo e relatório exportados.


## Plataforma de progresso (2026-10-15)
- `src/plataforma/` + `executar_plataforma.cmd` (http://127.0.0.1:8800): painel, mosaico por tabela, fila de trabalho, famílias, histórico e gaveta por tabela com geração/validação/teste/promoção de rascunhos de entidade. Guia: `docs/plataforma.md`.
- Estado atual: 4.727 tabelas no escopo; 75 modeladas (1,6%); 64 de 774 tabelas com ≥ 1.000 linhas (8,3%); 17,2% das linhas; 969 de 53.963 colunas úteis expostas.
- Corrigido durante o teste: catálogo SQLite compartilhado entre threads (`check_same_thread=False`) e API serializada por lock (o navegador faz requisições em paralelo).
- Testes: `tests/test_plataforma.py` (12); suíte total 73 passando.
- Limite: "Validada" é derivada de a entidade ter `regras`; promover rascunho exige reiniciar o MCP.