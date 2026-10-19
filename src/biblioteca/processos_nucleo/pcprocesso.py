# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pcprocesso (Processos) - módulo processos_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pcprocesso"
MODULO = "processos_nucleo"
ENTIDADES = ['pcprocesso']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
