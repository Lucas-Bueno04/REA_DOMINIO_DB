# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsdopro (Saldo mensal dos produtos (estoque fiscal)) - módulo estoque."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsdopro"
MODULO = "estoque"
ENTIDADES = ['saldo_produto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
