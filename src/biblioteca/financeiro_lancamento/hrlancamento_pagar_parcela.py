# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrlancamento_pagar_parcela (Lancamentos de contas a pagar - Parcelas) - módulo financeiro_lancamento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrlancamento_pagar_parcela"
MODULO = "financeiro_lancamento"
ENTIDADES = ['hrlancamento_pagar_parcela']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
