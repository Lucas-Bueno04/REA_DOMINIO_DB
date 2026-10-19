# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focat_agente_causador_lista (Lista de agentes causador da CAT.) - módulo pessoal_cat."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focat_agente_causador_lista"
MODULO = "pessoal_cat"
ENTIDADES = ['focat_agente_causador_lista']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
