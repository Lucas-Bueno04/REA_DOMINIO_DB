# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focargos (Cargos) - módulo folha."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focargos"
MODULO = "folha"
ENTIDADES = ['cargo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
