# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctgruposdva (ESTRUTURA DO DVA) - módulo contabil_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctgruposdva"
MODULO = "contabil_nucleo"
ENTIDADES = ['ctgruposdva']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
