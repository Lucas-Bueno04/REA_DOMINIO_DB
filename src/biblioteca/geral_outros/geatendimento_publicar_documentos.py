# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimento_publicar_documentos (Relação de documentos publicados) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimento_publicar_documentos"
MODULO = "geral_outros"
ENTIDADES = ['geatendimento_publicar_documentos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
