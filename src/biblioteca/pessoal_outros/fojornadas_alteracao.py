# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fojornadas_alteracao (Tabela de alteração das jornadas) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fojornadas_alteracao"
MODULO = "pessoal_outros"
ENTIDADES = ['fojornadas_alteracao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
