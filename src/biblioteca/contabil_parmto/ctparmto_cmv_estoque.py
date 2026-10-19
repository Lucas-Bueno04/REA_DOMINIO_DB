# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctparmto_cmv_estoque (Parametros - CMV Contas de estoque) - módulo contabil_parmto."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctparmto_cmv_estoque"
MODULO = "contabil_parmto"
ENTIDADES = ['ctparmto_cmv_estoque']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
