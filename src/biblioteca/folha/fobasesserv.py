# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fobasesserv (Bases e totais da folha) - módulo folha."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fobasesserv"
MODULO = "folha"
ENTIDADES = ['base_folha']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
