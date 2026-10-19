# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_finalidade_arquivo (Tabela Finalidade do Arquivo) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_finalidade_arquivo"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_finalidade_arquivo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
