# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fomovtoserv_simulacao (Movimentação do cálculo de simulação de rescisão/férias) - módulo pessoal_movtoserv."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fomovtoserv_simulacao"
MODULO = "pessoal_movtoserv"
ENTIDADES = ['fomovtoserv_simulacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
