# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela rgdocumentos_ole_modelos (Modelos de Documento) - módulo societario_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "rgdocumentos_ole_modelos"
MODULO = "societario_outros"
ENTIDADES = ['rgdocumentos_ole_modelos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
