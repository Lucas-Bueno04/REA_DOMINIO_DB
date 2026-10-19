# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efposse_produtos_competencia (Posse dos Produtos) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efposse_produtos_competencia"
MODULO = "fiscal_outros"
ENTIDADES = ['efposse_produtos_competencia']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
