# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrconversao (Conversão do Lalur) - módulo contabil_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrconversao"
MODULO = "contabil_nucleo"
ENTIDADES = ['lrconversao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
