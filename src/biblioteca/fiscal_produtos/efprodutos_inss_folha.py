# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efprodutos_inss_folha (Produtos - Cadastro - INSS folha) - módulo fiscal_produtos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efprodutos_inss_folha"
MODULO = "fiscal_produtos"
ENTIDADES = ['efprodutos_inss_folha']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
