# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pmconta_patrimonial (Contas Patrimoniais) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pmconta_patrimonial"
MODULO = "contabil_outros"
ENTIDADES = ['pmconta_patrimonial']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
