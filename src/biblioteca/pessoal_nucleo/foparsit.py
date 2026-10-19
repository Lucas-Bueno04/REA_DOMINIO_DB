# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foparsit (Parametros das situacoes) - módulo pessoal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foparsit"
MODULO = "pessoal_nucleo"
ENTIDADES = ['foparsit']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
