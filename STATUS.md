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

## Fase 3 — módulo CF-e (2026-10-18)
**Entregas:** `src/model/modulos/cfe.yaml` (6 entidades), `docs/modelo-cfe.md`, `scripts/sondar_cfe.py`. Validado (0 erros, 0 avisos), executado no banco real (6 de 6, sem multiplicar linhas) e suíte `pytest` com 73 testes passando. Só leitura, como no restante do projeto.

| Entidade | Tabela | Linhas |
|---|---|---|
| cupom_fiscal_eletronico | `efcupom_fiscal_eletronico` | 7.235.124 |
| item_cupom_fiscal_eletronico | `efcupom_fiscal_eletronico_estoque` | 12.416.469 |
| imposto_cupom_fiscal_eletronico | `..._impostos` | 7.623.014 |
| detalhe_imposto_cupom_fiscal_eletronico | `..._impostos_detalhamento` | 7.744.304 |
| pis_cofins_cupom_fiscal_eletronico | `..._pis_cofins` | 1.363.671 |
| lancamento_cupom_fiscal_eletronico | `..._lancto` (+ `_estoque_total` como vínculo) | 7.399.590 |

**Conciliação (empresa 1017, 554.404 CF-e):** valor do cabeçalho = `estoque_total` em 100%; `estoque_total` = soma dos itens e soma dos impostos = cabeçalho em 552.621 de 552.621; 0 itens órfãos; 0 chaves repetidas.
**Descobertas:** `situacao` 2 = cancelado (99,9% com extrato/chave de cancelamento e valor 0), 0 = normal; 1 e 4 não ocorrem (`confirmado: parcial`). `origem_reg` = 7 em 99,99% das linhas e **não consta no comentário** do banco (só 0 a 3). `tipo_titulo` é sempre 99 e `conferido` sempre N. Só 40 empresas usam CF-e (2017-07 a 2026-01).
**Fora de propósito:** `*_ESTOQUE_APURACAO_ESTOQUE` (12,4 mi, cálculo interno), saldo/monofásico/ICMS-ST, parcelas/pagamentos (376 linhas), tabelas vazias e `EFSAT_CF_E`.
**Pendente:** a apuração lê `EFTMP_CUPOM_FISCAL_ELETRONICO_PERIODO` (temporária); o critério de situação que a Domínio usa para escolher os CF-e do período ainda não foi extraído dos `.pbd`.
**Próximas da fila (por volume):** `efsdopro`/`efsdopro_diario` (8,7 mi), `GEGUIA_CONTRIBUICAO_PREVIDENCIARIA*` (4 mi; colunas já em `docs/colunas/`), INSS/IRRF/FGTS da folha, SPED ECF, auditoria.

## Fase 3 — módulo Contabilidade referencial (2026-10-18)
**Entregas:** `src/model/modulos/referencial.yaml` (10 entidades), `docs/modelo-referencial.md`, `scripts/sondar_ct_referencial.py`. Validado (0 erros, 0 avisos), executado no banco real (10 de 10, sem multiplicar linhas), 73 testes passando. Só leitura.

| Grupo | Entidades (tabela) | Linhas |
|---|---|---|
| Planos referenciais (globais) | plano_referencial_ecf (`ctcontas_sped_ecf_geral`), plano_referencial_srf (`ctcontas_srf`), plano_referencial_ecf_imune_isenta | 1.133 · 809 · 515 |
| Mapeamento conta → referencial | conta_referencial_ecf / _srf / _ecf_imune_isenta (`ctcontas_*_ref`) | 922 mil · 635 mil · 17,5 mil |
| Lançamentos referenciais | lancamento_referencial_ecf (`ctlancto_sped_ecf_geral`), _srf (`ctlancto_referencial_srf`), _ecf_imune_isenta | 21,7 mi · 1,15 mi · 470 mil |
| SCP | lancamento_scp (`ctlancto_scp`) | 2.742 |

