# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geindice_diario (Índice diário) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geindice_diario"
MODULO = "geral_outros"
ENTIDADES = ['geindice_diario']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
