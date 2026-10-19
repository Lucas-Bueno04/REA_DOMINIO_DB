# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela auvalores (Valores das colunas valoradas) - módulo sistema_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "auvalores"
MODULO = "sistema_nucleo"
ENTIDADES = ['auvalores']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
