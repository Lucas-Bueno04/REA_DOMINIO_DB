# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geindice_medio (Índice médio) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geindice_medio"
MODULO = "geral_outros"
ENTIDADES = ['geindice_medio']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
