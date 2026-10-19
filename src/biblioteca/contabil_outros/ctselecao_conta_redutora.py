# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctselecao_conta_redutora (Seleção de contas redutoras para o acompanhamento de lançamentos) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctselecao_conta_redutora"
MODULO = "contabil_outros"
ENTIDADES = ['ctselecao_conta_redutora']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
