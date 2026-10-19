# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geraexecutar (EXECUÇÃO DE ROTINAS AUTOMÁTICAS) - módulo geral_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geraexecutar"
MODULO = "geral_nucleo"
ENTIDADES = ['geraexecutar']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
