# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gemodulos (Lista dos módulos do sistema) - módulo geral_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gemodulos"
MODULO = "geral_nucleo"
ENTIDADES = ['gemodulos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
