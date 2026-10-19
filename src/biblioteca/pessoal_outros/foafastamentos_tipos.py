# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foafastamentos_tipos (TIPOS DE AFASTAMENTOS) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foafastamentos_tipos"
MODULO = "pessoal_outros"
ENTIDADES = ['foafastamentos_tipos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
