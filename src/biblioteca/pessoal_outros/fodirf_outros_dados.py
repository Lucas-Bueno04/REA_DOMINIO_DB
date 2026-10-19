# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fodirf_outros_dados (DIRF - Outros dados) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fodirf_outros_dados"
MODULO = "pessoal_outros"
ENTIDADES = ['fodirf_outros_dados']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
