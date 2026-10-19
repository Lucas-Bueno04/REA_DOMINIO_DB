# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pmbem_documentos_fiscais (Tabela de cadastro referente a documento Notas Fiscais / Conhecimento) - módulo contabil_bem."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pmbem_documentos_fiscais"
MODULO = "contabil_bem"
ENTIDADES = ['pmbem_documentos_fiscais']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
