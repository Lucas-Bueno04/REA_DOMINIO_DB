# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmvspro_is (Nota Fiscais de Saidas - Produtos - IS (Imposto Seletivo)) - módulo fiscal_mvspro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmvspro_is"
MODULO = "fiscal_mvspro"
ENTIDADES = ['efmvspro_is']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
