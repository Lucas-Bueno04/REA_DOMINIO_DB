# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrlancamento_receber (Lancamentos de contas a receber - Mensais e Fixos) - módulo financeiro_lancamento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrlancamento_receber"
MODULO = "financeiro_lancamento"
ENTIDADES = ['hrlancamento_receber']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
