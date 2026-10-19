# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pmbem_historico (Bens - Históricos) - módulo contabil_bem."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pmbem_historico"
MODULO = "contabil_bem"
ENTIDADES = ['pmbem_historico']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
