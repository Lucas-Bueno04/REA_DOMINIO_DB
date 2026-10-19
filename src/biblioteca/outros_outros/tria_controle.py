# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela tria_controle (Controle de funcionalidades que utilizam TRIA) - módulo outros_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "tria_controle"
MODULO = "outros_outros"
ENTIDADES = ['tria_controle']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
