# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foencargo_simples_domestico_rescisorio (Tabela do encargo rescisório do simples doméstico.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foencargo_simples_domestico_rescisorio"
MODULO = "pessoal_outros"
ENTIDADES = ['foencargo_simples_domestico_rescisorio']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
