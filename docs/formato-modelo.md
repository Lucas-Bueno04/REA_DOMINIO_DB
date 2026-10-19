# Formato do modelo de entidades (`src/model/modulos/*.yaml`)

Cada módulo (fiscal, comum, e os próximos) é um YAML que descreve **entidades de negócio** em cima das tabelas do banco.
O modelo é a fonte única de verdade para: validação (`validar_modelo.py`), documentação (`gerar_docs_modelo.py`),
geração de SQL (`src/server/sqlbuilder.py`) e, na Fase 5, as ferramentas MCP.

```yaml
modulo: fiscal
titulo: Escrita Fiscal
dominios:                     # significado dos códigos (enumerações)
  nome_do_dominio:
    confirmado: true | parcial | false     # false = hipótese; NÃO usar como regra
    nota: texto livre            # por que não é confirmado, evidências
    valores: {codigo: significado}
entidades:
  nome_da_entidade:
    titulo, descricao
    tabela: tabela_no_banco      # owner bethadba
    chave: [colunas]             # identifica uma linha (normalmente = PK)
    acesso:
      empresa: codi_emp | null   # coluna de empresa; obrigatória no filtro. null = tabela global
      periodo: coluna | {vinculo: v, coluna: c}   # onde recortar por datas (pode vir de um vínculo)
      exige_algum: [filtros]     # pelo menos um destes filtros é obrigatório (protege tabelas grandes)
      volume: pequeno | medio | grande
    ordem: [[coluna, asc|desc]]  # a chave desempata automaticamente (paginação estável)
    colunas:                     # nome_api: coluna  |  nome_api: {coluna, dominio, sensivel, nulo_se, nota}
    vinculos:                    # lookups N:1 por LEFT JOIN
      nome: {tabela, liga: {coluna_local: coluna_remota}, colunas: {nome_api: coluna_remota}}
    filtros:                     # nome: {coluna, ops: [eq,in,entre,gte,lte,contem,prefixo]}
    filhos:                      # relações 1:N: nome: {entidade, liga: {coluna_do_pai: nome_api_ou_coluna_do_filho}}
    calculadas: {nome: "col_a - col_b"}          # aritmética (+ - * / parênteses) só com colunas da própria tabela
    coalescidas: {nome: ["vinculo.coluna", "outro.coluna", "'S'"]}   # primeiro valor não nulo; literal opcional entre aspas simples
    privacidade: texto           # aviso exibido na documentação para entidades com dado pessoal
    regras: [texto]              # regras de negócio VALIDADAS contra dados reais (cite a evidência)
```
Nos vínculos, `sensiveis: [nome_api, ...]` marca colunas trazidas do vínculo que identificam pessoas (ex.: nome do empregado).
Em `colunas`, `sensivel: pessoal | financeiro | parcial | sim` marca dado a mascarar por padrão (Fase 4).
Colunas marcadas `sensivel` NUNCA têm mínimo/máximo guardados no perfil (`scripts/verificar_privacidade_perfil.py` confere).

## Regras do formato
1. **Nunca use a chave `on`.** O YAML 1.1 (PyYAML) a lê como o booleano `True`. Use `liga`.
2. Chaves de domínio `S`/`N` funcionam; evite `y`, `n`, `yes`, `no`, `on`, `off` como valores sem aspas.
3. Todo vínculo precisa ligar pela **chave única completa** da tabela remota — senão o JOIN multiplica linhas
   (o validador recusa).
4. `sensivel: parcial` marca colunas que podem conter dado pessoal de pessoa física (CPF, endereço, telefone, e-mail).
   A política de mascaramento será aplicada na camada de consulta (Fase 4).
5. `nulo_se: "1900-01-01"` informa que aquele valor significa "não informado".
6. Uma regra de negócio só entra em `regras` se foi conferida com dados (ex.: conciliação com a apuração da Domínio).

## Ciclo de trabalho
```powershell
.\.venv\Scripts\python.exe src\model\validar_modelo.py fiscal             # catálogo: tabelas, colunas, junções, grafo
$env:DOM_UID='<usuario>'; $env:DOM_PWD='<senha>'
.\.venv\Scripts\python.exe scripts\testar_entidades.py [--empresa N]      # banco real: SQL roda? junção multiplica linhas?
.\.venv\Scripts\python.exe scripts\conciliar_fiscal.py EMPRESA 1 6        # significado: bate com a apuração da Domínio?
.\.venv\Scripts\python.exe src\extractor\perfil_colunas.py fiscal comum   # % de preenchimento das colunas
.\.venv\Scripts\python.exe src\model\gerar_docs_modelo.py fiscal          # docs/modelo-fiscal.md
```

## Ciclo em lote (módulos `<departamento>_<familia>.yaml`)
Para mapear muitas tabelas de uma vez (STATUS.md, "Mapeamento em lote"): `scripts/mapear_lote.py --dep <Departamento>` gera, valida e testa no banco; `scripts/medir_fatos.py --todos-gerados` grava as regras medidas; `scripts/marcar_sensiveis.py` marca dados pessoais. Arquivos com o cabeçalho "Gerado em lote" podem ser regerados pelos scripts; **não edite à mão** um arquivo assim sem tirar o cabeçalho (ou o `medir_fatos.py --refazer` e o `marcar_sensiveis.py` o reescrevem). Para curar uma entidade, copie-a para um módulo manual (ex.: `fiscal.yaml`) e remova-a do arquivo gerado.
