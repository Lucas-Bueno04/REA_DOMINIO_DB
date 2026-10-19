# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pmbem_taxa_alternativa (Bens - Taxa Alternativa) - módulo contabil_bem."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pmbem_taxa_alternativa"
MODULO = "contabil_bem"
ENTIDADES = ['pmbem_taxa_alternativa']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
