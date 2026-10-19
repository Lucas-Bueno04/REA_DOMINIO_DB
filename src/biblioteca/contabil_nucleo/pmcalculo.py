# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pmcalculo (Cálculo patrimonial) - módulo contabil_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pmcalculo"
MODULO = "contabil_nucleo"
ENTIDADES = ['pmcalculo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
