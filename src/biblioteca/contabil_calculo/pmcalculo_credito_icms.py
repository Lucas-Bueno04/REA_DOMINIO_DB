# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pmcalculo_credito_icms (Cálculo patrimonial - Crédito ICMS) - módulo contabil_calculo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pmcalculo_credito_icms"
MODULO = "contabil_calculo"
ENTIDADES = ['pmcalculo_credito_icms']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