**Descobertas:** cada linha referencial é **uma perna** (débito *ou* crédito, a outra conta vale 0), então somar `valor` direto dá o dobro do lançamento. A conta referencial é a que o mapeamento `ctcontas_*_ref` associa à conta do livro (100% das pernas de débito, empresas 1017 e 596). Conciliação ECF (empresa 1017, 580.266 lançamentos): soma das pernas de débito = `vlor_lan` em 579.198; todo lançamento tem linha referencial; 0 órfãos. No SRF só existe perna para conta com mapeamento (52.961 de 54.974 lançamentos da empresa 596). `origem_reg` é sempre 0 nas tabelas referenciais. No plano ECF a utilização 3 (só Presumido) está no comentário mas não ocorre nos dados.
**Fora de propósito:** 24 tabelas `CTLANCTO_*` vazias (COSIF, FCONT, BC, ANS, etc.), planos de setores regulados, `CTCONTAS_*_REF_SA_SCP`, `CTSPED_*` (próxima rodada).

## Fase 3 — módulo SPED ECF, Outros Dados (2026-10-18)
**Entregas:** `src/model/modulos/sped_ecf.yaml` (11 entidades), `docs/modelo-sped_ecf.md`, `scripts/sondar_sped_ecf.py`. Validado (0 erros, 0 avisos), executado no banco real (11 de 11), 73 testes passando. Só leitura.

| Grupo | Entidades (tabela) | Linhas |
|---|---|---|
| Parâmetros | ecf_outros_dados (`ctsped_ecf_od`) | 2.533 |
| Valores | valor_registro_ecf (`..._registro`), conta_registro_ecf, valor_mes_registro_ecf | 8,58 mi · 4.866 · 32.556 |
| Layout | layout_registro_ecf (`cttabela_sped_ecf_od_registro`) | 10.776 |
| Lalur | valor_lalur_ecf (`..._registro_lalur`), conta_lalur_ecf, lancamento_lalur_ecf, base_negativa_parte_b_ecf | 4,08 mi · 1.825 · 14.978 · 194 |
| Signatários | signatario_ecf, qualificacao_signatario | 1.051 · 21 |

**Descobertas:** há 1 registro por (empresa, ano-calendário, SCP) em 613 empresas, anos 2017-2025; lucro presumido trimestral é 83% (2.112 de 2.533). 99% de `valor_registro_ecf` vale 0 (o sistema grava todas as linhas do layout). **Erro evitado:** o `codigo` do Lalur *não* é o do layout da ECF (só 3,9% casa, por coincidência numérica); os programas ligam-no às tabelas `LRTABELA_GRUPO_*` (módulo Lalur, ainda não modelado). O vínculo com o layout foi retirado de `valor_lalur_ecf`. Tipo de saldo vazio ('') existe e não consta no comentário do banco. O cadastro tem 110 campos e a entidade expõe 56.
**Fora de propósito:** registros específicos da ECF (Y570, Y600, Y612, Y620, Y671, Y672, Y720, Y800, W100, L200, M010, M410, X360, X430, X450, X480; 6 a 18 mil linhas), SPED Contábil (`CTSPED_CONTABIL_OD*`), e-mail/telefone de signatário.
**Próximo:** módulo Lalur (`LR*`, 129 tabelas, para ligar o `codigo`), registros específicos da ECF e SPED Contábil.

## Mapeamento em lote — Fiscal (2026-10-18)
**Decisão do dono do projeto:** mapear 100% do banco útil, departamento por departamento, até não restar tabela "não iniciada". O controle do que foi feito é o **status derivado da plataforma** (por tabela) + este arquivo; não existe outro controle.

