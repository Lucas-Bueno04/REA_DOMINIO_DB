# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela atmovimp (Movimentacao dos Impostos em atraso) - módulo fiscal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "atmovimp"
MODULO = "fiscal_nucleo"
ENTIDADES = ['atmovimp']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
