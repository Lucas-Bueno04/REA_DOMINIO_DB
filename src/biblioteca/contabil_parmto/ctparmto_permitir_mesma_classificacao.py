# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctparmto_permitir_mesma_classificacao (Parametros - Contas que poderão ter as contas analíticas cadastradas com a mesma classificação) - módulo contabil_parmto."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctparmto_permitir_mesma_classificacao"
MODULO = "contabil_parmto"
ENTIDADES = ['ctparmto_permitir_mesma_classificacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
