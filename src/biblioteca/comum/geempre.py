# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geempre (Empresa (cadastro)) - módulo comum."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geempre"
MODULO = "comum"
ENTIDADES = ['empresa']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
