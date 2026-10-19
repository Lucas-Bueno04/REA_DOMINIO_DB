# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrparametro_saldo_inicial_parte_b (Parâmetros Lalur - Saldo inicial Parte B) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrparametro_saldo_inicial_parte_b"
MODULO = "contabil_outros"
ENTIDADES = ['lrparametro_saldo_inicial_parte_b']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
