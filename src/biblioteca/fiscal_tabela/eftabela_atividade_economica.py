# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_atividade_economica (Tabela de Atividade Econômica) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_atividade_economica"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_atividade_economica']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
