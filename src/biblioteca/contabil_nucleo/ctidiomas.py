# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctidiomas (Idiomas) - módulo contabil_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctidiomas"
MODULO = "contabil_nucleo"
ENTIDADES = ['ctidiomas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
