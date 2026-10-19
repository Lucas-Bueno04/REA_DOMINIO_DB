# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctlista_bancos_banco_central (Bancos) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctlista_bancos_banco_central"
MODULO = "contabil_outros"
ENTIDADES = ['ctlista_bancos_banco_central']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
