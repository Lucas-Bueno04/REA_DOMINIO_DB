# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_simp_serie (Tabela de Série - SIMP) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_simp_serie"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_simp_serie']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
