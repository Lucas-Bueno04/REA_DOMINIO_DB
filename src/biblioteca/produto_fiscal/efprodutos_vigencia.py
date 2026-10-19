# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efprodutos_vigencia (Classificação fiscal do produto por vigência) - módulo produto_fiscal."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efprodutos_vigencia"
MODULO = "produto_fiscal"
ENTIDADES = ['produto_vigencia']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
