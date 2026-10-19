# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela rgdadosdw (Dados do relatorios) - módulo societario_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "rgdadosdw"
MODULO = "societario_nucleo"
ENTIDADES = ['rgdadosdw']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