**Processo (scripts novos, todos só leitura no banco):**
1. `scripts/mapear_lote.py --dep <Departamento>`: pega as tabelas "não iniciadas", gera uma entidade por tabela com o gerador da plataforma (colunas sem binário/credencial/"SEM USO", domínios dos comentários, vínculos pelas FKs declaradas, filtros), agrupa por família em `src/model/modulos/<dep>_<familia>.yaml` (famílias de até 3 tabelas vão para `<dep>_outros.yaml`), valida no catálogo e **executa cada entidade no banco real** (SELECT de 200 linhas e fan-out dos vínculos). Relatório em `data/lotes/<dep>.json`.
2. `scripts/medir_fatos.py --todos-gerados`: mede, no banco, volume/período/empresas, colunas nulas em 100%, domínios (valores reais x comentário; só vira `confirmado: true` com ao menos um valor real e nenhum fora do comentário) e linhas sem pai em cada vínculo; grava como `regras` (com a data da medição).
3. `scripts/marcar_sensiveis.py`: marca `sensivel: parcial` (CPF/CNPJ, inscrição, e-mail, telefone, endereço) e remove colunas de texto de certificado digital.
4. `gerar_docs_modelo.py <modulo>` e `dump_colunas.py` para a documentação.

**Resultado do Fiscal:** 876 tabelas "não iniciadas" → **875 entidades em 33 módulos** (`fiscal_*.yaml`); 0 erros de validação; 875 de 875 executam no banco real; 0 multiplicam linhas; 191 domínios confirmados contra os dados e 18 parciais; 111 colunas marcadas como sensíveis. Modelo total: 980 entidades. Cobertura: 989 tabelas e 66,4% das linhas do banco (175,7 mi de 264,6 mi).
**A tabela removida do banco:** `EFSDOIMP_PIS_COFINS_REDUCAO_LINEAR_FILIAL_APROVEITAMENTO_CREDITO` (7.166 linhas no catálogo de 15/10) não existe mais; marcada como "ignorada". É a única diferença entre o catálogo e o banco hoje (5.140 x 5.139 tabelas).

**O que "validada" significa para as entidades em lote — leia antes de confiar:** a plataforma deriva "validada" de a entidade ter `regras`. Nas 875 entidades geradas, as regras são **fatos estruturais medidos** (volume, período, colunas nulas, domínios, órfãos de vínculo), **não** conciliações de regra de negócio com um total que a Domínio calcula (como as 54 entidades curadas à mão). Os nomes de API vêm dos comentários do banco (alguns truncados), as descrições são automáticas e as chaves de 6 tabelas sem PK nem índice único são o conjunto de colunas expostas. Próximo nível de validação (manual) para as de maior valor: `efsdopro`, `efoutrosdados_dados`, `efacumulador_vigencia*`, `efsdoimp_*`.
**Não foi feito:** as 1.789 tabelas fiscais vazias; leitura do conteúdo de colunas de XML/binário (excluídas); regras de negócio (só as curadas).

### Lote Pessoal (2026-10-18)
464 tabelas "não iniciadas" → **464 entidades em 29 módulos** (`pessoal_*.yaml`); 0 erros de validação; 464 de 464 executam no banco real; 0 multiplicam linhas; 270 colunas marcadas como sensíveis (`pessoal` para nascimento, CID, deficiência, documentos e filiação; `financeiro` para salário e remuneração; CPF/CNPJ, e-mail, telefone e endereço como `parcial`). Descoberta do processo: 8 tabelas grandes (≥ 100 mil linhas) ficaram sem filtro obrigatório que liderasse um índice; o novo `scripts/proteger_acesso.py` cria esses filtros e os torna `exige_algum` (agora faz parte de `scripts/fechar_lote.py`, que encadeia medir fatos → sensíveis → proteger acesso → validar → documentar). Mesmas ressalvas do Fiscal sobre o que "validada" significa.

