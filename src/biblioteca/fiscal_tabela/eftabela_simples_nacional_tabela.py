# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_simples_nacional_tabela (Simples Nacional - Tabelas) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_simples_nacional_tabela"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_simples_nacional_tabela']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
