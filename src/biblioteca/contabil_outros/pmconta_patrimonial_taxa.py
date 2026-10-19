# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pmconta_patrimonial_taxa (Contas Patrimoniais - Taxas variáveis de depreciação) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pmconta_patrimonial_taxa"
MODULO = "contabil_outros"
ENTIDADES = ['pmconta_patrimonial_taxa']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
