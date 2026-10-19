# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pminformacao_calculo_credito_icms (Informações para Cálculo do Crédito de ICMS) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pminformacao_calculo_credito_icms"
MODULO = "contabil_outros"
ENTIDADES = ['pminformacao_calculo_credito_icms']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
