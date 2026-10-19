# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctlanctopadrao_contas (Lancamentos Padroes em Lote - Contas) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctlanctopadrao_contas"
MODULO = "contabil_outros"
ENTIDADES = ['ctlanctopadrao_contas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
