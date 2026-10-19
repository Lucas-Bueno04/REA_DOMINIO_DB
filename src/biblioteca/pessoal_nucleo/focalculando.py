# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focalculando (Controle de concorrencia) - módulo pessoal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focalculando"
MODULO = "pessoal_nucleo"
ENTIDADES = ['focalculando']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
