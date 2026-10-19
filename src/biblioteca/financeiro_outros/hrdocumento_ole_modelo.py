# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrdocumento_ole_modelo (Modelos de documentos OLEs) - módulo financeiro_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrdocumento_ole_modelo"
MODULO = "financeiro_outros"
ENTIDADES = ['hrdocumento_ole_modelo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
