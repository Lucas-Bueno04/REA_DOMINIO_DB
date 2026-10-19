# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fobasesserv_simulacao (Bases da simulação de rescisão/férias) - módulo pessoal_basesserv."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fobasesserv_simulacao"
MODULO = "pessoal_basesserv"
ENTIDADES = ['fobasesserv_simulacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
