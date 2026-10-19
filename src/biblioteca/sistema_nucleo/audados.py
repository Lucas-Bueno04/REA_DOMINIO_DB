# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela audados (Movimentos da auditoria) - módulo sistema_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "audados"
MODULO = "sistema_nucleo"
ENTIDADES = ['audados']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
