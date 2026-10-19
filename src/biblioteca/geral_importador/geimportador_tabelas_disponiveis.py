# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geimportador_tabelas_disponiveis (Tabelas disponíveis para definição no importador) - módulo geral_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geimportador_tabelas_disponiveis"
MODULO = "geral_importador"
ENTIDADES = ['geimportador_tabelas_disponiveis']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
