# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gerarotinas (CADASTRO DE ROTINAS AUTOMÁTICAS) - módulo geral_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gerarotinas"
MODULO = "geral_nucleo"
ENTIDADES = ['gerarotinas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
