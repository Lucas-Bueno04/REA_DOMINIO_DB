# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrparametro_saldo_inicial_base_negativa (Parâmetros Lalur - Saldo inicial Base Negativa CSLL) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrparametro_saldo_inicial_base_negativa"
MODULO = "contabil_outros"
ENTIDADES = ['lrparametro_saldo_inicial_base_negativa']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
