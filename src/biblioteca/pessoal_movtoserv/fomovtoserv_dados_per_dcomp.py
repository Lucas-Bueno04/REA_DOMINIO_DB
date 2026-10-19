# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fomovtoserv_dados_per_dcomp (Informações do cálculo da fórmula.) - módulo pessoal_movtoserv."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fomovtoserv_dados_per_dcomp"
MODULO = "pessoal_movtoserv"
ENTIDADES = ['fomovtoserv_dados_per_dcomp']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
