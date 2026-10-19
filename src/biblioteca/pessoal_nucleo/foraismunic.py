# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foraismunic (Municipios da RAIS) - módulo pessoal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foraismunic"
MODULO = "pessoal_nucleo"
ENTIDADES = ['foraismunic']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
