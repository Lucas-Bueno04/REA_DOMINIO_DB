# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmvepro_apuracao_estoque (Notas Fiscais de Entrada - Produtos - Apuração de estoque) - módulo fiscal_mvepro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmvepro_apuracao_estoque"
MODULO = "fiscal_mvepro"
ENTIDADES = ['efmvepro_apuracao_estoque']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
