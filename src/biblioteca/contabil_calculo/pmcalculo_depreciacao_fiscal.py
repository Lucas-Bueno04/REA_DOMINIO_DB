# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pmcalculo_depreciacao_fiscal (Cálculo patrimonial - Depreciação Fsical) - módulo contabil_calculo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pmcalculo_depreciacao_fiscal"
MODULO = "contabil_calculo"
ENTIDADES = ['pmcalculo_depreciacao_fiscal']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
