# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctparmto_cmv_estoque_grupo (Parametros - CMV Contas de estoque - Grupos de produtos) - módulo contabil_parmto."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctparmto_cmv_estoque_grupo"
MODULO = "contabil_parmto"
ENTIDADES = ['ctparmto_cmv_estoque_grupo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
