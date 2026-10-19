# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geimportador_equivalencias_valores (Valores das tabelas equivalentes) - módulo geral_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geimportador_equivalencias_valores"
MODULO = "geral_importador"
ENTIDADES = ['geimportador_equivalencias_valores']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
