# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela auusuarios (Usuarios selecionados) - módulo sistema_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "auusuarios"
MODULO = "sistema_nucleo"
ENTIDADES = ['auusuarios']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
