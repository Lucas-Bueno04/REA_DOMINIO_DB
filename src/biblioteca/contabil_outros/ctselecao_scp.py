# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctselecao_scp (Seleção de Sociedade em Conta de Participação - SCP) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctselecao_scp"
MODULO = "contabil_outros"
ENTIDADES = ['ctselecao_scp']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
