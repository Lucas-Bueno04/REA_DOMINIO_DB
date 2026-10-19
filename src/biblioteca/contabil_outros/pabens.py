# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pabens (Bens - Cadastro) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pabens"
MODULO = "contabil_outros"
ENTIDADES = ['pabens']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
