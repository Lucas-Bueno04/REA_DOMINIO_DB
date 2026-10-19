# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fomovtoserv_pensao_alimenticia (Valores de pensão alimentícia nas férias por dependente.) - módulo pessoal_movtoserv."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fomovtoserv_pensao_alimenticia"
MODULO = "pessoal_movtoserv"
ENTIDADES = ['fomovtoserv_pensao_alimenticia']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
