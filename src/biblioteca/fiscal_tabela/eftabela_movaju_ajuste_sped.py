# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_movaju_ajuste_sped (Tabela de ajustes sped para lançamentos de ajustes) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_movaju_ajuste_sped"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_movaju_ajuste_sped']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
