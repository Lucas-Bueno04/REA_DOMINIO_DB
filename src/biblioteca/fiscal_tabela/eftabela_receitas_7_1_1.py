# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_receitas_7_1_1 (Tabela de Receitas 7.1.1) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_receitas_7_1_1"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_receitas_7_1_1']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
