# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hraviso (Avisos do modulo Honorarios) - módulo financeiro_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hraviso"
MODULO = "financeiro_nucleo"
ENTIDADES = ['hraviso']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
