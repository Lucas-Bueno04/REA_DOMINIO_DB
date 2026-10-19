# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabaju (Outros Movimentos - Impostos Lancados - Detalhamento de Ajustes - RS) - módulo fiscal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabaju"
MODULO = "fiscal_nucleo"
ENTIDADES = ['eftabaju']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
