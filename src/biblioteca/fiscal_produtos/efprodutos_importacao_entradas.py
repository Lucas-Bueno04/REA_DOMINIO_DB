# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efprodutos_importacao_entradas (Tabela de relacionamento de importação de produtos - Entradas - Fornecedores) - módulo fiscal_produtos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efprodutos_importacao_entradas"
MODULO = "fiscal_produtos"
ENTIDADES = ['efprodutos_importacao_entradas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
