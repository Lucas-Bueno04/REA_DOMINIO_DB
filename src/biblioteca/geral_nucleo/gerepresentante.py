# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gerepresentante (Tabela de Representantes) - módulo geral_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gerepresentante"
MODULO = "geral_nucleo"
ENTIDADES = ['gerepresentante']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
