# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foestabilidade_tipos (Tipos de estabilidade.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foestabilidade_tipos"
MODULO = "pessoal_outros"
ENTIDADES = ['foestabilidade_tipos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
