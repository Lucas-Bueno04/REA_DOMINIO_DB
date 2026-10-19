# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fobasesserv_fofilhos (Dependentes que foram considerados para o cálculo.) - módulo pessoal_basesserv."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fobasesserv_fofilhos"
MODULO = "pessoal_basesserv"
ENTIDADES = ['fobasesserv_fofilhos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