### Lote dos demais departamentos (2026-10-18)
| Departamento | Tabelas | Módulos | Observação |
|---|---|---|---|
| Contábil | 278 | 14 (`contabil_*`) | 20 colunas sensíveis |
| Geral | 257 | 21 (`geral_*`) | 52 colunas sensíveis; 2 entidades protegidas por `proteger_acesso` |
| Financeiro do escritório | 76 | 7 (`financeiro_*`) | |
| Processos | 26 | 4 (`processos_*`) | |
| Societário | 19 | 2 (`societario_*`) | |
| Sistema | 14 | 2 (`sistema_*`) | auditoria: `audados` (31,8 mi) expõe só metadados; o `conteudo` das linhas auditadas é `long varchar` e foi excluído de propósito |
| Outros | 3 | 1 (`outros_outros`) | |

**Situação da plataforma ao fim do dia:** 0 tabelas "não iniciadas" em qualquer departamento; 2.134 tabelas modeladas (2.066 "validadas" pelo critério mecânico, 50 modeladas à mão sem regras, 18 de apoio); **99,99% das linhas do banco cobertas** (264,57 mi de 264,59 mi); 773 de 773 tabelas com ≥ 1.000 linhas; 2.117 entidades; 21.631 colunas expostas de 53.963 úteis; 1.324 domínios, dos quais 1.247 confirmados. 0 erros de validação; só os 2 avisos antigos e 26 "tabela sem PK" (esperados e documentados no teste). Ficam fora: as 2.580 tabelas vazias, as 12 bloqueadas (credenciais) e 1 removida do banco.
**Ressalva que continua valendo:** em lote, "validada" = fatos estruturais medidos, não conciliação de regra de negócio. A próxima fase é **curar à mão as entidades de maior valor** (nomes, descrições, regras conciliadas com totais que a Domínio calcula) e transformar o modelo em funções de consulta nomeadas (futuras ferramentas MCP).

## Curadoria das tabelas de maior valor (2026-10-18, em andamento)
Depois do mapeamento em lote, cada tabela de alto valor é **curada à mão** (nomes legíveis, descrição, regras conciliadas com um total que a Domínio calcula) em módulo manual; `scripts/curar_entidade.py <tabela>` tira a entidade do módulo gerado. Entregues:

| Módulo | Entidades | Conciliação feita (só leitura) |
|---|---|---|
| `estoque` | `saldo_produto` (8,45 mi), `saldo_produto_diario` | saldo = anterior + entradas − saídas (valor 100%, físico 100% a menos de 0,001); continuidade entre meses 62.130/62.130; entradas = `efmvepro`; **saídas = notas de saída + CF-e vigentes (100% a menos de 0,001; só com notas seriam 90,2%)**; diário fecha com o mensal 82.962/82.962 (`scripts/sondar_saldo_produtos.py`) |
| `simples` | `apuracao_simples_nacional`, `aliquota_simples_nacional`, `receita_bruta_anterior_simples` | total = soma dos detalhes em 18.355/18.355 grupos (**nunca some todas as linhas**: dobra); imposto = IRPJ+CSLL+COFINS+PIS+INSS+IPI+ICMS+ISS em 13.403/13.403; **receita bruta recalculada pelos documentos fecha ao centavo em 38 de 40 empresa/competências sorteadas** (`scripts/conciliar_receita_simples.py`); 2 exceções registradas (1110/2025-10: serviços 87.948,65 acima da base — hipótese de regime de caixa NÃO confirmada; 1649/2026-03: 198,27 no grupo de ST) |

| `parametro_fiscal` | `parametro_fiscal`, `parametro_fiscal_imposto`, `acumulador_vigencia`, `acumulador_vigencia_imposto` | vigência em vigor = a mais recente até a data (a mesma regra dos acumuladores, validada na receita do Simples); regimes deduzidos dos dados (ver abaixo); 0 órfãos de vigência/acumulador |

