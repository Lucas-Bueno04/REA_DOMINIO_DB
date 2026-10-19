# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctdocumentos_ole (Documentos OLEs) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctdocumentos_ole"
MODULO = "contabil_outros"
ENTIDADES = ['ctdocumentos_ole']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
