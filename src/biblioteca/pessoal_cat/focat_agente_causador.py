# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focat_agente_causador (Agente causador da CAT.) - módulo pessoal_cat."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focat_agente_causador"
MODULO = "pessoal_cat"
ENTIDADES = ['focat_agente_causador']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
