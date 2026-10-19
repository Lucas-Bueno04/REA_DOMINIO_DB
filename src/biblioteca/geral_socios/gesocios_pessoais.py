# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gesocios_pessoais (Socios - Cadastro - Referencias Pessoais) - módulo geral_socios."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gesocios_pessoais"
MODULO = "geral_socios"
ENTIDADES = ['gesocios_pessoais']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