| `esocial` | `evento_esocial` (913 mil), `catalogo_evento_esocial` (44), `lote_esocial` (210 mil), `ocorrencia_evento_esocial` (82 mil) | 99,99% dos eventos têm recibo+validação+resposta; **resposta 202 = sucesso com advertência** (10.730 de 10.730 com ocorrência; 201 nunca tem: 262.934); evento = número S-xxxx (1299 = fechamento); catálogo cobre 100%; lote do registro tem o mesmo evento em 100% (78.357); ID de envio único |

| `guias` | `guia_imposto` (408 mil), `pagamento_imposto` (35 mil) | `valor_pago` da apuração fecha com a soma dos pagamentos em 98,2% (2.044/2.082, 2023-2024); `saldo_recolher = saldo_devedor` em 99,9%; **o registro de pagamentos parou em 2023** (guias com saldo e valor pago: 1.525 em 2023, 17 em 2024, 6 em 2025, 0 em 2026; `efpagimp` termina em 2025-04) |
| `parametros_empresa` | `parametro_contabil` (1.441), `parametro_folha` (1.356) | plano de contas de 87 empresas vem de OUTRA empresa; 971 bloqueiam lançamento fora do período de trabalho; `mes_encerrado` da folha está desatualizado (≤ 2026-03): usar o S-1299 |

| `informativos` | `informativo` (82), `informativo_empresa` (83 mil), `dado_informativo` (3,84 mi) | todo campo tem cabeçalho (0 órfãos em 3,8 mi); 9 competências com ano impossível (20, 2240, 3202, 5025); informativo 35 (SPED PIS/COFINS) tem 2,9 mi de campos |
| `lalur` | `calculo_lalur` (2.884), `apuracao_irpj_real` e `apuracao_csll_real` (3.108 cada), `lucro_antes_irpj_csll` (2.813) | **todas as identidades fecham**: lucro real e base 3.108/3.108; IRPJ = 15% (278/278); CSLL = 9% (277/278, 1 em 9,03%); adicional = 10% × (LR − 20.000 × m), m inteiro de 1 a 12 em 167/167; a recolher com piso zero 278/278 (IRPJ e CSLL); deduções do IRPJ 3.108/3.108, da CSLL 3.103/3.108 |
| `parametro_fiscal` (EFPARAMETRO) | `parametro_fiscal_geral` (1.434) | `PFEC_PAR` (fechamento fiscal) está antes do período atual em 1.433 das 1.434 empresas |

| `das_api` | `envio_das_api` (13.320), `mensagem_envio_das_api` (18.777), `bilhetagem_das_api` (13.320) | **situação do envio coincide 1 para 1 com o código HTTP da mensagem** (0 aguardando, 1 sucesso/200, 2 recusado/400-403, 3 erro/500, 4 não autorizado/401); número do DAS (17 posições) só em emissões; **a partir da 2ª transmissão com sucesso todas são retificadoras (1.334/1.334)**; só há dados de 2024-04 em diante |

| `folha_historico` | `alteracao_salarial` (27.825), `alteracao_contratual` (33.339), `lancamento_evento_folha` (226 mil), `situacao_mensal_empregado` (429 mil) | aumento percentual fecha 3.727/3.731, adição de valor 107/107, continuidade do salário anterior 8.915/8.955; **`foafastamentos_competencia` é a situação MENSAL do empregado: 93% das linhas são "Trabalhando" (código 1)**, afastamentos são a minoria |

| `guias` (regras) | `regra_recolhimento` (315 mil), `codigo_receita_imposto` (38 mil) | código de recolhimento da guia = o da regra em 7.426/7.427; **vencimento: 62,5% no dia configurado, 28,3% antecipado para o dia útil anterior quando cai no fim de semana, 9,2% não explicado (provável feriado)**; a lista de códigos de receita tem só 19 códigos e é usada por 1,4% das regras |
| `produto_fiscal` | `produto_vigencia` (261 mil) | classificação por vigência (PIS/COFINS, ICMS, IPI, ST, monofásico); só 46 vigências monofásicas; dados PIS/COFINS conferidos em 71.071 de 261.175; todas as vigências têm produto no cadastro (0 sem cadastro em 71.973) |

