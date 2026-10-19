# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gecmdexecutado (Indica se um comando SQL ja foi executado) - módulo geral_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gecmdexecutado"
MODULO = "geral_nucleo"
ENTIDADES = ['gecmdexecutado']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
