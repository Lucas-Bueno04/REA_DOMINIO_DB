# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctcontas_grupos_dlpa (Grupos DLPA que fazem parte da conta) - módulo contabil_contas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctcontas_grupos_dlpa"
MODULO = "contabil_contas"
ENTIDADES = ['ctcontas_grupos_dlpa']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