| `parametro_fiscal` (filhos do acumulador) | `acumulador_vigencia_cfop` (768 mil), `acumulador_vigencia_aliquota` (379 mil), `acumulador_vigencia_conta` (453 mil) | 0 órfãos nos três; **o CFOP da nota de saída está na lista do acumulador vigente em 13.071 de 13.088 notas (99,9%)** |
| `icms` | `apuracao_icms_st_uf` (706 mil), `ajuste_apuracao` (50 mil) | **saldo devedor − credor = débitos − créditos em 706.590/706.590**; só 1.076 linhas têm saldo (a tabela guarda as 27 UFs de cada apuração); legenda de `oper_aju` deduzida dos nomes padrão (1 outros créditos … 7 outros recolhimentos, 43 ativo permanente) |

| `folha_calculo` | `cadastro_base_calculo_folha` (270), `calculo_base_folha` (8,4 mi), `incidencia_evento_folha` (6,1 mi) | **base do INSS mensal = soma dos proventos que incidem na base 9** em 582 de 688 cálculos (84,6%), 36 limitados ao teto de R$ 8.475,55 e 70 (10%) não explicados; sem órfãos (0 base sem cadastro em 3,66 mi); as fórmulas do sistema (`frm_script`) ficam fora |
| `folha_contabil` | `configuracao_integracao_folha` (112.913), `evento_integracao_folha` (831.213), `lancamento_integracao_folha` (213.590) | todo lançamento da integração existe em `ctlancto` (0 sem lançamento nos 38.065 de 2025); a **legenda de `tipo` (1–8, 10) não está no banco** e não fechou com os totais da folha (empresa 1430, 2026-08): domínio mantido sem legenda (`confirmado: false`) |

**Descobertas de dados:** o saldo de produtos inclui CF-e; a receita do Simples é definida pelo acumulador (`IREC_ACU`/`IDEV_ACU`), com a vigência mais recente até a data do documento (as notas não guardam a vigência); a empresa 715 tem 12 linhas de receita anterior com ano 2170-2171 (erro de digitação); em `EFSDOIMP_SIMPLES_NACIONAL_ALIQUOTAS` o total é a soma das partes só no anexo 1 (17.045/17.045), nunca no anexo 2 (0/17.045).

