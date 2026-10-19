# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fomovtoserv_planosaude (Movimentação - Cálculo - Plano de saúde) - módulo pessoal_movtoserv."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fomovtoserv_planosaude"
MODULO = "pessoal_movtoserv"
ENTIDADES = ['fomovtoserv_planosaude']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
