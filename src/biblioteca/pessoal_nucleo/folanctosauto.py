# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela folanctosauto (Lançamentos automaticos) - módulo pessoal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "folanctosauto"
MODULO = "pessoal_nucleo"
ENTIDADES = ['folanctosauto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
