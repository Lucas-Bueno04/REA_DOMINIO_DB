# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gesocios_dependentes (Socios - Cadastro - Dependentes) - módulo geral_socios."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gesocios_dependentes"
MODULO = "geral_socios"
ENTIDADES = ['gesocios_dependentes']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
