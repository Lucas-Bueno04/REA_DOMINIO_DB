# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fofgtsfilial (Valor de fgts por filial) - módulo pessoal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fofgtsfilial"
MODULO = "pessoal_nucleo"
ENTIDADES = ['fofgtsfilial']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
