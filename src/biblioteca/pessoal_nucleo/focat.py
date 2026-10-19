# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focat (Comunicação de Acidente do trabalho - CAT) - módulo pessoal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focat"
MODULO = "pessoal_nucleo"
ENTIDADES = ['focat']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
