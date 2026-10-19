# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela rgdocumentos_documentacao (Documentos - Documentacao) - módulo societario_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "rgdocumentos_documentacao"
MODULO = "societario_outros"
ENTIDADES = ['rgdocumentos_documentacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
