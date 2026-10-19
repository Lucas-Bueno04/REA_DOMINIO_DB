# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_simp_recipiente_glp (Tabela Recipiente GLP - SIMP) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_simp_recipiente_glp"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_simp_recipiente_glp']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
