# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focat_natureza_lesao (Tabela de catálogo das naturezas de lesões do CAT) - módulo pessoal_cat."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focat_natureza_lesao"
MODULO = "pessoal_cat"
ENTIDADES = ['focat_natureza_lesao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
