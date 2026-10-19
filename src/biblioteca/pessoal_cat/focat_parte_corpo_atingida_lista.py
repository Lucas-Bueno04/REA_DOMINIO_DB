# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focat_parte_corpo_atingida_lista (Lista de partes do corpo atingida da CAT.) - módulo pessoal_cat."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focat_parte_corpo_atingida_lista"
MODULO = "pessoal_cat"
ENTIDADES = ['focat_parte_corpo_atingida_lista']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
