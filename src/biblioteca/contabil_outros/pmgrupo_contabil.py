# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pmgrupo_contabil (Grupos Contábeis) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pmgrupo_contabil"
MODULO = "contabil_outros"
ENTIDADES = ['pmgrupo_contabil']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
