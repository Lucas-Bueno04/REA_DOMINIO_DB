# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctbalancosocial (Balanco Social - Estrutura) - módulo contabil_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctbalancosocial"
MODULO = "contabil_nucleo"
ENTIDADES = ['ctbalancosocial']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
