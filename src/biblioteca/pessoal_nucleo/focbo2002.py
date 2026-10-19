# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focbo2002 (CBO 2002) - módulo pessoal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focbo2002"
MODULO = "pessoal_nucleo"
ENTIDADES = ['focbo2002']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