**Funções de consulta nomeadas** (`src/server/consultas.py`, com catálogo `FUNCOES` pronto para virar ferramentas MCP; `tests/test_consultas.py`, contra o banco real): `receita_bruta_simples(empresa, competencia)` recalcula a receita e compara com a base apurada (`confere` / `diverge` / `sem_apuracao`); `perfil_fiscal(empresa, data)` devolve regimes em vigor, impostos ativos e **evidências** (apurações dos últimos 12 meses) porque a legenda do regime federal não está no banco.
`situacao_esocial(empresa, competencia)` informa se a folha está **fechada no eSocial** (vale o último S-1298/S-1299 da competência: o padrão real é fechar, reabrir e fechar de novo), quantos S-1200/S-1210 foram aceitos/rejeitados/com advertência e as pendências sem recibo.
`guias_do_mes(empresa, competencia)` lista as guias com situação (paga / parcial / vencida ou a vencer **sem pagamento registrado**) e avisa que o registro de pagamentos é incompleto de 2024 em diante; `apuracao_lalur(empresa, competencia)` refaz o cálculo do IRPJ/CSLL do lucro real passo a passo e confere com o gravado (**2.884 de 2.884 competências conferem**); `situacao_das(empresa, competencia)` resume apuração, declaração PGDAS-D, guia DAS e erros da API (4.477 competências com envio: 2.676 declaradas com DAS emitido; entre as **com movimento**, só 37 declaradas sem DAS e 191 sem declaração transmitida são casos de atenção; as sem movimento não têm guia a emitir); `situacao_reinf(empresa, competencia)` (fechamento R-2099/R-2098, eventos aceitos/rejeitados; 300 competências sorteadas sem erro); `receita_bruta_mensal(empresa, de, ate)` (série de até 36 meses, mesma regra validada do Simples, serve a presumido e real); `resumo_folha(empresa, competencia)` (totais por tipo de folha; líquido gravado = proventos − descontos em 254/254 cálculos); `classificacao_produto(empresa, produto, data)` (enquadramento fiscal vigente de um produto); `historico_salarial(empresa, empregado)` (linha do tempo salarial com checagem de continuidade); `informativos_da_empresa(empresa, de, ate)` lista as obrigações acessórias preparadas, com recibo e retificadora; `perfil_empresa(empresa)` é a porta de entrada (cadastro, regimes e impostos, parâmetros contábeis e de folha, último fechamento do eSocial; 40 de 40 empresas sorteadas sem erro). `memoria_calculo_folha(empresa, empregado, competencia, tipo_folha)` mostra cada base do cálculo (INSS, FGTS, IRRF, férias...) com base, taxa e valor; `valor = base × taxa/100` em 86,6% das bases com taxa (empresa 354, 2026), as demais são progressivas ou com dedução. **Correções do lote feitas depois:** 15 colunas GUID que são PK/FK voltaram às entidades (`scripts/incluir_chaves_guid.py`), 31 colunas que são código do próprio sistema (scripts/fórmulas compiladas de 1.000+ caracteres: `foformulas`, `focadbases`, `poprocedim`...) foram retiradas (`scripts/limpar_colunas_script.py`), e o painel passou a separar **"validada"** (curada e conciliada, 59+ tabelas) de **"medida"** (gerada em lote, 2.000+).
**Legenda do regime federal (`efparametro_vigencia.rfed_par`), deduzida dos dados:** 5 = lucro presumido (733 empresas; 447 apuram IRPJ), 4 = Simples Nacional (466; 166 apuram Simples em 2025), 2 = variante do Simples (29; 10 apuram Simples, 103 de 114 vigências com regime estadual 13), 1 = provável lucro real (170); 6, 8 e 9 não determinados. O regime estadual 13 (não consta no comentário) é o do Simples. O regime de recolhimento é sempre R (não distingue presumido de real).
**Descoberta de entidades:** com 2.117 entidades, o MCP ganhou `buscar_entidades(termo)` (sem acento, todas as palavras, curadas primeiro) e `listar_entidades` paginado (13 ferramentas; `docs/uso-mcp.md`). Verificação de que as 2.117 entidades executam e serializam pelo `Motor` (como o MCP faz): `scripts/testar_motor_entidades.py` — 2.117 de 2.117 (3 corrigidas: `codi_emp` nulo em 100% nas notificações de atendimento).

### Qualidade e desempenho (2026-10-18)
- `docs/funcoes.md` (gerado por `scripts/gerar_docs_funcoes.py`) especifica as 15 funções de `src/server/consultas.py`, prontas para virar ferramentas MCP; `visao_mensal(empresa, competencia)` junta receita, guias, folha e o estado de eSocial, Reinf e DAS com alertas (40 de 40 empresas ativas sorteadas sem erro).
- `tests/test_todas_entidades.py` roda **todas as 2.117 entidades** pelo `Motor` no banco real (≈ 1 min): 0 falhas. Suíte: 117 testes.
- Carregamento do modelo com o `CSafeLoader` do PyYAML (libyaml): `Motor()` de 7,3 s para 1,05 s; validação do modelo 1,3 s; suíte de 207 s para 114 s.

