# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gesocios (Sócios (cadastro mínimo)) - módulo geral."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gesocios"
MODULO = "geral"
ENTIDADES = ['socio']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
