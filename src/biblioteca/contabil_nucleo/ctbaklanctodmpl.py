# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctbaklanctodmpl (Lancamento DMPL eliminados) - módulo contabil_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctbaklanctodmpl"
MODULO = "contabil_nucleo"
ENTIDADES = ['ctbaklanctodmpl']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
