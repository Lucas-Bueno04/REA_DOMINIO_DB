# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela rgcondicoes (Relacao de Condicoes dos Socios) - módulo societario_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "rgcondicoes"
MODULO = "societario_nucleo"
ENTIDADES = ['rgcondicoes']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
