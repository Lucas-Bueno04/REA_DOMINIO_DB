# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctcmv_apuracao_estoque (CMV - Apuração do Custo das Mercadorias Vendidas - Estoque) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctcmv_apuracao_estoque"
MODULO = "contabil_outros"
ENTIDADES = ['ctcmv_apuracao_estoque']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
