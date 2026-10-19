# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efinformativos (Catálogo de informativos (obrigações acessórias)) - módulo informativos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efinformativos"
MODULO = "informativos"
ENTIDADES = ['informativo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
