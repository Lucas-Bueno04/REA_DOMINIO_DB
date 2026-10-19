# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrlancamento_receber_competencia (Lancamentos de contas a receber - Mensais e Fixos - Competencias para faturamento futuro) - módulo financeiro_lancamento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrlancamento_receber_competencia"
MODULO = "financeiro_lancamento"
ENTIDADES = ['hrlancamento_receber_competencia']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
