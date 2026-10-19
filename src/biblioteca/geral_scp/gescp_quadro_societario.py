# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gescp_quadro_societario (SCP - Quadro Societário) - módulo geral_scp."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gescp_quadro_societario"
MODULO = "geral_scp"
ENTIDADES = ['gescp_quadro_societario']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
