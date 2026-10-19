# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efentradaspag_lancto (Baixas de entradas X Lancamentos contabeis) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efentradaspag_lancto"
MODULO = "fiscal_outros"
ENTIDADES = ['efentradaspag_lancto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
