# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela aucolunasexclusao (Colunas gravadas na exclusao) - módulo sistema_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "aucolunasexclusao"
MODULO = "sistema_nucleo"
ENTIDADES = ['aucolunasexclusao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
