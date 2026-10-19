# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrpagamento (Pagamentos de contas a pagar) - módulo financeiro_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrpagamento"
MODULO = "financeiro_nucleo"
ENTIDADES = ['hrpagamento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
