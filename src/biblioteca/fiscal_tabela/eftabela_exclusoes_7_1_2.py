# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_exclusoes_7_1_2 (Tabela de Exclusões/Deduções 7.1.2) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_exclusoes_7_1_2"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_exclusoes_7_1_2']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
