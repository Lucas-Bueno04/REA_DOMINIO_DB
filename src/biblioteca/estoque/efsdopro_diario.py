# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsdopro_diario (Saldo diário dos produtos (estoque fiscal)) - módulo estoque."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsdopro_diario"
MODULO = "estoque"
ENTIDADES = ['saldo_produto_diario']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
