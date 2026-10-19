# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_grupo_st_estoque_rs (Tabela dos grupos da substituição tributário do estoque - RS) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_grupo_st_estoque_rs"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_grupo_st_estoque_rs']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
