# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrrenegociacao (Renegociacoes) - módulo financeiro_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrrenegociacao"
MODULO = "financeiro_nucleo"
ENTIDADES = ['hrrenegociacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