## Biblioteca de tools MCP (2026-10-18)
Pedido: transformar **todas** as tabelas mapeadas (inclusive as geradas em lote) numa biblioteca de ferramentas MCP, uma pasta por módulo e um arquivo por tabela, com descrição para o modelo de IA, validação e casos de uso. Arquitetura, perfis e processo em `docs/biblioteca.md`; catálogo em `docs/biblioteca/` (`scripts/gerar_docs_biblioteca.py`).
- **Biblioteca** `src/biblioteca/`: 137 pastas de módulo, 1 arquivo por tabela (gerado por `scripts/gerar_biblioteca.py`), mais `casos_de_uso/` com as 15 funções nomeadas como tools. Por tabela: `*_consultar` (filtros, ordenação, paginação), `*_obter` (chave) e `*_totais` (contagem/soma por grupo). Servidor: perfil `compacto` (gateway `buscar_ferramentas`/`descrever_ferramenta`/`executar_ferramenta` + casos de uso) ou `completo` (todas; ≈14 MB de schema, por isso o gateway é o padrão).
- **Bateria de validação** (`scripts/validar_biblioteca.py`, contra o banco, só leitura): esquema, descrição, entrada, execução com amostra real, campos, credenciais, filtro, paginação, obter e totais (total geral = contagem da consulta = soma dos grupos). Resultado em `data/biblioteca_estado.db`; a aba **Biblioteca de tools** da plataforma mostra o status por tabela (sem_ferramenta → gerada → validada → curada/revisada → falhou).
- **A bateria achou defeitos reais do motor** (valem para todas as entidades): `CHAR(n)` com brancos misturados (`NCM = '0101'` não achava `'0101    '`; agora testa as variantes com IN, mantendo o índice), filtro chamado `periodo` tratado como período da tabela (4 entidades renomeadas para `periodo_referencia`), texto vazio (`''` × `' '`), 5 nomes de campo com mojibake.
- **Revisão independente por agentes** (9 agentes sem contexto em 3 rodadas, só pela interface do cliente MCP, amostras estratificadas sorteadas com sementes diferentes; ferramentas reprovadas são retestadas na rodada seguinte): aprovação **80% (rodada 1, 133 ferramentas) → 77% (rodada 2, 125) → 90% (rodada 3, 117; IC 95% Wilson 83–94%)**. A regra de decisão fixada (limite inferior do IC ≥ 85%) **não foi atingida** na rodada 3 (83%): por isso só as ferramentas aprovadas individualmente têm veredito `[aprovada]` (status `revisada` quando todas as da tabela foram aprovadas); a biblioteca como um todo NÃO está carimbada como revisada. O que sobra de reprovação é, em sua maior parte, limitação do banco (códigos sem legenda, tabelas de configuração interna, períodos em colunas vazias) que a descrição só pode avisar.
- **Defeitos reais achados pelos revisores e corrigidos:** `resumo_folha` dobrava proventos e descontos (`fobasesserv` grava o cálculo em 2 linhas, `rateio` 0 e 1; agora só `rateio = 0`: líquido calculado = gravado = 67.938,00 na empresa 354/2026-08, com teste de regressão); filtros de texto só com `contem/prefixo` anunciados como "valor simples" (descrição e mensagem de erro corrigidas); descrições que prometiam mascaramento inexistente; `*_totais` sem aviso de soma sem sinal/linha de total, somando alíquotas, códigos, acumulados e datas seriais (lista de campos somáveis agora exige nome de valor/quantidade); `periodo` sem dizer a coluna e sem avisar que linhas com a coluna vazia não aparecem; falsos positivos do alerta de dado pessoal ("PIS" imposto) e ausências (login, IP, máquina). As ferramentas agora trazem empresa-exemplo com dados, comentário da tabela no banco, campos de vínculo, datas sentinela e regras da tabela nos totais.
- **Armadilha de processo:** a sincronização do estado apagava vereditos quando a biblioteca carregava quebrada durante uma edição; agora só apaga com carga íntegra (os vereditos da rodada 1 foram perdidos assim; os números acima vêm dos relatórios dos revisores).
- Mapeadas também as 12 tabelas "apoio" com dados (sem entidade própria), que agora têm ferramentas.

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