# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctcontas_idiomas (Contas Contabeis Outros Idiomas) - módulo contabil_contas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctcontas_idiomas"
MODULO = "contabil_contas"
ENTIDADES = ['ctcontas_idiomas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
